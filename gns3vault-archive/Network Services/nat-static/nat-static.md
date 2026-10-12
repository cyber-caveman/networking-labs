# NAT Static

![Network Topology](./topology-nat-static.jpg)

## Scenario

As one of the network engineers for a small company you are responsible for all network operations. One of the branch offices has a single host PC that needs access to a server located on the internet. You only have private IP addresses for your internal network so you need to configure network address translation (NAT). Since there is only a single host a static NAT will be sufficient.

## Goal

- IP addresses have been preconfigured as specified in the topology picture.
- Create a static NAT configuration on router NAT to translate the 192.168.12.1 IP address into the 192.168.23.2 IP address.
- You are not allowed to translate any port numbers.

## GNS3 2.2.56.1

Import [nat-static-startup-configs IOU.gns3project](nat-static-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `nat-static-startup-configs.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Host | FastEthernet0/0 | Ethernet0/0 |
| NAT | FastEthernet0/0 | Ethernet0/0 |
| NAT | FastEthernet1/0 | Ethernet0/1 |
| Server | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

## Video Solution

[Video: NAT Static Configuration](http://www.youtube.com/watch?v=daCFd29KwxQ)
