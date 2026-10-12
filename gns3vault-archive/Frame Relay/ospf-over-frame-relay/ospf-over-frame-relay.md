# OSPF over Frame-Relay

![Network Topology](./topology-ospf-over-frame-relay.jpg)

## Scenario

After successfully configuring the previous frame-relay lab you feel it's time to try and run OSPF over this frame-relay link. OSPF knows many different network types and every type has a different solution, up to you to try them all out!

Hint: this lab uses the same topology as the "Frame-Relay Basics" lab, make sure you configured this lab first, then continue with this one.

## Goal

* Create loopbacks on all routers:
  * Paris: 1.1.1.1 /24
  * Berlin: 2.2.2.2 /24
  * Stockholm: 3.3.3.3 /24
* Configure OSPF on all routers using the point-to-multipoint interface (192.168.123.X subnet).
* Advertise all loopbacks in OSPF.
* Paris should be the OSPF designated router.
* Configure the OSPF network type on all routers to "Broadcast", ensure you have full connectivity to all subnets.
* Configure the OSPF network type on all routers to "Non-Broadcast", ensure you still have full connectivity.
* Configure the OSPF network type on all routers to "Point-to-Multipoint", ensure you still have full connectivity.
* Configure the OSPF network type on all routers to "Point-to-Multipoint non-broadcast", ensure you still have full connectivity.

## GNS3 2.2.56.1

Import [ospf-over-frame-relay IOU.gns3project](ospf-over-frame-relay%20IOU.gns3project) using **File > Import portable project**. To open `ospf-over-frame-relay.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Frame Relay switching routers retain Dynamips and the available C3640 appliance, with device-specific config packaging. Their source configuration text is preserved.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Paris | Serial0/0 | Serial4/0 |
| Paris | Serial0/1 | Serial4/1 |
| Paris | Serial0/2 | Serial4/2 |
| Paris | Serial0/3 | Serial4/3 |
| FRSW | Serial0/0 | Serial0/0 |
| FRSW | Serial0/1 | Serial0/1 |
| FRSW | Serial0/2 | Serial0/2 |
| FRSW | Serial0/3 | Serial0/3 |
| Berlin | Serial0/0 | Serial4/0 |
| Berlin | Serial0/1 | Serial4/1 |
| Berlin | Serial0/2 | Serial4/2 |
| Berlin | Serial0/3 | Serial4/3 |
| Stockholm | Serial0/0 | Serial4/0 |
| Stockholm | Serial0/1 | Serial4/1 |
| Stockholm | Serial0/2 | Serial4/2 |
| Stockholm | Serial0/3 | Serial4/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

## Video Solution

* [YouTube Video](http://www.youtube.com/watch?v=oEZfeyf8_p4)
