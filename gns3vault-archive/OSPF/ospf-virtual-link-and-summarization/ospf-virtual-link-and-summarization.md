# OSPF Virtual Link and Summarization

![Network Topology](./topology-ospf-virtual-link-and-summarization.jpg)

## Scenario

The Company you are currently working for has recently bought a smaller organization and now needs to connect the 2 networks together. Company policy specifies that only OSPF can be used as a routing protocol and it's physically impossible to connect the Louie router to the Huey router. Up to you to find a good solution...!

## Goal

- All IP addresses have been preconfigured for you.
- Configure OSPF on all routers, configure the areas as specified in the topology picture.
- Area 2 has no direct connection to Area 0, solve this by using OSPF commands.
- Ensure you have full reachability.
- Create some extra loopbacks on router Louie and advertise them in area 2:
  - Loopback0: 172.16.0.1 /24
  - Loopback1: 172.16.1.1 /24
  - Loopback2: 172.16.2.1 /24
  - Loopback3: 172.16.3.1 /24
- Make sure router Huey only sees 172.16.0.0/22 in it's routing table, you are only allowed to make changes to router Dewey.

## Key Concepts

This lab covers:
- OSPF Virtual Links
- Route Summarization
- OSPF Area Design
- Multi-area OSPF Configuration

## GNS3 2.2.56.1

Import `ospf-vl-and-summarization-startup-configs IOU.gns3project` with **File > Import portable project**.
The archive includes the startup configs and the original topology illustration.
For direct opening, keep `ospf-vl-and-summarization-startup-configs.gns3` beside `project-files`.

Exercise routers use `x86_64_crb_linux-adventerprisek9-ms.bin`
(MD5 `4a2fce8de21d1831fbceffd155e41ae7`), 768 MB RAM, 128 KB NVRAM,
four Ethernet adapters and four serial adapters. Console ports are allocated automatically.

Startup and solution configs use the mapped IOU interfaces. Ethernet interfaces
retain the original bandwidth values in Kbit/s so OSPF metrics preserve the exercise.
Original reference images and legacy `.net` files may show the old interface names;
the converted `.gns3` project is the runnable topology.

| Router | Original interface | IOU interface |
| --- | --- | --- |
| Huey | FastEthernet0/0 | Ethernet0/0 |
| Dewey | FastEthernet0/0 | Ethernet0/0 |
| Dewey | FastEthernet1/0 | Ethernet0/1 |
| Dewey | FastEthernet2/0 | Ethernet0/2 |
| Louie | FastEthernet0/0 | Ethernet0/0 |
| Louie | FastEthernet1/0 | Ethernet0/1 |

Containerlab files are independent and unchanged. Structure, config packaging and
interface mappings were validated; boot and protocol behavior require the target
GNS3 server and the specified images.

## Topology

## Video Solution

- [YouTube: OSPF Virtual Link and Summarization](http://www.youtube.com/watch?v=36FyRk5fmkI)

## Configuration verification

Area 1 virtual-link peer identities, Area 2 attachment, four /24 loopbacks and the 172.16.0.0/22 range retained.

Dewey’s virtual-link router ID is selected automatically from its active interfaces, as in the source; virtual-link establishment and resulting LSAs require live testing.

These findings come from configuration analysis against the original files.
Boot, command support, adjacencies, routing tables and packet forwarding were not
tested live. See [the full verification report](../VERIFICATION.md) in the repository
(or `VERIFICATION.md` included in the portable archive).
