# Login Menu

## Scenario

You are a network teacher specialized in routing and switching. To help your students who are not so familiar with the command-line you want to use one of your routers so it displays a menu everytime they login.

## Goal

- All IP addresses have been preconfigured for you (except router Flynn).
- Configure router Classroom so whenever users telnet to it with username "STUDENT" and password "VAULT" they get a menu with the following options:

1. Show ip interface brief.
2. Show ip protocols.
3. Logout.

## GNS3 2.2.56.1

Import [Login Menu IOU.gns3project](Login%20Menu%20IOU.gns3project) using **File > Import portable project**. To open `Login Menu.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Classroom | FastEthernet0/0 | Ethernet0/0 |
| Student | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-login-menu.png)

## Video Solution

http://www.youtube.com/watch?v=jPwLIsQSyc4
