# NAT Overlapping Networks

## Scenario

Fruity international has bought Juicy Corporate and is merging the companies into a new one called "Fruity Juicy". You are the network engineer responsible for the network migration. Unfortunately both networks are using the same address space so you'll have to use NAT temporarily so you can do an IP address migration somewhere in the future.

## Goal

- All IP addresses have been preconfigured for you.
- Ensure router Banana and Apple can communicate with each other without changing any IP address.

## GNS3 2.2.56.1

Import [nat-overlapping-networks IOU.gns3project](nat-overlapping-networks%20IOU.gns3project) using **File > Import portable project**. To open `nat-overlapping-networks.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Kiwi | FastEthernet0/0 | Ethernet0/0 |
| Kiwi | FastEthernet1/0 | Ethernet0/1 |
| Apple | FastEthernet0/0 | Ethernet0/0 |
| Apple | FastEthernet0/1 | Ethernet0/1 |
| Banana | FastEthernet0/0 | Ethernet0/0 |
| Pineapple | FastEthernet0/0 | Ethernet0/0 |
| Pineapple | FastEthernet1/0 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-nat-overlapping-networks.png)

## Video Solution

[Video Tutorial](http://www.youtube.com/watch?v=Srca-sbtBv0)
