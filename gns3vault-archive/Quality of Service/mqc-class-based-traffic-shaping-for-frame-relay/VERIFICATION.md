# MQC Class-Based Traffic Shaping for Frame-Relay: conversion verification

Reviewed on 2026-10-10 for GNS3 **2.2.56.1** against the pre-conversion working-tree files. **Configuration analysis only; no devices were booted.**

## Project and startup checks

- 4 IOU devices (0 CLI switches), 0 Dynamips routers, 0 unmanaged Ethernet switches, 1 built-in Frame Relay switches and 0 clouds.
- All IOU image/checksum/template, RAM/NVRAM, adapter and common settings match `AGENTS.md`; NVRAM is 512 KB.
- Project and device properties pass the installed GNS3 schemas. Every link endpoint exists in GNS3’s actual port factory and connects compatible media. IDs are unique and console ports automatic.
- Link peers and interface identities match the source topology after conversion, except for the explicit source reconstructions below. VLAN/PVC mappings are preserved.
- Bundled startup configs match the loose startup files. The portable archive passes ZIP integrity checks and matches the project/config files.

## Supplied solution comparison

All **4 supplied final config files**, including any backup variants, were associated with a device and compared in command context. The comparison checks addressing and interface references, routing processes and metrics, authentication, ordered ACLs/route maps, service configuration and lab-specific policy statements. Physical-interface bandwidth/delay and administrative state were compared separately. Hardware-only removals and the documented default/transport adjustments are the only allowed differences.

| Configuration group | Statements checked in final configs |
| --- | ---: |
| addressing | 6 |
| routing | 8 |
| services | 9 |
| policy | 9 |

This establishes preservation of the supplied configuration, subject to target-image support/defaults. It does not establish that a source solution is complete or correct, or that a reconstructed startup is identical to a missing original. Duplicate/conflicting source commands and solution variants have not been silently repaired.

## Source notes and reconstruction

Jack: missing startup recovered as addressing-only from final-configs/Jack.cfg; exercise routing/services were not inferred unless specified below.

Jack: retained basic Frame Relay encapsulation, addressing and DLCI maps as transport prerequisites; QoS policies remain unconfigured.

James: missing startup recovered as addressing-only from final-configs/James.cfg; exercise routing/services were not inferred unless specified below.

James: retained basic Frame Relay encapsulation, addressing and DLCI maps as transport prerequisites; QoS policies remain unconfigured.

Kos: missing startup recovered as addressing-only from final-configs/Kos.cfg; exercise routing/services were not inferred unless specified below.

Kos: retained basic Frame Relay encapsulation, addressing and DLCI maps as transport prerequisites; QoS policies remain unconfigured.

Quall: missing startup recovered as addressing-only from final-configs/Quall.cfg; exercise routing/services were not inferred unless specified below.

Quall: retained basic Frame Relay encapsulation, addressing and DLCI maps as transport prerequisites; QoS policies remain unconfigured.

## Live behavior not verified

Policy classes, attachment points, marking, policing/shaping rates, queue parameters and configured bandwidth inputs are preserved where supplied. Actual scheduler behavior, congestion, throughput, compression, FRF.12, RSVP and hardware queue/ring commands require live validation; an emulated interface does not reproduce physical throughput just because its bandwidth value matches.

All platform-specific CLI acceptance, protocol state and packet forwarding are unverified. Start with `show ip interface brief`, the relevant neighbor/session and routing-table commands, then the exercise-specific verification commands and pings.
