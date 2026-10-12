# QoS Hold-Queue and TX-Ring

## Scenario

As a famous adventurer you are well known for your discoveries. Every time you make an archaeological treasure you send the acquired information to your father's router. His router is an older model and has problems keeping up with the incoming data. Let's see if your networking adventures are just as fun...

## Goal

* All IP addresses have been preconfigured for you.
* OSPF has been configured to ensure full reachibility.
* Configure router Henry's input software queue to 12 packets on fastethernet 0/0.
* Configure router Henry's output software queue to 24 packets on fastethernet 1/0.
* Configure router Henry's hardware queue to be 20 packets.
* Use the `show interfaces fastethernet 0/0 | include queue` command to check your configuration.
* Optional: test your configuration by using the ping command, `ping 192.168.23.3 repeat 99999 timeout 0 size 1500` from router Indiana. You can see the queue fill up on router Henry.

## GNS3 2.2.56.1

Import [hold-queue-startup-configs IOU.gns3project](hold-queue-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `hold-queue-startup-configs.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| INDIANA | FastEthernet0/0 | Ethernet0/0 |
| HENRY | FastEthernet0/0 | Ethernet0/0 |
| HENRY | FastEthernet1/0 | Ethernet0/1 |
| MARION | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-qos-hold-queue-and-tx-ring.png)

## Video Solution

http://www.youtube.com/watch?v=jBq7HX1c2Qo
