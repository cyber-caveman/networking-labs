# IOS HTTP Server

## Scenario

You are working as a network engineer for a Charity helping homeless people. At one day the webserver crashes and you don't have any spare equipment lying around. Since the website only has HTML images you decide to configure one of your spare routers as a HTTP server.

## Goal

* All IP addresses have been preconfigured for you.
* Configure router HTTP as a HTTP server and make it serve files from the flash.
* Configure router HTTP so it only allows HTTP connections from port 5001 and the 192.168.12.0/24 network. There should be a maximum of 5 connections.
* Configure router HTTP so users have to authenticate to access the webserver. Use the username "VAULT" and password "SAFE".
* Test your configuration by transfering a file stored on router HTTP to router CLIENT.

## GNS3 2.2.56.1

Import [IOS HTTP Server IOU.gns3project](IOS%20HTTP%20Server%20IOU.gns3project) using **File > Import portable project**. To open `IOS HTTP Server.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Client | FastEthernet0/0 | Ethernet0/0 |
| HTTP | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-ios-http-server.png)

## Video Solution

http://www.youtube.com/watch?v=MDprS6DIWHc
