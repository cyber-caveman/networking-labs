# Prefix List Filtering

## Scenario

As a true coffee addict and network junkie you are working on the network of a world famous coffeeshop. Today your caffeine rush kicks in and you have a sudden desire to clean up some of the routing tables on the company routers. Let's see what you can do here with a couple of prefix-lists. Black......no sugar, no milk!

## Goal

- All IP addresses have been preconfigured for you.
- EIGRP AS12 has been preconfigured for you.
- Router Mint advertises a bunch of prefixes to router Vanilla, take a quick look at the routing table to see them.
- You are only allowed to use one prefix-list.
- Create a single prefix-list statement to filter out all /32 networks in the 1.0.0.0 range, as a result the 1.0.0.0 /30's should still be in Vanilla's routing table.
- Create a single prefix-list statement to filter out any subnet in the Class B network range.
- Create a single prefix-list statement to filter out any subnet in the Class C network range that has a subnetmask of /25, /26 or /27. As a result all the Class C subnets with /24 or higher than /27 should still be in Vanilla's routing table.
- Create a single prefix-list statement to filter out all subnets in the 2.0.0.0 range which has less than 256 IP addresses.
- Change your prefix-list so that only the default-route is allowed, as a result only the default route should be in Vanilla's routing table.

## GNS3 2.2.56.1

Import [Prefix-list IOU.gns3project](Prefix-list%20IOU.gns3project) using **File > Import portable project**. To open `Prefix-list.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Vanilla | FastEthernet0/0 | Ethernet0/0 |
| Mint | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-prefix-list-filtering.png)

## Video Solution

http://www.youtube.com/watch?v=ZbRxRcn2Awk
