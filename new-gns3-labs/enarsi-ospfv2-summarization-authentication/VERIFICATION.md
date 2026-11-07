# Verification scope — VRF revision

Run `python3 validate.py` for the current result. This is static configuration analysis with bounded topology/policy models, not an IOS CLI parser, OSPF emulator or live forwarding test.

## What changed and what was preserved

The original global-table domain is now BLUE/process 10. All original interface addresses, area assignments, network types, costs, authentication policies, summaries, redistribution filters, external metrics/tags, NSSA stages and stub behavior are preserved inside BLUE. The material additions are VRF membership, `capability vrf-lite`, and the two migrated Loopback900 /32s. Original destinations therefore have the same intended reachability and protocol behavior when observed in BLUE; global-table reachability intentionally disappears.

RED/process 20 adds three dedicated links on Ethernet1/x across R1/R2/R4/R5, overlapping connected/service prefixes, independent router IDs and secrets, a cost-70 internal summary, and a metric-60/tag-1505 E2 external summary. A RED-only marker and the BLUE-only migration endpoints provide unambiguous negative isolation probes. No route leak is configured. The portable archive has a new project UUID but keeps its existing filename.

All four sets (startup, core final, NSSA-ASBR checkpoint, SHA final) were regenerated. `blue-baseline-contract.json` records the pre-VRF parsed configuration for each set. The validator compares every original block against the migrated BLUE block, normalizing only descriptions, VRF bindings, the process heading and VRF-Lite capability. This checks preservation of actual policies, not only interface names. Additional checks cover the new interfaces and their intended tenant/process.

## Automated checks

- Eight preferred IOU routers, twelve valid links, known-working revision-9 format, image/adapter/RAM defaults, unique node/application/link IDs, automatic consoles and packaged startup paths.
- Byte-identical startup copies; identical addresses across all four stages; same-subnet peer endpoints; no duplicate local IP within one VRF. Duplicate addresses across BLUE/RED are intentional.
- VRF definitions and RDs, binding-before-address ordering, explicit process-to-VRF association, VRF-Lite capability, router IDs, passive interfaces and matching endpoint authentication. Only R1/R5 Loopback900 starts global; every addressed final interface is in a tenant VRF.
- BLUE's original exact /22+/23 coverage, suppression, alternate ABR costs, E1 redistribution selection and metric/tag, NSSA aggregation placement, Type-7 forwarding-address reachability configuration, default policies and discard defaults.
- RED's exact /22 cover and cost, separate connected selector, E2 metric/tag, process scope, credentials and marker origin. No unintended OSPF processes, BGP, static routes, import/export policy or PBR.
- BLUE predicted R1 campus metric 60, alternate cost 90 and E1 metric 50; RED predicted campus metric 80 and configured E2 metric 60. Contributor-set models cover partial/all-component withdrawal.
- A router/VRF graph models independent connected tenant domains with no inter-VRF edges. Removing RED's R1–R5 edge disconnects RED R5 while the BLUE path remains. This proves properties of the configured topology model, not an observed IOS RIB/FIB.
- Whole-config comparisons verify that solved variants change only the intended NSSA aggregation placement or BLUE R6–R7 SHA authentication; RED remains equivalent across variants.
- SVG/XML syntax, eight fault snippet files, ZIP CRCs, complete manifest and byte-for-byte equality of every bundled file.

## Live verification still required

No GNS3 server or Cisco image was accessed. Not run: GNS3 2.2.56.1 import/boot; core VRF command acceptance; interface address removal during migration; actual 12 FULL adjacencies; per-VRF Type-3/5/7 LSDBs; VRF-Lite PE-check behavior; Type-7 translation forwarding addresses; tags/metrics in installed routes; discard-route installation; timed withdrawal; isolation pings/captures; RED-only outage tests; nondisruptive MD5 rollover; or SHA feature support.

Before operational acceptance, execute V1–V4 and WORKBOOK Activity 9 on the actual image, plus both NSSA stages, both BLUE ABR failure cases, component withdrawal tests and MD5 rollover. Record route/CEF evidence for both positive and negative VRF tests, and capture egress links for duplicated destinations. SHA remains optional and capability-gated. Predictions in the solution guides are not fabricated router logs.
