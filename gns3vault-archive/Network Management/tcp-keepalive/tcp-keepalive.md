# TCP Keepalive

## Scenario

A well-known science laboratory specialized in researching "portal" technology has a small network running OSPF. One of their terminals is used by a scientist to reach a central server. However every time router Alive crashes it's impossible to re-connect to the central server. Besides a scientist you are also a network engineer, let's see if you can portal yourself out of this one...

## Goal

* All IP addresses have been preconfigured for you.
* OSPF has been configured for connectivity.
* Configure router Terminal so it detects dead TCP connections and closes them.
* You can test this by using telnet on router Server to router Terminal and shutting the F1/0 interface on router Alive afterwards to simulate a dead connection.

## GNS3 2.2.56.1

Import [TCP Keepalive IOU.gns3project](TCP%20Keepalive%20IOU.gns3project) using **File > Import portable project**. To open `TCP Keepalive.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Alive | FastEthernet0/0 | Ethernet0/0 |
| Alive | FastEthernet1/0 | Ethernet0/1 |
| Server | FastEthernet0/0 | Ethernet0/0 |
| Still | FastEthernet0/0 | Ethernet0/0 |
| Still | FastEthernet1/0 | Ethernet0/1 |
| Terminal | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-tcp-keepalive.png)

## Video Solution

[Watch on YouTube](http://www.youtube.com/watch?v=2Oo3Asc-OYI)
