# RIP Advanced

![Network Topology](./topology-rip-advanced.jpg)

## Scenario

You are a freelance network engineer and one of your customers has an old network based on the RIP routing protocol. This network needs some tuning so it's time to use some more advanced RIP tricks.

## Goal

- All IP addresses are preconfigured as specified in the topology picture.
- Configure RIP version 2 on all routers, make sure it does no summarization by itself.
- Advertise all networks in RIP, including the loopback interfaces. Achieve full connectivity.
- After using a debug on Router Fred, you notice that RIP is sending updates towards the loopback interfaces. Disable this.
- The link between Router Wilma and Betty is not allowed to send RIP traffic by using broadcast or multicast.
- When you start a ping from Router Wilma to 4.4.4.4 you notice the traffic is being sent down the slow serial-link, change the RIP configuration on Router Betty so the Fast Ethernet links will be used. You are not allowed to shutdown the serial link.
- Create a new loopback10 interface on router Betty, use IP address 44.44.44.44 /24
- Change the configuration on Router Fred so pings to 44.44.44.44 will be sent only through the serial link, not through the link towards Barney.
- Change the configuration on Router Wilma and Betty so only triggered updates are sent on the serial link.
- Configure Router Wilma so RIP V1 updates are sent towards Fred. You are not allowed to change the RIP version on Fred.
- Configure authentication between Router Barney and Betty:
  - key-chain: VAULT
  - key-id: 1
  - key-string: FREE
- Create 4 loopback interfaces on router Betty:
  - Loopback1: 172.16.0.1 /24
  - Loopback2: 172.16.1.1 /24
  - Loopback3: 172.16.2.1 /24
  - Loopback4: 172.16.3.1 /24
- Configure a summary on Router Barney so Router Fred will have a 172.16.0.0/22 entry in its routing table.

## GNS3 2.2.56.1

Import [rip-advanced-startup-configs IOU.gns3project](rip-advanced-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `rip-advanced-startup-configs.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Barney | FastEthernet0/0 | Ethernet0/0 |
| Barney | FastEthernet1/0 | Ethernet0/1 |
| Betty | FastEthernet1/0 | Ethernet0/0 |
| Betty | Serial0/0 | Serial4/0 |
| Betty | Serial0/1 | Serial4/1 |
| Betty | Serial0/2 | Serial4/2 |
| Betty | Serial0/3 | Serial4/3 |
| Fred | FastEthernet0/0 | Ethernet0/0 |
| Fred | FastEthernet1/0 | Ethernet0/1 |
| Wilma | FastEthernet0/0 | Ethernet0/0 |
| Wilma | Serial1/0 | Serial4/0 |
| Wilma | Serial1/1 | Serial4/1 |
| Wilma | Serial1/2 | Serial4/2 |
| Wilma | Serial1/3 | Serial4/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

## Video Solution

[RIP Advanced Video Solution](http://www.youtube.com/watch?v=17s2_1rpSSM)
