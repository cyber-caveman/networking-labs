# OSPF Capability Transit Troubleshooting

## Scenario

After months of hard work, studying and doing labs you have the feeling you truly know how routing protocols work. Your boss decides to upgrade your salary and your title from Trainee to Junior network engineer and you will be responsible for daily maintenance for the network. Your senior network colleague (who is a true Guru but also very chaotic) is away for the the day and you are unable to reach him. Some users called you and complained about unreachable servers and slow links. It's 8:00am and they need to have access to the network by 12:00am. Time to show your boss who the new Guru is and perhaps get another salary upgrade!

## Goal

- All IP addresses have been preconfigured for you as specified in the topology picture.
- OSPF is preconfigured with the areas as specified in the topology picture.
- **Do not use show run**! (this will spoil the fun :) use the appropriate 'show' and 'debug' commands. This will teach you the skills needed to become a true troubleshooting master.
- Whenever router Nima tries to ping the FastEthernet0/0 interface of router Kyle traffic is being dropped. Solve the problem by using OSPF commands.

## GNS3 2.2.56.1

Import [OSPF Capability Transit IOU.gns3project](OSPF%20Capability%20Transit%20IOU.gns3project) using **File > Import portable project**. To open `OSPF Capability Transit.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Kyle | FastEthernet0/0 | Ethernet0/0 |
| Nima | FastEthernet0/0 | Ethernet0/0 |
| Nima | FastEthernet1/0 | Ethernet0/1 |
| Vanessa | FastEthernet0/0 | Ethernet0/0 |
| Vanessa | FastEthernet1/0 | Ethernet0/1 |
| Wilee | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-ospf-capability-transit-troubleshooting.png)
