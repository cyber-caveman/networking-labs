# Expert Redistribution

![Network Topology](./topology-expert-redistribution.jpg)

## Scenario:

You have been a network engineer as long as you can remember. Recently the company experienced a network failure and your colleagues have blamed you for misconfiguration of the routers. As a result you are taken to a mental institution and it seems your networking days are over...however during your sleep you are being plagued by nightmares about redistribution scenarios. Let's see if you can suckerpunch this one!

## Goal:

* All IP addresses have been preconfigured for you:
  * Loopback interface: L0: x.x.x.x /24, for example 1.1.1.1 for router 1
* EIGRP AS 123 has been preconfigured on router BabyDoll, SweetPea and Rocket
* OSPF Area 0 (Process 234) has been preconfigured on router SweetPea, Rocket and Blondie
* EIGRP AS 356 has been preconfigured on router Rocket, BlueJones and Amber
* RIP Version 2 has been preconfigured on router Blondie, Amber and WiseMan
* Router BabyDoll's loopback0 interface is advertised in EIGRP AS123
* Router SweetPea's, Blondie's and Rocket's loopback0 interfaces are advertised in OSPF Area 0
* Router Amber's and BlueJones's loopback0 interfaces are advertised in EIGRP AS356
* Router WiseMan's loopback0 interface is advertised in RIPV2
* Configure 2-way redistribution on router SweetPea and Rocket between EIGRP AS123 and OSPF
* Configure redistribution on router Rocket between EIGRP AS356 and OSPF
* Configure redistribution on router Blondie between RIPV2 and OSPF
* Ensure you have full connectivity at this moment, every network / loopback should be reachable from any device
* Remove the "network 1.0.0.0" command on router BabyDoll and replace it by redistributing the loopback0 interface into EIGRP AS123
* Do a traceroute from router SweetPea and Rocket to 1.1.1.1, you notice packets are sent through the OSPF network. Ensure they take the most optimal route to the destination
* Ensure all traffic will be sent using the FastEthernet links. The Frame-Relay links should only be used as a backup when the FastEthernet links are down

## GNS3 2.2.56.1

Import `Expert Redistribution IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `Expert Redistribution.gns3` beside `project-files`.

Routers use the preferred IOU L3 image `x86_64_crb_linux-adventerprisek9-ms.bin`
(MD5 `4a2fce8de21d1831fbceffd155e41ae7`), template
`b3b10b90-adfb-43f8-b289-b68bcf322ad8`, 768 MB RAM, 512 KB NVRAM,
four Ethernet and four serial adapters, with automatically allocated consoles.
Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Physical interface names and link endpoints are updated together in startup and
all supplied final configs. Original bandwidth and delay are explicit where
needed to preserve EIGRP/IGP metric inputs. Source protocol settings and intended
startup state are preserved; final configs are not loaded at startup.

Built-in Frame Relay switches and PVC mappings retain their original type and
settings. Connected IOU interfaces explicitly select ANSI LMI, supported by the
built-in switch. This is a transport compatibility adjustment in startup and
available final configs, not a change to the routing exercise.

Unmanaged Ethernet switches retain their original type and VLAN settings.

| Router | Original interface | IOU interface |
| --- | --- | --- |
| BabyDoll | FastEthernet0/0 | Ethernet0/0 |
| SweetPea | FastEthernet0/0 | Ethernet0/0 |
| SweetPea | Serial1/0 | Serial4/0 |
| SweetPea | Serial1/1 | Serial4/1 |
| SweetPea | Serial1/2 | Serial4/2 |
| SweetPea | Serial1/3 | Serial4/3 |
| Rocket | FastEthernet0/0 | Ethernet0/0 |
| Rocket | FastEthernet1/0 | Ethernet0/1 |
| Rocket | Serial2/0 | Serial4/0 |
| Rocket | Serial2/1 | Serial4/1 |
| Rocket | Serial2/2 | Serial4/2 |
| Rocket | Serial2/3 | Serial4/3 |
| Blondie | FastEthernet0/0 | Ethernet0/0 |
| Blondie | Serial1/0 | Serial4/0 |
| Blondie | Serial1/1 | Serial4/1 |
| Blondie | Serial1/2 | Serial4/2 |
| Blondie | Serial1/3 | Serial4/3 |
| Amber | FastEthernet0/0 | Ethernet0/0 |
| Amber | FastEthernet1/0 | Ethernet0/1 |
| BlueJones | FastEthernet0/0 | Ethernet0/0 |
| WiseMan | FastEthernet0/0 | Ethernet0/0 |

### Source notes

No completed solution configs were supplied; none were invented.

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology:
