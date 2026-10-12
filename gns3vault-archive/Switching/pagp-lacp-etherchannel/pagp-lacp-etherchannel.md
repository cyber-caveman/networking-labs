# PAgP LACP Etherchannel

## Scenario



You are a master of spanning tree and specialized in migration scenarios. Corkscrew inc. is one of your customers and they are having issues with their switches. There are many VLANs in the network and you would like to reduce the number of spanning tree calculations. As a result you decide to implement MST (Multiple Spanning Tree) for them.

## Goal

- Configure PAgP between SW1 and SW2. SW1 should actively try to form an Etherchannel and SW2 should only respond to requests.
- Configure LACP between SW1 and SW3. SW1 should actively try to form an Etherchannel and SW3 should only respond to requests.
- Configure an Etherchannel between SW2 and SW3. You are not allowed to use any protocol for negotiation.
- Configure the etherchannel between SW1 and SW2 to use destination MAC address load-balancing.

## GNS3 2.2.56.1

Import [pagp-lacp-etherchannel IOU.gns3project](pagp-lacp-etherchannel%20IOU.gns3project) using **File > Import portable project**. To open `pagp-lacp-etherchannel.gns3` directly, keep it beside `project-files`.

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
| SW1 | FastEthernet0/2 | Ethernet1/1 |
| SW1 | FastEthernet0/3 | Ethernet1/2 |
| SW1 | FastEthernet0/4 | Ethernet1/3 |
| SW1 | FastEthernet0/5 | Ethernet2/0 |
| SW1 | FastEthernet0/6 | Ethernet2/1 |
| SW1 | FastEthernet0/7 | Ethernet2/2 |
| SW1 | FastEthernet0/8 | Ethernet2/3 |
| SW1 | FastEthernet0/9 | Ethernet3/0 |
| SW1 | FastEthernet0/10 | Ethernet3/1 |
| SW1 | FastEthernet0/11 | Ethernet3/2 |
| SW1 | FastEthernet0/12 | Ethernet3/3 |
| SW2 | FastEthernet0/13 | Ethernet0/0 |
| SW2 | FastEthernet0/14 | Ethernet0/1 |
| SW2 | FastEthernet0/16 | Ethernet0/2 |
| SW2 | FastEthernet0/17 | Ethernet0/3 |
| SW2 | FastEthernet0/1 | Ethernet1/0 |
| SW2 | FastEthernet0/2 | Ethernet1/1 |
| SW2 | FastEthernet0/3 | Ethernet1/2 |
| SW2 | FastEthernet0/4 | Ethernet1/3 |
| SW2 | FastEthernet0/5 | Ethernet2/0 |
| SW2 | FastEthernet0/6 | Ethernet2/1 |
| SW2 | FastEthernet0/7 | Ethernet2/2 |
| SW2 | FastEthernet0/8 | Ethernet2/3 |
| SW2 | FastEthernet0/9 | Ethernet3/0 |
| SW2 | FastEthernet0/10 | Ethernet3/1 |
| SW2 | FastEthernet0/11 | Ethernet3/2 |
| SW2 | FastEthernet0/12 | Ethernet3/3 |
| SW3 | FastEthernet0/13 | Ethernet0/0 |
| SW3 | FastEthernet0/14 | Ethernet0/1 |
| SW3 | FastEthernet0/16 | Ethernet0/2 |
| SW3 | FastEthernet0/17 | Ethernet0/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-pagp-lacp-etherchannel.png)

## Video Solution

[YouTube Video](http://www.youtube.com/watch?v=SohMnr_H4R4)
