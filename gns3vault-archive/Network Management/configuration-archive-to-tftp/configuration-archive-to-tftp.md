# Configuration Archive to TFTP

## Scenario

Recently your company was audited and didn't pass the security test. One of the complaints was that there is no automated backup mechanism for routers. You decide to configure your network so the routers will copy their configuration every 24 hours to a TFTP server.

## Goal

* All IP addresses have been preconfigured for you.
* Configure router Safety so it will save its configuration every 24 hours to TFTP server 192.168.12.2.
* Everytime you save your running-config to the startup-config it should also be copied to the TFTP server.

## GNS3 2.2.56.1

Import [Configuration Archive to TFTP IOU.gns3project](Configuration%20Archive%20to%20TFTP%20IOU.gns3project) using **File > Import portable project**. To open `Configuration Archive to TFTP.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Safety | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-configuration-archive-to-tftp.png)
