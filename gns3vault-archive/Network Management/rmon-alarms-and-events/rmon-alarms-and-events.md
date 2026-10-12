# RMON Alarms and Events

## Scenario

The Agency has created a new security policy and since you are part of the security team you need to help them implement them. Whenever anything funky happens on the network you want to ensure a RMON alarm informs the logging server what is going on.

## Goal

- All IP addresses have been preconfigured for you.
- Optional: You can use the cloud interface to connect your router to a free syslog server like Kiwi Syslog Server (also works for SNMPv2).
- Configure router Ripley to track the packet rate on the FastEthernet 1/0 interface.
- When the packet rate is above 50 packets you need to send a SMTP trap with the message "too much!".
- When the packet rate falls below 50 packets you need to send a SMTP trap with the message "ah much better!".
- Use SNMP community string "VAULT".
- Configure router Bishop to check the CPU average each 5 minutes. When it's above 85% it should generate a message "hot hot!". When it falls below 30% it should generate the message "Cool".
- Send these messages to SNMP server 192.168.12.2.

## GNS3 2.2.56.1

Import [RMON Alarms and Events IOU.gns3project](RMON%20Alarms%20and%20Events%20IOU.gns3project) using **File > Import portable project**. To open `RMON Alarms and Events.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Bishop | FastEthernet0/0 | Ethernet0/0 |
| Ripley | FastEthernet0/0 | Ethernet0/0 |
| Ripley | FastEthernet1/0 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-rmon-alarms-and-events.png)
