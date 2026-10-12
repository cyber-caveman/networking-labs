# Payload Compression Serial Links

## Scenario

You are the owner of a small ISP company located in The Netherlands. Most of the equipment you have running is fairly old and you have multiple different serial links in use. Bandwidth is an issue and since you don't have the budget to replace any links you are looking for a cheaper solution...think you can compress things?

## Goal

- All IP addresses have been preconfigured for you.
- Configure PPP encapsulation between router Lloyd and Carter.
- Configure HDLC encapsulation between router Carter and Griggs.
- Configure frame-relay encapsulation between router Griggs and Wolner.
- Configure LZS compression on the PPP link.
- Configure STACKER compression on the HDLC link.
- Configure packet-by-packet compression on the frame-relay link.

## GNS3 2.2.56.1

Import [Payload Compression Serial Links IOU.gns3project](Payload%20Compression%20Serial%20Links%20IOU.gns3project) using **File > Import portable project**. To open `Payload Compression Serial Links.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Carter | Serial0/0 | Serial4/0 |
| Carter | Serial0/1 | Serial4/1 |
| Carter | Serial0/2 | Serial4/2 |
| Carter | Serial0/3 | Serial4/3 |
| Griggs | Serial0/0 | Serial4/0 |
| Griggs | Serial0/1 | Serial4/1 |
| Griggs | Serial0/2 | Serial4/2 |
| Griggs | Serial0/3 | Serial4/3 |
| Lloyd | Serial0/0 | Serial4/0 |
| Lloyd | Serial0/1 | Serial4/1 |
| Lloyd | Serial0/2 | Serial4/2 |
| Lloyd | Serial0/3 | Serial4/3 |
| Wolner | Serial0/0 | Serial4/0 |
| Wolner | Serial0/1 | Serial4/1 |
| Wolner | Serial0/2 | Serial4/2 |
| Wolner | Serial0/3 | Serial4/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-payload-compression-serial-links.png)

## Video Solution

[Payload Compression Serial Links Solution](http://www.youtube.com/watch?v=jwbp-Emjw_I)
