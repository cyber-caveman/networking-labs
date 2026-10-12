# Remote Shell

## Scenario

You are working as a network engineer at a Turtle Aquarium based in Florida. Your colleague wants to check the running-configuration of one of the routers in the network but because of the security policy he's not allowed to use HTTP, TFTP, TELNET or SSH. You can't break company regulations but maybe you can bend it a little?

## Goal

* All IP addresses have been preconfigured for you.
* Configure router Shell so router Turtle can view its running configuration.

## GNS3 2.2.56.1

Import [Remote Shell IOU.gns3project](Remote%20Shell%20IOU.gns3project) using **File > Import portable project**. To open `Remote Shell.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Shell | FastEthernet0/0 | Ethernet0/0 |
| Turtle | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-remote-shell.png)

## Video Solution

http://www.youtube.com/watch?v=Y3LAM8P3j7s
