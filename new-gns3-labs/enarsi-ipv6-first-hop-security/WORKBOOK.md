# Candidate workbook

Do not read the solution directories during a scored attempt. Policy names are required to make review repeatable. Configure only the named devices. Preserve addresses, VLANs and routes except for explicitly requested experiments. An IPv6 traffic ACL is not an acceptable substitute for a requested guard feature. Capture outputs and packets for each acceptance criterion.

All exhibits below are **constructed practice data**, not captured IOU output. Complete Activities 1–5 cumulatively. Activity 6 uses a separate profile. The lab's 100-point rubric is a practice rubric, not Cisco's scoring system.

## Activity 0 — Establish the baseline (unscored, 10 minutes)

Complete the preflight. Confirm all four links and access VLAN 10. Use these tests before adding enforcement:

```text
H1# ping ipv6 2001:DB8:10::1 source 2001:DB8:10::11
H1# ping ipv6 2001:DB8:20::2 source 2001:DB8:10::11
R2# ping ipv6 2001:DB8:10::11 source 2001:DB8:20::2
ROGUE# ping ipv6 2001:DB8:10::1 source Loopback99
```

Use extended ping prompts if your image does not accept the inline source syntax. These tests must succeed before security changes. Capture R1–SW1 and SW1–H1 links in GNS3. R1's legitimate RAs should appear on both; use Wireshark `icmpv6.type == 134`. For timed RA tests capture at least a full advertised interval, or trigger a new RA by bouncing R1 Ethernet0/0 and wait for DAD to finish. Bouncing may also reset bindings; regenerate traffic afterward.

## Activity 1 — Build the binding database (10 points, 15 minutes)

An access switch must learn IPv6 endpoints before the next change window. The operator wants observation only during this stage.

1. Create SW1 snooping policy `LEARN`, explicitly enabling NDP and DHCP learning with security level `glean`.
2. Attach it to all three connected SW1 interfaces. Do not enable data-glean recovery, trust bypasses, or other guard features.
3. After attaching the policy, bounce H1 and ROGUE Ethernet0/0 separately, wait for DAD and send the baseline pings. Observe NS/NA packets and the FHS database.
4. Record H1 and ROGUE address, MAC, ingress interface and VLAN. Confirm `2001:db8:99::66` has **not** been learned on SW1. Stop and resolve unexpected learning before using it as a negative test.
5. Explain why a neighbor-cache entry on R1 does not establish the presence of an FHS binding on SW1.

Acceptance: correct attachments (4), valid host bindings (4), accurate distinction between observation and enforcement (2). The glean policy deliberately does not secure ownership; this is a teaching stage, not a complete production access policy.

## Activity 2 — Stop unauthorized RAs (15 points, 20 minutes)

A workstation has begun advertising itself as a default router. Only R1 may originate RAs in the normal host profile.

1. Create `RA-HOST` with host role; attach to SW1 Ethernet0/1 and Ethernet0/2.
2. Create `RA-ROUTER` with router role on Ethernet0/0. Its `RA-R1` IPv6 ACL must accept only sender `fe80::1`, and `LAN-RA` must accept exactly `2001:db8:10::/64` as an advertised prefix.
3. Do not configure `trusted-port`. Preserve legitimate RAs, RS, NS and NA behavior.
4. For the negative test, temporarily remove `ipv6 nd ra suppress all` from ROGUE Ethernet0/0. Capture SW1–ROGUE and SW1–H1. Verify RAs sourced by `fe80::66` enter SW1 but do not reach H1. Reapply suppression afterward.
5. Prove R1's RAs still reach H1, and baseline data connectivity remains intact.

Acceptance: host/router placement (5), sender/prefix restrictions (4), captures proving both outcomes (4), restore rogue suppression (2). A failed ping alone earns no RA-blocking evidence credit.

## Activity 3 — Stop unauthorized DHCPv6 service (15 points, 20 minutes)

R1 provides the authorized DHCPv6 service. Hosts must remain able to send client messages; server-originated traffic from access endpoints must be rejected.

1. Configure `DHCP-CLIENT` on SW1 Ethernet0/1 and Ethernet0/2, with client role.
2. Configure `DHCP-SERVER` on Ethernet0/0, with server role and source ACL `DHCP-R1` restricted to `fe80::1`. Do not add a trust bypass.
3. Temporarily enable `ipv6 address dhcp` on H1 Ethernet0/0, retaining `2001:db8:10::11/64`. Record the allocated address and server identity. Inspect R1's DHCP bindings. The captured server source must match the configured ACL; a mismatch is a troubleshooting finding.
4. In an isolated test, configure a competing DHCPv6 server on ROGUE using the stimulus in VALIDATION.md. Prove its server messages arrive on SW1 Ethernet0/2 and do not leave toward H1, while R1's exchange succeeds.
5. Remove H1's temporary DHCP client and ROGUE's temporary DHCP server/pool. Keep all guard policies.

Acceptance: placement/roles (5), restricted server source (3), successful authorized exchange and blocked rogue exchange (5), cleanup (2). Do not infer that DHCPv6 supplied H1's default route; H1's static route predates this test.

## Activity 4 — Enforce source bindings (15 points, 20 minutes)

The switch forwards packets from ROGUE's loopback source even though that source has no valid binding on its access port. Close this gap without blocking correctly learned endpoint traffic.

1. Reconfirm that the Loopback99 ping passes before attaching Source Guard, and that its address is absent from SW1's FHS database. Do not configure Loopback99's address on Ethernet0/0.
2. Create `SG-HOST` with address validation. Attach it to Ethernet0/1 and Ethernet0/2 only. Do not use `trusted`, a blanket link-local bypass, or `deny global-autoconf`.
3. Refresh H1/ROGUE bindings and repeat the normal-source tests. Then repeat the Loopback99 ping.
4. Capture the negative packet entering Ethernet0/2 and its absence on SW1–R1. Compare feature counters where available. Record the source/MAC/port/VLAN relationship in the binding database.
5. Explain why placing a new address on the LAN interface and allowing normal ND learning is a poor test of an **unknown** source.

Acceptance: interface placement and policy (5), preserved valid traffic (4), controlled negative test (4), explanation (2). Source Guard relies on the quality of the binding database; this lab's observation-level snooping does not claim to resist every forged ND ownership attack.

## Activity 5 — Protect routed neighbor resolution (15 points, 20 minutes)

R2 sends traffic toward unused addresses in the directly attached LAN. R1 should avoid initiating neighbor resolution for destinations absent from its own FHS database.

1. On R1 create `LAN-BINDINGS`, with NDP/DHCP learning and `security-level glean`, attached to Ethernet0/0. Do not enable destination recovery in this experiment.
2. Relearn H1 and ROGUE on **R1** by generating ND after attachment. Check R1's binding database; SW1's entries are not sufficient.
3. Create `DG-LAN`, using continuous enforcement, and attach to R1 Ethernet0/0.
4. Use R2 as the external source. Compare traffic to known H1 `2001:db8:10::11` and unused `2001:db8:10::dead`. Follow the cold-adjacency procedure in VALIDATION.md, including a control run with Destination Guard detached.
5. Explain why both protected and unprotected pings to an unused address time out, and what observation actually distinguishes them.

Acceptance: local binding population (4), policy and attachment (4), cold-adjacency positive test (3), unknown-target NS comparison (4). Do not apply the test to R2's directly connected transit address or use a same-VLAN H1-to-ROGUE ping as proof of routed Destination Guard behavior.

## Activity 6 — Validate a prefix rather than individual hosts (15 points, 20 minutes)

Use a fresh copy of checkpoint 05. In this **separate** experiment ROGUE represents an authorized branch router, retaining its label only for topology consistency. It may advertise `2001:db8:30::/64` as well as the transit LAN prefix, but it must not forward data sourced outside the permitted learned prefixes.

1. On SW1 Ethernet0/2 replace `LEARN` with `LEARN-PREFIX`: observation-level NDP/DHCP learning plus prefix gleaning.
2. Replace `RA-HOST` on that port with `RA-BRANCH`: router role, sender ACL `RA-BRANCH` allowing only `fe80::66`, and prefix list `BRANCH-RA` allowing exactly the LAN /64 and `2001:db8:30::/64`. Keep DHCP client-role enforcement.
3. Replace `SG-HOST` there with `PG-BRANCH`: disable address validation, enable prefix validation and permit link-local data. Keep H1's original per-address protection.
4. On ROGUE, remove RA suppression, set RA router lifetime to zero, advertise `2001:db8:30::/64`, and add Loopback30 address `2001:db8:30::66/128`. Do not add `99::/64` to its RA prefixes. On R1 add a return route for `2001:db8:30::/64` via `2001:db8:10::66`.
5. Wait for RAs and verify a **prefix** binding associated with the branch port. Do not accept a host /128 entry as equivalent evidence.
6. Ping R1's `2001:db8:10::1` from Loopback30, then Loopback99. The former should pass and the latter should be dropped at SW1. First prove both pass with the prefix policy temporarily detached; reattach before recording enforcement. Check no per-host binding for Loopback30 is needed for the prefix-mode result.
7. Explain the difference between `match ra prefix-list` and `validate prefix`. Restore checkpoint 05 afterward.

Acceptance: prefix learning and restricted RA admission (4), correct validation mode/attachment (4), positive/negative data captures with return routes (5), restored host profile (2). This is an RA-learned prefix experiment, not a DHCPv6-PD deployment. Prefix Guard also has delegated-prefix applications; this activity does not validate DHCPv6-PD.

## Activity 7 — Resolve three tickets (15 points, 20 minutes)

Start each ticket independently from checkpoint 05; restore it before the next ticket. Do not alter addressing, routes or client interfaces. For each ticket record the cause, smallest correction and a positive/negative verification pair. Three points per diagnosis/correction and two per evidence pair.

**Ticket A:** The intended R1 RA policy exists, but the effective attachment on SW1 Ethernet0/0 is `RA-HOST`. Authorized RAs no longer reach H1. Implement this fault by detaching `RA-ROUTER` and attaching `RA-HOST`. Restore authorized RAs without permitting ROGUE RAs.

**Ticket B:** `DHCP-CLIENT` contains `trusted-port`. On a platform where that option bypasses DHCP Guard checks, unauthorized server traffic reaches H1. Apply this one-line fault and reproduce the Activity 3 stimulus. Restore enforcement without preventing client requests. If the option is unavailable, analyze the supplied scenario rather than claiming a live reproduction.

**Ticket C:** `DG-LAN` has `enforcement stressed`. During a low-load test, unknown-target NS packets are still generated. Apply that change and repeat the unused-target test. Meet the original requirement for enforcement even under normal load. Relearn valid bindings before retesting H1.

Submit the worksheet in VALIDATION.md and your answers to QUESTIONS.md. Save the restored checkpoint-05 state with `copy running-config startup-config` on each node.
