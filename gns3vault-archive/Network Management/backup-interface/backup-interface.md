# Backup Interface

## Scenario

You are responsible for a number of routers of a network that connects multiple cities. Whenever router Barcelona sends traffic towards Boston it has to use the link to Tilburg. Unfortunately it is load balancing since the paths are equal. You don't want to make any changes to the routing protocol because you don't want to impact the whole network. You decide to configure a backup interface on router Barcelona.

## Goal

- All IPv4 addresses have been preconfigured for you.
- EIGRP has been configured for connectivity.
- Configure router Barcelona so F1/0 is a backup interface. Whenever F0/0 goes down it should enable F1/0.

## GNS3 2.2.56.1

Import [Backup Interface IOU.gns3project](Backup%20Interface%20IOU.gns3project) using **File > Import portable project**. To open `Backup Interface.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Barcelona | FastEthernet1/0 | Ethernet0/0 |
| Barcelona | Serial0/0 | Serial4/0 |
| Barcelona | Serial0/1 | Serial4/1 |
| Barcelona | Serial0/2 | Serial4/2 |
| Barcelona | Serial0/3 | Serial4/3 |
| Venice | FastEthernet1/0 | Ethernet0/0 |
| Venice | FastEthernet0/0 | Ethernet0/1 |
| Tilburg | FastEthernet0/0 | Ethernet0/0 |
| Tilburg | Serial1/0 | Serial4/0 |
| Tilburg | Serial1/1 | Serial4/1 |
| Tilburg | Serial1/2 | Serial4/2 |
| Tilburg | Serial1/3 | Serial4/3 |
| Boston | FastEthernet1/0 | Ethernet0/0 |
| Boston | FastEthernet0/0 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-backup-interface.png)

## Video Solution

http://www.youtube.com/watch?v=2iIWtINTEiE
