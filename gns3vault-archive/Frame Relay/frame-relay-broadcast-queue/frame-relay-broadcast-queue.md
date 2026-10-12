# Frame Relay Broadcast Queue

## Scenario

Jack and Emma are using frame relay but it seems there is so much broadcast traffic that the link is experiencing congestion. You need to make sure this will not happen in the future without using QoS or influencing any routing protocols (except RIPv1).

## Goal

* All IP addresses have been preconfigured for you.
* Configure router Jack and Emma so the broadcast queue has a maximum of 50 packets. The rate should only be 64KBps and there shouldn't be more than 20 packets per second.

## GNS3 2.2.56.1

Import [Frame Relay Broadcast Queue IOU.gns3project](Frame%20Relay%20Broadcast%20Queue%20IOU.gns3project) using **File > Import portable project**. To open `Frame Relay Broadcast Queue.gns3` directly, keep it beside `project-files`.

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

![Network Topology](./topology-frame-relay-broadcast-queue.png)

## Video Solution

http://www.youtube.com/watch?v=RiwOadVowvs
