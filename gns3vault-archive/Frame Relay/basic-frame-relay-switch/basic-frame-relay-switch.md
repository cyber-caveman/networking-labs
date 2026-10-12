# Basic Frame-Relay Switch

![Network Topology](./topology-basic-frame-relay-switch.jpg)

## Scenario

You are working for a huge international car company as the senior network engineer. Recently the Frame-relay switch of one of your WAN links died and you decided to replace it with a Cisco Router.

## Goal:

- Take a good look at the topology before you start configuring.
- The blue/red lines are PVC's (Permanent Virtual Circuit).
- DLCI numbers are shown on the topology picture.
- Enable frame-relay switching on Router Bumblebee.
- Configure the correct PVC's.
- Using the 'show frame-relay route' command on Router Bumblebee should show both PVC's as 'active'.
- Using the 'show frame-relay map' command on Router Optimus or Ironhide should show both PVC's as active.
- Optional: Try to achieve the same result without using the 'frame-relay route' command.

## GNS3 2.2.56.1

Import [basic-frame-relay-switch IOU.gns3project](basic-frame-relay-switch%20IOU.gns3project) using **File > Import portable project**. To open `basic-frame-relay-switch.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Frame Relay switching routers retain Dynamips and the available C3640 appliance, with device-specific config packaging. Their source configuration text is preserved.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Optimus | Serial0/0 | Serial4/0 |
| Optimus | Serial0/1 | Serial4/1 |
| Optimus | Serial0/2 | Serial4/2 |
| Optimus | Serial0/3 | Serial4/3 |
| Bumblebee | Serial0/0 | Serial0/0 |
| Bumblebee | Serial0/1 | Serial0/1 |
| Bumblebee | Serial0/2 | Serial0/2 |
| Bumblebee | Serial0/3 | Serial0/3 |
| Ironhide | Serial0/0 | Serial4/0 |
| Ironhide | Serial0/1 | Serial4/1 |
| Ironhide | Serial0/2 | Serial4/2 |
| Ironhide | Serial0/3 | Serial4/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology:

## Video Solution:

http://www.youtube.com/watch?v=mJe18NW-V3Y
