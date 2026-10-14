# Live acceptance checklist

These are expected results, not captured router output. Record `show version`, image version, commands and actual results for all four devices when running the lab. Any `% Invalid input`, `% Incomplete command`, or `% Ambiguous command` during solution loading is a failure requiring investigation.

## 1. Underlay and syntax

- `show ip interface brief`: all linked Ethernet interfaces and configured loopbacks up/up; unused Ethernet0 ports shut.
- On R1: `ping 172.16.12.2`, `ping 172.16.13.2`, `ping 172.16.14.2`; expect success. Each branch must ping its `.1` peer.
- `show running-config | section router bgp`: confirm templates survived parsing, explicit remote AS, `no bgp default ipv4-unicast`, and address-family activation. No peer groups or unexpected neighbor overrides.
- `show ip bgp template peer-session` on all routers: EDGE-SESSION inherits SESSION-BASE, yielding password and 10/30 timers.
- On R1: `show ip bgp template peer-policy PREFERRED detail`, then BACKUP and LAST. Check EDGE-BASE, the correct PREF template, inbound/outbound prefix lists, maximum-prefix, and route map.
- `show ip bgp neighbors 172.16.12.2 policy detail` on R1; repeat for `.13.2` and `.14.2`. Inspect effective policies, not just template definitions.

## 2. Sessions, authentication and routes

| Check | Expected |
|---|---|
| R1 `show ip bgp summary` | Three Established neighbors; State/PfxRcd is numeric 2 for each after convergence |
| R2/R3/R4 `show ip bgp summary` | One Established neighbor; one received prefix |
| R1 `show ip bgp neighbors 172.16.12.2` (repeat for each) | Correct remote AS, established, negotiated hold 30 / keepalive 10 |
| R1 `show ip bgp` | Five distinct prefixes: local 10.1.0.0/24, three branch /24s, shared 203.0.113.0/24; three candidate paths for shared prefix |
| R1 `show ip bgp 203.0.113.0` | Best via 172.16.12.2, local preference 200, AS path 65102; alternatives 150/65103 and 100/65104 |
| R1 `show ip route 203.0.113.0` | Installed next hop 172.16.12.2 |
| R1 `show ip bgp neighbors 172.16.12.2 advertised-routes` (repeat) | Only 10.1.0.0/24 |
| R2/R3/R4 BGP table | Three local originated prefixes plus the hub /24; no other branch customer /24 |

R1 must have no BGP or RIB entries for `198.18.2.0/24`, `198.18.3.0/24`, or `198.18.4.0/24`. On the originating branch, `show ip bgp neighbors <hub-IP> advertised-routes` must include that branch's test prefix, proving the negative test reached the outbound advertisement stage. Do not interpret its local connected route as a filter failure. Do not use `received-routes` as a mandatory check: inbound soft-reconfiguration is not configured.

For an authentication negative test, on R2 temporarily override `neighbor 172.16.12.1 password WrongLabKey` in router BGP mode, then `clear ip bgp 172.16.12.1`. Confirm the session cannot reestablish. Remove the neighbor-level override using `no neighbor 172.16.12.1 password`, inspect the inherited password, clear that session again, and verify recovery. This affects only this isolated lab. Established authenticated sessions plus the mismatch test verify behavior more strongly than a config inspection alone.

## 3. Data plane and failover

1. R1: `ping 10.2.0.1 source Loopback10`; repeat for 10.3.0.1 and 10.4.0.1. Each branch: `ping 10.1.0.1 source Loopback10`. These source addresses have BGP return routes; Loopback0 addresses do not.
2. R1: `ping 203.0.113.1 source Loopback10`. Confirm the selected next hop with `show ip route 203.0.113.0`; the same service IP exists on all three branches, so ping alone does not prove which path won.
3. Shut R1 Ethernet0/0. After convergence, shared prefix best path must be 172.16.13.2 (local preference 150). Repeat the service ping. R2's unique customer route disappears, as expected.
4. Also shut R1 Ethernet0/1. Shared prefix must move to 172.16.14.2 (local preference 100), with service ping still working.
5. Restore Ethernet0/1 and Ethernet0/0 using `no shutdown`. Confirm three sessions, R2 preferred, all expected routes restored, and successful customer pings. Save configs.

Branches intentionally cannot reach other branches' customer networks: R1 exports only its own /24. Maximum-prefix enforcement is configured but not exercised by the baseline, which accepts only two prefixes per hub neighbor. To test it separately, temporarily lower R1 EDGE-BASE to `maximum-prefix 1`, observe the prefix-limit shutdown after re-evaluation, restore 10, and manually clear affected peers. Preserve logs and recover all sessions before saving.

## Troubleshooting order

Check interface state/subnets → TCP reachability and reciprocal AS/password → inherited session settings → AF activation → exact connected route for each network statement → effective policy/filter → local preference and next-hop resolution → return route for the chosen ping source. Changing a route policy may require `clear ip bgp <peer> soft in` or `soft out`; changing session authentication requires session reestablishment.
