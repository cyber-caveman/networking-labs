# BGP Filtering Maximum Prefix

![Network Topology](./topology-bgp-filtering-maximum-prefix.png)

## Scenario:

The national hedgehog protection foundation needs your help with their network. They are using BGP for their International networking but the router they are using is a bit old and doesn't take many prefixes in its BGP table. You want to ensure there is a maximum number of prefixes your router will accept.

## Goal:

* All IP addresses have been preconfigured for you.
* Configure EBGP between router Sonic and Tails.
* Configure router Sonic so it will remove the BGP neighbor adjacency when it learns more than 8 prefixes.
* Configure router Sonic so it gives a warning once it receives 6 prefixes.
* After the BGP neighbor adjacency has been removed it should retry creating the BGP adjacency in 2 minutes.
* Configure router Tails so it will generate a warning when it receives 4 prefixes but it should never remove the BGP neighbor adjacency.

## Additional Resources

## GNS3 2.2.56.1

Import `bgp-filtering-maximum-prefix IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `bgp-filtering-maximum-prefix.gns3` beside `project-files`.

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
| Sonic | FastEthernet0/0 | Ethernet0/0 |
| Tails | FastEthernet0/0 | Ethernet0/0 |
| Tails | FastEthernet1/0 | Ethernet0/1 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology:

## Video Solution:

* [YouTube Video Solution](http://www.youtube.com/watch?v=SOMYjacgWOc)
