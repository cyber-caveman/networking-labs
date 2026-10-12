# PVRST (Per VLAN Rapid Spanning Tree)

## Scenario



You are the network engineer for a company in Florida that is specialized in campus LAN designs. One of your customers is having issues with their network and it seems their spanning-tree topology has been misconfigured. The network has a number of non-Cisco devices so you need to run an IEEE version of spanning-tree.

## Goal

- Ensure all switches run PVRST.
- Create VLAN 10, 20 and 30 on all switches.
- Ensure SW1 is the root bridge for VLAN 10.
- Ensure SW2 is the root bridge for VLAN 20.
- Ensure SW3 is the root bridge for VLAN 30.
- Ensure SW2 prefers the path through SW3 to reach the root bridge in VLAN 10. You are only allowed to change the cost.
- Ensure SW3 prefers interface fa0/14 to reach the root bridge for VLAN 10. You are only allowed to change the port priority.
- Ensure the fa0/5 interface on all switches is seen as an edge port for PVRST.

## GNS3 2.2.56.1

Import [pvrst-per-vlan-rapid-spanning-tree IOU.gns3project](pvrst-per-vlan-rapid-spanning-tree%20IOU.gns3project) using **File > Import portable project**. To open `pvrst-per-vlan-rapid-spanning-tree.gns3` directly, keep it beside `project-files`.

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
| SW1 | FastEthernet0/5 | Ethernet1/0 |
| SW2 | FastEthernet0/13 | Ethernet0/0 |
| SW2 | FastEthernet0/14 | Ethernet0/1 |
| SW2 | FastEthernet0/16 | Ethernet0/2 |
| SW2 | FastEthernet0/17 | Ethernet0/3 |
| SW2 | FastEthernet0/5 | Ethernet1/0 |
| SW3 | FastEthernet0/13 | Ethernet0/0 |
| SW3 | FastEthernet0/14 | Ethernet0/1 |
| SW3 | FastEthernet0/16 | Ethernet0/2 |
| SW3 | FastEthernet0/17 | Ethernet0/3 |
| SW3 | FastEthernet0/5 | Ethernet1/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-pvrst-per-vlan-rapid-spanning-tree.png)

## Video Solution

http://www.youtube.com/watch?v=WivZPfRRrj0&
