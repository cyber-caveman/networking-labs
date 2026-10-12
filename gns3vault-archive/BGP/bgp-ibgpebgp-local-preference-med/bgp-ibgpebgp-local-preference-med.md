# BGP IBGP/EBGP Local Preference MED

![Network Topology](./topology-bgp-ibgpebgp-local-preference-med.png)

## Scenario:

You are working for a company specialized in selling vegetables and fruit and responsible for the whole network. To reduce the risk of losing the connection to the Internet you decided to get another link to your ISP. The first link between Cherry and ISP is an expensive link where you have to pay for every megabyte that is transfered, this link should only be used for backup. The second link between Berry and ISP is cheap and up 24/7. All traffic should be sent using this link.

## Goal:

- All IP addresses are preconfigured as specified in the topology picture.
- Every router has a loopback interface:
  - Kerry: Loopback0: 1.1.1.1 /24
  - Cherry: Loopback0: 2.2.2.2 /24
  - Berry: Loopback0: 3.3.3.3 /24
  - ISP: Loopback0: 4.4.4.4 /24
- Configure EIGRP in AS 100.
- Do not advertise the links between AS100 and AS200 in EIGRP.
- Configure IBGP within AS100, the source of BGP updates has to be the loopback interface.
- Configure EBGP between router Cherry and ISP.
- Configure EBGP between router Berry and ISP.
- Advertise the loopback interfaces into BGP, do this on all routers.
- Ensure you have full reachability to all networks.
- Do a traceroute from router ISP to the 1.1.1.0 network. Which path does it take? Do you know why this path was preferred over the other?
- You need to make sure that all traffic for AS100 is being sent using the link between router Berry and ISP. You are only allowed to make changes on router Berry or Cherry. (hint: use MED)
- To conform to the company policy, you need to make sure that all outgoing traffic will be sent using the link between router Berry and ISP. (hint: use Local Preference)
- Optional: change the BGP setup between Cherry and ISP so the BGP updates are sourced from the loopback interfaces.

## GNS3 2.2.56.1

Import `bgp-ibgp-ebgp-lp-med-startup-configs IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `bgp-ibgp-ebgp-lp-med-startup-configs.gns3` beside `project-files`.

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
| Berry | FastEthernet0/0 | Ethernet0/0 |
| Berry | FastEthernet1/0 | Ethernet0/1 |
| Berry | Serial2/0 | Serial4/0 |
| Berry | Serial2/1 | Serial4/1 |
| Berry | Serial2/2 | Serial4/2 |
| Berry | Serial2/3 | Serial4/3 |
| Cherry | FastEthernet0/0 | Ethernet0/0 |
| Cherry | FastEthernet1/0 | Ethernet0/1 |
| Cherry | Serial2/0 | Serial4/0 |
| Cherry | Serial2/1 | Serial4/1 |
| Cherry | Serial2/2 | Serial4/2 |
| Cherry | Serial2/3 | Serial4/3 |
| ISP | Serial0/0 | Serial4/0 |
| ISP | Serial0/1 | Serial4/1 |
| ISP | Serial0/2 | Serial4/2 |
| ISP | Serial0/3 | Serial4/3 |
| Kerry | FastEthernet0/0 | Ethernet0/0 |
| Kerry | FastEthernet1/0 | Ethernet0/1 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology:

## Video Solution:

[YouTube Video](http://www.youtube.com/watch?v=PbjNJK13ZZ8)
