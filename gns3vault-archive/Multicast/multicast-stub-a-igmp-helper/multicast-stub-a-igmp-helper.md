# Multicast Stub & IGMP Helper

![Network Topology](./topology-multicast-stub-a-igmp-helper.jpg)

## Scenario

Your career started in the 80's as a star in a famous action show, almost 30 years later your career is even more successful as a senior networking engineer. The company you are working for broadcasts old action series by using multicast, one of the branch offices however has performance problems with an old router. You need to make some changes to fix this, because you love it when a plan comes together...

## Goal

- All IP addresses have been preconfigured for you.
- Configure OSPF on all routers, advertise all networks. Achieve full connectivity.
- Configure router Receiver to join the multicast group 224.4.4.4 on it's Fastethernet interface.
- Configure dense-mode multicast between router VideoStation and BA.
- Configure dense-mode multicast between router BA and Murdock.
- Make sure router Receiver can receive the multicast stream, test this by sending a ping to 224.4.4.4 from router VideoStation.
- You are not allowed to form a PIM neighbor relationship between router BA and murdock.

## GNS3 2.2.56.1

Import [multicast-stub-igmp-helper-startup-configs IOU.gns3project](multicast-stub-igmp-helper-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `multicast-stub-igmp-helper-startup-configs.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| VideoStation | FastEthernet0/0 | Ethernet0/0 |
| BA | FastEthernet0/0 | Ethernet0/0 |
| BA | Serial1/0 | Serial4/0 |
| BA | Serial1/1 | Serial4/1 |
| BA | Serial1/2 | Serial4/2 |
| BA | Serial1/3 | Serial4/3 |
| Murdock | FastEthernet1/0 | Ethernet0/0 |
| Murdock | Serial0/0 | Serial4/0 |
| Murdock | Serial0/1 | Serial4/1 |
| Murdock | Serial0/2 | Serial4/2 |
| Murdock | Serial0/3 | Serial4/3 |
| Receiver | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

## Video Solution

http://www.youtube.com/watch?v=rLG45ALJya8
