# TCP and RTP Header Compression

## Scenario

You are responsible for the WAN links at the company you work for. Your routers have a very low CPU load and the serial interfaces you have are pretty slow. You decide one day to run TCP and UDP header compression to get the most out of your connections...let's squeeze some bits!

## Goal

- All IP addresses have been preconfigured for you.
- Enable TCP and RTP header compression on both routers.
- Configure a maximum of 12 compressed TCP or RTP sessions.
- Router Smaller should only use compression when it receives compressed traffic.

## GNS3 2.2.56.1

Import [TCP and UDP Header Compression IOU.gns3project](TCP%20and%20UDP%20Header%20Compression%20IOU.gns3project) using **File > Import portable project**. To open `TCP and UDP Header Compression.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Compress | Serial0/0 | Serial4/0 |
| Compress | Serial0/1 | Serial4/1 |
| Compress | Serial0/2 | Serial4/2 |
| Compress | Serial0/3 | Serial4/3 |
| Smaller | Serial0/0 | Serial4/0 |
| Smaller | Serial0/1 | Serial4/1 |
| Smaller | Serial0/2 | Serial4/2 |
| Smaller | Serial0/3 | Serial4/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-tcp-and-udp-header-compression.png)

## Video Solution

http://www.youtube.com/watch?v=2D47Pu_SueU
