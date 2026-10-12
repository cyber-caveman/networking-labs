# EIGRP CCNA 1

![Network Topology](./topology-eigrp-for-ccna-1.png)

## Scenario:

Tillywood is where all the famous blockbuster movies are created in Tilburg, The Netherlands. This year there is a convention and all big star actors will be there. Cisco is promoting the event and thus you are going to use EIGRP as the routing protocol of choice to get connectivity. Since you are close to passing your CCNA exam this should be no problem for you...get to work!

## Goal:

* All IPv4 addresses have been preconfigured for you.
* Each router has a loopback0 interface.
* Configure EIGRP AS 1 on the frame-relay network connecting router Bates, Bond and Corleone. Advertise the loopback0 interfaces.
* You notice that router Bond and Corleone do not see each others loopback interfaces in the routing table. Configure router Bates to solve this.
* Configure EIGRP AS 1 on both fastethernet links connecting router Bates and oHara.
* Change the bandwidth on the fastethernet 1/0 interfaces so only fastethernet 0/0 is used for successor routes.
* Configure EIGRP AS 1 on router Dobbs and Corleone.
* Make sure you disable auto-summary for EIGRP AS 1.
* At this point you should have full connectivity for all networks and loopback0 interfaces.
* Create a summary on interface serial0/0 of router Dobbs so it advertises 5.5.0.0 /16 with an administrative distance of 85.
* Change the EIGRP K-Values so only delay will be used as a metric.
* Ensure router Bates can use the frame-relay network as a feasible successor route to network 4.4.4.0 /24.
* Make sure you see this feasible successor route not only in the topology table but also in the routing table.
* Enable authentication between router Dobbs and Corleone. Use a keychain called "VAULT" and password "LABS".

## GNS3 2.2.56.1

Import [eigrp-ccna-1-startup-configs IOU.gns3project](eigrp-ccna-1-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `eigrp-ccna-1-startup-configs.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Bates | FastEthernet0/0 | Ethernet0/0 |
| Bates | FastEthernet1/0 | Ethernet0/1 |
| Bates | Serial2/0 | Serial4/0 |
| Bates | Serial2/1 | Serial4/1 |
| Bates | Serial2/2 | Serial4/2 |
| Bates | Serial2/3 | Serial4/3 |
| Bond | Serial0/0 | Serial4/0 |
| Bond | Serial0/1 | Serial4/1 |
| Bond | Serial0/2 | Serial4/2 |
| Bond | Serial0/3 | Serial4/3 |
| Corleone | Serial0/0 | Serial4/0 |
| Corleone | Serial0/1 | Serial4/1 |
| Corleone | Serial0/2 | Serial4/2 |
| Corleone | Serial0/3 | Serial4/3 |
| Dobbs | Serial0/0 | Serial4/0 |
| Dobbs | Serial0/1 | Serial4/1 |
| Dobbs | Serial0/2 | Serial4/2 |
| Dobbs | Serial0/3 | Serial4/3 |
| oHara | FastEthernet0/0 | Ethernet0/0 |
| oHara | FastEthernet1/0 | Ethernet0/1 |
| oHara | Serial2/0 | Serial4/0 |
| oHara | Serial2/1 | Serial4/1 |
| oHara | Serial2/2 | Serial4/2 |
| oHara | Serial2/3 | Serial4/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology:

## Video Solution:

http://www.youtube.com/watch?v=BbZnd5PyT5I
