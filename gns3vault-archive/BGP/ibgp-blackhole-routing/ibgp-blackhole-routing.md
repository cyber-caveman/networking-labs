# BGP IBGP Blackhole Routing

![Network Topology](./topology-ibgp-blackhole-routing.jpg)

## Scenario

You are applying for a new job at a Dutch networking company specialised in routing & switching solutions. One of the senior networking engineers decides to take you up the test and see what your skills are like. He shows you an IBGP problem where traffic is being blackholed...time for you to show him a trick or two.

## Goal

- IP addresses have been preconfigured as specified in the topology picture.
- Configure IBGP AS 123 on router King and Queen, use the physical interfaces.
- The senior network engineer has prohibited you from making any changes to router Prince.
- Advertise the loopback0 interfaces from router King and Queen into BGP.
- You are not allowed to use static routes to reach the loopback interfaces, use IBGP to achieve this.
- Ensure you can ping each others loopback addresses from router King or Queen.

## GNS3 2.2.56.1

Import `bgp-blackhole-startup-configs IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `bgp-blackhole-startup-configs.gns3` beside `project-files`.

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
| King | FastEthernet0/0 | Ethernet0/0 |
| Prince | FastEthernet0/0 | Ethernet0/0 |
| Prince | FastEthernet1/0 | Ethernet0/1 |
| Queen | FastEthernet0/0 | Ethernet0/0 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

## Video Solution

[Video Solution on YouTube](http://www.youtube.com/watch?v=tX_mLFebwuw)
