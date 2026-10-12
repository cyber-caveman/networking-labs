# BGP Disable Connected Check

![Network Topology](./topology-bgp-disable-connected-check.jpg)

## Scenario

You are a big poker fan and also a master in networking. Your favorite online poker room has been experiencing connection problems and you decided to help them out. They added another link to the service provider for extra redundancy, now the only thing left to do is making sure the BGP configuration is also correct...can you go all-in on this one?

## Goal

- All IP addresses have been preconfigured as specified in the topology picture.
- Create 2 static routes pointing to each others loopback interface:
  - For the 10.1.12.X link use an administrative distance of 10.
  - For the 10.2.12.X link use an administrative distance of 20.
- Ensure you can ping every IP address.
- Configure EBGP and use the correct AS numbers, the updates must be sourced from the loopback interfaces.
- You are not allowed to use EBGP Multihop to solve this problem.

## GNS3 2.2.56.1

Import `bgp-disable-connected-check-startup-configs IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `bgp-disable-connected-check-startup-configs.gns3` beside `project-files`.

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
| Flush | FastEthernet0/0 | Ethernet0/0 |
| Flush | FastEthernet1/0 | Ethernet0/1 |
| Straight | FastEthernet0/0 | Ethernet0/0 |
| Straight | FastEthernet1/0 | Ethernet0/1 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

## Video Solution

[Watch on YouTube](http://www.youtube.com/watch?v=vWC33cuf9y4)
