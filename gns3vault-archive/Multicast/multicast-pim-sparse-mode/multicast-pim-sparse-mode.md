# Multicast PIM Sparse Mode

![Network Topology](./topology-multicast-pim-sparse-mode.jpg)

## Scenario

Being a big table tennis fan and professional network engineer you decide to enhance your company's network by adding Multicast. This way everyone can enjoy the latest video replays of your sports action. Multicast Dense might burden the network with too much multicast traffic so you decide to implement Multicast Sparse Mode, hopefully your boss won't find out...

## Goal

- All IP addresses have been preconfigured for you.
- Configure OSPF on all routers, advertise all networks. Achieve full connectivity.
- Configure sparse-mode multicast on all routers.
- Configure all routers manually so that router Pong is the Rendezvous Point (RP).
- Configure router VideoReceiver to join the multicast group 224.4.4.4 on its FastEthernet interface.
- Make sure you can ping the 224.4.4.4 group address from router VideoServer.

## GNS3 2.2.56.1

Import [multicast-pim-sparse-mode-startup-configs IOU.gns3project](multicast-pim-sparse-mode-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `multicast-pim-sparse-mode-startup-configs.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Ping | FastEthernet0/0 | Ethernet0/0 |
| Ping | FastEthernet1/0 | Ethernet0/1 |
| Pong | FastEthernet0/0 | Ethernet0/0 |
| Pong | FastEthernet1/0 | Ethernet0/1 |
| VideoReceiver | FastEthernet0/0 | Ethernet0/0 |
| VideoServer | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

## Video Solution

[Video Solution on YouTube](http://www.youtube.com/watch?v=uK43VRNrMd8)
