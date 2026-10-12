# VLANs and Trunks

![Network Topology](./topology-vlans-and-trunks.png)

## Scenario:


**_You only need layer 2 switches for this lab. The Cisco Catalyst 2950 or higher will work._**

The school you work for has a flat network design and they only use layer 2 switches. One of the teachers built the network in his own time but he has no clue what he exactly did. There is only one VLAN and there have been issues with applications that generate too much broadcast traffic. It's up to you to segment the network and implement some VLANs.

## Goal:

- Create the following VLANs and configure the correct names:
  - VLAN 10: name Engineering
  - VLAN 20: name Marketing
  - VLAN 30: name Research
  - VLAN 40: name Sales
  - VLAN 50: name Management
- Configure fa0/1 on SW1 as an access interface in VLAN 10
- Configure fa0/2 on SW2 as an access interface in VLAN 20
- One of the links between SW1 and SW2 should use ISL encapsulation
- One of the links between SW2 and SW3 is not allowed to dynamically negotiate a trunking protocol
- One of the links between SW1 and SW3 should never send any DTP messages
- Only VLAN 1, 10 and VLAN 20 are allowed between SW1 and SW2
- Only VLAN 1, 10, 20, 40 and 50 are allowed between SW2 and SW3
- The native VLAN between SW1 and SW3 should be VLAN 50 on both links

## GNS3 2.2.56.1

Import [vlans-and-trunks IOU.gns3project](vlans-and-trunks%20IOU.gns3project) using **File > Import portable project**. To open `vlans-and-trunks.gns3` directly, keep it beside `project-files`.

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
| SW1 | FastEthernet0/1 | Ethernet1/0 |
| SW2 | FastEthernet0/13 | Ethernet0/0 |
| SW2 | FastEthernet0/14 | Ethernet0/1 |
| SW2 | FastEthernet0/16 | Ethernet0/2 |
| SW2 | FastEthernet0/17 | Ethernet0/3 |
| SW2 | FastEthernet0/15 | Ethernet1/0 |
| SW3 | FastEthernet0/13 | Ethernet0/0 |
| SW3 | FastEthernet0/14 | Ethernet0/1 |
| SW3 | FastEthernet0/16 | Ethernet0/2 |
| SW3 | FastEthernet0/17 | Ethernet0/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology:

## Video Solution:

[Video Solution on YouTube](http://www.youtube.com/watch?v=k8OwNfTtRpU&)
