# OSPF Summarization Discard Route

## Scenario

Ever since you encountered a router your quest has been to become a successful network engineer. Your career is prosperous and there isn't a bit that you haven't slain before. This time however you are running into trouble with one of your OSPF routers. It seems one of your routers is installing a null0 route whenever you do summarization and this is something you don't want to happen...

## Goal

- All IP addresses have been preconfigured for you.
- Configure OSPF and use the correct areas.
- Configure a loopback0 interface on router Spielburg with network address 3.3.3.3 /24.
- Configure router Shapeir to summarize network 3.3.3.0 /24 to 3.0.0.0 /8.
- Configure router Shapeir so it doesn't add a null0 entry in its routing table.

## GNS3 2.2.56.1

Import `OSPF Summarization Discard Route IOU.gns3project` with **File > Import portable project**.
The archive includes the startup configs and the original topology illustration.
For direct opening, keep `OSPF Summarization Discard Route.gns3` beside `project-files`.

Exercise routers use `x86_64_crb_linux-adventerprisek9-ms.bin`
(MD5 `4a2fce8de21d1831fbceffd155e41ae7`), 768 MB RAM, 128 KB NVRAM,
four Ethernet adapters and four serial adapters. Console ports are allocated automatically.

Startup and solution configs use the mapped IOU interfaces. Ethernet interfaces
retain the original bandwidth values in Kbit/s so OSPF metrics preserve the exercise.
Original reference images and legacy `.net` files may show the old interface names;
the converted `.gns3` project is the runnable topology.

| Router | Original interface | IOU interface |
| --- | --- | --- |
| Shapeir | FastEthernet0/0 | Ethernet0/0 |
| Shapeir | FastEthernet1/0 | Ethernet0/1 |
| Spielburg | FastEthernet0/0 | Ethernet0/0 |
| Tarna | FastEthernet0/0 | Ethernet0/0 |

Containerlab files are independent and unchanged. Structure, config packaging and
interface mappings were validated; boot and protocol behavior require the target
GNS3 server and the specified images.

## Topology

![Network Topology](./topology-ospf-summarization-discard-route.png)

## Video Solution

[Video: OSPF Summarization Discard Route Solution](http://www.youtube.com/watch?v=kBMf5oF_tzM)

## Configuration verification

Area assignments, 3.3.3.0/24 and ABR range 3.0.0.0/8 retained.

Source Shapeir final config lacks no discard-route internal; the requested suppression of the Null0 summary route is not implemented in that source solution.

These findings come from configuration analysis against the original files.
Boot, command support, adjacencies, routing tables and packet forwarding were not
tested live. See [the full verification report](../VERIFICATION.md) in the repository
(or `VERIFICATION.md` included in the portable archive).
