# ENARSI BGP peer-session and peer-policy templates

Four-router exercise for GNS3 **2.2.56.1**, using the repository's preferred IOU L3 model. BGP syntax is checked against Cisco IOS XE 17.x documentation. **IOU is not IOS XE**; neither a live IOU run nor an IOS XE parser test has been performed. Cisco images and licenses are not included.

## Open the lab

Import `ENARSI BGP Peer Templates IOU.gns3project` through GNS3's portable-project import/open workflow into a new project directory. The installed image must match `x86_64_crb_linux-adventerprisek9-ms.bin` (MD5 `4a2fce8de21d1831fbceffd155e41ae7`). Each router uses 768 MB RAM, 512 KB NVRAM, four Ethernet adapters and four serial adapters; total configured router RAM is 3 GB. Nodes use `compute_id: local`, automatic console allocation, and the supplied IOU template ID.

Follow this README to complete the exercise. The canvas contains the topology title and addressing labels; exercise instructions are kept here. Full instructions and answers are also bundled in the portable project. Start the routers manually. The unpacked `project.gns3` must stay beside its `project-files` directory if opened directly.

## Topology and addressing

```text
                     R2 — AS 65102
                    /     172.16.12.0/30
R1 — AS 65000 ----- R3 — AS 65103
                    \     172.16.13.0/30
                     R4 — AS 65104
                          172.16.14.0/30
```

| Link | R1 interface/address | Remote interface/address |
|---|---|---|
| R1—R2 | Ethernet0/0, 172.16.12.1/30 | R2 Ethernet0/0, 172.16.12.2/30 |
| R1—R3 | Ethernet0/1, 172.16.13.1/30 | R3 Ethernet0/0, 172.16.13.2/30 |
| R1—R4 | Ethernet0/2, 172.16.14.1/30 | R4 Ethernet0/0, 172.16.14.2/30 |

The following addresses are already present in both the startup and final configs:

| Router | BGP AS to configure | Loopback0 / router ID | Loopback10 | Loopback100 | Loopback199 |
|---|---|---|---|---|---|
| R1 | 65000 | 1.1.1.1/32 | 10.1.0.1/24 | — | — |
| R2 | 65102 | 2.2.2.2/32 | 10.2.0.1/24 | 203.0.113.1/24 | 198.18.2.1/24 |
| R3 | 65103 | 3.3.3.3/32 | 10.3.0.1/24 | 203.0.113.1/24 | 198.18.3.1/24 |
| R4 | 65104 | 4.4.4.4/32 | 10.4.0.1/24 | 203.0.113.1/24 | 198.18.4.1/24 |

Loopback10 represents the customer network, Loopback100 the shared service, and Loopback199 a test prefix that R1 must reject. The duplicate service address intentionally models three independent origins of the same prefix, each in a separate AS and broadcast domain. Do not bridge the branches together.

## Initial state and objectives

All four startup configs contain interfaces, hostnames and console settings. There is **no BGP configuration**. There is no IGP or static routing. First confirm directly connected pings. From R1, pings to the branch customer addresses `10.2.0.1`, `10.3.0.1`, and `10.4.0.1` should fail initially. A branch ping to `203.0.113.1` reaches its own local loopback and does not prove remote connectivity. Use directly connected addresses for eBGP, not Loopback0; no update-source or ebgp-multihop is needed.

Complete these tasks without classic peer groups:

1. On every router, configure BGP with the AS above and its Loopback0 address as the router ID. Disable default IPv4 neighbor activation, then explicitly activate each peer under IPv4 unicast. Declare each neighbor's remote AS before attaching templates.
2. On every router create `SESSION-BASE`: keepalive 10 seconds, hold time 30 seconds, and the lab-only password `EnarsiBGP`. Create `EDGE-SESSION` inheriting `SESSION-BASE`. Apply `EDGE-SESSION` to every neighbor in router BGP mode. Keep these common settings in the templates.
3. Originate each router's Loopback10 /24. On each branch also originate `203.0.113.0/24` and its Loopback199 /24. Use exact network/mask statements; do not redistribute connected routes. Loopback0 and transit links must not be advertised.
4. On R1 create `EDGE-IN`, permitting exactly `10.2.0.0/24`, `10.3.0.0/24`, `10.4.0.0/24`, and `203.0.113.0/24`. Create `HUB-ONLY`, permitting exactly `10.1.0.0/24`. All other prefixes must be implicitly denied. This shared inbound filter is a lab-wide allowlist, not a per-customer anti-spoofing policy.
5. R1's `EDGE-BASE` peer-policy must apply `EDGE-IN` inbound, `HUB-ONLY` outbound, and `maximum-prefix 10` (enforcing, not warning-only).
6. Create R1 route maps `LP-200`, `LP-150`, and `LP-100`, each with a permit clause matching all routes and setting the indicated local preference. Create policies `PREF-200`, `PREF-150`, and `PREF-100` that attach these route maps inbound.
7. Create R1 policies `PREFERRED`, `BACKUP`, and `LAST`. Each inherits `EDGE-BASE` at sequence 10 and its corresponding `PREF-*` at sequence 20. On R1, attach `PREFERRED` to `172.16.12.2`, `BACKUP` to `172.16.13.2`, and `LAST` to `172.16.14.2` inside IPv4 unicast. No direct neighbor policy overrides are needed.
8. On each branch create a `HUB-ONLY` prefix list permitting exactly `10.1.0.0/24`, then create the `TO-HUB` peer-policy with `prefix-list HUB-ONLY in` and `maximum-prefix 10`. Attach `TO-HUB` in IPv4 unicast to that branch's R1 neighbor (`172.16.12.1`, `172.16.13.1`, or `172.16.14.1`). Intentionally leave branch outbound routes unfiltered so the hub must reject the test prefix.
9. Execute the checks in `VALIDATION.md`, including sequential failure of the R2 and R3 links. Restore both interfaces, verify R2 wins again, and save with `copy running-config startup-config`.

Explain why session settings belong outside the address family, why policy inheritance has sequence numbers, why activation is still explicit, and why the branches do not learn one another's networks. Optional experiment: change `SESSION-BASE` timers on both ends and inspect effective timers after resetting the sessions. Restore 10/30 afterward.

## Expected completed state

| Router | Established peers | Accepted prefixes from each peer | Policy outcome |
|---|---|---|---|
| R1 | R2, R3, R4 | Two: that branch's customer /24 and 203.0.113.0/24 | Reject all 198.18 test prefixes; export only 10.1.0.0/24 |
| R2 | R1 | One: 10.1.0.0/24 | Originate its three loopback /24s |
| R3 | R1 | One: 10.1.0.0/24 | Originate its three loopback /24s |
| R4 | R1 | One: 10.1.0.0/24 | Originate its three loopback /24s |

On R1, the shared service prefix must select R2 (local preference 200), then R3 (150) when R1 Ethernet0/0 is shut, then R4 (100) when Ethernet0/1 is also shut. Restore both links afterward. Source customer and service test pings from Loopback10 so the return route is advertised. Branch-to-branch customer traffic is intentionally unavailable.

## Full solutions and reset

`final-configs/R1.cfg` through `R4.cfg` are complete configurations, not command deltas. `startup-configs/` holds readable copies of the configs in `project-files/iou/<node-id>/startup-config.cfg`.

For a clean solution run, stop all nodes in a fresh imported copy. Use GNS3's per-node startup configuration editor/import action to replace each startup config with its corresponding `final-configs/Rn.cfg`, then start the nodes. If saved runtime state takes precedence, use a fresh project import. Avoid merging solutions into an unknown running configuration: old neighbor overrides and route-map entries may survive a merge.

To reset the exercise, reimport the original portable archive into a fresh directory. It always contains the unsolved startup state; final configs are separate attachments.

## Verification scope

Run `python3 validate.py` in this directory. It checks archive integrity and byte equality, node preferences, links and subnets, preserved interface state, template modes/references, reciprocal AS/password/timers, exact network origination, effective prefix policies, route-map preference values, and modeled failover order. It is a lab-specific static validator, **not a Cisco parser or BGP emulator**. See `VERIFICATION.md` for results and IOS XE references.
