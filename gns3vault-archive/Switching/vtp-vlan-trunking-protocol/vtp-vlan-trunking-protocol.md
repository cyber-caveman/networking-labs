# VTP - Vlan Trunking Protocol

![Network Topology](./topology-vtp-vlan-trunking-protocol.jpg)

## Scenario


You are working as a trainee at a large African safari company and acquired the task of setting up VTP (Vlan Trunking Protocol). You need to create a bunch of VLANS and it would be a shame if you had to do everything by hand, let's see if you can find a faster and more scalable solution.

## Goals

- Create the following VLANS on switch Bobcat:
  - VLAN 10: name Tigers
  - VLAN 20: name Lions
  - VLAN 30: name Panthers
- Configure the interfaces between the switches as trunks.
- Configure switch Bobcat to be the VTP server.
- Configure switch Panther to be a VTP client.
- Configure switch Tiger so it does not synchronise itself to the latest VTP information, it should forward advertisements to switch Panther though.
- Change the VTP domain name to "GNS3Vault".
- Use the password "Vault" for VTP.
- Make sure there is no unnecessary vlan traffic flooded on the trunk links.

## GNS3 2.2.56.1

Import [vtp-vlan-trunking-protocol IOU.gns3project](vtp-vlan-trunking-protocol%20IOU.gns3project) using **File > Import portable project**. To open `vtp-vlan-trunking-protocol.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

CLI switches explicitly select PVST when the source relies on that default. Converted EtherSwitch routers retain their default IP-routing state and routed FastEthernet0 ports. Use the IOU names below when following old interface references in the instructions and diagrams.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Tiger | FastEthernet1/0 | Ethernet0/0 |
| Tiger | FastEthernet1/1 | Ethernet0/1 |
| Tiger | FastEthernet0/0 | Ethernet0/2 |
| Tiger | FastEthernet0/1 | Ethernet0/3 |
| Tiger | FastEthernet1/2 | Ethernet1/0 |
| Tiger | FastEthernet1/3 | Ethernet1/1 |
| Tiger | FastEthernet1/4 | Ethernet1/2 |
| Tiger | FastEthernet1/5 | Ethernet1/3 |
| Tiger | FastEthernet1/6 | Ethernet2/0 |
| Tiger | FastEthernet1/7 | Ethernet2/1 |
| Tiger | FastEthernet1/8 | Ethernet2/2 |
| Tiger | FastEthernet1/9 | Ethernet2/3 |
| Tiger | FastEthernet1/10 | Ethernet3/0 |
| Tiger | FastEthernet1/11 | Ethernet3/1 |
| Tiger | FastEthernet1/12 | Ethernet3/2 |
| Tiger | FastEthernet1/13 | Ethernet3/3 |
| Bobcat | FastEthernet1/0 | Ethernet0/0 |
| Bobcat | FastEthernet0/0 | Ethernet0/1 |
| Bobcat | FastEthernet0/1 | Ethernet0/2 |
| Bobcat | FastEthernet1/1 | Ethernet0/3 |
| Bobcat | FastEthernet1/2 | Ethernet1/0 |
| Bobcat | FastEthernet1/3 | Ethernet1/1 |
| Bobcat | FastEthernet1/4 | Ethernet1/2 |
| Bobcat | FastEthernet1/5 | Ethernet1/3 |
| Bobcat | FastEthernet1/6 | Ethernet2/0 |
| Bobcat | FastEthernet1/7 | Ethernet2/1 |
| Bobcat | FastEthernet1/8 | Ethernet2/2 |
| Bobcat | FastEthernet1/9 | Ethernet2/3 |
| Bobcat | FastEthernet1/10 | Ethernet3/0 |
| Bobcat | FastEthernet1/11 | Ethernet3/1 |
| Bobcat | FastEthernet1/12 | Ethernet3/2 |
| Bobcat | FastEthernet1/13 | Ethernet3/3 |
| Panther | FastEthernet1/0 | Ethernet0/0 |
| Panther | FastEthernet0/0 | Ethernet0/1 |
| Panther | FastEthernet0/1 | Ethernet0/2 |
| Panther | FastEthernet1/1 | Ethernet0/3 |
| Panther | FastEthernet1/2 | Ethernet1/0 |
| Panther | FastEthernet1/3 | Ethernet1/1 |
| Panther | FastEthernet1/4 | Ethernet1/2 |
| Panther | FastEthernet1/5 | Ethernet1/3 |
| Panther | FastEthernet1/6 | Ethernet2/0 |
| Panther | FastEthernet1/7 | Ethernet2/1 |
| Panther | FastEthernet1/8 | Ethernet2/2 |
| Panther | FastEthernet1/9 | Ethernet2/3 |
| Panther | FastEthernet1/10 | Ethernet3/0 |
| Panther | FastEthernet1/11 | Ethernet3/1 |
| Panther | FastEthernet1/12 | Ethernet3/2 |
| Panther | FastEthernet1/13 | Ethernet3/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

## Video Solution

http://www.youtube.com/watch?v=NFgqDU0-3hc
