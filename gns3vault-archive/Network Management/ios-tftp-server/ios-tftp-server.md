# IOS TFTP Server

## Scenario

You are working as a network engineer for a Charity helping homeless people. At one day the webserver crashes and you don't have any spare equipment lying around. The website is used to download food coupons.

## Goal

- All IP addresses have been preconfigured for you.
- Configure router TFTP as a TFTP server.
- Configure router TFTP so only network 192.168.12.0 /24 is allowed to access the TFTP server.
- When router Client tries to download a file called "config" it should receive the configuration file of router TFTP.
- Test your configuration by copying the "config" file from router Client by using TFTP.

## GNS3 2.2.56.1

Import [IOS TFTP Server IOU.gns3project](IOS%20TFTP%20Server%20IOU.gns3project) using **File > Import portable project**. To open `IOS TFTP Server.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Client | FastEthernet0/0 | Ethernet0/0 |
| TFTP | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-ios-tftp-server.png)

## Video Solution

http://www.youtube.com/watch?v=hWWV6Ax5jOo
