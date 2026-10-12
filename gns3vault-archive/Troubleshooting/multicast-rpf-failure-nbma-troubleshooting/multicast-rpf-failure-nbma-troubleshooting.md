# Multicast RPF Failure NBMA Troubleshooting

## Scenario

You are responsible for the frame relay and multicast configuration within the network. You use a lot of hub and spoke topologies and up to now you haven't seen any problems. Yesterday one of your customers called claiming they are having some problems. There is a videostation behind one of the spoke routers streaming video using multicast. It seems one of the other spoke routers is unable to receive this stream...let's see what you can do.

## Goal

- All IP addresses have been preconfigured for you as specified in the topology picture.
- OSPF is preconfigured for full connectivity.
- **Do not use show run**! (this will spoil the fun :) use the appropiate 'show' and 'debug' commands. This will teach you the skills needed to become a true troubleshooting master.
- Start a ping on router SpokeA to IP address 224.9.9.9 to generate multicast traffic.
- Configure the network so router Receiver can receive this multicast traffic.
- You are not allowed to make any changes to the frame-relay network or change the PIM mode.

## GNS3 2.2.56.1

Import [Multicast RPF Failure NBMA IOU.gns3project](Multicast%20RPF%20Failure%20NBMA%20IOU.gns3project) using **File > Import portable project**. To open `Multicast RPF Failure NBMA.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| HUB | Serial0/0 | Serial4/0 |
| HUB | Serial0/1 | Serial4/1 |
| HUB | Serial0/2 | Serial4/2 |
| HUB | Serial0/3 | Serial4/3 |
| Receiver | FastEthernet0/0 | Ethernet0/0 |
| SpokeA | Serial0/0 | Serial4/0 |
| SpokeA | Serial0/1 | Serial4/1 |
| SpokeA | Serial0/2 | Serial4/2 |
| SpokeA | Serial0/3 | Serial4/3 |
| SpokeB | FastEthernet1/0 | Ethernet0/0 |
| SpokeB | Serial0/0 | Serial4/0 |
| SpokeB | Serial0/1 | Serial4/1 |
| SpokeB | Serial0/2 | Serial4/2 |
| SpokeB | Serial0/3 | Serial4/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-multicast-rpf-failure-nbma-troubleshooting.png)

## Video Solution

[Video: Multicast RPF Failure NBMA Troubleshooting](http://www.youtube.com/watch?v=KrXrh46Cqp4)
