# EIGRP IP Default Network

## Scenario

As the network engineer for your Cisco-only network you run into a strange problem. Some of the routers have been replaced and have empty configs and per configuration template you need to configure EIGRP IP Default Network. Some of the older routers still run IGRP and are unable to advertise default routes, in order to keep all configs on routers the same you are forced to use the older "IP Default Network command". One of your colleagues still has an output from an old "show ip route" command which will show you what you need to achieve.

## Goal

- All IP addresses have been preconfigured for you.
- Configure EIGRP AS12 as following:
  - Do not disable auto-summarization.
  - Advertise network 172.23.23.0 /24
  - Advertise network 10.12.12.0 /24
  - Do not use any other network commands.
- You have completed this lab when you see the following when you type "show ip route" on router Erik:

**Gateway of last resort is 10.12.12.2 to network 172.33.0.0**

---

## GNS3 2.2.56.1

Import `eigrp-default-network-startup-configs IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `eigrp-default-network-startup-configs.gns3` beside `project-files`.

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
| Erik | FastEthernet0/0 | Ethernet0/0 |
| Lisanne | FastEthernet1/0 | Ethernet0/0 |
| Lisanne | Serial0/0 | Serial4/0 |
| Lisanne | Serial0/1 | Serial4/1 |
| Lisanne | Serial0/2 | Serial4/2 |
| Lisanne | Serial0/3 | Serial4/3 |
| Jan | Serial0/0 | Serial4/0 |
| Jan | Serial0/1 | Serial4/1 |
| Jan | Serial0/2 | Serial4/2 |
| Jan | Serial0/3 | Serial4/3 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-eigrp-ip-default-network.png)

## Video Solution

[Watch on YouTube](http://www.youtube.com/watch?v=5ldJuSs7PlY)
