# OSPF Over Frame-Relay: Point-to-Point

![Network Topology](./topology-ospf-over-frame-relay-point-to-point.jpg)

## Scenario

As the senior network engineer for a Dutch fishing company you are responsible for connecting all the different branch offices to the main network. The WAN technology you are using is Frame Relay, and you need to run OSPF over this WAN connection. It's impossible to broadcast on this WAN connection.

## Goal

- The frame-relay switch has been preconfigured for you, as you can see in the topology picture the following PVC's has been configured:
  - Router Barracuda to Salmon:
    - Barracuda: DLCI 102
    - Salmon: DLCI 201
  - Router Barracuda to Herring:
    - Barracuda: DLCI 103
    - Herring: DLCI 301

- Router Barracuda is the "Hub" router and the other 2 routers are the "Spoke" routers.

- Do not change any configuration on the Frame-Relay switch.

- You will need to create sub-interfaces on Router Barracuda.

- Configure the following IP addresses:
  - Router Barracuda:
    - S4/0.102: 192.168.12.1 /24
    - S4/0.103: 192.168.13.1 /24
    - L0: 1.1.1.1 /24
  - Router Salmon:
    - S4/0.201: 192.168.12.2 /24
    - L0: 2.2.2.2 /24
  - Router Herring:
    - S4/0.301: 192.168.13.3 /24
    - L0: 3.3.3.3 /24

- Configure all serial interfaces for encapsulation Frame-Relay.

- Disable Frame-relay inverse arp on all serial interfaces.

- Use 'clear frame-relay inarp' to make sure the ARP table is cleared.

- Configure the correct DLCI numbers on all routers and make sure you can ping every IP address from router Barracuda.

- Configure the OSPF network type to "point-to-point" on all serial interfaces.

- Configure OSPF on all 3 routers, make sure you have full connectivity. All IP addresses including the loopbacks should be reachable.

## GNS3 2.2.56.1

Import `OSPF over FrameRelay PointtoPoint IOU.gns3project` with **File > Import portable project**.
The archive includes the startup configs and the original topology illustration.
For direct opening, keep `OSPF over FrameRelay PointtoPoint.gns3` beside `project-files`.

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
| HERRING | Serial0/0 | Serial4/0 |
| HERRING | Serial0/1 | Serial4/1 |
| HERRING | Serial0/2 | Serial4/2 |
| HERRING | Serial0/3 | Serial4/3 |
| BARRACUDA | Serial0/0 | Serial4/0 |
| BARRACUDA | Serial0/1 | Serial4/1 |
| BARRACUDA | Serial0/2 | Serial4/2 |
| BARRACUDA | Serial0/3 | Serial4/3 |
| SALMON | Serial0/0 | Serial4/0 |
| SALMON | Serial0/1 | Serial4/1 |
| SALMON | Serial0/2 | Serial4/2 |
| SALMON | Serial0/3 | Serial4/3 |

Containerlab files are independent and unchanged. Structure, config packaging and
interface mappings were validated; boot and protocol behavior require the target
GNS3 server and the specified images.

## Topology

## Video Solution

http://www.youtube.com/watch?v=85FvtIVuGBQ

## Configuration verification

Point-to-point subinterfaces, 102↔201 and 103↔301 DLCIs, separate /24 subnets, loopbacks and area 0 retained.

DLCI/LMI status and point-to-point adjacency formation not tested live.

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
