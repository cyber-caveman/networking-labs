# MPLS AtoM / Pseudowire Frame-Relay over MPLS (FoMPLS)

![Network Topology](./topology-mpls-atom-pseudowire-frame-relay-over-mpls-eompls.jpg)

## Scenario

Molenaar Furniture is a wholesaler of furniture & more and located in The Netherlands. Recently the company has been expanding their business by taking it online. The warehouse needs to be connected to the store to make sure inventory can be updated real-time at the store's website. The company sites are currently connected by using Frame-Relay but the provider doesn't support these links anymore. It is however possible to hook up the Frame-relay links to the MPLS Backbone so these connections can be supported in the future. Let's see if you can tag this one...

## Goal

* All IP addresses have been preconfigured for you.
* All ISP routers have a loopback0 interfaced configured as following:
  - PE1: 2.2.2.2 /25
  - P: 3.3.3.3 /25
  - PE2: 4.4.4.4 /25
* Configure OSPF Area 0 at the provider side (Router PE1, PE2 and P).
* Advertise the loopback interfaces as well in OSPF.
* Make sure you don't send any OSPF Hello packets towards the customer.
* Ensure you have full reachability in the OSPF domain.
* Configure MPLS on all physical interfaces in the service provider domain, do not configure MPLS on physical interfaces pointing towards the customer.
* Router Store and Warehouse have been preconfigured with a DLCI number:
  - Store: DLCI 105
  - Warehouse: DLCI 501
* Configure the PE routers so you have end-to-end Frame-Relay connectivity over the MPLS Backbone, you are not allowed to make any changes to router P.
* Make sure router Store and Warehouse can ping each other.

## GNS3 2.2.56.1

Import [MPLSAtomFRoverMPLS IOU.gns3project](MPLSAtomFRoverMPLS%20IOU.gns3project) using **File > Import portable project**. To open `MPLSAtomFRoverMPLS.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Store | FastEthernet0/0 | Ethernet0/0 |
| Store | FastEthernet0/1 | Ethernet0/1 |
| Store | Serial1/0 | Serial4/0 |
| Store | Serial1/1 | Serial4/1 |
| Store | Serial1/2 | Serial4/2 |
| Store | Serial1/3 | Serial4/3 |
| Store | Serial1/4 | Serial5/0 |
| Store | Serial1/5 | Serial5/1 |
| Store | Serial1/6 | Serial5/2 |
| Store | Serial1/7 | Serial5/3 |
| PE1 | FastEthernet1/0 | Ethernet0/0 |
| PE1 | FastEthernet1/1 | Ethernet0/1 |
| PE1 | FastEthernet0/0 | Ethernet0/2 |
| PE1 | FastEthernet0/1 | Ethernet0/3 |
| PE1 | Serial2/0 | Serial4/0 |
| PE1 | Serial2/1 | Serial4/1 |
| PE1 | Serial2/2 | Serial4/2 |
| PE1 | Serial2/3 | Serial4/3 |
| PE1 | Serial2/4 | Serial5/0 |
| PE1 | Serial2/5 | Serial5/1 |
| PE1 | Serial2/6 | Serial5/2 |
| PE1 | Serial2/7 | Serial5/3 |
| P | FastEthernet1/0 | Ethernet0/0 |
| P | FastEthernet1/1 | Ethernet0/1 |
| P | FastEthernet0/0 | Ethernet0/2 |
| P | FastEthernet0/1 | Ethernet0/3 |
| PE2 | FastEthernet1/0 | Ethernet0/0 |
| PE2 | FastEthernet1/1 | Ethernet0/1 |
| PE2 | FastEthernet0/0 | Ethernet0/2 |
| PE2 | FastEthernet0/1 | Ethernet0/3 |
| PE2 | Serial2/0 | Serial4/0 |
| PE2 | Serial2/1 | Serial4/1 |
| PE2 | Serial2/2 | Serial4/2 |
| PE2 | Serial2/3 | Serial4/3 |
| PE2 | Serial2/4 | Serial5/0 |
| PE2 | Serial2/5 | Serial5/1 |
| PE2 | Serial2/6 | Serial5/2 |
| PE2 | Serial2/7 | Serial5/3 |
| Warehouse | FastEthernet0/0 | Ethernet0/0 |
| Warehouse | FastEthernet0/1 | Ethernet0/1 |
| Warehouse | Serial1/0 | Serial4/0 |
| Warehouse | Serial1/1 | Serial4/1 |
| Warehouse | Serial1/2 | Serial4/2 |
| Warehouse | Serial1/3 | Serial4/3 |
| Warehouse | Serial1/4 | Serial5/0 |
| Warehouse | Serial1/5 | Serial5/1 |
| Warehouse | Serial1/6 | Serial5/2 |
| Warehouse | Serial1/7 | Serial5/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

## Video Solution

[MPLS AtoM / Pseudowire Frame-Relay over MPLS (FoMPLS) Video Solution](http://www.youtube.com/watch?v=QYejOszFAOI)
