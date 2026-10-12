# BGP Attribute Local Preference

## Scenario

You work as a network engineer for a laboratory in San Francisco which is specialized in genetic engineering. To exchange research information with other laboratories and universities you have built a network using BGP. At this moment you have not configured any path selection for BGP and you want to make sure you have a little more control to influence your routing. Local preference is one of the BGP attributes that you are going to use to fix this.

## Goal

- All IP addresses have been preconfigured for you as specified in the topology picture.
- Configure IBGP within AS 1.
- Configure EBGP between router Franklin and Jacobs.
- Configure EBGP between router Jacobs and Pinto.
- Configure EBGP between router Pinto and Franco.
- Configure EBGP between router Hunisker and Franco.
- Advertise all networks from AS1, AS2, AS3 and AS4 in BGP.
- Ensure AS1 can reach any network in AS2, AS3 or AS4.
- You are only allowed to use the local preference attribute for the upcoming tasks.
- Configure router Franklin so all networks learned through EBGP have a local preference of 500.
- Configure router Hunisker so network 6.6.6.0/24 has a local preference of 600.
- Configure router Hunisker so all networks from AS 4 have a local preference of 700.
- Configure router Hunisker so network 66.66.66.0/24 has a local preference of 800, you are not allowed to use an access-list.

## GNS3 2.2.56.1

Import `bgp-attribute-local-preference IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `bgp-attribute-local-preference.gns3` beside `project-files`.

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
| Landon | FastEthernet0/0 | Ethernet0/0 |
| Landon | FastEthernet1/0 | Ethernet0/1 |
| Hunisker | FastEthernet0/0 | Ethernet0/0 |
| Hunisker | FastEthernet1/0 | Ethernet0/1 |
| Hunisker | FastEthernet2/0 | Ethernet0/2 |
| Rodman | FastEthernet0/0 | Ethernet0/0 |
| Rodman | FastEthernet1/0 | Ethernet0/1 |
| Franklin | FastEthernet0/0 | Ethernet0/0 |
| Franklin | FastEthernet1/0 | Ethernet0/1 |
| Franklin | FastEthernet2/0 | Ethernet0/2 |
| Franco | FastEthernet0/0 | Ethernet0/0 |
| Franco | FastEthernet1/0 | Ethernet0/1 |
| Jacobs | FastEthernet0/0 | Ethernet0/0 |
| Jacobs | FastEthernet1/0 | Ethernet0/1 |
| Pinto | FastEthernet0/0 | Ethernet0/0 |
| Pinto | FastEthernet1/0 | Ethernet0/1 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-bgp-attribute-local-preference.png)

## Video Solution

http://www.youtube.com/watch?v=sR27p8dpeGI
