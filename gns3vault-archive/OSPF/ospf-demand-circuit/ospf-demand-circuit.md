# OSPF Demand Circuit

## Scenario

Living on a tropical island isn't all that bad. You run a small network used to order cocktails at the Coconut Bar so they are delivered at Palm beach. Unfortunately the links you are using are leased line and pretty expensive. You need to make sure you don't send any unnecessary OSPF traffic or you won't be able to afford any more sunscreen.

## Goal

- All IP addresses have been preconfigured for you.
- Configure OSPF on both routers. Achieve full connectivity.
- Ensure no periodic hello packets are sent on the serial interfaces without breaking the OSPF neighbor adjacency.

## GNS3 2.2.56.1

Import `OSPF Demand Circuit IOU.gns3project` with **File > Import portable project**.
The archive includes the startup configs and the original topology illustration.
For direct opening, keep `OSPF Demand Circuit.gns3` beside `project-files`.

Exercise routers use `x86_64_crb_linux-adventerprisek9-ms.bin`
(MD5 `4a2fce8de21d1831fbceffd155e41ae7`), 768 MB RAM, 128 KB NVRAM,
four Ethernet adapters and four serial adapters. Console ports are allocated automatically.

Startup and solution configs use the mapped IOU interfaces. Ethernet interfaces
retain the original bandwidth values in Kbit/s so OSPF metrics preserve the exercise.
Original reference images and legacy `.net` files may show the old interface names;
the converted `.gns3` project is the runnable topology.

| Router | Original interface | IOU interface |
| --- | --- | --- |
| Coconut | Serial0/0 | Serial4/0 |
| Coconut | Serial0/1 | Serial4/1 |
| Coconut | Serial0/2 | Serial4/2 |
| Coconut | Serial0/3 | Serial4/3 |
| Palm | Serial0/0 | Serial4/0 |
| Palm | Serial0/1 | Serial4/1 |
| Palm | Serial0/2 | Serial4/2 |
| Palm | Serial0/3 | Serial4/3 |

Containerlab files are independent and unchanged. Structure, config packaging and
interface mappings were validated; boot and protocol behavior require the target
GNS3 server and the specified images.

## Topology

![Network Topology](./topology-ospf-demand-circuit.png)

## Video Solution

http://www.youtube.com/watch?v=iqTVtgjI8Us

## Configuration verification

Matching serial /24, loopbacks, area 0 and demand-circuit on both endpoints retained.

Hello suppression and demand-circuit support on the chosen image need live testing.

These findings come from configuration analysis against the original files.
Boot, command support, adjacencies, routing tables and packet forwarding were not
tested live. See [the full verification report](../VERIFICATION.md) in the repository
(or `VERIFICATION.md` included in the portable archive).
