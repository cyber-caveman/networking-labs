# EIGRP over Frame-Relay with Sub-interfaces

## Scenario

A couple of stooge network engineers are trying to configure EIGRP over the frame-relay network. They read all about frame-relay, EIGRP and split-horizon and decided it sounded like a good idea to use sub-interface. Unfortunately things are not working as they should. Do you think you can help them out?

## Goal

- All IP addresses have been preconfigured for you as specified in the topology picture except for router Moe.
- Every router has a loopback0 interface:
  - Moe: 1.1.1.1 /24
  - Curly: 2.2.2.2 /24
  - Larry: 3.3.3.3 /24
- You are not allowed to make any changes to the frame-relay configurations.
- Configure a sub-interface on router Moe for each PVC.
- Configure EIGRP AS 123 on all routers and advertise the loopback interfaces.
- Ensure router Curly and Larry can see each other's loopback interfaces. Test this by sending a ping that is sourced from the loopback0 interfaces and destined for the other loopback0 interface.

## GNS3 2.2.56.1

Import `EIGRP over Frame-Relay IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `EIGRP over Frame-Relay.gns3` beside `project-files`.

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
| Curly | Serial0/0 | Serial4/0 |
| Curly | Serial0/1 | Serial4/1 |
| Curly | Serial0/2 | Serial4/2 |
| Curly | Serial0/3 | Serial4/3 |
| Larry | Serial0/0 | Serial4/0 |
| Larry | Serial0/1 | Serial4/1 |
| Larry | Serial0/2 | Serial4/2 |
| Larry | Serial0/3 | Serial4/3 |
| Moe | Serial0/0 | Serial4/0 |
| Moe | Serial0/1 | Serial4/1 |
| Moe | Serial0/2 | Serial4/2 |
| Moe | Serial0/3 | Serial4/3 |

### Source notes

No completed solution configs were supplied; none were invented.

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-eigrp-over-frame-relay-with-sub-interfaces.png)
