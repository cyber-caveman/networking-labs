# MQC Class-Based Traffic Shaping for Frame-Relay

## Scenario

You work for a large provider in India as a senior network engineer specialized in Quality of Service. All the customers of the service provider have an Ethernet connection which is capable of delivering speeds up to 10Mbps. The ISP has different subscriptions and you need to enforce that customers only get what they are paying for...time to get in shape!

## Goal

- All IP addresses have been preconfigured for you.
- Configure router Kos so telnet traffic for the PVC with DLCI 102 is shaped to an average of 128Kbps.
- Configure router Quall so http traffic for the PVC with DLCI 201 is shaped to a peak rate of 64Kbps.

## GNS3 2.2.56.1

Import [MQC Class-Based Traffic Shaping for Frame-Relay IOU.gns3project](MQC%20Class-Based%20Traffic%20Shaping%20for%20Frame-Relay%20IOU.gns3project) using **File > Import portable project**. To open `MQC Class-Based Traffic Shaping for Frame-Relay.gns3` directly, keep it beside `project-files`.

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

![Network Topology](./topology-mqc-class-based-traffic-shaping-for-frame-relay.png)

## Video Solution

[Video Solution on YouTube](http://www.youtube.com/watch?v=ixsMPfbUj4s)
