# Exec Alias

## Scenario

You run a local petshop located in The Netherlands and the network in use has been configured for you. Your colleagues like routers but they are not used to working with the command-line. You decide to help them by using exec aliases for some of the commands they require most.

## Goal

* All IP addresses have been preconfigured for you.
* OSPF has been configured for connectivity.
* Typing "shr" should show the routing table.
* Typing "sho" should show the OSPF database.
* Typing "i l0" in global configuration mode should switch to the configuration of the loopback0 interface.
* Typing "newsa VAULT" in global configuration mode should create a new standard access-list called VAULT.

## GNS3 2.2.56.1

Import [Exec Alias IOU.gns3project](Exec%20Alias%20IOU.gns3project) using **File > Import portable project**. To open `Exec Alias.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Fred | FastEthernet0/0 | Ethernet0/0 |
| Fred | FastEthernet1/0 | Ethernet0/1 |
| Hans | FastEthernet0/0 | Ethernet0/0 |
| Hans | FastEthernet1/0 | Ethernet0/1 |
| Norris | FastEthernet0/0 | Ethernet0/0 |
| Norris | FastEthernet1/0 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-exec-alias.png)
