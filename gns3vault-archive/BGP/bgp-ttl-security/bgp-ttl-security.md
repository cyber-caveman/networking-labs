# BGP TTL Security

## Scenario

After years of plumbing work you switched your career to become a network engineer. Besides being good at routing & switching you are very security-minded. One of your routers is connected to your brother's network and you use BGP to exchange routing information. You want to make sure hackers are unable to spoof the BGP peering in any way.

## Goal

- All IP addresses have been preconfigured for you.
- Configure EBGP between router Mario and Luigi.
- Ensure router Bowser can't spoof BGP packets by changing the TTL on router Mario for BGP.

## GNS3 2.2.56.1

Import `BGP TTL Security IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `BGP TTL Security.gns3` beside `project-files`.

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
| Bowser | FastEthernet0/0 | Ethernet0/0 |
| Luigi | FastEthernet0/0 | Ethernet0/0 |
| Luigi | FastEthernet1/0 | Ethernet0/1 |
| Mario | FastEthernet0/0 | Ethernet0/0 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-bgp-ttl-security.png)

## Video Solution

http://www.youtube.com/watch?v=YiuzLFEQZY4
