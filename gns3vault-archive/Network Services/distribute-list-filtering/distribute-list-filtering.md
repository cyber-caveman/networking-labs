# Distribute List Filtering

## Scenario

Ever since you were a child you wanted to be a trappist monk, the silence of the monastery and the science of trappist beer have been a part of your life as far as you can remember. Recently the monastery decided to cooperate with other monks to share information about the brewing process of trappist beer. One of the monks configured the routers and has setup redistribution between EIGRP and OSPF so there is full connectivity between the networks. However, your monastery holds some precious recipies that are not to be shared with everyone, you need to make sure access to these networks is filtered in the routing or redistribution process....Cheers!

## Goal

* All IP addresses have been preconfigured for you.
* OSPF and EIGRP have been preconfigured for you on the corresponding routers.
* Redistribution has been preconfigured for you on router Chimay.
* Router Orval and Achel both have 2 loopback interfaces:
  * Orval: L0: 1.1.1.1 and L1: 11.11.11.11
  * Achel: L0: 3.3.3.3 and L1: 33.33.33.33
* You are not allowed to make any changes to the network commands under the OSPF or EIGRP process.
* Ensure router Chimay does not advertise the 3.3.3.0 /24 network towards router Orval, use an access-list to accomplish this.
* Ensure router Orval does not advertise the 1.1.1.0 /24 network towards router Chimay, use a prefix-list to accomplish this.
* Ensure router Chimay does not redistribute the 11.11.11.0 network into OSPF, use a route-map to accomplish this.

## GNS3 2.2.56.1

Import [Distribute List Filtering IOU.gns3project](Distribute%20List%20Filtering%20IOU.gns3project) using **File > Import portable project**. To open `Distribute List Filtering.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Orval | FastEthernet0/0 | Ethernet0/0 |
| Chimay | FastEthernet0/0 | Ethernet0/0 |
| Chimay | FastEthernet1/0 | Ethernet0/1 |
| Achel | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-distribute-list-filtering.png)

## Video Solution

http://www.youtube.com/watch?v=ThdivcRrQQE
