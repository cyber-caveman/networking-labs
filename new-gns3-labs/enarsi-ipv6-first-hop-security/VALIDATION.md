# Live validation and evidence worksheet

These are procedures and expected results, **not completed tests**. Retain the ingress and egress capture files plus CLI evidence. Traffic volume is intentionally small: use five pings per test; no flood is needed. Keep the lab isolated from production networks.

## Common checks

```text
show version
show running-config
show interfaces status
show vlan brief
show ipv6 interface brief
show ipv6 route
show ipv6 neighbors
show ipv6 neighbors binding
show ipv6 snooping policy
show ipv6 nd raguard policy
show ipv6 dhcp guard policy
show ipv6 source-guard policy
show ipv6 destination-guard policy
```

Run only commands relevant to each device. Use contextual help for release-specific spellings described in PREFLIGHT.md. Policy display proves configuration/attachment, not packet disposition. `show ipv6 snooping capture-policy interface Ethernet0/2` and the supported snooping counter command can help locate a drop. Counter availability and names vary; paired packet captures are the primary evidence.

## Test matrix

| ID | Stage / generator | Positive control | Negative or comparison | Required observation |
|---|---|---|---|---|
| T0 | Startup / H1, R2, ROGUE | Baseline pings from workbook | None | Routes and all four links work before guards |
| T1 | 01 / bounce H1, then ping | H1 and ROGUE link addresses learned | Loopback99 remains absent | FHS bindings have correct VLAN, port and MAC |
| T2 | 02 / R1 and ROGUE RAs | fe80::1 RA arrives at H1 | fe80::66 RA blocked | Same rogue RA visible before SW1, absent after SW1 |
| T3 | 03 / H1 DHCP client | R1 Advertise/Reply reaches H1 | ROGUE server messages blocked | DHCP exchange and ingress/egress captures |
| T4 | 04 / ROGUE pings R1 | Source 2001:db8:10::66 passes | Source Loopback99 blocked | Unknown source absent from FHS table; dropped at SW1 |
| T5 | 05 / R2 pings LAN | Known H1 reachable with cold adjacency | Unknown ::dead produces no target NS with DG | Control without DG does generate target NS |
| T6 | 06 / ROGUE pings R1 | Loopback30 source allowed | Loopback99 blocked | Prefix binding on branch port, not individual host requirement |
| T7 | 05 + isolated faults | Legitimate service restored | Rogue/unknown tests still blocked | Before/after policy and packet evidence per ticket |

If a positive control fails, do not award negative-test credit. Investigate learning, return routes, RA source/prefix checks, overlapping policies, parser support and enforcement support first.

## RA stimulus and capture

On ROGUE, for Activity 2 only:

```text
configure terminal
interface Ethernet0/0
 no ipv6 nd ra suppress all
end
```

Observe `icmpv6.type == 134 && ipv6.src == fe80::66` on both SW1–ROGUE and SW1–H1. Wait for actual emissions; absence of any ingress RA invalidates the test. Restore `ipv6 nd ra suppress all` on ROGUE. Verify legitimate R1 RAs separately with source `fe80::1`. Do not confuse the IPv6 header Hop Limit with the Cur Hop Limit advertised inside the RA.

## DHCPv6 stimulus and cleanup

On ROGUE, in Activity 3:

```text
configure terminal
ipv6 dhcp pool BAD
 address prefix 2001:DB8:10::/64
 dns-server 2001:DB8:99::53
 domain-name rogue.example
exit
interface Ethernet0/0
 ipv6 dhcp server BAD
end
```

Keep rogue RA suppression active. The duplicate pool is deliberate and temporary: packets advertise competing service on the same LAN. No actual DNS server is needed. On H1:

```text
configure terminal
interface Ethernet0/0
 ipv6 address dhcp
end
show ipv6 dhcp interface
show ipv6 interface Ethernet0/0
```

Capture `dhcpv6` on SW1–H1, SW1–R1 and SW1–ROGUE. Identify server DUIDs and IPv6 source addresses; inspect Advertise and Reply messages, not just Solicit. Do not assume a winning server proves that another server was blocked. A server can lose selection while its messages still reach H1.

To start a fresh exchange, remove/reapply H1's DHCP address command and bounce its interface if necessary, retaining the fixed address. Verify a new Solicit in the capture. A guard-detached comparison on SW1 Ethernet0/2 may be used to show the rogue server is functional: detach only `DHCP-CLIENT`, capture its Advertise reaching H1, then reattach it and initiate another exchange. Snooping is set to glean and RA Guard does not replace DHCP Guard, so these do not intentionally mask this test.

Cleanup:

```text
! H1
configure terminal
interface Ethernet0/0
 no ipv6 address dhcp
end
! ROGUE
configure terminal
interface Ethernet0/0
 no ipv6 dhcp server BAD
exit
no ipv6 dhcp pool BAD
end
```

Check that the temporary address has been removed, all intended attachments remain, and the fixed-source baseline pings still work. A leased address may remain in a database until expiration; do not interpret a stale entry as fresh DHCP success.

## Source Guard stimulus

Confirm H1 and ROGUE's actual LAN addresses and link-local addresses have valid bindings. Use:

```text
ROGUE# ping ipv6 2001:DB8:10::1 source 2001:DB8:10::66
ROGUE# ping ipv6 2001:DB8:10::1 source Loopback99
```

The return route for Loopback99 already exists on R1. Capture request packets with `icmpv6.type == 128 && ipv6.src == 2001:db8:99::66`. Prove they leave ROGUE and disappear across SW1. If the address unexpectedly appears in SW1's binding database, first inspect data-glean, static entries and how the source was generated. Do not declare the guard defective based on a now-authorized source.

## Destination Guard: cold-adjacency test

1. Attach R1 snooping before the test. Bounce H1 Ethernet0/0 and send a fixed-source ping to R1. Verify H1 in **R1's FHS binding database**. R1's LAN policy is separate from SW1's.
2. Start captures on R2–R1 and R1–SW1. Use R2's source `2001:db8:20::2` for all probes, ensuring they traverse R1.
3. With DG detached, use an unused target `2001:db8:10::dead`, confirmed absent from all device configs, R1's bindings and R1's adjacency cache. Send five pings from R2. Observe R1's NS packets for that target. A cached INCOMPLETE entry from a previous attempt can change timing.
4. Let the unresolved entry expire or use the platform-supported selective neighbor-cache clear. Discover the exact `clear ipv6 neighbors ?` syntax first. This is an **adjacency-cache clear**, not a clear of FHS bindings. If only a broad clear is supported, immediately verify the FHS table afterward and relearn it if affected.
5. Attach `DG-LAN`, with `enforcement always`, to R1 Ethernet0/0. Verify the unknown target is still absent from both tables and repeat the exact R2 probe. Expect the request to enter R1 but no NS for that target on the LAN. Filter `icmpv6.type == 135 && icmpv6.nd.ns.target_address == 2001:db8:10::dead`.
6. Clear only H1's R1 neighbor/adjacency entry while retaining its valid FHS binding. Verify both conditions. From R2 ping `2001:db8:10::11`; expect resolution and replies. A warm-cache ping alone does not prove the known-destination resolution path.
7. If cache clearing also removes FHS state, relearn the binding and repeat the controlled separation. If the platform cannot expose or establish these preconditions, mark the cold-adjacency test inconclusive.

Both pings to ::dead time out because no host owns that address. The guard's observable benefit is suppressed unnecessary resolution. Background NS for other targets is not a failure. Keep recovery off for this controlled comparison.

## Prefix experiment

Load all configs in `solutions/06-prefix-guard/` if checking the reference solution. Learn H1/ROGUE again on SW1 and R1, and wait for the authorized branch RA. ROGUE advertises lifetime zero to avoid becoming a default router; a zero router lifetime does not remove its prefix-information options. R1's route to the branch prefix is static, not learned from those RAs.

Verify SW1's learned `2001:db8:30::/64` and branch-port association. Run:

```text
ROGUE# ping ipv6 2001:DB8:10::1 source Loopback30
ROGUE# ping ipv6 2001:DB8:10::1 source Loopback99
```

Both source prefixes have return routes on R1. Detach only `PG-BRANCH` first to prove both sources work, then reattach it: expect 30::66 allowed, 99::66 blocked. Compare captures on SW1 ingress and egress. Do not introduce 99::/64 through a static/prefix binding or an RA. A platform that cannot create the required prefix binding has not passed this activity. Restore full checkpoint 05; removing only one policy leaves branch-mode changes behind.

## Submission record

Copy this row for every test. Attach evidence outside the supplied reference configs.

| Test ID | Image/release | Preconditions demonstrated | Before/after commands | Ingress/egress capture filenames | Actual result | Pass / fail / unavailable / inconclusive |
|---|---|---|---|---|---|---|
| T0 | | | | | | |

For each failure distinguish configuration errors, unsupported CLI, absent enforcement and insufficient evidence. Save the corrected normal-profile configs only after successful verification.
