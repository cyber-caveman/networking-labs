# Solution and evidence guide — spoilers

All original OSPF discussions below refer to BLUE/process 10. The VRF-specific solution is in [VRF-SOLUTIONS.md](VRF-SOLUTIONS.md); read it for RED, migration, and isolation checks.

The complete baseline answers are in `final-configs/`, including RED and the migrated Loopback900 interfaces. They represent Activity 5B and the completed key rollover. They are full startup configurations, not incremental repair snippets. The predictions below follow configuration analysis; they are not captured router output.

## Routing and authentication

Create `router ospf 10 vrf BLUE` with `capability vrf-lite` before interface activation. BLUE/RED interface bindings precede IP addresses because changing a binding clears the address. Use interface `ip ospf 10 area <area>`, with `ip ospf network point-to-point` on cabled links and internal /24 loopbacks. Loopback0 remains /32. Set `passive-interface default` under process 10, then unpassive the cabled interfaces. R3 uses `area 30 stub no-summary`; R8 uses `area 30 stub`. R6 uses `area 20 nssa default-information-originate`, R7 `area 20 nssa`. The NSSA ABR can originate this default without a pre-existing default route; this differs from ordinary `default-information originate` on an ASBR.

Expected BLUE/process-10 neighbor counts: R1=4, R2=3, R3=4, R4=2, R5=1, R6=2, R7=1, R8=1. RED/process-20 counts are R1=2, R2=2, R4=1, R5=1, with none elsewhere. Point-to-point Ethernet means FULL/- and no DR election. All loopbacks are passive.

| Links | Effective method | Configuration scope | Final credential |
|---|---|---|---|
| R1–R2, R1–R3, R2–R3, R1–R5, R1–R6 | MD5 | `area 0 authentication message-digest`; interface keys | ID 20, CoreNew20 |
| R2–R4, R3–R4 | Simple password | `area 10 authentication`; interface password | A10plain |
| R6–R7 | MD5 | Explicit interface method and key | ID 7, NssaKey7 |
| R3–R8 | Null | Explicit interface override over area-30 MD5 | None |

For Activity 2, substitute ID 10 / CoreOld10 for the final backbone key. To roll a link, add ID 20 at both ends while retaining ID 10, inspect `show ip ospf 10 interface` and neighbor uptimes for completed rollover, then remove ID 10 at both ends. Repeat across all five backbone links. Do not retire a key on the basis of elapsed time alone. Cisco IOS MD5 rollover can send authenticated copies using old and new keys until neighbors demonstrate the new key. Algorithm changes to SHA are a separate operation and are not assumed hitless.

Simple authentication exposes the password in OSPF packets. MD5 provides packet authentication, not encryption of LSAs. Authentication Type 0 is null, Type 1 simple password, Type 2 cryptographic authentication; HMAC-SHA is another cryptographic algorithm, not a new OSPF authentication-type number. `no ip ospf authentication` restores inherited area behavior; `ip ospf authentication null` explicitly overrides it. Area method selection does not distribute or configure the interface secrets.

## Inter-area aggregation

The exact minimum cover for the six /24s is **10.10.0.0/22 plus 10.10.4.0/23**. A /21 also includes unassigned 10.10.6.0/24 and 10.10.7.0/24; a /20 would include the independent .8 and more holes.

R2:

```text
router ospf 10 vrf BLUE
 area 10 range 10.10.0.0 255.255.252.0 cost 50
 area 10 range 10.10.4.0 255.255.254.0 cost 50
 area 10 range 10.10.250.0 255.255.255.0 not-advertise
```

R3 has the same ranges and suppression but cost 80. Both ABRs must summarize or the unconfigured ABR leaks specifics. R1 receives two Type-3 advertisements per aggregate, advertised by 2.2.2.2 and 3.3.3.3. The selected installed route normally has cost **60 via 10.255.12.2** (10 to R2 plus 50). R3's candidate costs 90. Failure of R2's area-10 interface removes its contribution; R1 selects cost **90 via 10.255.13.2**. Failure of only the R1–R2 backbone link would not necessarily move selection to R3's aggregate: R2 remains reachable through R3. That is why the requested failure targets the campus-facing interface.

R2/R3 retain the intra-area /24 routes; R4 retains connected /24s. Their area-10 Type-1 information is not replaced by Type-3 aggregates inside area 10. The .8/24 remains independently advertised. The .250/24 stays inside area 10 and has no covering external advertisement; suppression applies at both exits. This is route advertisement policy, not a packet security ACL.

## External aggregation and NSSA stages

R5 redistributes only the five exact connected /24s allowed by EXT-R5 and CONNECTED-R5. No OSPF activation is present on those service loopbacks. The final policy is:

```text
router ospf 10 vrf BLUE
 redistribute connected subnets metric 40 metric-type 1 route-map CONNECTED-R5
 summary-address 172.20.16.0 255.255.252.0 tag 505
 summary-address 172.20.99.0 255.255.255.0 not-advertise
```

The Type-5 service aggregate is **172.20.16.0/22**, advertising router **5.5.5.5**, metric type 1, external metric 40, tag 505. R1's E1 route metric is **50** because the internal cost to R5 is 10. The four components and .99/24 must not be separate Type-5 advertisements. The route-map includes .99 so its suppression is demonstrably the summary policy's effect.

For R7, EXT-R7 permits only 172.21.32.0/24 through .35/24; redistribution uses type 2, metric 30, tag 707. The aggregate is **172.21.32.0/22**.

| Observation | Stage A: R7 aggregates | Stage B: R6 aggregates (final) |
|---|---|---|
| R7 policy | `summary-address 172.21.32.0 255.255.252.0 tag 707` | No service summary-address |
| R6 policy | No service summary-address | `summary-address 172.21.32.0 255.255.252.0 tag 707` |
| Service Type-7 LSAs in area 20 | One /22, advertiser 7.7.7.7 | Four /24s, advertiser 7.7.7.7 |
| Service Type-5 LSAs in area 0 | One /22, translated by 6.6.6.6 | One /22, aggregated by 6.6.6.6 |
| External metric/type/tag outside | 30 / E2 / 707 | 30 / E2 / 707 |

R6's NSSA default is a separate Type-7 LSA and is excluded from the service-LSA counts. R6 learns N2 service routes; R1 learns the E2 aggregate. E2 retains the external metric 30; internal cost is still relevant to path resolution and tie-breaking. R7 sees its service subnets as connected routes rather than N2 routes.

To change A to B, remove the service `summary-address` from R7 and add it on R6, leaving the R7 redistribution policy unchanged. A transient change in advertised specifics is acceptable during this exercise. `checkpoints/nssa-asbr-final-configs/` contains the complete Stage A alternative, including the final authentication settings. During the workbook's earlier Activity 5, retain your current backbone key 10 until Activity 7.

Inspect the actual forwarding-address fields rather than assuming they equal router IDs. For a nonzero forwarding address, prove an internal OSPF route to it; translated aggregate behavior can differ from an individual translated LSA. R7's internal loopback and the NSSA transit subnet remain unsummarized and advertised. A router ID identifies the LSA originator; it is not automatically a routable destination. Do not use `suppress-fa` to bypass the exercise.

## Reachability, area scope and default routes

R7's NSSA blocks incoming Type-5 LSAs, but its N2 default points to R6. R6 has normal-area routes to R5 and forwards those packets to R1, then R5. Return traffic reaches R7 using internal routes to its loopback or the NSSA service aggregate, depending on the source. R8's totally stubby area blocks Type 5 and non-default inter-area Type 3; R8 uses its O*IA default through R3. R8's own area-30 networks still propagate outward. Default-only stub behavior is not the same mechanism as a manually configured prefix summary.

R4 reaches R5 through a campus ABR and the backbone; R5 returns to 10.10.0.1 through one of the campus summaries. R4 reaches R7's services through a campus ABR, R1, and R6; R6 has the specific NSSA routes. R7 returns toward campus on internal inter-area routes. R8 sends service traffic by default to R3; service origins return using the independently advertised area-30 network. Prefix selectors prevent accidental redistribution of transit or loopback infrastructure.

## Withdrawal and discard evidence

With one component down, an aggregate still exists if another matching component remains. At the summarizing router, an absent more-specific destination falls into the local summary discard route instead of following a less-specific route back toward the sender. Observe the specific RIB/CEF entries: a traceroute timeout by itself does not establish where the discard occurs. Removing all eligible components withdraws the corresponding summary after convergence. On R4 the /22 and /23 have independent contributor sets. On R5 the suppressed .99/24 lies outside the service /22 and cannot hold it up.

Keep internal and external discard defaults enabled. Removing the discard can create a loop in a topology with a usable less-specific return route; it cannot reconstruct a vanished subnet. This baseline does not deliberately create such a loop and does not require you to disable discard behavior.

## Fault repairs

Apply one injection only after restoring the final baseline. Allow at least the dead interval for an authentication fault to expire an existing neighbor.

| Ticket | Root cause | Minimum repair | Evidence |
|---|---|---|---|
| T1 | R2 e0/0 secret for ID 20 differs from R1 | Restore `ip ospf message-digest-key 20 md5 CoreNew20` on R2 e0/0 | Matching key ID/method, FULL neighbor, route recovery |
| T2 | R3 lacks the .0/22 range | Restore `area 10 range 10.10.0.0 255.255.252.0 cost 80` on R3 | No four component Type-3 LSAs from R3 outside area 10 |
| T3 | R6 uses internal area-range policy for external Type-7 routes | Remove injected `area 20 range 172.21.32.0 255.255.252.0`; restore R6 `summary-address 172.21.32.0 255.255.252.0 tag 707` | Four service Type 7 in area 20; one service Type 5 outside |
| T4 | R8 inherits MD5 after losing null override | Restore `ip ospf authentication null` on R8 e0/0 | Effective null at both ends; branch neighbor/default recovered |
| T5 | R2 advertises an oversized .0/21 | Remove injected .0/21; restore .0/22 cost 50 and .4/23 cost 50 | No /21, /22+/23 only; no explicit coverage of .6/.7 |

## Operational command set

Choose commands based on the hypothesis; these are verification commands, not fabricated results.

```text
show ip interface brief
show ip ospf 10 neighbor
show ip ospf 10 interface Ethernet0/0
show ip protocols vrf BLUE
show ip ospf 10 database summary
show ip ospf 10 database external
show ip ospf 10 database nssa-external
show ip ospf 10 border-routers
show ip ospf 10 summary-address
show ip route vrf BLUE ospf
show ip route vrf BLUE 10.10.0.0 255.255.252.0
show ip route vrf BLUE 172.20.16.0 255.255.252.0
show ip route vrf BLUE 172.21.32.0 255.255.252.0
show ip cef vrf BLUE 10.10.0.1 detail
show ip prefix-list
show route-map
```

On R4, use `ping vrf BLUE 172.20.16.1 source 10.10.0.1`, then .17.1, .18.1, .19.1 and 172.21.32.1 through .35.1. Repeat on R8 with source 10.30.0.1. On R7, ping R5 service addresses with source 10.255.0.7. If the image does not accept the one-line source option, use the image’s VRF-aware extended ping syntax (check `ping vrf BLUE ?`); do not fall back to a global ping. Check the return-path RIB on the destination router. Capture baseline, fault, and restored outputs for each experiment.

## SHA extension solution

On both R6 and R7 create:

```text
key chain OSPF20
 key 20
  key-string NssaSHA256-Lab
  cryptographic-algorithm hmac-sha-256
```

Under R6 e0/1 and R7 e0/0, remove `ip ospf message-digest-key 7`, then select `ip ospf authentication key-chain OSPF20` in place of the interface message-digest method. No lifetime commands means always-valid keys. Verify `show key chain` and `show ip ospf 10 interface` for the sending SA and HMAC-SHA-256, then neighbors and service traffic. The full SHA variant preserves every routing policy and address from the core final set. It is conditional on actual CLI support; it has not been boot-tested on the selected IOU binary.

For a scheduled key change, stage a second matching key/algorithm at both peers, start accepting it before either peer sends it, set coordinated future send transitions, and retain old-key acceptance through the overlap. Validate clocks and operational selection before retiring old keys. Do not hard-code expired calendar dates into a reusable lab.
