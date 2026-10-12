# DNS Server

![Network Topology](./topology-dns-server.png)

## Scenario:

You are responsible for the network of a major international hotel organization. You make sure that all the guests can use the Internet services. One of the things you need to do is ensure DNS lookups can be done quickly without relying too much on external DNS servers. You decide to use one of your routers for the job...

## Goal:

- All IP addresses have been preconfigured for you.
- OSPF has been preconfigured for full connectivity.
- Configure router PRIMARY as the primary DNS server for domain "vault.local". This router should use hostname ns1.vault.local.
- Configure router SECONDARY as the secondary DNS server for domain "vault.local". This router should use hostname ns2.vault.local.
- Router CLIENT1 should be able to resolve the hostnames of the DNS servers.
- Router CLIENT1 should use both DNS servers by using round-robin.
- Router CLIENT2 should do DNS lookups by using CLIENT1.
- Configure a loopback0 interface on router CLIENT1 with IP address 3.3.3.3 /24.
- Configure the network so CLIENT1 responds with IP address 3.3.3.3 as a DNS response when the DNS servers are unreachable.

---

## GNS3 2.2.56.1

Import [DNS Server IOU.gns3project](DNS%20Server%20IOU.gns3project) using **File > Import portable project**. To open `DNS Server.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Client1 | FastEthernet0/0 | Ethernet0/0 |
| Client1 | FastEthernet1/0 | Ethernet0/1 |
| Client2 | FastEthernet0/0 | Ethernet0/0 |
| Primary | FastEthernet0/0 | Ethernet0/0 |
| Secondary | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology:

## Video Solution:

[Video on YouTube](http://www.youtube.com/watch?v=hMB5iRv_Kjk)
