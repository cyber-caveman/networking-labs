# GLBP Troubleshooting

## Scenario

The agency has acquired you as a special network engineer. Within the organization there is a network that is using GLBP as their FHRP (First Hop Routing Protocol). Recently the agency was hit by an EMP (Electromagnetic Pulse) attack and some of the bits on your routers have been flipped. As a result the GLBP configuration is messed up and agents Connery and Brosnan have trouble reaching router Moneypenny. Up to you to shake it up and fix GLBP!

## Goal

* All IP addresses have been preconfigured for you.
* **Do not use show run**! (this will spoil the fun :) use the appropriate 'show' and 'debug' commands. This will teach you the skills needed to become a true troubleshooting master.
* Router Dalton and Moore are configured for GLBP but there are issues.
* Make sure router Dalton and Moore are both configured for GLBP Virtual IP address 7.7.7.7 and that they can serve clients.

## GNS3 2.2.56.1

Import [GLBP Troubleshooting IOU.gns3project](GLBP%20Troubleshooting%20IOU.gns3project) using **File > Import portable project**. To open `GLBP Troubleshooting.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Brosnan | FastEthernet0/0 | Ethernet0/0 |
| Connery | FastEthernet0/0 | Ethernet0/0 |
| Dalton | FastEthernet0/0 | Ethernet0/0 |
| Dalton | Serial1/0 | Serial4/0 |
| Dalton | Serial1/1 | Serial4/1 |
| Dalton | Serial1/2 | Serial4/2 |
| Dalton | Serial1/3 | Serial4/3 |
| MoneyPenny | Serial0/0 | Serial4/0 |
| MoneyPenny | Serial0/1 | Serial4/1 |
| MoneyPenny | Serial0/2 | Serial4/2 |
| MoneyPenny | Serial0/3 | Serial4/3 |
| Moore | FastEthernet0/0 | Ethernet0/0 |
| Moore | Serial1/0 | Serial4/0 |
| Moore | Serial1/1 | Serial4/1 |
| Moore | Serial1/2 | Serial4/2 |
| Moore | Serial1/3 | Serial4/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-glbp-troubleshooting.png)
