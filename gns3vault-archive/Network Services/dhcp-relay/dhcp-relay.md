# DHCP Relay

## Scenario

You used to have a DHCP server for each VLAN but this wasn't much of a scalable solution. You decide to get rid of all the DHCP servers and install a single DHCP server in the datacenter. You see that the clients are sending DHCP discover messages but they are not reaching the DHCP server, up to you to relay some packets...

## Goal

- All IPv4 addresses have been preconfigured for you.
- Configure router Odin as a DHCP server.
- Ensure router Loki and Frey can get an IP address from the DHCP server.

## GNS3 2.2.56.1

Import [DHCP Relay IOU.gns3project](DHCP%20Relay%20IOU.gns3project) using **File > Import portable project**. To open `DHCP Relay.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Frey | FastEthernet0/0 | Ethernet0/0 |
| Loki | FastEthernet0/0 | Ethernet0/0 |
| Odin | FastEthernet0/0 | Ethernet0/0 |
| Thor | FastEthernet0/0 | Ethernet0/0 |
| Thor | FastEthernet1/0 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-dhcp-relay.png)

## Video Solution

http://www.youtube.com/watch?v=V-0ubwujny4
