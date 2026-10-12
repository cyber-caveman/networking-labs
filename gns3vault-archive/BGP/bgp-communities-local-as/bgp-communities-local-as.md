# BGP Communities Local-AS

## Scenario

The company you work for is a large game console development company. They have a large international network and you are responsible for the BGP configuration. One of the ASes is so large that you decided to implement confederations. For security reasons you need to make sure not all prefixes are advertised to all routers within AS 2.

## Goal

- All IP addresses have been preconfigured for you.
- Configure AS 2 with the federations AS 10 and AS 20.
- Configure EBGP between AS 1 and AS 2.
- Advertise the loopback0 interface on router Wintendo in BGP.
- Ensure network 1.1.1.0 /24 only shows up in sub-AS 10. Use the correct community to achieve this.

## GNS3 2.2.56.1

Import `BGP Communities Local AS IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `BGP Communities Local AS.gns3` beside `project-files`.

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
| Etari | FastEthernet0/0 | Ethernet0/0 |
| Etari | FastEthernet1/0 | Ethernet0/1 |
| MacroZoft | FastEthernet0/0 | Ethernet0/0 |
| MacroZoft | FastEthernet1/0 | Ethernet0/1 |
| MacroZoft | FastEthernet2/0 | Ethernet0/2 |
| Seega | FastEthernet0/0 | Ethernet0/0 |
| Seega | FastEthernet1/0 | Ethernet0/1 |
| Wintendo | FastEthernet0/0 | Ethernet0/0 |
| Zony | FastEthernet0/0 | Ethernet0/0 |
| Zony | FastEthernet1/0 | Ethernet0/1 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-bgp-communities-local-as.png)

## Video Solution

[BGP Communities Local-AS Video Solution](http://www.youtube.com/watch?v=h0vr2yp2stA)
