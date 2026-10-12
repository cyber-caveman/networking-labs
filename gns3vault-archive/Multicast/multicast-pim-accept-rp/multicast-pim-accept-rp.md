# Multicast PIM Accept RP

![Network Topology](./topology-multicast-pim-accept-rp.jpg)

## Scenario

Since you are a excellent network engineer at the company you are working for, the network rarely has any problems and you have plenty of spare time. One of the days you were slacking off at the job and you implemented multicast on some of the routers to stream Star Trek videos across the network. Unfortunately some of your network colleagues found out and they are streaming some of their own videos using your configured rendezvous point (RP). Time to fix this before your the network is cluttered with useless video streams, after all you want your network career to be long and prosper...

## Goal

* All IP addresses have been preconfigured for you.
* Configure OSPF on all routers, achieve full connectivity.
* Configure sparse-mode multicast on all routers.
* Configure router Vulcan to be the rendezvous point (RP) in your network, use the loopback0 interface.
* Configure router Klingon to join the following 2 multicast groups:
  * 224.1.1.1 (Star Trek videos)
  * 224.2.2.2 (Company's funniest home videos)
* Configure router Vulcan so it only accepts the Star Trek video multicast group.
* Test this by pinging 224.1.1.1 and 224.2.2.2 from router Borg.

## GNS3 2.2.56.1

Import [multicast-pim-accept-rp-startup-configs IOU.gns3project](multicast-pim-accept-rp-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `multicast-pim-accept-rp-startup-configs.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Borg | FastEthernet0/0 | Ethernet0/0 |
| Klingon | FastEthernet0/0 | Ethernet0/0 |
| Vulcan | FastEthernet0/0 | Ethernet0/0 |
| Vulcan | FastEthernet1/0 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

## Video Solution

[Watch on YouTube](http://www.youtube.com/watch?v=m7IvlPV25IM)
