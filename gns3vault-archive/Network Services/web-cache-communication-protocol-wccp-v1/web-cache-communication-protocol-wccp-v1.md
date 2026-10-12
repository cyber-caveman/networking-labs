# Web Cache Communication Protocol (WCCP) V1

## Scenario

Many users on your network are using the Internet but the connection you have from the ISP is quite expensive. You want to get the most out of your connection and ensure users don't load pages from the Internet that have been loaded previously. You decide to implement a web cache server using WCCP v1. Let's see if you can configure the router to support this.

## Goal

- All IP addresses have been preconfigured for you.
- Router "webcache" is a fictional web cache server, we can still practice the commands needed for WCCPv1 with this lab.
- Configure router "redirector" so it redirects packet for web caching to router "webcache".
- Configure a loopback0 interface on router "client" with IP address 1.1.1.1 /24.
- Configure router "redirector" so it excludes redirection from network 1.1.1.0 /24.

## GNS3 2.2.56.1

Import [Web Cache Communication Protocol (WCCP) V1 IOU.gns3project](Web%20Cache%20Communication%20Protocol%20%28WCCP%29%20V1%20IOU.gns3project) using **File > Import portable project**. To open `Web Cache Communication Protocol (WCCP) V1.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Client | FastEthernet0/0 | Ethernet0/0 |
| Internet | FastEthernet0/0 | Ethernet0/0 |
| Redirector | FastEthernet0/0 | Ethernet0/0 |
| Redirector | FastEthernet1/0 | Ethernet0/1 |
| Redirector | FastEthernet2/0 | Ethernet0/2 |
| WebCache | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-web-cache-communication-protocol-wccp-v1.png)

## Video Solution

http://www.youtube.com/watch?v=4_xEqrSGj2A
