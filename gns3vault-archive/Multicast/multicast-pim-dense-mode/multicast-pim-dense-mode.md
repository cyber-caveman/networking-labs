# Multicast PIM Dense Mode

![Network Topology](./topology-multicast-pim-dense-mode.jpg)

## Scenario

You are working for a big Dutch company specialized in delivering Video-over-IP to their Customers. Since almost all customers are using their connection to receive video, the company decided to implement Multicast. To gain experience with the operation of Multicast they decided to implement Dense mode.

## Goal

- All IP addresses have been preconfigured for you.
- Configure OSPF on all routers, achieve full connectivity.
- Configure dense-mode multicast on all routers.
- Configure router Utrecht to join the multicast group 224.4.4.4 on its Fastethernet 1/0 interface.
- Ping this multicast group address from 224.4.4.4 from router Amsterdam to test your multicast configuration.

## GNS3 2.2.56.1

Import [multicast-pim-dense-mode-startup-configs IOU.gns3project](multicast-pim-dense-mode-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `multicast-pim-dense-mode-startup-configs.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Amsterdam | FastEthernet0/0 | Ethernet0/0 |
| Amsterdam | FastEthernet1/0 | Ethernet0/1 |
| Eindhoven | FastEthernet0/0 | Ethernet0/0 |
| Eindhoven | FastEthernet1/0 | Ethernet0/1 |
| Tilburg | FastEthernet0/0 | Ethernet0/0 |
| Tilburg | FastEthernet1/0 | Ethernet0/1 |
| Utrecht | FastEthernet0/0 | Ethernet0/0 |
| Utrecht | FastEthernet1/0 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

## Video Solution

[Video Solution on YouTube](http://www.youtube.com/watch?v=6sdaElU--8g)
