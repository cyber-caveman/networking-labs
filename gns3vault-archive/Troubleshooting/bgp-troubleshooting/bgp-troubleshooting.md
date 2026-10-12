# BGP Troubleshooting

## Scenario

The fermentum corporation has hired you to troubleshoot their international network that consists of BGP routers. There are a number of issues. Some BGP routers are unable to establish a neighbor adjacency and others are having issues with prefixes not showing up in the routing tables. You have access to all devices so it's time to fix this network!

## Goal

* All IP addresses have been preconfigured for you.
* **Do not use show run**! (this will spoil the fun :) use the appropiate 'show' and 'debug' commands. This will teach you the skills needed to become a true troubleshooting master.
* The EBGP neighbor adjacency between router Dhaka and Berlin is not working, fix it!
* The EBGP neighbor adjacency between router NewDelhi and Amsterdam is not working, solve this issue!
* Router Berlin is supposed to receive the 11.11.0.0/16 prefix from router Dhaka but you don't see it in the BGP table, see if you can fix it.
* Router Amsterdam is not receiving any prefixes through BGP from within AS 2, get rid of this problem.
* Router Amsterdam is expecting the 5.5.5.0/24 prefix from router NewDelhi but you don't see it in it's BGP table.
* Router Amsterdam should now have 1.1.1.0/24 in its routing table, however if you try to ping it you cannot reach it...fix this.
* Whenever you send traffic from router Dhaka to NewDelhi nothing will arrive, make the required changes to fix this problem.

## GNS3 2.2.56.1

Import [BGP Troubleshooting IOU.gns3project](BGP%20Troubleshooting%20IOU.gns3project) using **File > Import portable project**. To open `BGP Troubleshooting.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Amsterdam | FastEthernet0/0 | Ethernet0/0 |
| Amsterdam | FastEthernet1/0 | Ethernet0/1 |
| Berlin | FastEthernet0/0 | Ethernet0/0 |
| Berlin | FastEthernet1/0 | Ethernet0/1 |
| Dhaka | FastEthernet0/0 | Ethernet0/0 |
| NewDelhi | FastEthernet0/0 | Ethernet0/0 |
| Paris | FastEthernet0/0 | Ethernet0/0 |
| Paris | FastEthernet1/0 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-bgp-troubleshooting.png)
