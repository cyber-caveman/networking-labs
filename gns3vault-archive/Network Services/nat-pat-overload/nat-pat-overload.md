# NAT PAT Overload

## Scenario

Emma and Alice are in trouble. They just got a new Internet connection but they forgot to mention to the Internet provider that they required two public IP addresses so they both can access the Internet at the same time. Can you help the damsels in distress?

## Goal

- All IPv4 addresses have been preconfigured for you.
- IP Routing has been disabled and a default gateway is configured on router Emma, Alice and WWW.
- Configure PAT so when router Emma or Alice sends an IP packet to router WWW the source address is translated to the IP address on the F0/0 interface of router PAT.

## GNS3 2.2.56.1

Import [nat-pat-overload IOU.gns3project](nat-pat-overload%20IOU.gns3project) using **File > Import portable project**. To open `nat-pat-overload.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| WWW | FastEthernet0/0 | Ethernet0/0 |
| PAT | FastEthernet0/0 | Ethernet0/0 |
| PAT | FastEthernet1/0 | Ethernet0/1 |
| Alice | FastEthernet0/0 | Ethernet0/0 |
| Alice | FastEthernet1/0 | Ethernet0/1 |
| Emma | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-nat-pat-overload.png)

## Video Solution

http://www.youtube.com/watch?v=jCr24iGIqko
