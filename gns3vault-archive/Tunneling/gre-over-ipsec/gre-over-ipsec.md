# GRE over IPSEC

![Network Topology](./topology-gre-over-ipsec.jpg)

## Scenario

Your colleagues at "BigLabs" are very pleased with your performance so far…you managed to successfully configure the "Basic GRE" lab and the "Site-to-Site IPSEC VPN" lab. You managed to configure a GRE tunnel and encrypt it with IPSEC. Now your final task will be to configure an IPSEC tunnel and run GRE on top of it, let's see what you can do this time!

## Goal

- All IP addresses are preconfigured as specified in the topology picture.
- Router Godzilla and Nessie have the following loopback interfaces:
  - Godzilla: Loopback1: 11.11.11.11 /24
  - Nessie: Loopback1: 33.33.33.33 /24
- Configure EIGRP AS1 on all 3 routers, only advertise the 192.168.12.0 and 192.168.23.0 network, do not advertise the loopbacks.
- Ensure Router Godzilla and Nessie can ping each other.
- Configure a IPSEC tunnel between Router Godzilla and Nessie.
- Configure the 192.168.13.0 /24 network on the IPSEC tunnel:
  - Godzilla: 192.168.13.1
  - Nessie: 192.168.13.3
- Ensure you can ping the IP addresses that you configured on the tunnel interface.
- Configure static routes on router Godzilla and Nessie so they can reach each other's loopback1 interface through the Tunnel interface.
- Create an IKE Policy with the following parameters:
  - Authentication: pre-shared-key
  - Encryption: AES 256
  - Hashing: sha
  - DH: Group 5
  - Lifetime: 3600
  - The pre-shared-key should be "VAULT".
- Create an IPSEC Transform-set with the following parameters:
  - ESP (Encapsulating Security Payload)
  - Encryption: AES 256
  - Hashing: SHA-HMAC
- Create the correct policy profile to finish the IPSEC configuration.
- Verify the IPSEC configuration, you can use the following show/debug commands:
  - show crypto ipsec transform-set
  - show crypto map
  - show crypto ipsec sa
  - debug crypto isakmp

## GNS3 2.2.56.1

Import [gre-over-ipsec IOU.gns3project](gre-over-ipsec%20IOU.gns3project) using **File > Import portable project**. To open `gre-over-ipsec.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| KingKong | FastEthernet0/0 | Ethernet0/0 |
| KingKong | FastEthernet1/0 | Ethernet0/1 |
| Nessie | FastEthernet0/0 | Ethernet0/0 |
| Godzilla | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

## Video Solution

[YouTube Video](http://www.youtube.com/watch?v=aGisOZaXa08)
