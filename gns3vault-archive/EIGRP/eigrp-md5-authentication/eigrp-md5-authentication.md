# EIGRP MD5 Authentication

![Network Topology](./topology-eigrp-md5-authentication.jpg)

## Scenario

Ben and Jerry are running their business from the north pole and have an icy request for you. They would like you to setup EIGRP (Enhanced Interior Gateway Routing Protocol) and make sure that all network updates are secure by enabling authentication...don't get cold fingers on this one, time to warm up the routers!

## Goal

- All IP addresses have been preconfigured for you.
- Both routers has a loopback0 interface:
  - Ben: 1.1.1.1 /24
  - Jerry: 2.2.2.2 /24
- Configure the correct date and time for both routers. Just configure today's date/time.
- Configure EIGRP AS 12 on both routers, advertise all networks.
- Ensure you have an adjancency and routing information is exchanged.
- Enable MD5 authentication for EIGRP AS 12 with the following parameters:
  - Key Chain: GNS3VAULT
  - Key-ID 1: password chunky
  - Key-ID 2: password monkey
- Key1 should be valid from today until 15 minutes later from the moment you configure it.
- Key2 should be valid from today and will never expire.
- Ensure routing information is still exchanged between both routers.

## GNS3 2.2.56.1

Import `eigrp-md5-authentication-startup-configs IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `eigrp-md5-authentication-startup-configs.gns3` beside `project-files`.

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
| BEN | Serial0/0 | Serial4/0 |
| BEN | Serial0/1 | Serial4/1 |
| BEN | Serial0/2 | Serial4/2 |
| BEN | Serial0/3 | Serial4/3 |
| JERRY | Serial0/0 | Serial4/0 |
| JERRY | Serial0/1 | Serial4/1 |
| JERRY | Serial0/2 | Serial4/2 |
| JERRY | Serial0/3 | Serial4/3 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

## Video Solution

http://www.youtube.com/watch?v=msebqIer_wk
