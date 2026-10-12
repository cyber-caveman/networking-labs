# AAA Authentication

## Scenario

As part of the security team you are always looking for ways to improve security within the company. You want to get rid of all the local vty/console logins within your network so you decide to setup a radius server. Routers should use the external radius server for authentication from now on...let's see if you can secure this one!

## Goal

* All IP addresses have been configured for you, look at the topology picture for the IP addresses.
* Configure router Fuzz so it uses the (fictional) radius server at IP address 192.168.23.3. Updates should be sourced from the loopback0 interface.
* Configure router Fuzz so console access uses a local username 'console' with password 'vault'.
* Configure router Fuzz so VTY access uses the radius server, when it fails it should switch to a local username 'telnet' with password 'unsafe'.
* Configure router Fuzz so everyone sees the message "ID required" when they try to login using AAA.

## Topology

![Network Topology](./topology-aaa-authentication.png)

## GNS3 2.2.56.1

Import [AAA Authentication IOU.gns3project](AAA%20Authentication%20IOU.gns3project) using **File > Import portable project**. To open `AAA Authentication.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Lock | FastEthernet0/0 | Ethernet0/0 |
| Fuzz | FastEthernet0/0 | Ethernet0/0 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.
