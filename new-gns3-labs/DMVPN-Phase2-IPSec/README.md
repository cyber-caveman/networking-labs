# DMVPN-Phase2-IPSec

Configure secure connectivity between headquarters R11 and branch routers R31 and R41 using the supplied topology. This is original exam-style practice material, not an actual Cisco exam item or an official Cisco assessment. Suggested time: 60–90 minutes.

## Launch and initial state

Import **DMVPN-Phase2-IPSec.gns3project** using GNS3's portable-project import action. Target version: **2.2.56.1**. All four routers use the repository's preferred `x86_64_crb_linux-adventerprisek9-ms.bin` IOU L3 appliance (768 MB RAM, 512 KB NVRAM, four Ethernet and four serial adapters). Supply your own installed image and IOU license. Console ports are allocated automatically.

The archive contains the unsolved exercise. Startup files include only interface IP addresses, `no shutdown`, configuration separators, and `end`. No hostname, routing, NHRP, GRE parameters, or crypto configuration is supplied. Identify consoles by their GNS3 node labels; IOS prompts may initially have a default hostname. Tunnel0 already has its IP address but is not operational until you configure its source and mode. Adjacent transport addresses are reachable initially; remote transport subnets and remote LANs are not.

The diagram's cloud is implemented by a fourth router, **ISP**, with three directly connected networks. Its IP-only configuration is sufficient to forward transport packets. The three depicted LANs are represented by Loopback0 interfaces so no end hosts or additional switches are required. Transport /24 masks, ISP addresses, and tunnel host addresses are lab design choices; the supplied diagram specifies only the transport host addresses and overlay/LAN prefixes.

| Router | Role | Ethernet0/0 | Loopback0 (site LAN) | Tunnel0 |
|---|---|---|---|---|
| R11 | Hub | 172.16.11.1/24 | 10.1.1.1/24 | 192.168.100.11/24 |
| R31 | Spoke | 172.16.31.1/24 | 10.3.3.1/24 | 192.168.100.31/24 |
| R41 | Spoke | 172.16.41.1/24 | 10.4.4.1/24 | 192.168.100.41/24 |

| Physical link | ISP address |
|---|---|
| R11 Ethernet0/0 — ISP Ethernet0/0 | 172.16.11.254/24 |
| R31 Ethernet0/0 — ISP Ethernet0/1 | 172.16.31.254/24 |
| R41 Ethernet0/0 — ISP Ethernet0/2 | 172.16.41.254/24 |

Logical overlay: `R31 ←→ R11 ←→ R41`, with on-demand direct `R31 ←→ R41` forwarding. Physical packets still traverse ISP; direct means bypassing R11 as a VPN transit router.

## Candidate instructions

Complete the following tasks on R11, R31, and R41. Do not modify ISP. Do not change the supplied addressing. Use the object names and values specified below. Configure hostnames to match the node labels and enable CEF on the three VPN routers.

### Task 1 — Establish transport reachability

1. Configure one IPv4 default route on each VPN router through its directly connected ISP address.
2. Verify that every VPN router can reach both remote NBMA addresses when sourcing traffic from Ethernet0/0.
3. Do not run a routing protocol on the transport interfaces. Do not add routes for the site LANs on ISP or static routes for remote LANs on the VPN routers.

### Task 2 — Configure the DMVPN overlay

1. Configure **DMVPN Phase 2** on Tunnel0 on all three VPN routers. Use Ethernet0/0 as the source, multipoint GRE, tunnel key **100**, NHRP network ID **100**, and NHRP authentication string **ENARSI**.
2. Configure R11 as the NHRP next-hop server. R11 must learn spoke NBMA mappings and multicast replication destinations dynamically.
3. On each spoke, configure only the hub's static unicast mapping and hub multicast mapping. Register with the hub at **192.168.100.11**. Do not configure static mappings for the other spoke.
4. Permit direct spoke-to-spoke tunnels to form dynamically. Do not configure tunnel destinations, NHRP redirects, or NHRP shortcuts.
5. Set tunnel IPv4 MTU to **1400** and TCP maximum segment size adjustment to **1360** on all three routers.

### Task 3 — Protect the overlay with IPsec

Apply these identical security requirements on all three VPN routers:

| Item | Required value |
|---|---|
| IKE version | IKEv2 |
| IKEv2 proposal | `DMVPN-PROPOSAL` |
| IKE encryption / integrity / PRF | AES-CBC-256 / SHA-1 / SHA-1 (`encryption aes-cbc-256`, `integrity sha1`, `prf sha1`) |
| IKEv2 policy | `DMVPN-POLICY`, referencing `DMVPN-PROPOSAL` in the global routing table |
| IKE authentication | Local and remote pre-shared key authentication |
| Diffie–Hellman group / IKE SA lifetime | 14 / 86400 seconds (lifetime in the IKEv2 profile) |
| IKEv2 keyring | `DMVPN-KEYRING` |
| Keyring peer entry | `DMVPN-PE÷ERS`, matching any IPv4 peer address (`0.0.0.0 0.0.0.0`) |
| Local and remote passphrase | `ENARSI-DMVPN-2026` (case-sensitive, identical in both directions) |
| IKEv2 profile | `DMVPN-IKE`, matching any remote IPv4 identity; use `keyring local DMVPN-KEYRING` |
| Local IKE identity | Each router's own Ethernet0/0 NBMA IPv4 address |
| IPsec transform set | `DMVPN-TS` |
| ESP encryption / integrity | AES-256 / HMAC-SHA-1 (`esp-aes 256 esp-sha-hmac`) |
| Encapsulation mode | Transport |
| IPsec profile | `DMVPN-IPSEC`, referencing the transform set and IKEv2 profile (`set ikev2-profile DMVPN-IKE`) |
| Attachment | Tunnel protection on Tunnel0 |

Use an IKEv2 keyring for both local and remote passphrases. Bind it to the IKEv2 profile and bind that profile to the IPsec profile. Do not configure IKEv1/ISAKMP objects. Do not use a crypto map or a crypto ACL. Keep IPsec SA lifetime at its platform default and do not add PFS to the IPsec profile. Protect both hub–spoke and dynamic spoke–spoke sessions.

AES supplies encryption; SHA-1 is selected for IKEv2 integrity and its pseudorandom function (PRF); HMAC-SHA-1 supplies ESP integrity/authentication. These are distinct algorithm roles, not three separate IPsec protocols.

### Task 4 — Exchange site routes using EIGRP

1. Configure classic IPv4 EIGRP autonomous system **100** on all three VPN routers.
2. Advertise only the local Loopback0 /24 and **192.168.100.0/24** using specific network statements. Do not redistribute routes or advertise transport prefixes or a default route.
3. Make all interfaces passive by default, enabling EIGRP neighbor formation only on Tunnel0. Disable automatic summarization.
4. Ensure that R11 advertises routes learned from one spoke to the other spoke and preserves the originating spoke's tunnel address as the EIGRP next hop. Apply the necessary interface-level settings on R11.
5. Do not summarize the spoke LANs. R31 must learn 10.4.4.0/24 with next hop **192.168.100.41**; R41 must learn 10.3.3.0/24 with next hop **192.168.100.31**.

### Task 5 — Verify and save

Use [VALIDATION.md](VALIDATION.md) to demonstrate transport connectivity, NHRP registration, EIGRP adjacency and route selection, encrypted site-to-site traffic, and dynamic spoke-to-spoke forwarding. Successful pings alone do not satisfy the security requirement. Save each VPN router's configuration after all checks pass.

## Files and solution workflow

- `project.gns3` and `project-files/`: unpacked portable-project contents.
- `startup-configs/`: readable copies of each node's IP-only initial configuration.
- `final-configs/`: complete reference configurations for R11, R31, R41, and ISP. ISP's final configuration equals its startup configuration.
- `VALIDATION.md`: runtime checks and expected results.
- `VERIFICATION.md`: performed offline checks, limitations, and Cisco references.
- `validate.py`: reproducible static validation of the delivered files.

To load the reference solution, use a fresh imported copy, keep all nodes stopped, and replace each node's startup configuration through GNS3's startup-configuration editor/import action with its matching `final-configs/<node>.cfg`. Then start all nodes. These are configuration files, not exec-mode paste scripts. Do not merge them into an unknown running configuration. To restart the unsolved exercise, import the original archive into a fresh directory; saved runtime state in an existing project may override edited startup files.

The preferred IOU image has not been booted or parser-tested here. Live acceptance of the crypto commands and encrypted forwarding must be confirmed on your installed image; see the validation checklist. No image or license is distributed.
