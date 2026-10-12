# Frame-Relay Back to Back

## Scenario

You are working for a huge international car company as the senior network engineer. You need to connect a new branch office to the Headquarters. Since the company believes in proven technology they want you to connect the 2 sites by using Frame-Relay without a Frame-Relay switch.

## Goal

- You are not allowed to use the 'Frame-Relay Switching' command on any router.
- Configure Frame-Relay encapsulation on both Routers.
- Configure the IP addresses as specified in the topology picture.
- Use the DLCI numbers as specified in the topology picture.
- Achieve IP connectivity across the frame-relay link.

## GNS3 2.2.56.1

Import [frame-relay-back-to-back-startup-configs IOU.gns3project](frame-relay-back-to-back-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `frame-relay-back-to-back-startup-configs.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Bumblebee | Serial0/0 | Serial4/0 |
| Bumblebee | Serial0/1 | Serial4/1 |
| Bumblebee | Serial0/2 | Serial4/2 |
| Bumblebee | Serial0/3 | Serial4/3 |
| Ironhide | Serial0/0 | Serial4/0 |
| Ironhide | Serial0/1 | Serial4/1 |
| Ironhide | Serial0/2 | Serial4/2 |
| Ironhide | Serial0/3 | Serial4/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Frame-Relay Back to Back](http://d3w1odjdta16tt.cloudfront.net/images/stories/framerelayback2back.jpg)

## Video Solution

[Watch on YouTube](http://www.youtube.com/watch?v=NcURovS2YNA)
