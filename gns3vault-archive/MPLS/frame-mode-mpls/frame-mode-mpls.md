# Frame Mode MPLS

![Network Topology](./topology-frame-mode-mpls.jpg)

## Scenario

You are working as a network engineer at an ISP called "StoryTellers" and until now you have been responsible for the Frame-Relay network of this service provider. Since MPLS is becoming more popular every day, you are being moved from the Frame-Relay team to the MPLS team...you do need to upgrade your skills though, so it's time to start with a basic MPLS lab and see what it's all about.

## Goal

- All IP addresses are preconfigured as specified in the topology picture.
- Configure EIGRP AS 100 and advertise all networks, ensure you have full reachability.
- Perform a traceroute from Router Gepetto to the Loopback0 interface of Pinoccio. Take a good look at this trace so you can compare it to the MPLS traceroute (hint: copy/paste this information into notepad).
- Configure MPLS on all physical interfaces, do NOT configure MPLS on the loopback interfaces.
- Use the "show mpls ldp bindings" command to check what labels are being used for all networks.
- Are these labels the same or different on all routers? why?
- Perform a traceroute from Router Gepetto to Pinoccio's Loopback0 interface, what is the difference compared to the traceroute you did before?

## GNS3 2.2.56.1

Import [frame-mode-mpls IOU.gns3project](frame-mode-mpls%20IOU.gns3project) using **File > Import portable project**. To open `frame-mode-mpls.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Gepetto | FastEthernet0/0 | Ethernet0/0 |
| Figaro | FastEthernet0/0 | Ethernet0/0 |
| Figaro | FastEthernet1/0 | Ethernet0/1 |
| Pinoccio | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

## Video Solution

http://www.youtube.com/watch?v=Kg5xfbl0h_c
