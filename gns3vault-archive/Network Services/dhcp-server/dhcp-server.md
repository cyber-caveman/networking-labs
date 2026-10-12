# DHCP Server

## Scenario

You are a trainee and studying for your CCNA certification. Your boss asks you if you can configure a DHCP server for some wireless clients. Confident as you are you take one of your routers and start typing in commands...

## Goal

* The IP address on router Bliss has been preconfigured for you.
* Configure a DHCP pool on router Bliss called "VAULT" with the following configuration:
  * Clients should use the DNS server with IP address 1.1.1.1.
  * Clients should use network 192.168.12.0 /24.
  * Clients should not use the 192.168.12.10 - 20 range.
  * Clients should renew their IP address after 2 hours.
* Configure router Bliss so it does not respond to BOOTP.
* Configure router Bliss so it stores DHCP bindings in flash.
* Configure router Ignorance so it receives an IP address through DHCP.

## GNS3 2.2.56.1

Import [DHCP Server IOU.gns3project](DHCP%20Server%20IOU.gns3project) using **File > Import portable project**. To open `DHCP Server.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Bliss | FastEthernet0/0 | Ethernet0/0 |
| Ignorance | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-dhcp-server.png)

## Video Solution

[Video Solution on YouTube](http://www.youtube.com/watch?v=8E8e1232ZiM)
