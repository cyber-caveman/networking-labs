# BGP Conditional Advertisement

## Scenario

An international toy store company needs your help. They use BGP to exchange routing information between their sites but everytime one of their IBGP routers fails they have connectivity issues. Let's see if you can help them out!

## Goal

* All IP addresses have been preconfigured for you.
* Configure EBGP between AS 1 and AS 2.
* Configure EBGP between AS 2 and AS 3.
* Configure router Pegasus to advertise network 2.2.2.0 /24 in BGP.
* Configure router Phoenix to advertise network 1.1.1.0 /24 in BGP.
* Configure router Pegasus so it does no longer advertise network 2.2.2.0 /24 when network 1.1.1.0 /24 is no longer reachable.

## GNS3 2.2.56.1

Import `BGP Conditional Advertisement IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `BGP Conditional Advertisement.gns3` beside `project-files`.

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
| Pegasus | FastEthernet0/0 | Ethernet0/0 |
| Pegasus | FastEthernet1/0 | Ethernet0/1 |
| Phoenix | FastEthernet0/0 | Ethernet0/0 |
| Pixie | FastEthernet0/0 | Ethernet0/0 |

### Source notes

No completed solution configs were supplied; none were invented.

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-bgp-conditional-advertisement.png)

## Video Solution

http://www.youtube.com/watch?v=lqpTUHu3j9o
