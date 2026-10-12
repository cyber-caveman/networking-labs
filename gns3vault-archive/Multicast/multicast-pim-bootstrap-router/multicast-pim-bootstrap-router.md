# Multicast PIM Bootstrap Router

![Network Topology](./topology-multicast-pim-bootstrap-router.jpg)

## Scenario

You are a network engineer and responsible for the main network of Gotham City. Multicast will be needed to send video replays throughout the city, and to decrease network load your boss has decided that you need to implement sparse-dense-mode. The network will be fairly large, so you don't want to configure the RP address manually on every router, the network might contain non-Cisco router in the future so you'll need to use a standards-based protocol.

## Goal

- All IP addresses on the physical interfaces have been preconfigured for you.
- Configure a loopback interface on router Joker:
  Loopback0: 2.2.2.2/32
- Configure a loopback interface on router Robin:
  Loopback0: 3.3.3.3/32
- Configure a loopback interface on router Batman:
  Loopback0: 4.4.4.4/32
- Configure OSPF on all routers, advertise all networks. Achieve full connectivity.
- Configure sparse-dense-mode multicast on all routers.
- Configure Bootstrap so router Joker is the Rendezvous Point (RP), use the loopback0 interface.
- Configure router Batman to join the multicast group 224.4.4.4 on it's loopback0 interface.
- Make sure you can ping the 224.4.4.4 group address from router Catwoman.

## GNS3 2.2.56.1

Import [multicast-pim-bootstrap-startup-configs IOU.gns3project](multicast-pim-bootstrap-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `multicast-pim-bootstrap-startup-configs.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Catwoman | FastEthernet0/0 | Ethernet0/0 |
| Joker | FastEthernet0/0 | Ethernet0/0 |
| Joker | FastEthernet1/0 | Ethernet0/1 |
| Robin | FastEthernet0/0 | Ethernet0/0 |
| Robin | FastEthernet1/0 | Ethernet0/1 |
| Batman | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

## Video Solution

[View Solution on YouTube](http://www.youtube.com/watch?v=CNcu2vAi7HY)
