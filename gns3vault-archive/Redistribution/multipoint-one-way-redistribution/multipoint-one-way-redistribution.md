# Multipoint One-Way Redistribution

Your local neighborhood pet shop has asked you to help them solve some network problems. The pet shop is running OSPF and recently bought another shop that is running EIGRP. To achieve connectivity they use redistribution but now some users are complaining about unreachable networks and the slowness of the network. Someone at the pet shop tried one-way redistribution but had trouble with non-optimal paths. They decided to configure multipoint one-way redistribution but this also introduced the problem of flapping networks...think you can solve it?

## Goal

* All IP addresses have been preconfigured for you.
* Configure OSPF on router Ace and Aggie and only advertise network 192.168.12.0 /24.
* Configure EIGRP AS 1 on router Ace, Aggie and Abu. Only advertise network 192.168.13.0 /24 and 192.168.23.0 /24.
* Redistribute the loopback0 interface in EIGRP AS 1 on router Abu.
* Redistribute EIGRP information into OSPF on router Ace and Aggie.
* Check router Ace and Aggie for possible redistribution problems and solve the problem.

## GNS3 2.2.56.1

Import `Multipoint One-Way Redistribution IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `Multipoint One-Way Redistribution.gns3` beside `project-files`.

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
| Abu | FastEthernet0/0 | Ethernet0/0 |
| Abu | FastEthernet1/0 | Ethernet0/1 |
| Ace | FastEthernet0/0 | Ethernet0/0 |
| Ace | FastEthernet1/0 | Ethernet0/1 |
| Aggie | FastEthernet0/0 | Ethernet0/0 |
| Aggie | FastEthernet1/0 | Ethernet0/1 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-multipoint-one-way-redistribution.png)

## Video Solution

http://www.youtube.com/watch?v=zMozo8uLmzs
