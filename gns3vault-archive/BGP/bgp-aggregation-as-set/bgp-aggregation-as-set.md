# BGP Aggregation AS SET

## Scenario

You work for a large Dutch webdevelopment company as the senior network engineer. Some of the sites are connected to each other through BGP. One of the network engineers in Hoofddorp has created a summary which aggregates some of the networks from AS 3 and advertises them to AS 1. Unfortunately there is a side-effect because AS 3 installs this summary as well.

## Goal

* All IP addresses have been preconfigured for you.
* Configure EBGP between Tilburg and Hoofddorp.
* Configure EBGP between Hoofddorp and Haarlem.
* Configure EBGP between Tilburg and Haarlem.
* Advertise the networks on the loopback interfaces on router Haarlem.
* Create a summary on router Hoofddorp that aggregates to network 172.16.0.0 / 16.
* Ensure AS 3 does not install this summary in its BGP table. You are not allowed to use any filters or prefix/access-lists.

## GNS3 2.2.56.1

Import `BGP Aggregation AS-Set IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `BGP Aggregation AS-Set.gns3` beside `project-files`.

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
| Haarlem | FastEthernet0/0 | Ethernet0/0 |
| Haarlem | FastEthernet1/0 | Ethernet0/1 |
| Hoofddorp | FastEthernet0/0 | Ethernet0/0 |
| Hoofddorp | FastEthernet1/0 | Ethernet0/1 |
| Tilburg | FastEthernet0/0 | Ethernet0/0 |
| Tilburg | FastEthernet1/0 | Ethernet0/1 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-bgp-aggregation-as-set.png)

## Video Solution

[http://www.youtube.com/watch?v=GK8_R7z2ieo](http://www.youtube.com/watch?v=GK8_R7z2ieo)
