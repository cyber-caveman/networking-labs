# IP Event Dampening

## Scenario

Garden Tools inc. has some trouble with their network. Every now and then the serial link fails which results in flapping networks for their routing protocol EIGRP. You want to configure damping so this is no issue anymore.

## Goal

- All IP addresses have been preconfigured for you.
- Configure EIGRP AS 1 and achieve full connectivity.
- Configure dampening on router Spray so whenever the serial link fails the route will not be advertised in EIGRP for 20 seconds. It shouldn't be dampened for more than 40 seconds.

## GNS3 2.2.56.1

Import [IP Event Dampening IOU.gns3project](IP%20Event%20Dampening%20IOU.gns3project) using **File > Import portable project**. To open `IP Event Dampening.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Rinse | Serial0/0 | Serial4/0 |
| Rinse | Serial0/1 | Serial4/1 |
| Rinse | Serial0/2 | Serial4/2 |
| Rinse | Serial0/3 | Serial4/3 |
| Spray | FastEthernet1/0 | Ethernet0/0 |
| Spray | Serial0/0 | Serial4/0 |
| Spray | Serial0/1 | Serial4/1 |
| Spray | Serial0/2 | Serial4/2 |
| Spray | Serial0/3 | Serial4/3 |
| Sprinkle | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-ip-event-dampening.png)

## Video Solution

[Video Solution on YouTube](http://www.youtube.com/watch?v=63BLfPjJWj0)
