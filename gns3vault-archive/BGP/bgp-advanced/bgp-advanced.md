# BGP Advanced

![Network Topology](./topology-bgp-advanced.jpg)

## Scenario:

You have been working for a service provider called "FreedomBits" for quite some time and you have been responsible for the operation of all IGP's. Your BGP expert/colleague has won the X-factor competition and decided to start a singing career...it's up to you to upgrade your skills and become the new BGP guru in town. You have heard alot about BGP and even did some basic configurations but never tried anything with confederations or route-reflectors...time for a change!

## Goal:

All IP addresses have been preconfigured for you in the following order:

- R1 - R2: 192.168.12.X
- R1 - R3: 192.168.13.X
- R3 - R4: 192.168.34.X

(Where X = Router number)

And so on...

Every router has a Loopback0 interface:
X.X.X.X

(Where X = Router number)

### Configuration Requirements:

- Configure each Autonomous System (AS) with a different IGP:
  - AS100: RIP
  - AS300: OSPF
  - AS200: EIGRP
  - AS400: OSPF

- Do not configure the IGP on the interfaces connecting to another AS. For example; R3 should not send any RIP routing updates towards R4.

- Make sure the loopbacks are advertised in the IGP's.

- Configure BGP on every router, make sure you have the right IBGP and EBGP configurations. AS300 has to be configured as a confederation.

- R1 has to be configured as a route-reflector for R2 and R3.

- Configure on all routers that BGP updates are sourced from the Loopback0 interface.

- Configure BGP authentication between R7 and R11, use password VAULT

- Make sure all BGP neighbor relationships are working before you continue with the next steps.

- Advertise all physical and loopback interfaces in BGP, you are not allowed to use the "network" command to achieve this.

- Achieve full connectivity, every IP address should be pingable. Use a TCLSH script to do this.

- When R4 sends a ping to the loopback interface of R1 it should choose the path through R2. You are only allowed to make changes on R3.

- Create another loopback interface on R1 with ip address 172.16.1.1 /24, advertise this in RIP.

- When R4 sends a ping to the 172.16.1.1 address it should take the path through R3, you are only allowed to make changes on R4.

- When R6 sends a ping towards the loopback interface on R11 it should go through AS300.

- R7 should prefer the path through R11 for all external networks except for 172.16.1.1.

- Configure AS300 so it is no longer a transit AS for AS200 to reach 172.16.1.1 in AS100. AS400 should not be influenced.

## GNS3 2.2.56.1

Import `bgp-advanced-startup-configs IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `bgp-advanced-startup-configs.gns3` beside `project-files`.

Routers use the preferred IOU L3 image `x86_64_crb_linux-adventerprisek9-ms.bin`
(MD5 `4a2fce8de21d1831fbceffd155e41ae7`), template
`b3b10b90-adfb-43f8-b289-b68bcf322ad8`, 768 MB RAM, 512 KB NVRAM,
four Ethernet and four serial adapters, with automatically allocated consoles.
Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Physical interface names and link endpoints are updated together in startup and
all supplied final configs. Original bandwidth and delay are explicit where
needed to preserve EIGRP/IGP metric inputs. Source protocol settings and intended
startup state are preserved; final configs are not loaded at startup.

| Router | Original interface | IOU interface |
| --- | --- | --- |
| R1 | FastEthernet0/0 | Ethernet0/0 |
| R1 | FastEthernet1/0 | Ethernet0/1 |
| R10 | FastEthernet0/0 | Ethernet0/0 |
| R10 | FastEthernet1/0 | Ethernet0/1 |
| R11 | FastEthernet0/0 | Ethernet0/0 |
| R11 | FastEthernet1/0 | Ethernet0/1 |
| R2 | FastEthernet0/0 | Ethernet0/0 |
| R2 | FastEthernet1/0 | Ethernet0/1 |
| R3 | FastEthernet0/0 | Ethernet0/0 |
| R3 | FastEthernet1/0 | Ethernet0/1 |
| R4 | FastEthernet0/0 | Ethernet0/0 |
| R4 | FastEthernet1/0 | Ethernet0/1 |
| R4 | FastEthernet2/0 | Ethernet0/2 |
| R4 | FastEthernet3/0 | Ethernet0/3 |
| R5 | FastEthernet0/0 | Ethernet0/0 |
| R5 | FastEthernet1/0 | Ethernet0/1 |
| R5 | FastEthernet2/0 | Ethernet0/2 |
| R6 | FastEthernet0/0 | Ethernet0/0 |
| R6 | FastEthernet1/0 | Ethernet0/1 |
| R6 | FastEthernet2/0 | Ethernet0/2 |
| R7 | FastEthernet0/0 | Ethernet0/0 |
| R7 | FastEthernet1/0 | Ethernet0/1 |
| R8 | FastEthernet0/0 | Ethernet0/0 |
| R8 | FastEthernet1/0 | Ethernet0/1 |
| R9 | FastEthernet0/0 | Ethernet0/0 |
| R9 | FastEthernet1/0 | Ethernet0/1 |

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology:

## Video Solution:

http://www.youtube.com/watch?v=FtD8W3Q97HI
