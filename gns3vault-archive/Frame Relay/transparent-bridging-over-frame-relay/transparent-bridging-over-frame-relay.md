# Transparent Bridging over Frame Relay

## Scenario

Your work for a large ISP that still has some old frame-relay equipment. One of your customers wants their sites to be directly connected. Since you know frame relay pretty well you know you can setup some bridging.

## Goal

* All IP addresses have been preconfigured for you.
* Enable frame relay encapsulation on the serial0/0 interfaces of router Compact and Decrease.
* Configure a bridge group on router Compact and Decrease, use IEEE. Apply the bridge group to the serial0/0 interfaces.
* Ensure router Jack and Emma can ping each other and that they have multicast and broadcast capabilities.

## GNS3 2.2.56.1

Import [Transparent Bridging over Frame Relay IOU.gns3project](Transparent%20Bridging%20over%20Frame%20Relay%20IOU.gns3project) using **File > Import portable project**. To open `Transparent Bridging over Frame Relay.gns3` directly, keep it beside `project-files`.

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

![Network Topology](./topology-transparent-bridging-over-frame-relay.png)

## Video Solution

[http://www.youtube.com/watch?v=J0epdnR5DY4](http://www.youtube.com/watch?v=J0epdnR5DY4)
