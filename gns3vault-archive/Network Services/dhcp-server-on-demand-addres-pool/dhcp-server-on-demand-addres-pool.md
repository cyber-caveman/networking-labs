# DHCP Server On-Demand Addres Pool

## Scenario

Your network has many serial links running PPP. You heard some good things about DHCP and how you can create on-demand pools using IPCP. Let's see if it works the way you expect...

## Goal

- Configure both routers for PPP encapsulation.
- Configure router John so router Williams receives IP address 192.168.12.2 thanks to IPCP.
- Configure router William with a DHCP pool that imports the subnet mask that it receives from router John.

## GNS3 2.2.56.1

Import [DHCP Server  On-Demand Address Pool IOU.gns3project](DHCP%20Server%20%20On-Demand%20Address%20Pool%20IOU.gns3project) using **File > Import portable project**. To open `DHCP Server  On-Demand Address Pool.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| John | Serial0/0 | Serial4/0 |
| John | Serial0/1 | Serial4/1 |
| John | Serial0/2 | Serial4/2 |
| John | Serial0/3 | Serial4/3 |
| Williams | Serial0/0 | Serial4/0 |
| Williams | Serial0/1 | Serial4/1 |
| Williams | Serial0/2 | Serial4/2 |
| Williams | Serial0/3 | Serial4/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-dhcp-server-on-demand-addres-pool.png)

## Video Solution

[Video: DHCP Server On-Demand Address Pool](http://www.youtube.com/watch?v=V7Qc25B-51I)
