# EIGRP Summarization Leak-Map

## Scenario

The movie industry is dominated by Holly- and Bollywood. Recently the two companies are creating movies together and using a shared network infrastructure. To make sure the routing tables of the EIGRP routes don't grow too much you decide to implement summarization. This has a unwanted side-effect however since now the serial-link is used to reach some networks.

## Goal

- All IP addresses have been preconfigured for you.
- Configure EIGRP on both routers and advertise everything. Activate it on both interfaces.
- Create a summary advertising a default route on router Bollywood using the FastEthernet 0/0 interface.
- Ensure router Hollywood doesn't use the serial link to reach network 2.2.2.0 /24. You are not allowed to create any static routes.

## GNS3 2.2.56.1

Import `EIGRP Summarization Leak-Map IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `EIGRP Summarization Leak-Map.gns3` beside `project-files`.

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
| Bollywood | FastEthernet0/0 | Ethernet0/0 |
| Bollywood | Serial1/0 | Serial4/0 |
| Bollywood | Serial1/1 | Serial4/1 |
| Bollywood | Serial1/2 | Serial4/2 |
| Bollywood | Serial1/3 | Serial4/3 |
| Hollywood | FastEthernet0/0 | Ethernet0/0 |
| Hollywood | Serial1/0 | Serial4/0 |
| Hollywood | Serial1/1 | Serial4/1 |
| Hollywood | Serial1/2 | Serial4/2 |
| Hollywood | Serial1/3 | Serial4/3 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-eigrp-summarization-leak-map.png)

## Video Solution

- [Watch on YouTube](http://www.youtube.com/watch?v=QLJqR4klOfc)
