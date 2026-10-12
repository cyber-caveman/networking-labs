# Floating Static Routes

## Scenario

While you are drifting on a inflatable bed at your swimming pool you fall asleep and dream about floating static routes. There's this issue at work you couldn't solve but sometimes the best ideas arrive in your dreams right?

## Goal

- All IPv4 addresses have been preconfigured for you.
- Create two static routes on router Float pointing to the loopback0 interface of router Drift.
- Ensure the FastEthernet link is used for all traffic, when it fails traffic should be sent down the serial link.

## GNS3 2.2.56.1

Import [Floating Static Routes IOU.gns3project](Floating%20Static%20Routes%20IOU.gns3project) using **File > Import portable project**. To open `Floating Static Routes.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Drift | FastEthernet0/0 | Ethernet0/0 |
| Drift | Serial1/0 | Serial4/0 |
| Drift | Serial1/1 | Serial4/1 |
| Drift | Serial1/2 | Serial4/2 |
| Drift | Serial1/3 | Serial4/3 |
| Float | FastEthernet0/0 | Ethernet0/0 |
| Float | Serial1/0 | Serial4/0 |
| Float | Serial1/1 | Serial4/1 |
| Float | Serial1/2 | Serial4/2 |
| Float | Serial1/3 | Serial4/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-floating-static-routes.png)

## Video Solution

http://www.youtube.com/watch?v=LBdbE6wBvBk
