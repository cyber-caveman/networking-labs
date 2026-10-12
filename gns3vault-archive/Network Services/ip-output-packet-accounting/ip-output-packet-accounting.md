# IP Output Packet Accounting

## Scenario

Your boss is very interested to know which MAC addresses on the network are responsible for most traffic. Besides MAC addresses you would also like to see how many packets are marked with IP precedence. Time for some accounting...

## Goal

* All IP addresses have been preconfigured for you.
* Configure a loopback0 interface on router Tomb with IP address 3.3.3.3 /24.
* Configure EIGRP AS 1 on all routers and achieve full connectivity.
* Configure IP Output Packet accounting on router Wodan so you can trace packets from router Jack to the loopback0 interface of router Tomb.

## GNS3 2.2.56.1

Import [IPOutputPacketAccounting IOU.gns3project](IPOutputPacketAccounting%20IOU.gns3project) using **File > Import portable project**. To open `IPOutputPacketAccounting.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Jack | FastEthernet0/0 | Ethernet0/0 |
| Tomb | FastEthernet0/0 | Ethernet0/0 |
| Wodan | FastEthernet0/0 | Ethernet0/0 |
| Wodan | FastEthernet1/0 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-ip-output-packet-accounting.png)

## Video Solution

http://www.youtube.com/watch?v=FswWzfWccqY
