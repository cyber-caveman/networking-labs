# OSPF NSSA (Not so stubby area)

![Network Topology](./topology-ospf-nssa-not-so-stubby-area.jpg)

## Scenario

You are the network engineer for a new service provider called "Mythical Bits". The routing protocol for the backbone of the network will be OSPF. To reduce the size of routing tables the company decided they want to create a design with different OSPF types like the "NSSA".

## Goal

- All IP addresses have been preconfigured for you, every router has a loopback interface:
  - Router Wodan: L0: 1.1.1.1 /24
  - Router Zeus: L0: 2.2.2.2 /24
  - Router Thor: L0: 3.3.3.3 /24

- Configure OSPF on all routers, configure the areas as specified in the topology picture.
- Router Wodan: Loopback0 should be Area 0.
- Router Zeus: Loopback0 should be Area 4.
- Area 4 has no direct connection to Area 0, solve this by using OSPF commands.
- Ensure you have full reachability.
- Configure Area 3 into a NSSA (Not so stubby area).

- Router Thor: add the following loopbacks:
  - Loopback1: 172.16.0.3 /24
  - Loopback2: 172.16.1.3 /24

- Advertise these networks into OSPF, do not use the "network" command to achieve this!
- Router Thor: configure a summary towards Area 0 for the 2 loopbacks you just created, make sure you do not advertise networks you do not have.

- Router Zeus: add the following loopbacks:
  - Loopback1: 172.16.2.2 /24
  - Loopback2: 172.16.3.2 /24

- Router Zeus: configure a summary towards Area 0 for the 2 loopbacks you just created, make sure you do not advertise networks you do not have.
- When you look in the routing table of Router Wodan you see some of the loopbacks advertised as /32's. Make sure you see the correct subnet mask that has been configured.

## GNS3 2.2.56.1

Import `OSPF Nssa IOU.gns3project` with **File > Import portable project**.
The archive includes the startup configs and the original topology illustration.
For direct opening, keep `OSPF Nssa.gns3` beside `project-files`.

Exercise routers use `x86_64_crb_linux-adventerprisek9-ms.bin`
(MD5 `4a2fce8de21d1831fbceffd155e41ae7`), 768 MB RAM, 128 KB NVRAM,
four Ethernet adapters and four serial adapters. Console ports are allocated automatically.

Startup and solution configs use the mapped IOU interfaces. Ethernet interfaces
retain the original bandwidth values in Kbit/s so OSPF metrics preserve the exercise.
Original reference images and legacy `.net` files may show the old interface names;
the converted `.gns3` project is the runnable topology.

| Router | Original interface | IOU interface |
| --- | --- | --- |
| Wodan | Serial0/0 | Serial4/0 |
| Wodan | Serial0/1 | Serial4/1 |
| Wodan | Serial0/2 | Serial4/2 |
| Wodan | Serial0/3 | Serial4/3 |
| Zeus | Serial0/0 | Serial4/0 |
| Zeus | Serial0/1 | Serial4/1 |
| Zeus | Serial0/2 | Serial4/2 |
| Zeus | Serial0/3 | Serial4/3 |
| Thor | Serial0/0 | Serial4/0 |
| Thor | Serial0/1 | Serial4/1 |
| Thor | Serial0/2 | Serial4/2 |
| Thor | Serial0/3 | Serial4/3 |

Containerlab files are independent and unchanged. Structure, config packaging and
interface mappings were validated; boot and protocol behavior require the target
GNS3 server and the specified images.

## Topology

## Video Solution

http://www.youtube.com/watch?v=byptcizL3lM

## Configuration verification

Serial peer addressing, Area 3 NSSA, connected redistribution, 172.16.0.0/23 external summary, reciprocal Area 2 virtual links and Area 4 172.16.2.0/23 range retained.

Loopback network-type settings remain exactly as supplied; full advertised-mask behavior was not established live.

These findings come from configuration analysis against the original files.
Boot, command support, adjacencies, routing tables and packet forwarding were not
tested live. See [the full verification report](../VERIFICATION.md) in the repository
(or `VERIFICATION.md` included in the portable archive).
