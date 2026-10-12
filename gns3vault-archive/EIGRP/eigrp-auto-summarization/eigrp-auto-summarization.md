# EIGRP Auto Summarization

![Network Topology](./topology-eigrp-auto-summarization.jpg)

## Scenario

Working as a freelance network engineer you have some strange customers. One of them is a scatterbrain inventor who claims to work on a 'world-changing' machine. He has problems with his network and is currently unable to upload some schematics. The routing protocol of choice is EIGRP (Enhanced Interior Gateway Routing Protocol) and since you are an expert you should be able to fix his problems....back to the labs!

## Goal

- All IP addresses have been preconfigured for you.
- EIGRP AS123 has been preconfigured for you and is advertising all networks.
- You are not allowed to disable EIGRP auto-summarization.
- When you try to reach the networks on the loopback interfaces from router Delorean you have reachability problems, solve this problem.
- When you send a ping from router McFly's loopback0 interface to router Brown's loopback0 interface you have reachability problems, solve this problem.
- Ensure there is full reachability for all networks.

## GNS3 2.2.56.1

Import `eigrp-auto-summarization-startup-configs IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `eigrp-auto-summarization-startup-configs.gns3` beside `project-files`.

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
| MCFLY | FastEthernet0/0 | Ethernet0/0 |
| DELOREAN | FastEthernet0/0 | Ethernet0/0 |
| DELOREAN | FastEthernet1/0 | Ethernet0/1 |
| BROWN | FastEthernet0/0 | Ethernet0/0 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

## Video Solution

[EIGRP Auto Summarization Video Solution](http://www.youtube.com/watch?v=GGWXNQ4O5tY)
