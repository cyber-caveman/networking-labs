# Kron Task Scheduler

## Scenario

You want to make sure your router automatically saves its configuration every day. You are familiar with Cron for Linux and you just heard from a colleague that there is a similar feature for Cisco routers. Kron time!

## Goal

* All IP addresses have been preconfigured for you.
* Configure router Kron so it saves the running-config every Saturday at 20:00.

## GNS3 2.2.56.1

Import [Kron Task Scheduler IOU.gns3project](Kron%20Task%20Scheduler%20IOU.gns3project) using **File > Import portable project**. To open `Kron Task Scheduler.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-kron-task-scheduler.png)

## Video Solution

[Kron Task Scheduler Solution](http://www.youtube.com/watch?v=orefN5KG7AY)
