# Frame-Relay Basics

![Network Topology](./topology-frame-relay-basics.jpg)

## Scenario

As a CCNA candidate you are familiar with the concept of Frame-Relay, although you do not need to configure the Frame-Relay switch. Since you are working your way to becoming the ultimate networking Guru, you are prepared to do a full Frame-Relay config....that includes the Frame-Relay Switch! Configuring a point-to-multipoint and point-to-point PVC and having ip connectivity is your goal.

## Goal

* Take a good look at the topology before you start configuring.
* The green lines are PVC's (Permanent Virtual Circuit) and this is supposed to be a point-to-multipoint.
* Paris should be the "hub" and Berlin and Stockholm are "spoke" routers.
* The blue line is a point-to-point PVC between Paris and Berlin.
* DLCI numbers are shown on the topology picture.
* Use the 192.168.123.0 /24 subnet for the point-to-multipoint connection, use a subinterface.
* Use the 192.168.12.0 /24 subnet for the point-to-point connection, use a subinterface.
* Achieve full IP connectivity, all ip addresses should be pingable.

## GNS3 2.2.56.1

Import [frame-relay-basics-startup-configs IOU.gns3project](frame-relay-basics-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `frame-relay-basics-startup-configs.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Frame Relay switching routers retain Dynamips and the available C3640 appliance, with device-specific config packaging. Their source configuration text is preserved.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| FRSW | Serial0/0 | Serial0/0 |
| FRSW | Serial0/1 | Serial0/1 |
| FRSW | Serial0/2 | Serial0/2 |
| FRSW | Serial0/3 | Serial0/3 |
| Paris | Serial0/0 | Serial4/0 |
| Paris | Serial0/1 | Serial4/1 |
| Paris | Serial0/2 | Serial4/2 |
| Paris | Serial0/3 | Serial4/3 |
| Berlin | Serial0/0 | Serial4/0 |
| Berlin | Serial0/1 | Serial4/1 |
| Berlin | Serial0/2 | Serial4/2 |
| Berlin | Serial0/3 | Serial4/3 |
| Stockholm | Serial0/0 | Serial4/0 |
| Stockholm | Serial0/1 | Serial4/1 |
| Stockholm | Serial0/2 | Serial4/2 |
| Stockholm | Serial0/3 | Serial4/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

## Video Solution

[Frame-Relay Basics Video Solution](http://www.youtube.com/watch?v=77J47L5FQNI)
