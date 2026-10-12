# RSVP Subnetwork Bandwidth Manager (SBM)

## Scenario

You are one of the member of a underground organization with special abilities. Your ability is being able to take the form of an IP packet and work your way through the network with your mind. You want to ensure some of the traffic streams are able to make a reservation in the network to ensure there is enough bandwidth.

## Goal

* All IP addresses have been preconfigured for you.
* OSPF has been preconfigure for full connectivity.
* Configure the link between router Mystique and Beast with a bandwidth of 256Kbps.
* Enable RSVP on all interfaces in the network. Ensure RSVP can use the highest bandwidth on the link between router Mystique and Beast but a single flow should have a maximum of 96Kbps.
* Configure router Magneto as the Designated Subnetwork Bandwidth Manager.
* Configure 512KBps for RSVP flows for network 192.168.123.0 /24.
* Configure router Magneto so it tells router Xavier and Mystique not to send more than 70Kbyte/sec for non-RSVP traffic.
* You can test your configuration by making reservations from router Xavier and Magneto.

## GNS3 2.2.56.1

Import [RSVP Subnetwork Bandwidth Manager (SBM) IOU.gns3project](RSVP%20Subnetwork%20Bandwidth%20Manager%20%28SBM%29%20IOU.gns3project) using **File > Import portable project**. To open `RSVP Subnetwork Bandwidth Manager (SBM).gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Beast | FastEthernet0/0 | Ethernet0/0 |
| Magneto | FastEthernet0/0 | Ethernet0/0 |
| Mystique | FastEthernet0/0 | Ethernet0/0 |
| Mystique | FastEthernet1/0 | Ethernet0/1 |
| Xavier | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-rsvp-subnetwork-bandwidth-manager-sbm.png)
