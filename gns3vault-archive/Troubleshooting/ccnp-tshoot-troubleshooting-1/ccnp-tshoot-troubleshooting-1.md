# CCNP TSHOOT Troubleshooting 1

## Scenario

This is the first CCNP TSHOOT Troubleshooting scenario based on the official Cisco CCNP TSHOOT topology. This lab is pre-configured and "broken" so you can learn how to troubleshoot a full network. Before you start with this lab I highly recommend you to study the topology, you can find the PDF in the attachments. Below you will find the troubleshooting tickets for you to solve!

## Goal

- Everything is pre-configured for you.
- **Do not use show run**! (this will spoil the fun :) use the appropriate 'show' and 'debug' commands. This will teach you the skills needed to become a true troubleshooting master.
- **Ticket #1:** One of the users was working on Client1 but he's complaining that there is no connectivity. He left a comment that he saw a message on the windows taskbar that said something like "no network connectivity". One of your colleagues looked into the problem and told you it had probably something to do with DHCP.
- **Ticket #2:** After fixing the issue with Client1 you receive another ticket that users from VLAN 10 are complaining that they are unable to connect to the FTP server.
- **Ticket #3:** Your users are happy that they can connect to the FTP server but they are still unable to reach the webserver.
- **Ticket #4:** The IPv6 team left a ticket for you that they are unable to reach 2026::12:/122 from DSW1 or DSW2.

## GNS3 2.2.56.1

Import [CCNP TSHOOT Troubleshooting 1 IOU.gns3project](CCNP%20TSHOOT%20Troubleshooting%201%20IOU.gns3project) using **File > Import portable project**. To open `CCNP TSHOOT Troubleshooting 1.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

CLI switches explicitly select PVST when the source relies on that default. Converted EtherSwitch routers retain their default IP-routing state and routed FastEthernet0 ports. Use the IOU names below when following old interface references in the instructions and diagrams.

| Device | Source interface | Current interface |
| --- | --- | --- |
| ASW1 | FastEthernet0/0 | Ethernet0/0 |
| ASW1 | FastEthernet0/1 | Ethernet0/1 |
| ASW1 | FastEthernet1/0 | Ethernet0/2 |
| ASW1 | FastEthernet1/1 | Ethernet0/3 |
| ASW1 | FastEthernet1/2 | Ethernet1/0 |
| ASW1 | FastEthernet1/3 | Ethernet1/1 |
| ASW1 | FastEthernet1/4 | Ethernet1/2 |
| ASW1 | FastEthernet1/5 | Ethernet1/3 |
| ASW1 | FastEthernet1/6 | Ethernet2/0 |
| ASW1 | FastEthernet1/7 | Ethernet2/1 |
| ASW1 | FastEthernet1/8 | Ethernet2/2 |
| ASW1 | FastEthernet1/9 | Ethernet2/3 |
| ASW1 | FastEthernet1/10 | Ethernet3/0 |
| ASW1 | FastEthernet1/11 | Ethernet3/1 |
| ASW1 | FastEthernet1/12 | Ethernet3/2 |
| ASW1 | FastEthernet1/13 | Ethernet3/3 |
| ASW2 | FastEthernet0/0 | Ethernet0/0 |
| ASW2 | FastEthernet0/1 | Ethernet0/1 |
| ASW2 | FastEthernet1/0 | Ethernet0/2 |
| ASW2 | FastEthernet1/1 | Ethernet0/3 |
| ASW2 | FastEthernet1/2 | Ethernet1/0 |
| ASW2 | FastEthernet1/3 | Ethernet1/1 |
| ASW2 | FastEthernet1/4 | Ethernet1/2 |
| ASW2 | FastEthernet1/5 | Ethernet1/3 |
| ASW2 | FastEthernet1/6 | Ethernet2/0 |
| ASW2 | FastEthernet1/7 | Ethernet2/1 |
| ASW2 | FastEthernet1/8 | Ethernet2/2 |
| ASW2 | FastEthernet1/9 | Ethernet2/3 |
| ASW2 | FastEthernet1/10 | Ethernet3/0 |
| ASW2 | FastEthernet1/11 | Ethernet3/1 |
| ASW2 | FastEthernet1/12 | Ethernet3/2 |
| ASW2 | FastEthernet1/13 | Ethernet3/3 |
| Client1 | FastEthernet0/0 | Ethernet0/0 |
| Client1 | FastEthernet0/1 | Ethernet0/1 |
| Client2 | FastEthernet0/0 | Ethernet0/0 |
| Client2 | FastEthernet0/1 | Ethernet0/1 |
| DSW1 | FastEthernet0/0 | Ethernet0/0 |
| DSW1 | FastEthernet0/1 | Ethernet0/1 |
| DSW1 | FastEthernet1/0 | Ethernet0/2 |
| DSW1 | FastEthernet1/1 | Ethernet0/3 |
| DSW1 | FastEthernet1/2 | Ethernet1/0 |
| DSW1 | FastEthernet1/3 | Ethernet1/1 |
| DSW1 | FastEthernet1/4 | Ethernet1/2 |
| DSW1 | FastEthernet1/5 | Ethernet1/3 |
| DSW1 | FastEthernet1/6 | Ethernet2/0 |
| DSW1 | FastEthernet1/7 | Ethernet2/1 |
| DSW1 | FastEthernet1/8 | Ethernet2/2 |
| DSW1 | FastEthernet1/9 | Ethernet2/3 |
| DSW1 | FastEthernet1/10 | Ethernet3/0 |
| DSW1 | FastEthernet1/11 | Ethernet3/1 |
| DSW1 | FastEthernet1/12 | Ethernet3/2 |
| DSW1 | FastEthernet1/13 | Ethernet3/3 |
| DSW2 | FastEthernet0/0 | Ethernet0/0 |
| DSW2 | FastEthernet0/1 | Ethernet0/1 |
| DSW2 | FastEthernet1/0 | Ethernet0/2 |
| DSW2 | FastEthernet1/1 | Ethernet0/3 |
| DSW2 | FastEthernet1/2 | Ethernet1/0 |
| DSW2 | FastEthernet1/3 | Ethernet1/1 |
| DSW2 | FastEthernet1/4 | Ethernet1/2 |
| DSW2 | FastEthernet1/5 | Ethernet1/3 |
| DSW2 | FastEthernet1/6 | Ethernet2/0 |
| DSW2 | FastEthernet1/7 | Ethernet2/1 |
| DSW2 | FastEthernet1/8 | Ethernet2/2 |
| DSW2 | FastEthernet1/9 | Ethernet2/3 |
| DSW2 | FastEthernet1/10 | Ethernet3/0 |
| DSW2 | FastEthernet1/11 | Ethernet3/1 |
| DSW2 | FastEthernet1/12 | Ethernet3/2 |
| DSW2 | FastEthernet1/13 | Ethernet3/3 |
| FTPServer | FastEthernet0/0 | Ethernet0/0 |
| FTPServer | FastEthernet0/1 | Ethernet0/1 |
| ISP | FastEthernet0/0 | Ethernet0/0 |
| ISP | FastEthernet0/1 | Ethernet0/1 |
| ISP | Serial0/0 | Serial4/0 |
| ISP | Serial0/2 | Serial4/1 |
| ISP | Serial0/1 | Serial4/2 |
| R1 | FastEthernet0/0 | Ethernet0/0 |
| R1 | FastEthernet0/1 | Ethernet0/1 |
| R1 | Serial0/0 | Serial4/0 |
| R1 | Serial0/2 | Serial4/1 |
| R1 | Serial0/1 | Serial4/2 |
| R2 | FastEthernet0/0 | Ethernet0/0 |
| R2 | FastEthernet0/1 | Ethernet0/1 |
| R2 | Serial0/0 | Serial4/0 |
| R2 | Serial0/1 | Serial4/1 |
| R2 | Serial0/2 | Serial4/2 |
| R3 | FastEthernet0/0 | Ethernet0/0 |
| R3 | FastEthernet0/1 | Ethernet0/1 |
| R3 | Serial0/0 | Serial4/0 |
| R3 | Serial0/1 | Serial4/1 |
| R3 | Serial0/2 | Serial4/2 |
| R4 | FastEthernet0/0 | Ethernet0/0 |
| R4 | FastEthernet0/1 | Ethernet0/1 |
| R4 | FastEthernet1/0 | Ethernet0/2 |
| R4 | FastEthernet2/0 | Ethernet0/3 |
| R4 | Serial0/0 | Serial4/0 |
| R4 | Serial0/1 | Serial4/1 |
| R4 | Serial0/2 | Serial4/2 |
| WebServer | FastEthernet0/0 | Ethernet0/0 |
| WebServer | FastEthernet0/1 | Ethernet0/1 |
| WebServer | Serial0/0 | Serial4/0 |
| WebServer | Serial0/2 | Serial4/1 |
| WebServer | Serial0/1 | Serial4/2 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-ccnp-tshoot-troubleshooting-1.png)
