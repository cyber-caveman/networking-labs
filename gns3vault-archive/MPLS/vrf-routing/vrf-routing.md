# VRF Routing

## Scenario

As the captain of an interstellar spaceship you are responsible for the well-being of your ship. You need to setup a secure line to exchange information between your crewmembers. You are going to use a technique that was created 200 years ago called VRF Routing. Back then this technique was the basis of MPLS and you need to make sure your crewmembers fully understand it before they dive deeper into MPLS....engage!

## Goal

All IP addresses have been preconfigured for you.

- Router Sulu and Chekov both have a loopback0 and loopback1 interface we are going to use for VRFs.
- Configure VRF SULU on router Sulu, add the loopback0 and loopback1 interface to this VRF.
- Configure VRF CHEKOV on router Chekov, add the loopback0 and loopback1 interface to this VRF.
- Configure the tunnel1 interface on both routers. Make sure the source and destination IP addresses of the Fastethernet link are used for this.
- Make sure the tunnel1 interface is added to VRF SULU and CHEKOV.
- Configure the 192.168.21.0 /24 subnet on the tunnel1 interface.
- Configure EIGRP AS 12 as the routing protocol for these VRFs. Make sure both routers can ping each others loopback interfaces.

## GNS3 2.2.56.1

Import [vrf-routing-startup-configs IOU.gns3project](vrf-routing-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `vrf-routing-startup-configs.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Chekov | FastEthernet0/0 | Ethernet0/0 |
| Sulu | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-vrf-routing.png)

## Video Solution

[Video Solution on YouTube](http://www.youtube.com/watch?v=1ggrVqnKGAw)
