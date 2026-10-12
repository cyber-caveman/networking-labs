# RIP Send and Receive V1-V2

![Network Topology](./topology-rip-send-and-receive-v1-v2.png)

## Scenario:

A large international Movie company has decided all Dutch actors should have a private network for communications. Budgets are tight so you only have access to a couple of old routers that support RIP version 2 or 1. Can you configure this network to get things going?

## Goal:

- All IP addresses have been preconfigured for you.
- Every router has a loopback0 interface:
  - Hauer: 1.1.1.1 /24
  - vanHouten: 2.2.2.2 /24
  - Janssen: 3.3.3.3 /24
- Configure RIP version 2 on router Hauer.
- Configure RIP version 1 on router vanHouten.
- Configure RIP version 2 on router Janssen.
- Ensure you have full connectivity.

## GNS3 2.2.56.1

Import [RIP Send and Receive V1-V2 IOU.gns3project](RIP%20Send%20and%20Receive%20V1-V2%20IOU.gns3project) using **File > Import portable project**. To open `RIP Send and Receive V1-V2.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Hauer | FastEthernet0/0 | Ethernet0/0 |
| Janssen | FastEthernet0/0 | Ethernet0/0 |
| vanHouten | FastEthernet0/0 | Ethernet0/0 |
| vanHouten | FastEthernet1/0 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology:

## Video Solution:

http://www.youtube.com/watch?v=r0bKOFv17GQ
