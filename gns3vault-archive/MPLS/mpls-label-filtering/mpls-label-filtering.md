# MPLS Label Filtering

![Network Topology](./topology-mpls-label-filtering.jpg)

## Scenario

Your MPLS Backbone works like a charm but your security officer still has some issues. He doesn't like that some of the prefixes are advertised with a label and it's up to you to fix it....bring on the sticker remover!

## Goal

* All IP addresses on the customer routers have been preconfigured for you.
* OSPF has been configured on all routers and all networks are advertised.
* Configure MPLS on all routers, ensure all prefixes are advertised with a label.
* The prefixes on the loopback interfaces should NOT be advertised with a label.

## GNS3 2.2.56.1

Import [MPLS Label Filtering IOU.gns3project](MPLS%20Label%20Filtering%20IOU.gns3project) using **File > Import portable project**. To open `MPLS Label Filtering.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Shepard | FastEthernet0/0 | Ethernet0/0 |
| Mordin | FastEthernet0/0 | Ethernet0/0 |
| Mordin | FastEthernet1/0 | Ethernet0/1 |
| Garrus | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

## Video Solution

[YouTube Video](http://www.youtube.com/watch?v=_vkCmt9MEq4)
