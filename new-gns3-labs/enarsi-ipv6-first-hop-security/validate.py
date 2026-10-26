#!/usr/bin/env python3
"""Lab-specific static analysis. Not an IOS parser, emulator, or live test."""
from pathlib import Path
import ipaddress as ip
import json
import re
import uuid
import zipfile
import xml.etree.ElementTree as ET
from package import members, ARCHIVE
P = Path(__file__).resolve().parent
checks = 0

def check(ok, message):
    global checks
    if not ok:
        raise AssertionError(message)
    checks += 1

def blocks(text):
    result = {}
    current = None
    for line in text.splitlines():
        if not line or line == '!':
            continue
        if not line.startswith(' '):
            current = line
            check(current not in result, 'duplicate global block: ' + current)
            result[current] = []
        else:
            check(current is not None, 'orphan subcommand')
            result[current].append(line.strip())
    return result

def addresses(config):
    return {key: tuple(v for v in values if v.startswith('ipv6 address '))
            for key, values in config.items() if key.startswith('interface ')}

def iface(config, name):
    return config['interface '+name]

def attachment(config, port, kind):
    prefix = kind + ' attach-policy '
    matches = [x[len(prefix):] for x in iface(config, port) if x.startswith(prefix)]
    check(len(matches) <= 1, f'multiple {kind} on {port}')
    return matches[0] if matches else None

def policy(config, port, kind):
    name = attachment(config, port, kind)
    return config[kind+' policy '+name] if name else None

def acl_permits(config, name, source):
    # These lab ACLs intentionally contain one explicit source permit each.
    entries = config['ipv6 access-list '+name]
    return any(x == f'permit ipv6 host {source.upper()} any' for x in entries)

def ra_permits(config, port, source, prefixes):
    rules = policy(config, port, 'ipv6 nd raguard')
    if rules is None: return True
    if 'trusted-port' in rules: return True
    if 'device-role host' in rules: return False
    for rule in rules:
        if rule.startswith('match ipv6 access-list '):
            if not acl_permits(config, rule.split()[-1], source): return False
        if rule.startswith('match ra prefix-list '):
            name = rule.split()[-1]
            allowed = {ip.ip_network(x.split()[-1]) for x in config if x.startswith('ipv6 prefix-list '+name+' ')}
            if not all(ip.ip_network(p) in allowed for p in prefixes): return False
    return True

def dhcp_server_permits(config, port, source):
    rules = policy(config, port, 'ipv6 dhcp guard')
    if rules is None or 'trusted-port' in rules: return True
    if 'device-role client' in rules: return False
    for rule in rules:
        if rule.startswith('match server access-list ') and not acl_permits(config, rule.split()[-1], source): return False
    return True

def source_permits(config, port, source, bindings, prefixes=()):
    rules = policy(config, port, 'ipv6 source-guard')
    if rules is None or 'trusted' in rules: return True
    addr = ip.ip_address(source)
    if addr.is_link_local and 'permit link-local' in rules: return True
    if 'no validate address' in rules and 'validate prefix' in rules:
        return any(addr in ip.ip_network(p) for p in prefixes)
    return (port, addr) in bindings

project = json.loads((P/'project.gns3').read_text())
check((project['revision'],project['version'],project['type']) == (9,'2.2.0','topology'), 'compatible format')
check(not project['auto_start'], 'manual startup')
nodes = project['topology']['nodes']
check({n['name'] for n in nodes} == {'SW1','R1','R2','H1','ROGUE'}, 'device set')
check(len({n['node_id'] for n in nodes}) == 5, 'unique node IDs')
check(len({n['properties']['application_id'] for n in nodes}) == 5, 'unique application IDs')
byid = {n['node_id']: n['name'] for n in nodes}
startup = {}
for n in nodes:
    uuid.UUID(n['node_id'])
    prop = n['properties']; switch = n['name']=='SW1'
    check(n['node_type']=='iou' and n['compute_id']=='local', 'node/compute')
    check(n['console'] is None and n['console_type']=='telnet' and not n['console_auto_start'], 'console')
    check(n['custom_adapters']==[] and n['first_port_name'] is None, 'adapter conventions')
    check(n['port_name_format']=='Ethernet{segment0}/{port0}' and n['port_segment_size']==4, 'port format')
    check((prop['ethernet_adapters'],prop['serial_adapters'],prop['ram'],prop['nvram']) == ((4,0,256,512) if switch else (4,4,768,512)), 'resources')
    check(not prop['l1_keepalives'] and prop['use_default_iou_values'] and prop['usage']=='', 'shared properties')
    expected=('i86bi-linux-l2-adventerprisek9-15.2d.bin','f16db44433beb3e8c828db5ddad1de8a','87fd8b26-489a-424e-a7de-1e590da4ccc6') if switch else ('x86_64_crb_linux-adventerprisek9-ms.bin','4a2fce8de21d1831fbceffd155e41ae7','b3b10b90-adfb-43f8-b289-b68bcf322ad8')
    check((prop['path'],prop['md5sum'],n['template_id']) == expected,'image/template')
    expected_visual = (':/symbols/classic/multilayer_switch.svg',51,48) if switch else (':/symbols/classic/router.svg',66,45)
    check((n['symbol'],n['width'],n['height']) == expected_visual, 'node visual')
    raw=(P/'startup-configs'/f"{n['name']}.cfg").read_bytes()
    check(raw == (P/'project-files/iou'/n['node_id']/'startup-config.cfg').read_bytes(),'startup packaging')
    startup[n['name']] = blocks(raw.decode())
used=set(); actual=set()
for link in project['topology']['links']:
    ends=[]
    for ep in link['nodes']:
        key=(byid[ep['node_id']],ep['adapter_number'],ep['port_number'])
        check(key not in used, 'port used twice');used.add(key)
        check(key[1]==0 and 0<=key[2]<4,'endpoint bounds')
        check('no shutdown' in iface(startup[key[0]],f'Ethernet0/{key[2]}'),'link enabled')
        ends.append((key[0],key[2]))
    actual.add(frozenset(ends))
expected=[(('SW1',0),('R1',0)),(('SW1',1),('H1',0)),(('SW1',2),('ROGUE',0)),(('R1',1),('R2',0))]
check(actual == {frozenset(x) for x in expected},'topology endpoints')
for drawing in project['topology']['drawings']: ET.fromstring(drawing['svg'])
for port in range(3):
    check('switchport access vlan 10' in iface(startup['SW1'],f'Ethernet0/{port}'),'access VLAN')
for n in ['R1','H1','ROGUE']:
    addr=[x.split()[2] for x in iface(startup[n],'Ethernet0/0') if x.startswith('ipv6 address ') and 'link-local' not in x][0]
    check(ip.ip_interface(addr).network==ip.ip_network('2001:db8:10::/64'),'LAN network')
check('ipv6 route 2001:DB8:10::/64 2001:DB8:20::1' in startup['R2'],'external return path')
for n in ['H1','ROGUE']: check('ipv6 route ::/0 2001:DB8:10::1' in startup[n],'endpoint route')
check('ipv6 route 2001:DB8:99::/64 2001:DB8:10::66' in startup['R1'],'negative-source return path')
check(not any(' policy ' in k or any('attach-policy' in x for x in v) for k,v in startup['SW1'].items()), 'unsolved switch')
profiles={}
for directory in sorted((P/'solutions').iterdir()):
    configs={p.stem:blocks(p.read_text()) for p in directory.glob('*.cfg')}
    check(set(configs)==set(startup),'complete checkpoint')
    profiles[directory.name]=configs
    for name,cfg in configs.items():
        for ifname,addrs in addresses(startup[name]).items():
            check(addresses(cfg).get(ifname)==addrs,'preserved addressing: '+directory.name+'/'+name+'/'+ifname)
        check(all(k in cfg for k in startup[name] if k.startswith('ipv6 route ')),'preserved return paths')
        for key,values in cfg.items():
            if key.startswith('interface '):
                for val in values:
                    if ' attach-policy ' in val:
                        kind,pol=val.split(' attach-policy ')
                        check(kind+' policy '+pol in cfg,'defined attached policy')
                        check('trusted' not in cfg[kind+' policy '+pol] and 'trusted-port' not in cfg[kind+' policy '+pol],'no trust bypass')
            for val in values:
                if val.startswith(('match ipv6 access-list ','match server access-list ')):
                    check('ipv6 access-list '+val.split()[-1] in cfg,'defined ACL')
                if val.startswith('match ra prefix-list '):
                    check(any(x.startswith('ipv6 prefix-list '+val.split()[-1]+' ') for x in cfg),'defined prefix list')
        check('ipv6 dhcp pool BAD' not in cfg,'rogue service cleaned up')
        check(not any('ipv6 address dhcp' in v for v in cfg.values()),'temporary client removed')

# Functional reasoning over declared policies, with explicitly assumed valid bindings.
# This cannot establish runtime learning, packet classification or hardware behavior.
bindings={(p,ip.ip_address(a)) for p,a in [('Ethernet0/1','2001:db8:10::11'),('Ethernet0/2','2001:db8:10::66')]}
lan=['2001:db8:10::/64']
s1=profiles['01-snooping']['SW1']
check(ra_permits(s1,'Ethernet0/2','fe80::66',lan),'observation-stage RA control')
s2=profiles['02-ra-guard']['SW1']
check(ra_permits(s2,'Ethernet0/0','fe80::1',lan),'legitimate RA')
check(not ra_permits(s2,'Ethernet0/2','fe80::66',lan),'rogue RA')
check(not ra_permits(s2,'Ethernet0/0','fe80::66',lan),'wrong sender on router port')
check(not ra_permits(s2,'Ethernet0/0','fe80::1',['2001:db8:99::/64']),'wrong RA prefix')
s3=profiles['03-dhcpv6-guard']['SW1']
check(dhcp_server_permits(s3,'Ethernet0/0','fe80::1'),'authorized DHCP server')
check(not dhcp_server_permits(s3,'Ethernet0/2','fe80::66'),'rogue DHCP server')
check(not dhcp_server_permits(s3,'Ethernet0/0','fe80::66'),'wrong DHCP sender')
check(source_permits(s3,'Ethernet0/2','2001:db8:99::66',bindings),'unprotected negative-source control')
s4=profiles['04-source-guard']['SW1']
check(source_permits(s4,'Ethernet0/1','2001:db8:10::11',bindings),'valid H1 source')
check(source_permits(s4,'Ethernet0/2','2001:db8:10::66',bindings),'valid ROGUE LAN source')
check(not source_permits(s4,'Ethernet0/2','2001:db8:99::66',bindings),'unbound source rejected')
check(not source_permits(s4,'Ethernet0/2','2001:db8:10::11',bindings),'wrong-port binding rejected in address model')
check(source_permits(s4,'Ethernet0/0','2001:db8:20::2',bindings),'routed external source preserved')
r1=profiles['05-destination-guard']['R1']
check(policy(r1,'Ethernet0/0','ipv6 destination-guard')==['enforcement always'],'continuous destination guard')
check('security-level glean' in policy(r1,'Ethernet0/0','ipv6 snooping'),'local learning')
check(not any('destination-glean' in line for v in r1.values() for line in v),'no destination recovery')
for n in startup:
    check((P/'final-configs'/f'{n}.cfg').read_bytes()==(P/'solutions/05-destination-guard'/f'{n}.cfg').read_bytes(),'final checkpoint equality')
p6=profiles['06-prefix-guard'];s6=p6['SW1'];prefixes=['2001:db8:10::/64','2001:db8:30::/64']
check('prefix-glean' in policy(s6,'Ethernet0/2','ipv6 snooping'),'prefix learning enabled')
check(ra_permits(s6,'Ethernet0/2','fe80::66',prefixes),'authorized branch RA')
check(not ra_permits(s6,'Ethernet0/2','fe80::66',['2001:db8:99::/64']),'branch cannot advertise test-invalid prefix')
check(source_permits(s6,'Ethernet0/2','2001:db8:30::66',bindings,prefixes),'prefix source without host binding')
check(not source_permits(s6,'Ethernet0/2','2001:db8:99::66',bindings,prefixes),'outside-prefix source rejected')
check(attachment(s6,'Ethernet0/1','ipv6 source-guard')=='SG-HOST','H1 remains address guarded')
check('ipv6 route 2001:DB8:30::/64 2001:DB8:10::66' in p6['R1'],'branch return route')
check('ipv6 nd ra lifetime 0' in iface(p6['ROGUE'],'Ethernet0/0'),'no branch default-router advertisement')
check('ipv6 nd prefix 2001:DB8:30::/64' in iface(p6['ROGUE'],'Ethernet0/0'),'branch prefix advertisement')
check('ipv6 address 2001:DB8:30::66/128' in iface(p6['ROGUE'],'Loopback30'),'positive source')
with zipfile.ZipFile(ARCHIVE) as archive:
    check(archive.testzip() is None,'zip CRC integrity')
    expected={p.relative_to(P).as_posix():p for p in members()}
    check(set(archive.namelist())==set(expected),'exact archive member set')
    check(len(archive.namelist())==len(expected),'no duplicate archive entries')
    for name,path in expected.items():check(archive.read(name)==path.read_bytes(),'archive byte equality: '+name)
print(f'PASS: {checks} static checks (including declared-policy reasoning and archive equality).')
print('NOT RUN: Cisco parser, GNS3 import, dynamic learning, or live packet enforcement.')
