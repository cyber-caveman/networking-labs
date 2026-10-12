# System Message Logging

## Scenario

Two brothers are working as network consultants. One of their customers asked them to implement logging system messages on their routers. There is no central logging server so you need to configure the routers for optimal logging.

## Goal

- All IP addresses have been preconfigured for you.
- EIGRP has been configured for connectivity.
- Output from debug messages on router Erik should be sent to the console but limited to 3 messages per second.
- Both routers have to save debugging messages to their buffers up to 4096 bytes.
- Messages on the console log should not interrupt any command output.
- When you login router Rene using telnet you should only see messages from level "notifications" and higher.

## GNS3 2.2.56.1

Import [System Message Logging IOU.gns3project](System%20Message%20Logging%20IOU.gns3project) using **File > Import portable project**. To open `System Message Logging.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Erik | FastEthernet0/0 | Ethernet0/0 |
| Rene | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-system-message-logging.png)
