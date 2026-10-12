# IPv6 ISATAP

## Scenario

You are working as the network engineer for an Asian based company and responsible for the deployment of IPv6. You heard some good things about this new protocol and are interested in the new autoconfiguration feature, let's see if you can configure this.

## Goal

* All IPv4 addresses have been preconfigured for you.
* OSPFv2 has been configured to ensure full connectivity for IPv4.
* Configure a tunnel0 interface on router ISATAPRouter and set mode to ISATAP.
* Configure IPv6 address 2001::1/64 on the tunnel0 interface and use EUI-64 for the last 64 bits.
* Make sure router advertisements are sent through the tunnel0 interface.
* Make sure source updates are sent from the Loopback0 interface on router ISATAPRouter.
* Configure a tunnel0 interface on router ISATAPClient and set the correct tunnel mode.
* Source updates should be sent from the Fastethernet0/0 interface, Destination should be Loopback0 of router ISATAPRouter.
* Ensure the IPv6 address on router ISATAPClient will be automatically configured.

## GNS3 2.2.56.1

Import [IPv6 ISATAP IOU.gns3project](IPv6%20ISATAP%20IOU.gns3project) using **File > Import portable project**. To open `IPv6 ISATAP.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| ISATAPClient | FastEthernet0/0 | Ethernet0/0 |
| ISATAPRouter | FastEthernet0/0 | Ethernet0/0 |
| MiddleMan | FastEthernet0/0 | Ethernet0/0 |
| MiddleMan | FastEthernet1/0 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-ipv6-isatap.png)

## Video Solution

[Video Solution on YouTube](http://www.youtube.com/watch?v=HLwgzF7zpgU)
