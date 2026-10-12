# PPP Authentication

![Network Topology](./topology-ppp-authentication.jpg)

## Scenario

The puppet business is becoming more popular everyday and that's why your boss decided to have redundant links between the 2 sites. Since they are afraid of company espionage you also need to configure authentication.

## Goals

- All IP addresses have been preconfigured as specified in the topology picture.
- Configure both links for encapsulation PPP.
- Use PAP authentication on the 10.10.12.0 link, use password "VAULT".
- Use CHAP authentication on the 10.11.12.0 link, use password "CISCO".

## GNS3 2.2.56.1

Import [ppp-authentication-startup-configs IOU.gns3project](ppp-authentication-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `ppp-authentication-startup-configs.gns3` directly, keep it beside `project-files`.

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

http://www.youtube.com/watch?v=tmesuyp9qmc
