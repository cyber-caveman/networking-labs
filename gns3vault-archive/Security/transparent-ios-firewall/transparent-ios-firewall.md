# Transparent IOS Firewall

## Scenario

You are part of the security team for the Rotterdam Harbor located in The Netherlands. One of your firewalls has crashed and due to decreased IT budgets you don't have any spare firewalls around. You do have a spare router that you could use so you decide to turn it into a transparent firewall. Hopefully everything will be OK and your boss doesn't send you to null0...

## Goal

- All IP addresses have been configured for you.
- Configure router Haven as a transparent firewall. You will need the bridge function to achieve this.
- Use network 192.168.13.0 /24 so router Harbor and Terminal are in the same subnet.
- Ensure router Harbor can reach router Terminal by using TELNET or HTTP, all other traffic should be dropped.
- Ensure router Harbor and Terminal are unable to communicate using IPv6.

## GNS3 2.2.56.1

Import [IOS Transparent Firewall IOU.gns3project](IOS%20Transparent%20Firewall%20IOU.gns3project) using **File > Import portable project**. To open `IOS Transparent Firewall.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Harbor | FastEthernet0/0 | Ethernet0/0 |
| Harbor | FastEthernet0/1 | Ethernet0/1 |
| Haven | FastEthernet0/0 | Ethernet0/0 |
| Haven | FastEthernet0/1 | Ethernet0/1 |
| Terminal | FastEthernet0/0 | Ethernet0/0 |
| Terminal | FastEthernet0/1 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-transparent-ios-firewall.png)

## Video Solution

http://www.youtube.com/watch?v=KeFPJInD3TQ
