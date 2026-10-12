# BGP Attribute MED

## Scenario

The biggest ISP in the carribean needs your help with BGP. One of the junior BGP network engineers configured some new sites but has trouble influencing traffic patterns. Show him how to configure BGP MED and you'll have the day off to enjoy the beach and some nice sunshine.

## Goal

- All IP addresses have been preconfigured for you as specified in the topology picture.
- Configure IBGP in AS 1.
- Configure EBGP between AS1 and AS 2.
- Advertise the 4.4.4.0 /24 network on router Jamaica.
- Ensure AS 1 will use the link between Cuba and Jamaica for traffic towards network 4.4.4.0 /24. You are only allowed to use the MED (metric) BGP attribute for this.

---

## GNS3 2.2.56.1

Import `BGP Attribute MED IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `BGP Attribute MED.gns3` beside `project-files`.

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
| Cuba | FastEthernet0/0 | Ethernet0/0 |
| Cuba | FastEthernet1/0 | Ethernet0/1 |
| Cuba | FastEthernet2/0 | Ethernet0/2 |
| Haiti | FastEthernet0/0 | Ethernet0/0 |
| Haiti | FastEthernet1/0 | Ethernet0/1 |
| Haiti | FastEthernet2/0 | Ethernet0/2 |
| Jamaica | FastEthernet0/0 | Ethernet0/0 |
| Jamaica | FastEthernet1/0 | Ethernet0/1 |
| Suriname | FastEthernet0/0 | Ethernet0/0 |
| Suriname | FastEthernet1/0 | Ethernet0/1 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-bgp-attribute-med.png)

## Video Solution

- [YouTube: BGP Attribute MED Configuration](http://www.youtube.com/watch?v=04kXmcJy9TQ)
