# IPv6 Troubleshooting

## Scenario

Your colleague Henry Exadecimal has been busy upgrading the network to IPv6 to replace the old IPv4 topology. Some of the routers have been configured for RIPNG, OSPFv3 and even some tunneling over IPv4. Unfortunately Henry isn't very good at IPv6 and the network is one big mess. You have been studying CCNP ROUTE for quite some time so you are very familiar with IPv6...it's up to you to fix this!

## Goal

* All IP addresses have been preconfigured for you.
* **Do not use show run**! (this will spoil the fun :) use the appropiate 'show' and 'debug' commands. This will teach you the skills needed to become a true troubleshooting master.
* R1 is supposed to receive an IPv6 prefix from R2 through autoconfiguration but for some reason this is not working.
* R1 should have an IPv6 default route in its routing table. You are not allowed to create a default route yourself or configure a routing protocol on R1.
* R3 should be able to reach the loopback0 interface of R2 but this is not working.
* R3 and R4 are configured for OSPFv3 but for some reason no neighbor adjacency is appearing.
* R2 should be able to reach the loopback0 interface of R4 and vice versa, however this is not working as expected.
* R4 and R5 are configured for OSPFv3 on the frame-relay link. The neighbor adjacency is not working however...
* R5 and R7 are configured for IPv6 6to4 tunneling because R6 is an IPv4-only device. For some reason the tunnel is not working.
* When you are finished, R2, R3, R4, R5 and R7 should be able to ping each others loopback0 interfaces.

## GNS3 2.2.56.1

Import [ipv6-troubleshooting-startup-configs IOU.gns3project](ipv6-troubleshooting-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `ipv6-troubleshooting-startup-configs.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| R1 | FastEthernet0/0 | Ethernet0/0 |
| R2 | FastEthernet0/0 | Ethernet0/0 |
| R2 | FastEthernet1/0 | Ethernet0/1 |
| R3 | FastEthernet0/0 | Ethernet0/0 |
| R3 | FastEthernet1/0 | Ethernet0/1 |
| R4 | FastEthernet0/0 | Ethernet0/0 |
| R4 | Serial1/0 | Serial4/0 |
| R4 | Serial1/1 | Serial4/1 |
| R4 | Serial1/2 | Serial4/2 |
| R4 | Serial1/3 | Serial4/3 |
| R5 | FastEthernet1/0 | Ethernet0/0 |
| R5 | Serial0/0 | Serial4/0 |
| R5 | Serial0/1 | Serial4/1 |
| R5 | Serial0/2 | Serial4/2 |
| R5 | Serial0/3 | Serial4/3 |
| R6 | FastEthernet0/0 | Ethernet0/0 |
| R6 | FastEthernet1/0 | Ethernet0/1 |
| R7 | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-ipv6-troubleshooting.png)
