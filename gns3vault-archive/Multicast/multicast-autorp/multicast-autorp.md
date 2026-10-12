# Multicast Auto-RP

## Scenario

You are a network engineer and responsible for the main network of Gotham City. Multicast will be needed to send video replays throughout the city, and to decrease network load your boss has decided that you need to implement sparse-dense-mode. The network will be fairly large, so you don't want to configure the RP address manually on every router, let's see if there's an easier way...

## Goal

* All IP addresses have been preconfigured for you.
* Configure OSPF on all routers, advertise all networks. Achieve full connectivity.
* Configure sparse-dense-mode multicast on all routers.
* Configure AutoRP so router Joker is the Rendezvous Point (RP), use the loopback0 interface.
* Configure AutoRP so router Catwoman is the mapping agent (MP), use the loopback0 interface.
* Configure router Batman to join the multicast group 224.4.4.4 on it's Fastethernet interface.
* Make sure you can ping the 224.4.4.4 group address from router Catwoman.

## GNS3 2.2.56.1

Import [multicast-auto-rp-startup-configs IOU.gns3project](multicast-auto-rp-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `multicast-auto-rp-startup-configs.gns3` directly, keep it beside `project-files`.

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
| MrFreeze | FastEthernet0/0 | Ethernet0/0 |
| MrFreeze | FastEthernet1/0 | Ethernet0/1 |
| Batman | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-multicast-autorp.png)

## Video Solution

http://www.youtube.com/watch?v=KKdq07MqLB0
