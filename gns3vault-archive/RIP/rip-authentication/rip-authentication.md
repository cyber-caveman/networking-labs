# RIP Authentication

## Scenario

Your local dentist just checked your teeth and has some bad news for you. He mentions he has some trouble with the dentist network running RIP and authentication. If you don't fix his RIP network he will perform root canal surgery on you so it's time to get going!

## Goal

- All IP addresses have been preconfigured for you.
- All routers have a loopback interface as following:
  - Bite: 1.1.1.1/24
  - Arch: 2.2.2.2/24
  - Apex: 3.3.3.3/24
- Configure RIP version 2 on all routers, achieve full connectivity for all networks (including the loopbacks)
- Configure RIP plaintext authentication between router Bite and Arch.
- Configure RIP MD5 authentication between router Bite and Apex.

## GNS3 2.2.56.1

Import [RIP Authentication IOU.gns3project](RIP%20Authentication%20IOU.gns3project) using **File > Import portable project**. To open `RIP Authentication.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Apex | FastEthernet0/0 | Ethernet0/0 |
| Arch | FastEthernet0/0 | Ethernet0/0 |
| Bite | FastEthernet0/0 | Ethernet0/0 |
| Bite | FastEthernet1/0 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-rip-authentication.png)

## Video Solution

http://www.youtube.com/watch?v=g8MmoNP9rt0
