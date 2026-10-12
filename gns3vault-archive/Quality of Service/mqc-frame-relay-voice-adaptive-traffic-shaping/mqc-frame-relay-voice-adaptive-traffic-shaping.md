# MQC Frame Relay Voice-Adaptive Traffic Shaping

## Scenario

As one of the network engineers for a large frame-relay provider in the US you are asked by your boss to configure QoS. Whenever there is congestion there is a certain amount that could be dropped from customers, it's up to you to configure it!

## Goal

* All IP addresses have been preconfigured for you.
* Configure router Kos so there is a priority queue of 64Kbps for VoIP packets on the frame-relay link.
* Configure router Kos so you don't exceed the CIR rate of 128Kbps when there are VoIP packets in the queue.

## GNS3 2.2.56.1

Import [mqc-frame-relay-voice-adaptive-traffic-shaping IOU.gns3project](mqc-frame-relay-voice-adaptive-traffic-shaping%20IOU.gns3project) using **File > Import portable project**. To open `mqc-frame-relay-voice-adaptive-traffic-shaping.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| James | FastEthernet0/0 | Ethernet0/0 |
| Jack | FastEthernet0/0 | Ethernet0/0 |
| Quall | FastEthernet0/0 | Ethernet0/0 |
| Quall | Serial1/0 | Serial4/0 |
| Quall | Serial1/1 | Serial4/1 |
| Quall | Serial1/2 | Serial4/2 |
| Quall | Serial1/3 | Serial4/3 |
| Kos | FastEthernet0/0 | Ethernet0/0 |
| Kos | Serial1/0 | Serial4/0 |
| Kos | Serial1/1 | Serial4/1 |
| Kos | Serial1/2 | Serial4/2 |
| Kos | Serial1/3 | Serial4/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-mqc-frame-relay-voice-adaptive-traffic-shaping.png)

## Video Solution

[Video Solution](http://www.youtube.com/watch?v=gR8IM_pdty0)
