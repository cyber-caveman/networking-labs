# BGP Soft Reconfiguration

## Scenario

You are a network engineer responsible for the network for a local fighting tournament. Two of the fighters exchange tactics using BGP to advertise the networks. They don't want to exchange everything they know so they are a number of inbound route filters. You want to make sure the new filters are applied without resetting the BGP peering...get over here!

## Goal

- All IP addresses have been preconfigured for you.
- Configure EBGP between AS1 and AS2.
- Advertise network 2.2.2.0 /24 on router Scorpion in BGP.
- Configure a prefix-list on router SubZero that filters network 2.2.2.0 /24 and apply it to neighbor router Scorpion.
- Ensure the changes are visible without resetting the BGP peering.

## GNS3 2.2.56.1

Import `BGP Soft Reconfiguration IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `BGP Soft Reconfiguration.gns3` beside `project-files`.

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
| Scorpion | FastEthernet0/0 | Ethernet0/0 |
| SubZero | FastEthernet0/0 | Ethernet0/0 |

### Source notes

No source startups were supplied. Recovered addressing from final configs, enabled the initial connected links and left routing/policies unconfigured for the exercise.

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-bgp-soft-reconfiguration.png)

## Video Solution

[BGP Soft Reconfiguration Video Solution](http://www.youtube.com/watch?v=OfsDApMIfhA)
