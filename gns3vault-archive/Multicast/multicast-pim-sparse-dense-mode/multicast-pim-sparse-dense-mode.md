# Multicast PIM Sparse-Dense Mode

![Network Topology](./topology-multicast-pim-sparse-dense-mode.jpg)

## Scenario

As a volunteer working at a huge Monkey Reserve located in The Netherlands you decide to capture videos of all the monkeys and send them over the network to interested paying customers. This way you can aid the Reserve with some of the financial problems they have been dealing with...time for some Monkey Business!

## Goal

- All IP addresses have been preconfigured for you.
- Configure OSPF on all routers, advertise all networks. Achieve full connectivity.
- Configure sparse-dense-mode multicast on all routers.
- Configure all routers manually so that router Gibbon is the Rendezvous Point (RP) only for the 224.4.4.4 multicast group. Use the loopback0 interface as the IP address for the RP.
- Configure router Drill to join the multicast group 224.4.4.4 on it's Fastethernet interface.
- Configure router Drill to join the multicast group 239.4.4.4 on it's Fastethernet interface.
- Make sure you can ping the 224.4.4.4 group address and 239.4.4.4 group address from router Orangutan.

## GNS3 2.2.56.1

Import [multicast-pim-sparse-dense-startup-configs IOU.gns3project](multicast-pim-sparse-dense-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `multicast-pim-sparse-dense-startup-configs.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Chimpanzee | FastEthernet0/0 | Ethernet0/0 |
| Chimpanzee | FastEthernet1/0 | Ethernet0/1 |
| Drill | FastEthernet0/0 | Ethernet0/0 |
| Gibbon | FastEthernet0/0 | Ethernet0/0 |
| Gibbon | FastEthernet1/0 | Ethernet0/1 |
| Orangutan | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

## Video Solution

http://www.youtube.com/watch?v=rVHJf5RbK4A
