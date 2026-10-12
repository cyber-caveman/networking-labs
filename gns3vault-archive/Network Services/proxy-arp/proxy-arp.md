# Proxy ARP

## Scenario

One of the trainees has configured your network and has assigned static IP addresses to all computer in the network. Unfortunately he made some errors and the computers are not able to reach each other. Think you can help him out?

## Goal

* All IPv4 addresses have been preconfigured for you.
* Ensure all hosts can communicate with each other without changing the IP addresses.
* What MAC address does router Medusa use to reach router Ladon or Poseidon?

## GNS3 2.2.56.1

Import [Proxy ARP IOU.gns3project](Proxy%20ARP%20IOU.gns3project) using **File > Import portable project**. To open `Proxy ARP.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Ceto | FastEthernet0/0 | Ethernet0/0 |
| Ladon | FastEthernet0/0 | Ethernet0/0 |
| Medusa | FastEthernet0/0 | Ethernet0/0 |
| Poseidon | FastEthernet0/0 | Ethernet0/0 |
| Proxy | FastEthernet0/0 | Ethernet0/0 |
| Proxy | FastEthernet1/0 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-proxy-arp.png)

## Video Solution

[http://www.youtube.com/watch?v=uU1iqR_r4qc](http://www.youtube.com/watch?v=uU1iqR_r4qc)
