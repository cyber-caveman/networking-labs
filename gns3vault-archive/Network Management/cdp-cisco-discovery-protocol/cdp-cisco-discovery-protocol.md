# CDP (Cisco Discovery Protocol)

## Scenario

Since the average life expectancy of a spartian warrior isn't very promising, some of them decided to switch careers and become network engineer. The spartian engineers really enjoy CDP (Cisco Discovery Protocol) but they would like to tune some settings to their liking.

## Goal

- All IP addresses have been preconfigured for you (but you won't really need them).
- Make sure there are no CDP packets sent between router Gorgo and Theron.
- Create a loopback0 interface on router Gorgo with IP address 1.1.1.1 /24.
- Configure router Gorgo so the IP address of the loopback0 interface will show up in CDP advertisements.
- Configure all routers to send CDP packets every 5 seconds.
- Configure router Leonidas so it tells its neighbors to keep CDP packets for 20 seconds.
- Configure all routers so CDP doesn't log any duplex mismatch errors.

## GNS3 2.2.56.1

Import [CDP IOU.gns3project](CDP%20IOU.gns3project) using **File > Import portable project**. To open `CDP.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Is | FastEthernet0/0 | Ethernet0/0 |
| Is | FastEthernet1/0 | Ethernet0/1 |
| Sparta | FastEthernet0/0 | Ethernet0/0 |
| Sparta | FastEthernet1/0 | Ethernet0/1 |
| This | FastEthernet0/0 | Ethernet0/0 |
| This | FastEthernet1/0 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-cdp-cisco-discovery-protocol.png)

## Video Solution

[CDP Video Solution on YouTube](http://www.youtube.com/watch?v=Zy7UEREcolQ)
