# Static Routing Beginners Lab

![Network Topology](./topology-static-routing-beginners-lab.jpg)

## Scenario

You are working as a networking specialist at a company called "Networks4All". One of their customers has 2 dedicated links to connect their New York site to the Washington site. You are not allowed to use routing protocols because they are paying for every single bit that's sent on these links. You need to do use static routing to get the job done and keep the customer happy.

## Goal

* All IP addresses are preconfigured as shown in the topology picture.
* There is a Loopback0 interface on the Washington router: IP Address 2.2.2.2/30.
* There is a Loopback0 interface on the New York router: IP Address 1.1.1.1/30.
* New York: create a static route pointing to the Loopback0 network on Washington, traffic should pass the 192.168.1.0 network.
* Washington: create a default route pointing to the Loopback0 network on New York, traffic should pass the 192.168.2.0 network. In the routing table you should see a 0.0.0.0 entry.
* New York: create a backup static route pointing to the Loopback0 network on Washington, administrative distance should be 100.
* Washington: change the default route so it stays in the routing table even when the interface goes down.

## GNS3 2.2.56.1

Import [static-routing-beginners-lab-startup-configs IOU.gns3project](static-routing-beginners-lab-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `static-routing-beginners-lab-startup-configs.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| NewYork | Serial0/0 | Serial4/0 |
| NewYork | Serial0/1 | Serial4/1 |
| NewYork | Serial0/2 | Serial4/2 |
| NewYork | Serial0/3 | Serial4/3 |
| Washington | Serial0/0 | Serial4/0 |
| Washington | Serial0/1 | Serial4/1 |
| Washington | Serial0/2 | Serial4/2 |
| Washington | Serial0/3 | Serial4/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

## Video Solution

[Video Tutorial](http://www.youtube.com/watch?v=XQcF8yMIwkw)
