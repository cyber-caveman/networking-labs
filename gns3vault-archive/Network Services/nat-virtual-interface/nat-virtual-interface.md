# NAT Virtual Interface

## Scenario

After passing the CCNA exam you feel like you could do anything with NAT. You just started at a new job as a junior network engineer but to your surprise the router you are working on doesn't have any "inside" or "outside" commands. It does create a NVI interface but you have no idea what it is...let's see if you can configure NAT anyway...

## Goal

* All IP addresses have been preconfigured for you.
* Configure NAT so hosts on network 192.168.12.0 /24 are translated to network 192.168.23.0 /24.
* You are not allowed to use the "ip nat inside" or "ip nat outside" command.

## GNS3 2.2.56.1

Import [NAT Virtual Interface IOU.gns3project](NAT%20Virtual%20Interface%20IOU.gns3project) using **File > Import portable project**. To open `NAT Virtual Interface.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Jack | FastEthernet0/0 | Ethernet0/0 |
| NAT | FastEthernet0/0 | Ethernet0/0 |
| NAT | FastEthernet1/0 | Ethernet0/1 |
| Tomb | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-nat-virtual-interface.png)

## Video Solution

[NAT Virtual Interface - Video Solution](http://www.youtube.com/watch?v=PcKblmk9Yns)
