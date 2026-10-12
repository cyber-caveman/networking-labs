# MPLS Traffic Engineering per L2TPV3

![Network Topology](./topology-mpls-traffic-engineering-per-l2tpv3.png)

## Scenario

You are the senior network engineer for a large MPLS provider based in the United Kingdom. 2 of your customers called "Toy" and "Arcade" would like to use your MPLS services to connect their HQ and branch offices. Your MPLS backbone has multiple routers and one of the problems you encounter is that there is no load-sharing within the MPLS cloud. Your customers are connecting the sites using pseudowires and this is something you don't want to change. Make sure your customers can use pseudowires and that you can use load balancing within your MPLS backbone. See if you can tag this one...

## Goal

All IP addresses have been preconfigured for you.

- Every router has a loopback0 interfaced configured.
- Configure OSPF Area 0 at the provider side (Router PE1, PE2, P1, P2 and P3).
- Advertise the loopback interfaces as well in OSPF.
- Make sure you advertise the loopback0 interfaces as /24 instead of the default /32 or you will run into trouble.
- Ensure you have full reachability in the OSPF domain.
- Configure MPLS on all physical interfaces in the service provider domain, do not configure MPLS on physical interfaces pointing towards the customer.
- Configure BGP AS 1 between Router PE1 and PE2.
- Configure the correct BGP address families and make sure communities are sent between neighbors.
- Configure a pseudowire on PE1 and PE2 to connect ToyHQ and ToyBranch.
- Configure a pseudowire on PE1 and PE2 to connect ArcadeHQ and ArcadeBranch.
- Configure OSPF Area 0 on router ToyHQ and ToyBranch. Advertise the loopbacks as well.
- Configure EIGRP AS 2 on router ArcadeHQ and ArcadeBranch. Advertise the loopbacks as well.
- Make sure you have an OSPF adjacency between the 2 Toy routers.
- Make sure you have an EIGRP adjacency between the 2 EIGRP routers.
- Ensure you have full connectivity for the customer networks. ToyHQ and ToyBranch should exchange OSPF prefixes and ArcadeHQ and ArcadeBranch should exchange EIGRP prefixes.
- At this moment you should have a working MPLS network but all traffic is being sent through P3. We are going to use MPLS traffic engineering to use P1 and P2 as well.
- Configure a tunnel10 interface on router PE1 and PE2 for VRF Toy. Make sure the tunnel is in MPLS traffic engineer mode.
- Configure the hold and setup priority to 1 for the tunnel 10 interface, set the bandwidth to 2000.
- Configure a tunnel11 interface on router PE1 and PE2 for VRF Arcade. Make sure the tunnel is in MPLS traffic engineer mode.
- Configure the hold and setup priority to 1 for the tunnel 11 interface, set the bandwidth to 2000.
- Configure the RSVP bandwidth to 2000 for all links interconnecting the P and PE routers.
- Configure MPLS traffic engineering tunnel support for all links interconnecting the P and PE routers.
- Finish your configuration so traffic for customer Toy is sent from PE1 through P1 and P2.
- Finish your configuration so traffic for customer Arcade is sent from PE1 through P3 and P2.

## GNS3 2.2.56.1

Import [mpls-traffic-eng-l2tpv3-startup-configs IOU.gns3project](mpls-traffic-eng-l2tpv3-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `mpls-traffic-eng-l2tpv3-startup-configs.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| ArcadeBranch | FastEthernet0/0 | Ethernet0/0 |
| ArcadeBranch | FastEthernet0/1 | Ethernet0/1 |
| ArcadeHQ | FastEthernet0/0 | Ethernet0/0 |
| ArcadeHQ | FastEthernet0/1 | Ethernet0/1 |
| P1 | FastEthernet0/0 | Ethernet0/0 |
| P1 | FastEthernet0/1 | Ethernet0/1 |
| P2 | FastEthernet0/0 | Ethernet0/0 |
| P2 | FastEthernet0/1 | Ethernet0/1 |
| P3 | FastEthernet0/0 | Ethernet0/0 |
| P3 | FastEthernet0/1 | Ethernet0/1 |
| PE1 | FastEthernet0/0 | Ethernet0/0 |
| PE1 | FastEthernet0/1 | Ethernet0/1 |
| PE1 | FastEthernet1/0 | Ethernet0/2 |
| PE1 | FastEthernet2/0 | Ethernet0/3 |
| PE2 | FastEthernet0/0 | Ethernet0/0 |
| PE2 | FastEthernet0/1 | Ethernet0/1 |
| PE2 | FastEthernet1/0 | Ethernet0/2 |
| PE2 | FastEthernet2/0 | Ethernet0/3 |
| ToyBranch | FastEthernet0/0 | Ethernet0/0 |
| ToyBranch | FastEthernet0/1 | Ethernet0/1 |
| ToyHQ | FastEthernet0/0 | Ethernet0/0 |
| ToyHQ | FastEthernet0/1 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.
