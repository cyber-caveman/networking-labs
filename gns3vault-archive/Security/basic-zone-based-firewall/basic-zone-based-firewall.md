# Basic Zone Based Firewall

![Network Topology](./topology-basic-zone-based-firewall.jpg)

## Scenario

Being a full-time Cisco Network Engineer you decide to implement a new router at your home network. You heard good stories about Zone Based Firewalls so you decide to beef up your home security. Let's see what you can do...

## Goal

* All IP addresses have been configured for you, every router has a loopback interface:
  * Router LAN: L0: 1.1.1.1 /24
  * Router FIREWALL: L0: 2.2.2.2 /24
  * Router INTERNET: L0: 3.3.3.3 /24 and L1: 33.33.33.33 /24

* Static routes have been configured for you, there is full connectivity between the routers.

* Router INTERNET has the following services configured: SSH, TELNET, DNS, HTTP and HTTPS.

* Router FIREWALL has the following services configured: SSH and TELNET.

* Username: gns3vault

* Password: gns3vault

* Create 2 security zones called "LAN" and "INTERNET" on router FIREWALL.

* Place the corresponding interfaces into the correct zones.

* Create the correct class-map, policy-map and zone-pair so traffic from LAN to INTERNET is allowed, including the return traffic.

* Traffic from INTERNET to LAN should be blocked.

* Increase security by only allowing HTTP, ICMP and HTTPS traffic from LAN to INTERNET.

* Test this by using telnet from router LAN to router INTERNET, this should be blocked.

The security between your LAN and the INTERNET is looking good, but users from the LAN are still able to telnet or ssh into your Firewall. Even worse, people from the Internet can telnet or ssh into your firewall as well! Time to protect your firewall...

* Connections from the INTERNET should only be able to ping to router FIREWALL. Use "Zone Self" to achieve this.

* Users from the LAN should only be able to SSH into router FIREWALL, Telnet should be blocked. Use "Zone Self" to achieve this.

## GNS3 2.2.56.1

Import [basic-zone-based-firewall IOU.gns3project](basic-zone-based-firewall%20IOU.gns3project) using **File > Import portable project**. To open `basic-zone-based-firewall.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| LAN | FastEthernet0/0 | Ethernet0/0 |
| LAN | FastEthernet0/1 | Ethernet0/1 |
| FIREWALL | FastEthernet0/0 | Ethernet0/0 |
| FIREWALL | FastEthernet0/1 | Ethernet0/1 |
| INTERNET | FastEthernet0/0 | Ethernet0/0 |
| INTERNET | FastEthernet0/1 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

## Video Solution

[YouTube Video Solution](http://www.youtube.com/watch?v=1LyBonrz9yc)
