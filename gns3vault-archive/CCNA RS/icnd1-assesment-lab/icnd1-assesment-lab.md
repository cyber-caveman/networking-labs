# ICND1 Assesment Lab

![Network Topology](./topology-icnd1-assesment-lab.jpg)

## Scenario:

You have been studying for the CCNA for quite some time, and you have just passed the ICND1 exam. While you continue your work towards achieving the ICND2 certificate to become fully CCNA certified you felt it was time to get a job to start your IT networking career. You apply for a job at "BigMobs inc" and the job interview went very smoothly...there is just one thing, they want you to show your newly acquired networking skills in a testlab! You are confident and willing to show your newly acquired tricks.

## Goal:

- Set all the correct hostnames on the routers.
- Set all the correct IP addresses and subnet masks, you are not allowed to use a subnet calculator.
- Godzilla: configure a type7 enable password "vault"
- Kingkong: configure a type5 enable password "vault"
- Nessie: only SSH access is allowed, no telnet. Username = big , Password = mobs
- Kingkong: configure password "cisco" on the console 0.
- The link between Godzilla and Nessie should be PPP encapsulation.
- The link between all other routers should be HDLC encapsulation.
- When you login remotely on Godzilla it should show a banner "Get away from Godzilla"
- Create a static host configuration so you can telnet to "KingKong" instead of the IP address.
- Disable automatic DNS lookups on Nessie.
- Godzilla: Make sure items sent to the console are not interrupting the command you type.
- Kingkong: the console should never timeout.
- Create a loopback1 interface on Godzilla, IP Address 1.1.1.1/24
- Create a static route on KingKong pointing to the loopback1 interface of Godzilla.
- Create a default route on Nessie pointing to the loopback1 interface of Godzilla, it should have an Administrative Distance of 200.
- Configure RIP on all routers, version2. You should be able to ping all networks.
- Make sure the subnetmask information is included with the routing updates.
- Disable CDP between KingKong and Godzilla.

## GNS3 2.2.56.1

Import [icnd1-assessment-startup-configs IOU.gns3project](icnd1-assessment-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `icnd1-assessment-startup-configs.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Godzilla | Serial0/0 | Serial4/0 |
| Godzilla | Serial0/1 | Serial4/1 |
| Godzilla | Serial0/2 | Serial4/2 |
| Godzilla | Serial0/3 | Serial4/3 |
| Nessie | Serial0/0 | Serial4/0 |
| Nessie | Serial0/1 | Serial4/1 |
| Nessie | Serial0/2 | Serial4/2 |
| Nessie | Serial0/3 | Serial4/3 |
| KingKong | Serial0/0 | Serial4/0 |
| KingKong | Serial0/1 | Serial4/1 |
| KingKong | Serial0/2 | Serial4/2 |
| KingKong | Serial0/3 | Serial4/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology:

## Video Solution:

http://www.youtube.com/watch?v=ksy5zq43wws
