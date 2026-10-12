# BGP Transit AS

## Scenario

Tillywood is one of the major movie studios located in Tilburg, The Netherlands. You are working there as a junior network engineer and assigned at the BGP team. One of the trainees has configured part of the network which has a transit AS but he has trouble sending packets between AS 1 and AS 3. Can you show him how it's done?

## Goal

- All IP addresses have been preconfigured for you as specified in the topology picture.
- Configure EBGP between AS 1 and AS 2.
- Configure EBGP between AS 2 and AS 3.
- Configure IBGP within AS 2.
- Ensure AS 1 and AS 3 can reach each others loopback interfaces.

## GNS3 2.2.56.1

Import `BGP Transit AS IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `BGP Transit AS.gns3` beside `project-files`.

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
| Aniston | FastEthernet0/0 | Ethernet0/0 |
| Aniston | FastEthernet1/0 | Ethernet0/1 |
| Bullock | FastEthernet0/0 | Ethernet0/0 |
| Diaz | FastEthernet0/0 | Ethernet0/0 |
| Diaz | FastEthernet1/0 | Ethernet0/1 |
| Parker | FastEthernet0/0 | Ethernet0/0 |
| Parker | FastEthernet1/0 | Ethernet0/1 |
| Parker | FastEthernet2/0 | Ethernet0/2 |
| Roberts | FastEthernet0/0 | Ethernet0/0 |
| Witherspoon | FastEthernet0/0 | Ethernet0/0 |
| Witherspoon | FastEthernet1/0 | Ethernet0/1 |
| Witherspoon | FastEthernet2/0 | Ethernet0/2 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-bgp-transit-as.png)

## Video Solution

http://www.youtube.com/watch?v=kSsEDpd40uI
