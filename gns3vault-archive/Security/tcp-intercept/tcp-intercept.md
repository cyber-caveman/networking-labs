# TCP Intercept

## Scenario

As part of the security team you are always looking for ways to improve security within the company. Lately the company is under fire by TCP SYN floods. You don't have any budget to buy some firewalls so you decide to look for a cheaper solution to solve this problem. You heard some good things about the "TCP Intercept" feature so you decide to look into it.

## Goal

- All IP addresses have been configured for you, look at the topology picture for the IP addresses.
- OSPF has been preconfigured for you on all routers.
- Configure Telnet on router Flash.
- Configure router Mirror so it closes half-open connections to router Flash after 15 seconds.
- Configure router Mirror so it starts closing half-open connections when there is more than one connection per second. It should keep doing this until the connection rate is about one per three minutes.
- Configure router Mirror so it only allows 20 half-open connections. Drop connections until you hit 15 half-open connections.

## Topology

![Network Topology](./topology-tcp-intercept.png)

**You need to register to be able to download the GNS3 Topology File. (Registration is Free!)**

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
