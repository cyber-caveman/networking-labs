# EIGRP Router ID

## Scenario

Your colleague asks for your help with a strange EIGRP problem. He redistributed a network into EIGRP but for some reason it doesn't show up in the routing table of one of the routers. You verify the redistribution commands are looking good and there are filters in action. Let's see if you can find the root of this problem...

## Goal

* All IP addresses have been preconfigured for you.
* Configure EIGRP on all FastEthernet interfaces.
* Redistribute the loopback interface on router Spy into EIGRP.
* Ensure router CopyCat does not see network 2.2.2.0 /24 in it's routing table without applying any filtering techniques.

## GNS3 2.2.56.1

Import `EIGRP Router ID IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `EIGRP Router ID.gns3` beside `project-files`.

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
| CopyCat | FastEthernet0/0 | Ethernet0/0 |
| Imposter | FastEthernet0/0 | Ethernet0/0 |
| Imposter | FastEthernet1/0 | Ethernet0/1 |
| Spy | FastEthernet0/0 | Ethernet0/0 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-eigrp-router-id.png)

## Video Solution

http://www.youtube.com/watch?v=Ez1QBxA0Eck
