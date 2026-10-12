# EIGRP Point-to-Point Bandwidth Pacing

![Network Topology](./topology-eigrp-point-to-point-bandwidth-pacing.png)

## Scenario:

A large international ISP has hired you as one of their network engineers. The ISP still has a fairly large customer that is using an older frame-relay network. All of your colleagues are too busy working with MPLS and you are the only one who is capable of fixing frame-relay problems. Whenever router Tilburg is sending major EIGRP updates there are problems with congestion. Think you can tune EIGRP so this network won't have congestion anymore?

## Goal:

- All IP addresses have been preconfigured for you as specified in the topology picture.
- Every router has a loopback0 interface:
  - Tilburg: 1.1.1.1 /24
  - NewDelhi: 2.2.2.2 /24
  - Berlin: 3.3.3.3 /24
  - Paris: 4.4.4.4 /24
  - NewYork: 5.5.5.5 /24
- You are not allowed to make any changes to the frame-relay configurations.
- In this topology you can see 4 spoke routers but in reality there are 10 spoke routers. I didn't add them all to save CPU power when you run this topology. Each PVC has a CIR of 64kbps.
- Router Tilburg has a serial interface 0/0 that only has a physical bandwidth of 256kbps.
- Configure EIGRP AS 1 on all routers and make sure you have full connectivity.
- Whenever router Tilburg sends EIGRP updates to all spoke routers there is congestion because the physical bandwidth of serial interface s0/0 is only 256kbps.
- Configure your network so the bandwidth reflects the CIR on the PVCs and EIGRP will only use 50% of the CIR.

## GNS3 2.2.56.1

Import `EIGRP P2P Bandwidth Pacing IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `EIGRP P2P Bandwidth Pacing.gns3` beside `project-files`.

Routers use the preferred IOU L3 image `x86_64_crb_linux-adventerprisek9-ms.bin`
(MD5 `4a2fce8de21d1831fbceffd155e41ae7`), template
`b3b10b90-adfb-43f8-b289-b68bcf322ad8`, 768 MB RAM, 512 KB NVRAM,
four Ethernet and four serial adapters, with automatically allocated consoles.
Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Physical interface names and link endpoints are updated together in startup and
all supplied final configs. Original bandwidth and delay are explicit where
needed to preserve EIGRP/IGP metric inputs. Source protocol settings and intended
startup state are preserved; final configs are not loaded at startup.

Built-in Frame Relay switches and PVC mappings retain their original type and
settings. Connected IOU interfaces explicitly select ANSI LMI, supported by the
built-in switch. This is a transport compatibility adjustment in startup and
available final configs, not a change to the routing exercise.

| Router | Original interface | IOU interface |
| --- | --- | --- |
| Berlin | Serial0/0 | Serial4/0 |
| Berlin | Serial0/1 | Serial4/1 |
| Berlin | Serial0/2 | Serial4/2 |
| Berlin | Serial0/3 | Serial4/3 |
| NewDelhi | Serial0/0 | Serial4/0 |
| NewDelhi | Serial0/1 | Serial4/1 |
| NewDelhi | Serial0/2 | Serial4/2 |
| NewDelhi | Serial0/3 | Serial4/3 |
| NewYork | Serial0/0 | Serial4/0 |
| NewYork | Serial0/1 | Serial4/1 |
| NewYork | Serial0/2 | Serial4/2 |
| NewYork | Serial0/3 | Serial4/3 |
| Paris | Serial0/0 | Serial4/0 |
| Paris | Serial0/1 | Serial4/1 |
| Paris | Serial0/2 | Serial4/2 |
| Paris | Serial0/3 | Serial4/3 |
| Tilburg | Serial0/0 | Serial4/0 |
| Tilburg | Serial0/1 | Serial4/1 |
| Tilburg | Serial0/2 | Serial4/2 |
| Tilburg | Serial0/3 | Serial4/3 |

### Source notes

No completed solution configs were supplied; none were invented.

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology:
