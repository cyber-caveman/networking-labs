# ENARSI: IPv6 first-hop security

A five-device, multi-activity lab for **GNS3 2.2.56.1**. Covers IPv6 Snooping, RA Guard, DHCPv6 Guard, Source Guard, Destination Guard and Prefix Guard. Includes original scenario questions, configuration tasks, fault isolation, complete solution checkpoints and a portable project.

**Support status:** topology and configurations have been statically checked; no GNS3 import, Cisco parser or packet-forwarding test has been run. The preferred IOU images are used, but support for the six features is **unverified**. Complete [PREFLIGHT.md](PREFLIGHT.md) first. If a feature is absent or not enforced, complete its exhibit questions and use a Cisco platform/release supporting that feature for live testing. Command acceptance alone does not prove enforcement. The C3640 is not a substitute assumed to support these features.

## Start here

1. Import `ENARSI IPv6 First-Hop Security IOU.gns3project` into a fresh GNS3 project. Images and licenses are not included. Alternatively open `project.gns3` alongside its `project-files` directory.
2. Start the five nodes manually and complete [PREFLIGHT.md](PREFLIGHT.md).
3. Work through [WORKBOOK.md](WORKBOOK.md), Activities 0–7. Allow approximately 2–3 hours, excluding platform troubleshooting.
4. Complete [QUESTIONS.md](QUESTIONS.md) before reading [SOLUTIONS.md](SOLUTIONS.md).
5. Use [VALIDATION.md](VALIDATION.md) to record actual evidence. Consult [VERIFICATION.md](VERIFICATION.md) for the checks already performed and their limits.

These are original practice assignments using concise scenarios, exhibits, single-answer/multiple-answer items and outcome-based configuration requirements. They are not copied Cisco exam questions, Cisco-endorsed material, or a claim about the exact format or scoring of a live exam.

The verified [300-410 ENARSI v1.1 blueprint, objective 3.4](https://learningcontent.cisco.com/documents/marketing/exam-topics/300-410-ENARSI-v1.1.pdf) covers describing first-hop security, including RA Guard, DHCP Guard, the binding table, ND inspection/snooping and Source Guard. Configuration practice develops that understanding; Destination Guard and Prefix Guard are included as requested extensions. DHCPv6 testing also reinforces objective 4.4. See [SOURCES.md](SOURCES.md).

## Topology

```text
 H1 e0/0 -------- e0/1
                       SW1 e0/0 ------- e0/0 R1 e0/1 ------- e0/0 R2
 ROGUE e0/0 ----- e0/2       VLAN 10             routed transit
```

| Device | Interface | Address | Purpose |
|---|---|---|---|
| R1 | Ethernet0/0 | 2001:db8:10::1/64; fe80::1 | Authorized RA/DHCPv6 server and LAN gateway |
| R1 | Ethernet0/1 | 2001:db8:20::1/64; fe80::1 | Transit to R2; link-local reuse is on a different link |
| R2 | Ethernet0/0 | 2001:db8:20::2/64; fe80::2 | External source for routed-destination testing |
| H1 | Ethernet0/0 | 2001:db8:10::11/64; fe80::11 | Host emulated by an IOU router |
| ROGUE | Ethernet0/0 | 2001:db8:10::66/64; fe80::66 | Controlled unauthorized source |
| ROGUE | Loopback99 | 2001:db8:99::66/128 | Unlearned source for negative data tests |
| SW1 | Ethernet0/0–2 | Layer 2 access ports, VLAN 10 | FHS enforcement |

H1 and ROGUE have static defaults via R1. R2 has a route to the LAN via R1. R1 has a deliberate return route for `2001:db8:99::/64` via ROGUE: this makes the unprotected negative-source ping work and prevents a missing return route from masquerading as a guard drop. R2 is advertised as the DHCP DNS address only as an identifiable option; it is **not** running a DNS service.

H1 has a fixed address for repeatable tests. DHCPv6 is enabled temporarily in Activity 3, alongside that fixed address. H1 does not run SLAAC or rely on RAs to install its default route. Inspect packet captures to prove RA forwarding; a working H1 ping does not prove that RA Guard allows authorized RAs.

## Device defaults

SW1 uses `i86bi-linux-l2-adventerprisek9-15.2d.bin`, MD5 `f16db44433beb3e8c828db5ddad1de8a`, 256 MB RAM, four Ethernet adapters and no serial adapters. R1/R2/H1/ROGUE use `x86_64_crb_linux-adventerprisek9-ms.bin`, MD5 `4a2fce8de21d1831fbceffd155e41ae7`, 768 MB RAM each, four Ethernet and four serial adapters. All nodes use 512 KB NVRAM, the repository template IDs, `compute_id: local`, unique node/application IDs and automatic console allocation. Configured RAM totals 3328 MB, excluding GNS3 overhead.

## Checkpoints and reset

`startup-configs/` matches the unsolved configurations embedded in `project-files/iou/<node-id>/startup-config.cfg`. There are no guard policies in the initial state. The rogue RA and DHCP servers are initially inactive.

| Full configuration directory | State |
|---|---|
| `solutions/01-snooping/` | Activity 1 complete |
| `solutions/02-ra-guard/` | Activities 1–2 complete |
| `solutions/03-dhcpv6-guard/` | Activities 1–3 complete, temporary DHCP client removed |
| `solutions/04-source-guard/` | Activities 1–4 complete |
| `solutions/05-destination-guard/` | Activities 1–5 complete |
| `final-configs/` | Same as checkpoint 05; normal host-security state |
| `solutions/06-prefix-guard/` | Separate branch-router experiment; ROGUE is now an authorized prefix advertiser |

Each checkpoint contains **all five complete configs**. To load one, stop all nodes in a fresh import, use GNS3's startup configuration editor/import action for each node, then start them. Do not merge complete configs into an unknown running state. Dynamic bindings must be relearned; they are not packaged. Reimport the original archive to reset. After Activity 6 restore checkpoint 05 before Activity 7. Prefix Guard replaces per-address Source Guard on the branch port; their final states intentionally differ.

The archive bundles the workbook, questions, solutions, validation guidance and full configurations. Run `python3 validate.py` from this folder to check its integrity. Run `python3 package.py` to rebuild it after deliberate edits.
