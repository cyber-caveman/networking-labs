# Telnet Server Tuning

## Scenario

You own a company specialized in network and router tuning. One of your customers sells customized cars and uses telnet to work remotely between their two sites. They would like you to tweak their telnet server for optimal settings. Think you can pimp this ride?

## Goal

* All IP addresses have been preconfigured for you.
* EIGRP has been configured for connectivity.
* Configure router WestCoast so it sources all telnet sessions from the loopback0 interface.
* Configure router WestCoast so it uses DSCP value "EF" for all telnet sessions.
* Configure router WestCoast so it doesn't show any informational telnet messages.

## GNS3 2.2.56.1

Import [Telnet Server Tuning IOU.gns3project](Telnet%20Server%20Tuning%20IOU.gns3project) using **File > Import portable project**. To open `Telnet Server Tuning.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| EastCoast | FastEthernet0/0 | Ethernet0/0 |
| WestCoast | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-telnet-server-tuning.png)
