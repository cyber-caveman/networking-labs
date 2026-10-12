# EIGRP Unicast

![Network Topology](./topology-eigrp-unicast.jpg)

## Scenario

You are working as a trainee for an old service provider. Currently the network has a frame relay network which is still very popular among the customers. The service provider wants to replace the static routes from the past and use Cisco EIGRP (Enhanced Interior Gateway Routing Protocol). Up to you to implement this without changing any of the frame-relay configurations.

## Goal

- The frame-relay switch has been preconfigured for you, there is only a single PVC: Router Zebra to Hippo
  - Zebra: DLCI 102
  - Hippo: DLCI 201
- Do not change any of the frame-relay configurations.
- IP Addresses have been preconfigured for you.
  - **Router Zebra:**
    - S0/0: 192.168.12.1 /24
    - L0: 1.1.1.1 /24
  - **Router Hippo:**
    - S0/0: 192.168.12.2 /24
    - L0: 2.2.2.2 /24
- Configure EIGRP and advertise the serial and loopback interfaces.
- Ensure you establish a neighbor adjacency and are able to ping each others loopback interface.

## GNS3 2.2.56.1

Import `eigrp-unicast-startup-configs IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `eigrp-unicast-startup-configs.gns3` beside `project-files`.

Routers use the preferred IOU L3 image `x86_64_crb_linux-adventerprisek9-ms.bin`
(MD5 `4a2fce8de21d1831fbceffd155e41ae7`), template
`b3b10b90-adfb-43f8-b289-b68bcf322ad8`, 768 MB RAM, 512 KB NVRAM,
four Ethernet and four serial adapters, with automatically allocated consoles.
Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Physical interface names and link endpoints are updated together in startup and
all supplied final configs. Original bandwidth and delay are explicit where
needed to preserve EIGRP/IGP metric inputs. Source protocol settings and intended
startup state are preserved; final configs are not loaded at startup.

| Router | Original interface | IOU interface |
| --- | --- | --- |
| Zebra | Serial0/0 | Serial4/0 |
| Zebra | Serial0/1 | Serial4/1 |
| Zebra | Serial0/2 | Serial4/2 |
| Zebra | Serial0/3 | Serial4/3 |
| Hippo | Serial0/0 | Serial4/0 |
| Hippo | Serial0/1 | Serial4/1 |
| Hippo | Serial0/2 | Serial4/2 |
| Hippo | Serial0/3 | Serial4/3 |
| FRSW | Serial0/0 | Serial4/0 |
| FRSW | Serial0/1 | Serial4/1 |
| FRSW | Serial0/2 | Serial4/2 |
| FRSW | Serial0/3 | Serial4/3 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

## Video Solution

[EIGRP Unicast Video Solution on YouTube](http://www.youtube.com/watch?v=Pu3uNBZDhfA)
