# OSPF LSA Type 3 summarization

## Scenario

The mineral express is specialized in trading expensive minerals. You are their senior network engineer and responsible for the OSPF network that they have running. One of your colleagues is complaining that the routing table is becoming too large. It's up to you to configure some summarization!

## Goal

- All IP addresses have been preconfigured for you.
- Configure OSPF on all routers. Achieve full connectivity.
- Router Talc and Fluorite have multiple loopback interfaces. Configure the network so Area 0 only sees a summary of these networks. Use the most optimal summary.

## About This Lab

## GNS3 2.2.56.1

Import `OSPF LSA Type 3 summarization IOU.gns3project` with **File > Import portable project**.
The archive includes the startup configs and the original topology illustration.
For direct opening, keep `OSPF LSA Type 3 summarization.gns3` beside `project-files`.

Exercise routers use `x86_64_crb_linux-adventerprisek9-ms.bin`
(MD5 `4a2fce8de21d1831fbceffd155e41ae7`), 768 MB RAM, 128 KB NVRAM,
four Ethernet adapters and four serial adapters. Console ports are allocated automatically.

Startup and solution configs use the mapped IOU interfaces. Ethernet interfaces
retain the original bandwidth values in Kbit/s so OSPF metrics preserve the exercise.
Original reference images and legacy `.net` files may show the old interface names;
the converted `.gns3` project is the runnable topology.

| Router | Original interface | IOU interface |
| --- | --- | --- |
| Diamond | FastEthernet0/0 | Ethernet0/0 |
| Diamond | FastEthernet1/0 | Ethernet0/1 |
| Fluorite | FastEthernet0/0 | Ethernet0/0 |
| Quartz | FastEthernet0/0 | Ethernet0/0 |
| Quartz | FastEthernet1/0 | Ethernet0/1 |
| Talc | FastEthernet0/0 | Ethernet0/0 |
| Topaz | FastEthernet0/0 | Ethernet0/0 |
| Topaz | FastEthernet1/0 | Ethernet0/1 |

Containerlab files are independent and unchanged. Structure, config packaging and
interface mappings were validated; boot and protocol behavior require the target
GNS3 server and the specified images.

## Topology

![Network Topology](./topology-ospf-lsa-type-3-summarization.png)

## Video Solution

[OSPF LSA Type 3 Summarization Lab Solution](http://www.youtube.com/watch?v=WMknpsFqtOM)

## Configuration verification

Area 0/1/2 assignments and ABR ranges 172.16.0.0/22 and 10.10.0.0/21 retained; ranges cover the configured loopback prefixes.

Actual Type 3 LSAs and routing tables not observed.

These findings come from configuration analysis against the original files.
Boot, command support, adjacencies, routing tables and packet forwarding were not
tested live. See [the full verification report](../VERIFICATION.md) in the repository
(or `VERIFICATION.md` included in the portable archive).
