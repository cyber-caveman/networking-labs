# Redistribution: verification index

6 projects checked on 2026-10-10. All installed GNS3 schema, endpoint/port, device-preference and archive-integrity checks passed. IOU NVRAM is 512 KB. Startup/final configuration analysis checks command contexts, effective bandwidth/delay, administrative state and mapped connectivity. Earlier conversions received a settings refresh without changing config text.

**No live testing:** command acceptance, services, protocol behavior, convergence, hardware-dependent features and forwarding require testing on the target server. Source limitations and reconstruction assumptions are listed per lab; preserving a source solution is not proof it satisfies every exercise goal.

| Lab review | Final configs | Notes |
| --- | ---: | --- |
| [expert-redistribution](expert-redistribution/VERIFICATION.md) | 0 | No completed final configs were supplied; none were invented. |
| [multipoint-one-way-redistribution](multipoint-one-way-redistribution/VERIFICATION.md) | 3 | Prior verification/source notes retained; NVRAM refreshed. |
| [one-way-redistribution](one-way-redistribution/VERIFICATION.md) | 3 | Prior verification/source notes retained; NVRAM refreshed. |
| [rip-eigrp-redistribution-route-tagging](rip-eigrp-redistribution-route-tagging/VERIFICATION.md) | 0 | No completed final configs were supplied; none were invented. |
| [rip-to-eigrp-redistribution](rip-to-eigrp-redistribution/VERIFICATION.md) | 6 | Prior verification/source notes retained; NVRAM refreshed. |
| [rip-to-ospf-redistribution](rip-to-ospf-redistribution/VERIFICATION.md) | 6 | Prior verification/source notes retained; NVRAM refreshed. |

## Earlier conversion review (historical)

The following records the prior configuration analysis and source defects. Current memory settings are 512 KB; the checks above supersede old memory/packaging values.

# Redistribution conversion verification

**6 projects, 29 IOU routers and 18 supplied final configs** checked against source commit `2a744b01522c3a774960769ea92414fc5d9b3a23`. This is configuration analysis, not live IOS testing.

## Checks completed

- All topology and IOU properties pass the installed GNS3 2.2.56.1 schemas. Every endpoint is a real port of its configured device; medium types and endpoint uniqueness match.
- Every router matches all L3/shared preferences in `AGENTS.md`. UUIDs and IOU application IDs are unique as required; consoles allocate automatically.
- Original peer connections, VLANs and Frame Relay PVC mappings are retained, except for documented reconstructions.
- Startup and final configurations were compared in command context, including addresses, BGP neighbor/policy settings, EIGRP processes and summaries, authentication, redistribution metrics/tags and ordered filters. Effective bandwidth, delay and interface state were checked separately so hardware replacement preserves routing metric inputs.
- Every portable archive passes ZIP integrity checks; its `project.gns3` and all bundled configuration files match the loose project files.

No remote-server access or router boot was performed. Image command support, actual adjacencies, route selection, convergence, clocks/key lifetimes, Frame Relay operation and forwarding require live verification. Preserving source configurations does not certify that every original solution meets every exercise goal.

## Per-lab findings

| Lab | Supplied final configs | Source limitations / notes |
| --- | ---: | --- |
| [expert-redistribution](expert-redistribution/VERIFICATION.md) | 0 | No completed solution configs were supplied; none were invented. |
| [multipoint-one-way-redistribution](multipoint-one-way-redistribution/VERIFICATION.md) | 3 | Configuration comparison passed; runtime behavior untested. |
| [one-way-redistribution](one-way-redistribution/VERIFICATION.md) | 3 | Configuration comparison passed; runtime behavior untested. |
| [rip-eigrp-redistribution-route-tagging](rip-eigrp-redistribution-route-tagging/VERIFICATION.md) | 0 | No completed solution configs were supplied; none were invented. |
| [rip-to-eigrp-redistribution](rip-to-eigrp-redistribution/VERIFICATION.md) | 6 | Configuration comparison passed; runtime behavior untested. |
| [rip-to-ospf-redistribution](rip-to-ospf-redistribution/VERIFICATION.md) | 6 | Configuration comparison passed; runtime behavior untested. |

## References

- [GNS3 project format](https://api.gns3.net/en/2.2/file_format.html)
- [Cisco EIGRP metrics and operation](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/16406-eigrp-toc.html)
