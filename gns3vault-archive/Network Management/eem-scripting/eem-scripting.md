# EEM Scripting

![Network Topology](./topology-eem-scripting.png)

## Scenario:

Ever since you switched your career from Linux engineer to networking you missed your good old scripting tools. You just heard about network engineer about EEM scripting for Cisco routers and you can't wait to try it out!

## Goal:

* All IP addresses have been preconfigured for you.
* Configure router Autobot so when the FastEthernet 0/0 interface goes down a script runs that also shuts down the FastEthernet1/0 interface.
* You are only allowed to use EEM scripting to achieve this.

## GNS3 2.2.56.1

Import [EEM Scripting IOU.gns3project](EEM%20Scripting%20IOU.gns3project) using **File > Import portable project**. To open `EEM Scripting.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| AutoBot | FastEthernet0/0 | Ethernet0/0 |
| AutoBot | FastEthernet1/0 | Ethernet0/1 |
| Rick | FastEthernet0/0 | Ethernet0/0 |
| Rock | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology:

**You need to register to download the GNS3 Topology File. (Registration is Free!)**
