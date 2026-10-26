# Solutions and explanations

Use after completing the workbook. Full device configurations are in the six `solutions/` directories, not just command deltas. `final-configs/` is the complete normal host profile after Activity 5. Load checkpoints using the README procedure. These are documentation-based reference configurations subject to the feature preflight; they are not captured running configs from tested IOU devices.

## Configuration answer map

| Activity | Reference files | Essential result |
|---|---|---|
| 1 | `solutions/01-snooping/SW1.cfg` | LEARN attached on all three active switch ports; NDP/DHCP learning in glean mode |
| 2 | `solutions/02-ra-guard/SW1.cfg` | R1 port uses RA-ROUTER with source/prefix checks; H1/ROGUE ports use RA-HOST |
| 3 | `solutions/03-dhcpv6-guard/SW1.cfg` | DHCP-SERVER restricted to R1 source on e0/0; DHCP-CLIENT on e0/1–2 |
| 4 | `solutions/04-source-guard/SW1.cfg` | SG-HOST validates addresses on client ports only |
| 5 | `solutions/05-destination-guard/R1.cfg` | R1 learns local bindings and enforces DG-LAN on the LAN interface |
| 6 | `solutions/06-prefix-guard/{SW1,R1,ROGUE}.cfg` | Branch prefix learning, constrained RAs, prefix validation and return route |

Read the complete files for exact interface and policy commands. No policy in the intended answers uses `trusted` or `trusted-port`. `permit link-local` is used only in the branch prefix profile and intentionally permits link-local data there; it is not a general recommendation for every access port.

### Activity 1

The expected host records associate H1's fixed address and link-local address with SW1 Ethernet0/1, and ROGUE's LAN addresses with Ethernet0/2, in VLAN 10. MAC addresses are discovered at runtime and must not be guessed. Loopback99 does not perform LAN DAD as an Ethernet0/0 address. Normal-source traffic and post-attachment ND establish the positive-control records. If the platform still has no valid binding, investigate before enabling dependent guards.

Snooping's FHS database and a router's ordinary neighbor cache serve different consumers. Observing either does not establish the contents of the other. The explicit glean level is intentional so later RA and DHCP Guard tests are not masked by snooping's own guard-level rejection. A production policy may also need ownership enforcement, limits and tracking; that is outside this controlled comparison.

### Activity 2

`RA-HOST` rejects router advertisements on the endpoint ports. On e0/0, `RA-ROUTER` admits the expected router sender and advertised /64. Its ACL is a policy match input, not an interface traffic filter. The prefix list has no `le` expansion: the task permits the exact /64 advertisement. No trust bypass is needed. Neither Source Guard nor DHCPv6 Guard substitutes for RA admission control.

R1's valid RA must be observed at H1. H1's static address/default route deliberately keep the data tests deterministic and cannot demonstrate successful RA delivery. Rogue RA suppression must be restored after testing; stale routes on a different host implementation would require separate cleanup.

### Activity 3

The allowed server source is R1 Ethernet0/0's explicit `fe80::1`. Both unauthorized endpoint ports retain client role. DHCP client requests may pass, but this does not authorize those endpoints to serve clients. Confirm the source in actual server packets before concluding an ACL mismatch is an implementation failure.

The DHCP activity is temporary. A second acquired address does not replace the fixed test address in the other activities. R1's pool supplies addressing and identifiable DNS/domain options; no default-router option is used. Restoring the checkpoint removes the test client and rogue pool, but dynamic leases may outlive their configuration.

### Activity 4

SG-HOST applies only to endpoints. Applying it to the R1-facing port without planning for routed source ranges could break legitimate traffic arriving from R2. The negative test uses a source outside the endpoint's learned addresses, with a known return route and a previously successful unprotected control. Re-enabling binding recovery or learning that source changes the test's premise.

A static IP is not inherently illegitimate. It can be represented by a suitable learned or static binding. Conversely, a ping failure without evidence at the enforcement point is not proof of Source Guard.

### Activity 5

The guarded router is R1, so the required database is R1's. DG-LAN uses `enforcement always`. The test addresses are on R1's directly connected LAN, and R2 supplies transit traffic that requires R1 to route toward it. A known H1 with no existing adjacency should still resolve; a truly unknown target should not cause target-specific resolution in the controlled no-recovery test.

A ping to an unused address never returns a reply. Comparing its NS generation with and without the guard isolates the behavior being assessed. A warm neighbor cache can bypass the resolution event under test, so the workbook explicitly requires cold-adjacency evidence.

### Activity 6

The branch profile is a different trust scenario from the normal rogue-host profile. SW1 learns the permitted /64 from an authorized branch RA; the data source test then uses an address inside that range. The prefix policy has `no validate address` followed by `validate prefix`. Per-address learning is not the criterion for the branch's loopback source in this mode.

RA-BRANCH controls admission of advertisements; PG-BRANCH controls data sources. The branch may advertise the common LAN prefix and 30::/64, never 99::/64. The authorized branch has a zero default-router lifetime, and R1 uses an explicit route to reach its loopback. This exercise does not model how an ISP authorizes DHCPv6 prefix delegation. Restore all five checkpoint-05 configs to return to host mode.

### Activity 7: minimal corrections

Ticket A, SW1:

```text
configure terminal
interface Ethernet0/0
 no ipv6 nd raguard attach-policy RA-HOST
 ipv6 nd raguard attach-policy RA-ROUTER
end
```

The policy definition was correct; attachment selected host behavior on the router-facing port. Verify legitimate RAs pass and rogue RAs remain blocked.

Ticket B, SW1:

```text
configure terminal
ipv6 dhcp guard policy DHCP-CLIENT
 no trusted-port
end
```

The bypass undermined the intended client-role policy. Verify legitimate client/server exchange and reject server messages arriving from ROGUE. Remove the temporary DHCP stimulus afterward.

Ticket C, R1:

```text
configure terminal
ipv6 destination-guard policy DG-LAN
 enforcement always
end
```

`stressed` does not express the requested unconditional behavior. Check cold-adjacency resolution for known H1 and absence of target NS for the unbound address under normal load.

## Question answer key

| Question | Answer | Explanation |
|---|---|---|
| 1 | B | Establish the valid binding rather than bypassing the requested source check. A disables protection; C confuses feature roles; D removes connectivity. |
| 2 | C | The router port needs the restricted router-role policy. A expands router privileges, B removes unrelated learning, D has neither the correct protocol nor function. |
| 3 | A, C | These describe the client/server admission boundary. DHCPv6 does not supply the lab default route; RA Guard is a separate control; client traffic is not universally rejected. |
| 4 | B | Glean is observation. Learning is not proof of trusted assignment, and NDP can also supply bindings. |
| 5 | C | The policy selects prefix-based source validation. The other answers describe unrelated route, RA-payload or destination checks. |
| 6 | A | Target-specific NS behavior isolates resolution protection. Timeouts and their duration do not establish the drop mechanism. |
| 7 | Snooping; RA Guard; DHCPv6 Guard; Source Guard; Destination Guard; Prefix Guard | In table order. Each requirement names a different stage or object of validation. |
| 8 | B | The two checks protect different traffic and fields; an RA allowlist does not itself validate all data sources. |
| 9 | C | The source was learned before the test. Static addresses do not categorically bypass the policy. |
| 10 | B | No database replication is configured. Resolve the local learning precondition instead of changing routing protocols. |
| 11 | C | Always is the requested enforcement level. Stressed is conditional; the other options belong to other policy functions. |
| 12 | A, D | The correct binding and controlled before/after behavior support attribution to Source Guard. Failed pings, IPv4 ARP or unattached policies do not suffice. |

Score the questions out of 12 separately from the 100-point practical rubric. Award live evidence points only for observed results; record unavailable features separately, not as passes. A perfect configuration-analysis score is not a claim of successful packet enforcement.
