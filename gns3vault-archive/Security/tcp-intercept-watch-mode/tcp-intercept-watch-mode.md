# TCP Intercept Watch Mode

## Scenario

As part of the security team you are always looking for ways to improve security within the company. Lately the company is under fire by TCP SYN floods. You don't have any budget to buy some firewalls so you decide to look for a cheaper solution to solve this problem. You heard some good things about the "TCP Intercept" feature so you decide to look into it.

## Goal

- All IP addresses have been configured for you, look at the topology picture for the IP addresses.
- OSPF has been preconfigured for you on all routers.
- Configure router Mirror so it resets all connections that don't finish the TCP 3 way handshake within 10 seconds by sending a RST to router Flash.

## Topology

![Network Topology](./topology-tcp-intercept-watch-mode.png)

## Video Solution

[Video Solution on YouTube](http://www.youtube.com/watch?v=3VuILNNh25E)

## GNS3 2.2.56.1

Import [TCP Intercept IOU.gns3project](TCP%20Intercept%20IOU.gns3project) using **File > Import portable project**. To open `TCP Intercept.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Catch | FastEthernet0/0 | Ethernet0/0 |
| Flash | FastEthernet0/0 | Ethernet0/0 |
| Mirror | FastEthernet0/0 | Ethernet0/0 |
| Mirror | FastEthernet1/0 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.
