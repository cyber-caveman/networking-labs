# IPv6 EIGRP

## Scenario

After waking up from cryosleep the year appears to be 2020 and there is not a single IPv4 address left on the planet. The last thing you remember are the stories about the end of IPv4 and the migration plans for IPv6...now it seems this is all reality! It's up to you to configure EIGRP for IPv6 and make the network operational...resistance is futile ;)

## Goal

- You are not allowed to use IPv4 addresses.
- You are not allowed to use any IPv6 global unicast addresses except the ones on the loopback interfaces.
- Use the MAC-address for the last 64 bits of the IPv6 addresses required for the FastEthernet links.
- Configure EIGRP AS 6 and achieve full connectivity between the networks on the loopback interfaces.
- Configure the FastEthernet 0/0 interface of router Romulan so EIGRP can use up to 75% of available bandwidth.
- Configure EIGRP authentication between router Borg and Klingon. Use password GNS3VAULT.
- Change the EIGRP hello interval to 9 seconds between router Vulcan and Borg.

## Background

## GNS3 2.2.56.1

Import [ipv6-eigrp-startup-configs IOU.gns3project](ipv6-eigrp-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `ipv6-eigrp-startup-configs.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Borg | FastEthernet0/0 | Ethernet0/0 |
| Borg | FastEthernet1/0 | Ethernet0/1 |
| Borg | FastEthernet0/1 | Ethernet0/2 |
| Klingon | FastEthernet0/0 | Ethernet0/0 |
| Klingon | FastEthernet1/0 | Ethernet0/1 |
| Klingon | FastEthernet0/1 | Ethernet0/2 |
| Romulan | FastEthernet0/0 | Ethernet0/0 |
| Romulan | FastEthernet1/0 | Ethernet0/1 |
| Romulan | FastEthernet0/1 | Ethernet0/2 |
| Vulcan | FastEthernet0/0 | Ethernet0/0 |
| Vulcan | FastEthernet1/0 | Ethernet0/1 |
| Vulcan | FastEthernet0/1 | Ethernet0/2 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-ipv6-eigrp.png)

## Video Solution

[Watch on YouTube](http://www.youtube.com/watch?v=Tn-ZCa1uhZI)
