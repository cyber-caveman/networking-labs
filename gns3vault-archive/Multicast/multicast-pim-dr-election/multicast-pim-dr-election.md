# Multicast PIM DR Election

![Network Topology](./topology-multicast-pim-dr-election.jpg)

## Scenario

Your have been streaming Star Trek videos by using multicast on your corporate network for quite some time without anyone noticing...recently one of your colleagues found you out...he's going to tell your boss unless you agree to him and stream some of his favorite Star Wars videos as well. You don't want to make a lot of changes to the network, but router Spock will not enough capacity to send this much traffic, you will need to change router Kirk to be the Designated Router (DR) for our multicast setup....may the force be with you...

## Goal

* All IP addresses have been preconfigured for you.
* Configure OSPF on all routers, achieve full connectivity.
* Configure sparse-mode multicast on all routers.
* Configure router Picard to be the rendezvous point (RP) in your network, use the loopback0 interface.
* Configure router Picard to be the mapping agent (MP) in your network, use the loopback0 interface.
* Configure router Scotty to join the following multicast group: 224.1.1.1
* Start a ping from router Picard to the multicast group address 224.1.1.1 to generate traffic.
* Make sure router Spock is the Designated Router (DR) and forwards multicast traffic towards router Scotty.

## GNS3 2.2.56.1

Import [multicast-pim-dr-election-startup-configs IOU.gns3project](multicast-pim-dr-election-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `multicast-pim-dr-election-startup-configs.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Kirk | FastEthernet0/0 | Ethernet0/0 |
| Kirk | FastEthernet1/0 | Ethernet0/1 |
| Picard | FastEthernet0/0 | Ethernet0/0 |
| Picard | FastEthernet1/0 | Ethernet0/1 |
| Scotty | FastEthernet0/0 | Ethernet0/0 |
| Spock | FastEthernet0/0 | Ethernet0/0 |
| Spock | FastEthernet1/0 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

## Video Solution

[http://www.youtube.com/watch?v=PX18OqVh52w](http://www.youtube.com/watch?v=PX18OqVh52w)
