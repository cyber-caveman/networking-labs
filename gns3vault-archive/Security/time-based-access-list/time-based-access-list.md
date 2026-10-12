# Time Based Access-List

![Network Topology](./topology-time-based-access-list.jpg)

## Scenario

As the owner of a large swiss watch company you would like to make sure your employees are unable to browse the Internet during working hours. Time is money so it's time to find a solution...

## Goal

* All IP addresses have been configured for you, look at the topology picture for the IP addresses.
* OSPF has been configured for full connectivity.
* Configure router Tube so users are unable to access the HTTP server on weekdays between 9:00 - 17:00.

## Topology

## Video Solution

[YouTube Video Solution](http://www.youtube.com/watch?v=MHZ5Mh9nzM8)

## GNS3 2.2.56.1

Import [time-based-acl-startup-configs IOU.gns3project](time-based-acl-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `time-based-acl-startup-configs.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Stem | FastEthernet0/0 | Ethernet0/0 |
| Stem | FastEthernet0/1 | Ethernet0/1 |
| Tube | FastEthernet0/0 | Ethernet0/0 |
| Tube | FastEthernet0/1 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.
