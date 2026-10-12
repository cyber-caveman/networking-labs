# DHCP Troubleshooting

## Scenario

As one of the network engineers of the network you are responsible for all DHCP related configurations. In this scenario there is one DHCP server that is configured to supply IP addresses for the 192.168.12.0/24 and 192.168.23.0/24 subnet. However both clients are not receiving any IP addresses...up to you to find a solution!

## Goal

* All required IP addresses have been preconfigured as specified in the topology picture.
* **Do not use show run**! (this will spoil the fun :) use the appropiate 'show' and 'debug' commands. This will teach you the skills needed to become a true troubleshooting master.
* Router DHCPClient1 needs to get an IP address through DHCP on its fa0/0 interface.
* Router DHCPClient2 needs to get an IP address through DHCP on its fa0/0 interface.
* Only router DHCPServer has to supply IP addresses.

## GNS3 2.2.56.1

Import [DHCP Troubleshooting IOU.gns3project](DHCP%20Troubleshooting%20IOU.gns3project) using **File > Import portable project**. To open `DHCP Troubleshooting.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| DHCPClient1 | FastEthernet0/0 | Ethernet0/0 |
| DHCPClient1 | FastEthernet1/0 | Ethernet0/1 |
| DHCPClient2 | FastEthernet0/0 | Ethernet0/0 |
| DHCPServer | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-dhcp-troubleshooting.png)
