# Multicast RPF Failure

## Scenario

As one of the network engineers for a national Tennis organization you are responsible for all Multicast operations. Multicast is vital for the organization because video replays of all Tennis matches are being sent within the company. Without Multicast the network will be burdened by traffic overhead.

## Goal

* Configure OSPF on all routers, advertise all networks. Achieve full connectivity.
* Configure dense-mode multicast only on routers LiveMatch, Ace, Alley and Backspin.
* Configure router Backspin to join the multicast group 224.4.4.4 on its FastEthernet interface.
* Make sure you can ping the 224.4.4.4 group address from router LiveMatch. You are not allowed to configure Multicast on router Backhand.

## GNS3 2.2.56.1

Import [multicast-rpf-failure-startup-configs IOU.gns3project](multicast-rpf-failure-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `multicast-rpf-failure-startup-configs.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Ace | FastEthernet1/0 | Ethernet0/0 |
| Ace | FastEthernet2/0 | Ethernet0/1 |
| Ace | Serial0/0 | Serial4/0 |
| Ace | Serial0/1 | Serial4/1 |
| Ace | Serial0/2 | Serial4/2 |
| Ace | Serial0/3 | Serial4/3 |
| Alley | FastEthernet1/0 | Ethernet0/0 |
| Alley | Serial0/0 | Serial4/0 |
| Alley | Serial0/1 | Serial4/1 |
| Alley | Serial0/2 | Serial4/2 |
| Alley | Serial0/3 | Serial4/3 |
| Backhand | FastEthernet0/0 | Ethernet0/0 |
| Backhand | FastEthernet1/0 | Ethernet0/1 |
| Backspin | FastEthernet0/0 | Ethernet0/0 |
| Backspin | FastEthernet1/0 | Ethernet0/1 |
| LiveMatch | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-multicast-rpf-failure.png)

## Video Solution

[Multicast RPF Failure Video Solution](http://www.youtube.com/watch?v=JHPd9hoa-Xs)
