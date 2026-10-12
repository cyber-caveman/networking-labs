# Link fragmentation and Interleaving for Multilink PPP

## Scenario

Your VoIP network is a little problematic to say the least. VoIP calls sound choppy and users are complaining all over the place. You look into the datastreams and it seems large data frames are preventing VoIP packets to get to their destination in time. You can't upgrade the links but you have read about link fragmentation and interleaving...let's chop em down!

## Goal

* All IP addresses have been preconfigured for you.
* Configure PPP encapsulation between router Chop and Slice.
* Configure PPP Multilink between router Chop and Slice.
* Configure fragmentation and interleaving on router Chop and Slice.
* The serialization delay should have a maximum of 10ms. The bandwidth of the serial link is 64kbps.

## GNS3 2.2.56.1

Import [Link Fragmentation and Interleaving for Multilink PPP IOU.gns3project](Link%20Fragmentation%20and%20Interleaving%20for%20Multilink%20PPP%20IOU.gns3project) using **File > Import portable project**. To open `Link Fragmentation and Interleaving for Multilink PPP.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Chop | FastEthernet1/0 | Ethernet0/0 |
| Chop | Serial0/0 | Serial4/0 |
| Chop | Serial0/1 | Serial4/1 |
| Chop | Serial0/2 | Serial4/2 |
| Chop | Serial0/3 | Serial4/3 |
| Frank | FastEthernet0/0 | Ethernet0/0 |
| Jack | FastEthernet0/0 | Ethernet0/0 |
| Slice | FastEthernet1/0 | Ethernet0/0 |
| Slice | Serial0/0 | Serial4/0 |
| Slice | Serial0/1 | Serial4/1 |
| Slice | Serial0/2 | Serial4/2 |
| Slice | Serial0/3 | Serial4/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-link-fragmentation-and-interleaving-for-multilink-ppp.png)

## Video Solution

[Link Fragmentation and Interleaving for Multilink PPP - Video Solution](http://www.youtube.com/watch?v=dohclmbeY0M)
