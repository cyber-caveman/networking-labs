# BGP Local AS

## Scenario

The local hedgehog protection foundation is merging with the local Fox protection program. The networks are connected through BGP and part of the migration means you have to change your AS number. You don't mind doing this but you don't want to break the BGP neighbor adjacency.

## Goal

* All IP addresses have been preconfigured for you.
* Configure EBGP on router Sonic and use AS number 1.
* Configure EBGP on router Tails and use AS number 2.
* You have to configure router Tails with the "neighbor remote-as 100" command.
* Ensure your EBGP configuration is working.

## GNS3 2.2.56.1

Import `BGPLocalAS IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `BGPLocalAS.gns3` beside `project-files`.

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
| Sonic | FastEthernet0/0 | Ethernet0/0 |
| Tails | FastEthernet0/0 | Ethernet0/0 |
| Tails | FastEthernet1/0 | Ethernet0/1 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-bgp-local-as.png)

## Video Solution

[BGP Local AS Video Solution](http://www.youtube.com/watch?v=mY_sYY1GwfI)
