# Role Based CLI Access

## Scenario

As the security specialist for your company you want to ensure employees don't get more access than they need to. At this moment everyone is logging in using privilege level 15 for your routers and you want to ensure this doesn't happen anymore in the future.

## Goals

- All IP addresses have been preconfigure for you.
- Configure a role called "TRAINEE" on router Rollin.
- Role "TRAINEE" should be able to change the IP address on loopback0.
- Configure a role called "DEBUG" on router Rollin.
- Role "DEBUG" should be able to use all debug commands.
- Configure a role called "ALLMIGHTY" on router Rollin.
- Role "ALLMIGHTY" should be able to do whatever role "TRAINEE" and "DEBUG" can do.
- To authenticate the roles you should use password "VAULT".

## GNS3 2.2.56.1

Import [Role-Based CLI Access IOU.gns3project](Role-Based%20CLI%20Access%20IOU.gns3project) using **File > Import portable project**. To open `Role-Based CLI Access.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-role-based-cli-access.png)

## Video Solution

[Video Solution on YouTube](http://www.youtube.com/watch?v=XOBzlMOZ2Bs)
