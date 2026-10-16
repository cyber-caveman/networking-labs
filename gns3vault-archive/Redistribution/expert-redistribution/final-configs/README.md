# Expert Redistribution — final solution

Full startup configurations for the seven existing IOU routers, targeting GNS3 2.2.56.1. These are a newly authored solution to the lab, not an original GNS3Vault answer key. BlueJones and WiseMan need no changes, but their complete configs are included.

| Router | Configuration | Main change |
| --- | --- | --- |
| BabyDoll | [BabyDoll.cfg](BabyDoll.cfg) | Redistribute only Loopback0 into EIGRP 123; remove `network 1.0.0.0` |
| SweetPea | [SweetPea.cfg](SweetPea.cfg) | EIGRP 123 ↔ OSPF 234, prefer Ethernet, filter reflected backups |
| Rocket | [Rocket.cfg](Rocket.cfg) | Both EIGRP ASes ↔ OSPF, plus EIGRP 123 ↔ 356 |
| Blondie | [Blondie.cfg](Blondie.cfg) | RIP ↔ OSPF; advertise its own loopback with a preferred RIP metric |
| Amber | [Amber.cfg](Amber.cfg) | EIGRP 356 ↔ RIP, destination-specific RIP distance |
| BlueJones | [BlueJones.cfg](BlueJones.cfg) | Original config |
| WiseMan | [WiseMan.cfg](WiseMan.cfg) | Original config |

## Applying the solution

Use the router names, not the old `i5`–`i11` filenames, to select each file. Replace each router's startup configuration with its complete final file using your usual GNS3 configuration import/export workflow, then reload the routers. These files are replacement configs, not merge patches. On IOS, an alternative is to transfer the appropriate file to `startup-config` and reload without saving the old running configuration over it.

If you instead paste into a clean lab's running configuration, explicitly run `no network 1.0.0.0` under BabyDoll's `router eigrp 123` first. Omitting a line from a pasted config does not remove the existing command. Apply the complete policies to all routers before evaluating convergence, then save with `copy running-config startup-config`.

The original project, portable archive, bundled startup files, interfaces, addresses, and Frame Relay switch settings are preserved. The `.gns3project` still boots the unsolved exercise. No configuration is required for the unmanaged switches or FR1.

## How the solution meets the goals

All original routing domains and loopback advertisements remain in place, except for the explicitly requested BabyDoll change. The OSPF loopbacks retain `ip ospf network point-to-point`, so their /24 masks remain consistent across redistribution. BabyDoll's connected redistribution matches both Loopback0 and exactly `1.1.1.0/24`; it does not indiscriminately export connected networks.

SweetPea and Rocket mutually redistribute EIGRP 123 and OSPF 234. Rocket also mutually redistributes EIGRP 356 and OSPF; Blondie mutually redistributes RIP and OSPF. OSPF redistribution includes `subnets`, uses type-1 externals with metric 20, and the reverse directions explicitly include internal and both external OSPF route types.

The final Ethernet path is:

```text
BabyDoll / SweetPea — [123 LAN] — Rocket — [35 LAN] — Amber — [45 LAN] — Blondie / WiseMan
                                                     |
                                                 BlueJones
```

Rocket's EIGRP-to-EIGRP redistribution and Amber's EIGRP-to-RIP redistribution are necessary to complete that path. They implement the last goal without adding routing protocols to new interfaces, static routes, tunnels, or policy-based forwarding.

### Administrative distance and seed metrics

* SweetPea, Rocket, and Blondie use OSPF distance **180 for all three route types**. EIGRP external routes (170) and RIP routes (120) therefore beat Frame Relay OSPF routes. Increasing only OSPF external distance would leave the remote OSPF loopbacks preferring serial links.
* On Amber, RIP distance is **175**, with a **120 exception** for `4.4.4.0/24`, `7.7.7.0/24`, and `192.168.45.0/24`. This makes northbound routes prefer EIGRP 356, while southbound routes prefer RIP. Raising every RIP route to 175 would incorrectly make Amber prefer Rocket's OSPF-derived backup route to Blondie.
* Preferred EIGRP redistribution seeds are `100000 100 255 1 1500`. Remote OSPF backup seeds are `64 100000 255 1 1500`. Preferred RIP seeds are 1; remote OSPF backup seeds are 10, safely below RIP's unreachable metric of 16 across this topology.
* SweetPea's own OSPF loopback enters EIGRP 123 with the preferred seed. Rocket's own loopback enters both EIGRP processes with the preferred seed. Blondie's own loopback enters RIP with metric 1. These local injections do not traverse Frame Relay.

With the Ethernet links healthy, both SweetPea and Rocket select BabyDoll's external EIGRP route directly through `192.168.123.1`, despite the OSPF copies. All normal traffic to the other loopback and Ethernet subnets also uses Ethernet.

**Necessary exception:** traffic addressed to the Frame Relay interfaces themselves (`192.168.234.2/.3/.4`) can use Frame Relay even when Ethernet is healthy. That subnet is directly connected on the three OSPF routers. OSPF/LMI control traffic also continues on serial links. The backup requirement applies to transit traffic between the other networks; prohibiting even serial-subnet and control traffic would contradict the supplied topology.

### Feedback prevention

Exact /24 prefix lists bound every export to the lab's eleven networks; there is no catch-all redistribution. Directional filters at Rocket keep the normal north/south transfers separate.

Tag **100** marks native/preferred exports. Tag **234** marks remote routes imported from OSPF as backup paths. The bridges preserve 234 explicitly. `TO-OSPF` rejects 234, and also permits only the seven non-OSPF-native prefixes. Thus neither OSPF backups nor OSPF's native loopbacks/transit subnet are injected back as OSPF externals.

On SweetPea and Rocket, `E123-IN` rejects tag 234 from EIGRP 123. This matters because their OSPF distance is higher than EIGRP external distance: accepting each other's OSPF-derived backup routes can otherwise cause mutual dependency and route withdrawal/reinjection. Each uses its own OSPF backup instead. The FR subnet has an explicit exception so a router with its serial interface down can still reach the surviving FR subnet through its Ethernet peer. Native loopback exports use tag 100 and remain accepted.

The policies cover the supplied topology and single-link/whole-LAN outages. They are not a generic arbitrary-topology redistribution template; new prefixes or simultaneous compound failures require another policy review.

## Expected healthy forwarding

| Source | Destination | Expected first hop / path |
| --- | --- | --- |
| SweetPea | 1.1.1.1 | 192.168.123.1, E0/0, D EX |
| Rocket | 1.1.1.1 | 192.168.123.1, E0/0, D EX |
| SweetPea | 4.4.4.4 / 7.7.7.7 | Rocket → Amber → Blondie / WiseMan |
| Rocket | 4.4.4.4 / 7.7.7.7 | 192.168.35.5, E0/1, D EX |
| Amber | 1.1.1.1 / 2.2.2.2 / 3.3.3.3 | 192.168.35.3, E0/0, D EX, AD 170 |
| Amber | 4.4.4.4 / 7.7.7.7 | 192.168.45.4 / .7, E0/1, RIP, AD 120 |
| Blondie | 1.1.1.1 / 6.6.6.6 | 192.168.45.5, E0/0, RIP |
| BlueJones | 7.7.7.7 | 192.168.35.5, E0/0, D EX |
| WiseMan | 1.1.1.1 | 192.168.45.5, E0/0, RIP |

## Verification performed

Configuration inspection confirmed the original interface blocks, addresses, bandwidth/delay values, ANSI LMI, full-mesh PVC mapping, routing-domain membership, and /24 OSPF loopback behavior. BlueJones and WiseMan are byte-for-byte copies of their startup configs. There was no supplied final solution to compare against.

`../verify_final_configs.py` reads the final configs and models connected-route ownership, configured routing-domain membership, prefix-list/route-map decisions, tag preservation, redistribution of installed routes and participating connected routes, administrative distances, and relative seed-metric ordering. It checks forwarding chains for loops and missing routes, and checks that healthy forwarding to non-FR prefixes avoids OSPF.

Result: **1,118 router/prefix forwarding checks passed over 16 scenarios**: healthy topology, each of the 12 connected physical router interfaces down separately, and each of the three Ethernet LANs down as a whole. It checks only physically reachable router/prefix pairs. BabyDoll, BlueJones, and WiseMan have no redundant uplink; losing their sole link necessarily isolates their loopback. A whole LAN outage removes that LAN's connected prefix as well.

This is an abstract steady-state policy model, not an IOS emulator. It uses one deterministic route for ties and simplified protocol metrics; it does not validate all ECMP alternatives, DUAL feasibility, IOS command acceptance, RIP timers/split horizon, convergence transients, live OSPF adjacency/DR election, inverse ARP, PVC state, or packet delivery. No routers were booted or live-tested. Model results support the configuration analysis; they do not certify the remote IOS image.

Run the analysis from the lab folder:

```sh
python3 verify_final_configs.py
```

## Live acceptance checks

1. On every router, check `show ip interface brief` and `show ip protocols`. Confirm the imported commands were accepted, BabyDoll has no EIGRP `network 1.0.0.0`, and Amber shows the intended RIP distances.
2. Check `show ip eigrp neighbors`, `show ip ospf neighbor`, and `show ip rip database` as applicable. On the three serial routers, check `show frame-relay pvc` and `show frame-relay map`: PVCs should be active and inverse ARP should supply the peer mappings with broadcast capability. FR1 has 203↔302, 204↔402, and 304↔403 PVCs. No FR transport changes were needed for this solution.
3. Check `show ip route 1.1.1.1` and `traceroute 1.1.1.1 source Loopback0` on SweetPea and Rocket. Both should go directly to BabyDoll over E0/0. Inspect `show ip eigrp topology` to confirm it is external.
4. From every router, ping all seven loopback addresses using Loopback0 as the source. Also ping every active physical interface address. This validates return paths as well as outward reachability. Use the forwarding table above for representative traceroutes and inspect `show ip route`, `show ip cef`, and `show route-map`.
5. Shut one interface at a time, allow convergence, repeat loopback-sourced pings/traceroutes, then restore it before the next test. In particular: Rocket E0/0, Rocket E0/1, Amber E0/0, Amber E0/1, Blondie E0/0, and SweetPea E0/0. Surviving routers should retain reachability through OSPF where the Ethernet path is broken. Failure of either shared-medium endpoint is worth testing separately.
6. With all Ethernet links restored, shut the three Serial4/0 interfaces. All seven loopbacks and all three Ethernet networks should remain reachable, though the FR subnet is gone. Restore serial and confirm that normal paths continue to use Ethernet.

Cisco references used to check the design: [redistribution and feedback prevention](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8606-redist.html), [OSPF administrative-distance controls](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/15-mt/iro-15-mt-book/iro-cfg.html), and [EIGRP inbound route-map filtering](https://www.cisco.com/c/en/us/td/docs/routers/ios-xe/ip-routing/b-ip-routing/m_eigrp-route-map.html). Exact support on the installed IOU image still requires the live checks above.
