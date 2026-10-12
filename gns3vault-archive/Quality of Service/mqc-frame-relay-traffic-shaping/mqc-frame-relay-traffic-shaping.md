# MQC Frame-Relay Traffic Shaping

## Scenario

As one of the network engineers for a large frame-relay provider in the US you are asked by your boss to configure QoS. He wants you to get in shape by configuring traffic shaping for frame-relay. You are familiar with the old legacy solution but you need to use MQC for this one.

## Goal

- All IP addresses have been preconfigured for you.
- Configure router Kos so all traffic passing the frame-relay link has a CIR of 64Kbps.
- You are not allowed to enable frame-relay shaping on the physical interface.

## GNS3 2.2.56.1

Import [MQCFrameRelayTrafficShaping IOU.gns3project](MQCFrameRelayTrafficShaping%20IOU.gns3project) using **File > Import portable project**. To open `MQCFrameRelayTrafficShaping.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Jack | FastEthernet0/0 | Ethernet0/0 |
| James | FastEthernet0/0 | Ethernet0/0 |
| Kos | FastEthernet0/0 | Ethernet0/0 |
| Kos | Serial1/0 | Serial4/0 |
| Kos | Serial1/1 | Serial4/1 |
| Kos | Serial1/2 | Serial4/2 |
| Kos | Serial1/3 | Serial4/3 |
| Quall | FastEthernet0/0 | Ethernet0/0 |
| Quall | Serial1/0 | Serial4/0 |
| Quall | Serial1/1 | Serial4/1 |
| Quall | Serial1/2 | Serial4/2 |
| Quall | Serial1/3 | Serial4/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-mqc-frame-relay-traffic-shaping.png)

## Video Solution

[Video Solution on YouTube](http://www.youtube.com/watch?v=QP0z4x4GSrU)
