# BGP Communities No-Advertise

## Scenario

As the owner of a small dutch ISP you like to configure some of the networking stuff yourself. For one of your customers you have to make some changes to the network. They want to advertise their networks to you but you want to prevent this information to be spread to other customers or other parts within your network.

## Goal

* All IP addresses have been preconfigured for you.
* Configure EBGP between AS 1 and AS 2.
* Configure EBGP between AS 2 and AS 3.
* Configure IBGP in AS 2.
* Advertise the loopback0 interface on router Erik in BGP.
* Configure router Rene so it doesn't advertise network 1.1.1.0 /24 to any other BGP neighbor. Use one of the communities to achieve this.

## GNS3 2.2.56.1

Import `BGP Communities No-Advertise IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `BGP Communities No-Advertise.gns3` beside `project-files`.

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
| Bert | FastEthernet0/0 | Ethernet0/0 |
| Erik | FastEthernet0/0 | Ethernet0/0 |
| Frans | FastEthernet0/0 | Ethernet0/0 |
| Rene | FastEthernet0/0 | Ethernet0/0 |
| Rene | FastEthernet1/0 | Ethernet0/1 |
| Rene | FastEthernet2/0 | Ethernet0/2 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-bgp-communities-no-advertise.png)

## Video Solution

[BGP Communities No-Advertise Solution](http://www.youtube.com/watch?v=XPjCSiNxKE0)
