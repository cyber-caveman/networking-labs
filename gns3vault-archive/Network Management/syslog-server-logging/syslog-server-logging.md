# Syslog Server Logging

## Scenario

Router MasterMind has a large memory but due to security reasons you want to make sure all logging information isn't saved locally but dumped to an external syslog server. You don't want to use the default configuration though so let's see how you can tune syslog logging...

## Goal

- All IP addresses have been preconfigured for you.
- Router MasterMind has a loopback0 interface with IP address 1.1.1.1 /24.
- Optional: You can use the cloud interface to connect your router to a free syslog server like Kiwi Syslog Server.
- Configure router MasterMind so it sends all logging information to a syslog server with IP address 192.168.12.2.
- Configure router MasterMind so a reliable protocol is used for logging messages and use port 4040.
- Configure router MasterMind so logging messages are sent from the loopback0 interface.
- Configure router MasterMind so all messages are logged up to the emergencies level.
- Configure router MasterMind so it uses origin-ID string "MasterMind" and facility local1.

## GNS3 2.2.56.1

Import [Syslog Server Logging IOU.gns3project](Syslog%20Server%20Logging%20IOU.gns3project) using **File > Import portable project**. To open `Syslog Server Logging.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| MasterMind | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-syslog-server-logging.png)
