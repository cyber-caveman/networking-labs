# NAT Dynamic Troubleshooting

![Network Topology](./topology-nat-dynamic-troubleshooting.jpg)

## Scenario

Working for a company based in the caribbean isn't such a bad life. The sun is always shining and when there is no work you can relax at the beach. Today however you get a stress call from a junior network engineer who tried to replace a failed router. He claims to have configured NAT (network address translation) correctly but it's not working. Time for you to fix the problem!

## Goal

- All IP addresses have been preconfigured for you as following: 192.168.XY.X /24 where X = router1 and Y = router2. For example: 192.168.58.5 between router5 and router8.
- You are only allowed to make changes on router Jamaica.
- Your ISP has given you the 172.16.1.0/24 subnet to use for the NAT translation.
- **Do not use show run**! (this will spoil the fun :) use the appropriate 'show' and 'debug' commands. This will teach you the skills needed to become a true troubleshooting master.
- You need to make sure the 192.168.12.0 /24 subnet is translated into the IP addresses the ISP gave you when router John communicates with router Dave.

## GNS3 2.2.56.1

Import [nat-dynamic-troubleshooting-startup-configs IOU.gns3project](nat-dynamic-troubleshooting-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `nat-dynamic-troubleshooting-startup-configs.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| John | FastEthernet0/0 | Ethernet0/0 |
| Jamaica | FastEthernet0/0 | Ethernet0/0 |
| Jamaica | Serial1/0 | Serial4/0 |
| Jamaica | Serial1/1 | Serial4/1 |
| Jamaica | Serial1/2 | Serial4/2 |
| Jamaica | Serial1/3 | Serial4/3 |
| Florida | FastEthernet1/0 | Ethernet0/0 |
| Florida | Serial0/0 | Serial4/0 |
| Florida | Serial0/1 | Serial4/1 |
| Florida | Serial0/2 | Serial4/2 |
| Florida | Serial0/3 | Serial4/3 |
| Dave | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

## Video Solution

[Video Solution on YouTube](http://www.youtube.com/watch?v=THZ7git9wdk)
