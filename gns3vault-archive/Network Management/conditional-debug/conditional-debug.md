# Conditional Debug

## Scenario

Frank has heard about a feature called "conditional debug" that sounds interesting to him. It seems that you can use this command to only show the output of certain protocols instead of having your screen flooded with debug information. Think you can teach a fellow network engineer this feature?

## Goal

* All IP addresses have been preconfigured for you.
* OSPF and RIP have been preconfigured to generate some traffic.
* Enable a debug on router Frank which only shows RIP information on the FastEthernet0/0 interface. You are not allowed to use any access-lists.

## GNS3 2.2.56.1

Import [Conditional Debug IOU.gns3project](Conditional%20Debug%20IOU.gns3project) using **File > Import portable project**. To open `Conditional Debug.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Erik | FastEthernet0/0 | Ethernet0/0 |
| Frank | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-conditional-debug.png)

## Video Solution

http://www.youtube.com/watch?v=L6iQy1mAE4s
