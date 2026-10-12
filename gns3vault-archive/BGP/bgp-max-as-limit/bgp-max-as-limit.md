# BGP Max AS Limit

## Scenario

AsianFish inc. is expanding their business towards Europe so they need to expand their network as well. BGP has been configured for inter-AS connectivity but you want to make sure you don't receive just any prefix on the Internet. Business has been fishy lately so there's no budget for routers with enough memory to carry all the BGP prefixes. To make sure your routers keep running you only want to accept prefixes from a number of autonomous systems.

## Goal

* All IP addresses have been preconfigured for you.
* Configure EBGP between AS 1 - 2, AS 2 - 3 and AS 3 - 4.
* Advertise the loopback0 interfaces of all routers in BGP.
* Configure router Tilburg so it only allows prefixes from directly connected autonomous systems.
* You are not allowed to use as path filtering or any regular expressions.

## GNS3 2.2.56.1

Import `BGP Max AS Limit IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `BGP Max AS Limit.gns3` beside `project-files`.

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
| NewYork | FastEthernet0/0 | Ethernet0/0 |
| NewYork | FastEthernet1/0 | Ethernet0/1 |
| Shanghai | FastEthernet0/0 | Ethernet0/0 |
| Tilburg | FastEthernet0/0 | Ethernet0/0 |
| Tilburg | FastEthernet1/0 | Ethernet0/1 |
| Tokio | FastEthernet0/0 | Ethernet0/0 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-bgp-max-as-limit.png)

## Video Solution

http://www.youtube.com/watch?v=dE2asMqoM7o
