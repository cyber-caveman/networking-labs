# Frame Relay End to End Keepalive

## Scenario

Jack and Emma are using frame relay for their network but it seems there are some problems with LMI. Frame relay is being used at router Jack and Emma but they are not directly connected but through a MPLS backbone. As a result LMI is not working as a end-to-end solution. Configure the network so we can use a keepalive mechanism that works.

## Goal

* All IP addresses have been preconfigured for you.
* Router Emma should start by sending keepalive messages, router Jack should only respond to them.
* A keepalive message should be sent every 3 seconds, the event windows should be 6 and the threshold for errors should be 5.
* Configure router Emma so the configuration is attached to the DLCI.
* Configure router Jack so the configuration is attached to the physical interface.

## GNS3 2.2.56.1

Import [Frame Relay End-to-End KeepAlive IOU.gns3project](Frame%20Relay%20End-to-End%20KeepAlive%20IOU.gns3project) using **File > Import portable project**. To open `Frame Relay End-to-End KeepAlive.gns3` directly, keep it beside `project-files`.

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

![Network Topology](./topology-frame-relay-end-to-end-keepalive.png)

## Video Solution

http://www.youtube.com/watch?v=9-5d4kMETnA
