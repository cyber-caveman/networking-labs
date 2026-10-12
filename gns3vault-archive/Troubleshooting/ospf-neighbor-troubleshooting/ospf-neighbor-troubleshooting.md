# OSPF Neighbor Troubleshooting

## Scenario

The hotel agency has had several network engineers trying to configure OSPF for them. As a result the whole network is one big mess and they decide to hire you to fix their problems. There are two OSPF areas and all routers are running OSPF. Unfortunately all OSPF neighbor adjacencies are broken...you feel like you are standing on a ledge but you should be able to fix this!

## Goal

* All IP addresses have been preconfigured for you.
* OSPF is preconfigured with the areas as specified in the topology picture.
* **Do not use show run**! (this will spoil the fun :) use the appropriate 'show' and 'debug' commands. This will teach you the skills needed to become a true troubleshooting master.
* Your goal is simple: Make sure all OSPF neighbor adjacencies are working!

## GNS3 2.2.56.1

Import [OSPF Neighbor Troubleshooting IOU.gns3project](OSPF%20Neighbor%20Troubleshooting%20IOU.gns3project) using **File > Import portable project**. To open `OSPF Neighbor Troubleshooting.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Angie | FastEthernet0/0 | Ethernet0/0 |
| Angie | FastEthernet1/0 | Ethernet0/1 |
| Angie | FastEthernet2/0 | Ethernet0/2 |
| Jack | FastEthernet0/0 | Ethernet0/0 |
| Janice | Serial0/0 | Serial4/0 |
| Janice | Serial0/1 | Serial4/1 |
| Janice | Serial0/2 | Serial4/2 |
| Janice | Serial0/3 | Serial4/3 |
| Joey | FastEthernet0/0 | Ethernet0/0 |
| Joey | FastEthernet1/0 | Ethernet0/1 |
| Joey | Serial2/0 | Serial4/0 |
| Joey | Serial2/1 | Serial4/1 |
| Joey | Serial2/2 | Serial4/2 |
| Joey | Serial2/3 | Serial4/3 |
| Mike | FastEthernet0/0 | Ethernet0/0 |
| Mike | FastEthernet1/0 | Ethernet0/1 |
| Nick | FastEthernet0/0 | Ethernet0/0 |
| Nick | FastEthernet1/0 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-ospf-neighbor-troubleshooting.png)
