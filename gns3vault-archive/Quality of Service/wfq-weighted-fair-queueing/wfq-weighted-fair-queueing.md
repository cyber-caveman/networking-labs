# WFQ Weighted Fair Queueing

## Scenario

Ada and Silver are using the network for a range of applications like FTP, HTTP, TELNET and more. Recently there have been some complaints about slow network performance and it's up to you to make sure each application gets a fair share of the bandwidth.

## Goal

- All IP addresses have been preconfigured for you.
- EIGRP has been configured for full connectivity.
- Configure the S0/1 interface of router Rae with a bandwidth of 64kbps.
- Configure WFQ on the S0/1 interface of router Rae. The output hold-queue size should be 128, length of 16 for congestive discard threshold, a maximum of 128 conversations and 4 queues for RSVP.
- Configure the hardware queue on router Rae so WFQ will be activated as soon as possible.

## GNS3 2.2.56.1

Import [WFQ Weighted Fair Queueing IOU.gns3project](WFQ%20Weighted%20Fair%20Queueing%20IOU.gns3project) using **File > Import portable project**. To open `WFQ Weighted Fair Queueing.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Ada | Serial0/0 | Serial4/0 |
| Ada | Serial0/1 | Serial4/1 |
| Ada | Serial0/2 | Serial4/2 |
| Ada | Serial0/3 | Serial4/3 |
| Rae | Serial0/0 | Serial4/0 |
| Rae | Serial0/1 | Serial4/1 |
| Rae | Serial0/2 | Serial4/2 |
| Rae | Serial0/3 | Serial4/3 |
| Silver | Serial0/0 | Serial4/0 |
| Silver | Serial0/1 | Serial4/1 |
| Silver | Serial0/2 | Serial4/2 |
| Silver | Serial0/3 | Serial4/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-wfq-weighted-fair-queueing.png)

## Video Solution

[WFQ Weighted Fair Queueing Video Solution](http://www.youtube.com/watch?v=tzXj-Ik3Iow)
