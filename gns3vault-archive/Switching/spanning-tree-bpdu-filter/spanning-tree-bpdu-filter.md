# Spanning Tree BPDU Filter

## Scenario



You are working as the network engineer at a school located in Germany. The network has been having issues last month after students took a CCNA class. You want to make sure the access layer of the network is more secure. When students try to mess with spanning-tree it should block the interface they are connected to.

## Goal

- Configure SW1 so it does not send any BPDUs towards router Neo. Any BPDU that you receive from router Neo should be ignored.

## Note

## GNS3 2.2.56.1

Import [spanning-tree-bpdu-filter IOU.gns3project](spanning-tree-bpdu-filter%20IOU.gns3project) using **File > Import portable project**. To open `spanning-tree-bpdu-filter.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

CLI switches explicitly select PVST when the source relies on that default. Converted EtherSwitch routers retain their default IP-routing state and routed FastEthernet0 ports. Use the IOU names below when following old interface references in the instructions and diagrams.

| Device | Source interface | Current interface |
| --- | --- | --- |
| SW1 | FastEthernet0/1 | Ethernet0/0 |
| Neo | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-spanning-tree-bpdu-filter.png)

## Video Solution

http://www.youtube.com/watch?v=Drz6i_wZWTs
