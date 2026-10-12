# BGP Traffic Engineering Unsuppress-Map

## Scenario

The mystical creature corporation has a large international network of fantasy enthusiastics people sharing new mystical rumors. They are running BGP to exchange routing information between each other. At some point in the network you are aggregating a number of prefixes but a downside of this that you are unable to use traffic engineering. Let's see what solution you can come up with.

## Goal

- All IP addresses have been preconfigured for you.
- Configure IBGP within AS 3.
- Configure EBGP between AS 2 and AS 3.
- Configure EBGP between AS 1 and AS 2.
- Configure router Blob to advertise all loopback interfaces in BGP.
- Configure BGP aggregation on router Behemoth to summarize the loopback interfaces in the most optimal summary towards AS 3.
- Configure the network so AS 3 sends traffic to network 172.16.0.0 /24 through router Banshee.
- Configure the network so AS 3 sends traffic to network 172.16.1.0 /24 through router BigFoot.
- You are not allowed to use static, default routes or any IGP. Do not remove the summary on router Behemoth.
- You are not allowed to use any BGP communities or attributes.

## GNS3 2.2.56.1

Import `BGP Traffic Engineering Unsuppress-Map IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `BGP Traffic Engineering Unsuppress-Map.gns3` beside `project-files`.

Routers use the preferred IOU L3 image `x86_64_crb_linux-adventerprisek9-ms.bin`
(MD5 `4a2fce8de21d1831fbceffd155e41ae7`), template
`b3b10b90-adfb-43f8-b289-b68bcf322ad8`, 768 MB RAM, 512 KB NVRAM,
four Ethernet and four serial adapters, with automatically allocated consoles.
Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Physical interface names and link endpoints are updated together in startup and
all supplied final configs. Original bandwidth and delay are explicit where
needed to preserve EIGRP/IGP metric inputs. Source protocol settings and intended
startup state are preserved; final configs are not loaded at startup.

Unmanaged Ethernet switches retain their original type and VLAN settings.

| Router | Original interface | IOU interface |
| --- | --- | --- |
| Banshee | FastEthernet0/0 | Ethernet0/0 |
| Banshee | FastEthernet1/0 | Ethernet0/1 |
| Behemoth | FastEthernet0/0 | Ethernet0/0 |
| Behemoth | FastEthernet1/0 | Ethernet0/1 |
| Behemoth | FastEthernet2/0 | Ethernet0/2 |
| BigFoot | FastEthernet0/0 | Ethernet0/0 |
| BigFoot | FastEthernet1/0 | Ethernet0/1 |
| Blob | FastEthernet0/0 | Ethernet0/0 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-bgp-traffic-engineering-unsuppress-map.png)

## Video Solution

[YouTube Video: BGP Traffic Engineering Unsuppress Map](http://www.youtube.com/watch?v=T9A_tP2vlVg)
