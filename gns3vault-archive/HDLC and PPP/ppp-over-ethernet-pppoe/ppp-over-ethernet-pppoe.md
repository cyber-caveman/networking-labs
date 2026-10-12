# PPP over Ethernet (PPPOE)

![Network Topology](./topology-ppp-over-ethernet-pppoe.jpg)

## Scenario

You are working for a small company as a network engineer and currently you are still using a dial-up modem for Internet access. The company will upgrade the Internet access to a DSL connection and your service provider promised they will send you a Cisco 800 series router so you can configure it already for PPPoE. The problem is you never configured PPPoE before so it's time to upgrade your skills!

## Goals

- Do not configure any IP address on the Fast Ethernet interfaces.
- Router Artemis will be the PPPoE server (to emulate the service provider)
- Configure a DHCP pool on Router Artemis for the PPP connection, use the 192.168.12.0 subnet.
- Configure Router Artemis as a PPPoE server using the DHCP pool you just created. Use a Virtual-Template and configure the 192.168.12.2 IP address on this router.
- Router Poseidon should get IP address 192.168.12.1 from the PPPoE server.
- Configure Router Poseidon as the PPPoE Client.
- Your end result should be a working PPPoE session and Router Poseidon should get an IP address from DHCP.
- When your PPPoE connection is working, configure CHAP authentication:
  - Username: Poseidon
  - Password: VAULT
- Optional: Configure Router Artemis so PPPoE clients cannot initiate more than 5 sessions within 1 minute for 10 minutes.

## GNS3 2.2.56.1

Import [pppoe-startup-configs IOU.gns3project](pppoe-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `pppoe-startup-configs.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Poseidon | FastEthernet0/0 | Ethernet0/0 |
| Artemis | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

## Video Solution

[YouTube: PPP over Ethernet (PPPoE) Configuration](http://www.youtube.com/watch?v=vaWXeZHFXvI)
