# RIP to EIGRP redistribution

## Scenario

A famous research company is trying to develop a medicine to increase the capabilities of the brain. They are trying to connect their site to another research center to exchange information but there is some trouble with the redistribution of routing protocols. You as a senior network engineer are able to solve this problem without too much trouble..or do you? Let's see!

## Goal

- All IP addresses have been preconfigured for you as specified in the topology picture.
- Each router has a loopback0 interface.
- Configure EIGRP AS 1 on router Charles, Caesar, Landon and Hunsiker.
- Configure RIP Version 2 on router Rodman, Aranha, Landon and Charles.
- Configured two-way redistribution on router Charles and Landon.
- Achieve full connectivity so you can ping all physical and loopback interfaces.

## Background

## GNS3 2.2.56.1

Import `RIP to EIGRP redistribution IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `RIP to EIGRP redistribution.gns3` beside `project-files`.

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
| Aranha | FastEthernet0/0 | Ethernet0/0 |
| Aranha | FastEthernet1/0 | Ethernet0/1 |
| Caesar | FastEthernet0/0 | Ethernet0/0 |
| Caesar | FastEthernet1/0 | Ethernet0/1 |
| Charles | FastEthernet0/0 | Ethernet0/0 |
| Charles | FastEthernet1/0 | Ethernet0/1 |
| Charles | FastEthernet2/0 | Ethernet0/2 |
| Hunsiker | FastEthernet0/0 | Ethernet0/0 |
| Hunsiker | FastEthernet1/0 | Ethernet0/1 |
| Landon | FastEthernet0/0 | Ethernet0/0 |
| Landon | FastEthernet1/0 | Ethernet0/1 |
| Landon | FastEthernet2/0 | Ethernet0/2 |
| Rodman | FastEthernet0/0 | Ethernet0/0 |
| Rodman | FastEthernet1/0 | Ethernet0/1 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-rip-to-eigrp-redistribution.png)

## Video Solution

[Video Solution on YouTube](http://www.youtube.com/watch?v=LaJwjc0H-ps)
