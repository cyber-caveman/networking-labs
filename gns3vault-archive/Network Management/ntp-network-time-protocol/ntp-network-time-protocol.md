# NTP (Network Time Protocol)

## Scenario

You are the owner of a Swiss watch factory. Time is everything to you and the same applies to your network. You want to make sure that your complete network is synchronized and up-to-date. Now get going since time is money!

## Goal

* All IP addresses have been preconfigured for you.
* EIGRP has been configured for full connectivity.
* Configure router Planck and Atomic to be NTP Masters, use stratum 10.
* Make sure router Planck and Atomic synchronize with each other.
* Router Julian has to check router Planck and Atomic for NTP updates, it has to prefer router Atomic.
* Configure router Julian so it broadcasts NTP packets on its FastEthernet 1/0 interface.
* Configure router Century so it configures itself using the NTP broadcast packets from router Julian.
* Configure router Planck to send NTP packets to multicast address 239.5.5.5.
* Configure router Millenium to configure itself using the NTP multicast packets.

## GNS3 2.2.56.1

Import [NTP (Network Time Protocol) IOU.gns3project](NTP%20%28Network%20Time%20Protocol%29%20IOU.gns3project) using **File > Import portable project**. To open `NTP (Network Time Protocol).gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Atomic | FastEthernet0/0 | Ethernet0/0 |
| Atomic | FastEthernet1/0 | Ethernet0/1 |
| Century | FastEthernet0/0 | Ethernet0/0 |
| Julian | FastEthernet0/0 | Ethernet0/0 |
| Julian | FastEthernet1/0 | Ethernet0/1 |
| Millenium | FastEthernet0/0 | Ethernet0/0 |
| Planck | FastEthernet0/0 | Ethernet0/0 |
| Planck | FastEthernet1/0 | Ethernet0/1 |
| Planck | FastEthernet2/0 | Ethernet0/2 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-ntp-network-time-protocol.png)

## Video Solution

[http://www.youtube.com/watch?v=3rFSwtPnp3g](http://www.youtube.com/watch?v=3rFSwtPnp3g)
