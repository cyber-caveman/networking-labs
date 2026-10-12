# NAT and Route-Map

## Scenario

Your network has two connections to the outside world. One is used for the Internet and the other one connects to a partner. You are using NAT to translate the IP addresses of your LAN but you want to ensure the correct IP addresses will be used...time to combine route-maps with NAT!

## Goal

- All IP addresses have been preconfigured for you.
- Configure router NAT so when router Jack communicates with router WWW it will be translated to an IP address in the 192.168.23.0 /24 range.
- Configure router NAT so when router Jack communicates with router Partner it will be translated to an IP address in the 192.168.24.0 /24 range.

## GNS3 2.2.56.1

Import [NAT and Route-Map IOU.gns3project](NAT%20and%20Route-Map%20IOU.gns3project) using **File > Import portable project**. To open `NAT and Route-Map.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Jack | FastEthernet0/0 | Ethernet0/0 |
| NAT | FastEthernet0/0 | Ethernet0/0 |
| NAT | Serial1/0 | Serial4/0 |
| NAT | Serial1/1 | Serial4/1 |
| NAT | Serial1/2 | Serial4/2 |
| NAT | Serial1/3 | Serial4/3 |
| Partner | Serial0/0 | Serial4/0 |
| Partner | Serial0/1 | Serial4/1 |
| Partner | Serial0/2 | Serial4/2 |
| Partner | Serial0/3 | Serial4/3 |
| WWW | Serial0/0 | Serial4/0 |
| WWW | Serial0/1 | Serial4/1 |
| WWW | Serial0/2 | Serial4/2 |
| WWW | Serial0/3 | Serial4/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-nat-and-route-map.png)

## Video Solution

[YouTube Video](http://www.youtube.com/watch?v=SUbJulQ7y_I)
