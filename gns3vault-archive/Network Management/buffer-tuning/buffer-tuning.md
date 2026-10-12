# Buffer Tuning

## Scenario

After a hard day of studying networking you decide to chill out and head for the local gym. As soon as you arrive the owner of the place comes to you and he seems to be upset. A staff member tried to buff up the routers but something went terrible wrong. Your brain is sore but do you think you can push one more rep?

## Goal

- All IP addresses have been preconfigured for you.
- Configure router Buffed for automatic buffer tuning.
- Configure router Spice to triple all public buffers.
- Configure router Spice so there are at least 20 Large and Huge buffers available.

## GNS3 2.2.56.1

Import [Buffer Tuning IOU.gns3project](Buffer%20Tuning%20IOU.gns3project) using **File > Import portable project**. To open `Buffer Tuning.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Buffed | FastEthernet0/0 | Ethernet0/0 |
| Spice | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-buffer-tuning.png)

## Video Solution

[http://www.youtube.com/watch?v=5zkrX_FrWLE](http://www.youtube.com/watch?v=5zkrX_FrWLE)
