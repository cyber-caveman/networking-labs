# MST (Multiple Spanning Tree)

![Network Topology](./topology-mst-multiple-spanning-tree.png)

## Scenario:



You are a master of spanning tree and specialized in migration scenarios. Corkscrew inc. is one of your customers and they are having issues with their switches. There are many VLANs in the network and you would like to reduce the number of spanning tree calculations. As a result you decide to implement MST (Multiple Spanning Tree) for them.

## Goal:

* Configure all switches to use MST.
* Configure VLAN 10,20,30,40,50 and 60 on all switches.
* Configure VLAN 10,20 and 30 to use instance 1 for the spanning tree calculation.
* Configure VLAN 40,50 and 60 to use instance 2 for the spanning tree calculation.
* Configure SW1 to be the root bridge for the CIST.
* Configure SW2 to be the root bridge for instance 2.

## GNS3 2.2.56.1

Import [mst-multiple-spanning-tree IOU.gns3project](mst-multiple-spanning-tree%20IOU.gns3project) using **File > Import portable project**. To open `mst-multiple-spanning-tree.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

CLI switches explicitly select PVST when the source relies on that default. Converted EtherSwitch routers retain their default IP-routing state and routed FastEthernet0 ports. Use the IOU names below when following old interface references in the instructions and diagrams.

| Device | Source interface | Current interface |
| --- | --- | --- |
| SW1 | FastEthernet0/13 | Ethernet0/0 |
| SW1 | FastEthernet0/14 | Ethernet0/1 |
| SW1 | FastEthernet0/16 | Ethernet0/2 |
| SW1 | FastEthernet0/17 | Ethernet0/3 |
| SW2 | FastEthernet0/13 | Ethernet0/0 |
| SW2 | FastEthernet0/14 | Ethernet0/1 |
| SW2 | FastEthernet0/16 | Ethernet0/2 |
| SW2 | FastEthernet0/17 | Ethernet0/3 |
| SW3 | FastEthernet0/13 | Ethernet0/0 |
| SW3 | FastEthernet0/14 | Ethernet0/1 |
| SW3 | FastEthernet0/16 | Ethernet0/2 |
| SW3 | FastEthernet0/17 | Ethernet0/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology:

## Video Solution:

http://www.youtube.com/watch?v=LVN_43nzYF0
