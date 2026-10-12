# MPLS VPN PE CE using OSPF & Sham-Link

![Network Topology](./topology-mpls-vpn-pe-ce-using-ospf.jpg)

## Scenario

You have been dreaming of starting your own ISP for years and now the moment is finally here. You bought a couple of brand new routers and you are about to implement your MPLS backbone. Your first customer has just signed a contract for connecting two sites so there is nothing stopping you. One of your routers will be the "P" router for the backbone. The other two routers will be used as "PE" router to connect the customer's end devices. Your customer is running RIP as their (IGP) internal routing protocol. Your backbone will use OSPF as the IGP....time to create your business!

## Goal

- All IP addresses have been preconfigured for you.
- Every router has a loopback0 interfaced configured as following:
  - HQ: 1.1.1.1 /25
  - PE1: 2.2.2.2 /25
  - P2: 3.3.3.3 /25
  - PE2: 4.4.4.4 /25
  - BRANCH: 5.5.5.5 /25
- Configure OSPF Area 0 at the provider side (Router PE1, PE2 and P).
- Advertise the loopback interfaces as well in OSPF.
- Ensure you have full reachability in the OSPF domain.
- Configure MPLS on all physical interfaces in the service provider domain, do not configure MPLS on physical interfaces pointing towards the customer.
- Configure VRF "customer" on PE1 and PE2 as following:
  - RD 100:1
  - Route-target both 1:100
- On router PE1 and PE2 add the interfaces pointing towards the customer to the VRF you just created.
- Ensure you can ping from within the VRF, try this as following on PE1:
  - `ping vrf customer 192.168.12.1`
- Configure OSPF Area 0 on router HQ and Branch. Advertise the loopbacks as well.
- Configure OSPF on router PE1 and PE2 for the correct VRF "customer".
- Ensure you receive prefixes from the customer routers on your PE routers.
- Configure BGP AS 1 between Router PE1 and PE2.
- Configure the correct BGP address families and make sure communities are sent between neighbors.
- Redistribute OSPF into BGP, use the correct address-family for the VRF "customer".
- Ensure you have full connectivity between router HQ and Branch. You should see each other's OSPF routes that have been carried over the service provider's MPLS backbone.
- The OSPF prefixes on the HQ and Branch router are showing up as O IA (Inter-Area). Change this so they show up as E2 routes.
- Enable OSPF on the serial link between router HQ and Branch, this will be a backup link in case the MPLS Backbone crashes.
- You notice packets are being sent through the backup serial link instead of the MPLS Backbone. Make sure all packets are sent through the MPLS Backbone without removing OSPF on the serial link or shutting down the interface.

## GNS3 2.2.56.1

Import [MPLSVPNPECEOspf IOU.gns3project](MPLSVPNPECEOspf%20IOU.gns3project) using **File > Import portable project**. To open `MPLSVPNPECEOspf.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| HQ | FastEthernet0/0 | Ethernet0/0 |
| HQ | Serial1/0 | Serial4/0 |
| HQ | Serial1/1 | Serial4/1 |
| HQ | Serial1/2 | Serial4/2 |
| HQ | Serial1/3 | Serial4/3 |
| PE1 | FastEthernet0/0 | Ethernet0/0 |
| PE1 | FastEthernet1/0 | Ethernet0/1 |
| P | FastEthernet0/0 | Ethernet0/0 |
| P | FastEthernet1/0 | Ethernet0/1 |
| PE2 | FastEthernet0/0 | Ethernet0/0 |
| PE2 | FastEthernet1/0 | Ethernet0/1 |
| Branch | FastEthernet0/0 | Ethernet0/0 |
| Branch | Serial1/0 | Serial4/0 |
| Branch | Serial1/1 | Serial4/1 |
| Branch | Serial1/2 | Serial4/2 |
| Branch | Serial1/3 | Serial4/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

## Video Solution

[MPLS VPN PE CE using OSPF & Sham-Link - Video](http://www.youtube.com/watch?v=gCwrF6muDyM)
