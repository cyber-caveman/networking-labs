# eigrp-intermediate-startup-configs: conversion verification

Configuration analysis for GNS3 **2.2.56.1**, against source files at repository commit `2a744b01522c3a774960769ea92414fc5d9b3a23`. No routers were booted for this review.

## Topology and startup state

- 4 IOU L3 routers follow all device and shared settings in `AGENTS.md`; console ports are automatic.
- 4 links pass the installed GNS3 schemas and port-factory checks. Peer and port identities match the source topology after interface mapping, except for the documented reconstructed sources below.
- All 4 startup configs match their bundled `project-files/iou/<node-id>/startup-config.cfg` copies. Addressing, routing-process presence and administrative states were compared with the source or the documented reconstructed initial state.
- Unmanaged switches, where present, retain their types and VLAN/PVC mappings. Frame Relay connections use ANSI LMI for the built-in switch.

## Supplied solution analysis

All **4 supplied final configs** passed command-context comparison after interface mapping and removal of obsolete hardware commands. This comparison includes policy ordering and references, protocol network statements and identifiers, authentication/key configuration, redistribution metrics and tags, static routes, and Frame Relay mappings.

Effective physical-interface bandwidth, delay and administrative state were checked separately against the source, including explicit overrides. FastEthernet-to-Ethernet conversions explicitly retain 100000 Kbit/s bandwidth and delay 10 where those source defaults apply. This retains EIGRP metric inputs, pacing bandwidth and OSPF cost inputs. Configured EIGRP automatic-summary choices are explicit in the supplied processes and are retained.

| Router | Source solution | Routing processes retained |
| --- | --- | --- |
| R1 | `R1-show-run-2017-10-26-13-11-43-clean.cfg` | eigrp 1 |
| R2 | `R2-show-run-2017-10-26-13-11-54-clean.cfg` | eigrp 1 |
| R4 | `R4-show-run-2017-10-26-13-12-13-clean.cfg` | eigrp 1 |
| R3 | `R3-show-run-2017-10-26-13-12-04-clean.cfg` | eigrp 1 |

Lab-relevant configuration groups found and compared:

- Policy attachment and ordered filtering rules: 2 matching statements retained (interface references adapted).
- EIGRP metrics, variance, summarization and stub behavior: 15 matching statements retained (interface references adapted).
- Redistribution seed metrics, route maps and route tags: 1 matching statements retained (interface references adapted).
- Authentication mode, key chains and key lifetimes: 10 matching statements retained (interface references adapted).
- OSPF/RIP areas, networks, costs and timers: 16 matching statements retained (interface references adapted).

## Source limitations and reconstruction

No source startups were supplied. Recovered addressing from final configs, enabled the initial connected links and left routing/policies unconfigured for the exercise.

The recovered initial state excludes the additional Loopback10–13 exercise networks. Source final configs contain only one of R3’s four requested loopbacks, and no R2 Loopback1; these source solution omissions are retained.

## Runtime verification still needed

Configuration equivalence preserves source behavior, including source mistakes. The target image has not been booted: command acceptance, neighbor formation/authentication, BGP path selection, EIGRP feasible successors and variance, redistribution feedback prevention, Frame Relay PVC state, routing tables and packet forwarding remain unverified. Timer/key-lifetime behavior also depends on the running clock.

Import the portable project, confirm interfaces and neighbors (`show ip interface brief`, `show ip bgp summary`, `show ip eigrp neighbors`, or the relevant IGP), apply the supplied solutions when appropriate, and check the exercise-specific routes and end-to-end pings. For redistribution inspect external metrics and tags; for Frame Relay inspect `show frame-relay pvc`.

## 2026-10-10 settings refresh

All IOU devices now use 512 KB NVRAM. Other device settings were checked against `AGENTS.md`. Config text is byte-for-byte unchanged from the previously converted working tree; startup and solution behavior was not altered by this memory-setting change. Switch port lists were normalized where needed so GNS3’s port indices match the saved link endpoints. Projects pass the installed schemas and real port-factory checks; portable archives were rebuilt and checked against loose files. Prior source limitations remain. No live router testing was performed.
