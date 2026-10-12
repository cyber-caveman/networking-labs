# RIP Unicast

## Scenario

You are the junior network engineer of a company selling Videogames. The company has a small network running RIP between their routers. It seems something is going wrong with RIP multicast traffic. Think you can solve this game?

## Goal

- All IP addresses have been preconfigured for you.
- Both routers have a loopback interface as following:
  - Game: 1.1.1.1/24
  - Over: 2.2.2.2/24
- Configure RIP version 2 on both routers, achieve full connectivity for all networks (including the loopbacks).
- You are not allowed to send RIP packets by multicast or broadcast.

## GNS3 2.2.56.1

Import [RIP Unicast IOU.gns3project](RIP%20Unicast%20IOU.gns3project) using **File > Import portable project**. To open `RIP Unicast.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Game | FastEthernet0/0 | Ethernet0/0 |
| Over | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-rip-unicast.png)

## Video Solution

http://www.youtube.com/watch?v=-F5wyfVrx5g
