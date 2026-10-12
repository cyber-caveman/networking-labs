# IPv6 Autoconfiguration

## Scenario

You are working as the network engineer for an Asian based company and responsible for the deployment of IPv6. You heard some good things about this new protocol and are interested in the new autoconfiguration feature, let's see if you can configure this.

## Goal

* Configure the unique local address FC00:12:0::1/64 on router Red's f0/0 interface.
* Configure an additional local address FC00:21:0::1/64 on router Red's f0/0 interface.
* Configure router Red to broadcast both prefixes using ICMPv6 Neighbor Discovery Router Advertisements (ND RA) but make sure only FC00:12::/64 is used for autoconfiguration.
* Configure both prefixes so the valid and prefered lifetime is 2 hours.
* Configure router Red to advertise itself as the default router every 20 seconds with a lifetime interval of 50 seconds.
* Configure router Blue to learn it's ipv6 address on the f0/0 interface and uses router Red as the default gateway.

## GNS3 2.2.56.1

Import [IPv6 Autoconfiguration IOU.gns3project](IPv6%20Autoconfiguration%20IOU.gns3project) using **File > Import portable project**. To open `IPv6 Autoconfiguration.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Blue | FastEthernet0/0 | Ethernet0/0 |
| Red | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-ipv6-autoconfiguration.png)

## Video Solution

[Video Solution](http://www.youtube.com/watch?v=_cVYVAmsTWE)
