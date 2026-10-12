# IP Service Level Agreement (SLA)

## Scenario

As the senior network engineer for "Groceries 'r' Us" you are responsible for all routing within the company. Every now and then you have links that are still in the up/up state but you are unable to send any IP packets over them. You also would like something that could generate different traffic streams like RTP to simulate VoIP or HTTP. You heard good things about IP SLA so you decide to build a lab and test some things...

## Goal

- All IP addresses have been preconfigured for you.
- OSPF has been configured for full connectivity.
- Configure router Lettuce to send ICMP echo packets to IP address 4.4.4.4 every 9 seconds. It should never stop.
- Configure router Cucumber to send DNS request packets to IP address 1.1.1.1 every 8 seconds. It should never stop.
- Configure router Pickle to send G711 packets to IP address 2.2.2.2 port 16384 with a codec-size of 160 bytes with an interval of 20ms. It should never stop.
- Configure router Cucumber to respond to the G711 packets.
- Configure router Tomato to send G729 packets to IP address 3.3.3.3 port 16374 with a codec-size of 20 bytes. It should never stop.
- Configure router Pickle to respond to the G729 packets.
- Configure router Lettuce to send HTTP GET packets to IP address 192.168.34.4 every 60 seconds.

## GNS3 2.2.56.1

Import [IP SLA IOU.gns3project](IP%20SLA%20IOU.gns3project) using **File > Import portable project**. To open `IP SLA.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Cucumber | FastEthernet0/0 | Ethernet0/0 |
| Cucumber | FastEthernet1/0 | Ethernet0/1 |
| Lettuce | FastEthernet0/0 | Ethernet0/0 |
| Lettuce | FastEthernet1/0 | Ethernet0/1 |
| Pickle | FastEthernet0/0 | Ethernet0/0 |
| Pickle | FastEthernet1/0 | Ethernet0/1 |
| Tomato | FastEthernet0/0 | Ethernet0/0 |
| Tomato | FastEthernet1/0 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-ip-service-level-agreement-sla.png)

## Video Solution

http://www.youtube.com/watch?v=TZFUCwoQjx4
