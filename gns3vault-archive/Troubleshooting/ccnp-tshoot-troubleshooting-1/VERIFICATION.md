# CCNP TSHOOT Troubleshooting 1: conversion verification

Reviewed on 2026-10-10 for GNS3 **2.2.56.1** against the pre-conversion working-tree files. **Configuration analysis only; no devices were booted.**

## Project and startup checks

- 13 IOU devices (4 CLI switches), 0 Dynamips routers, 0 unmanaged Ethernet switches, 1 built-in Frame Relay switches and 0 clouds.
- All IOU image/checksum/template, RAM/NVRAM, adapter and common settings match `AGENTS.md`; NVRAM is 512 KB.
- Project and device properties pass the installed GNS3 schemas. Every link endpoint exists in GNS3’s actual port factory and connects compatible media. IDs are unique and console ports automatic.
- Link peers and interface identities match the source topology after conversion, except for the explicit source reconstructions below. VLAN/PVC mappings are preserved.
- Bundled startup configs match the loose startup files. The portable archive passes ZIP integrity checks and matches the project/config files.

## Supplied solution comparison

All **13 supplied final config files**, including any backup variants, were associated with a device and compared in command context. The comparison checks addressing and interface references, routing processes and metrics, authentication, ordered ACLs/route maps, service configuration and lab-specific policy statements. Physical-interface bandwidth/delay and administrative state were compared separately. Hardware-only removals and the documented default/transport adjustments are the only allowed differences.

| Configuration group | Statements checked in final configs |
| --- | ---: |
| switching | 71 |
| addressing | 40 |
| services | 43 |
| routing | 39 |
| policy | 2 |

This establishes preservation of the supplied configuration, subject to target-image support/defaults. It does not establish that a source solution is complete or correct, or that a reconstructed startup is identical to a missing original. Duplicate/conflicting source commands and solution variants have not been silently repaired.

## Source notes and reconstruction

Repaired missing source link endpoint R1 Serial0/1 from its original link description.

Repaired missing source link endpoint ISP Serial0/1 from its original link description.

ASW1: omitted unused hardware-only ports to fit the selected adapter count: Serial0/0, Serial0/1, Serial0/2, FastEthernet1/14, FastEthernet1/15.

ASW2: omitted unused hardware-only ports to fit the selected adapter count: Serial0/0, Serial0/1, Serial0/2, FastEthernet1/14, FastEthernet1/15.

DSW1: omitted unused hardware-only ports to fit the selected adapter count: Serial0/0, Serial0/1, Serial0/2, FastEthernet1/14, FastEthernet1/15.

DSW2: omitted unused hardware-only ports to fit the selected adapter count: Serial0/0, Serial0/1, Serial0/2, FastEthernet1/14, FastEthernet1/15.

## Live behavior not verified

Original faults in supplied startup configs are retained; reconstructed startups are explicitly identified. Command-context comparison does not establish that the source solution fixes every exercise fault. Validate the intended failure and the solution on running devices.

All platform-specific CLI acceptance, protocol state and packet forwarding are unverified. Start with `show ip interface brief`, the relevant neighbor/session and routing-table commands, then the exercise-specific verification commands and pings.
