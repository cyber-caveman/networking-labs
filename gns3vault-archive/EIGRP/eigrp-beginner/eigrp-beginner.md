# EIGRP Beginner

![Network Topology](./topology-eigrp-beginner.jpg)

## Scenario

Company XYZ decided to upgrade their network to Cisco only equipment and implement the EIGRP routing protocol. It's up to you to get the job done!

## Goal

- Configure all IP addresses as specified in the topology.
- Create 3 loopback interfaces:
  - Router X: 172.16.1.0 /24
  - Router Y: 172.16.2.0 /24
  - Router Z: 172.16.3.0 /24
- Configure EIGRP on all routers, use AS number 100. Achieve full connectivity
- You notice that when you start a ping from router Y's loopback to the loopback of router X that this is not possible, you need to fix the problem.
- Change the bandwidth so traffic from router Z to router Y's loopback interface uses the link between X and Z.
- Change the EIGRP configuration on all routers so load and reliability are also used as metrics.
- RouterX: create a summary towards Router Y and Z for the 172.16.1.0 /24 network. It should appear as 172.16.0.0 /16.
- Configure EIGRP authentication on all routers:
  - Key-Chain: XYZ
  - Key-ID: 1
  - Password: vault
- Create key-ID 2 in the XYZ key-chain and configure a accept and send-lifetime.
  - Key-ID 1: valid from 1 June 2010 till 14 June 2010.
  - Key-ID 2: valid from 14 June 2010 till 28 June 2010.

## GNS3 2.2.56.1

Import `eigrp-beginner-startup-configs IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `eigrp-beginner-startup-configs.gns3` beside `project-files`.

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
| X | FastEthernet0/0 | Ethernet0/0 |
| X | FastEthernet1/0 | Ethernet0/1 |
| Y | FastEthernet0/0 | Ethernet0/0 |
| Y | FastEthernet1/0 | Ethernet0/1 |
| Z | FastEthernet0/0 | Ethernet0/0 |
| Z | FastEthernet1/0 | Ethernet0/1 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

## Video Solution

[Video Solution on YouTube](http://www.youtube.com/watch?v=aadOWeM0gb0)
