# IP Source Tracker

## Scenario

You are the security office for the national security team in the Netherlands. It seems your webserver is under attack but you are unsure where the attacker is located. You want to use a method to track down the source IP address from the attacker.

## Goals

* All IP addresses have been preconfigure for you.
* EIGRP has been configured for connectivity.
* Start a ping from the attacker to the webserver.
* Use the "source track" command to track down the attacker in your network.
* Send syslog messages every 2 minutes.

## GNS3 2.2.56.1

Import [IP Source Tracker IOU.gns3project](IP%20Source%20Tracker%20IOU.gns3project) using **File > Import portable project**. To open `IP Source Tracker.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Attacker | FastEthernet0/0 | Ethernet0/0 |
| Attacker | FastEthernet0/1 | Ethernet0/1 |
| Bashful | FastEthernet0/0 | Ethernet0/0 |
| Bashful | FastEthernet0/1 | Ethernet0/1 |
| Bashful | FastEthernet1/0 | Ethernet0/2 |
| Doc | FastEthernet0/0 | Ethernet0/0 |
| Doc | FastEthernet0/1 | Ethernet0/1 |
| Dopey | FastEthernet0/0 | Ethernet0/0 |
| Dopey | FastEthernet0/1 | Ethernet0/1 |
| Grumpy | FastEthernet0/0 | Ethernet0/0 |
| Grumpy | FastEthernet0/1 | Ethernet0/1 |
| Grumpy | FastEthernet1/0 | Ethernet0/2 |
| Happy | FastEthernet0/0 | Ethernet0/0 |
| Happy | FastEthernet0/1 | Ethernet0/1 |
| Happy | FastEthernet1/0 | Ethernet0/2 |
| Sleepy | FastEthernet0/0 | Ethernet0/0 |
| Sleepy | FastEthernet0/1 | Ethernet0/1 |
| Sneezy | FastEthernet0/0 | Ethernet0/0 |
| Sneezy | FastEthernet0/1 | Ethernet0/1 |
| Webserver | FastEthernet0/0 | Ethernet0/0 |
| Webserver | FastEthernet0/1 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-ip-source-tracker.png)

## Video Solution

[Watch on YouTube](http://www.youtube.com/watch?v=mvArYqcwpiI)
