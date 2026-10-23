# Runtime acceptance checks

These are expected results, not captured live outputs. Perform checks in order, preferably starting from a fresh solution import so shortcut caches are empty. Record evidence before generating spoke-to-spoke traffic.

## 1. FVRF and eBGP

On each VPN router:

```text
show vrf
show ip interface brief
show bgp ipv4 unicast vrf FVRF-INTERNET summary
show ip route vrf FVRF-INTERNET
show ip route
```

If the image uses the older display syntax, use `show ip bgp vpnv4 vrf FVRF-INTERNET summary`. Ethernet0/0 must belong to FVRF-INTERNET, while Tunnel0 and Loopback0 remain global. Each VPN router has one established eBGP peer and accepts two remote transport /24s. Its own transport subnet is connected in the VRF.

| Router | BGP peer | Expected BGP routes in FVRF |
|---|---|---|
| R11 | 172.16.11.254 / AS 65000 | 172.16.31.0/24, 172.16.41.0/24 |
| R31 | 172.16.31.254 / AS 65000 | 172.16.11.0/24, 172.16.41.0/24 |
| R41 | 172.16.41.254 / AS 65000 | 172.16.11.0/24, 172.16.31.0/24 |

On ISP, `show ip bgp summary` must show three established peers in AS 65111/65131/65141, each advertising one local transport prefix. ISP's own locally originated paths can remain best for these connected networks; neighbor received-prefix counts do not imply selected routes. Inspect advertised routes per peer: exactly the two remote transport /24s, no LANs or tunnel network.

From each VPN router, ping both remote NBMA addresses in the FVRF. Example on R31:

```text
ping vrf FVRF-INTERNET 172.16.11.1 source Ethernet0/0
ping vrf FVRF-INTERNET 172.16.41.1 source Ethernet0/0
```

These tests must pass before troubleshooting IPsec. No static or default routes are needed. The global table must contain no 172.16.x.0/24 transport routes; the FVRF must contain no 10.x LAN or 192.168.100.0/24 overlay routes. A global-table ping to a remote NBMA is expected to fail with this design.

## 2. IKEv2, NHRP, and OSPF

```text
show crypto ikev2 proposal
show crypto ikev2 policy
show crypto ikev2 profile
show crypto ikev2 sa detailed
show crypto ipsec sa
show dmvpn
show ip nhrp
show ip ospf neighbor
show ip ospf interface Tunnel0
show ip route ospf
```

Confirm the policy/profile match FVRF-INTERNET and the SAs show that front-door VRF with a global inside routing context. Sessions should become READY; verify AES-256, SHA-1 integrity/PRF, DH14 and PSK authentication. A Tunnel0 up/up state alone does not establish success.

R11 must learn both spoke NBMA mappings dynamically. Each spoke must have its static hub mapping and an operational protected hub session. OSPF must show point-to-multipoint with FULL/- neighbors (no DR/BDR). R11 has two neighbors; each spoke has one. OSPF's default point-to-multipoint hello/dead timers must agree across routers.

Before shortcut creation, expect these remote LAN routes:

| Router | Destination | OSPF next hop |
|---|---|---|
| R11 | 10.3.3.0/24 | 192.168.100.31 |
| R11 | 10.4.4.0/24 | 192.168.100.41 |
| R31 | 10.1.1.0/24 and 10.4.4.0/24 | 192.168.100.11 |
| R41 | 10.1.1.0/24 and 10.3.3.0/24 | 192.168.100.11 |

LAN routes must be /24s, not /32s. Remote OSPF /32 routes within 192.168.100.0/24 must not be installed. The local interface's `L` host route is normal and must remain. OSPF's LSDB may still contain tunnel host information because an inbound distribute list filters local route installation, not LSAs. The connected 192.168.100.0/24 route remains usable for NHRP.

## 3. Prove the Phase 3 transition

On R31, before pinging R41's LAN, record:

```text
show ip route 10.4.4.1
show ip cef 10.4.4.1 detail
show ip nhrp
show crypto ipsec sa
```

The initial OSPF path goes through R11. Then run:

```text
ping 10.4.4.1 source Loopback0 repeat 50
show ip route 10.4.4.1
show ip cef 10.4.4.1 detail
show ip nhrp
show dmvpn
show crypto ikev2 sa detailed
show crypto ipsec sa
```

Repeat after convergence if initial packets are lost. R11 forwards initial traffic and sends an NHRP redirect. R31 resolves R41 and creates a shortcut; return traffic should establish the reverse shortcut on R41. Depending on IOS release, route output can show an NHRP (`H`) route or a next-hop override (`%`); inspect CEF and NHRP as well as the route table. Do not require OSPF to change its LSDB or originate a new route to create the shortcut.

Prove all of the following:

- Dynamic mapping from R31 to tunnel 192.168.100.41 / NBMA 172.16.41.1, and the reverse on R41.
- CEF/NHRP resolves traffic to the destination LAN directly through the remote spoke, despite the hub-based OSPF topology.
- A direct IKEv2/IPsec session between 172.16.31.1 and 172.16.41.1, using FVRF-INTERNET.
- Increasing encryption and decryption counters on that direct spoke SA during repeated Loopback0-sourced traffic. Hub-only SAs do not meet this criterion.
- OSPF adjacencies remain hub-and-spoke; a direct spoke OSPF adjacency is not required.

Capture on R31–ISP during the repeated test. Filter `ip.addr == 172.16.31.1 && ip.addr == 172.16.41.1`. Expect ESP (protocol 50) between the two spokes; initial IKE traffic uses UDP 500. No NAT is configured. Inner LAN traffic and GRE must not be visible in plaintext on the physical link. Direct means bypassing R11 for VPN forwarding; the physical path still traverses ISP.

To repeat from an empty dynamic state, restart the lab from fresh saved solution configurations. This clears volatile SAs and NHRP caches. Do not expect an already established shortcut to demonstrate the initial hub path again without clearing/restarting state.

## 4. Connectivity, isolation, and dependency

Ping both remote Loopback0 addresses from each site's Loopback0 (six directed tests). All must pass after convergence. Use extended ping to test a 1400-byte IPv4 datagram with DF set. TCP MSS adjustment applies to TCP SYNs, not ICMP.

For a controlled underlay dependency test, on R31 temporarily shut Ethernet0/0. Verify its eBGP adjacency drops and remote transport routes become unavailable; hub/direct VPN connectivity and eventually its OSPF adjacency should fail. Restore `no shutdown`, allow BGP/IKE/NHRP/OSPF to recover, and repeat LAN tests. Do not save the shutdown state.

Finally confirm no BGP/OSPF redistribution, VRF route leaks, overlay BGP routes, or global transport routes. Save all four nodes with `copy running-config startup-config`.

Troubleshoot in order: VRF membership and re-applied IP addresses → eBGP/filter acceptance → VRF-aware NBMA reachability → IKEv2 FVRF selection and credentials → NHRP registration/multicast → OSPF network type/MTU/passivity → redirect/shortcut processing and tunnel /32 filtering → direct ESP counters.
