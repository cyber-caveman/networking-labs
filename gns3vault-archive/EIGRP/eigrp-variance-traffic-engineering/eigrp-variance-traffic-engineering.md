# EIGRP Variance Traffic Engineering

![Network Topology](./topology-eigrp-variance-traffic-engineering.jpg)

## Scenario

You are the senior network engineer for a company specialized in 80's pop-music. The network is experiencing congestion and you want to use one of the WAN links to share the bandwidth so the load on the main Fast Ethernet link will decrease....let's boogy!

## Goal

- All IP addresses have been preconfigured as specified in the topology picture.
- Configure EIGRP on all routers, disable auto-summary. Achieve full connectivity.
- Change the EIGRP metrics so only delay is being used for the calculations.
- Change the delay on every interface (including the loopback) to 300usec
- If you send a ping from router Jermaine to the loopback of router Michael it should use the link to router Jackie. (succesor route)
- Change the delays on the routers so the link between Jermaine and Tito becomes a feasible succesor route to reach the loopback.
- Change the delays so traffic will be sent in a 1:5 ratio. Use the "show ip route 3.3.3.0" command to check this.

## Additional Resources

## GNS3 2.2.56.1

Import `eigrp-variance-te-startup-configs IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `eigrp-variance-te-startup-configs.gns3` beside `project-files`.

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
| Jackie | FastEthernet0/0 | Ethernet0/0 |
| Jackie | FastEthernet1/0 | Ethernet0/1 |
| Jackie | FastEthernet2/0 | Ethernet0/2 |
| Jermaine | FastEthernet0/0 | Ethernet0/0 |
| Jermaine | FastEthernet1/0 | Ethernet0/1 |
| Marlon | FastEthernet0/0 | Ethernet0/0 |
| Marlon | Serial1/0 | Serial4/0 |
| Marlon | Serial1/1 | Serial4/1 |
| Marlon | Serial1/2 | Serial4/2 |
| Marlon | Serial1/3 | Serial4/3 |
| Michael | FastEthernet0/0 | Ethernet0/0 |
| Tito | FastEthernet0/0 | Ethernet0/0 |
| Tito | Serial1/0 | Serial4/0 |
| Tito | Serial1/1 | Serial4/1 |
| Tito | Serial1/2 | Serial4/2 |
| Tito | Serial1/3 | Serial4/3 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

## Video Solution

http://www.youtube.com/watch?v=SJ-HzMR6tV8
