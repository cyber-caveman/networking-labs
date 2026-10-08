# OSPF Flood Reduction

![Network Topology](./topology-ospf-flood-reduction.png)

## Scenario:

You live on a tropical island and work as a network engineer and scientist. After years of study you have discovered a formula so you do not age anymore. Unfortunately your network is running OSPF and LSAs still age...you are wondering if you can do something to OSPF as well.

## Goal:

* All IP addresses have been preconfigured for you.
* Configure OSPF on all routers. Achieve both connectivity.
* Configure OSPF so there is no longer a periodic refresh of LSAs.

## GNS3 2.2.56.1

Import `OSPF Flood-Reduction IOU.gns3project` with **File > Import portable project**.
The archive includes the startup configs and the original topology illustration.
For direct opening, keep `OSPF Flood-Reduction.gns3` beside `project-files`.

Exercise routers use `x86_64_crb_linux-adventerprisek9-ms.bin`
(MD5 `4a2fce8de21d1831fbceffd155e41ae7`), 768 MB RAM, 128 KB NVRAM,
four Ethernet adapters and four serial adapters. Console ports are allocated automatically.

Startup and solution configs use the mapped IOU interfaces. Ethernet interfaces
retain the original bandwidth values in Kbit/s so OSPF metrics preserve the exercise.
Original reference images and legacy `.net` files may show the old interface names;
the converted `.gns3` project is the runnable topology.

| Router | Original interface | IOU interface |
| --- | --- | --- |
| Beach | FastEthernet0/0 | Ethernet0/0 |
| Coconut | FastEthernet0/0 | Ethernet0/0 |
| Coconut | FastEthernet1/0 | Ethernet0/1 |
| Palm | FastEthernet0/0 | Ethernet0/0 |

Containerlab files are independent and unchanged. Structure, config packaging and
interface mappings were validated; boot and protocol behavior require the target
GNS3 server and the specified images.

## Topology:

## Video Solution:

http://www.youtube.com/watch?v=11kwf88nco4

## Configuration verification

Both routed links, area 0 and flood-reduction on each participating interface retained.

LSA refresh suppression requires live observation.

These findings come from configuration analysis against the original files.
Boot, command support, adjacencies, routing tables and packet forwarding were not
tested live. See [the full verification report](../VERIFICATION.md) in the repository
(or `VERIFICATION.md` included in the portable archive).
