# Access-List Logging

## Scenario

The local boyscout needs your help as a network engineer. They want to make sure everytime their router receives an OSPF packet this will be logged on their local router. Think you can help them out?

## Goal

* All IP addresses have been preconfigured for you.
* OSPF has been configured for you.
* Configure router Scout so every OSPF packet that is received on the interface will be logged. Use an access-list for this.
* Your log file should be updated every 4 packets.
* Make sure you log the MAC address of the device sending the OSPF packet.

## GNS3 2.2.56.1

Import [Access-List Logging IOU.gns3project](Access-List%20Logging%20IOU.gns3project) using **File > Import portable project**. To open `Access-List Logging.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Scout | FastEthernet0/0 | Ethernet0/0 |
| Watch | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-access-list-logging.png)

## Video Solution

http://www.youtube.com/watch?v=qlU9U3kZXgI
