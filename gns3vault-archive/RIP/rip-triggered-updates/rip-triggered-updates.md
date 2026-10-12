# RIP Triggered Updates

## Scenario

Harry and Sara are network consultants and studying for their CCIE R&S certification. They both have a router and they are running RIP on the serial link to exchange routing information. Their ISP charges them for each byte sent so they want to make sure RIP doesn't send any unnecessary traffic.

## Goal

- All IP addresses have been preconfigured for you.
- Both routers have a loopback interface as following:
  - Sara: 1.1.1.1/24
  - Harry: 2.2.2.2/24
  - Configure RIP version 1 on both routers, achieve full connectivity for all networks (including the loopbacks).
- Ensure RIP only sends updates when unnecessary.
- Sara and Harry would like to know how they can see this configuration is active without looking at the running- or startup-config. Can you help them?

## GNS3 2.2.56.1

Import [RIP Triggered Updates IOU.gns3project](RIP%20Triggered%20Updates%20IOU.gns3project) using **File > Import portable project**. To open `RIP Triggered Updates.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Harry | Serial0/0 | Serial4/0 |
| Harry | Serial0/1 | Serial4/1 |
| Harry | Serial0/2 | Serial4/2 |
| Harry | Serial0/3 | Serial4/3 |
| Sara | Serial0/0 | Serial4/0 |
| Sara | Serial0/1 | Serial4/1 |
| Sara | Serial0/2 | Serial4/2 |
| Sara | Serial0/3 | Serial4/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-rip-triggered-updates.png)

## Video Solution

http://www.youtube.com/watch?v=feVtPueT1AQ
