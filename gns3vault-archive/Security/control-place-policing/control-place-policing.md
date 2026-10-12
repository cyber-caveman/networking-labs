# Control Plane Policing

![Network Topology](./topology-control-place-policing.png)

## Scenario:

You are the security office for the national security team in the Netherlands. Recently you did everything in order to protect the data plane of your routers. The only you haven't done yet is securing the control plane for your routers...

## Goals:

- All IP addresses have been preconfigure for you.
- EIGRP has been configured for connectivity.
- Use control plane policing to solve everything.
- Configure router Harbor so ARP traffic to the control plane is limited to 75 packets per second.
- Configure router Harbo so telnet traffic from router Terminal is dropped.

## GNS3 2.2.56.1

Import [Control Place Policing IOU.gns3project](Control%20Place%20Policing%20IOU.gns3project) using **File > Import portable project**. To open `Control Place Policing.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Harbor | FastEthernet0/0 | Ethernet0/0 |
| Haven | FastEthernet0/0 | Ethernet0/0 |
| Haven | FastEthernet1/0 | Ethernet0/1 |
| Terminal | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology:

## Video Solution:

http://www.youtube.com/watch?v=tsF1Pn6w7Ww
