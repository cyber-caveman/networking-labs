---
# Title: "BGP Attribute Origin"
# Category: "BGP"
# Wordpress_id: 757
---

## Scenario

You are a gunslinger living in Arizona and also a network engineer for the town network. To make sure your town has connectivity with other towns you have configured the town router with BGP. Another town is using AS 1 and they are advertising a network to you. Unfortunately they have misconfigured their network so you are sending traffic to the wrong router. Your own router is an old model from 1873 and doesn't allow many changes...let's see if you can configure AS 1 to solve your problem.

## Goal

* All IP addresses have been preconfigured for you as specified in the topology picture.
* Configure EBGP between router Lonergan and Colorado.
* Configure EBGP between router Claiborne and Colorado.
* Advertise the 13.13.13.0 /24 network on router Lonergan and Claiborne.
* Make sure router Colorado sends traffic to 13.13.13.0 /24 to router Claiborne, you are only allowed to use the origin attribute.

## GNS3 2.2.56.1

Import `bgp-attribute-origin-startup-configs IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `bgp-attribute-origin-startup-configs.gns3` beside `project-files`.

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
| Claiborne | FastEthernet0/0 | Ethernet0/0 |
| Colorado | FastEthernet0/0 | Ethernet0/0 |
| Colorado | FastEthernet1/0 | Ethernet0/1 |
| Lonergan | FastEthernet0/0 | Ethernet0/0 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-bgp-attribute-origin.png)

## Video Solution

[BGP Attribute Origin Video Solution](http://www.youtube.com/watch?v=0n65ou1CASI)
