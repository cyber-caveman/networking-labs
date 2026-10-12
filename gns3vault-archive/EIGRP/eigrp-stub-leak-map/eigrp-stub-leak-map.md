# EIGRP Stub Leak Map

![Network Topology](./topology-eigrp-stub-leak-map.jpg)

## Scenario

You are enjoying life as a lifeguard and parttime network administrator. Just like real life your routers cry out for help by sending queries whenever they have lost a certain network. You decide to implement EIGRP Stub routing and only allow some of the networks to be advertised. Now you have another problem...people are complaining about reachability..up to you to be there and fix it!

## Goal

- All IP addresses have been preconfigured for you.
- Router Yasmine has a loopback interface: Loopback0: 3.3.3.3 /24
- Router Carmen has 2 loopback interfaces: Loopback0: 4.4.4.4 /24 and Loopback1: 44.44.44.44 /24
- Configure router Yasmine so only the directly connected networks are advertised towards the neighbors.
- Router David and Pamela should have 4.4.4.0 /24 in their routing table, learned from EIGRP.
- 44.44.44.0 /24 is not allowed to be in the routing table of router David and Pamela.

## GNS3 2.2.56.1

Import `eigrp-stub-leak-map-startup-configs IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `eigrp-stub-leak-map-startup-configs.gns3` beside `project-files`.

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
| DAVID | FastEthernet0/0 | Ethernet0/0 |
| PAMELA | FastEthernet0/0 | Ethernet0/0 |
| YASMINE | FastEthernet0/0 | Ethernet0/0 |
| YASMINE | FastEthernet1/0 | Ethernet0/1 |
| YASMINE | FastEthernet2/0 | Ethernet0/2 |
| CARMEN | FastEthernet0/0 | Ethernet0/0 |

### Source notes

No completed solution configs were supplied; none were invented.

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

You need to register to download the GNS3 Topology File. (Registration is Free!)

## Video Solution

http://www.youtube.com/watch?v=VRsVKQLupSs
