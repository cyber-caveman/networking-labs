# ACL Selective IP Options Drop

## Scenario

You are the security office for the national security team in the Netherlands. One of your routers has a very high CPU load and after looking closely you can see it's spending a lot of cycles processing IP packets with special options. Since this isn't normal you decide to implement some filtering.

## Goals

- All IP addresses have been preconfigure for you.
- Configure router Trash so it drops IP packets with the timestamp option.
- Configure router Trash so it drops IP packets with the loose source option.

## GNS3 2.2.56.1

Import [ACL Selective IP Option Drop IOU.gns3project](ACL%20Selective%20IP%20Option%20Drop%20IOU.gns3project) using **File > Import portable project**. To open `ACL Selective IP Option Drop.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Crash | FastEthernet0/0 | Ethernet0/0 |
| Trash | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-acl-selective-ip-options-drop.png)

## Video Solution

[http://www.youtube.com/watch?v=DWCjzhNLLK4](http://www.youtube.com/watch?v=DWCjzhNLLK4)
