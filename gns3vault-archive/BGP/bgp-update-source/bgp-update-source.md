# BGP Update Source

![Network Topology](./topology-bgp-update-source.jpg)

## Scenario

As the senior network engineer of an international fruit-selling company you need to configure IBGP within the network. Since your manager wants no SPOF (single point of failure) you decide to add another link between the routers, now the only thing left to do is make sure the logical configuration is also redundant...back to work!

## Goal

* All IP addresses have been preconfigured for you.
* Both routers have a loopback interface:
  * Router King: L0: 1.1.1.1 /32
  * Router Kong: L0: 2.2.2.2 /32
* Configure EIGRP AS 100 on both routers, advertise all networks.
* Ensure you have full reachability and can ping both loopbacks.
* Configure BGP AS 100 on both routers, do not advertise any networks.
* Make sure that whenever a single link goes down, the BGP neighbor relationship will not reset itself.
* Try this by first shutting down the FastEthernet link, bring it back up and then try the serial link.

## Background

## GNS3 2.2.56.1

Import `bgp-update-source-startup-configs IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `bgp-update-source-startup-configs.gns3` beside `project-files`.

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
| King | FastEthernet0/0 | Ethernet0/0 |
| King | Serial1/0 | Serial4/0 |
| King | Serial1/1 | Serial4/1 |
| King | Serial1/2 | Serial4/2 |
| King | Serial1/3 | Serial4/3 |
| Kong | FastEthernet0/0 | Ethernet0/0 |
| Kong | Serial1/0 | Serial4/0 |
| Kong | Serial1/1 | Serial4/1 |
| Kong | Serial1/2 | Serial4/2 |
| Kong | Serial1/3 | Serial4/3 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

You need to register to be able to download the GNS3 Topology File. (Registration is Free!)

## Video Solution

[View Video Solution on YouTube](http://www.youtube.com/watch?v=kVY8_250Up8)
