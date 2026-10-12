# HSRP Troubleshooting

![Network Topology](./topology-hsrp-troubleshooting.png)

## Scenario:

Hot Standby Routing Protocol is configured on an inter-city network and you are responsible for the configuration. While you were on vacation one of your colleagues tried to "tune" HSRP to make it failover faster. Unfortunately he totally messed up the configuration and he asks you to restore it back to normal. There are no backup configurations so you'll have to fix it yourself...time to put that martini aside and fix things!

## Goal:

- All IP addresses have been preconfigured for you.
- **Do not use show run**! (this will spoil the fun :) use the appropriate 'show' and 'debug' commands. This will teach you the skills needed to become a true troubleshooting master.
- Router NewYork, NewJersey and LA are configured for HSRP so router Host has a virtual gateway IP address.
- Fix HSRP so router NewYork, NewJersey and LA are in the same HSRP Group and form a single virtual gateway.
- Each HSRP router should be able to become the active router and forward IP packets from the host to the ISP.

## GNS3 2.2.56.1

Import [HSRP Troubleshooting IOU.gns3project](HSRP%20Troubleshooting%20IOU.gns3project) using **File > Import portable project**. To open `HSRP Troubleshooting.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Host | FastEthernet0/0 | Ethernet0/0 |
| ISP | FastEthernet0/0 | Ethernet0/0 |
| LA | FastEthernet0/0 | Ethernet0/0 |
| LA | FastEthernet1/0 | Ethernet0/1 |
| NewJersey | FastEthernet0/0 | Ethernet0/0 |
| NewJersey | FastEthernet1/0 | Ethernet0/1 |
| NewYork | FastEthernet0/0 | Ethernet0/0 |
| NewYork | FastEthernet1/0 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology:
