# Integrated Routing and Bridging (IRB)

![Network Topology](./topology-integrated-routing-and-bridging.jpg)

## Scenario

As the network manager for a greek company called "DivineLabs" you are assigned the task to configure Integrated Routing and Bridging (IRB) on some of your routers. Some of the older applications that the company is still using only work with IPX, and they need to be supported in the future as well. You heard about IRB and how it can turn a router into a bridge, this might be a good solution for some future problems when the network will be upgraded. Time for you to configure some bridging!

## Goal

- You are only allowed to use a single subnet: 192.168.123.0 /24
  - Router Wodan: 192.168.123.1
  - Router Thor: 192.168.123.2
  - Router Zeus: 192.168.123.3
- Configure IRB on Router Thor.
- The goal is to achieve full connectivity, you need to be able to ping all IP addresses.

## GNS3 2.2.56.1

Import [irb-startup-configs IOU.gns3project](irb-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `irb-startup-configs.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Thor | FastEthernet0/0 | Ethernet0/0 |
| Thor | FastEthernet1/0 | Ethernet0/1 |
| Wodan | FastEthernet0/0 | Ethernet0/0 |
| Zeus | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

## Video Solution

[Video Solution](http://www.youtube.com/watch?v=AbvZLIB5VZ0)
