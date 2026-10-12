# RIP Offset List

## Scenario

You are a loyal customer of a company called "Ratchet Construction". They heard you are a famous network engineer and are looking for your help with their network. Their routers are running RIP and they would like to influence the routing paths currently in use. Since the routers are a couple of years old they don't support anything fancy like policy-based routing. See if you can grind your way through some RIP configurations...

## Goal

- All IP addresses have been preconfigured for you.
- Configure RIP version 2 on all routers and make sure you have full connectivity. Advertise all loopback interfaces on router Drill.
- You are only allowed to use offset-lists for this lab.
- Ensure router Burr, Ratchet and Grinder use the F1/0 link on router Drill to reach network 1.1.1.0 /24.
- Ensure router Ratchet uses the F0/0 link on router Drill to reach network 11.11.11.0 /24.
- Ensure network 111.111.111.0 /24 is unreachable for router Grinder. It has to be reachable for Burr and Ratchet.

## GNS3 2.2.56.1

Import [RIP Offset-List IOU.gns3project](RIP%20Offset-List%20IOU.gns3project) using **File > Import portable project**. To open `RIP Offset-List.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Burr | FastEthernet0/0 | Ethernet0/0 |
| Burr | FastEthernet1/0 | Ethernet0/1 |
| Drill | FastEthernet0/0 | Ethernet0/0 |
| Drill | FastEthernet1/0 | Ethernet0/1 |
| Grinder | FastEthernet0/0 | Ethernet0/0 |
| Grinder | FastEthernet1/0 | Ethernet0/1 |
| Ratchet | FastEthernet0/0 | Ethernet0/0 |
| Ratchet | FastEthernet1/0 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-rip-offset-list.png)

## Video Solution

http://www.youtube.com/watch?v=epKKpwKXp7s
