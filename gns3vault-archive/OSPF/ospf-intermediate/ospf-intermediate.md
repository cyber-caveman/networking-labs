# OSPF Intermediate

![Network Topology](./topology-ospf-intermediate.jpg)

## Scenario

As a network engineer you are familiar with the concepts of OSPF and single-area implementations, however you never tried to create a multi-area ospf configuration. You have heard about different area types like stubby, not so stubby but never encountered them in real life. You boot up your good old routers and prepare for the lab to change this once and for all.

## Goal

- All IP addresses have been preconfigured for you.
- Configure OSPF on all routers, achieve full connectivity. Make sure you can ping any IP Address from all routers. All networks should be in Area 0.
- Manually set the Router-ID of R1 to 1.1.1.2, make sure if you look at R2 or R3 that you really see the new router ID.
- Change OSPF so R3 becomes the designated router on the 192.168.34.X segment.
- Change the metric on the link between R1 and R2, do not use the ip ospf cost command for this.
- Change the reference bandwidth on all routers to 1500.
- Enable cleartext authentication between R2 and R4.
- Enable MD5 authentication between R3 and R4.
- On the link between R2 and R4, change the hello timer to 10 seconds and the dead-interval to 60 seconds.
- Insert a default route on R4 so that you see a 0.0.0.0/0 route in the routing table of R1, R2 and R3.
- Shutdown the link between R2 and R4.
- The link between R1 and R2, and R2's loopback interface should be configured as area 1.
- Configure area 1 as a not so stubby area (nssa).
- Configure R4's loopback0 interface as area 2.
- Create 4 loopbacks on R4:
  - Loopback10: 172.16.0.1 /24
  - Loopback11: 172.16.1.1 /24
  - Loopback12: 172.16.2.1 /24
  - Loopback13: 172.16.3.1 /24
- Advertise these networks in OSPF area 2 but make sure you only see a single entry (172.16.0.0 /22) in the routing table of R1, R2 and R3.
- Create another loopback on R4:
  - Loopback14: 172.16.4.1 /24
- You are not allowed to advertise this loopback in OSPF or by using redistribution. Ensure other routers can reach this loopback.

## GNS3 2.2.56.1

Import `OSPF Intermediate IOU.gns3project` with **File > Import portable project**.
The archive includes the startup configs and the original topology illustration.
For direct opening, keep `OSPF Intermediate.gns3` beside `project-files`.

Exercise routers use `x86_64_crb_linux-adventerprisek9-ms.bin`
(MD5 `4a2fce8de21d1831fbceffd155e41ae7`), 768 MB RAM, 128 KB NVRAM,
four Ethernet adapters and four serial adapters. Console ports are allocated automatically.

Startup and solution configs use the mapped IOU interfaces. Ethernet interfaces
retain the original bandwidth values in Kbit/s so OSPF metrics preserve the exercise.
Original reference images and legacy `.net` files may show the old interface names;
the converted `.gns3` project is the runnable topology.

| Router | Original interface | IOU interface |
| --- | --- | --- |
| R4 | FastEthernet0/0 | Ethernet0/0 |
| R4 | FastEthernet1/0 | Ethernet0/1 |
| R1 | FastEthernet0/0 | Ethernet0/0 |
| R1 | FastEthernet1/0 | Ethernet0/1 |
| R2 | FastEthernet0/0 | Ethernet0/0 |
| R2 | FastEthernet1/0 | Ethernet0/1 |
| R3 | FastEthernet0/0 | Ethernet0/0 |
| R3 | FastEthernet1/0 | Ethernet0/1 |

Containerlab files are independent and unchanged. Structure, config packaging and
interface mappings were validated; boot and protocol behavior require the target
GNS3 server and the specified images.

## Topology

## Video Solution

- http://www.youtube.com/watch?v=C2uc8qEacOM
- http://www.youtube.com/watch?v=cb5ai2zldug

## Configuration verification

Reference bandwidth 1500, 2000 Kbit/s R1–R2 bandwidth (cost 750), other Ethernet costs 15, matching authentication/dead timers, final R4–R2 shutdown, NSSA, /22 range and default origination retained.

Source final configs omit R1 router-id 1.1.1.2 and R4 Loopback14; R4 priority 200 favors R4 rather than the requested R3 DR. These pre-existing differences remain.

These findings come from configuration analysis against the original files.
Boot, command support, adjacencies, routing tables and packet forwarding were not
tested live. See [the full verification report](../VERIFICATION.md) in the repository
(or `VERIFICATION.md` included in the portable archive).
