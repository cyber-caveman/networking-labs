# IOS Login Enhancements

## Scenario

You are the security office for the national security team in the Netherlands. One of your colleagues demonstrated you how to perform a dictionary attack on the VTY of one of your routers. You read about the different IOS login enhancements and decide to protect your network a little bit more.

## Goals

- All IP addresses have been preconfigured for you.
- Configure OSPF for full connectivity.
- Configure router Bulldog so it will block all access to the VTY for 50 seconds when there are three failed attempts within 20 seconds. This should not apply for traffic that is sourced from the loopback0 interface on router Guard.
- Configure router Bulldog so all successful logins are logged.
- Configure router Bulldog so there is a delay between login attempts of 5 seconds.

## GNS3 2.2.56.1

Import [IOS Login Enhancements IOU.gns3project](IOS%20Login%20Enhancements%20IOU.gns3project) using **File > Import portable project**. To open `IOS Login Enhancements.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Bulldog | FastEthernet0/0 | Ethernet0/0 |
| Guard | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-ios-login-enhancements.png)

## Video Solution

[Video Link](http://www.youtube.com/watch?v=9RhVbvwq3I4)
