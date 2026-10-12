# Spanning Tree Loop Guard

![Network Topology](./topology-spanning-tree-loop-guard.png)

## Scenario:



The network agency corporation has hired you as a spanning tree specialist. One of their customers has issues with a switched network that only has fiber connections. Every now and then there's a problem with the fiber and as a result layer 2 loops occur. It will take two months for the fiber company to check all cables/connectors so you want a temporary solution...

## Goal:

- Configure SW1 so it is the root bridge for VLAN 1.
- Configure your spanning-tree topology so the fa0/16 interface on SW3 becomes an alternate port.
- Configure the fa0/16 interface on SW2 so it does not send or receive any BPDUs. This will cause a loop.
- Configure all switches so this loop will be detected and SW3 will shut its fa0/16 interface.

## GNS3 2.2.56.1

Import [spanning-tree-loop-guard IOU.gns3project](spanning-tree-loop-guard%20IOU.gns3project) using **File > Import portable project**. To open `spanning-tree-loop-guard.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

CLI switches explicitly select PVST when the source relies on that default. Converted EtherSwitch routers retain their default IP-routing state and routed FastEthernet0 ports. Use the IOU names below when following old interface references in the instructions and diagrams.

| Device | Source interface | Current interface |
| --- | --- | --- |
| SW1 | FastEthernet0/14 | Ethernet0/0 |
| SW1 | FastEthernet0/17 | Ethernet0/1 |
| SW2 | FastEthernet0/14 | Ethernet0/0 |
| SW2 | FastEthernet0/16 | Ethernet0/1 |
| SW3 | FastEthernet0/14 | Ethernet0/0 |
| SW3 | FastEthernet0/16 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology:

## Video Solution:

http://www.youtube.com/watch?v=Do42S-_w8KU&
