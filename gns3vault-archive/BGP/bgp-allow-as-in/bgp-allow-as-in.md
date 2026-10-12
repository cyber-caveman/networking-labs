# BGP Allow AS In

## Scenario

An international toy store company needs your help. They use BGP to exchange routing information between their sites but everytime one of their IBGP routers fails they have connectivity issues. Let's see if you can help them out!

## Goal

* All IP addresses have been preconfigured for you.
* Configure IBGP within AS 1, source BGP updates from the loopback0 interfaces.
* Configure EBGP between router Woody and Buzz.
* Configure EBGP between router Andy and Buzz.
* Advertise the loopback1 interfaces in BGP on router Woody and Andy.
* Ensure router Woody and Andy can still reach each others loopback interfaces when router Rex fails.

## Additional Information

## GNS3 2.2.56.1

Import `BGP Allow AS in IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `BGP Allow AS in.gns3` beside `project-files`.

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
| Andy | FastEthernet0/0 | Ethernet0/0 |
| Andy | FastEthernet1/0 | Ethernet0/1 |
| Buzz | FastEthernet0/0 | Ethernet0/0 |
| Buzz | FastEthernet1/0 | Ethernet0/1 |
| Rex | FastEthernet0/0 | Ethernet0/0 |
| Rex | FastEthernet1/0 | Ethernet0/1 |
| Woody | FastEthernet0/0 | Ethernet0/0 |
| Woody | FastEthernet1/0 | Ethernet0/1 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-bgp-allow-as-in.png)

## Video Solution

* [Video Solution on YouTube](http://www.youtube.com/watch?v=Ec07c8Qz1CU)
