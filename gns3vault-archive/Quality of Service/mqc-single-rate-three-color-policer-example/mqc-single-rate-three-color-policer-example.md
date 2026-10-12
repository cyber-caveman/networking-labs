# MQC Single Rate Three-Color Policer Example

## Scenario

You work for a large provider in India as a senior network engineer specialized in Quality of Service. All the customers of the service provider have an Ethernet connection which is capable of delivering speeds up to 10Mbps. The ISP has different subscriptions and you need to enforce that customers only get what they are paying for...when traffic exceeds a certain rate you need to police it!

## Goal

* All IP addresses have been preconfigured for you.
* Configure router Line to police all TELNET traffic heading for router Jack with the following configuration:
* When traffic is less than 64Kbps the DSCP value should be set to AF21.
* When traffic exceeds 64Kbps the DSCP value should be set to 0.
* Traffic that is violating should be dropped.

## GNS3 2.2.56.1

Import [MQCSingleRate3colorPolicer IOU.gns3project](MQCSingleRate3colorPolicer%20IOU.gns3project) using **File > Import portable project**. To open `MQCSingleRate3colorPolicer.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Frank | FastEthernet0/0 | Ethernet0/0 |
| Jack | FastEthernet0/0 | Ethernet0/0 |
| Line | FastEthernet1/0 | Ethernet0/0 |
| Line | Serial0/0 | Serial4/0 |
| Line | Serial0/1 | Serial4/1 |
| Line | Serial0/2 | Serial4/2 |
| Line | Serial0/3 | Serial4/3 |
| Prio | FastEthernet1/0 | Ethernet0/0 |
| Prio | Serial0/0 | Serial4/0 |
| Prio | Serial0/1 | Serial4/1 |
| Prio | Serial0/2 | Serial4/2 |
| Prio | Serial0/3 | Serial4/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-mqc-single-rate-three-color-policer-example.png)

## Video Solution

http://www.youtube.com/watch?v=uBqalWETZ0M
