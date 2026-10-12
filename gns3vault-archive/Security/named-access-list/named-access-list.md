# Named Access-List

## Scenario

After configuring standard and extended access-lists for the agents of three well-known agencies you were promoted to junior security operator. It's now time to upgrade your skills and show them how to implement named access-lists.

## Goal

- All IP addresses have been configured for you, look at the topology picture for the IP addresses.
- OSPF has been configured for full connectivity.
- All routers are running services like HTTP, HTTPS, TELNET and SSH.
- Make sure you use the most specific wildcard for all your access-lists.
- You are not allowed to use numbered access-lists, only named access-lists.
- Configure the network so users from router NSA's L1 interface are not allowed to reach the HTTPS server on router CIA's L2 interface.
- Configure the network so nobody is allowed to reach HTTP servers on router NSA except the L2 interface on router FBI.
- Configure the network so users from router NSA's L0 interface are allowed to reach the HTTPS server on router CIA's L2 interface.
- Configure the network so users from router CIA's L2 interface are not allowed to SSH into router FBI's 222.222.222.222 IP address.

## Topology

![Network Topology](./topology-named-access-list.png)

## Video Solution

[Video Solution on YouTube](http://www.youtube.com/watch?v=hnrcI_ebk3I)

## GNS3 2.2.56.1

Import [named-acl-startup-configs IOU.gns3project](named-acl-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `named-acl-startup-configs.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| CIA | FastEthernet0/0 | Ethernet0/0 |
| CIA | FastEthernet0/1 | Ethernet0/1 |
| FBI | FastEthernet0/0 | Ethernet0/0 |
| FBI | FastEthernet0/1 | Ethernet0/1 |
| NSA | FastEthernet0/0 | Ethernet0/0 |
| NSA | FastEthernet0/1 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.
