# BGP Attribute Router ID

![Network Topology](./topology-bgp-attribute-router-id.png)

## Scenario

You are one of the trainees at a fairly small ISP. Your boss is on vacation and all colleagues are out of the office troubleshooting problems at customers. You receive a phonecall of one of the network engineers in NewDelhi who complains you are sending all traffic meant for Paris through his network and he wants it solved in the next 10 minutes. You google a bit for BGP attributes but it isn't making sense much to you at this moment...you do read something about Router ID so maybe that'll be helpful to you...ignorance is bliss right? Let's go!

## Goal

- All IP addresses have been preconfigured for you as specified in the topology picture.
- Configure EBGP between all ASes.
- Advertise the loopback0 interface on router Barcelona in BGP.
- Router Paris should have two paths to reach network 1.1.1.0 /24.
- Ensure router Paris sends traffic to router Sydney to reach network 1.1.1.0 /24. You are only allowed to make changes on router Sydney.

## GNS3 2.2.56.1

Import `BGPAttributeRouterID IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `BGPAttributeRouterID.gns3` beside `project-files`.

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
| Barcelona | FastEthernet0/0 | Ethernet0/0 |
| Barcelona | FastEthernet1/0 | Ethernet0/1 |
| NewDelhi | FastEthernet0/0 | Ethernet0/0 |
| NewDelhi | FastEthernet1/0 | Ethernet0/1 |
| Paris | FastEthernet0/0 | Ethernet0/0 |
| Paris | FastEthernet1/0 | Ethernet0/1 |
| Sydney | FastEthernet0/0 | Ethernet0/0 |
| Sydney | FastEthernet1/0 | Ethernet0/1 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Video Solution

[YouTube - BGP Attribute Router ID Solution](http://www.youtube.com/watch?v=0x--bvHJsuY)
