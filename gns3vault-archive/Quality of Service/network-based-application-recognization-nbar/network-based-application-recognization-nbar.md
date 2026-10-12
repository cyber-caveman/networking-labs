# Network Based Application Recognization (NBAR)

## Scenario

As the owner of a small company you notice some of your employees are slacking off at the job and spending their time at Facebook, Twitter and some other sites. You want to configure your network so these sites are blocked. While you are at it you also want to block some of the worms that are on the Internet.

## Goal

- All IP addresses have been preconfigured for you.
- OSPF has been preconfigure for full connectivity.
- Configure router Sluggish so all traffic from Twitter is dropped on the FastEthernet 1/0 interface.
- Configure router Sluggish so it can detect the NIMDA worm and drops the traffic on the FastEthernet 1/0 interface.
- Configure router Sluggish so it marks Youtube traffic down to DSCP 0 on the FastEthernet 1/0 interface.

## GNS3 2.2.56.1

Import [Network Based Application Recognization (NBAR) IOU.gns3project](Network%20Based%20Application%20Recognization%20%28NBAR%29%20IOU.gns3project) using **File > Import portable project**. To open `Network Based Application Recognization (NBAR).gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Drowsy | FastEthernet0/0 | Ethernet0/0 |
| Lazy | FastEthernet0/0 | Ethernet0/0 |
| Sluggish | FastEthernet0/0 | Ethernet0/0 |
| Sluggish | FastEthernet1/0 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-network-based-application-recognization-nbar.png)

## Video Solution

[YouTube Video](http://www.youtube.com/watch?v=JXHtctRgcSg)
