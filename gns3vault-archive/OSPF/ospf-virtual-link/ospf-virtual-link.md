# OSPF Virtual Link

## Scenario

You are a freelance network engineer specialized in routing and switching. One of your customers (a local butcher) has some trouble setting up their OSPF network. Some of the networks are not reachable and it's up to you to provide them with a solution.

## Goal

* All IP addresses have been preconfigured for you as specified in the topology picture.
* Each router has a loopback0 interface.
* Configure OSPF on all routers.
* Ensure you restore connectivity for the discontigious backbone area 0.
* Ensure area 2 has connectivity to the backbone area.

## Introduction

## GNS3 2.2.56.1

Import `OSPF Virtual Link IOU.gns3project` with **File > Import portable project**.
The archive includes the startup configs and the original topology illustration.
For direct opening, keep `OSPF Virtual Link.gns3` beside `project-files`.

Exercise routers use `x86_64_crb_linux-adventerprisek9-ms.bin`
(MD5 `4a2fce8de21d1831fbceffd155e41ae7`), 768 MB RAM, 128 KB NVRAM,
four Ethernet adapters and four serial adapters. Console ports are allocated automatically.

Startup and solution configs use the mapped IOU interfaces. Ethernet interfaces
retain the original bandwidth values in Kbit/s so OSPF metrics preserve the exercise.
Original reference images and legacy `.net` files may show the old interface names;
the converted `.gns3` project is the runnable topology.

| Router | Original interface | IOU interface |
| --- | --- | --- |
| Beef | FastEthernet0/0 | Ethernet0/0 |
| Beef | FastEthernet1/0 | Ethernet0/1 |
| Beef | FastEthernet2/0 | Ethernet0/2 |
| Chicken | FastEthernet0/0 | Ethernet0/0 |
| Fish | FastEthernet0/0 | Ethernet0/0 |
| Pork | FastEthernet0/0 | Ethernet0/0 |

Containerlab files are independent and unchanged. Structure, config packaging and
interface mappings were validated; boot and protocol behavior require the target
GNS3 server and the specified images.

## Topology

![Network Topology](./topology-ospf-virtual-link.png)

## Video Solution

[OSPF Virtual Link Solution Video](http://www.youtube.com/watch?v=39bDdpb4nT0)

## Configuration verification

Transit Area 1, reciprocal Chicken–Fish and Chicken–Pork virtual links and backbone/Area 2 networks retained.

Beef’s 2.2.2.2 loopback is not advertised by the source final config; full loopback reachability cannot be claimed.

These findings come from configuration analysis against the original files.
Boot, command support, adjacencies, routing tables and packet forwarding were not
tested live. See [the full verification report](../VERIFICATION.md) in the repository
(or `VERIFICATION.md` included in the portable archive).
