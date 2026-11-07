# VRF practice stations — candidate tasks

These four activities are required parts of the revised lab, not optional extensions. Execute **V1 → WORKBOOK 1–7 → V2 → WORKBOOK 8 → V3 → V4 → WORKBOOK 9**. OSPF activities 1–9 remain in BLUE. Total target is **270 minutes** before optional SHA.

## V1 — Administer and migrate routing contexts (20 minutes, 10 points)

1. Inventory the preprovisioned VRFs, RDs and interfaces. BLUE exists on all eight routers; RED exists on R1/R2/R4/R5. RDs are 65000:10 and 65000:20. Explain why duplicate addresses are valid in these separate contexts, why an RD is not an access-control policy, and why route targets alone would not exchange routes in this OSPF-only VRF-Lite design.
2. On R1 create IPv4 VRF **STAGING**, RD **65000:99**, without import/export policy. Move the already addressed Loopback900 into it. Capture the binding change and any address-removal message, then restore **198.18.0.1/32**. Confirm its local/connected route exists in STAGING and is absent from the global table. Do not add another loopback.
3. Move R1 Loopback900 from STAGING to BLUE, restore the same address, then remove the now-unused STAGING VRF. Move R5 Loopback900 from global into BLUE and restore **198.18.0.5/32**. Leave both interfaces enabled. In Activity 1 activate them in BLUE area 0, passive. After Activity 1 prove R1-to-R5 reachability with source 198.18.0.1 using BLUE, and prove no corresponding global route exists.
4. Before starting OSPF, inspect support for `router ospf <id> vrf <name>` and `capability vrf-lite` on the actual image. Explain the latter's role in suppressing PE-specific OSPF checks. Use it in every tenant process. Do not use MPLS, BGP, route targets, inter-process redistribution, static leaking or PBR to solve any activity. Do not remove the tenant VRFs to make a failed global ping succeed.

## V2 — Build a second tenant with overlapping addresses (35 minutes, 15 points)

1. On R1/R2/R4/R5 create OSPF **20 bound to RED**, with router IDs **20.20.20.r**, where r is the router number. Preserve BLUE process 10. Use interface activation, cost 10, point-to-point Ethernet, /24-preserving loopback network type, passive-by-default with only RED cabled interfaces active. R1–R2 and R1–R5 are area 0; R2–R4 is normal area 10. Advertise Loopback1000 in the indicated area and R5 Loopback1900 in area 0. Never activate OSPF on R5's RED service loopbacks.
2. On RED area 0 use area-default MD5, key **20 / RedCore20**. On RED area 10 use area-default simple authentication, secret **RedPlain**. BLUE credentials must remain unchanged. Establish three RED adjacencies while all nine BLUE adjacencies remain FULL.
3. On the RED ABR summarize R4's four RED campus /24s into the minimum exact aggregate, with LSA metric **70**. Do not change BLUE's ranges, metrics or suppression. On R1 compare the same aggregate in both RIBs and both LSDBs. Explain why identical next-hop IPs do not imply identical forwarding paths.
4. Redistribute only R5's four RED connected service /24s, using an exact prefix-list and dedicated route-map. Originate one minimum-size external aggregate with **E2 metric 60, tag 1505**. Do not redistribute the RED transit interfaces, Loopback1000 or Loopback1900. Compare its LSA origin, metric type, metric and tag to the identically addressed BLUE E1 aggregate.
5. From R4, send explicitly sourced pings to every R5 service .1 address in **each** VRF, using source 10.10.0.1 in each. Record RIB and CEF egress interfaces and capture packets on the corresponding R5-facing links to demonstrate that you reached the intended tenant. Explain why success to this duplicated address cannot by itself prove cross-VRF reachability or isolation.

## V3 — Resolve VRF incidents (20 minutes, 10 points)

Restore the full BLUE+RED baseline before each ticket. Apply only one of T6–T8 from `faults/`, preferably via a partner. These snippets contain spoilers. Do not restore full configs as a repair.

1. **T6 (6 minutes):** RED routing works, but one BLUE migration endpoint disappears. Identify its current routing context, restore the intended binding, address and OSPF activation, and prove no route remains in the wrong context.
2. **T7 (6 minutes):** RED neighbors remain FULL, but the RED campus aggregate is replaced by specific routes after work on an ABR. Inspect the correct process, repair only the RED range, and prove BLUE metrics and advertisements remain intact.
3. **T8 (6 minutes):** The R1–R5 RED adjacency expires after someone reuses a familiar key. Diagnose using interface, process and authentication evidence; restore the tenant's credential without changing the healthy BLUE adjacency.
4. Use the remaining two minutes to check both tenants' neighbor counts and the migration endpoints. For every incident record the smallest repair, relevant RIB/LSDB/VRF evidence, and impact on the other tenant.

## V4 — Prove isolation and failure independence (15 minutes, 15 points)

1. Execute the acceptance matrix below. Negative tests must pair an absent route/CEF lookup with a failed sourced ping; a timeout alone is insufficient. Do not use an overlapping destination as a negative isolation test. Verify no default route on R1's RED table can hide missing specific routes. BLUE NSSA/stub defaults stay within BLUE.
2. Shut **R1 Ethernet1/1 only**. Prove RED loses R5 reachability and its external aggregate; BLUE's identically addressed aggregate and BLUE R5 reachability must remain. Record the egress interfaces. Restore the link, wait for FULL and route recovery, then repeat the required positive tests.
3. Explain VRF versus OSPF process isolation, RD versus route target, and why an IP packet must arrive through the correct VRF-bound interface. Explain why this task demonstrates VRF-Lite rather than an MPLS L3VPN. Finish with STAGING removed, all interfaces enabled, and no route leaks, static routes, PBR, BGP or MPLS added.

| Router / context | Destination | Source | Required result |
|---|---|---|---|
| R1 BLUE | 198.18.0.5 | 198.18.0.1 | Reachable after migration; route only in BLUE |
| R1 RED | 198.18.0.5 | 10.255.0.1 | No route / unreachable; BLUE-only marker |
| R1 RED | 198.51.100.5 | 10.255.0.1 | Reachable; RED-only marker |
| R1 BLUE | 198.51.100.5 | 10.255.0.1 | No route / unreachable |
| R1 RED | 10.10.8.1 | 10.255.0.1 | No route / unreachable; BLUE-only campus subnet |
| R1 BLUE | 10.10.8.1 | 10.255.0.1 | Reachable |
| R1 global table | Both marker /32s and tenant service prefixes | No source required | No tenant routes; ordinary ping failure is supplementary only |
| R4 BLUE and RED separately | 172.20.16.1–19.1 | 10.10.0.1 | Success in each VRF, using its own egress and return path |

R1 is chosen for negative tests because it is neither the NSSA nor stub leaf with an intentional default. Never infer isolation by testing a locally owned duplicated address. Complete WORKBOOK Activity 9 afterward, keeping V4's evidence with the original acceptance results.
