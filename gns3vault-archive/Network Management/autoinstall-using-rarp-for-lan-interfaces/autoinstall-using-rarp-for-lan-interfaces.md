# AutoInstall using RARP for LAN Interfaces

## Scenario

You are the network engineer at a company specialized in creating virtual worlds. The last few months the company gained quite some new customers, for each customer a new router has to be installed and to save time you want to make sure you can automatically them using the auto-install feature.

## Goal

* All IP addresses have been preconfigured for you (except router Flynn).
* EIGRP has been configured for connectivity.
* Router Flynn should request an IP address for the FastEthernet 0/0 interface using RARP.
* Router Quorra should give router Flynn IP address 192.168.12.1.
* Router Flynn has to receive its configuration file from router Jarvis.

## GNS3 2.2.56.1

Import [AutoInstall Using RARP for LAN Interfaces IOU.gns3project](AutoInstall%20Using%20RARP%20for%20LAN%20Interfaces%20IOU.gns3project) using **File > Import portable project**. To open `AutoInstall Using RARP for LAN Interfaces.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Flynn | FastEthernet0/0 | Ethernet0/0 |
| Gem | FastEthernet0/0 | Ethernet0/0 |
| Jarvis | FastEthernet0/0 | Ethernet0/0 |
| Jarvis | FastEthernet1/0 | Ethernet0/1 |
| Quorra | FastEthernet0/0 | Ethernet0/0 |
| Quorra | FastEthernet1/0 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-autoinstall-using-rarp-for-lan-interfaces.png)
