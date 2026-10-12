# EIGRP Intermediate

![Network Topology](./topology-eigrp-intermediate.jpg)

## Scenario

You and a colleague network administrator were talking about the scalability and flapping network issues that you have encountered in the past. Especially the stories about EIGRP stuck-in-active make you shiver. On your network you are using EIGRP as a routing protocol, and you have heard that summarization and stub routers might solve some of your problems. Time for some good old lab action!

## Goal

- Achieve full connectivity, every IP Address should be pingable from any router.
- When you ping 1.1.1.1 from R4 it should take the path through R2.
- Change the EIGRP Metrics so load/reliability are also used in addition to bandwidth and delay.
- Disable EIGRP auto-summary.
- Create 4 extra loopbacks on R3:
  - Loopback10: 172.16.0.1 /24
  - Loopback11: 172.16.1.1 /24
  - Loopback12: 172.16.2.1 /24
  - Loopback13: 172.16.3.1 /24
- Advertise these networks in EIGRP, the routing table on R1, R2 and R4 should only show a single entry for these networks: 172.16.0.0/22
- Create a default route on R1, if you look at the routing table on R2, R3 or R4 it should show the default route pointing to R1.
- Change the bandwidth on R2 on FastEthernet0/0 to 100. Make sure you only see 1 entry for the 1.1.1.0 network in R4.
- Without modifying R2, make sure R4 has 2 entries for the 1.1.1.0 network, one by going through R2, the other one through R3. Only use EIGRP or bandwidth commands to achieve this.
- Enable authentication between R1 and R2:
  - key-chain: CISCO
  - key-string: PASSWORD
- Disable the link between R3 and R4.
- Make sure that when you type 'shutdown' on Loopback1 at R2, R1 will not send a QUERY to R3. (hint: to check this, do a 'debug eigrp packets query reply')

## GNS3 2.2.56.1

Import `eigrp-intermediate-startup-configs IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `eigrp-intermediate-startup-configs.gns3` beside `project-files`.

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
| R2 | FastEthernet0/0 | Ethernet0/0 |
| R2 | FastEthernet1/0 | Ethernet0/1 |
| R3 | FastEthernet0/0 | Ethernet0/0 |
| R3 | FastEthernet1/0 | Ethernet0/1 |
| R4 | FastEthernet0/0 | Ethernet0/0 |
| R4 | FastEthernet1/0 | Ethernet0/1 |

### Source notes

No source startups were supplied. Recovered addressing from final configs, enabled the initial connected links and left routing/policies unconfigured for the exercise.

The recovered initial state excludes the additional Loopback10–13 exercise networks. Source final configs contain only one of R3’s four requested loopbacks, and no R2 Loopback1; these source solution omissions are retained.

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology
