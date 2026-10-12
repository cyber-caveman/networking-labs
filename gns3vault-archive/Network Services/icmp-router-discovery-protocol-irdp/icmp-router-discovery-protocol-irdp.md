# ICMP Router Discovery Protocol (IRDP)

## Scenario

As the senior network engineer for "Groceries 'r' Us" you are responsible for all routing within the company. The network you are running is fairly old and doesn't support any fancy routing protocols. Your routers seem to support ICMP Route Discovery Protocol (IRDP) but you are not sure what it does...time to find out!

## Goal

- All IP addresses have been preconfigured for you.
- You are not allowed to use any routing protocol or static routing.
- Disable IP routing on router Broccoli.
- Configure router Potato and Tomato to advertise themselves as gateways for router Brocolli.
- Router Tomato should be the default gateway.

## GNS3 2.2.56.1

Import [ICMP Router Discovery Protocol (IRDP) IOU.gns3project](ICMP%20Router%20Discovery%20Protocol%20%28IRDP%29%20IOU.gns3project) using **File > Import portable project**. To open `ICMP Router Discovery Protocol (IRDP).gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Broccoli | FastEthernet0/0 | Ethernet0/0 |
| Broccoli | FastEthernet1/0 | Ethernet0/1 |
| Mustard | FastEthernet0/0 | Ethernet0/0 |
| Mustard | FastEthernet1/0 | Ethernet0/1 |
| Potato | FastEthernet0/0 | Ethernet0/0 |
| Potato | FastEthernet1/0 | Ethernet0/1 |
| Tomato | FastEthernet0/0 | Ethernet0/0 |
| Tomato | FastEthernet1/0 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-icmp-router-discovery-protocol-irdp.png)

## Video Solution

- [YouTube Video Solution](http://www.youtube.com/watch?v=WvPGdf0bueA)
