# OSPF Summarization Troubleshooting

## OSPF Summarization Troubleshooting

## Scenario

Mystical Corporation is using OSPF within their autonomous system. Their network is configured using different areas which seems to be working fine. One of the network engineers configured a summary for area 0 but it seems it's not working, up to you to solve the problem.

## Goal

* All IP addresses have been preconfigured for you as specified in the topology picture.
* OSPF is preconfigured with the areas as specified in the topology picture.
* **Do not use show run**! (this will spoil the fun :) use the appropriate 'show' and 'debug' commands. This will teach you the skills needed to become a true troubleshooting master.
* Configure the network so you have full connectivity, make sure you use the areas as seen in the topology picture.
* Configure a summary on router Chimaera for the two loopback interfaces of router Cerberus. Ensure the summary is as specific as possible. The summary should show up as an interarea router, not as an external route.
* Ensure router Cyclops only sees the summary and not the specific routes.

## GNS3 2.2.56.1

Import [OSPF Summarization Troubleshooting IOU.gns3project](OSPF%20Summarization%20Troubleshooting%20IOU.gns3project) using **File > Import portable project**. To open `OSPF Summarization Troubleshooting.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Centaur | FastEthernet0/0 | Ethernet0/0 |
| Centaur | FastEthernet1/0 | Ethernet0/1 |
| Cerberus | FastEthernet0/0 | Ethernet0/0 |
| Chimaera | FastEthernet0/0 | Ethernet0/0 |
| Chimaera | FastEthernet1/0 | Ethernet0/1 |
| Cyclops | FastEthernet0/0 | Ethernet0/0 |
| Cyclops | FastEthernet1/0 | Ethernet0/1 |
| Poseidon | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-ospf-summarization-troubleshooting.png)

## Video Solution

[OSPF Summarization Troubleshooting Video](http://www.youtube.com/watch?v=pIVOJqnawzQ)
