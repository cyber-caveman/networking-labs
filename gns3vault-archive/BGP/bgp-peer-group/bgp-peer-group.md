# BGP Peer Group

## Scenario

Your autonomous system has a lot of IBGP routers. You are already familiar with route reflectors which saves you a lot of trouble configuring all the IBGP neighbor peerings. You just read about BGP peer groups which sounds very interesting. Less CPU overhead and even less configuration for you. Let's see if this will work.

## Goal

- All IP addresses have been preconfigured for you as specified in the topology picture.
- Configure a peer group called "PEERS" on router Bit.
- Router Byte, Octet and Nibble should only form IBGP peerings with router Bit.
- Ensure you have full connectivity within AS 1234.

## GNS3 2.2.56.1

Import `BGP Peer Group IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `BGP Peer Group.gns3` beside `project-files`.

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
| Bit | FastEthernet0/0 | Ethernet0/0 |
| Bit | FastEthernet1/0 | Ethernet0/1 |
| Bit | FastEthernet2/0 | Ethernet0/2 |
| Byte | FastEthernet0/0 | Ethernet0/0 |
| Nibble | FastEthernet0/0 | Ethernet0/0 |
| Octet | FastEthernet0/0 | Ethernet0/0 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-bgp-peer-group.png)

## Video Solution

[http://www.youtube.com/watch?v=qiRlhR_Q1uU](http://www.youtube.com/watch?v=qiRlhR_Q1uU)
