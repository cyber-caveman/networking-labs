# spanning-tree-root-guard: conversion verification

Reviewed on 2026-10-10 for GNS3 **2.2.56.1** against the pre-conversion working-tree files. **Configuration analysis only; no devices were booted.**

## Project and startup checks

- 3 IOU devices (3 CLI switches), 0 Dynamips routers, 0 unmanaged Ethernet switches, 0 built-in Frame Relay switches and 0 clouds.
- All IOU image/checksum/template, RAM/NVRAM, adapter and common settings match `AGENTS.md`; NVRAM is 512 KB.
- Project and device properties pass the installed GNS3 schemas. Every link endpoint exists in GNS3’s actual port factory and connects compatible media. IDs are unique and console ports automatic.
- Link peers and interface identities match the source topology after conversion, except for the explicit source reconstructions below. VLAN/PVC mappings are preserved.
- Bundled startup configs match the loose startup files. The portable archive passes ZIP integrity checks and matches the project/config files.

## Supplied solution comparison

All **3 supplied final config files**, including any backup variants, were associated with a device and compared in command context. The comparison checks addressing and interface references, routing processes and metrics, authentication, ordered ACLs/route maps, service configuration and lab-specific policy statements. Physical-interface bandwidth/delay and administrative state were compared separately. Hardware-only removals and the documented default/transport adjustments are the only allowed differences.

| Configuration group | Statements checked in final configs |
| --- | ---: |
| switching | 7 |

This establishes preservation of the supplied configuration, subject to target-image support/defaults. It does not establish that a source solution is complete or correct, or that a reconstructed startup is identical to a missing original. Duplicate/conflicting source commands and solution variants have not been silently repaired.

## Source notes and reconstruction

No source topology/startup set was supplied. Reconstructed links from the topology diagram; switches and endpoint routers start with hostnames only so the exercise configuration remains to be done. Original final snippets and backup variants are retained, including source errors.

## Live behavior not verified

Live verification must check VLAN/trunk forwarding, STP costs/roles/timers, EtherChannel negotiation, SVI routing and the exercise-specific security feature. Image support for private VLANs, VACLs, Flex Links, UDLD, ISL and hardware-dependent behavior is not established. Bandwidth settings preserve configured STP cost inputs, but verify operational costs with show spanning-tree. Automatic bridge IDs, port IDs and election timing may differ.

All platform-specific CLI acceptance, protocol state and packet forwarding are unverified. Start with `show ip interface brief`, the relevant neighbor/session and routing-table commands, then the exercise-specific verification commands and pings.

[GNS3 switching documentation](https://docs.gns3.com/docs/using-gns3/beginners/switching-and-gns3) describes the available switch emulation options; feature support still depends on the image. [Cisco STP command reference](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/lanswitch/command/lsw-cr-book/lsw-s2.html) describes path-cost inputs.
