# RIP EIGRP Redistribution Route Tagging

## Scenario

The Australia Zoo has hired you as a network engineer responsible for all bits & bytes in the zoo. As an experiment the zoo decided to have the kangaroos and dolphins around the same lake to study the interaction between the animals. Both departments need to have access to each other's data which means you'll have to exchange routing information. To make sure there is no single point of failure you will use router Lassie and Willy to configure two-way redistribution. This however will also introduce new problems like routing loops or sub-optimal routing, it's up to you to enable redistribution and solve any problems along the way...

## Goal

* All IP addresses have been preconfigured for you.
* RIP and EIGRP have been preconfigured for you on the corresponding routers.
* Enable two-way redistribution between RIP and EIGRP on router Lassie and Willy.
* You notice that router Willy or Lassie are sending traffic to 4.4.4.4 towards router Flipper, make sure you get rid of this sub-optimal routing.
* Use route tagging to accomplish this.

## GNS3 2.2.56.1

Import `rip2eigrp IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `rip2eigrp.gns3` beside `project-files`.

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
| Flipper | FastEthernet0/0 | Ethernet0/0 |
| Flipper | FastEthernet1/0 | Ethernet0/1 |
| Lassie | FastEthernet0/0 | Ethernet0/0 |
| Lassie | FastEthernet1/0 | Ethernet0/1 |
| Willy | FastEthernet0/0 | Ethernet0/0 |
| Willy | FastEthernet1/0 | Ethernet0/1 |
| Skippy | FastEthernet0/0 | Ethernet0/0 |
| Skippy | FastEthernet1/0 | Ethernet0/1 |

### Source notes

No completed solution configs were supplied; none were invented.

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-rip-eigrp-redistribution-route-tagging.png)
