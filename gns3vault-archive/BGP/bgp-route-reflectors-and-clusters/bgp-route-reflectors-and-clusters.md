# BGP Route Reflectors and Clusters

## Scenario

As the senior network engineer for a large international company you are always trying to optimize your network and get the most out of your time. The network has a lot of IBGP routers and you got sick of configuring all those neighbor peerings. To fix this you configured the network with some route reflectors...this has saved you a lot of work but you want to take it one step further by clustering the network.

## Goal

* All IP addresses have been preconfigured for you. You don't see them in the topology picture or it would look like a picasso painting.
* Each router has a loopback0 interface.
* All routers belong to AS 1.
* Configure router Tilburg as the route-reflector for router Amsterdam and Utrecht. Use cluster-ID 1.1.1.1.
* Configure router NewYork as the route-reflector for router LosAngeles and Boston. Use cluster-ID 4.4.4.4.
* Configure router Hamburg as the route-reflector for router Dusseldorf and Berlin. Use cluster-ID 7.7.7.7
* Configure router Tilburg, Newyork and Hamburg with the correct IBGP neighbor peerings.
* Advertise all loopback0 interfaces in BGP.
* Ensure you have full reachability within AS 1. All loopback0 interfaces should be reachable.

## GNS3 2.2.56.1

Import `BGP Route Reflectors and Clusters IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `BGP Route Reflectors and Clusters.gns3` beside `project-files`.

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
| Amsterdam | FastEthernet0/0 | Ethernet0/0 |
| Amsterdam | FastEthernet1/0 | Ethernet0/1 |
| Berlin | FastEthernet0/0 | Ethernet0/0 |
| Berlin | FastEthernet1/0 | Ethernet0/1 |
| Boston | FastEthernet0/0 | Ethernet0/0 |
| Boston | FastEthernet1/0 | Ethernet0/1 |
| Dusseldorf | FastEthernet0/0 | Ethernet0/0 |
| Dusseldorf | FastEthernet1/0 | Ethernet0/1 |
| Hamburg | FastEthernet0/0 | Ethernet0/0 |
| Hamburg | FastEthernet1/0 | Ethernet0/1 |
| Hamburg | FastEthernet2/0 | Ethernet0/2 |
| Hamburg | FastEthernet3/0 | Ethernet0/3 |
| LosAngeles | FastEthernet0/0 | Ethernet0/0 |
| LosAngeles | FastEthernet1/0 | Ethernet0/1 |
| NewYork | FastEthernet0/0 | Ethernet0/0 |
| NewYork | FastEthernet1/0 | Ethernet0/1 |
| NewYork | FastEthernet2/0 | Ethernet0/2 |
| NewYork | FastEthernet3/0 | Ethernet0/3 |
| Tilburg | FastEthernet0/0 | Ethernet0/0 |
| Tilburg | FastEthernet1/0 | Ethernet0/1 |
| Tilburg | FastEthernet2/0 | Ethernet0/2 |
| Tilburg | FastEthernet3/0 | Ethernet0/3 |
| Utrecht | FastEthernet0/0 | Ethernet0/0 |
| Utrecht | FastEthernet1/0 | Ethernet0/1 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-bgp-route-reflectors-and-clusters.png)

## Video Solution

[BGP Route Reflectors and Clusters Video Solution](http://www.youtube.com/watch?v=Naq0v_cKSIM)
