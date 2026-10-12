# EIGRP CCNP 1

## Scenario

Woods 'r' Us is looking for network engineers that are CCNP certified. You apply for a job as an EIGRP network engineer and instead of a job interview they ask you to configure a network so you can show them your EIGRP skills. If you successfully configure this network you are certain to get the job!

## Goal

- All IPv4 addresses have been preconfigured for you.
- Each router has a loopback0 interface.
- Configure EIGRP AS 1 on all routers. Disable auto-summary.
- Configure EIGRP so reliability is also used as a metric.
- Make sure router Alder will use the serial 1/0 interface as the primary link.
- Make sure the FastEthernet0/0 interface on router Alder is a feasible successor and visible in the routing table for unequal load-balancing.
- Router Walnut should send a summary route towards router Lyptus which only includes the loopback0 interfaces of router Alder, Cherry, Maple and Walnut. The summary route has to be as specific as possible.
- The summary route you just created should show up with an administrative distance of 51 on router Walnut.
- Ensure router Alder does not send EIGRP packets towards its loopback0 interface.
- Configure router Walnut so the loopback0 interface of router Lyptus will not be advertised towards router Cherry and Maple.
- Create a default route on router Cherry and advertise it in EIGRP.
- Ensure only one path is used between router Walnut and Lyptus without breaking the EIGRP neighbor adjacency. You are not allowed to change the metrics.
- Configure the serial interface of router Alder so EIGRP is allowed only 25% the available physical bandwidth.
- Configure authentication between router Cherry and Walnut. The key-chain should be called "GNS3VAULT" and the password is "WOOD".
- Router Lyptus shouldn't receive any query packets for lost networks.
- The serial link between router Alder and Maple will not allow multicast traffic in the future. Make the changes so the EIGRP neighbor adjacency doesn't drop when this change takes effect.
- Configure EIGRP on the frame relay network between router Maple, Pine and Oak. You have to configure EIGRP using the multipoint sub-interfaces. Advertise the loopback0 interfaces and ensure you have full reachability between the three routers.

---

## GNS3 2.2.56.1

Import [EIGRP CCNP 1 IOU.gns3project](EIGRP%20CCNP%201%20IOU.gns3project) using **File > Import portable project**. To open `EIGRP CCNP 1.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Alder | FastEthernet0/0 | Ethernet0/0 |
| Alder | Serial1/0 | Serial4/0 |
| Alder | Serial1/1 | Serial4/1 |
| Alder | Serial1/2 | Serial4/2 |
| Alder | Serial1/3 | Serial4/3 |
| Cherry | FastEthernet0/0 | Ethernet0/0 |
| Cherry | FastEthernet1/0 | Ethernet0/1 |
| Lyptus | FastEthernet0/0 | Ethernet0/0 |
| Lyptus | FastEthernet1/0 | Ethernet0/1 |
| Maple | FastEthernet1/0 | Ethernet0/0 |
| Maple | Serial0/0 | Serial4/0 |
| Maple | Serial0/1 | Serial4/1 |
| Maple | Serial0/2 | Serial4/2 |
| Maple | Serial0/3 | Serial4/3 |
| Oak | Serial0/0 | Serial4/0 |
| Oak | Serial0/1 | Serial4/1 |
| Oak | Serial0/2 | Serial4/2 |
| Oak | Serial0/3 | Serial4/3 |
| Pine | Serial0/0 | Serial4/0 |
| Pine | Serial0/1 | Serial4/1 |
| Pine | Serial0/2 | Serial4/2 |
| Pine | Serial0/3 | Serial4/3 |
| Walnut | FastEthernet0/0 | Ethernet0/0 |
| Walnut | FastEthernet1/0 | Ethernet0/1 |
| Walnut | FastEthernet2/0 | Ethernet0/2 |
| Walnut | FastEthernet3/0 | Ethernet0/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-eigrp-ccnp-1.png)
