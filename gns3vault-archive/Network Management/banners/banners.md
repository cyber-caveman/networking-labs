# Banners

## Scenario

You are a teacher at large university and responsible for all network equipment. You want to make sure all students see the correct banners whenever they logon one of the routers.

## Goal

* All IP addresses have been preconfigured for you.
* Everyone that telnets to router Classroom should see a message "Welcome to the classroom".
* Reverse telnet connections should see a message "Let's go reverse!".
* All users that connect to the classroom router should see which line is in use and the classroom router should report it's hostname.

## GNS3 2.2.56.1

Import [Banners IOU.gns3project](Banners%20IOU.gns3project) using **File > Import portable project**. To open `Banners.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Classroom | FastEthernet0/0 | Ethernet0/0 |
| Student | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-banners.png)
