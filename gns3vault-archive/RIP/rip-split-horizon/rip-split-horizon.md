# RIP Split Horizon

## Scenario

Jack and Joe both have important information to share with each other but they don't have a direct connection between them. Tori agreed to help out and so they setup a Frame-Relay network to share information. RIP is used as the routing protocol to dynamically learn new networks. Configuring RIP should be straight forward but Joe and Jack are complaining that they are unable to reach other's networks...time for you to fix it!

## Goal

- All IP addresses have been preconfigured for you.
- Every router has a loopback0 interface:
  - Tori: 1.1.1.1 /24
  - Joe: 2.2.2.2 /24
  - Jack: 3.3.3.3 /24
- You are not allowed to make any changes to the frame-relay configurations.
- Configure RIPv2 on all routers, advertise all networks.
- Ensure router Joe and Jack can see each other's loopback interfaces. Test this by sending a ping that is sourced from the loopback0 interfaces and destined for the other loopback0 interface.

## GNS3 2.2.56.1

Import [RIP Split Horizon IOU.gns3project](RIP%20Split%20Horizon%20IOU.gns3project) using **File > Import portable project**. To open `RIP Split Horizon.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Jack | Serial0/0 | Serial4/0 |
| Jack | Serial0/1 | Serial4/1 |
| Jack | Serial0/2 | Serial4/2 |
| Jack | Serial0/3 | Serial4/3 |
| Joe | Serial0/0 | Serial4/0 |
| Joe | Serial0/1 | Serial4/1 |
| Joe | Serial0/2 | Serial4/2 |
| Joe | Serial0/3 | Serial4/3 |
| Tori | Serial0/0 | Serial4/0 |
| Tori | Serial0/1 | Serial4/1 |
| Tori | Serial0/2 | Serial4/2 |
| Tori | Serial0/3 | Serial4/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-rip-split-horizon.png)

## Video Solution

[Video Solution](http://www.youtube.com/watch?v=FqSIX7bOFxo)
