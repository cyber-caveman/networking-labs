# RIP Summarization

## Scenario

Your are a construction worker for a company called "Apron Construction". You are looking for a method so your colleagues can easily send you information about construction parts they need. You grab a couple of older routers running RIP but they are running out of memory. You'll have to create some summaries to decrease the size of your routing tables and thus save some memory. Think you can DIY?

## Goal

- All IP addresses have been preconfigured for you.
- Configure RIP version 2 on all routers and make sure you have full connectivity.
- Create a summary on router Ballast so all networks on the loopback interfaces are advertised as one optimal route.
- Create four summaries for the loopback interfaces on router Beam without having overlapping networks.
- Create one summary on router Brick so all networks on the loopback interfaces are advertises as one optimal route.

## GNS3 2.2.56.1

Import [RIP Summarization IOU.gns3project](RIP%20Summarization%20IOU.gns3project) using **File > Import portable project**. To open `RIP Summarization.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Apron | FastEthernet0/0 | Ethernet0/0 |
| Apron | FastEthernet1/0 | Ethernet0/1 |
| Apron | FastEthernet2/0 | Ethernet0/2 |
| Ballast | FastEthernet0/0 | Ethernet0/0 |
| Beam | FastEthernet0/0 | Ethernet0/0 |
| Brick | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-rip-summarization.png)

## Video Solution

http://www.youtube.com/watch?v=jgDqE1oq5xA
