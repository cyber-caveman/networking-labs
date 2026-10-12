![Network Topology](./topology-bgp-neighbor-troubleshooting.png)

# BGP Neighbor Troubleshooting

## Scenario:

As the network engineer for a large corporation you are responsible for the configuration of BGP. One of your colleagues tried to install some new routers and configure BGP between them but he got stuck and is asking for your help. The BGP neighbor adjacencies are not even working so it's up to you to fix these...

## Goal:

- All IP addresses have been preconfigured for you.
- **Do not use show run**! (this will spoil the fun :) use the appropriate 'show' and 'debug' commands. This will teach you the skills needed to become a true troubleshooting master.
- Fix the BGP neighbor adjacency between AS1 and AS2. You are not allowed to change the neighbor commands.
- Fix the BGP neighbor adjacency between AS1 and AS3. You are not allowed to change the neighbor commands.
- Fix the BGP neighbor adjacency within AS3. You are not allowed to change the neighbor commands.

## GNS3 2.2.56.1

Import [BGP Neighbor Troubleshooting IOU.gns3project](BGP%20Neighbor%20Troubleshooting%20IOU.gns3project) using **File > Import portable project**. To open `BGP Neighbor Troubleshooting.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Amsterdam | FastEthernet0/0 | Ethernet0/0 |
| Amsterdam | FastEthernet1/0 | Ethernet0/1 |
| Miami | FastEthernet0/0 | Ethernet0/0 |
| NewYork | FastEthernet0/0 | Ethernet0/0 |
| NewYork | FastEthernet1/0 | Ethernet0/1 |
| Tokyo | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology:
