# Switch SVI Interface and Routing

## Scenario



The network agency corporation has hired you as a spanning tree specialist. One of their customers has issues with a switched network that only has fiber connections. Every now and then there's a problem with the fiber and as a result layer 2 loops occur. It will take two months for the fiber company to check all cables/connectors so you want a temporary solution...

## Goal

* Configure all IP addresses as specified in the topology picture.
* Configure SW1 so it builds a routing table.
* Configure SW1 so router DNS1 and DNS2 are in VLAN 10.
* Configure the fa0/3 interface on SW1 as a routed port.
* Ensure all routers are able to communicate with each other.

## GNS3 2.2.56.1

Import [switch-svi-interface-and-routing IOU.gns3project](switch-svi-interface-and-routing%20IOU.gns3project) using **File > Import portable project**. To open `switch-svi-interface-and-routing.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

CLI switches explicitly select PVST when the source relies on that default. Converted EtherSwitch routers retain their default IP-routing state and routed FastEthernet0 ports. Use the IOU names below when following old interface references in the instructions and diagrams.

| Device | Source interface | Current interface |
| --- | --- | --- |
| SW1 | FastEthernet0/1 | Ethernet0/0 |
| SW1 | FastEthernet0/2 | Ethernet0/1 |
| SW1 | FastEthernet0/3 | Ethernet0/2 |
| DNS1 | FastEthernet0/0 | Ethernet0/0 |
| DNS2 | FastEthernet0/0 | Ethernet0/0 |
| WWW1 | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-switch-svi-interface-and-routing.png)

## Video Solution

[Video Solution on YouTube](http://www.youtube.com/watch?v=AB5Gr4vTmPw)
