# BGP Remove Private AS

## Scenario

The imperial museum corporation has many museums around the world. All networks are connected and BGP is used as the routing protocol. One of the autonomous systems is a transit AS and has two autonomous systems behind it with private AS numbers. You want to ensure that nobody sees those private AS numbers without having trouble with reachability.

## Goal

- All IP addresses have been preconfigured for you.
- Configure EBGP between AS 1 and AS 2.
- Configure EBGP between AS 2 and AS 65503.
- Configure EBGP between AS 2 and AS 65504.
- Advertise the loopback0 interfaces on router Kaiser and Caesar.
- Ensure AS 1 doesn't see the private AS numbers but has connectivity to network 3.3.3.0 /24 and 4.4.4.0 /24.

## GNS3 2.2.56.1

Import `BGP Remove Private AS IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `BGP Remove Private AS.gns3` beside `project-files`.

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
| Caesar | FastEthernet0/0 | Ethernet0/0 |
| Emperor | FastEthernet0/0 | Ethernet0/0 |
| Kaiser | FastEthernet0/0 | Ethernet0/0 |
| Tsar | FastEthernet0/0 | Ethernet0/0 |
| Tsar | FastEthernet1/0 | Ethernet0/1 |
| Tsar | FastEthernet2/0 | Ethernet0/2 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-bgp-remove-private-as.png)

## Video Solution

[BGP Remove Private AS Video Solution](http://www.youtube.com/watch?v=Z0wkiGxfgsI)
