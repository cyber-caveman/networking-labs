# BGP Communities Delete and Additive

## Scenario

Mushroom Kingdom is stronger than ever before. Some of the citizens have switched their career to become network engineers specializing themselves in BGP. One of the moustached network engineers is sending some communities values along with prefixes but you want to change this slightly.

## Goal

- All IP addresses have been preconfigured for you.
- Configure EBGP between AS 1 and AS 2.
- Configure EBGP between AS 2 and AS 3.
- Advertise the loopback0 interface on router Mario in BGP.
- Configure router Mario so it sends community value 100:100, 200:200 and 300:300 along with the update.
- Configure router Luigi to remove community value 200:200 and add 400:400 instead.

## GNS3 2.2.56.1

Import `BGP Communities Delete & Additive IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `BGP Communities Delete & Additive.gns3` beside `project-files`.

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
| Luigi | FastEthernet0/0 | Ethernet0/0 |
| Mario | FastEthernet0/0 | Ethernet0/0 |
| Toad | FastEthernet0/0 | Ethernet0/0 |
| Toad | FastEthernet1/0 | Ethernet0/1 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-bgp-communities-delete-and-additive.png)

## Video Solution

http://www.youtube.com/watch?v=MvYUKty1lCM
