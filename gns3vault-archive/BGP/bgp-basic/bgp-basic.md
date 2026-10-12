# BGP Basic

![Network Topology](./topology-bgp-basic.jpg)

## Scenario

You are responsible for the Internet connection of a company called "Wooden Shoe Corp". Their main site is located in Amsterdam and is currently connected with a single connection to an ISP. Because the Internet connection is critical to the company, you decided to become multi-homed by connecting to another provider. To connect to both providers and be ready for the future you decide to implement BGP.

## Goal

- All IP addresses have been preconfigured for you.
- Configure BGP on all routers, use the Autonomous System (AS) numbers as specified in the topology picture.
- The ISP routers have the following loopbacks:
  - ISP1 Loopback0: 2.2.2.2 /24
  - ISP2 Loopback0: 3.3.3.3 /28
- Advertise these loopbacks in BGP and ensure you have reachability from the Amsterdam router.
- Achieve full connectivity, only use BGP to achieve this.

## Additional Information

## GNS3 2.2.56.1

Import `bgp-basic-startup-configs IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `bgp-basic-startup-configs.gns3` beside `project-files`.

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
| AMSTERDAM | FastEthernet0/0 | Ethernet0/0 |
| AMSTERDAM | FastEthernet1/0 | Ethernet0/1 |
| ISP1 | FastEthernet0/0 | Ethernet0/0 |
| ISP2 | FastEthernet0/0 | Ethernet0/0 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

## Video Solution

- [BGP Basic - Video Solution](http://www.youtube.com/watch?v=vJUdum9Fdeo)
