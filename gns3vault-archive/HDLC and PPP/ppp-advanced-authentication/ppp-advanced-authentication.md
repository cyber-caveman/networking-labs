# PPP Advanced Authentication

![Network Topology](./topology-ppp-advanced-authentication.jpg)

## Scenario

After configuring some basic PPP authentication, the management of the puppet business decided they want to increase security. One of the things they want you to do is change the behavior of using the hostname as username.

## Goal

- Configure the IP addresses as specified in the topology picture.
- Configure the correct hostname on both routers.
- Configure both links for encapsulation PPP.
- Router Kermit should authenticate Grover by using PAP, if it fails it should switch to CHAP, use the S0/0 interfaces.
- Router Grover should refuse PAP authentication and use CHAP authentication, use the S0/0 interfaces.
- Router Kermit should use the alternate CHAP hostname "MUPPET". You are not allowed to change the hostname of any router, use the S0/0 interfaces.
- Configure both routers to they want to authenticate the PPP connection on the S0/1 interfaces by using the fictional radius server at IP address 1.1.1.1, use password "MUPPET" for the fictional radius server.
- In case the radius server fails both routers should use the local database for authentication.

## GNS3 2.2.56.1

Import [ppp-advanced-startup-configs IOU.gns3project](ppp-advanced-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `ppp-advanced-startup-configs.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Grover | Serial0/0 | Serial4/0 |
| Grover | Serial0/1 | Serial4/1 |
| Grover | Serial0/2 | Serial4/2 |
| Grover | Serial0/3 | Serial4/3 |
| Kermit | Serial0/0 | Serial4/0 |
| Kermit | Serial0/1 | Serial4/1 |
| Kermit | Serial0/2 | Serial4/2 |
| Kermit | Serial0/3 | Serial4/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

## Video Solution

[YouTube Video](http://www.youtube.com/watch?v=grb4QyZCB7I)
