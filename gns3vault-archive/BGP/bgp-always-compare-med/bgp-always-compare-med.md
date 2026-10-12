# BGP Always compare MED

![Network Topology](./topology-bgp-always-compare-med.jpg)

## Scenario

You are the senior networking engineer working for a huge comic book provider. Your network (AS 100) is connected to 2 different service providers and normally all traffic is being sent to your main ISP which is AS 300. However there is a certain network that is being sent to AS 200 which is your backup ISP. All traffic should be sent towards AS300, is this a cheap trick from your backup ISP to make more money? Or is there something else going on? Time for justice!

## Goal

* All IP addresses are preconfigured as specified in the topology picture.
* Configure EBGP between AS 100 and AS 200.
* Configure EBGP between AS 100 and AS 300, make sure you have a neighbor relationship between router Spiderman and Superman as well as between router Spiderman and Ironman.
* Configure IBGP within AS 300.
* Make sure all neighbor relationships are working, advertise the correct networks in BGP to achieve full connectivity.
* Router Batman AND Superman have the same IP address on the loopback1 interface, advertise this in BGP on both routers.
* Ensure you can ping the 1.2.3.4 address from router Spiderman.
* Take a look at the BGP table with `show ip bgp` on router Spiderman.
* Which path is being used for the 1.2.3.4 network?
* Configure router Ironman and Superman so they send a MED of 50 for the 1.2.3.4 network towards router Spiderman.
* Configure router Batman so it sends a MED of 150 for the 1.2.3.4 network towards router Spiderman.
* Check router Spiderman with `show ip bgp` to see the changes you just made, if not do a `clear ip bgp *`
* Even though the MED from AS 300 is better, why is traffic towards 1.2.3.4 still being sent towards AS 200?
* Configure router Spiderman so traffic towards 1.2.3.4 is sent towards AS 300, the only attribute you are allowed to change is MED.

## GNS3 2.2.56.1

Import `bgp-always-compare-med-startup-configs IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `bgp-always-compare-med-startup-configs.gns3` beside `project-files`.

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
| Batman | FastEthernet0/0 | Ethernet0/0 |
| Batman | FastEthernet1/0 | Ethernet0/1 |
| Ironman | FastEthernet0/0 | Ethernet0/0 |
| Ironman | FastEthernet1/0 | Ethernet0/1 |
| Spiderman | FastEthernet0/0 | Ethernet0/0 |
| Spiderman | FastEthernet1/0 | Ethernet0/1 |
| Spiderman | FastEthernet2/0 | Ethernet0/2 |
| Superman | FastEthernet0/0 | Ethernet0/0 |
| Superman | FastEthernet1/0 | Ethernet0/1 |
| Superman | FastEthernet2/0 | Ethernet0/2 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

## Video Solution

http://www.youtube.com/watch?v=W07g1ktHGl4
