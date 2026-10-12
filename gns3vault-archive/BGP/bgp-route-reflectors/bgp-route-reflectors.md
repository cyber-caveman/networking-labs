# BGP Route Reflectors

![Network Topology](./topology-bgp-route-reflectors.jpg)

## Scenario

Company Veggie inc. is growing rapidly and the network needs to support the growing company. More routers are added every week and network engineers are complaining it takes too much time to setup BGP. Especially typing in all the neighbor commands is becoming an annoyance for them. Time for you to show up and teach them what a route-reflector is!

## Goal

- All IP addresses have been preconfigured as specified in the topology picture.
- All routers have the following loopback interface:
  - Cherry: Loopback0: 1.1.1.1 /24
  - Berry: Loopback0: 2.2.2.2 /24
  - Dairy: Loopback0: 3.3.3.3 /24
- Configure OSPF on all routers, ensure you have full reachability.
- Disable the link between Cherry and Berry.
- Configure BGP between Cherry and Dairy.
- Configure BGP between Berry and Dairy.
- Do not configure BGP between Berry and Cherry.
- Create a new loopback interface on router Berry:
  - Loopback1: 22.22.22.22 /24
- Advertise this loopback into BGP by using a network command.
- Ensure you see 22.22.22.0 network in the routing table of router Dairy.
- Do you see this network in the routing table of router Cherry? Why not?
- Change the configuration on router Dairy so that router Cherry will have the 22.22.22.0 network in it's routing table (hint: *Route Reflector*).

## GNS3 2.2.56.1

Import `bgp-route-reflectors-startup-configs IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `bgp-route-reflectors-startup-configs.gns3` beside `project-files`.

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
| Berry | FastEthernet0/0 | Ethernet0/0 |
| Berry | Serial1/0 | Serial4/0 |
| Berry | Serial1/1 | Serial4/1 |
| Berry | Serial1/2 | Serial4/2 |
| Berry | Serial1/3 | Serial4/3 |
| Cherry | FastEthernet0/0 | Ethernet0/0 |
| Cherry | Serial1/0 | Serial4/0 |
| Cherry | Serial1/1 | Serial4/1 |
| Cherry | Serial1/2 | Serial4/2 |
| Cherry | Serial1/3 | Serial4/3 |
| Dairy | Serial0/0 | Serial4/0 |
| Dairy | Serial0/1 | Serial4/1 |
| Dairy | Serial0/2 | Serial4/2 |
| Dairy | Serial0/3 | Serial4/3 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

## Video Solution

http://www.youtube.com/watch?v=K39KAX1zNzQ
