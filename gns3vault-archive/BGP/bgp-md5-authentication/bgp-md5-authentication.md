# BGP MD5 Authentication

## Scenario

You are working for a networking site and responsible for creating labs. After a day of working on BGP labs you notice you don't have any lab on MD5 authentication. BGP authentication is one of the features that is not too spectacular but you need to write an article to show other network gurus how it works...let's see if you can do it!

## Goal

- All IP addresses have been preconfigured for you as specified in the topology picture.
- Configure EBGP between AS 1 and AS 2.
- Configure MD5 authentication between router Piece and Cake.

## GNS3 2.2.56.1

Import `BGP MD5 Authentication IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `BGP MD5 Authentication.gns3` beside `project-files`.

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
| Cake | FastEthernet0/0 | Ethernet0/0 |
| Piece | FastEthernet0/0 | Ethernet0/0 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-bgp-md5-authentication.png)

## Video Solution

[BGP MD5 Authentication Lab Video](http://www.youtube.com/watch?v=hgO6zX6lCTg)
