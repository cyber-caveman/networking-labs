# EEM Scripting Event Detector

## Scenario

You are the security officer of the network and recently some of the network engineers have been sloppy with the security rules within the company. You decide to implement EEM scripting so passwords don't show up some of the show commands.

## Goal

* All IP addresses have been preconfigured for you.
* Configure router Scriptor so when someone types "show running config" you won't see the VTY password.
* You are only allowed to use EEM scripting to solve this.

## GNS3 2.2.56.1

Import [EEM Scripting Event Detector IOU.gns3project](EEM%20Scripting%20Event%20Detector%20IOU.gns3project) using **File > Import portable project**. To open `EEM Scripting Event Detector.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-eem-scripting-event-detector.png)
