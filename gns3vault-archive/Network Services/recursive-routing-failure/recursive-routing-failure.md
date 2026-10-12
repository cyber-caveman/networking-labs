# Recursive Routing Failure

## Scenario

You work as the network engineer for a company with an ambitious plan to build a tunnel between Japan and Australia. To support this project you have to configure the network with some new routers. You configure your network but you receive some "%TUN-5-RECURDOWN: Tunnel0 temporarily disabled due to recursive routing" errors. Time to dig to the core of this problem...

## Goal

- All IPv4 addresses have been preconfigured for you.
- Configure RIP version 2 on all routers. Use "network 0.0.0.0" to advertise everything on all routers.
- Configure a tunnel0 interface between the FastEthernet interfaces of router Japan and Australia.
- Configure network 192.168.13.0 /24 on the tunnel0 interface.
- Solve your recursive routing failure in any possible way.

## GNS3 2.2.56.1

Import [Recursive Routing Failure IOU.gns3project](Recursive%20Routing%20Failure%20IOU.gns3project) using **File > Import portable project**. To open `Recursive Routing Failure.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Australia | FastEthernet0/0 | Ethernet0/0 |
| China | FastEthernet0/0 | Ethernet0/0 |
| China | FastEthernet1/0 | Ethernet0/1 |
| Japan | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-recursive-routing-failure.png)

## Video Solution

[YouTube: Recursive Routing Failure Solution](http://www.youtube.com/watch?v=U2W777W7VGk)
