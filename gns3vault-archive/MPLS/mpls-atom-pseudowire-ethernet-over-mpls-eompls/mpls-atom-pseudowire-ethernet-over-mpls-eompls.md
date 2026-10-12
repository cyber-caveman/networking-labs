# MPLS AtoM / Pseudowire Ethernet over MPLS (EoMPLS)

![Network Topology](./topology-mpls-atom-pseudowire-ethernet-over-mpls-eompls.jpg)

## Scenario

One of the largest service providers in The Netherlands has been successfully implementing MPLS in their backbone. The last years they have been serving customers with PE-CE setups without any problem. Yesterday a new customer specialized in selling Bananas arrived who is not looking for a PE-CE solution but rather would see an end-to-end Ethernet solution. Since the ISP has never configured this before they ask you; A respected Cisco Guru to implement MPLS AtoM (Any Type over MPLS) for them. Let's see if you can pull this one off!

## Goal

- All IP addresses have been preconfigured for you.
- All ISP routers have a loopback0 interface configured as following:
  - PE1: 2.2.2.2 /25
  - P: 3.3.3.3 /25
  - PE2: 4.4.4.4 /25
- Configure OSPF Area 0 at the provider side (Router PE1, PE2 and P).
- Advertise the loopback interfaces as well in OSPF.
- Make sure you don't send any OSPF Hello packets towards the customer.
- Ensure you have full reachability in the OSPF domain.
- Configure MPLS on all physical interfaces in the service provider domain, do not configure MPLS on physical interfaces pointing towards the customer.
- Configure the PE routers to encapsulate every frame in a MPLS packet and to forward it to the other PE router using VC ID 15.
- Make sure router BananaHQ and BananaBranch can ping each other.

## GNS3 2.2.56.1

Import [MPLSAtomEoMPLS IOU.gns3project](MPLSAtomEoMPLS%20IOU.gns3project) using **File > Import portable project**. To open `MPLSAtomEoMPLS.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| BananaHQ | FastEthernet1/0 | Ethernet0/0 |
| BananaHQ | FastEthernet1/1 | Ethernet0/1 |
| BananaHQ | FastEthernet0/0 | Ethernet0/2 |
| BananaHQ | FastEthernet0/1 | Ethernet0/3 |
| PE1 | FastEthernet1/0 | Ethernet0/0 |
| PE1 | FastEthernet1/1 | Ethernet0/1 |
| PE1 | FastEthernet0/0 | Ethernet0/2 |
| PE1 | FastEthernet0/1 | Ethernet0/3 |
| P | FastEthernet1/0 | Ethernet0/0 |
| P | FastEthernet1/1 | Ethernet0/1 |
| P | FastEthernet0/0 | Ethernet0/2 |
| P | FastEthernet0/1 | Ethernet0/3 |
| PE2 | FastEthernet1/0 | Ethernet0/0 |
| PE2 | FastEthernet1/1 | Ethernet0/1 |
| PE2 | FastEthernet0/0 | Ethernet0/2 |
| PE2 | FastEthernet0/1 | Ethernet0/3 |
| BananaBranch | FastEthernet1/0 | Ethernet0/0 |
| BananaBranch | FastEthernet1/1 | Ethernet0/1 |
| BananaBranch | FastEthernet0/0 | Ethernet0/2 |
| BananaBranch | FastEthernet0/1 | Ethernet0/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

## Video Solution

[MPLS AtoM / Pseudowire Ethernet over MPLS (EoMPLS) - Video](http://www.youtube.com/watch?v=gNVGr-3p0u0)
