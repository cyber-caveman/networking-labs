#!/usr/bin/env python3
"""Static checks for this lab only; no claim of Cisco parser/runtime validation."""
from pathlib import Path
import ipaddress as ip
import json
import re
import zipfile
import xml.etree.ElementTree as ET

P = Path(__file__).resolve().parent
checks = 0

def check(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1

def parse(text):
    data = dict(interfaces={}, session={}, policy={}, neighbors={}, prefixes={}, maps={}, networks=set())
    mode = None
    current = None
    for raw in text.splitlines():
        s = raw.strip()
        if not s or s == '!':
            continue
        if s.startswith('interface '):
            mode, current = 'interfaces', s.split()[1]
            data[mode][current] = []
        elif s.startswith('router bgp '):
            mode = 'bgp'
            data['asn'] = int(s.split()[-1])
        elif s.startswith('template peer-'):
            check(mode == 'bgp', 'template must be defined in BGP mode')
            mode = 'session' if 'peer-session' in s else 'policy'
            current = s.split()[-1]
            data[mode][current] = []
        elif s in ('exit-peer-session', 'exit-peer-policy'):
            check(mode == ('session' if s.endswith('session') else 'policy'), 'template exit mismatch')
            mode = 'bgp'
        elif s == 'address-family ipv4 unicast':
            check(mode == 'bgp', 'AF context')
            mode = 'af'
        elif s == 'exit-address-family':
            check(mode == 'af', 'AF exit context')
            mode = 'bgp'
        elif s.startswith('neighbor '):
            _, peer, cmd = s.split(' ', 2)
            check(mode == ('af' if cmd.startswith(('activate', 'inherit peer-policy')) else 'bgp'), 'neighbor mode: '+s)
            data['neighbors'].setdefault(peer, []).append(cmd)
        elif s.startswith('network '):
            check(mode == 'af', 'network mode')
            a = s.split()
            data['networks'].add(ip.ip_network(a[1]+'/'+a[3]))
        elif s.startswith('ip prefix-list '):
            a = s.split()
            data['prefixes'].setdefault(a[2], set()).add(ip.ip_network(a[6]))
            check(a[5] == 'permit' and len(a) == 7, 'exact permit syntax')
            mode = None
        elif s.startswith('route-map ' ) and not raw.startswith(' '):
            a = s.split()
            check(a[2:] == ['permit', '10'], 'route map permit-all clause')
            mode, current = 'maps', a[1]
            data['maps'][current] = []
        elif raw.startswith(' ') and mode in ('interfaces', 'session', 'policy', 'maps'):
            data[mode][current].append(s)
        elif not raw.startswith(' '):
            mode = None
    return data

def effective(data, kind, name, seen=()):
    check(name not in seen and name in data[kind], 'missing/cyclic template '+name)
    local = data[kind][name]
    inherited = [s.split() for s in local if s.startswith('inherit ')]
    if kind == 'session':
        check(len(inherited) <= 1, 'single parent session')
    else:
        inherited.sort(key=lambda a: int(a[3]))
    result = []
    for a in inherited:
        result.extend(effective(data, kind, a[2], seen+(name,)))
    return result+[s for s in local if not s.startswith('inherit ')]

project = json.loads((P/'project.gns3').read_text())
check(project['revision'] == 9 and project['version'] == '2.2.0', 'known-working project format')
nodes = project['topology']['nodes']
check(len(nodes) == 4, 'four routers')
check(len({n['node_id'] for n in nodes}) == 4, 'unique node UUIDs')
check(len({n['properties']['application_id'] for n in nodes}) == 4, 'unique IOU IDs')
configs = {}
byid = {}
for n in nodes:
    name = n['name']
    byid[n['node_id']] = name
    props = n['properties']
    check(n['node_type'] == 'iou' and n['compute_id'] == 'local' and n['console'] is None, 'node defaults')
    check(n['template_id'] == 'b3b10b90-adfb-43f8-b289-b68bcf322ad8', 'template ID')
    check((props['ethernet_adapters'], props['serial_adapters'], props['ram'], props['nvram']) == (4,4,768,512), 'resources')
    check(props['path'] == 'x86_64_crb_linux-adventerprisek9-ms.bin' and props['md5sum'] == '4a2fce8de21d1831fbceffd155e41ae7', 'image')
    start = (P/'startup-configs'/f'{name}.cfg').read_text()
    final = (P/'final-configs'/f'{name}.cfg').read_text()
    check(start == (P/'project-files/iou'/n['node_id']/'startup-config.cfg').read_text(), 'startup copy equality')
    check('router bgp' not in start and 'peer-group' not in final, 'initial state / no peer groups')
    configs[name] = parse(final)
    check(parse(start)['interfaces'] == configs[name]['interfaces'], 'preserved interfaces')
    connected = {ip.ip_interface(s.split()[2]+'/'+s.split()[3]).network for commands in configs[name]['interfaces'].values() for s in commands if s.startswith('ip address ')}
    check(configs[name]['networks'] <= connected, 'exact connected route exists for origination')
    i = int(name[1:])
    expected = {ip.ip_network(f'10.{i}.0.0/24')}
    if i > 1:
        expected |= {ip.ip_network('203.0.113.0/24'), ip.ip_network(f'198.18.{i}.0/24')}
    check(configs[name]['networks'] == expected, 'only intended origins')

used = set()
check(len(project['topology']['links']) == 3, 'three links')
for link in project['topology']['links']:
    ends = []
    for e in link['nodes']:
        key = (e['node_id'],e['adapter_number'],e['port_number'])
        check(key not in used, 'no duplicate physical endpoint')
        used.add(key)
        name = byid[e['node_id']]
        commands = configs[name]['interfaces'][f"Ethernet{e['adapter_number']}/{e['port_number']}"]
        check('no shutdown' in commands, 'link enabled')
        a = next(s.split() for s in commands if s.startswith('ip address '))
        ends.append((name,ip.ip_interface(a[2]+'/'+a[3])))
    (a,ia),(b,ib) = ends
    check(ia.network == ib.network and ia.ip != ib.ip, 'peer subnet matches')
    for local,remote,remote_ip in [(a,b,str(ib.ip)),(b,a,str(ia.ip))]:
        c = configs[local]
        commands = c['neighbors'][remote_ip]
        check(f"remote-as {configs[remote]['asn']}" in commands and 'activate' in commands, 'reciprocal AS and activation')
        session = effective(c,'session',next(s.split()[-1] for s in commands if s.startswith('inherit peer-session')))
        check(set(session) == {'timers 10 30','password EnarsiBGP'}, 'effective authentication/timers')

hub = configs['R1']
check(len(hub['neighbors']) == 3, 'hub peers')
expected_in = {ip.ip_network(f'10.{i}.0.0/24') for i in range(2,5)} | {ip.ip_network('203.0.113.0/24')}
check(hub['prefixes']['EDGE-IN'] == expected_in, 'hub exact inbound allowlist')
candidates = []
for i,lp in [(2,200),(3,150),(4,100)]:
    branch = configs[f'R{i}']
    check(len(branch['neighbors']) == 1, 'branch peer')
    commands = hub['neighbors'][f'172.16.1{i}.2']
    policy = effective(hub,'policy',next(s.split()[-1] for s in commands if s.startswith('inherit peer-policy')))
    check({'prefix-list EDGE-IN in','prefix-list HUB-ONLY out','maximum-prefix 10'} <= set(policy), 'inherited base policy')
    route_map = next(s.split()[1] for s in policy if s.startswith('route-map '))
    check(hub['maps'][route_map] == [f'set local-preference {lp}'], 'effective local preference')
    accepted = branch['networks'] & hub['prefixes']['EDGE-IN']
    check(accepted == {ip.ip_network(f'10.{i}.0.0/24'),ip.ip_network('203.0.113.0/24')}, 'two accepted, test prefix denied')
    branch_policy = effective(branch,'policy','TO-HUB')
    check(set(branch_policy) == {'prefix-list HUB-ONLY in','maximum-prefix 10'}, 'branch policy')
    exported = hub['networks'] & hub['prefixes']['HUB-ONLY'] & branch['prefixes']['HUB-ONLY']
    check(exported == {ip.ip_network('10.1.0.0/24')}, 'hub export and branch return path')
    candidates.append((lp,i))
check([i for lp,i in sorted(candidates,reverse=True)] == [2,3,4], 'modeled failover order')
for drawing in project['topology']['drawings']:
    ET.fromstring(drawing['svg'])
check(not any('START HERE' in d['svg'] or 'worksheet' in d['svg'] for d in project['topology']['drawings']), 'no canvas instructions')
archive = P/'ENARSI BGP Peer Templates IOU.gns3project'
with zipfile.ZipFile(archive) as z:
    check(z.testzip() is None, 'archive CRC')
    expected_files = {str(f.relative_to(P)) for f in P.rglob('*') if f.is_file() and f.suffix != '.gns3project' and '__pycache__' not in f.parts}
    check(set(z.namelist()) == expected_files, 'all deliverables bundled')
    for f in expected_files:
        check(z.read(f) == (P/f).read_bytes(), 'archive matches file '+f)
print(f'PASS: {checks} static assertions; 4 routers, 3 links, 6 reciprocal peer definitions.')
print('PASS: prefix filtering, return paths and local-preference failover model (R2 > R3 > R4).')
print('NOT RUN: GNS3 import/boot, Cisco CLI parser, BGP convergence, authentication and packet forwarding.')
