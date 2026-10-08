# OSPF Totally NSSA

![Network Topology](./topology-ospf-totally-nssa.jpg)

## Scenario

You are working for a well-known wrestling federation and after countless battles you decided to switch your career and become a network engineer. The federation is using network equipment that is still from the 80's, therefore you need to make sure the routing tables will be as small as possible to guarantee good performance...get ready to rumble!

## Goal

- All IP addresses have been preconfigured for you.
- Configure OSPF on all routers, use the Area's as specified in the topology picture.
- Achieve full connectivity.
- Router Hogan: create additional loopbacks:
  - L1: 172.16.0.1 /24
  - L2: 172.16.1.1 /24
  - L3: 172.16.2.1 /24
  - L4: 172.16.3.1 /24
- Redistribute these networks into OSPF Area 0. Do not use the "network" command to achieve this.
- Take a look at the routing table of Router Undertaker, you should see all 4 networks. Make sure you can ping them.
- Change the area type of Area 1 so you don't see the 4 networks anymore but only 1 default route.
- Make sure you can still ping the 4 networks.
- Router Hogan: create additional loopbacks:
  - L4: 172.16.4.1 /24
  - L5: 172.16.5.1 /24
  - L6: 172.16.6.1 /24
  - L7: 172.16.7.1 /24
- Advertise these 4 networks into OSPF Area 0 by using the network command.
- Take a look at Router Undertaker, you should see all 4 networks.
- Change the area type of Area 1 so you don't see these 4 networks anymore but only a default route.
- Router Undertaker: create a loopback interface:
  - L0: 2.2.2.2 /24
- Configure RIP version 2 and advertise the 2.2.2.0 network into RIP.
- Router Undertaker: Redistribute RIP into OSPF, you are not allowed to turn Area 1 back into a standard Area.
- Make sure you still meet all the previous requirements.
- Make sure you can ping the 2.2.2.0 network from Router Hogan.
- Router Undertaker should only have a default route pointing to the Loopbacks of Router Hogan.

## Additional Content

## GNS3 2.2.56.1

Import `ospf-totally-nssa-startup-configs IOU.gns3project` with **File > Import portable project**.
The archive includes the startup configs and the original topology illustration.
For direct opening, keep `ospf-totally-nssa-startup-configs.gns3` beside `project-files`.

Exercise routers use `x86_64_crb_linux-adventerprisek9-ms.bin`
(MD5 `4a2fce8de21d1831fbceffd155e41ae7`), 768 MB RAM, 128 KB NVRAM,
four Ethernet adapters and four serial adapters. Console ports are allocated automatically.

Startup and solution configs use the mapped IOU interfaces. Ethernet interfaces
retain the original bandwidth values in Kbit/s so OSPF metrics preserve the exercise.
Original reference images and legacy `.net` files may show the old interface names;
the converted `.gns3` project is the runnable topology.

| Router | Original interface | IOU interface |
| --- | --- | --- |
| Hogan | FastEthernet0/0 | Ethernet0/0 |
| Piper | FastEthernet0/0 | Ethernet0/0 |
| Piper | FastEthernet1/0 | Ethernet0/1 |
| Undertaker | FastEthernet0/0 | Ethernet0/0 |

Containerlab files are independent and unchanged. Structure, config packaging and
interface mappings were validated; boot and protocol behavior require the target
GNS3 server and the specified images.

## Topology

## Video Solution

[OSPF Totally NSSA - Video Solution](http://www.youtube.com/watch?v=KHY-Mk6cpL0)

## Configuration verification

Backbone prefixes, connected redistribution, Area 1 nssa no-summary, RIP v2 and RIP-to-OSPF redistribution retained.

Type 7 translation, default-route behavior and reachability need live testing.

These findings come from configuration analysis against the original files.
Boot, command support, adjacencies, routing tables and packet forwarding were not
tested live. See [the full verification report](../VERIFICATION.md) in the repository
(or `VERIFICATION.md` included in the portable archive).
