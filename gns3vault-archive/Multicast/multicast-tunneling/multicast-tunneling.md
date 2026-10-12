# Multicast Tunneling

![Network Topology](./topology-multicast-tunneling.jpg)

## Scenario

It's your first day in the army working as a networking professional. You are sent to a small international outpost to look after the network. It's a rather old network but they need you to install Multicast so they can stream audio in a efficient matter over the network. There is one problem though...there's one router that is so old that it doesn't support Multicast, let's check it out.

## Goal

- All IP addresses have been preconfigured for you.
- Configure OSPF on all routers, achieve full connectivity.
- You are allowed to configure dense-mode Multicast on all routers EXCEPT router Charlie.
- Configure router Echo to join the following multicast group: 224.1.1.1
- Start a ping from router Alpha to the multicast group address 224.1.1.1 to generate traffic.
- Make sure router Echo can receive the multicast stream without configuring multicast on router Charlie.

## GNS3 2.2.56.1

Import [multicast-tunneling-startup-configs IOU.gns3project](multicast-tunneling-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `multicast-tunneling-startup-configs.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Alpha | FastEthernet0/0 | Ethernet0/0 |
| Bravo | FastEthernet0/0 | Ethernet0/0 |
| Bravo | FastEthernet1/0 | Ethernet0/1 |
| Charlie | FastEthernet0/0 | Ethernet0/0 |
| Charlie | FastEthernet1/0 | Ethernet0/1 |
| Delta | FastEthernet0/0 | Ethernet0/0 |
| Delta | FastEthernet1/0 | Ethernet0/1 |
| Echo | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

## Video Solution

http://www.youtube.com/watch?v=Jm6sJLVj8NY
