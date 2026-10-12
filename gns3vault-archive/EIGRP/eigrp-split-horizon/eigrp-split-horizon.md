# EIGRP Split Horizon

![Network Topology](./topology-eigrp-split-horizon.jpg)

## Scenario

Jack and Joe both have important information to share with each other but they don't have a direct connection between them. Tori agreed to help out and so they setup a Frame-Relay network to share information. EIGRP (Enhanced Interior Gateway Routing Protocol) is used as the routing protocol to dynamically learn new networks. Configuring EIGRP should be straight forward but Joe and Jack are complaining that they are unable to reach other's networks...time for you to fix it!

## Goal

- All IP addresses have been preconfigured for you.
- Every router has a loopback0 interface:
  - Tori: 1.1.1.1 /24
  - Joe: 2.2.2.2 /24
  - Jack: 3.3.3.3 /24
- You are not allowed to make any changes to the frame-relay configurations.
- Configure EIGRP AS 123 on all routers, advertise all networks.
- Ensure router Joe and Jack can see each other's loopback interfaces. Test this by sending a ping that is sourced from the loopback0 interfaces and destined for the other loopback0 interface.

## GNS3 2.2.56.1

Import `eigrp-split-horizon-startup-configs IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `eigrp-split-horizon-startup-configs.gns3` beside `project-files`.

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
| TORI | Serial0/0 | Serial4/0 |
| TORI | Serial0/1 | Serial4/1 |
| TORI | Serial0/2 | Serial4/2 |
| TORI | Serial0/3 | Serial4/3 |
| JOE | Serial0/0 | Serial4/0 |
| JOE | Serial0/1 | Serial4/1 |
| JOE | Serial0/2 | Serial4/2 |
| JOE | Serial0/3 | Serial4/3 |
| JACK | Serial0/0 | Serial4/0 |
| JACK | Serial0/1 | Serial4/1 |
| JACK | Serial0/2 | Serial4/2 |
| JACK | Serial0/3 | Serial4/3 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

## Video Solution

[EIGRP Split Horizon Video Solution](http://www.youtube.com/watch?v=gGet_AF-Vac)
