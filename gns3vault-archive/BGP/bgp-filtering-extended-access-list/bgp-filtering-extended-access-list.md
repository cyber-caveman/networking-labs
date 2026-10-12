# BGP Filtering Extended Access-List

## Scenario

Ever since Diablo was defeated Deckard Cain decided to become a network engineer. Two decades have passed and the village of Tristram has upgraded their network for inter-AS connectivity. Recently some security issues have been reported and Deckard asked you to help him to filter some of the prefixes through BGP. Unfortunately the router does not support prefix-lists so you'll have to use access-lists to accomplish this.

## Goal

* All IP addresses have been preconfigured for you.
* Advertise the loopback interfaces on both routers in BGP.
* Configure a summary that advertises 10.0.0.0/8 towards router Sanctuary.
* Configure an extended access-list on router Sanctuary that will block the 10.0.0.0/8 prefix but allows all other prefixes.
* Configure an extended access-list on router Tristram that blocks network 10.2.2.0/24.

## GNS3 2.2.56.1

Import `bgp-filtering-extended-access-list IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `bgp-filtering-extended-access-list.gns3` beside `project-files`.

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
| Tristram | FastEthernet0/0 | Ethernet0/0 |
| Sanctuary | FastEthernet0/0 | Ethernet0/0 |

### Source notes

No source topology or configs were supplied. Reconstructed the two-router link and visible addresses from the diagram; routing remains unconfigured.

The diagram omits loopback addresses. Assumed Tristram 10.1.1.1/24 and Sanctuary 10.2.2.2/24 to supply the prefixes needed by the filtering goals.

No completed solution configs were supplied; none were invented.

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-bgp-filtering-extended-access-list.png)

## Additional Resources
