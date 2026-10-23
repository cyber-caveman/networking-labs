#!/usr/bin/env python3
"""Offline lab-specific consistency checks; not an IOS parser or emulator."""
from pathlib import Path
import ipaddress as ip
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parent
p = json.loads((ROOT / 'project.gns3').read_text())
assert p['name'] == 'DMVPN-Phase3-IPSec'
nodes = {n['name']: n for n in p['topology']['nodes']}
assert set(nodes) == {'R11', 'R31', 'R41', 'ISP'}
assert len({n['node_id'] for n in nodes.values()}) == 4
assert len({n['properties']['application_id'] for n in nodes.values()}) == 4
assert p['revision'] == 9 and p['version'] == '2.2.0'
for n in nodes.values():
    assert n['node_type'] == 'iou' and n['compute_id'] == 'local'
    assert n['console'] is None and not n['console_auto_start']
    assert n['template_id'] == 'b3b10b90-adfb-43f8-b289-b68bcf322ad8'
    for k, v in {'ethernet_adapters': 4, 'serial_adapters': 4, 'ram': 768,
                 'nvram': 512, 'path': 'x86_64_crb_linux-adventerprisek9-ms.bin',
                 'md5sum': '4a2fce8de21d1831fbceffd155e41ae7'}.items():
        assert n['properties'][k] == v, (n['name'], k)

starts = {name: (ROOT / 'startup-configs' / f'{name}.cfg').read_text() for name in nodes}
finals = {name: (ROOT / 'final-configs' / f'{name}.cfg').read_text() for name in nodes}
def interfaces(text):
    out = {}
    for name, body in re.findall(r'^interface (\S+)\n(.*?)(?=^\S|\Z)', text, re.M | re.S):
        addr, mask = re.search(r'^ ip address (\S+) (\S+)$', body, re.M).groups()
        out[name] = ip.IPv4Interface(f'{addr}/{mask}')
        assert ' no shutdown\n' in body
    return out

addresses = {name: interfaces(cfg) for name, cfg in starts.items()}
for name, cfg in starts.items():
    assert all(re.fullmatch(r'(?:!|end|interface \S+| ip address [\d.]+ [\d.]+| no shutdown)', line)
               for line in cfg.splitlines()), name
    assert addresses[name] == interfaces(finals[name]), name
assert len(addresses['ISP']) == 3
for name, lan in [('R11','10.1.1.1'), ('R31','10.3.3.1'), ('R41','10.4.4.1')]:
    s = name[1:]
    assert addresses[name] == {'Ethernet0/0': ip.ip_interface(f'172.16.{s}.1/24'),
                               'Loopback0': ip.ip_interface(f'{lan}/24'),
                               'Tunnel0': ip.ip_interface(f'192.168.100.{s}/24')}

byid = {n['node_id']: name for name, n in nodes.items()}
seen = set()
assert len(p['topology']['links']) == 3
for link in p['topology']['links']:
    ends = []
    for ep in link['nodes']:
        key = (ep['node_id'], ep['adapter_number'], ep['port_number'])
        assert key not in seen
        seen.add(key)
        name = byid[ep['node_id']]
        iface = f"Ethernet{ep['adapter_number']}/{ep['port_number']}"
        ends.append((name, addresses[name][iface]))
    assert len(ends) == 2 and 'ISP' in {n for n, _ in ends}
    assert ends[0][1].network == ends[1][1].network
    assert ends[0][1].ip != ends[1][1].ip

with zipfile.ZipFile(ROOT / 'DMVPN-Phase3-IPSec.gns3project') as z:
    assert z.testzip() is None
    expected = {'project.gns3'}
    for name, n in nodes.items():
        f = f"project-files/iou/{n['node_id']}/startup-config.cfg"
        expected.add(f)
        assert z.read(f) == (ROOT / f).read_bytes() == starts[name].encode()
    assert set(z.namelist()) == expected
    assert z.read('project.gns3') == (ROOT / 'project.gns3').read_bytes()

# Parse individual config sections so required commands must be in the right scope.
def block(cfg, header):
    match = re.search(r'^' + re.escape(header) + r'\n(.*?)(?=^\S|\Z)', cfg, re.M | re.S)
    assert match, header
    return match.group(1)

def require(body, *lines):
    for line in lines:
        assert line in body.splitlines(), line

def permits(cfg, name, prefix):
    candidate = ip.ip_network(prefix)
    for action, net, ge, le in re.findall(
            r'^ip prefix-list ' + re.escape(name) +
            r' seq \d+ (permit|deny) (\S+?)(?: ge (\d+))?(?: le (\d+))?$', cfg, re.M):
        network = ip.ip_network(net)
        low = int(ge) if ge else network.prefixlen
        high = int(le) if le else (32 if ge else network.prefixlen)
        if candidate.subnet_of(network) and low <= candidate.prefixlen <= high:
            return action == 'permit'
    return False

sites = (11, 31, 41)
transport = {s: f'172.16.{s}.0/24' for s in sites}
isp = finals['ISP']
isp_bgp = block(isp, 'router bgp 65000')
require(isp_bgp, ' no bgp default ipv4-unicast', ' address-family ipv4')
assert 'router ospf' not in isp and 'crypto ' not in isp and 'vrf ' not in isp
for name, cfg in finals.items():
    for prohibited in ['router eigrp', 'crypto isakmp', 'set isakmp-profile',
                       'ip route ', 'redistribute ', 'route-target', 'tunnel destination']:
        assert prohibited not in cfg, (name, prohibited)

for s in sites:
    name = f'R{s}'; cfg = finals[name]
    require(block(cfg, 'vrf definition FVRF-INTERNET'),
            f' rd 651{s}:100', ' address-family ipv4')
    wan = block(cfg, 'interface Ethernet0/0')
    require(wan, ' vrf forwarding FVRF-INTERNET')
    assert wan.index('vrf forwarding') < wan.index('ip address')
    loop = block(cfg, 'interface Loopback0')
    tunnel = block(cfg, 'interface Tunnel0')
    assert 'vrf forwarding' not in loop + tunnel
    require(loop, ' ip ospf network point-to-point', ' ip ospf 100 area 0')
    require(tunnel, ' ip ospf network point-to-multipoint', ' ip ospf 100 area 0',
            ' no ip redirects', ' ip mtu 1400', ' ip tcp adjust-mss 1360',
            ' ip nhrp authentication ENARSI', ' ip nhrp network-id 100',
            ' tunnel key 100', ' tunnel mode gre multipoint',
            ' tunnel source Ethernet0/0', ' tunnel vrf FVRF-INTERNET',
            ' tunnel protection ipsec profile DMVPN-IPSEC')
    if s == 11:
        require(tunnel, ' ip nhrp redirect', ' ip nhrp map multicast dynamic')
        assert 'ip nhrp nhs' not in tunnel
    else:
        require(tunnel, ' ip nhrp shortcut', ' ip nhrp nhs 192.168.100.11',
                ' ip nhrp map 192.168.100.11 172.16.11.1',
                ' ip nhrp map multicast 172.16.11.1')
        assert len(re.findall(r'^ ip nhrp map ', tunnel, re.M)) == 2
    ospf = block(cfg, 'router ospf 100')
    require(ospf, f" router-id {addresses[name]['Loopback0'].ip}",
            ' passive-interface default', ' no passive-interface Tunnel0',
            ' distribute-list prefix OSPF-RIB in')
    assert cfg.count(' ip ospf 100 area 0') == 2
    # Model local OSPF RIB filtering: reject only overlay /32s, retain all LANs.
    for host in (11, 31, 41):
        assert not permits(cfg, 'OSPF-RIB', f'192.168.100.{host}/32')
    for prefix in ['192.168.100.0/24', '10.1.1.0/24', '10.3.3.0/24', '10.4.4.0/24']:
        assert permits(cfg, 'OSPF-RIB', prefix)
    require(block(cfg, 'crypto ikev2 proposal DMVPN-PROPOSAL'),
            ' encryption aes-cbc-256', ' integrity sha1', ' prf sha1', ' group 14')
    require(block(cfg, 'crypto ikev2 policy DMVPN-POLICY'),
            ' match fvrf FVRF-INTERNET', ' proposal DMVPN-PROPOSAL')
    require(block(cfg, 'crypto ikev2 keyring DMVPN-KEYRING'),
            ' peer DMVPN-PEERS', '  address 0.0.0.0 0.0.0.0',
            '  pre-shared-key local ENARSI-DMVPN-2026',
            '  pre-shared-key remote ENARSI-DMVPN-2026')
    require(block(cfg, 'crypto ikev2 profile DMVPN-IKE'),
            ' match fvrf FVRF-INTERNET',
            ' match identity remote address 0.0.0.0 0.0.0.0',
            f' identity local address 172.16.{s}.1',
            ' authentication local pre-share', ' authentication remote pre-share',
            ' keyring local DMVPN-KEYRING', ' lifetime 86400')
    require(block(cfg, 'crypto ipsec transform-set DMVPN-TS esp-aes 256 esp-sha-hmac'),
            ' mode transport')
    require(block(cfg, 'crypto ipsec profile DMVPN-IPSEC'),
            ' set transform-set DMVPN-TS', ' set ikev2-profile DMVPN-IKE')
    bgp = block(cfg, f'router bgp 651{s}')
    require(bgp, ' no bgp default ipv4-unicast',
            ' address-family ipv4 vrf FVRF-INTERNET',
            f'  network 172.16.{s}.0 mask 255.255.255.0',
            f'  neighbor 172.16.{s}.254 remote-as 65000',
            f'  neighbor 172.16.{s}.254 activate',
            f'  neighbor 172.16.{s}.254 prefix-list FROM-ISP in',
            f'  neighbor 172.16.{s}.254 prefix-list TO-ISP out')
    assert len(re.findall(r'^  network ', bgp, re.M)) == 1
    require(isp_bgp, f' neighbor 172.16.{s}.1 remote-as 651{s}',
            f'  network 172.16.{s}.0 mask 255.255.255.0',
            f'  neighbor 172.16.{s}.1 activate',
            f'  neighbor 172.16.{s}.1 prefix-list FROM-R{s} in',
            f'  neighbor 172.16.{s}.1 prefix-list TO-R{s} out')
    # Evaluate both sides of every BGP filter, including leakage probes.
    for t, prefix in transport.items():
        assert permits(cfg, 'TO-ISP', prefix) == (s == t)
        assert permits(isp, f'FROM-R{s}', prefix) == (s == t)
        assert permits(isp, f'TO-R{s}', prefix) == (s != t)
        assert permits(cfg, 'FROM-ISP', prefix) == (s != t)
    for prefix in ['0.0.0.0/0', '10.1.1.0/24', '10.3.3.0/24', '10.4.4.0/24',
                   '192.168.100.0/24', f'172.16.{s}.1/32', '172.16.0.0/16']:
        for c, pl in [(cfg,'TO-ISP'), (cfg,'FROM-ISP'),
                      (isp,f'TO-R{s}'), (isp,f'FROM-R{s}')]:
            assert not permits(c, pl, prefix), (name, pl, prefix)

# Compare identities with the source lab: separate projects can coexist.
source = ROOT.parent / 'DMVPN-Phase2-IPSec' / 'project.gns3'
if source.exists():
    previous = json.loads(source.read_text())
    assert p['project_id'] != previous['project_id']
    assert not set(byid).intersection(n['node_id'] for n in previous['topology']['nodes'])
print('PASS: project/archive integrity, IOU models, unique IDs, links, IP-only startup and addressing.')
print('PASS: scoped FVRF/IKEv2/NHRP/OSPF/BGP config, reciprocal AS/activation, exact filters,')
print('modeled remote NBMA route exchange, LAN and tunnel-host filtering, and protocol separation.')
print('Static checks only; IOS parser acceptance, convergence, shortcuts and ESP require live testing.')
