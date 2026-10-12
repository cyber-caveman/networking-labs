# BGP Confederations

## Scenario

You are the senior network engineer working for the federation of planets. BGP was developed on earth but is heavily used between planets as well. The network is expected to grow and to make you don't go crazy over configuring full mesh IBGP peerings you want to use a solution that is scalable for the future. You already know how to configure route reflectors and clusters but you haven't seen BGP confederations yet. Let's see if you can configure this.

## Goal

- All IP addresses have been preconfigured for you. I'm not showing them in the topology picture or it will be a big mess.
- Each router has a loopback0 interface.
- Configure OSPF within AS 2345 so the routers know how to reach each others loopback interfaces.
- Configure IBGP within AS 2345 but create confederations, use AS2, AS3, AS4 and AS 5.
- Configure EBGP between AS 1 and AS 2345.
- Configure EBGP between AS 2 and AS 2345.
- Advertise all loopback0 interfaces in BGP.
- Ensure all loopback0 interfaces are reachable throughout the BGP network.

## GNS3 2.2.56.1

Import `bgp-confederations-startup-configs IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `bgp-confederations-startup-configs.gns3` beside `project-files`.

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
| Crusher | FastEthernet0/0 | Ethernet0/0 |
| Crusher | FastEthernet1/0 | Ethernet0/1 |
| Crusher | FastEthernet2/0 | Ethernet0/2 |
| Data | FastEthernet0/0 | Ethernet0/0 |
| Data | FastEthernet1/0 | Ethernet0/1 |
| Data | FastEthernet2/0 | Ethernet0/2 |
| Picard | FastEthernet0/0 | Ethernet0/0 |
| Picard | FastEthernet1/0 | Ethernet0/1 |
| Riker | FastEthernet0/0 | Ethernet0/0 |
| Riker | FastEthernet1/0 | Ethernet0/1 |
| Worf | FastEthernet0/0 | Ethernet0/0 |
| Worf | FastEthernet1/0 | Ethernet0/1 |
| Worf | FastEthernet2/0 | Ethernet0/2 |
| laForge | FastEthernet0/0 | Ethernet0/0 |
| laForge | FastEthernet1/0 | Ethernet0/1 |
| laForge | FastEthernet2/0 | Ethernet0/2 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-bgp-confederations.png)

## Video Solution

http://www.youtube.com/watch?v=y1v_haNIM-w
