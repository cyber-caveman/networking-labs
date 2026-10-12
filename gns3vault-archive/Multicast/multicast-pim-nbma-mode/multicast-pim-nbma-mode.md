# Multicast PIM NBMA Mode

![Network Topology](./topology-multicast-pim-nbma-mode.jpg)

## Scenario

As a full-time IT instructor at a high school you are always busy with innovative ideas. The school network is pretty old and has a frame-relay network, your idea is to stream old school cartoon videos on the network but you are running into some problems when you configure multicast on this network...Do you think you can fix it or will one of the students need to help you?

## Goal

- Frame-relay has been configured as following:
  - Router Pooky will be the HUB
  - Router Odie and Arlene will be the SPOKE routers
  - Router Pooky (DLCI 402) ↔ Router Odie (DLCI 204)
  - Router Pooky (DLCI 403) ↔ Router Arlene (DLCI 304)

- Configure EIGRP on all routers, achieve full connectivity. Fix any problems that the frame-relay setup might cause to your EIGRP configuration.
- Configure PIM sparse multicast mode on all your routers.
- Configure router Arbuckle to be Rendezvous Point (RP) for this network, use the loopback0 interface.
- Configure router Arbuckle to be Mapping Agent (MP) for this network, use the loopback0 interface.
- Configure router Arlene to join the following multicast group: 224.1.1.1
- Start a ping from router Arbuckle to the multicast group address 224.1.1.1 to generate traffic, make sure you get a response.
- Start a ping from router Garfield to the multicast group address 224.1.1.1, make sure you get a response from router Arlene.

## GNS3 2.2.56.1

Import [multicast-pim-nbma-mode-startup-configs IOU.gns3project](multicast-pim-nbma-mode-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `multicast-pim-nbma-mode-startup-configs.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Frame Relay switching routers retain Dynamips and the available C3640 appliance, with device-specific config packaging. Their source configuration text is preserved.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Arbuckle | FastEthernet0/0 | Ethernet0/0 |
| Arlene | Serial0/0 | Serial4/0 |
| Arlene | Serial0/1 | Serial4/1 |
| Arlene | Serial0/2 | Serial4/2 |
| Arlene | Serial0/3 | Serial4/3 |
| FRSW | Serial0/0 | Serial0/0 |
| FRSW | Serial0/1 | Serial0/1 |
| FRSW | Serial0/2 | Serial0/2 |
| FRSW | Serial0/3 | Serial0/3 |
| Garfield | FastEthernet0/0 | Ethernet0/0 |
| Odie | FastEthernet1/0 | Ethernet0/0 |
| Odie | Serial0/0 | Serial4/0 |
| Odie | Serial0/1 | Serial4/1 |
| Odie | Serial0/2 | Serial4/2 |
| Odie | Serial0/3 | Serial4/3 |
| Pooky | FastEthernet1/0 | Ethernet0/0 |
| Pooky | Serial0/0 | Serial4/0 |
| Pooky | Serial0/1 | Serial4/1 |
| Pooky | Serial0/2 | Serial4/2 |
| Pooky | Serial0/3 | Serial4/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

## Video Solution

http://www.youtube.com/watch?v=jBNzfDa5rXk
