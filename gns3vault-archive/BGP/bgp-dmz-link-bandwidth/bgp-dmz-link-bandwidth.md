# BGP DMZ Link Bandwidth

## Scenario

You work for a greek ISP where you are known as "The Greek Wonder". You solve routing problems faster than Zeus could shoot lightning bolts. One part of the network uses BGP and there are multiple links between AS 1 and AS 2. Not all links have the same bandwidth but you would like to use all of them. You just read about the Link Bandwidth feature for BGP and you are looking forward to implementing it.

## Goal

- All IP addresses have been preconfigured for you.
- Configure IBGP within AS 1. Use the loopback0 interfaces to source the BGP updates from.
- Configure IBGP within AS 2. Use the loopback0 interfaces to source the BGP updates from.
- Configure EBGP between AS 1 and AS 2.
- Ensure traffic from router Athens is load balanced proportionally over all available links.

## GNS3 2.2.56.1

Import `BGP DMZ Link Bandwidth IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `BGP DMZ Link Bandwidth.gns3` beside `project-files`.

Routers use the preferred IOU L3 image `x86_64_crb_linux-adventerprisek9-ms.bin`
(MD5 `4a2fce8de21d1831fbceffd155e41ae7`), template
`b3b10b90-adfb-43f8-b289-b68bcf322ad8`, 768 MB RAM, 512 KB NVRAM,
four Ethernet and four serial adapters, with automatically allocated consoles.
Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Physical interface names and link endpoints are updated together in startup and
all supplied final configs. Original bandwidth and delay are explicit where
needed to preserve EIGRP/IGP metric inputs. Source protocol settings and intended
startup state are preserved; final configs are not loaded at startup.

Unmanaged Ethernet switches retain their original type and VLAN settings.

| Router | Original interface | IOU interface |
| --- | --- | --- |
| Athens | FastEthernet0/0 | Ethernet0/0 |
| Delphi | FastEthernet0/0 | Ethernet0/0 |
| Delphi | Ethernet1/0 | Ethernet0/1 |
| Delphi | Ethernet1/1 | Ethernet0/2 |
| Delphi | Ethernet1/2 | Ethernet0/3 |
| Delphi | Ethernet1/3 | Ethernet1/0 |
| Olympia | FastEthernet0/0 | Ethernet0/0 |
| Olympia | FastEthernet1/0 | Ethernet0/1 |
| Sparta | FastEthernet0/0 | Ethernet0/0 |
| Sparta | FastEthernet1/0 | Ethernet0/1 |
| Sparta | Serial2/0 | Serial4/0 |
| Sparta | Serial2/1 | Serial4/1 |
| Sparta | Serial2/2 | Serial4/2 |
| Sparta | Serial2/3 | Serial4/3 |
| Thebes | Ethernet1/0 | Ethernet0/0 |
| Thebes | Ethernet1/1 | Ethernet0/1 |
| Thebes | Ethernet1/2 | Ethernet0/2 |
| Thebes | Ethernet1/3 | Ethernet0/3 |
| Thebes | FastEthernet2/0 | Ethernet1/0 |
| Thebes | Serial0/0 | Serial4/0 |
| Thebes | Serial0/1 | Serial4/1 |
| Thebes | Serial0/2 | Serial4/2 |
| Thebes | Serial0/3 | Serial4/3 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-bgp-dmz-link-bandwidth.png)

## Video Solution

[Video Solution on YouTube](http://www.youtube.com/watch?v=fsrANHom7zo)
