# EIGRP Hybrid Bandwidth Pacing

## Scenario

A large international ISP has hired you as one of their network engineers. The ISP still has a fairly large customer that is using an older frame-relay network. All of your colleagues are too busy working with MPLS and you are the only one who is capable of fixing frame-relay problems. The ISP wants you to look at the frame-relay network because there have been some congestion problems with EIGRP. It's up to you to configure the most optimal settings!

## Goal

* The frame-relay switch has been preconfigured for you.
* Router Tilburg is the Hub router and all other routers are the spoke routers.
* Router NewDelhi, Berlin and Paris each have a PVC with a CIR of 256kbps.
* Router NewYork has a PVC with a CIR of 128kbps.
* Every router has a loopback0 interface:
  * Tilburg: 1.1.1.1 /24
  * NewDelhi: 2.2.2.2 /24
  * Berlin: 3.3.3.3 /24
  * Paris: 4.4.4.4 /24
  * NewYork: 5.5.5.5 /24
* Configure frame-relay and EIGRP AS 1 on all routers with the most optimal settings for this network.

## GNS3 2.2.56.1

Import `EIGRP Hybrid Bandwidth Pacing IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `EIGRP Hybrid Bandwidth Pacing.gns3` beside `project-files`.

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

## Topology

![Network Topology](./topology-eigrp-hybrid-bandwidth-pacing.png)
