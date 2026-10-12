# EIGRP Timers

## Scenario

You are the network engineer for a fairly large international operating company. One of the trainees in the company is studying for his CCNA and decided to practice on some of the company routers. EIGRP is now messed up and it's up to you to reconfigure the timers again.

## Goal

* All IP addresses have been preconfigured for you.
* Configure EIGRP on all interfaces.
* Router Boston should have a holddown timers of 9 seconds for all neighbors.
* Router NewYork should send an EIGRP hello packet every 5 seconds to router Philadelphia.
* Configure EIGRP so lost routes are stuck-in-active if you don't get a reply to your query in 2 minutes.

## GNS3 2.2.56.1

Import `EIGRP Timers IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `EIGRP Timers.gns3` beside `project-files`.

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
| Boston | FastEthernet0/0 | Ethernet0/0 |
| Boston | FastEthernet1/0 | Ethernet0/1 |
| NewYork | FastEthernet0/0 | Ethernet0/0 |
| NewYork | FastEthernet1/0 | Ethernet0/1 |
| Philadelphia | FastEthernet0/0 | Ethernet0/0 |
| Philadelphia | FastEthernet1/0 | Ethernet0/1 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-eigrp-timers.png)

## Video Solution

http://www.youtube.com/watch?v=wCuPubjZ7YQ
