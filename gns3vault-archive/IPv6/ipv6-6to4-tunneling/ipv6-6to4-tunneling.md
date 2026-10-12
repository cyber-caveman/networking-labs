# IPv6 6to4 Tunneling

## Scenario

The largest ISP in Europa has acquired you as their main IPv6 specialist. To ensure connectivity for all customers the ISP has used static tunneling in order to send IPv6 packets through the IPv4 network. They want you to change this and make life a bit easier by creating dynamic tunneling...let's see if you can nail this one.

## Goal

- All IPv4 and IPv6 addresses have been preconfigured for you.
- Router Pim has a loopback0 interface with the 2001:1::1/64 IPv6 address.
- Router Pet has a loopback0 interface with the 2001:3::3/64 IPv6 address.
- You are not allowed to make any changes on router Pam.
- Configure a tunnel between router Pim and Pet, you are not allowed to specify a "tunnel destination" address.
- Ensure you can ping each other's loopback0 interfaces on router Pim and Pet through the tunnel interface.

**NOTE:** If you have trouble calculating the IPv4 address in hexadecimal you can use the `ipv6 general-prefix MYPREFIX 6to4 fastethernet0/0` command.

## GNS3 2.2.56.1

Import [IPv6 6to4 Tunneling IOU.gns3project](IPv6%206to4%20Tunneling%20IOU.gns3project) using **File > Import portable project**. To open `IPv6 6to4 Tunneling.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Pam | FastEthernet0/0 | Ethernet0/0 |
| Pam | FastEthernet1/0 | Ethernet0/1 |
| Pet | FastEthernet0/0 | Ethernet0/0 |
| Pim | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-ipv6-6to4-tunneling.png)

## Video Solution

[YouTube Video](http://www.youtube.com/watch?v=4EWn9amnTmA)
