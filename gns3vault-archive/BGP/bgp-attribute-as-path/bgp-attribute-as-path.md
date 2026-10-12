# BGP Attribute AS Path

## Scenario

A local steelmill has asked you to help them with their BGP network. The steelmill has two sites and routing information is used by using BGP. Everything is working fine except the backup link is being used for all traffic at this moment. Can you influence BGP so the traffic path is changed? Are you as tough as steel?

## Goal

- All IP addresses have been preconfigured for you as specified in the topology picture.
- Configure EBGP between router Copper and Zinc.
- Configure EBGP between router Steel and Zinc.
- Configure IBGP in AS 1.
- Advertise the 4.4.4.0 /24 network on router Zinc.
- Make sure router Aluminium sends traffic to 4.4.4.0 /24 to router Steel, you are only allowed to use the AS Path attribute.

## GNS3 2.2.56.1

Import `BGP Attribute AS Path IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `BGP Attribute AS Path.gns3` beside `project-files`.

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
| Aluminium | FastEthernet0/0 | Ethernet0/0 |
| Aluminium | FastEthernet1/0 | Ethernet0/1 |
| Copper | FastEthernet0/0 | Ethernet0/0 |
| Copper | FastEthernet1/0 | Ethernet0/1 |
| Copper | FastEthernet2/0 | Ethernet0/2 |
| Steel | FastEthernet0/0 | Ethernet0/0 |
| Steel | FastEthernet1/0 | Ethernet0/1 |
| Steel | FastEthernet2/0 | Ethernet0/2 |
| Zinc | FastEthernet0/0 | Ethernet0/0 |
| Zinc | FastEthernet1/0 | Ethernet0/1 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-bgp-attribute-as-path.png)

## Video Solution

[Video Solution on YouTube](http://www.youtube.com/watch?v=DF7gjBvToPs)
