# ENARSI: VRF-Lite, OSPFv2 summarization and authentication

A difficult **eight-router, twelve-link** lab: the original four-area OSPF domain now runs in **VRF BLUE**, alongside a separate **VRF RED** on R1/R2/R4/R5. Tenants deliberately reuse transit, campus, loopback and service addresses. Different metrics, tags, authentication secrets and unique isolation probes distinguish them.

1. Import **ENARSI OSPFv2 Summarization and Authentication IOU.gns3project** into GNS3 **2.2.56.1** using **File → Import portable project**. The existing archive filename is retained, but its contents are the new VRF edition with a new project UUID. Import as a fresh project; do not merge it into a running copy of the previous lab.
2. Use installed image `x86_64_crb_linux-adventerprisek9-ms.bin`, MD5 `4a2fce8de21d1831fbceffd155e41ae7`. Each router has four Ethernet and four serial adapters, 768 MB RAM. Allow at least 6 GiB router RAM plus VM/GNS3 overhead. No images or licenses are included.
3. Open [TOPOLOGY.md](TOPOLOGY.md), [topology.svg](topology.svg), [WORKBOOK.md](WORKBOOK.md) and [VRF-ACTIVITIES.md](VRF-ACTIVITIES.md). Check image support and preconfigured addresses before starting your timer.
4. Execute **V1 → 1–7 → V2 → 8 → V3 → V4 → 9 → optional SHA**. There are thirteen required activities, including eight one-at-a-time fault tickets. Read [SOLUTIONS.md](SOLUTIONS.md), [VRF-SOLUTIONS.md](VRF-SOLUTIONS.md) and `final-configs/` only after attempting them.

## Starting and final states

All necessary IP addresses are preconfigured. BLUE/RED VRF definitions, RDs and interface bindings are provisioned to allow duplicate addresses from the start. **Loopback900 on R1 and R5 starts in the global table** for the migration exercise; you must restore its given IP address after moving it. No OSPF, summaries, authentication, redistribution or static routes are preconfigured.

V1 includes creating and deleting a temporary VRF, moving addressed interfaces, and diagnosing the address-clearing side effect. V2 builds independent RED routing and authentication; V3 adds tenant-specific faults; V4 proves isolation and failure independence. The original summarization/authentication tasks all run in BLUE. This is OSPF VRF-Lite without MPLS, BGP or route leaking. All final addressed interfaces belong to BLUE or RED; STAGING is absent.

The complete final files include BOTH tenants and the migrated interfaces. Core final configurations use NSSA translation aggregation on R6 and the completed BLUE MD5 rollover. The Stage A checkpoint changes only NSSA aggregation placement; the SHA variant changes only BLUE R6–R7 authentication. RED remains identical in all solved variants.

## Time budget

- **Timed complete core: 270 minutes (4½ hours)**: original activities 180 minutes plus VRF stations 90 minutes.
- First attempt with investigation: **6–8 hours**.
- Optional HMAC-SHA: **25–35 more minutes**, subject to image support; complete timed suite **295–305 minutes**.
- Experienced repeat target: **180–210 minutes**, including evidence and failure tests.

These are training estimates, not Cisco timings. The complete [300-410 ENARSI exam](https://www.cisco.com/site/us/en/learn/training-certifications/exams/enarsi.html) is 90 minutes; this deliberately oversized practice lab combines many skills and is intended for multiple timed stations. It contains original Cisco-style tasks, not actual exam questions.

## Files, reset and validation

- `startup-configs/`: readable starter configs; byte-identical copies under `project-files/iou/<node-id>/startup-config.cfg` boot in GNS3.
- `final-configs/`: all eight full BLUE+RED answers.
- `checkpoints/nssa-asbr-final-configs/`: full alternative NSSA Stage A answers; includes RED and migrated interfaces. During the original Activity 5, retain the current BLUE key 10 until Activity 7.
- `extensions/hmac-sha256/final-configs/`: full optional SHA variant; RED remains on MD5/simple authentication.
- `faults/`: T1–T5 target BLUE, T6–T8 exercise VRF membership, process scope and tenant credentials.
- `blue-baseline-contract.json`: pre-VRF configuration contract used to verify preservation of the original exercise's requirements within BLUE.
- [VERIFICATION.md](VERIFICATION.md): static checks, equivalence assessment and live-test limitations.

Reset by importing a fresh copy, or replacing each router's startup config with its corresponding full file and reloading without saving the old running config. Do not merge full configs into an already configured router: missing lines do not remove old VRFs, policies or keys. Retain console access while changing VRF bindings and authentication.

Run `python3 validate.py`. To rebuild in this repository: `python3 build.py`, then `python3 package.py`, then `python3 validate.py`. The builder reuses the repository's established IOU node schema. The portable document retains revision 9 / version 2.2.0 format for the GNS3 2.2.56.1 application. Configs declare VRFs and OSPF processes before interface activation, and interface VRF bindings before IP addresses.

No live GNS3 server was accessed. Actual VRF CLI support, boot, neighbor formation, forwarding, summary convergence and key rollover require validation on your image. Preflight the core VRF commands; SHA alone is an optional feature-gated extension.
