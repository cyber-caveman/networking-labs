# Unicast Reverse Path Forwarding (URPF)

## Scenario

As part of the security team you are always looking for ways to improve security within the company. Recently you are being plagued by different sources sending spoofed IP packets. You want to protect your network by checking for the source IP addresses using Unicast Reverse Path Forwarding. Let's see if you can find the root of this one...

## Goal

* All IP addresses have been configured for you, look at the topology picture for the IP addresses.
* OSPF has been preconfigured for you.
* Configure router Mirror so traffic on the FastEthernet 1/0 interface will be dropped if the source IP address doesn't match the next hop address that router Mirror has in its routing table.
* Configure router Mirror so traffic on the FastEthernet 0/0 interface will be dropped if the source IP address doesn't match anything that router Mirror has in its routing table.
* Configure router Mirror so all dropped packets are logged.

## Topology

![Network Topology](./topology-unicast-reverse-path-forwarding-urpf.png)

## Video Solution

[http://www.youtube.com/watch?v=fV7GQXAvPcc](http://www.youtube.com/watch?v=fV7GQXAvPcc)

## GNS3 2.2.56.1

Import [URPF IOU.gns3project](URPF%20IOU.gns3project) using **File > Import portable project**. To open `URPF.gns3` directly, keep it beside `project-files`.

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
