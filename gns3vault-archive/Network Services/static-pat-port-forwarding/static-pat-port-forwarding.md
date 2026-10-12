# Static PAT (Port Forwarding)

## Scenario

You are a trainee for a large international website covering a wide range of topics on automobiles. You are using NAT and PAT for connectivity to the Internet but you also have a number of hosts on your internal network. You need to make sure that the Webserver and Mailserver are reachable from the Internet.

## Goal

- All IP addresses have been preconfigured for you.
- Configure router PAT so all internal devices are able to reach the Internet.
- Configure router PAT so the Web- and Mailserver are reachable from the Internet.
- Ensure router Internet doesn't know about the 192.168.123.0 /24 network.

## GNS3 2.2.56.1

Import [Static PAT IOU.gns3project](Static%20PAT%20IOU.gns3project) using **File > Import portable project**. To open `Static PAT.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Internet | FastEthernet0/0 | Ethernet0/0 |
| Mail | FastEthernet0/0 | Ethernet0/0 |
| PAT | FastEthernet0/0 | Ethernet0/0 |
| PAT | FastEthernet1/0 | Ethernet0/1 |
| Rob | FastEthernet0/0 | Ethernet0/0 |
| WWW | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-static-pat-port-forwarding.png)

## Video Solution

[Video Solution on YouTube](http://www.youtube.com/watch?v=bptbBNdWCrY)
