# DMVPN-Phase3-IPSec

ENARSI practice: implement DMVPN Phase 3 with IKEv2/IPsec, eBGP transport routing, OSPF overlay routing, and a front-door VRF (FVRF). This is original exam-style practice material, not a Cisco exam item. Suggested time: 90–120 minutes.

## Launch and topology

Import **DMVPN-Phase3-IPSec.gns3project** in GNS3 **2.2.56.1**. The project uses four preferred IOU L3 routers: `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, 512 KB NVRAM, four Ethernet and four serial adapters. Supply your installed image and license. Console ports are automatic. Project and node UUIDs are distinct from the Phase 2 lab.

R11 is the hub; R31 and R41 are spokes. ISP implements the transport cloud. Loopback0 represents each site's LAN. The physical layout and addresses match the Phase 2 lab, making protocol and forwarding differences easier to observe.

| Router | AS | Ethernet0/0 | Loopback0 | Tunnel0 |
|---|---|---|---|---|
| R11 | 65111 | 172.16.11.1/24 | 10.1.1.1/24 | 192.168.100.11/24 |
| R31 | 65131 | 172.16.31.1/24 | 10.3.3.1/24 | 192.168.100.31/24 |
| R41 | 65141 | 172.16.41.1/24 | 10.4.4.1/24 | 192.168.100.41/24 |
| ISP | 65000 | 172.16.11.254/24 | — | — |

| Physical link | ISP interface/address |
|---|---|
| R11 Ethernet0/0 ↔ ISP | Ethernet0/0: 172.16.11.254/24 |
| R31 Ethernet0/0 ↔ ISP | Ethernet0/1: 172.16.31.254/24 |
| R41 Ethernet0/0 ↔ ISP | Ethernet0/2: 172.16.41.254/24 |

All startup files contain only interface addressing and `no shutdown`. Interfaces initially belong to the global table; no VRF, routing protocol, NHRP, tunnel source/mode, or IPsec configuration is supplied. Tunnel0 has its assigned address but is not operational. Identify consoles by GNS3 node labels until hostnames are set. ISP is also part of this exercise and requires BGP configuration.

## Candidate instructions

Complete all tasks using the specified names and values. Do not change addressing. Assign hostnames matching node labels and enable CEF. Do not configure static/default routes, NAT, MPLS, route leaking, or redistribution between BGP and OSPF.

### Task 1 — Separate the transport routing table

1. On R11, R31, and R41, create `FVRF-INTERNET`, enable its IPv4 address family, and use RD `<local-AS>:100`.
2. Place only Ethernet0/0 into that VRF. Applying VRF forwarding removes the interface IP address: reapply its original address afterward and ensure the interface is enabled.
3. Keep Loopback0, Tunnel0, and OSPF in the global routing table. ISP uses only its global table. Do not configure route targets or an inside VRF. The RD is a local VRF identifier here; no VPNv4 route exchange is required.

### Task 2 — Establish the BGP underlay

1. Establish directly connected eBGP between each VPN router and its ISP .254 address. Use the AS numbers in the table. On VPN routers configure neighbors in `address-family ipv4 vrf FVRF-INTERNET`; on ISP use global IPv4 unicast. Explicitly activate neighbors and disable automatic global IPv4 neighbor activation.
2. Set each VPN router's BGP router ID to its Loopback0 address; set ISP's to 172.16.11.254. A router ID is an identifier and does not require transport reachability to the loopback.
3. Use exact BGP network statements: each VPN router originates its own transport /24; ISP originates all three connected transport /24s. Do not redistribute connected routes.
4. Apply exact-prefix import/export filters. On each VPN router use `TO-ISP` to permit only its local transport /24 and `FROM-ISP` to permit only the other two transport /24s. On ISP use `FROM-R11`, `FROM-R31`, and `FROM-R41` to accept only that peer's local transport /24; use `TO-R11`, `TO-R31`, and `TO-R41` to advertise only the other two transport /24s to each peer. Implicitly deny everything else.
5. Verify that each VPN router installs two remote BGP transport routes in `FVRF-INTERNET` and can ping both other NBMA addresses using a VRF-aware ping sourced from Ethernet0/0.

ISP already has connected transport routes; it originates them into BGP to provide reachability to the VPN routers. Customer advertisements exercise outbound filtering and reciprocal eBGP but do not replace ISP's connected routes. No LAN or tunnel prefix belongs in BGP. The transport routes' expected AS path at each VPN router is `65000`.

### Task 3 — Build Phase 3 DMVPN

1. Configure Tunnel0 as mGRE, sourced from Ethernet0/0. Select `FVRF-INTERNET` for the tunnel's outer route lookup with `tunnel vrf`. Do not move Tunnel0 itself into that VRF.
2. Use tunnel key **100**, NHRP network ID **100**, and NHRP authentication **ENARSI** everywhere. Configure MTU **1400**, TCP MSS **1360**, and disable ordinary IP redirects on Tunnel0. IP redirects and NHRP redirects are different mechanisms.
3. Configure R11 to learn spoke multicast destinations dynamically and send **NHRP redirects**.
4. Configure each spoke with only a static hub mapping (192.168.100.11 → 172.16.11.1), multicast mapping to 172.16.11.1, hub NHS 192.168.100.11, and **NHRP shortcut** processing. Do not configure static mappings to the other spoke or a tunnel destination.
5. The initial spoke-to-spoke routed path must use the hub. Subsequent traffic must trigger a dynamic direct shortcut, even though the OSPF topology still describes the hub-and-spoke path.

### Task 4 — Configure VRF-aware IKEv2/IPsec

Apply these settings on all three VPN routers:

| Object | Requirements |
|---|---|
| Proposal `DMVPN-PROPOSAL` | AES-CBC-256 encryption, SHA-1 integrity, SHA-1 PRF, DH group 14 |
| Policy `DMVPN-POLICY` | Reference the proposal; match `FVRF-INTERNET` |
| IKEv2 keyring `DMVPN-KEYRING` | Peer `DMVPN-PEERS`, any IPv4 peer address; local and remote PSK `ENARSI-DMVPN-2026` |
| IKEv2 profile `DMVPN-IKE` | Match `FVRF-INTERNET` and any remote IPv4 identity; identify locally using own NBMA IPv4 address; local/remote pre-shared authentication; reference the local keyring; lifetime 86400 seconds |
| Transform `DMVPN-TS` | `esp-aes 256 esp-sha-hmac`, transport mode |
| IPsec profile `DMVPN-IPSEC` | Reference the transform and IKEv2 profile |
| Tunnel0 | Attach `DMVPN-IPSEC` using tunnel protection |

Configure explicit IKEv2 parameters, rather than relying on smart defaults. IKEv2 keyrings do not use the IKEv1 `crypto keyring ... vrf` configuration form; select the FVRF in the IKEv2 policy/profile and tunnel configuration. Keep IPsec lifetime at its platform default and do not configure additional PFS. The inherited SHA-1 selection is retained for this lab. Do not configure IKEv1 or crypto maps.

### Task 5 — Exchange LAN routes with OSPF

1. Use global OSPF process **100**, area **0**, and each site's Loopback0 address as its router ID.
2. Enable OSPF explicitly on Tunnel0 and Loopback0. Make interfaces passive by default and permit neighbor formation only on Tunnel0. Do not enable OSPF on Ethernet0/0 or on ISP.
3. Use **point-to-multipoint** network type on every Tunnel0. No DR/BDR election or static OSPF neighbor statements are required. Configure Loopback0 with OSPF point-to-point network type so it advertises its assigned **/24**, rather than a loopback host route.
4. On all three routers define prefix list `OSPF-RIB`: deny only /32 routes within 192.168.100.0/24, then permit all other IPv4 prefixes. Apply it inbound to the OSPF routing-table installation process. This prevents OSPF's point-to-multipoint tunnel host routes from overriding the connected tunnel subnet during NHRP resolution. It must not filter the LAN /24s or alter LSA flooding.
5. Verify two FULL neighbors on R11 and one FULL hub neighbor on each spoke. Before a shortcut is learned, R31 must route 10.4.4.0/24 through 192.168.100.11; R41 must similarly route 10.3.3.0/24 through the hub. Do not try to preserve the other spoke as the OSPF next hop as in Phase 2.

### Task 6 — Demonstrate forwarding and isolation

Complete [VALIDATION.md](VALIDATION.md), including before/after shortcut evidence, direct spoke IPsec counters, and VRF separation. Then save all four configurations.

## Files, solutions, and reset

- `DMVPN-Phase3-IPSec.gns3project`: importable unsolved project, containing `project.gns3` and packaged IOU startup files.
- `startup-configs/`: readable copies of all four IP-only configurations.
- `final-configs/`: complete solutions for R11, R31, R41, and ISP.
- `VALIDATION.md`: runtime acceptance checks and expected results.
- `VERIFICATION.md` and `validate.py`: offline verification scope and repeatable checks.

To load solutions, import a fresh copy, leave all nodes stopped, and use GNS3's per-node startup editor/import action to load the corresponding final config. Start all four nodes afterward. Avoid merging a solution into an old Phase 2 configuration; leftover EIGRP, global routes, and crypto objects can obscure results. Reset by importing the original archive into a fresh directory.

This lab has been statically checked, not booted or live-tested. The installed IOU image must support BGP VRF address families, OSPF, VRF-aware IKEv2, and NHRP Phase 3 shortcuts. Record exact parser errors if any command is unavailable.
