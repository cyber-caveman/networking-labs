# IP Traffic Export

## Scenario

You work for a local copyshop in a small town in the USA. To improve network security you have installed a new Intrusion Detection System (IDS) but right now it's only receiving traffic from router Ditto. You are familiar with SPAN for switches but you don't know how to export traffic on routers...let's see if there's a copycat in you!

## Goals

- All IP addresses have been preconfigure for you.
- EIGRP has been configured for connectivity.
- Configure router Ditto so all EIGRP and HTTP traffic is exported to router IDS.

## GNS3 2.2.56.1

Import [Router IP Traffic Export IOU.gns3project](Router%20IP%20Traffic%20Export%20IOU.gns3project) using **File > Import portable project**. To open `Router IP Traffic Export.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Ditto | FastEthernet0/0 | Ethernet0/0 |
| Ditto | FastEthernet1/0 | Ethernet0/1 |
| Ditto | FastEthernet2/0 | Ethernet0/2 |
| Forge | FastEthernet0/0 | Ethernet0/0 |
| IDS | FastEthernet0/0 | Ethernet0/0 |
| Repo | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-ip-traffic-export.png)

## Video Solution

[Video Solution on YouTube](http://www.youtube.com/watch?v=K-kBptdFEEs)
