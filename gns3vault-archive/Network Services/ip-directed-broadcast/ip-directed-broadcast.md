# IP Directed Broadcast

## Scenario

The smurfs got tired of recording cartoons so they decided to become network engineers. Unfortunately they are still using a very old application that only works using broadcast traffic. You need to change the network so it's possible for them to use the application.

## Goal

- All IP addresses have been preconfigured for you.
- Configure the network so router Smurf can send packets to IP address 192.168.23.255

## GNS3 2.2.56.1

Import [IP Directed Broadcast IOU.gns3project](IP%20Directed%20Broadcast%20IOU.gns3project) using **File > Import portable project**. To open `IP Directed Broadcast.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Gargamel | FastEthernet0/0 | Ethernet0/0 |
| Gargamel | FastEthernet1/0 | Ethernet0/1 |
| Papa | FastEthernet0/0 | Ethernet0/0 |
| Smurf | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-ip-directed-broadcast.png)

## Video Solution

http://www.youtube.com/watch?v=cYlz0h5NHbA
