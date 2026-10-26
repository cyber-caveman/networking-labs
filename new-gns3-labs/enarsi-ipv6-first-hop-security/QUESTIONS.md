# Original exam-style practice questions

Allow 20 minutes. Choose one answer unless explicitly told otherwise. Exhibits are simplified, constructed practice data. Each item is worth one practice point; no partial credit on multiple-answer or matching items. Answers and explanations are separate in SOLUTIONS.md.

## 1. Binding prerequisite

SW1 has an address-validation Source Guard policy on Ethernet0/1. H1's global unicast data is dropped. A capture shows packets arriving, and the FHS binding table has no entry for H1. Which action addresses the missing prerequisite while retaining enforcement?

A. Add `trusted` to Source Guard.
B. Configure appropriate snooping and verify H1's binding is learned on Ethernet0/1.
C. Configure DHCP server role in RA Guard.
D. Remove the source address from H1.

## 2. RA policy placement

Refer to the exhibit:

```text
interface Ethernet0/0
 description TO-R1
 ipv6 nd raguard attach-policy CLIENTS
!
ipv6 nd raguard policy CLIENTS
 device-role host
```

Authorized R1 RAs disappear across SW1. What is the best correction?

A. Change every client port to router role.
B. Remove all IPv6 snooping.
C. Apply a restricted router-role RA policy to Ethernet0/0.
D. Permit UDP port 547 in an IPv4 ACL.

## 3. DHCPv6 Guard (Choose two)

Which two statements describe the normal lab's intended DHCPv6 Guard behavior?

A. Client-role ports reject unauthorized server-originated Advertise/Reply traffic.
B. Guard installs H1's default route from DHCPv6 options.
C. The R1-facing port allows server messages satisfying its configured source check.
D. RA Guard's host role alone provides the DHCPv6 Guard requirement.
E. All DHCPv6 client messages must be dropped on client-role ports.

## 4. Observation mode

A snooping policy uses `security-level glean`. No other enforcement features are attached. Which conclusion is justified?

A. Every unbound IPv6 data source is blocked.
B. Snooping learns bindings, but this setting alone is not evidence of packet enforcement.
C. DHCPv6 is the only possible binding source.
D. All learned addresses must have been assigned by an authorized DHCP server.

## 5. Prefix Guard exhibit

```text
ipv6 source-guard policy BRANCH
 no validate address
 validate prefix
```

Assume the applicable learned prefix is `2001:db8:30::/64`, no trust bypass exists, and the source `2001:db8:30::1234` has no individual address binding. What does the configured mode validate?

A. Whether a BGP route for the destination exists.
B. Whether the packet contains an RA prefix-information option.
C. Whether the source is covered by an authorized applicable prefix binding.
D. Whether the destination was assigned by DHCPv6.

## 6. Destination Guard evidence

A ping to an unused LAN address times out both before and after Destination Guard is enabled. What additional observation best demonstrates the intended protection, with a cold adjacency and no recovery configured?

A. R1 stops generating NS for the unknown target while still resolving known bound targets.
B. R1 learns a default route from DHCPv6.
C. The ping timeout becomes shorter.
D. SW1 adds the unused address to its MAC table.

## 7. Match the feature to the requirement

Use each feature once: **Snooping, RA Guard, DHCPv6 Guard, Source Guard, Destination Guard, Prefix Guard**.

| Requirement | Feature |
|---|---|
| Learn address-to-link information from ND/DHCP traffic | |
| Restrict who can advertise IPv6 router information | |
| Stop server replies from an unauthorized DHCPv6 server | |
| Validate data sources against per-address bindings | |
| Avoid resolution for unknown on-link routed destinations | |
| Validate data sources against authorized address ranges | |

## 8. Two prefix checks

An engineer says `match ra prefix-list LAN-RA` makes Prefix Guard unnecessary. Which response is accurate?

A. Both commands filter every IPv6 packet's destination prefix.
B. RA prefix matching examines advertised prefixes; Prefix Guard validates data-packet source ranges.
C. Prefix Guard only checks RA flags.
D. Neither function can coexist with DHCPv6 Guard.

## 9. False negative test

The operator assigns a new IPv6 address to H1 Ethernet0/0, allows ND to populate its binding, then sends a ping from that address. The ping passes Source Guard. What is the best explanation?

A. Source Guard is necessarily broken.
B. Source Guard must block all new addresses forever.
C. The operator created a valid learned source, so this did not test an unknown source.
D. Every statically configured address automatically bypasses Source Guard.

## 10. Local database

SW1's table contains H1, but R1's FHS table does not. R1 has Destination Guard with always enforcement and no recovery; its H1 adjacency is absent. Which conclusion is correct?

A. SW1 automatically replicates its database to R1 in this lab.
B. R1's local binding precondition has not been met; populate and verify it before evaluating the positive test.
C. R2 must advertise H1 through OSPFv3.
D. Source Guard on H1 fixes every R1 database problem.

## 11. Continuous enforcement

The requirement states “suppress resolution for unknown targets even when the router is not stressed.” Which policy setting meets it?

A. `enforcement stressed`
B. `device-role client`
C. `enforcement always`
D. `trusted-port`

## 12. Binding evidence (Choose two)

Which two observations support a valid Source Guard test?

A. The authorized address is associated with the expected ingress port/VLAN in the FHS table.
B. The unbound-source ping fails, so no capture or return-route check is needed.
C. Only an IPv4 ARP entry exists.
D. The same negative-source traffic passes with enforcement detached and is dropped across the enforcement point when reattached.
E. A policy exists globally but has no attachment.
