# Frame Relay Static Mapping

## Scenario

Jack and Emma are using an old frame-relay switch to connect their routers. Unfortunately they are unable to get any connection. Think you can help them out?

## Goal

* All IP addresses have been preconfigured for you.
* Disable frame relay inverse ARP.
* Configure frame relay mappings so the routers can ping each other.
* Frame relay should support broadcast emulation.

## GNS3 2.2.56.1

Import [Frame Relay Static Mapping IOU.gns3project](Frame%20Relay%20Static%20Mapping%20IOU.gns3project) using **File > Import portable project**. To open `Frame Relay Static Mapping.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Emma | Serial0/0 | Serial4/0 |
| Emma | Serial0/1 | Serial4/1 |
| Emma | Serial0/2 | Serial4/2 |
| Emma | Serial0/3 | Serial4/3 |
| Jack | Serial0/0 | Serial4/0 |
| Jack | Serial0/1 | Serial4/1 |
| Jack | Serial0/2 | Serial4/2 |
| Jack | Serial0/3 | Serial4/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-frame-relay-static-mapping.png)

## Video Solution

[Video on YouTube](http://www.youtube.com/watch?v=h45467tCo3w)
