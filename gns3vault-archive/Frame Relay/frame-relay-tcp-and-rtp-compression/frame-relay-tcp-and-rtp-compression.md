# Frame Relay TCP and RTP compression

## Scenario

You are working at a frame relay provider as the senior network engineer. One of your customers has two PVCs and they are running a lot of TCP and RTP sessions through your frame relay network. The PVCs only have a CIR of 64kbps and you have plenty of CPU power on router Compact and Decrease. Let's see what you can squeeze out of those packets...

## Goal

- All IP addresses have been preconfigured for you.
- Configure two point-to-point subinterfaces for frame relay on router Compact and Decrease.
- Use network 192.168.23.0 /24 for DLCI 102 - 201.
- Use network 192.168.32.0 /24 for DLCI 112 - 221.
- Ensure traffic to router Jack uses network 192.168.23.0 /24 for the next-hop.
- Ensure traffic to router Emma uses network 192.168.32.0 /24 for the next-hop.
- Enable RTP compression for the PVC with DLCI 102 - 201.
- Enable TCP compression for the PVC with DLCI 112 - 221.

## GNS3 2.2.56.1

Import [Frame Relay TCP and RTP compression IOU.gns3project](Frame%20Relay%20TCP%20and%20RTP%20compression%20IOU.gns3project) using **File > Import portable project**. To open `Frame Relay TCP and RTP compression.gns3` directly, keep it beside `project-files`.

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

![Network Topology](./topology-frame-relay-tcp-and-rtp-compression.png)

## Video Solution

[YouTube Video: Frame Relay TCP and RTP Compression](http://www.youtube.com/watch?v=xQCrEdV--DU)
