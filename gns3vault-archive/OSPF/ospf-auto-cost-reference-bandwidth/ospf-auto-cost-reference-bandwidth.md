# OSPF Auto Cost Reference Bandwidth

## Scenario

The new muppet movie is almost finished. All the actresses prefer to have a dedicated internet connection in their trailers at the movie park. You configure a couple of routers with Gigabit and FastEthernet interfaces. Unfortunately OSPF doesn't seem to make a difference between FastEthernet and Gigabit links. It's up to you to make the changes so it does see a difference...

## Goal

- All IP addresses have been preconfigured for you.
- Configure OSPF on all routers. Achieve full connectivity.
- Without changing the OSPF cost on each interface, ensure OSPF will make the best use of the Gigabit interfaces. In the future you will also add some ten Gigabit links so this is something to be aware of.

## GNS3 2.2.56.1

Import `OSPF Auto Cost Reference Bandwidth IOU.gns3project` with **File > Import portable project**.
The archive includes the startup configs and the original topology illustration.
For direct opening, keep `OSPF Auto Cost Reference Bandwidth.gns3` beside `project-files`.

Exercise routers use `x86_64_crb_linux-adventerprisek9-ms.bin`
(MD5 `4a2fce8de21d1831fbceffd155e41ae7`), 768 MB RAM, 128 KB NVRAM,
four Ethernet adapters and four serial adapters. Console ports are allocated automatically.

Startup and solution configs use the mapped IOU interfaces. Ethernet interfaces
retain the original bandwidth values in Kbit/s so OSPF metrics preserve the exercise.
Original reference images and legacy `.net` files may show the old interface names;
the converted `.gns3` project is the runnable topology.

| Router | Original interface | IOU interface |
| --- | --- | --- |
| Amy | GigabitEthernet1/0 | Ethernet0/0 |
| Amy | FastEthernet2/0 | Ethernet0/1 |
| Amy | FastEthernet2/1 | Ethernet0/2 |
| Amy | FastEthernet0/0 | Ethernet0/3 |
| Amy | FastEthernet0/1 | Ethernet1/0 |
| Emily | FastEthernet1/0 | Ethernet0/0 |
| Emily | FastEthernet1/1 | Ethernet0/1 |
| Emily | FastEthernet2/0 | Ethernet0/2 |
| Emily | FastEthernet2/1 | Ethernet0/3 |
| Emily | FastEthernet0/0 | Ethernet1/0 |
| Emily | FastEthernet0/1 | Ethernet1/1 |
| Mila | GigabitEthernet1/0 | Ethernet0/0 |
| Mila | GigabitEthernet2/0 | Ethernet0/1 |
| Mila | FastEthernet3/0 | Ethernet0/2 |
| Mila | FastEthernet3/1 | Ethernet0/3 |
| Mila | FastEthernet0/0 | Ethernet1/0 |
| Mila | FastEthernet0/1 | Ethernet1/1 |
| Selena | GigabitEthernet1/0 | Ethernet0/0 |
| Selena | FastEthernet2/0 | Ethernet0/1 |
| Selena | FastEthernet2/1 | Ethernet0/2 |
| Selena | FastEthernet0/0 | Ethernet0/3 |
| Selena | FastEthernet0/1 | Ethernet1/0 |

Containerlab files are independent and unchanged. Structure, config packaging and
interface mappings were validated; boot and protocol behavior require the target
GNS3 server and the specified images.

## Topology

![Network Topology](./topology-ospf-auto-cost-reference-bandwidth.png)

## Video Solution

[Video Solution on YouTube](http://www.youtube.com/watch?v=zN_z1DeJBP0)

## Configuration verification

Reference bandwidth 10000 Mbit/s retained; FastEthernet 100000 Kbit/s gives cost 100 and Gigabit 1000000 Kbit/s gives cost 10. Addresses and linked peers match the source.

Selena’s link toward Emily is unaddressed and shut in the source startup and final configs; retained.

These findings come from configuration analysis against the original files.
Boot, command support, adjacencies, routing tables and packet forwarding were not
tested live. See [the full verification report](../VERIFICATION.md) in the repository
(or `VERIFICATION.md` included in the portable archive).
