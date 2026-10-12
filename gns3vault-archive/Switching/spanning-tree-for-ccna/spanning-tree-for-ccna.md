# Spanning Tree for CCNA

## Scenario

You are the leading network engineer of an international reptile and insects museum. Recently the museum has been experiencing trouble with their switched network due to loops. Up to you to optimize the spanning tree configuration!

## Goal

- Create VLAN 10, 20, 30 and 40 on all switches.
- Who is the root bridge for VLAN 10 and why?
- Make sure switch Ant is the root bridge for VLAN 10, switch Bee should be the backup in case switch Ant fails. You are not allowed to use the priority command.
- Make sure switch Bee is the root bridge for VLAN 20, switch Ant should be the backup in case switch Bee fails. You are not allowed to use the priority command.
- Make sure switch Butterfly is the root bridge for VLAN 30, switch Grasshopper should be the backup in case switch Butterfly fails. You are not allowed to use the spanning-tree root command.
- Make sure switch Grasshopper is the root bridge for VLAN 40, switch Butterfly should be the backup in case switch Butterfly fails. You are not allowed to use the spanning-tree root command.
- Change the hello timer on all switches for VLAN 10 to 4 seconds.
- Make sure switch Grasshopper does not use FastEthernet 1/1 to reach the root bridge in VLAN 10, you are not allowed to shutdown the interfaces.
- Make sure switch Grasshopper uses FastEthernet 1/3 to reach the root bridge in VLAN 20.
- In the future there will be a workstation connected to switch Bee's FastEthernet f1/4. Make sure it goes to forwarding mode immediately.

---

## GNS3 2.2.56.1

Import [spanning-tree-for-ccna IOU.gns3project](spanning-tree-for-ccna%20IOU.gns3project) using **File > Import portable project**. To open `spanning-tree-for-ccna.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

CLI switches explicitly select PVST when the source relies on that default. Converted EtherSwitch routers retain their default IP-routing state and routed FastEthernet0 ports. Use the IOU names below when following old interface references in the instructions and diagrams.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Butterfly | FastEthernet1/0 | Ethernet0/0 |
| Butterfly | FastEthernet1/1 | Ethernet0/1 |
| Butterfly | FastEthernet0/0 | Ethernet0/2 |
| Butterfly | FastEthernet0/1 | Ethernet0/3 |
| Butterfly | FastEthernet1/8 | Ethernet1/0 |
| Butterfly | FastEthernet1/9 | Ethernet1/1 |
| Butterfly | FastEthernet1/10 | Ethernet1/2 |
| Butterfly | FastEthernet1/11 | Ethernet1/3 |
| Butterfly | FastEthernet1/12 | Ethernet2/0 |
| Butterfly | FastEthernet1/13 | Ethernet2/1 |
| Butterfly | FastEthernet1/14 | Ethernet2/2 |
| Butterfly | FastEthernet1/15 | Ethernet2/3 |
| Butterfly | FastEthernet1/2 | Ethernet3/0 |
| Butterfly | FastEthernet1/3 | Ethernet3/1 |
| Butterfly | FastEthernet1/4 | Ethernet3/2 |
| Butterfly | FastEthernet1/5 | Ethernet3/3 |
| Grasshopper | FastEthernet1/0 | Ethernet0/0 |
| Grasshopper | FastEthernet1/1 | Ethernet0/1 |
| Grasshopper | FastEthernet1/3 | Ethernet0/2 |
| Grasshopper | FastEthernet0/0 | Ethernet0/3 |
| Grasshopper | FastEthernet0/1 | Ethernet1/0 |
| Grasshopper | FastEthernet1/8 | Ethernet1/1 |
| Grasshopper | FastEthernet1/9 | Ethernet1/2 |
| Grasshopper | FastEthernet1/10 | Ethernet1/3 |
| Grasshopper | FastEthernet1/11 | Ethernet2/0 |
| Grasshopper | FastEthernet1/12 | Ethernet2/1 |
| Grasshopper | FastEthernet1/13 | Ethernet2/2 |
| Grasshopper | FastEthernet1/14 | Ethernet2/3 |
| Grasshopper | FastEthernet1/15 | Ethernet3/0 |
| Grasshopper | FastEthernet1/2 | Ethernet3/1 |
| Grasshopper | FastEthernet1/4 | Ethernet3/2 |
| Grasshopper | FastEthernet1/5 | Ethernet3/3 |
| Bee | FastEthernet1/1 | Ethernet0/0 |
| Bee | FastEthernet1/2 | Ethernet0/1 |
| Bee | FastEthernet1/3 | Ethernet0/2 |
| Bee | FastEthernet0/0 | Ethernet0/3 |
| Bee | FastEthernet0/1 | Ethernet1/0 |
| Bee | FastEthernet1/9 | Ethernet1/1 |
| Bee | FastEthernet1/10 | Ethernet1/2 |
| Bee | FastEthernet1/11 | Ethernet1/3 |
| Bee | FastEthernet1/12 | Ethernet2/0 |
| Bee | FastEthernet1/13 | Ethernet2/1 |
| Bee | FastEthernet1/14 | Ethernet2/2 |
| Bee | FastEthernet1/15 | Ethernet2/3 |
| Bee | FastEthernet1/0 | Ethernet3/0 |
| Bee | FastEthernet1/4 | Ethernet3/1 |
| Bee | FastEthernet1/5 | Ethernet3/2 |
| Bee | FastEthernet1/6 | Ethernet3/3 |
| Ant | FastEthernet1/1 | Ethernet0/0 |
| Ant | FastEthernet1/2 | Ethernet0/1 |
| Ant | FastEthernet0/0 | Ethernet0/2 |
| Ant | FastEthernet0/1 | Ethernet0/3 |
| Ant | FastEthernet1/8 | Ethernet1/0 |
| Ant | FastEthernet1/9 | Ethernet1/1 |
| Ant | FastEthernet1/10 | Ethernet1/2 |
| Ant | FastEthernet1/11 | Ethernet1/3 |
| Ant | FastEthernet1/12 | Ethernet2/0 |
| Ant | FastEthernet1/13 | Ethernet2/1 |
| Ant | FastEthernet1/14 | Ethernet2/2 |
| Ant | FastEthernet1/15 | Ethernet2/3 |
| Ant | FastEthernet1/0 | Ethernet3/0 |
| Ant | FastEthernet1/3 | Ethernet3/1 |
| Ant | FastEthernet1/4 | Ethernet3/2 |
| Ant | FastEthernet1/5 | Ethernet3/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-spanning-tree-for-ccna.png)

## Video Solution

http://www.youtube.com/watch?v=QmR8ELpNUIw
