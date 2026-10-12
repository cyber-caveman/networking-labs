# RIP Broadcast

## Scenario

A small company selling physical security solutions has asked for your help with their network. They own two routers running RIP and it seems the switch in the middle is running amok when it receives multicast traffic. The company doesn't have any budget so they ask you to solve the problem without replacing the switch.

## Goal

- All IP addresses have been preconfigured for you.
- Both routers have a loopback interface as following:
  - Vault: 1.1.1.1/24
  - Safe: 2.2.2.2/24
- Configure RIP version 2 on both routers, achieve full connectivity for all networks (including the loopbacks).
- You are not allowed to send RIP packets by multicast or unicast.

## GNS3 2.2.56.1

Import [RIP Broadcast IOU.gns3project](RIP%20Broadcast%20IOU.gns3project) using **File > Import portable project**. To open `RIP Broadcast.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Safe | FastEthernet0/0 | Ethernet0/0 |
| Vault | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-rip-broadcast.png)

## Video Solution

[Video Solution on YouTube](http://www.youtube.com/watch?v=xtuOUtQY2eA)
