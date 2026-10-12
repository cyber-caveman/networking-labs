# GRE Tunnel Basic

![Network Topology](./topology-gre-tunnel-basic.jpg)

## Scenario

You are working for Company "BigLabs" and you have heard some colleague network engineers talk about VPN tunnels and how they were unable to send routing protocols across the VPN tunnels. You also heard that a GRE tunnel could possible solve this problem. Let's see what this is all about and lab it up!

## Goal

- Configure all IP addresses as specified in the topology picture.
- Configure a loopback interface on Router Godzilla and Nessie:
  - Godzilla: Loopback0: 1.1.1.1 /24
  - Nessie: Loopback0: 3.3.3.3 /24
- Configure EIGRP AS1 on all 3 routers, only advertise the 192.168.12.0 and 192.168.23.0 network, do not advertise the loopbacks.
- Ensure Router Godzilla and Nessie can ping each other.
- Configure a GRE tunnel between Router Godzilla and Nessie.
- Configure the 192.168.13.0 /24 network on the GRE tunnel:
  - Godzilla: 192.168.13.1
  - Nessie: 192.168.13.3
- Ensure you can ping the IP addresses that you configured on the tunnel interface.
- Configure another loopback interface on Router Godzilla and Nessie:
  - Godzilla: Loopback1: 11.11.11.11 /24
  - Nessie: Loopback1: 33.33.33.33 /24
- Configure OSPF and use network commands to advertise the network on the GRE tunnel.
- Advertise Loopback1 in OSPF on Router Godzilla and Nessie.
- Ensure you establish a OSPF neighbor relationship and that you see the loopback1 interfaces in the routing table.

## GNS3 2.2.56.1

Import [untitled IOU.gns3project](untitled%20IOU.gns3project) using **File > Import portable project**. To open `untitled.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Godzilla | FastEthernet0/0 | Ethernet0/0 |
| KingKong | FastEthernet1/0 | Ethernet0/0 |
| KingKong | FastEthernet0/0 | Ethernet0/1 |
| Nessie | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

## Video Solution

[Video Solution on YouTube](http://www.youtube.com/watch?v=TZ71eY0qpcY)
