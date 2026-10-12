# BGP AS Path Access List

## Scenario

Sugar Cane company is an international company that is growing at a rapid rate. To connect all the different sites, BGP is used. The security officer, however, doesn't want all the sites to have full connectivity and wants you to create some filters based on AS paths.

## Goal

* All IP addresses have been preconfigured for you.
* Configure EBGP between all routers.
* You are only allowed to use AS Path Access-Lists to complete the following tasks.
* Advertise the loopback0 and loopback1 interface on all routers in BGP.
* Ensure AS1 does not become a transit AS.
* Configure router Bakers so it doesn't advertise any prefixes from AS 2 towards AS 4.
* Configure AS4 so it doesn't accept any prefixes originated by AS 1.

## About This Lab

## GNS3 2.2.56.1

Import `BGP AS Path Access List IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `BGP AS Path Access List.gns3` beside `project-files`.

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
| Bakers | FastEthernet0/0 | Ethernet0/0 |
| Bakers | FastEthernet1/0 | Ethernet0/1 |
| Barbados | FastEthernet0/0 | Ethernet0/0 |
| Barbados | FastEthernet1/0 | Ethernet0/1 |
| Castor | FastEthernet0/0 | Ethernet0/0 |
| Castor | FastEthernet1/0 | Ethernet0/1 |
| Coarse | FastEthernet0/0 | Ethernet0/0 |
| Coarse | FastEthernet1/0 | Ethernet0/1 |

### Source notes

No completed solution configs were supplied; none were invented.

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-bgp-as-path-access-list.png)
