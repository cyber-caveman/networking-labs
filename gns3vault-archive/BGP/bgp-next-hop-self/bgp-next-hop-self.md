# BGP Next hop self

![Network Topology](./topology-bgp-next-hop-self.png)

## Scenario:

As a junior networking engineer you were always fascinated with science fiction movies, that's why you are now working at a company specialized in special effects. The closest you got to light speed was sending bits and bytes with electricity through wires...nevertheless there is a task waiting for you. You need to configure BGP between your network (AS100) and the service provider (AS200). Setting up BGP was no problem for you, but users behind router Luke are complaining they can't access networks in AS 200. Time for you to solve this problem...you feel the force is strong within you so this should be a piece of cake!

## Goal:

* All IP addresses have been preconfigured as specified in the topology picture.
* Configure IBGP between router Hansolo and Luke, use AS 100, use the loopback0 interfaces as source for BGP.
* Configure EBGP between router Hansolo and Leia.
* Ensure both BGP neighbor relationships are up.
* Router HanSolo: Advertise the 192.168.12.0/24 network into BGP.
* Router Leia: Advertise the 3.3.3.0 /24 on the loopback interface into BGP.
* Ensure you can ping this network from router Hansolo.
* Try to ping this network from router Luke, why does this fail?
* Fix this problem by using a BGP command on router Hansolo. You are not allowed to advertise the 192.168.13.X network in BGP.

## GNS3 2.2.56.1

Import `bgp-next-hop-self-startup-configs IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `bgp-next-hop-self-startup-configs.gns3` beside `project-files`.

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
| HanSolo | FastEthernet1/0 | Ethernet0/0 |
| HanSolo | Serial0/0 | Serial4/0 |
| HanSolo | Serial0/1 | Serial4/1 |
| HanSolo | Serial0/2 | Serial4/2 |
| HanSolo | Serial0/3 | Serial4/3 |
| Leia | Serial0/0 | Serial4/0 |
| Leia | Serial0/1 | Serial4/1 |
| Leia | Serial0/2 | Serial4/2 |
| Leia | Serial0/3 | Serial4/3 |
| Luke | FastEthernet0/0 | Ethernet0/0 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology:

## Video Solution:

http://www.youtube.com/watch?v=kjQ6cUcyVfI
