# EIGRP Stub

![Network Topology](./topology-eigrp-stub.png)

## Scenario:

A major soccer team in the UK is running EIGRP on their internal network. One of your colleague network engineers noticed that there are quite some EIGRP routers sending query packets and sometimes routers get stuck-in-active. Since you are an expert on EIGRP you'll have to configure the network using the EIGRP stub feature to make sure things work smoother...good luck!

## Goal:

- All IP addresses have been preconfigured as specified in the topology picture.
- Each router has a loopback0 interface.
- Use EIGRP AS 1 to configure on your routers.
- Configure router Thomas so it receives EIGRP routes but doesn't advertise anything.
- Configure router Harry so it only receives EIGRP routes and only advertises directly connected networks in EIGRP.
- Configure router Alfie so it only receives EIGRP routes and only advertises summary route 4.4.0.0 /16 in EIGRP.
- Configure router Jack so it only receives EIGRP routes and only advertises static routes.

## GNS3 2.2.56.1

Import `EIGRP Stub IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `EIGRP Stub.gns3` beside `project-files`.

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
| Alfie | FastEthernet0/0 | Ethernet0/0 |
| Charlie | FastEthernet0/0 | Ethernet0/0 |
| Harry | FastEthernet0/0 | Ethernet0/0 |
| Harry | FastEthernet1/0 | Ethernet0/1 |
| Jack | FastEthernet0/0 | Ethernet0/0 |
| Oliver | FastEthernet0/0 | Ethernet0/0 |
| Oliver | FastEthernet1/0 | Ethernet0/1 |
| Oliver | FastEthernet2/0 | Ethernet0/2 |
| Oliver | FastEthernet3/0 | Ethernet0/3 |
| Thomas | FastEthernet0/0 | Ethernet0/0 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology:

## Video Solution:

[Video Solution on YouTube](http://www.youtube.com/watch?v=ZMryQNCkOIY)
