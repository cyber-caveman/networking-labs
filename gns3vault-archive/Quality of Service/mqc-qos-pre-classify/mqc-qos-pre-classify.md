# MQC Qos Pre-Classify

## Scenario

You work for a Dutch service provider offering connections to customers with QoS-guarantee. One of your customers wants you to create a tunnel interface but they are also using a number of applications that require low latency...let's see if you can build some high quality tunnels.

## Goal

- All IP addresses have been preconfigured for you.
- Configure a GRE tunnel between router Tallet and Marvin.
- Configure the network so traffic from the loopback0 interfaces on router Kenton and Finn are sent through the GRE tunnel interface.
- Configure a service-policy on router Tallet's F1/0 interface that gives 64kb priority to ICMP traffic.
- Configure a service-policy on router Marvin's F0/0 interface that gives 64kb priority to ICMP traffic.

## GNS3 2.2.56.1

Import [MQC QoS Pre-Classify IOU.gns3project](MQC%20QoS%20Pre-Classify%20IOU.gns3project) using **File > Import portable project**. To open `MQC QoS Pre-Classify.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Finn | FastEthernet0/0 | Ethernet0/0 |
| Kenton | FastEthernet0/0 | Ethernet0/0 |
| Marvin | FastEthernet0/0 | Ethernet0/0 |
| Marvin | FastEthernet1/0 | Ethernet0/1 |
| Ricky | FastEthernet0/0 | Ethernet0/0 |
| Ricky | FastEthernet1/0 | Ethernet0/1 |
| Tallet | FastEthernet0/0 | Ethernet0/0 |
| Tallet | FastEthernet1/0 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-mqc-qos-pre-classify.png)

## Video Solution

http://www.youtube.com/watch?v=ZQfeVKBnb-k
