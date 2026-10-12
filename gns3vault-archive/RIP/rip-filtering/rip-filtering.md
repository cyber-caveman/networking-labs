# RIP Filtering

## Scenario

You are the owner of a Dutch webshop selling Dutch export products. Recently there have been problems on the network, some users had access to certain parts of the network without authorization. You want to use a RIP solution to filter some of the networks. See if you can dutchify this network...

## Goal

- All IP addresses have been preconfigured for you.
- All routers have a loopback interface as following:
  - WoodenShoe: 1.1.1.1/24
  - Cheese: 2.2.2.2/24
  - Tulip: 3.3.3.3/24
  - Windmill: 4.4.4.4/24
- Configure RIP version 2 on all routers, achieve full connectivity for all networks (including the loopbacks).
- You notice router WoodenShoe is sending RIP updates to the loopback interface, you have to stop this.
- Create a prefix-list so router Cheese doesn't advertise its loopback0 interface to router Windmill.
- Create an access-list so router Tulip doesn't accept network 1.1.1.0/24.
- Create an offset-list so router Windmill doesn't accept network 3.3.3.0/24.
- Change the AD (Administrative Distance) so router WoodenShoe doesn't place network 2.2.2.0/24 in its routing table.

## GNS3 2.2.56.1

Import [RIP Filtering IOU.gns3project](RIP%20Filtering%20IOU.gns3project) using **File > Import portable project**. To open `RIP Filtering.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Cheese | FastEthernet0/0 | Ethernet0/0 |
| Cheese | FastEthernet1/0 | Ethernet0/1 |
| Tulip | FastEthernet0/0 | Ethernet0/0 |
| Tulip | FastEthernet1/0 | Ethernet0/1 |
| Windmill | FastEthernet0/0 | Ethernet0/0 |
| Windmill | FastEthernet1/0 | Ethernet0/1 |
| WoodenShoe | FastEthernet0/0 | Ethernet0/0 |
| WoodenShoe | FastEthernet1/0 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-rip-filtering.png)

## Video Solution

[View on YouTube](http://www.youtube.com/watch?v=YlTLPlqeRjY)
