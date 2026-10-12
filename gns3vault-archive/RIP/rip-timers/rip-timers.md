# RIP Timers

## Scenario

"Tools Inc" is a small shop selling second-hand tools to network engineers. You are one of their customers and after buying a nice Axe they ask you for their help with their RIP network. The convergence time seems to be a bit slow and they ask you if it's possible to tune it. Can you drop the hammer on this one?

## Goal

- All IP addresses have been preconfigured for you.
- Configure RIP version 2 on all routers and make sure you have full connectivity.
- Tune the RIP timers so convergence is six times faster than the default.
- Your changes should not effect the link between router Hammer and Wrench.

## GNS3 2.2.56.1

Import [RIP Timers IOU.gns3project](RIP%20Timers%20IOU.gns3project) using **File > Import portable project**. To open `RIP Timers.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Axe | FastEthernet0/0 | Ethernet0/0 |
| Axe | FastEthernet1/0 | Ethernet0/1 |
| Hammer | FastEthernet0/0 | Ethernet0/0 |
| Hammer | FastEthernet1/0 | Ethernet0/1 |
| Wrench | FastEthernet0/0 | Ethernet0/0 |
| Wrench | FastEthernet1/0 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-rip-timers.png)

## Video Solution

http://www.youtube.com/watch?v=kfgyp6C-YBg
