# Candidate workbook

## Scenario and restrictions

You are implementing an OSPF migration for a campus with two ABRs, a redistributed services domain, an NSSA acquisition, and a stub branch. Addressing is already installed. Meet the operational requirements with the smallest necessary routing policy changes.

Activities 1–9 and the SHA extension operate exclusively in **VRF BLUE / process 10**. Activities V1–V4 add VRF administration and **VRF RED / process 20**. Keep every original BLUE requirement in force. Use `show ip ospf 10 ...` for BLUE, `show ip ospf 20 ...` for RED, and VRF-qualified RIB/CEF/ping commands. Unqualified pings use the global table and are not valid positive tests. Do not change addresses, cabling, router IDs, or subnet masks. Do not add static routes, tunnels, routing processes beyond BLUE 10 and RED 20, or additional interfaces. Temporary VRF STAGING is permitted only in V1; delete it afterward. Do not use blanket redistribution, distribute-lists, or prefix filters to substitute for the required summarization and suppression. Prefix lists and route maps are permitted only to select connected routes for redistribution. Do not use default routes as a substitute for campus summaries. Retain automatically generated discard routes. Temporary changes explicitly requested below must be restored.

Execution order: **V1 → 1–7 → V2 → 8 → V3 → V4 → 9 → optional SHA**. V activities add 90 minutes to the original 180-minute core.

Use [TOPOLOGY.md](TOPOLOGY.md) as your addressing sheet. Unless an activity explicitly says otherwise, all earlier requirements remain in force. BLUE uses Ethernet0/x and RED uses Ethernet1/x; never infer the tenant from an IP address alone. Keep notes of commands, LSA types, advertising-router IDs, masks, next hops, metrics, tags, and failures. A successful ping alone is insufficient proof. Save configurations at checkpoints.

The required [VRF practice stations](VRF-ACTIVITIES.md) contain V1–V4, their credentials, migration tasks and final isolation matrix. Start with V1.

## Activity 1 — Establish the routing domain (20 minutes, 10 points)

1. Create OSPF process 10 explicitly bound to BLUE before activating interfaces; enable `capability vrf-lite`. Configure router IDs `1.1.1.1` through `8.8.8.8` on the corresponding routers. Enable OSPF using interface-level activation only.
2. Place all BLUE interfaces in the areas specified in the addressing sheet. Do not enable OSPF on the 172.20.x.x and 172.21.x.x service loopbacks; they will be redistributed later.
3. Ensure every Ethernet adjacency is point-to-point, with interface cost 10. Advertise all internal /24 loopbacks with their configured masks rather than /32 host routes.
4. Suppress hellos on all loopbacks by default. Explicitly permit hellos only on the nine BLUE cabled links. Leave RED OSPF unconfigured until V2.
5. Configure area 20 as an NSSA. Provide R7 an NSSA default from R6 so it can reach external services in normal areas. Configure area 30 as a totally stubby area, retaining its ABR-generated default.
6. Establish all nine BLUE adjacencies. Prove bidirectional reachability between R4 Loopback100 and R8 Loopback100 before adding summaries. Capture neighbor state and initial route counts.

## Activity 2 — Apply differentiated authentication (20 minutes, 15 points)

1. Make MD5 the area-wide default for area 0. Initially use key ID **10**, secret **CoreOld10**, on every backbone link. Do not configure per-interface method overrides in area 0.
2. Make simple password authentication the area-wide default for area 10. Use the eight-character secret **A10plain** on both ends of both area-10 links.
3. Protect R6–R7 with interface-level MD5, key ID **7**, secret **NssaKey7**. Do not set an area-wide authentication policy in area 20.
4. Set area 30's area-wide default to MD5 on both routers, but implement the approved **null authentication exception** on the R3–R8 link at both ends. Retain that exception in the final core state.
5. Prove the effective authentication mode on every link. Capture packets on one simple-password link and one MD5 link; explain which secret is observable and whether either method encrypts OSPF routing information. Explain why removing an interface authentication command is not necessarily equivalent to selecting null authentication.

## Activity 3 — Summarize a dual-ABR campus (20 minutes, 15 points)

1. Advertise R4's six service subnets 10.10.0.0/24 through 10.10.5.0/24 outside area 10 using the **fewest aggregates that include no unassigned /24s**. Derive the boundaries yourself.
2. Keep 10.10.8.0/24 visible separately. Do not absorb it into an aggregate. Do not summarize transit networks or router loopback /32s.
3. Configure both ABRs so neither leaks the six specifics outside area 10. The aggregate LSA metric must be **50 from R2** and **80 from R3**, regardless of internal component costs.
4. Keep 10.10.250.0/24 usable inside area 10, but originate neither its specific nor a covering aggregate into other areas. Accomplish this with the area-range suppression mechanism. No outside reachability to that subnet is required.
5. On R1, prove the selected ABR and distinguish the LSA metric from the installed end-to-end route metric. On R2/R3, prove that intra-area component routes remain available.
6. Explain why configuring the same aggregate on internal router R4 cannot replace the ABR policy, and why an intra-area router cannot hide individual Type-1 link descriptions by summarizing them.

## Activity 4 — Summarize external routes at their source (20 minutes, 15 points)

1. On R5, select exactly 172.20.16.0/24 through 172.20.19.0/24 and 172.20.99.0/24 for connected redistribution. Do not redistribute infrastructure addresses or use static Null0 routes to manufacture routes.
2. Originate the four contiguous service prefixes outside the ASBR as one minimum-size aggregate. Use **E1**, external metric **40**, and aggregate tag **505**.
3. Suppress 172.20.99.0/24 using the external summarization suppression mechanism. Keep it in the redistribution selector so suppression, rather than exclusion, does the work.
4. On R1 and R4, demonstrate the Type-5 aggregate, tag, external metric, and forwarding reachability to all four .1 service addresses. Explain why R1's route metric is not merely 40. Explain why an ABR area range cannot perform this external aggregation.
5. On R7 and R8, explain why the same Type-5 LSA is absent yet these destinations remain reachable. Prove the return paths using explicit loopback-sourced pings.

## Activity 5 — Move summarization across the NSSA boundary (25 minutes, 15 points)

1. Select exactly R7's 172.21.32.0/24 through 172.21.35.0/24 for connected redistribution, external metric **30**, type **2**, tag **707**. No redistribution on R6.
2. **Stage A:** Summarize at the NSSA ASBR. R6 must see one Type-7 service aggregate; R1 must see the corresponding Type-5 aggregate. Capture the mask, metric, tag, advertising router and forwarding address at both observation points. Save this checkpoint.
3. **Stage B (required final state):** Restore the four specific Type-7 service LSAs inside area 20, while keeping only the single service aggregate as Type 5 in area 0. Move the aggregation policy to the translating ABR without changing the redistribution selector on R7. Ensure the Type-5 aggregate retains tag 707.
4. Show that Type-3 summarization of area 20's internal routes is not a replacement for Type-7-to-Type-5 aggregation. Explain which router originates each relevant LSA in each stage.
5. Prove all four NSSA service addresses are reachable from R4 and R8, and prove R7 can reach the R5 external services. Do not summarize or suppress the internal route used to resolve the NSSA forwarding address.

## Activity 6 — Prove failure and discard behavior (20 minutes, 10 points)

1. On R2, shut only its interface toward R4. Observe convergence on R1: the service aggregates must remain present through R3, with no /24 leaks. Restore the interface and verify the original preference returns. Repeat with only R3's R4-facing interface shut, then restore it. Record the actual outage durations; no particular subsecond target is assumed.
2. Shut R4 Loopback100 only. Explain why the associated aggregate should remain while .1 in the failed component is no longer reachable. Trace the forwarding decision at the advertising ABRs and identify the discard route. Do not confuse a failed destination with a failed whole aggregate.
3. Shut R4 Loopbacks100–103 together. Prove withdrawal of only their aggregate while the aggregate for Loopbacks104–105 remains. Restore all interfaces.
4. Repeat the component / all-components test on R5 Loopbacks100–103. Prove external aggregate retention, then withdrawal, then recovery. Do not count the suppressed 172.20.99.0/24 as a contributor.
5. Explain what removing a discard route would change when a less-specific route exists, and why that does not repair a missing component. Do not disable discard routes in the saved configuration.

## Activity 7 — Rotate a live backbone key (15 minutes, 10 points)

1. Migrate all five area-0 links from key **10 / CoreOld10** to key **20 / CoreNew20**. Keep each adjacency continuously FULL after the migration begins; record neighbor uptime before and after.
2. Stage the new key at both ends of each link, confirm rollover completion, and only then retire the old key. Do not clear OSPF, shut interfaces, or remove the old key first.
3. In the final state, only key 20 may remain on backbone interfaces. Explain why matching secrets with different key IDs is insufficient.

## Activity 8 — Troubleshooting tickets (30 minutes, 10 points)

Start from your saved BLUE+RED final state after V2. Have a partner apply one of T1–T5 from `faults/` without showing you the commands, or apply one yourself and close the file. Diagnose using operational evidence before reading running-config. Repair each ticket before applying the next. Do not reload or paste the complete answer configuration as a repair. A clean baseline has no intentionally hidden faults.

| Ticket | Reported symptom | Budget |
|---|---|---:|
| T1 | One backbone adjacency expires after a credential change, although other links continue working. | 5 min |
| T2 | All adjacencies are FULL, but component campus routes reappear outside area 10. | 5 min |
| T3 | R1 sees NSSA service specifics; the requested external aggregate is missing. | 6 min |
| T4 | The stub branch loses its only neighbor after an interface cleanup. | 5 min |
| T5 | Outside routers advertise reachability to unassigned campus space. | 5 min |

Use the remaining four minutes to compare the repaired route and adjacency state with the baseline. For each ticket, document the affected control-plane object, root cause, smallest repair, and verification. Award two points per ticket only when all four are present.

## Activity 9 — Final acceptance (10 minutes, pass/fail gate)

1. Restore every temporarily shut interface, finish Stage B of Activity 5, remove every fault injection, and save all eight configurations.
2. Confirm nine BLUE FULL adjacencies (18 process-10 neighbor entries) and three RED FULL adjacencies (six process-20 entries), 24 entries total, passive loopbacks, and the required authentication modes.
3. From R1, confirm two campus aggregates and the independent 10.10.8.0/24; no campus component /24s, no 10.10.250.0/24, one R5 service aggregate, and one NSSA service aggregate. Check exact prefixes/masks in the RIB **and** LSDB; a longest-match lookup alone is not proof of a specific route.
4. From R6, confirm four specific NSSA service Type-7 LSAs. R7 must have a default toward R6. R8 must have an inter-area default toward R3 and no Type-5 LSAs or non-default Type-3 routes from outside area 30.
5. Use R4 source 10.10.0.1 and R8 source 10.30.0.1 to ping all R5 and R7 service .1 addresses. From R7 source 10.255.0.7, ping all four R5 service .1 addresses. Document the routes used in both directions.
6. Compare your solution with `final-configs/` and explain harmless formatting differences. Wrong LSA scope, excess advertisements, unresolved next hops, or residual faults fail acceptance even if some pings work.

Target score: **135/150 plus acceptance**, including the VRF acceptance matrix in V4. V1/V2/V3/V4 add 10/15/10/15 points respectively; divide each V activity’s points equally among its numbered requirements. Activities 1–8 total 100 points; split each activity's points equally across its numbered requirements, except Activity 8 as specified. This is a local study rubric, not Cisco scoring.

## Extension — HMAC-SHA-256 (25–35 minutes; separate from core scoring)

First inspect `show version`, interface `ip ospf authentication ?`, and `cryptographic-algorithm ?` inside a temporary key-chain key. Do not infer support from the image filename. Remove the temporary probe key chain. If `key-chain` or `hmac-sha-256` is absent, record **unsupported on this image** and complete the design analysis without applying the extension; core MD5 remains valid.

On supported images, migrate only R6–R7 to key chain **OSPF20**, key ID **20**, algorithm **HMAC-SHA-256**, secret **NssaSHA256-Lab**. Use always-valid keys for this repeatable saved state. Remove the old interface MD5 key. A controlled adjacency reset during this algorithm change is permitted; it is not the nondisruptive MD5 rollover task.

Verify the sending security association, key ID, algorithm, neighbor recovery and external reachability. Explain how future-dated send lifetimes, overlapping accept lifetimes and consistent router clocks would support planned rollover; distinguish that design from the always-valid saved config. Consult `extensions/hmac-sha256/final-configs/` only after the attempt. Restore core MD5 afterward if you want the baseline to match `final-configs/`.
