# IPv6 NAT-PT Static

## Scenario

You are working for a large international mining company and responsible for the migration strategy towards IPv6. The ISP has run out of IPv4 addresses and can only supply you with fresh new IPv6 addresses. In order to connect the new "Gold" and "Silver" sites you will need to perform NAT-PT...start digging!

## Goal

- All IPv4 and IPv6 addresses have been preconfigured for you.
- All routers have a default route towards router NATPT.
- Configure NAT-PT and make sure router Platinum is reachable as 2001::C0A8:7B01.
- Configure NAT-PT and make sure router Bronze is reachable as 2001::C0A8:7B02.
- Configure NAT-PT and make sure router Gold is reachable as 192.168.123.4.
- Configure NAT-PT and make sure router Silver is reachable as 192.168.123.5.
- Your configuration is correct when you have full connectivity.

## GNS3 2.2.56.1

Import [IPv6-NAT-PT IOU.gns3project](IPv6-NAT-PT%20IOU.gns3project) using **File > Import portable project**. To open `IPv6-NAT-PT.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Bronze | FastEthernet0/0 | Ethernet0/0 |
| Bronze | FastEthernet0/1 | Ethernet0/1 |
| Gold | FastEthernet0/0 | Ethernet0/0 |
| Gold | FastEthernet0/1 | Ethernet0/1 |
| NATPT | FastEthernet0/0 | Ethernet0/0 |
| NATPT | FastEthernet0/1 | Ethernet0/1 |
| Platinum | FastEthernet0/0 | Ethernet0/0 |
| Platinum | FastEthernet0/1 | Ethernet0/1 |
| Silver | FastEthernet0/0 | Ethernet0/0 |
| Silver | FastEthernet0/1 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-ipv6-nat-pt-static.png)

## Video Solution

[YouTube Video Solution](http://www.youtube.com/watch?v=-fVr2Z1Pzc4)
