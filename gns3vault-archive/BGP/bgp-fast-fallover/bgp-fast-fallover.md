# BGP Fast Fallover

## Scenario

Kendrick and Scott are using BGP to exchange routing information. Unfortunately the link that connects both routers isn't that reliable. Everytime it goes down it also tears down the BGP peering...let's see if you can prevent that!

## Goal

- All IP addresses have been preconfigured for you.
- Configure EBGP on router Kendrick and use AS number 1.
- Configure EBGP on router Scott and use AS number 2.
- Ensure that whenever the physical interface fails the BGP peering only drops when the holddown timer expires.

## GNS3 2.2.56.1

Import `BGPFastFallover IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `BGPFastFallover.gns3` beside `project-files`.

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

![Network Topology](./topology-bgp-fast-fallover.png)

## Video Solution

http://www.youtube.com/watch?v=zQKjRrcx8GQ
