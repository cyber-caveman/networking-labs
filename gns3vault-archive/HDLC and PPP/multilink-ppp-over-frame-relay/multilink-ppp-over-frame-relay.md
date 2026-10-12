# Multilink PPP over Frame Relay

## Scenario

You are the senior network engineer working at a major frame relay ISP somewhere in Europe. One of your customers requests the company to run authentication over their frame relay connections and they would also like to see fragmentation. You know there is no way to do authentication with frame-relay so you decide to bundle their PVCs in a multilink PPP setup.

## Goals

- There are two PVCs using DLCI 102 + 201 and DLCI 112 + 211.
- Configure Multilink PPP to run over both PVCs. Use network 192.168.12.0 /24.
- Ensure packets will be fragmented on both serial links.
- Configure CHAP authentication for the PPP Multilink configuration.
- Ensure both routers can reach each others loopback0 interfaces through the PPP Multilink.

## GNS3 2.2.56.1

Import [PPP Multilink over Frame Relay IOU.gns3project](PPP%20Multilink%20over%20Frame%20Relay%20IOU.gns3project) using **File > Import portable project**. To open `PPP Multilink over Frame Relay.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Frank | Serial0/0 | Serial4/0 |
| Frank | Serial0/1 | Serial4/1 |
| Frank | Serial0/2 | Serial4/2 |
| Frank | Serial0/3 | Serial4/3 |
| Pim | Serial0/0 | Serial4/0 |
| Pim | Serial0/1 | Serial4/1 |
| Pim | Serial0/2 | Serial4/2 |
| Pim | Serial0/3 | Serial4/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-multilink-ppp-over-frame-relay.png)

## Video Solution

[YouTube Video Solution](http://www.youtube.com/watch?v=U6iM3jM_gVI)
