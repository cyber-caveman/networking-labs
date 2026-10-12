# BGP Timers

## Scenario

You are a film producer and part-time network engineer. You use BGP to connect two sites to each other but you feel things are a little slow. Let's see if you can tune up some of those BGP timers.

## Goal

* All IP addresses have been preconfigured for you.
* Configure EBGP between AS 1 and AS 2.
* The BGP scanner should run every 30 seconds on both routers.
* Ensure both routers don't wait till the next BGP advertisement-interval but send updates immediately.
* When there is no activity after 15 seconds the BGP peering should be dropped.

## GNS3 2.2.56.1

Import `BGP Timers IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `BGP Timers.gns3` beside `project-files`.

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
| Kendrick | FastEthernet0/0 | Ethernet0/0 |
| Scott | FastEthernet0/0 | Ethernet0/0 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-bgp-timers.png)

## Video Solution

[BGP Timers - Video Solution](http://www.youtube.com/watch?v=TTBqpG900YA)
