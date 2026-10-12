# IPv6 Tunneling over IPv4

## Scenario

You are the senior network designer for a large enterprise company specialized in exporting Fruit. The company has plans to upgrade their network and to ensure they are ready for the future they want to implement IPv6. The backbone of the network however is still based on IPv4 and you are not allowed to make any changes...let's see if you can achieve connectivity by tunneling...

## Goal

- All IPv4 and IPv6 addresses have been preconfigured for you.
- You are not allowed to make any changes to router Fruity.
- OSPFv2 has been configured in the IPv4 domain for connectivity between the routers.
- Configure a IPv6 over IPv4 tunnel between router Banana and Apple. You are allowed to use the 3000::/64 prefix for the tunnel interface.
- Enable RIPNG on router Melon, Banana, Apple and Kiwi.
- Ensure you have full connectivity between the 2000::/64 and 4000::/64 network.

## GNS3 2.2.56.1

Import [IPv6 Tunneling over IPv4 IOU.gns3project](IPv6%20Tunneling%20over%20IPv4%20IOU.gns3project) using **File > Import portable project**. To open `IPv6 Tunneling over IPv4.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Apple | FastEthernet0/0 | Ethernet0/0 |
| Apple | FastEthernet1/0 | Ethernet0/1 |
| Banana | FastEthernet0/0 | Ethernet0/0 |
| Banana | FastEthernet1/0 | Ethernet0/1 |
| Fruity | FastEthernet0/0 | Ethernet0/0 |
| Fruity | FastEthernet1/0 | Ethernet0/1 |
| Kiwi | FastEthernet0/0 | Ethernet0/0 |
| Melon | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-ipv6-tunneling-over-ipv4.png)

## Video Solution

[Video: IPv6 Tunneling over IPv4](http://www.youtube.com/watch?v=w24mG5WtjUM)
