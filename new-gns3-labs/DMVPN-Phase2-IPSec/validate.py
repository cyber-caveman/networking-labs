#!/usr/bin/env python3
"""Offline lab-specific consistency checks; not an IOS parser or emulator."""
from pathlib import Path
import ipaddress as ip
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parent
p = json.loads((ROOT / 'project.gns3').read_text())
assert p['name'] == 'DMVPN-Phase2-IPSec'
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
assert finals['ISP'] == starts['ISP']
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

with zipfile.ZipFile(ROOT / 'DMVPN-Phase2-IPSec.gns3project') as z:
    assert z.testzip() is None
    expected = {'project.gns3'}
    for name, n in nodes.items():
        f = f"project-files/iou/{n['node_id']}/startup-config.cfg"
        expected.add(f)
        assert z.read(f) == (ROOT / f).read_bytes() == starts[name].encode()
    assert set(z.namelist()) == expected
    assert z.read('project.gns3') == (ROOT / 'project.gns3').read_bytes()

# Underlay model: each default gateway is adjacent; ISP has a connected
# route to each remote NBMA. Overlay networks are disjoint from transport.
transport = [a.network for a in addresses['ISP'].values()]
for name in ('R11', 'R31', 'R41'):
    cfg = finals[name]
    routes = re.findall(r'^ip route (.*)$', cfg, re.M)
    gateway = ip.ip_address(f'172.16.{name[1:]}.254')
    assert routes == [f'0.0.0.0 0.0.0.0 {gateway}']
    assert gateway in addresses[name]['Ethernet0/0'].network
    assert gateway in [a.ip for a in addresses['ISP'].values()]
    for peer in ('R11','R31','R41'):
        assert any(addresses[peer]['Ethernet0/0'].ip in net for net in transport)
    assert not any(addresses[name]['Tunnel0'].network.overlaps(net) for net in transport)
    required = [
        'ip cef', 'crypto ikev2 proposal DMVPN-PROPOSAL',
        ' encryption aes-cbc-256', ' integrity sha1', ' prf sha1', ' group 14',
        'crypto ikev2 policy DMVPN-POLICY', ' proposal DMVPN-PROPOSAL',
        'crypto ikev2 keyring DMVPN-KEYRING', ' peer DMVPN-PEERS',
        '  address 0.0.0.0 0.0.0.0',
        '  pre-shared-key local ENARSI-DMVPN-2026',
        '  pre-shared-key remote ENARSI-DMVPN-2026',
        'crypto ikev2 profile DMVPN-IKE', ' keyring local DMVPN-KEYRING',
        ' match identity remote address 0.0.0.0 0.0.0.0',
        f" identity local address 172.16.{name[1:]}.1",
        ' authentication local pre-share', ' authentication remote pre-share',
        ' lifetime 86400',
        'crypto ipsec transform-set DMVPN-TS esp-aes 256 esp-sha-hmac',
        ' mode transport', 'crypto ipsec profile DMVPN-IPSEC',
        ' set transform-set DMVPN-TS', ' set ikev2-profile DMVPN-IKE',
        ' ip mtu 1400', ' ip tcp adjust-mss 1360',
        ' ip nhrp authentication ENARSI', ' ip nhrp network-id 100',
        ' tunnel source Ethernet0/0', ' tunnel mode gre multipoint',
        ' tunnel key 100', ' tunnel protection ipsec profile DMVPN-IPSEC',
        'router eigrp 100', ' passive-interface default',
        ' no passive-interface Tunnel0', ' no auto-summary']
    assert all(line in cfg.splitlines() for line in required), name
    for forbidden in ['crypto isakmp ', 'crypto keyring ', 'set isakmp-profile ', 'crypto map ', 'tunnel destination',
                      'ip nhrp redirect', 'ip nhrp shortcut', 'redistribute ',
                      'ip summary-address', 'set pfs']:
        assert forbidden not in cfg, (name, forbidden)
    networks = set(re.findall(r'^ network (\S+) (\S+)$', cfg, re.M))
    assert networks == {(str(addresses[name]['Loopback0'].network.network_address),'0.0.0.255'),
                         ('192.168.100.0','0.0.0.255')}
    # This leaves ISP out of EIGRP and keeps the underlay default from
    # competing with the more-specific learned remote LAN routes.
    if name == 'R11':
        assert ' ip nhrp map multicast dynamic\n' in cfg
        assert ' no ip split-horizon eigrp 100\n' in cfg
        assert ' no ip next-hop-self eigrp 100\n' in cfg
        assert not re.search(r'^ ip nhrp map \d', cfg, re.M)
    else:
        assert re.findall(r'^ ip nhrp map (.*)$', cfg, re.M) == [
            '192.168.100.11 172.16.11.1', 'multicast 172.16.11.1']
        assert ' ip nhrp nhs 192.168.100.11\n' in cfg
print('PASS: archive integrity/equality; IOU preferences; unique identities; physical links/subnets;')
print('IP-only startup allowlist; preserved addressing; underlay reachability model;')
print('NHRP/multicast roles; EIGRP origination/passivity/Phase-2 next-hop prerequisites;')
print('matching IKEv2 proposal/policy/keyring/profile/IPsec parameters and tunnel protection on all VPN routers.')
print('Static analysis only. IOS parser, GNS3 import, SAs, NHRP, routes and forwarding require live testing.')
