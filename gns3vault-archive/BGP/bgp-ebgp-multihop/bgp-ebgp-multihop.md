# BGP EBGP Multihop

![Network Topology](./topology-bgp-ebgp-multihop.jpg)

## Scenario

You are the junior network engineer for the biggest company in the world selling Arcade Games. You need to establish a BGP link with the service provider. In the future they will add another physical link for redundancy, so the provider wants you to setup the EBGP link between the loopback adapters for logical redundancy...time for some practice!

## Goal

- All IP addresses have been preconfigured for you as specified in the topology picture.
- Both routers have a loopback interface:
  - Router Ping: L0: 1.1.1.1 /32
  - Router Pong: L0: 2.2.2.2 /32
- Configure static routes on both sides pointing to each others loopback.
- Ensure you have full reachability and can ping both loopbacks.
- Router Ping: configure BGP AS 100
- Router Pong: configure BGP AS 200
- Establish a BGP neighbor relationship between the 2 routers. You need to source the BGP updates from the loopback interfaces.
- Ensure you have a BGP neighbor relationship, use the "show ip bgp summary" command to confirm this.

## Additional Information

## GNS3 2.2.56.1

Import `bgp-ebgp-multihop-startup-configs IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `bgp-ebgp-multihop-startup-configs.gns3` beside `project-files`.

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
| Ping | FastEthernet0/0 | Ethernet0/0 |
| Pong | FastEthernet0/0 | Ethernet0/0 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

## Video Solution

[YouTube - BGP EBGP Multihop Solution](http://www.youtube.com/watch?v=kMum9IrIpdw)
