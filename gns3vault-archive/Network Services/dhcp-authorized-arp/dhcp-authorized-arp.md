# DHCP Authorized ARP

## Scenario

You work as a network engineer for a Hotel offering Internet access for an hourly rate. Recently you notice that some customers have been spoofing MAC and IP addresses to get free access by pretending they are another customer. After kicking them out of the hotel you decide to make some changes to DHCP so this can't happen anymore.

## Goal

- The IP address for router DHCP has been preconfigured for you.
- Configure router DHCP as a DHCP server for network 192.168.123.0 /24.
- Configure router DHCP so whenever router CLIENT sends a DHCP Discover it will install a secure ARP entry.
- Configure router DHCP so it sends ARP messages every 60 seconds to ensure router CLIENT is still there.
- Configure router SPOOFER with an IP address and see how things have changed.

## GNS3 2.2.56.1

Import [DHCP Authorized ARP IOU.gns3project](DHCP%20Authorized%20ARP%20IOU.gns3project) using **File > Import portable project**. To open `DHCP Authorized ARP.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Client | FastEthernet0/0 | Ethernet0/0 |
| DHCP | FastEthernet0/0 | Ethernet0/0 |
| Spoofer | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-dhcp-authorized-arp.png)

## Video Solution

[Video: DHCP Authorized ARP Solution](http://www.youtube.com/watch?v=gct9bDSu9BY)
