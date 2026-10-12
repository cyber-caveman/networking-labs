# EIGRP Summarization

![Network Topology](./topology-eigrp-summarization.jpg)

## Scenario

The owner of this network has been complaining about performance issues for awhile. You as the junior network engineer have just learned about summarization and the possible advantages this might bring to your network. It's up to you to bring summarize the networks and bring the glory back to the routers...

## Goal

- All IP addresses have been preconfigured for you.
- EIGRP AS123 has been preconfigured for you and is advertising all networks.
- There are plenty of loopbacks with IP addresses configurated for you to summarize.
- You are not allowed to use EIGRP auto-summarization.
- Ensure router Cole and Santiago only have a single 172.16.0.0 /21 entry in their routing table.
- Ensure router Fenix will send traffic for 3.3.3.3 towards router Santiago. Do not change the Administrative Distance or Metric(s) to achieve this.
- Ensure router Fenix only sees 2 entries for the 10.0.0.0 network range. 10.0.0.0 /22 and 10.0.4.0 /22.
- Further summarize the 10.0.0.0 /22 and 10.0.4.0 /22 network so router Fenix and Cole only see the 10.0.0.0 /19 entry in their routing table.
- Advertise a default route on router Cole towards router Fenix, you are not allowed to use the default-network command.

## GNS3 2.2.56.1

Import `eigrp-summarization-startup-configs IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `eigrp-summarization-startup-configs.gns3` beside `project-files`.

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
| FENIX | FastEthernet0/0 | Ethernet0/0 |
| FENIX | FastEthernet1/0 | Ethernet0/1 |
| SANTIAGO | FastEthernet0/0 | Ethernet0/0 |
| SANTIAGO | FastEthernet1/0 | Ethernet0/1 |
| COLE | FastEthernet0/0 | Ethernet0/0 |
| COLE | FastEthernet1/0 | Ethernet0/1 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

## Video Solution

[EIGRP Summarization Video Solution](http://www.youtube.com/watch?v=2LQ8iamyJ4w)
