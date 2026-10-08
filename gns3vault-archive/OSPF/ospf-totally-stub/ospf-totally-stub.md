# OSPF Totally Stub

![Network Topology](./topology-ospf-totally-stub.jpg)

## Scenario:

This lab is a follow-up of the OSPF Stub lab. I'd recommend you configure that lab before this one. The company specialized in selling Fantasy E-books is becoming more popular everyday and after your trainee period they decided to offer you a job. They still don't have any money to upgrade their network equipment and they are still experiencing problems with big routing tables... time to tune OSPF some more!

## Goal:

- All IP addresses have been preconfigured for you.
- Configure OSPF on both routers, use the Area's as specified in the topology picture.
- Router Algrim: Loopback0 should be in Area0
- Achieve full connectivity.
- Router Algrim: create additional loopbacks:
  - L1: 172.16.0.1 /24
  - L2: 172.16.1.1 /24
  - L3: 172.16.2.1 /24
  - L4: 172.16.3.1 /24
- Advertise these networks into OSPF Area 0.
- Take a look at the routing table of Router Barik, you should see all 4 networks. Make sure you can ping them.
- Change the area type of Area 1 so you don't see the 4 networks anymore but only 1 default route.
- Make sure you can still ping the 4 networks.

## GNS3 2.2.56.1

Import `ospf-totally-stub-startup-configs IOU.gns3project` with **File > Import portable project**.
The archive includes the startup configs and the original topology illustration.
For direct opening, keep `ospf-totally-stub-startup-configs.gns3` beside `project-files`.

Exercise routers use `x86_64_crb_linux-adventerprisek9-ms.bin`
(MD5 `4a2fce8de21d1831fbceffd155e41ae7`), 768 MB RAM, 128 KB NVRAM,
four Ethernet adapters and four serial adapters. Console ports are allocated automatically.

Startup and solution configs use the mapped IOU interfaces. Ethernet interfaces
retain the original bandwidth values in Kbit/s so OSPF metrics preserve the exercise.
Original reference images and legacy `.net` files may show the old interface names;
the converted `.gns3` project is the runnable topology.

| Router | Original interface | IOU interface |
| --- | --- | --- |
| Algrim | FastEthernet0/0 | Ethernet0/0 |
| Barik | FastEthernet0/0 | Ethernet0/0 |

Containerlab files are independent and unchanged. Structure, config packaging and
interface mappings were validated; boot and protocol behavior require the target
GNS3 server and the specified images.

## Topology:

## Video Solution:

[Video Solution on YouTube](http://www.youtube.com/watch?v=KgRmxG5qXK4)

## Configuration verification

Original interface addressing and administrative state retained.

Both supplied final configs lack OSPF and the additional loopbacks; they are incomplete source solutions.

These findings come from configuration analysis against the original files.
Boot, command support, adjacencies, routing tables and packet forwarding were not
tested live. See [the full verification report](../VERIFICATION.md) in the repository
(or `VERIFICATION.md` included in the portable archive).
