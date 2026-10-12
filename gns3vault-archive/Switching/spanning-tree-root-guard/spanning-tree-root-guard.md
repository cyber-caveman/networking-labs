# Spanning Tree Root Guard

## Scenario



Medieval corporation is specialized in enhancing security for switched networks. You as one of the network engineers in the security team are working on a switched network of one of your customers. You want to enhance security by making sure the network will not accept any inferior root bridges.

## Goal

- Configure SW2 as the root bridge for VLAN 1.
- Configure SW3 to have a spanning tree priority of 4096 for VLAN 1.
- Ensure SW1 does not accept SW3 as a root bridge.

## GNS3 2.2.56.1

Import [spanning-tree-root-guard IOU.gns3project](spanning-tree-root-guard%20IOU.gns3project) using **File > Import portable project**. To open `spanning-tree-root-guard.gns3` directly, keep it beside `project-files`.

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
| SW3 | FastEthernet0/13 | Ethernet0/0 |
| SW3 | FastEthernet0/14 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-spanning-tree-root-guard.png)

## Video Solution

[Spanning Tree Root Guard Video](http://www.youtube.com/watch?v=dXGkJPw9xms)
