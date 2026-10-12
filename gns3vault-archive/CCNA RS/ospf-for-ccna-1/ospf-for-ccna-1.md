# OSPF CCNA 1

## Scenario

During the day you are working as a junior network engineer studying CCNA. During the night you are active as a respectable fighter and many of your matches are recorded on video. Some of your fans have requested your videos and you want to make sure you can deliver them over the network. You are going to configure OSPF for full connectivity...keep your fans happy, deliver the videos and study for CCNA at the same time! See if you can fight your way through this one...

## Goal

* All IPv4 addresses have been preconfigured for you.
* Each router has a loopback0 interface.
* Configure OSPF area 0 on router Durden, Paulson and Chesler. Advertise the loopback0 interfaces and make sure you have connectivity.
* Configure OSPF area 1 on router Singer, Bird and Dent. Advertise the loopback0 interfaces.
* You should now have full connectivity for your OSPF network. Make sure you can ping all interfaces including the loopback0 interfaces.
* Change the router ID of router Singer to 44.44.44.44. Make sure you can see the change by using the appropriate show command.
* Question: which router is the DR (Designated Router) and BDR (Backup Designated Router) that is connected to SW2? Can you explain why?
* Change the network so router Chesler will be the DR. Test this by resetting OSPF and using the appropriate show command.
* Enable MD5 authentication on the serial link between router Bird and Dent.
* Enable plaintext authentication on the fastethernet link between router Bird and Dent.
* Make sure all routers in area 0 send a hello packet every 4 seconds. If they don't hear anything from their neighbor after 17 seconds they should drop the neighbor adjacency.
* Advertise a default route on router Durden in OSPF. Test this by checking reachability of its loopback1 interfaces from other routers. Do not advertise the loopback1 interface in OSPF.
* Configure router Dent so it will load-balance over the serial and fastethernet link for all networks.

## GNS3 2.2.56.1

Import [ospf-ccna-1-startup-configs IOU.gns3project](ospf-ccna-1-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `ospf-ccna-1-startup-configs.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Bird | FastEthernet0/0 | Ethernet0/0 |
| Bird | FastEthernet2/0 | Ethernet0/1 |
| Bird | Serial1/0 | Serial4/0 |
| Bird | Serial1/1 | Serial4/1 |
| Bird | Serial1/2 | Serial4/2 |
| Bird | Serial1/3 | Serial4/3 |
| Chesler | FastEthernet0/0 | Ethernet0/0 |
| Chesler | FastEthernet1/0 | Ethernet0/1 |
| Dent | FastEthernet0/0 | Ethernet0/0 |
| Dent | Serial1/0 | Serial4/0 |
| Dent | Serial1/1 | Serial4/1 |
| Dent | Serial1/2 | Serial4/2 |
| Dent | Serial1/3 | Serial4/3 |
| Durden | FastEthernet0/0 | Ethernet0/0 |
| Paulson | FastEthernet0/0 | Ethernet0/0 |
| Singer | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-ospf-for-ccna-1.png)

## Video Solution

http://www.youtube.com/watch?v=Yzh9vh_xdFY
