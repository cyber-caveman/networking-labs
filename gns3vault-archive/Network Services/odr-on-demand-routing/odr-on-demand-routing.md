# ODR (On Demand Routing)

## Scenario

The international network of the Benelux doesn't have any more fancy equipment since the last cost saving project. The current routers don't support any routing protocol except ODR (On Demand Routing). You don't want to use static routes so it's up to you to setup ODR.

## Goal

- All IPv4 addresses have been preconfigured for you.
- Configure ODR on all routers and ensure you can reach the loopback interfaces of router Brussel and Luxemburg.

## GNS3 2.2.56.1

Import [ODR On Demand Routing IOU.gns3project](ODR%20On%20Demand%20Routing%20IOU.gns3project) using **File > Import portable project**. To open `ODR On Demand Routing.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Amsterdam | Serial0/0 | Serial4/0 |
| Amsterdam | Serial0/1 | Serial4/1 |
| Amsterdam | Serial0/2 | Serial4/2 |
| Amsterdam | Serial0/3 | Serial4/3 |
| Brussel | Serial0/0 | Serial4/0 |
| Brussel | Serial0/1 | Serial4/1 |
| Brussel | Serial0/2 | Serial4/2 |
| Brussel | Serial0/3 | Serial4/3 |
| Luxemburg | Serial0/0 | Serial4/0 |
| Luxemburg | Serial0/1 | Serial4/1 |
| Luxemburg | Serial0/2 | Serial4/2 |
| Luxemburg | Serial0/3 | Serial4/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-odr-on-demand-routing.png)

## Video Solution

http://www.youtube.com/watch?v=BKVWKOfB4VM
