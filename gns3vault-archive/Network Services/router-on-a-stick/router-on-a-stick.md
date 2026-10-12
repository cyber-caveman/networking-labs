# Router on a stick

## Scenario

You are Sam the network engineer who is responsible for all routing within your company. Two of your colleagues called John and Hadley are having trouble reaching each other, their routers do not have any routing capabilities and they are located in different vlans. It's up to you to help them restore connectivity by becoming a router on a stick.

## Goal

- All IP addresses have been preconfigured as specified in the topology picture.
- Do not configure any routing protocol or use static routes.
- You are allowed to create additional interfaces and IP addresses on router Sam.
- Ensure router John and Hadley can ping each other.

## Overview

## GNS3 2.2.56.1

Import [router-on-a-stick-startup-configs IOU.gns3project](router-on-a-stick-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `router-on-a-stick-startup-configs.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Hadley | FastEthernet0/0 | Ethernet0/0 |
| Hadley | FastEthernet0/1 | Ethernet0/1 |
| John | FastEthernet0/0 | Ethernet0/0 |
| John | FastEthernet0/1 | Ethernet0/1 |
| Sam | FastEthernet0/0 | Ethernet0/0 |
| Sam | FastEthernet0/1 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-router-on-a-stick.png)

## Video Solution

- [YouTube Video Solution](http://www.youtube.com/watch?v=BF5y7i5yZEA)
