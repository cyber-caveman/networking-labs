# Server Load Balancing (SLB)

![Network Topology](./topology-server-load-balancing-slb.png)

## Scenario:

You are the senior network engineer for a large online webshop called "Booky Wooky". One of your load balancers recently failed and you don't have any replacement...business hasn't been so good since the ereaders have been launched a few years ago. You decide to take a spare router and configure it for load balancing...

## Goal:

* All IP addresses have been preconfigured for you.
* Configure router SLB so it spreads connections to the webserver in a round-robin fashion to router WWW1 and WWW2.
* Configure router SLB so WWW1 gets twice as many connections as WWW2.

## GNS3 2.2.56.1

Import [Server Load Balancing (SLB) IOU.gns3project](Server%20Load%20Balancing%20%28SLB%29%20IOU.gns3project) using **File > Import portable project**. To open `Server Load Balancing (SLB).gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Jack | FastEthernet0/0 | Ethernet0/0 |
| James | FastEthernet0/0 | Ethernet0/0 |
| SLB | FastEthernet0/0 | Ethernet0/0 |
| SLB | FastEthernet1/0 | Ethernet0/1 |
| SLB | FastEthernet2/0 | Ethernet0/2 |
| WWW1 | FastEthernet0/0 | Ethernet0/0 |
| WWW2 | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology:

## Video Solution:

http://www.youtube.com/watch?v=J9sEB2kOqLw
