# NAT Port Forwarding

## Scenario

Your network at home has been configured for NAT so you and the rest of your family can access the Internet. You also have a webserver and a SSH server at home and you would like those to be accessible to the rest of the world. Time for some good old port forwarding on your Cisco router.

## Goal

- All IPv4 addresses have been preconfigured for you.
- Static routes have been configured on the webservers and the host for full connectivity.
- When router Host sends an IP packet to IP address 192.168.34.3 port 80 it should be sent to the webserver.
- When router Host sends an IP packet to IP address 192.168.34.3 port 22 it should be sent to the SSH server.

## About This Lab

## GNS3 2.2.56.1

Import [NAT Port Forwarding IOU.gns3project](NAT%20Port%20Forwarding%20IOU.gns3project) using **File > Import portable project**. To open `NAT Port Forwarding.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Host | FastEthernet0/0 | Ethernet0/0 |
| Host | FastEthernet1/0 | Ethernet0/1 |
| NAT | FastEthernet0/0 | Ethernet0/0 |
| NAT | FastEthernet1/0 | Ethernet0/1 |
| SSH | FastEthernet0/0 | Ethernet0/0 |
| Web | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-nat-port-forwarding.png)

## Video Solution

[Watch on YouTube](http://www.youtube.com/watch?v=WW8156W4Xao)
