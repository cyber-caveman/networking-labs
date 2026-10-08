
---
title: "OSPF per Neighbor Cost"
slug: "ospf-per-neighbor-cost"
category: "OSPF"
wordpress_id: 848
---

## Scenario

The local fish trading market needs your help with their OSPF network. It seems their routers are unable to change the bandwidth or cost on the interfaces so you need to use another solution to influence OSPF routing...sounds fishy!

## Goal

* All IP addresses have been preconfigured for you.
* Configure OSPF on all routers. Achieve full connectivity.
* Configure a loopback0 interface with IP address 1.1.1.1 /32 on router Salmon and Herring.
* Advertise the loopback0 interface on router Salmon and Herring.
* Configure your network so router Barracuda sends all traffic for 1.1.1.1 /32 to router Herring. You are not allowed to change the bandwidth or cost on the interface.

## Motivation

## GNS3 2.2.56.1

Import `OSPFperNeighborCost IOU.gns3project` with **File > Import portable project**.
The archive includes the startup configs and the original topology illustration.
For direct opening, keep `OSPFperNeighborCost.gns3` beside `project-files`.

Exercise routers use `x86_64_crb_linux-adventerprisek9-ms.bin`
(MD5 `4a2fce8de21d1831fbceffd155e41ae7`), 768 MB RAM, 128 KB NVRAM,
four Ethernet adapters and four serial adapters. Console ports are allocated automatically.

The preconfigured Frame Relay switch `FRSW` retains its original
C3640 Dynamips device, image `c3640-a3js-mz.124-25d.image` and PVC switching configuration.
That original IOS image must also be available on the GNS3 server.

Startup and solution configs use the mapped IOU interfaces. Ethernet interfaces
retain the original bandwidth values in Kbit/s so OSPF metrics preserve the exercise.
Original reference images and legacy `.net` files may show the old interface names;
the converted `.gns3` project is the runnable topology.

| Router | Original interface | IOU interface |
| --- | --- | --- |
| BARRACUDA | Serial0/0 | Serial4/0 |
| BARRACUDA | Serial0/1 | Serial4/1 |
| BARRACUDA | Serial0/2 | Serial4/2 |
| BARRACUDA | Serial0/3 | Serial4/3 |
| HERRING | Serial0/0 | Serial4/0 |
| HERRING | Serial0/1 | Serial4/1 |
| HERRING | Serial0/2 | Serial4/2 |
| HERRING | Serial0/3 | Serial4/3 |
| SALMON | Serial0/0 | Serial4/0 |
| SALMON | Serial0/1 | Serial4/1 |
| SALMON | Serial0/2 | Serial4/2 |
| SALMON | Serial0/3 | Serial4/3 |

Containerlab files are independent and unchanged. Structure, config packaging and
interface mappings were validated; boot and protocol behavior require the target
GNS3 server and the specified images.

## Topology

![Network Topology](./topology-ospf-per-neighbor-cost.png)

## Video Solution

[OSPF per Neighbor Cost Video Solution](http://www.youtube.com/watch?v=M33oKPT6oh8)

## Configuration verification

Common /24, point-to-multipoint OSPF, equal 1.1.1.1/32 spoke loopbacks and Herring neighbor cost 10 retained. The unchanged 1544 Kbit/s serial default implies cost 64 before that override.

Inverse ARP and dynamically learned Frame Relay mappings, as used by the source, need live verification.

These findings come from configuration analysis against the original files.
Boot, command support, adjacencies, routing tables and packet forwarding were not
tested live. See [the full verification report](../VERIFICATION.md) in the repository
(or `VERIFICATION.md` included in the portable archive).

## C3640 appliance compatibility

The Frame Relay switching router uses the user-provided working C3640 appliance:
`c3640-a3js-mz.124-25d.image`, MD5 `493c4ef6578801d74d715e7d11596964`,
template `b7a0bd2a-0e7d-4ea8-8c93-3b580f78971e`, 192 MB RAM,
256 KB NVRAM, clock divisor 4 and idle-PC `0x6050b114`.
Other runtime settings match that appliance example.

Slot 0 retains `NM-4T` because the Frame Relay topology requires Serial0/0–0/2;
the example's empty slots would provide no serial ports. The existing node UUID,
project-local Dynamips ID and matching startup-config filename are retained.
Console allocation and MAC-address generation are left to GNS3 rather than copying
the example's console port or MAC address. Startup/final configs and PVCs are unchanged.

Re-import this updated `.gns3project` archive to apply the appliance settings.
Existing imported copies are not updated by edits to this repository.
Local schema, runtime port construction, link lookup, archive and configuration
consistency checks passed. Opening and booting on the remote server remain untested;
the precise cause of the previously reported empty canvas has not been confirmed.
