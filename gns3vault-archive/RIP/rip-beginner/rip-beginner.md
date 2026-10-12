# RIP Beginner

![Network Topology](./topology-rip-beginner.jpg)

## Scenario

You are working for a company located in the Netherlands. Your manager is the nostalgic kind of guy and wants you to configure the RIP Routing protocol on all of their routers. You try to convince him to run OSPF or EIGRP because of faster convergence, but to no avail....time to get the job done.

## Goal

- All IP addresses have been preconfigured for you.
- All routers have a loopback interface as following:
  - Amsterdam: 1.1.1.1/24
  - Rotterdam: 2.2.2.2/24
  - Utrecht: 3.3.3.3/24
- Configure RIP version 1 on all routers, achieve full connectivity for all networks (including the loopbacks)
- Utrecht: configure RIP version 2
- Utrecht: make sure you accept version 1 and 2 routing updates.
- All Routers: make sure you are only running version 2
- Change the configuration on all routers so the subnetmask is sent along with the routing updates.
- Amsterdam: make sure no routing updates are sent to the loopback interface.
- All routers: Change the RIP timers so routing updates happen every 10 seconds.
- Utrecht: Advertise a default route into RIP.

## Additional Information

## GNS3 2.2.56.1

Import [rip-beginner-startup-configs IOU.gns3project](rip-beginner-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `rip-beginner-startup-configs.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Amsterdam | FastEthernet0/0 | Ethernet0/0 |
| Rotterdam | FastEthernet0/0 | Ethernet0/0 |
| Rotterdam | FastEthernet1/0 | Ethernet0/1 |
| Utrecht | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

## Video Solution

[Video Solution on YouTube](http://www.youtube.com/watch?v=AgTn1XI6A30)
