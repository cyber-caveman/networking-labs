# Spanning Tree BPDU Guard

![Network Topology](./topology-spanning-tree-bpdu-guard.png)

## Scenario:



You are working as the network engineer at a school located in Germany. The network has been having issues last month after students took a CCNA class. You want to make sure the access layer of the network is more secure. When students try to mess with spanning-tree it should block the interface they are connected to.

## Goal:

* Ensure all switches run PVST (default on most Cisco switches).
* Ensure that whenever you receive a BPDU from router Neo it will block the interface.
* After 400 seconds the interface should enable itself automatically again.

## GNS3 2.2.56.1

Import [spanning-tree-bpdu-guard IOU.gns3project](spanning-tree-bpdu-guard%20IOU.gns3project) using **File > Import portable project**. To open `spanning-tree-bpdu-guard.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

CLI switches explicitly select PVST when the source relies on that default. Converted EtherSwitch routers retain their default IP-routing state and routed FastEthernet0 ports. Use the IOU names below when following old interface references in the instructions and diagrams.

| Device | Source interface | Current interface |
| --- | --- | --- |
| SW1 | FastEthernet0/1 | Ethernet0/0 |
| Neo | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology:

## Video Solution:

[Video: Spanning Tree BPDU Guard Solution](http://www.youtube.com/watch?v=1VI_WAk4AcU)
