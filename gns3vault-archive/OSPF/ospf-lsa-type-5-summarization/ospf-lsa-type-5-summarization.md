# OSPF LSA Type 5 summarization

## Scenario

As the junior network engineer for a large cartoon network you are asked to look at the OSPF configuration of the network. Some external networks are redistributed into OSPF and your boss asks you if you can summarize them so the routing table stays small. Your colleague tried some summary commands but couldn't get it working...see if you can fix it!

## Goal

- All IP addresses have been preconfigured for you.
- Configure OSPF on all routers. Advertise all physical interfaces.
- Router Sam has a number of loopback interfaces. Redistribute them in OSPF so they show up as external routes on router Jack.
- Configure OSPF so there are two summaries for the loopback interfaces of router Sam. Use the most optimal summaries.

## GNS3 2.2.56.1

Import `OSPF LSA Type 5 summarization IOU.gns3project` with **File > Import portable project**.
The archive includes the startup configs and the original topology illustration.
For direct opening, keep `OSPF LSA Type 5 summarization.gns3` beside `project-files`.

Exercise routers use `x86_64_crb_linux-adventerprisek9-ms.bin`
(MD5 `4a2fce8de21d1831fbceffd155e41ae7`), 768 MB RAM, 128 KB NVRAM,
four Ethernet adapters and four serial adapters. Console ports are allocated automatically.

Startup and solution configs use the mapped IOU interfaces. Ethernet interfaces
retain the original bandwidth values in Kbit/s so OSPF metrics preserve the exercise.
Original reference images and legacy `.net` files may show the old interface names;
the converted `.gns3` project is the runnable topology.

| Router | Original interface | IOU interface |
| --- | --- | --- |
| Harry | FastEthernet0/0 | Ethernet0/0 |
| Harry | FastEthernet1/0 | Ethernet0/1 |
| Jack | FastEthernet0/0 | Ethernet0/0 |
| Sam | FastEthernet0/0 | Ethernet0/0 |

Containerlab files are independent and unchanged. Structure, config packaging and
interface mappings were validated; boot and protocol behavior require the target
GNS3 server and the specified images.

## Topology

![Network Topology](./topology-ospf-lsa-type-5-summarization.png)

## Video Solution

[Video Solution on YouTube](http://www.youtube.com/watch?v=4c-YooOgQPM)

## Configuration verification

Sam’s connected redistribution and two /22 summary-address statements retained.

Harry has no OSPF process in the source final config, preventing the intended end-to-end OSPF exchange; retained as a source defect.

These findings come from configuration analysis against the original files.
Boot, command support, adjacencies, routing tables and packet forwarding were not
tested live. See [the full verification report](../VERIFICATION.md) in the repository
(or `VERIFICATION.md` included in the portable archive).
