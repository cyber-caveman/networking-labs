# Frame Relay Point to Point Subinterface

## Scenario

Most toons from the fairy tale forest have switched their career to become network engineers. Cinderella has been trying to reach Hansel and Gretel through the frame relay network but hasn't had any luck. Think you can take this dance?

## Goal

* Configure all routers to use frame-relay encapsulation.
* Configure the IP addresses as specified in the topology picture on point-to-point subinterfaces.
* Ensure you can ping both routers from router Cinderella.

## GNS3 2.2.56.1

Import [Frame Relay Point to Point Subinterface IOU.gns3project](Frame%20Relay%20Point%20to%20Point%20Subinterface%20IOU.gns3project) using **File > Import portable project**. To open `Frame Relay Point to Point Subinterface.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Cinderella | Serial0/0 | Serial4/0 |
| Cinderella | Serial0/1 | Serial4/1 |
| Cinderella | Serial0/2 | Serial4/2 |
| Cinderella | Serial0/3 | Serial4/3 |
| Gretel | Serial0/0 | Serial4/0 |
| Gretel | Serial0/1 | Serial4/1 |
| Gretel | Serial0/2 | Serial4/2 |
| Gretel | Serial0/3 | Serial4/3 |
| Hansel | Serial0/0 | Serial4/0 |
| Hansel | Serial0/1 | Serial4/1 |
| Hansel | Serial0/2 | Serial4/2 |
| Hansel | Serial0/3 | Serial4/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-frame-relay-point-to-point-subinterface.png)

## Video Solution

[Video: Frame Relay Point to Point Subinterface](http://www.youtube.com/watch?v=mw0-DGFW_jg)
