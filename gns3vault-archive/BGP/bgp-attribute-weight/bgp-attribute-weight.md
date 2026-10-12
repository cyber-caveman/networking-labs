# BGP Attribute Weight

## Scenario

You wake up in what seems to be a server room...trapped in a chair and tied up by what seems to be networking cabling. In front of you is a LED screen showing you a lady in uniform. There are some problems with the BGP network and she asks you urgently if you can fix the problems. The network is running BGP but there is no load sharing at all. You need to configure AS12 and AS 34 by using the weight attribute to manipulate traffic patterns. You get 8 minutes before the network is overloaded and crashes...

## Goal

- All IP addresses have been preconfigured for you as specified in the topology picture.
- Configure IBGP within AS12 and AS34.
- Configure EBGP between router Stevens and Rutledge.
- Configure EBGP between router Warren and Goodwin.
- Advertise all physical interfaces in BGP.
- Advertise the loopback0 and loopback1 interfaces in BGP on all routers.
- Ensure you have full reachability, all physical interfaces and loopback interfaces should be reachable from any router.
- You are only allowed to use the weight attribute for the upcoming tasks.
- Configure router Stevens so traffic to 3.3.3.0 /24 is sent to router Warren.
- Configure router Stevens to ensure traffic to 44.44.44.0 /24 keeps the same next hop even when someone would change another BGP attribute like local preference or origin.
- Configure router Rutledge so traffic to 2.2.2.0 /24 is sent to router Goodwin.
- Configure router Goodwin so traffic to 11.11.11.0 /24 is sent to router Rutledge.

## GNS3 2.2.56.1

Import `bgp-attribute-weight IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `bgp-attribute-weight.gns3` beside `project-files`.

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
| Rutledge | FastEthernet0/0 | Ethernet0/0 |
| Rutledge | FastEthernet1/0 | Ethernet0/1 |
| Goodwin | FastEthernet0/0 | Ethernet0/0 |
| Goodwin | FastEthernet1/0 | Ethernet0/1 |
| Stevens | FastEthernet0/0 | Ethernet0/0 |
| Stevens | FastEthernet1/0 | Ethernet0/1 |
| Warren | FastEthernet0/0 | Ethernet0/0 |
| Warren | FastEthernet1/0 | Ethernet0/1 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-bgp-attribute-weight.png)

## Video Solution

http://www.youtube.com/watch?v=3UVg8mzJ_Us
