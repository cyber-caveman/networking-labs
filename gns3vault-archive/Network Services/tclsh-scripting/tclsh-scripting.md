# TCLSH Scripting

![Network Topology](./topology-tclsh-scripting.jpg)

## Scenario

To make your life easier you decided to practice some TCLSH scripting skills, this will ensure it takes less time to ping.

## Goal

* All IP addresses are preconfigured as specified in the topology picture.
* Ensure you can ping the loopbacks on PONG from router PING.
* Create a TCLSH script that pings all the loopback ip addresses at once.

## GNS3 2.2.56.1

Import [tclsh-scripting-startup-configs IOU.gns3project](tclsh-scripting-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `tclsh-scripting-startup-configs.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Ping | FastEthernet0/0 | Ethernet0/0 |
| Pong | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

## Video Solution

http://www.youtube.com/watch?v=awyT_1j8Zx8
