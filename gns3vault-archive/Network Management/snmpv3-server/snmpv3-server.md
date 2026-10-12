# SNMPv3 Server

![Network Topology](./topology-snmpv3-server.png)

## Scenario:

The Agency has created a new security policy and since you are part of the security team you need to help them implement them. Some changes on the network have to be implemented through SNMPv3 and it's up to you to configure your router as a SMPv3 agent.

## Goal:

* All IP addresses have been preconfigured for you.
* Optional: You can use the cloud interface to connect your router to a free syslog server like Spiceworks FREE SNMP Network Manager (also works for SNMPv3).
* Configure router Agent with a SNMP MIB VIEW called "EVERYONE".
* Configure router Agent with a SNMP MIB VIEW called "FORYOUREYESONLY"
* Configure router Agent so "EVERYONE" contains branch "iso".
* Configure router Agent with a SNMP group called "EVERYONE". Use security model "priv". Assign read/write view to SNMP MIB VIEW "EVERYONE".
* Configure router Agent with a user called "007". Use MD5 password "VAULT" and DES encryption password "SAFE". Add this user to the "EVERYONE" group.
* Configure router Agent with a SNMP group called "FORYOUREYESONLY". Use security model "auth". Assign read view to SNMP MIB VIEW "FORYOUREYESONLY".
* Configure router Agent with a user called "bigeyes". This user only requires the password "LENS". Add the user to the "FORYOUREYESONLY" group.
* Configure router Agent so only users from network 192.168.12.0 /24 are allowed to access the SNMP GROUP "EVERYONE".
* Configure router Agent with a group called "KICKME" and use security model "priv".
* Configure router Agent with a user called "WILL" and add him to the group "KICKME". Use password "VAULT".
* Configure router Agent with SNMP traps to host 192.168.12.2 and use security model 'priv'. Use username "WILL".
* Configure router Agent to send a SNMP trap for event 'warmstart' and 'coldstart'.

## GNS3 2.2.56.1

Import [SNMP v3 Server IOU.gns3project](SNMP%20v3%20Server%20IOU.gns3project) using **File > Import portable project**. To open `SNMP v3 Server.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Agent | FastEthernet0/0 | Ethernet0/0 |
| Agent | FastEthernet1/0 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology:
