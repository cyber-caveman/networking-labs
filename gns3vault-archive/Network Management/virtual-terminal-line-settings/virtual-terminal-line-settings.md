# Virtual Terminal Line Settings

## Scenario

Your network has two routers called Day and Night. Users behind router Day are using telnet to access router Night. Some users have been complaining that telnet access should be easier so you decide to look at it and do some tuning.

## Goal

- All IP addresses have been preconfigured for you.
- Configure router Night so only VTY line 0 - 2 will be used.
- Configure router Night so it uses port 3050 for telnet.
- Configure router Night so it shows a "Sorry Busy!" message when there are no available VTY lines.
- When someone from router Day telnets into router Night and makes a typing error it shouldn't try to do a domain lookup.
- Configure router Night so telnet sessions drop at 1 minute of inactivity.
- Configure router Night so telnet sessions will always drop after 2 minutes.
- Configure router Night so users can lock a VTY line.

## GNS3 2.2.56.1

Import [Virtual Terminal Line Settings IOU.gns3project](Virtual%20Terminal%20Line%20Settings%20IOU.gns3project) using **File > Import portable project**. To open `Virtual Terminal Line Settings.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Day | FastEthernet0/0 | Ethernet0/0 |
| Night | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-virtual-terminal-line-settings.png)
