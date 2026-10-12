# Dynamic Access List - Lock and Key

## Scenario

You are the senior network engineer at a company called "The Router Whisperer". Your boss heard about a new feature to increase security for one of your customers who is a famous dog trainer. You need to make sure that users authenticate to router Bulldog before they are allowed access to router ProtectMe.

## Goal

- All IP addresses have been configured for you, look at the topology picture for the IP addresses.
- Static routes have been configured for you to ensure full connectivity.
- Configure router Bulldog so users have to authenticate before they are allowed telnet access into router ProtectMe.

## Topology

![Network Topology](./topology-dynamic-access-list-lock-and-key.png)

## Video Solution

[View on YouTube](http://www.youtube.com/watch?v=qCyvUIHh2jo)

## GNS3 2.2.56.1

Import [lock-and-key-startup-configs IOU.gns3project](lock-and-key-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `lock-and-key-startup-configs.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Bulldog | FastEthernet0/0 | Ethernet0/0 |
| Bulldog | FastEthernet0/1 | Ethernet0/1 |
| Chihuahua | FastEthernet0/0 | Ethernet0/0 |
| Chihuahua | FastEthernet0/1 | Ethernet0/1 |
| ProtectMe | FastEthernet0/0 | Ethernet0/0 |
| ProtectMe | FastEthernet0/1 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.
