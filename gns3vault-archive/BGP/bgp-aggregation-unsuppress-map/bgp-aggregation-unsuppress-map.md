# BGP Aggregation Unsuppress Map

## Scenario

John and Jim are setting up their own ISP and start by configuring BGP between their routers. Because they want to make sure not to advertise too many prefixes they want to configure BGP aggregation. It's up to you to make it happen.

## Goal

* All IP addresses have been preconfigured for you.
* Configure EBGP between router John and Jim. Pick whatever AS you like.
* Advertise all loopback interfaces on router Jim in BGP.
* Create a summary for the loopback interfaces on router Jim. Ensure you don't have any overlapping address space.
* Ensure you only see the summary on router John with the exception of network 172.16.2.0 /24.

## GNS3 2.2.56.1

Import `BGP Aggregation IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `BGP Aggregation.gns3` beside `project-files`.

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
| Jim | FastEthernet0/0 | Ethernet0/0 |
| John | FastEthernet0/0 | Ethernet0/0 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-bgp-aggregation-unsuppress-map.png)

## Video Solution

[BGP Aggregation Unsuppress Map Video](http://www.youtube.com/watch?v=v4eHtre_hd4)
