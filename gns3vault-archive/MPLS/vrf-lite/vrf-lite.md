# VRF Lite

![Network Topology](./topology-vrf-lite.jpg)

## Scenario

You are running a small ISP on a tropical location somewhere in the pacific, recently two new customers have arrived and they both have 2 sites to connect. There's a headquarters (HQ) and a branch office and they want to use OSPF as the routing protocol. One of the problems you are facing is that both customers are using the same IP addressing scheme and it's impossible to change this. You also have to make sure that there is NO connectivity between the two companies. You believe vrf might be the solution to your problems...if you are able to pull this off you'll be rewarded with an infinite amount of grapes and melons from your customers...time to work!

## Goal

* All IP addresses on the customer routers have been preconfigured for you.
* You are not allowed to change the IP addressing scheme in this topology.
* Configure the ISP router so you can ping router MelonHQ and MelonBranch.
* Configure the ISP router so you can ping router GrapeHQ and GrapeBranch.
* Configure OSPF Area 0 on router ISP, MelonHQ and MelonBranch, advertise all networks.
* Configure OSPF Area 0 on router ISP, GrapeHQ and GrapeBranch, advertise all networks.
* Router MelonHQ and MelonBranch should see each other's loopback networks.
* Router GrapeHQ and GrapeBranch should see each other's loopback networks.
* The Melon and Grape routers should NOT see each others routes and there should be no connectivity between them.

## GNS3 2.2.56.1

Import [VRF Lite IOU.gns3project](VRF%20Lite%20IOU.gns3project) using **File > Import portable project**. To open `VRF Lite.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| ISP | FastEthernet0/0 | Ethernet0/0 |
| ISP | FastEthernet1/0 | Ethernet0/1 |
| ISP | FastEthernet2/0 | Ethernet0/2 |
| ISP | FastEthernet3/0 | Ethernet0/3 |
| GrapeHQ | FastEthernet0/0 | Ethernet0/0 |
| MelonHQ | FastEthernet0/0 | Ethernet0/0 |
| GrapeBranch | FastEthernet0/0 | Ethernet0/0 |
| MelonBranch | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

## Video Solution

http://www.youtube.com/watch?v=kR66WPUbgy0
