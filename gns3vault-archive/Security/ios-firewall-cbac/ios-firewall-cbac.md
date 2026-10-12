# IOS Firewall - CBAC

![Network Topology](./topology-ios-firewall-cbac.jpg)

## Scenario

As the network engineer for your company you are responsible for all network-related tasks. One day your security officer comes to you and asks if you can further enhance the network security. He wants you to implement an IOS Firewall feature to protect incoming traffic.

## Goal

- All IP addresses have been configured for you.
- Router Mainframe is configured as a webserver, telnet is enabled as well.
- You are not allowed to remove the access-list on the F1/0 interface of router FW.
- Traffic originated from Mainframe is not allowed to reach router Host.
- Router host should be able to telnet into router mainframe.

## GNS3 2.2.56.1

Import [cbac-firewall-startup-configs IOU.gns3project](cbac-firewall-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `cbac-firewall-startup-configs.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Host | FastEthernet0/0 | Ethernet0/0 |
| FW | FastEthernet0/0 | Ethernet0/0 |
| FW | FastEthernet1/0 | Ethernet0/1 |
| Mainframe | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

## Video Solution

[Video: IOS Firewall CBAC Configuration](http://www.youtube.com/watch?v=AAw81cf5IBE)
