# Extended Access-List

## Scenario

This morning you woke up in a cell feeling dizzy and nauseous, it appears you were kidnapped by a mixture of agents from federal agencies. Your task is to finish this security test, if you pass you might end up becoming their next security agent...with blurry eyes you start your task!

## Goal

* All IP addresses have been configured for you, look at the topology picture for the IP addresses.
* OSPF has been configured for full connectivity.
* All routers are running services like HTTP, HTTPS, TELNET and SSH.
* Make sure you use the most specific wildcard for all your access-lists.
* You are only allowed to use extended access-lists.
* Configure the network so traffic from router CIA's L0 interface towards the HTTP server on 3.3.3.3 is not permitted.
* Configure the network so traffic from router FBI's L1 interface is only allowed to reach the HTTPS server on IP address 33.33.33.33.
* Configure the network so only users from router NSA's L1 interface are allowed to telnet into router CIA.
* Configure the network so users from router FBI's L2 interface are not allowed to ping to router's NSA L1 interface.

## Topology

![Network Topology](./topology-extended-access-list.png)

## Video Solution

[Video Solution](http://www.youtube.com/watch?v=lV6C7ABL1Ug)

## GNS3 2.2.56.1

Import [extended-acl-startup-configs IOU.gns3project](extended-acl-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `extended-acl-startup-configs.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| CIA | FastEthernet0/0 | Ethernet0/0 |
| CIA | FastEthernet0/1 | Ethernet0/1 |
| FBI | FastEthernet0/0 | Ethernet0/0 |
| FBI | FastEthernet0/1 | Ethernet0/1 |
| NSA | FastEthernet0/0 | Ethernet0/0 |
| NSA | FastEthernet0/1 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.
