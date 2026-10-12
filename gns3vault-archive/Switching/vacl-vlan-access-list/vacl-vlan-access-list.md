# VACL (VLAN Access List)

## Scenario



The network agency corporation has security issues with their network. They are familiar with the configuration of access-lists but they have no idea how to filter traffic within a VLAN. You are familiar with Cisco catalyst switches so you decide to help them out to configure some VLAN access-lists (VACL).

## Goal

* Configure all IP addresses as specified in the topology picture.
* Configure SW1 so router DNS1 and DNS2 are unable to ping each other. Other traffic should be allowed.
* The interfaces on SW1 have to be layer 2 switchports.

## Additional Information

## GNS3 2.2.56.1

Import [vacl-vlan-access-list IOU.gns3project](vacl-vlan-access-list%20IOU.gns3project) using **File > Import portable project**. To open `vacl-vlan-access-list.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

CLI switches explicitly select PVST when the source relies on that default. Converted EtherSwitch routers retain their default IP-routing state and routed FastEthernet0 ports. Use the IOU names below when following old interface references in the instructions and diagrams.

| Device | Source interface | Current interface |
| --- | --- | --- |
| SW1 | FastEthernet0/1 | Ethernet0/0 |
| SW1 | FastEthernet0/2 | Ethernet0/1 |
| DNS1 | FastEthernet0/0 | Ethernet0/0 |
| DNS2 | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-vacl-vlan-access-list.png)

## Video Solution

[Video: VACL Configuration](http://www.youtube.com/watch?v=Ji4Hod7m_5U)
