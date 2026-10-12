# Reflexive Access-List

## Scenario

As part of the security team you are always looking for ways to improve security within the company. You want to get rid of all the local vty/console logins within your network so you decide to implement some AAA security.

## Goal

- All IP addresses have been configured for you, look at the topology picture for the IP addresses.
- OSPF has been preconfigured for full connectivity.
- Configure router Mirror so ICMP and TCP traffic from network 1.1.1.0 /24 is allowed.
- Configure router Mirror with an inbound access-list on the FastEthernet1/0 interface so return traffic is allowed. You are not allowed to create specific entries.

## Topology

![Network Topology](./topology-reflexive-access-list.png)

## Video Solution

[Watch on YouTube](http://www.youtube.com/watch?v=LzeJGF6hhBs)

## GNS3 2.2.56.1

Import [Reflexive Access-Lists IOU.gns3project](Reflexive%20Access-Lists%20IOU.gns3project) using **File > Import portable project**. To open `Reflexive Access-Lists.gns3` directly, keep it beside `project-files`.

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
