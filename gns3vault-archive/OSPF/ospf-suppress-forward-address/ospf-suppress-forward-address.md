# OSPF Suppress Forward Address

![Network Topology](./topology-ospf-suppress-forward-address.png)

## Scenario:

You are the senior network engineer for a company that runs the show "Two and a half Router". To increase OSPF performance your colleague has implemented a NSSA area and some prefix filters. Strangely enough you now have problems with reachability. Let's see what you can do about it.

## Goal:

- All IP addresses have been preconfigured for you.
- Configure OSPF and use the correct areas. Ensure Area 1 is a NSSA.
- Configure RIP between router Charlie and Evelyn.
- Create a loopback0 interface on router Evelyn with IP address 1.1.1.1 /24 and advertise it in RIP.
- Redistribute between RIP and OSPF.
- Configure a prefix-list on router Jake which filters network 192.168.13.0 /24.
- Ensure you can still reach network 1.1.1.0 /24 from all routers without removing the prefix-list. You are only allowed to use OSPF commands.

## GNS3 2.2.56.1

Import `OSPF Suppress Forward Address IOU.gns3project` with **File > Import portable project**.
The archive includes the startup configs and the original topology illustration.
For direct opening, keep `OSPF Suppress Forward Address.gns3` beside `project-files`.

Exercise routers use `x86_64_crb_linux-adventerprisek9-ms.bin`
(MD5 `4a2fce8de21d1831fbceffd155e41ae7`), 768 MB RAM, 128 KB NVRAM,
four Ethernet adapters and four serial adapters. Console ports are allocated automatically.

Startup and solution configs use the mapped IOU interfaces. Ethernet interfaces
retain the original bandwidth values in Kbit/s so OSPF metrics preserve the exercise.
Original reference images and legacy `.net` files may show the old interface names;
the converted `.gns3` project is the runnable topology.

| Router | Original interface | IOU interface |
| --- | --- | --- |
| Alan | FastEthernet0/0 | Ethernet0/0 |
| Alan | FastEthernet1/0 | Ethernet0/1 |
| Berta | FastEthernet0/0 | Ethernet0/0 |
| Berta | FastEthernet1/0 | Ethernet0/1 |
| Charlie | FastEthernet0/0 | Ethernet0/0 |
| Charlie | Serial1/0 | Serial4/0 |
| Charlie | Serial1/1 | Serial4/1 |
| Charlie | Serial1/2 | Serial4/2 |
| Charlie | Serial1/3 | Serial4/3 |
| Evelyn | Serial0/0 | Serial4/0 |
| Evelyn | Serial0/1 | Serial4/1 |
| Evelyn | Serial0/2 | Serial4/2 |
| Evelyn | Serial0/3 | Serial4/3 |
| Jake | FastEthernet0/0 | Ethernet0/0 |
| Jake | FastEthernet1/0 | Ethernet0/1 |

Containerlab files are independent and unchanged. Structure, config packaging and
interface mappings were validated; boot and protocol behavior require the target
GNS3 server and the specified images.

## Topology:

## Configuration verification

All five startup routers, Ethernet/serial links and original addressing retained.

No final-configs supplied; NSSA, RIP redistribution, prefix filtering and suppress-fa have no original completed solution to verify.

These findings come from configuration analysis against the original files.
Boot, command support, adjacencies, routing tables and packet forwarding were not
tested live. See [the full verification report](../VERIFICATION.md) in the repository
(or `VERIFICATION.md` included in the portable archive).
