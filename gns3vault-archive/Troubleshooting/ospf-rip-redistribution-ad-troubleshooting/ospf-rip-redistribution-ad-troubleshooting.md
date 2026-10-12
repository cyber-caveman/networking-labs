# OSPF RIP Redistribution AD Troubleshooting

## Scenario

Recently the australian government has decided that every major City should be interconnected. So far different states have used their own routing protocol and some of the older hardware is unable to run OSPF. Government workers have connected all routers and configured redistribution between RIP and OSPF so that every network is reachable. Everything seems to work fine and all routing tables have full information, however some people complained that the network is slow. You notice that when you start a traceroute from router Sydney or Melbourne towards the networks behind router Adelaide (4.4.4.4) or Darwin (5.5.5.5) that the traffic is sent towards router Perth. This is a classical example of sub-optimal routing...up to you to improve things!

## Goal

- All IP addresses have been preconfigured for you as following.
- Every router has 1 loopback interface as following: Loopback0: x.x.x.x /24 for example: 1.1.1.1 for router1.
- RIP and OSPF are preconfigured for you.
- **Do not use show run**! (this will spoil the fun :) use the appropiate 'show' and 'debug' commands. This will teach you the skills needed to become a true troubleshooting master.
- Do not make changes to the network commands in OSPF or RIP.
- You are not allowed to use distribute-lists, prefix-lists or route-maps.
- You are not allowed to change any of the redistribution commands.
- Ensure traffic takes the most optimal path to it's destination, use traceroute to check this.
- Ensure all routers have full connectivity, every network should be pingable using the most optimal path.

## GNS3 2.2.56.1

Import [OSPF RIP Redistribution AD Troubleshooting IOU.gns3project](OSPF%20RIP%20Redistribution%20AD%20Troubleshooting%20IOU.gns3project) using **File > Import portable project**. To open `OSPF RIP Redistribution AD Troubleshooting.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Perth | FastEthernet0/0 | Ethernet0/0 |
| Perth | FastEthernet1/0 | Ethernet0/1 |
| Sydney | FastEthernet0/0 | Ethernet0/0 |
| Sydney | FastEthernet1/0 | Ethernet0/1 |
| Melbourne | FastEthernet0/0 | Ethernet0/0 |
| Melbourne | FastEthernet1/0 | Ethernet0/1 |
| Adelaide | FastEthernet0/0 | Ethernet0/0 |
| Adelaide | FastEthernet1/0 | Ethernet0/1 |
| Darwin | FastEthernet0/0 | Ethernet0/0 |
| Darwin | FastEthernet1/0 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-ospf-rip-redistribution-ad-troubleshooting.png)

## Video Solution

[Video: OSPF RIP AD Troubleshooting Solution](http://www.youtube.com/watch?v=gQ0amfpJrsI)
