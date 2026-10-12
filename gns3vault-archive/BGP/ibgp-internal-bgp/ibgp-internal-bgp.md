# IBGP - Internal BGP

## Scenario

Big Blooms is a fairly large retail company selling all kinds of flowers. Big Blooms has multiple sites and will use BGP in the future to connect all the different sites. Their headquarters network will be used to connect all the different networks and will be used as a transit for all the different sites. In order to prepare for the BGP configuration you have to configure IBGP (Internal BGP) for them.

## Goal

* All IP addresses have been preconfigured for you as specified in the topology picture.
* Each router has a loopback0 and loopback1 interface.
* Configure IBGP AS 1234 on all routers. You are not allowed to use IP addresses on the physical interfaces for the neighbor adjacency.
* Advertise the loopback1 interfaces in IBGP and ensure you have full connectivity within AS 1234.

## GNS3 2.2.56.1

Import `IBGP - Internal BGP IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `IBGP - Internal BGP.gns3` beside `project-files`.

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
| Blossom | FastEthernet0/0 | Ethernet0/0 |
| Blossom | FastEthernet1/0 | Ethernet0/1 |
| Lily | FastEthernet0/0 | Ethernet0/0 |
| Lily | FastEthernet1/0 | Ethernet0/1 |
| Rose | FastEthernet0/0 | Ethernet0/0 |
| Rose | FastEthernet1/0 | Ethernet0/1 |
| Tulip | FastEthernet0/0 | Ethernet0/0 |
| Tulip | FastEthernet1/0 | Ethernet0/1 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-ibgp-internal-bgp.png)

## Video Solution

[Video: IBGP Configuration](http://www.youtube.com/watch?v=q7Lzjqt6GLY)
