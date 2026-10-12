# PPP over Frame Relay

## Scenario

You are a network engineer specialized in frame-relay. The ISP you work for has a new security policy and wants that all frame-relay connections run authentication. Unfortunately this is not possible so you prepare to configure PPP over frame-relay. Using PPP will ensure you can add authentication in the future.

## Goal

- All IP addresses have been preconfigured for you.
- Configure a virtual template on router Compact and Decrease and configure network 192.168.23.0 /24 on it.
- Configure the serial0/0 interfaces for frame relay and use the virtual-template and PPP.
- Ensure router Jack and Emma can ping each other through the PPP over frame relay network.

## GNS3 2.2.56.1

Import [PPP over Frame Relay IOU.gns3project](PPP%20over%20Frame%20Relay%20IOU.gns3project) using **File > Import portable project**. To open `PPP over Frame Relay.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Compact | FastEthernet1/0 | Ethernet0/0 |
| Compact | Serial0/0 | Serial4/0 |
| Compact | Serial0/1 | Serial4/1 |
| Compact | Serial0/2 | Serial4/2 |
| Compact | Serial0/3 | Serial4/3 |
| Decrease | FastEthernet1/0 | Ethernet0/0 |
| Decrease | Serial0/0 | Serial4/0 |
| Decrease | Serial0/1 | Serial4/1 |
| Decrease | Serial0/2 | Serial4/2 |
| Decrease | Serial0/3 | Serial4/3 |
| Emma | FastEthernet0/0 | Ethernet0/0 |
| Jack | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-ppp-over-frame-relay.png)

## Video Solution

http://www.youtube.com/watch?v=U2FlZaBP-3s
