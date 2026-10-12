# DHCP Snooping

![Network Topology](./topology-dhcp-snooping.png)

## Scenario:



One of your customers is being plagued by attacks on their switched infrastructure. You as a specialized switch specialist are looking for a method to counter DHCP spoofing attacks. Let's see what you can do for them...

## Goal:

* Configure the IP addresses on router Attacker and DHCP as specified in the topology picture.
* Configure DHCP server on router DHCP so it can serve the client an IP address.
* Configure DHCP snooping globally on SW1.
* Configure SW1 to use the correct trusted and untrusted interfaces.
* Configure SW1 so the client is limited to 10 DHCP packets per second.
* Configure router Attacker as a DHCP server to verify your DHCP snooping configuration.

## GNS3 2.2.56.1

Import [dhcp-snooping IOU.gns3project](dhcp-snooping%20IOU.gns3project) using **File > Import portable project**. To open `dhcp-snooping.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

CLI switches explicitly select PVST when the source relies on that default. Converted EtherSwitch routers retain their default IP-routing state and routed FastEthernet0 ports. Use the IOU names below when following old interface references in the instructions and diagrams.

| Device | Source interface | Current interface |
| --- | --- | --- |
| SW1 | FastEthernet0/1 | Ethernet0/0 |
| SW1 | FastEthernet0/13 | Ethernet0/1 |
| SW1 | FastEthernet0/16 | Ethernet0/2 |
| Attacker | FastEthernet0/0 | Ethernet0/0 |
| Client | FastEthernet0/0 | Ethernet0/0 |
| Client | FastEthernet0/13 | Ethernet0/1 |
| DHCPServer | FastEthernet0/0 | Ethernet0/0 |
| DHCPServer | FastEthernet0/13 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology:

## Video Solution:

http://www.youtube.com/watch?v=Mv9HsviLzdk&
