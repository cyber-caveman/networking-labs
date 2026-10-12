# NAT TCP Load Balancing

## Scenario

You are working as a networking trainee and in your pasttime you enjoy troubleshooting networks. Your roommate has a huge website and has bought multiple webservers to host the website. He doesn't have any more money for a decent load balancer so he asks you if you know any other method to share traffic along the webservers. Let's see if you can keep your balance...

## Goal

- All IPv4 addresses have been preconfigured for you.
- Static routes have been configured on the webservers and the host for full connectivity.
- Configure HTTP server on all webservers.
- Whenever router host sends an IP packet to IP address 192.168.45.100 port 80 it should be load-balanced using round-robin among the webservers.

## GNS3 2.2.56.1

Import [NAT TCP Load Balancing IOU.gns3project](NAT%20TCP%20Load%20Balancing%20IOU.gns3project) using **File > Import portable project**. To open `NAT TCP Load Balancing.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Host | FastEthernet0/0 | Ethernet0/0 |
| NAT | FastEthernet0/0 | Ethernet0/0 |
| NAT | FastEthernet1/0 | Ethernet0/1 |
| WWW1 | FastEthernet0/0 | Ethernet0/0 |
| WWW2 | FastEthernet0/0 | Ethernet0/0 |
| WWW3 | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-nat-tcp-load-balancing.png)

## Video Solution

http://www.youtube.com/watch?v=hSbY2E4mVNU
