# SNMPv2 Server

## Scenario

The Agency has created a new security policy and since you are part of the security team you need to help them implement them. Some changes on the network have to be implemented through SNMPv2 and it's up to you to configure your router as a SNMPv2 agent.

## Goal

- All IP addresses have been preconfigured for you.
- Optional: You can use the cloud interface to connect your router to a free syslog server like Kiwi Syslog Server (also works for SNMPv2).
- Configure router Agent so it uses community string "VAULT".
- Configure router Agent so the SNMP contact is "007".
- Configure router Agent so the SNMP location is "Agency".
- Configure router Agent so the largest SNMP packet is 1500.
- Configure router Agent so the router can be reloaded through SNMP.
- Configure router Agent so only network 192.168.12.0 /24 is allowed to contact the router. Dropped packets should be logged.
- Configure router Agent so it has a community string called "README". This should only be used for read-only access.
- Configure router Agent to traps are sent to SNMPv2 server IP address 192.168.12.2. Use community string "VAULT".
- Configure router Agent so it informs a device with IP address 192.168.12.3. Use community string "VAULT".
- Create a loopback0 interface on router Agent with IP address 1.1.1.1 /24.
- Configure router Agent so it doesn't send any traps or informs when something happens with the loopback0 interface.
- Configure router Agent so it generates a trap when a new OSPF LSA is originated.

## GNS3 2.2.56.1

Import [SNMP v2 Server IOU.gns3project](SNMP%20v2%20Server%20IOU.gns3project) using **File > Import portable project**. To open `SNMP v2 Server.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Agent | FastEthernet0/0 | Ethernet0/0 |
| Agent | FastEthernet1/0 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-snmpv2-server.png)
