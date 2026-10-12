# EBGP - External BGP

## Scenario

Textilalicious is a large international company specialized in selling Wool, Silk, Cotton and Flax. Each region is specialized in selling a different type of textile. To support the growth of the company network your boss has decided to use BGP to connect the different regions together. You just finished studying BGP for your CCNP ROUTE exam so your boss agrees to let you configure this network.

## Goal

- All IP addresses have been preconfigured for you as specified in the topology picture.
- Configure EBGP between AS 1 and AS 2.
- Configure EBGP between AS 2 and AS 3. You are not allowed to use the IP addresses on the physical interfaces to configure the BGP neighbor adjacency.
- Configure EBGP between AS 3 and AS 4.
- Advertise the loopback interfaces in BGP and ensure you have full reachability for this network.

## GNS3 2.2.56.1

Import `EBGP External BGP IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `EBGP External BGP.gns3` beside `project-files`.

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
| Cotton | FastEthernet0/0 | Ethernet0/0 |
| Flax | FastEthernet0/0 | Ethernet0/0 |
| Flax | FastEthernet1/0 | Ethernet0/1 |
| Silk | FastEthernet0/0 | Ethernet0/0 |
| Silk | FastEthernet1/0 | Ethernet0/1 |
| Wool | FastEthernet0/0 | Ethernet0/0 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-ebgp-external-bgp.png)

## Video Solution

http://www.youtube.com/watch?v=D0o-cdhiwjs
