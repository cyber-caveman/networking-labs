# UDLD (UniDirectional Link Detection)

![Network Topology](./topology-udld-unidirectional-link-detection.png)

## Scenario:



Fiber 'r' us is specialized in fiber solutions for layer 2 switches. They are concerned that layer 2 loops might occur when the transmit or receive connectors of their fiber links get disconnected. You want to implement a feature that will prevent a loop in case this happens. You don't want to use a spanning tree solution so there's something else you'll have to configure...

## Goal:

* Configure UDLD on interface fa0/16 of both switches, use aggressive mode.
* Configure a MAC filter on SW2 that filters MAC address 0100.0ccc.cccc to simulate a link failure.

## GNS3 2.2.56.1

Import [udld-unidirectional-link-detection IOU.gns3project](udld-unidirectional-link-detection%20IOU.gns3project) using **File > Import portable project**. To open `udld-unidirectional-link-detection.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

CLI switches explicitly select PVST when the source relies on that default. Converted EtherSwitch routers retain their default IP-routing state and routed FastEthernet0 ports. Use the IOU names below when following old interface references in the instructions and diagrams.

| Device | Source interface | Current interface |
| --- | --- | --- |
| SW2 | FastEthernet0/16 | Ethernet0/0 |
| SW3 | FastEthernet0/16 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology:

## Video Solution:

http://www.youtube.com/watch?v=GWBWMaRS47A
