# NAT Dynamic

## Scenario

Your friends Jack and Joe recently switched to a new Internet provider and instead of getting a single public IP address they have received multiple global IP addresses. To make sure all global IP addresses are used they ask you to configure NAT Dynamic for them. Action time!

## Goal

* All IPv4 addresses have been preconfigured for you.
* IP Routing has been disabled and a default gateway is configured on router Jack, Joe and WWW.
* Configure a pool for NAT Dynamic called "GNS3VAULT". The range of IP addresses you received from the Internet Provider is 172.16.0.1 - 172.16.0.100.
* Configure NAT Dynamic so when router Jack or Joe connect to router WWW they are translated to one of the IP addresses in the pool.

## GNS3 2.2.56.1

Import [NAT Dynamic IOU.gns3project](NAT%20Dynamic%20IOU.gns3project) using **File > Import portable project**. To open `NAT Dynamic.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Jack | FastEthernet0/0 | Ethernet0/0 |
| Joe | FastEthernet0/0 | Ethernet0/0 |
| NAT | FastEthernet0/0 | Ethernet0/0 |
| NAT | FastEthernet1/0 | Ethernet0/1 |
| NAT | FastEthernet2/0 | Ethernet0/2 |
| WWW | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-nat-dynamic.png)

## Video Solution

[NAT Dynamic - Video Solution](http://www.youtube.com/watch?v=jPcbcZQAJ6o)
