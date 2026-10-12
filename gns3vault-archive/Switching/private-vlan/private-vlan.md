# Private VLAN

![Network Topology](./topology-private-vlan.png)

## Scenario:



You are the senior network engineer of a small company specialized in switching solutions. The datacenter houses a couple of servers and you would like to increase security. You prefer to keep all servers within the same subnet and prevent the usage of access-lists. It sounds like Private VLANs could help you out...

## Goal:

* Configure all IP addresses as specified in the topology picture.
* Configure VLAN 500 to be the primary VLAN.
* Configure VLAN 501 as a secondary community VLAN.
* Configure VLAN 502 as a secondary isolated VLAN.
* Configure the correct mapping between the primary and secondary VLANs.
* Configure DNS1 and DNS2 to be in the secondary community VLAN 501.
* Configure WWW1 and WWW2 to be in the secondary isolated VLAN 502.
* Configure fa0/24 on SwitchA as the promiscious port.
* DNS1 and DNS2 should be able to communicate with each other and the Gateway.
* WWW1 and WWW2 should only be able to communicate with the Gateway.

## GNS3 2.2.56.1

Import [private-vlan IOU.gns3project](private-vlan%20IOU.gns3project) using **File > Import portable project**. To open `private-vlan.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

CLI switches explicitly select PVST when the source relies on that default. Converted EtherSwitch routers retain their default IP-routing state and routed FastEthernet0 ports. Use the IOU names below when following old interface references in the instructions and diagrams.

| Device | Source interface | Current interface |
| --- | --- | --- |
| SW1 | FastEthernet0/1 | Ethernet0/0 |
| SW1 | FastEthernet0/2 | Ethernet0/1 |
| SW1 | FastEthernet0/3 | Ethernet0/2 |
| SW1 | FastEthernet0/4 | Ethernet0/3 |
| SW1 | FastEthernet0/24 | Ethernet1/0 |
| DNS1 | FastEthernet0/0 | Ethernet0/0 |
| DNS2 | FastEthernet0/0 | Ethernet0/0 |
| WWW1 | FastEthernet0/0 | Ethernet0/0 |
| WWW2 | FastEthernet0/0 | Ethernet0/0 |
| Gateway | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology:

## Video Solution:

[YouTube Video: Private VLAN Configuration](http://www.youtube.com/watch?v=UYA7PQjNpls&)
