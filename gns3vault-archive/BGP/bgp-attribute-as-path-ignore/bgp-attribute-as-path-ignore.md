# BGP Attribute AS Path Ignore

## Scenario

You are responsible for an International network. All routers are connected through BGP. One of the network administrators in NewDelhi has configured AS Path prepending for their AS so Paris will send all traffic through Sydney. You heard about a hidden option to ignore AS Path information, maybe this is just what you need...

## Goal

- All IP addresses have been preconfigured for you as specified in the topology picture.
- Configure EBGP between all the ASes.
- Advertise the loopback0 interface on router Barcelona in BGP.
- Router Paris should have two paths to reach network 1.1.1.0/24.
- Configure AS Path prepending on router NewDelhi so router Paris sends all traffic to network 1.1.1.0/24 through router Sydney.
- Configure router Paris to ignore the added ASes so it will send traffic for network 1.1.1.0/24 to router NewDelhi. Don't use any of the other BGP attributes.

## Background

## GNS3 2.2.56.1

Import `BGP Attribute AS-Path Ignore IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `BGP Attribute AS-Path Ignore.gns3` beside `project-files`.

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
| Barcelona | FastEthernet0/0 | Ethernet0/0 |
| Barcelona | FastEthernet1/0 | Ethernet0/1 |
| NewDelhi | FastEthernet0/0 | Ethernet0/0 |
| NewDelhi | FastEthernet1/0 | Ethernet0/1 |
| Paris | FastEthernet0/0 | Ethernet0/0 |
| Paris | FastEthernet1/0 | Ethernet0/1 |
| Sydney | FastEthernet0/0 | Ethernet0/0 |
| Sydney | FastEthernet1/0 | Ethernet0/1 |

### Source notes

The supplied .gns3 described an unrelated Bit/Byte star. Reconstructed the Barcelona/NewDelhi/Paris/Sydney diamond and interface addresses from the diagram, with Barcelona Loopback0 1.1.1.1/24 from the goal. BGP remains unconfigured.

No completed solution configs were supplied; none were invented.

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-bgp-attribute-as-path-ignore.png)
