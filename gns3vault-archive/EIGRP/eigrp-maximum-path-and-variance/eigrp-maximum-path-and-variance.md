# EIGRP Maximum Path and Variance

![Network Topology](./topology-eigrp-maximum-path-and-variance.jpg)

## Scenario

As a fan of comedy movies you are making sure your network is optimized so you can send videos without any disruptions in the network. You heard EIGRP (Enhanced Interior Gateway Routing Protocol) is a good choice since the failover speed is low and it's able to load balance between unequal paths. There are 3 different serial links and you want to make the optimal use of them. Whenever a link fails you need to make sure the routing protocol converges as soon as it can....surely you can solve this!

## Goal

* All IP addresses have been preconfigured for you:
  * Leslie: 192.168.X.1 /24 (.1 - .2 & .3 on serial links)
  * Leslie L0: 1.1.1.1 /24
  * Airplane: 192.168.X.2 /24 (.1 - .2 & .3 on serial links)
  * Airplane F0/0: 192.168.23.2 /24
  * Shirley F0/0: 192.168.23.3 /24
  * Shirley L0: 3.3.3.3 /24

* Configure EIGRP AS123 on all routers, advertise all networks.
* You are not allowed to make changes to the K values or Bandwidth on interfaces.
* Disable EIGRP auto-summarization.
* Make sure that only S0/0 and S0/1 are visible in the routing table and used for sending traffic.
* When S0/0 and S0/1 both fail make sure that S0/2 takes over.

## GNS3 2.2.56.1

Import `eigrp-maximum-path-variance-startup-configs IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `eigrp-maximum-path-variance-startup-configs.gns3` beside `project-files`.

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
| LESLIE | Serial0/0 | Serial4/0 |
| LESLIE | Serial0/1 | Serial4/1 |
| LESLIE | Serial0/2 | Serial4/2 |
| LESLIE | Serial0/3 | Serial4/3 |
| AIRPLANE | FastEthernet1/0 | Ethernet0/0 |
| AIRPLANE | Serial0/0 | Serial4/0 |
| AIRPLANE | Serial0/1 | Serial4/1 |
| AIRPLANE | Serial0/2 | Serial4/2 |
| AIRPLANE | Serial0/3 | Serial4/3 |
| SHIRLEY | FastEthernet0/0 | Ethernet0/0 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Video Solution

* http://www.youtube.com/watch?v=CafZ1eQ5CEY
