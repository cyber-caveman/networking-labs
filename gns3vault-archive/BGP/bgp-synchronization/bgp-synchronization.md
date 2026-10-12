# BGP Synchronization

## Scenario

You are a freelance network consultant specialized in solving BGP problems. One of your customers, a small ISP has trouble with customers that are unable to reach each other. They use BGP synchronization on some of their routers.

## Goal

* All IP addresses have been preconfigured as specified in the topology picture.
* Each router has a loopback0 interface.
* Configure OSPF within AS 2 to advertise the loopback0 interfaces. Don't advertise or run OSPF on the links interconnecting AS 1 and AS 3.
* Configure IBGP between router Foxx and Green. Source the BGP updates from the loopback0 interfaces.
* Enable BGP synchronization.
* Configure EBGP between router Foxx and Baldwin.
* Configure EBGP between router Green and Rollins.
* Advertise the loopback0 interfaces on router Baldwin and Rollins.
* Ensure AS 1 and AS 3 can communicate with each other without removing the BGP synchronization command.

## GNS3 2.2.56.1

Import `BGP Synchronization IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `BGP Synchronization.gns3` beside `project-files`.

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
| Baldwin | FastEthernet0/0 | Ethernet0/0 |
| Foxx | FastEthernet0/0 | Ethernet0/0 |
| Foxx | FastEthernet1/0 | Ethernet0/1 |
| Green | FastEthernet0/0 | Ethernet0/0 |
| Green | FastEthernet1/0 | Ethernet0/1 |
| Mitchell | FastEthernet0/0 | Ethernet0/0 |
| Mitchell | FastEthernet1/0 | Ethernet0/1 |
| Rollins | FastEthernet0/0 | Ethernet0/0 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-bgp-synchronization.png)

## Video Solution

[Video: BGP Synchronization Lab Solution](http://www.youtube.com/watch?v=NVKfIZEncwk)
