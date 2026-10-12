# Logging Timestamps

## Scenario

"Time 'r Us" is a large swiss company selling a wide range of watches. Recently the company was hacked but the company's security officer traced down the hacker. Unfortunately the hacker got away because the log files didn't have any date or timestamps on it and couldn't be used as evidence in court. You as a security specialist decide to change this for the future and implement timestamps for logging on your routers.

## Goal

- All IP addresses have been preconfigured for you.
- EIGRP has been configured for connectivity.
- Configure router Precision so it saves date-time on its timestamps.
- Configure router Accuracy so it saves uptime on its timestamps.
- Configure both routers to save year information in their logging messages.
- Configure Router Accuracy so it adds milliseconds to the timestamps.
- Configure both routers to prevent tampering with stored logging information.

## GNS3 2.2.56.1

Import [Logging Timestamps IOU.gns3project](Logging%20Timestamps%20IOU.gns3project) using **File > Import portable project**. To open `Logging Timestamps.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Accuracy | FastEthernet0/0 | Ethernet0/0 |
| Precision | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-logging-timestamps.png)
