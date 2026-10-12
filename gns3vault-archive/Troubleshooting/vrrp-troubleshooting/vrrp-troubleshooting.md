# VRRP Troubleshooting

## Scenario

VRRP (Virtual Router Redundancy Protocol) is used within your organization to make sure clients will always have a working default gateway. One of your routers was having issues and someone from the network trainees decided to change the VRRP configuration to solve this problem. He didn't exactly know what he was doing and he confessed he totally screwed up the VRRP configuration on all routers...up to you to show him who the router guru is and fix this problem!

## Goal

- All IP addresses have been preconfigured for you.
- **Do not use show run**! (this will spoil the fun :) use the appropriate 'show' and 'debug' commands. This will teach you the skills needed to become a true troubleshooting master.
- Router NewYork, NewJersey and LA should work together for VRRP group 1 to create a virtual gateway with IP address 192.168.1.254.
- Test each router as the Master VRRP router and see if traffic from the client can successfully be sent to the ISP router on the far side.
- Test each router to see if interface tracking is working successfully. If the Fa0/1 interface on router NewYork, NewJersey or LA goes down then another router should become VRRP Master.

## GNS3 2.2.56.1

Import [VRRP Troubleshooting IOU.gns3project](VRRP%20Troubleshooting%20IOU.gns3project) using **File > Import portable project**. To open `VRRP Troubleshooting.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| HOST | FastEthernet0/0 | Ethernet0/0 |
| HOST | FastEthernet0/1 | Ethernet0/1 |
| ISP | FastEthernet0/0 | Ethernet0/0 |
| ISP | FastEthernet0/1 | Ethernet0/1 |
| LA | FastEthernet0/0 | Ethernet0/0 |
| LA | FastEthernet0/1 | Ethernet0/1 |
| NewJersey | FastEthernet0/0 | Ethernet0/0 |
| NewJersey | FastEthernet0/1 | Ethernet0/1 |
| NewYork | FastEthernet0/0 | Ethernet0/0 |
| NewYork | FastEthernet0/1 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-vrrp-troubleshooting.png)
