# OSPF DR BDR Election

![Network Topology](./topology-ospf-dr-bdr-election.png)

## Scenario:

You end up working as one of the network engineers for a nuclear powerplant located in a cartoony looking town. OSPF is being used as the IGP routing protocol but there have been some problems with the network. It is uncertain which router is being chosen as the designated or backup designated router. Up to you to fix these issues!

## Goal:

- All IP addresses have been preconfigured for you as specified in the topology picture.
- Configure OSPF on all routers, achieve full connectivity.
- Ensure router Marge is the DR for network 192.168.1.0 /24.
- Ensure router Bart is the BDR for network 192.168.1.0 /24.
- Ensure router Home is the DR for network 192.168.2.0 /24. You are not allowed to change the priority.
- Ensure router Maggie is the BDR for network 192.168.2.0 /24. You are not allowed to change the priority.

## GNS3 2.2.56.1

Import `OSPF DR BDR Election IOU.gns3project` with **File > Import portable project**.
The archive includes the startup configs and the original topology illustration.
For direct opening, keep `OSPF DR BDR Election.gns3` beside `project-files`.

Exercise routers use `x86_64_crb_linux-adventerprisek9-ms.bin`
(MD5 `4a2fce8de21d1831fbceffd155e41ae7`), 768 MB RAM, 128 KB NVRAM,
four Ethernet adapters and four serial adapters. Console ports are allocated automatically.
The unmanaged Ethernet switches retain their original device type.

Startup and solution configs use the mapped IOU interfaces. Ethernet interfaces
retain the original bandwidth values in Kbit/s so OSPF metrics preserve the exercise.
Original reference images and legacy `.net` files may show the old interface names;
the converted `.gns3` project is the runnable topology.

| Router | Original interface | IOU interface |
| --- | --- | --- |
| Bart | FastEthernet0/0 | Ethernet0/0 |
| Homer | FastEthernet0/0 | Ethernet0/0 |
| Homer | FastEthernet1/0 | Ethernet0/1 |
| Lisa | FastEthernet0/0 | Ethernet0/0 |
| Maggie | FastEthernet0/0 | Ethernet0/0 |
| Marge | FastEthernet0/0 | Ethernet0/0 |

Containerlab files are independent and unchanged. Structure, config packaging and
interface mappings were validated; boot and protocol behavior require the target
GNS3 server and the specified images.

## Topology:

## Video Solution:

[OSPF DR BDR Election Video](http://www.youtube.com/watch?v=E1sNeikHniQ)

## Configuration verification

Both broadcast segments, Marge priority 100, Bart priority 90 and other priorities retained.

Homer/Maggie DR/BDR selection depends on startup/election order; the source configs alone do not enforce it.

These findings come from configuration analysis against the original files.
Boot, command support, adjacencies, routing tables and packet forwarding were not
tested live. See [the full verification report](../VERIFICATION.md) in the repository
(or `VERIFICATION.md` included in the portable archive).
