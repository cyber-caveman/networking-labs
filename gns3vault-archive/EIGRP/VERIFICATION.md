# EIGRP: verification index

23 projects checked on 2026-10-10. All installed GNS3 schema, endpoint/port, device-preference and archive-integrity checks passed. IOU NVRAM is 512 KB. Startup/final configuration analysis checks command contexts, effective bandwidth/delay, administrative state and mapped connectivity. Earlier conversions received a settings refresh without changing config text.

**No live testing:** command acceptance, services, protocol behavior, convergence, hardware-dependent features and forwarding require testing on the target server. Source limitations and reconstruction assumptions are listed per lab; preserving a source solution is not proof it satisfies every exercise goal.

| Lab review | Final configs | Notes |
| --- | ---: | --- |
| [eigrp-authentication-rotating-key](eigrp-authentication-rotating-key/VERIFICATION.md) | 2 | Prior verification/source notes retained; NVRAM refreshed. |
| [eigrp-auto-summarization](eigrp-auto-summarization/VERIFICATION.md) | 3 | Prior verification/source notes retained; NVRAM refreshed. |
| [eigrp-beginner](eigrp-beginner/VERIFICATION.md) | 3 | Prior verification/source notes retained; NVRAM refreshed. |
| [eigrp-debug-as-number](eigrp-debug-as-number/VERIFICATION.md) | 0 | No completed final configs were supplied; none were invented. |
| [eigrp-hybrid-bandwidth-pacing](eigrp-hybrid-bandwidth-pacing/VERIFICATION.md) | 0 | No completed final configs were supplied; none were invented. |
| [eigrp-intermediate](eigrp-intermediate/VERIFICATION.md) | 4 | Prior verification/source notes retained; NVRAM refreshed. |
| [eigrp-ip-default-network](eigrp-ip-default-network/VERIFICATION.md) | 3 | Prior verification/source notes retained; NVRAM refreshed. |
| [eigrp-maximum-path-and-variance](eigrp-maximum-path-and-variance/VERIFICATION.md) | 3 | Prior verification/source notes retained; NVRAM refreshed. |
| [eigrp-md5-authentication](eigrp-md5-authentication/VERIFICATION.md) | 2 | Prior verification/source notes retained; NVRAM refreshed. |
| [eigrp-multipoint-bandwidth-pacing](eigrp-multipoint-bandwidth-pacing/VERIFICATION.md) | 0 | No completed final configs were supplied; none were invented. |
| [eigrp-over-frame-relay-with-multipoint-interface](eigrp-over-frame-relay-with-multipoint-interface/VERIFICATION.md) | 0 | No completed final configs were supplied; none were invented. |
| [eigrp-over-frame-relay-with-sub-interfaces](eigrp-over-frame-relay-with-sub-interfaces/VERIFICATION.md) | 0 | No completed final configs were supplied; none were invented. |
| [eigrp-point-to-point-bandwidth-pacing](eigrp-point-to-point-bandwidth-pacing/VERIFICATION.md) | 0 | No completed final configs were supplied; none were invented. |
| [eigrp-router-id](eigrp-router-id/VERIFICATION.md) | 3 | Prior verification/source notes retained; NVRAM refreshed. |
| [eigrp-split-horizon](eigrp-split-horizon/VERIFICATION.md) | 3 | Prior verification/source notes retained; NVRAM refreshed. |
| [eigrp-stub](eigrp-stub/VERIFICATION.md) | 6 | Prior verification/source notes retained; NVRAM refreshed. |
| [eigrp-stub-leak-map](eigrp-stub-leak-map/VERIFICATION.md) | 0 | No completed final configs were supplied; none were invented. |
| [eigrp-summarization](eigrp-summarization/VERIFICATION.md) | 3 | Prior verification/source notes retained; NVRAM refreshed. |
| [eigrp-summarization-leak-map](eigrp-summarization-leak-map/VERIFICATION.md) | 2 | Prior verification/source notes retained; NVRAM refreshed. |
| [eigrp-summarization-without-null0](eigrp-summarization-without-null0/VERIFICATION.md) | 0 | No completed final configs were supplied; none were invented. |
| [eigrp-timers](eigrp-timers/VERIFICATION.md) | 3 | Prior verification/source notes retained; NVRAM refreshed. |
| [eigrp-unicast](eigrp-unicast/VERIFICATION.md) | 3 | Prior verification/source notes retained; NVRAM refreshed. |
| [eigrp-variance-traffic-engineering](eigrp-variance-traffic-engineering/VERIFICATION.md) | 5 | Prior verification/source notes retained; NVRAM refreshed. |

## Earlier conversion review (historical)

The following records the prior configuration analysis and source defects. Current memory settings are 512 KB; the checks above supersede old memory/packaging values.

# EIGRP conversion verification

**23 projects, 77 IOU routers and 48 supplied final configs** checked against source commit `2a744b01522c3a774960769ea92414fc5d9b3a23`. This is configuration analysis, not live IOS testing.

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
| [eigrp-authentication-rotating-key](eigrp-authentication-rotating-key/VERIFICATION.md) | 2 | No source topology/startups were supplied. Reconstructed the serial link from the diagram and final configs; startup preserves EIGRP AS12 and addressing but omits authentication/key chains. Original key lifetimes expired in 2021. Set lab clocks to the historical exercise window before testing rollover; dates remain unchanged. The supplied Key2 lifetimes start at 08:45, while the goal specifies 08:50. |
| [eigrp-auto-summarization](eigrp-auto-summarization/VERIFICATION.md) | 3 | Configuration comparison passed; runtime behavior untested. |
| [eigrp-beginner](eigrp-beginner/VERIFICATION.md) | 3 | Configuration comparison passed; runtime behavior untested. |
| [eigrp-debug-as-number](eigrp-debug-as-number/VERIFICATION.md) | 0 | No completed solution configs were supplied; none were invented. |
| [eigrp-hybrid-bandwidth-pacing](eigrp-hybrid-bandwidth-pacing/VERIFICATION.md) | 0 | No completed solution configs were supplied; none were invented. |
| [eigrp-intermediate](eigrp-intermediate/VERIFICATION.md) | 4 | No source startups were supplied. Recovered addressing from final configs, enabled the initial connected links and left routing/policies unconfigured for the exercise. The recovered initial state excludes the additional Loopback10–13 exercise networks. Source final configs contain only one of R3’s four requested loopbacks, and no R2 Loopback1; these source solution omissions are retained. |
| [eigrp-ip-default-network](eigrp-ip-default-network/VERIFICATION.md) | 3 | Configuration comparison passed; runtime behavior untested. |
| [eigrp-maximum-path-and-variance](eigrp-maximum-path-and-variance/VERIFICATION.md) | 3 | Configuration comparison passed; runtime behavior untested. |
| [eigrp-md5-authentication](eigrp-md5-authentication/VERIFICATION.md) | 2 | Configuration comparison passed; runtime behavior untested. |
| [eigrp-multipoint-bandwidth-pacing](eigrp-multipoint-bandwidth-pacing/VERIFICATION.md) | 0 | No completed solution configs were supplied; none were invented. |
| [eigrp-over-frame-relay-with-multipoint-interface](eigrp-over-frame-relay-with-multipoint-interface/VERIFICATION.md) | 0 | No completed solution configs were supplied; none were invented. |
| [eigrp-over-frame-relay-with-sub-interfaces](eigrp-over-frame-relay-with-sub-interfaces/VERIFICATION.md) | 0 | No completed solution configs were supplied; none were invented. |
| [eigrp-point-to-point-bandwidth-pacing](eigrp-point-to-point-bandwidth-pacing/VERIFICATION.md) | 0 | No completed solution configs were supplied; none were invented. |
| [eigrp-router-id](eigrp-router-id/VERIFICATION.md) | 3 | Configuration comparison passed; runtime behavior untested. |
| [eigrp-split-horizon](eigrp-split-horizon/VERIFICATION.md) | 3 | Configuration comparison passed; runtime behavior untested. |
| [eigrp-stub](eigrp-stub/VERIFICATION.md) | 6 | Configuration comparison passed; runtime behavior untested. |
| [eigrp-stub-leak-map](eigrp-stub-leak-map/VERIFICATION.md) | 0 | No completed solution configs were supplied; none were invented. |
| [eigrp-summarization](eigrp-summarization/VERIFICATION.md) | 3 | Configuration comparison passed; runtime behavior untested. |
| [eigrp-summarization-leak-map](eigrp-summarization-leak-map/VERIFICATION.md) | 2 | Configuration comparison passed; runtime behavior untested. |
| [eigrp-summarization-without-null0](eigrp-summarization-without-null0/VERIFICATION.md) | 0 | No source topology or configs were supplied. Reconstructed the two-router link and visible addresses from the diagram; routing remains unconfigured. No completed solution configs were supplied; none were invented. |
| [eigrp-timers](eigrp-timers/VERIFICATION.md) | 3 | Configuration comparison passed; runtime behavior untested. |
| [eigrp-unicast](eigrp-unicast/VERIFICATION.md) | 3 | Configuration comparison passed; runtime behavior untested. |
| [eigrp-variance-traffic-engineering](eigrp-variance-traffic-engineering/VERIFICATION.md) | 5 | Configuration comparison passed; runtime behavior untested. |

## References

- [GNS3 project format](https://api.gns3.net/en/2.2/file_format.html)
- [Cisco EIGRP metrics and operation](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/16406-eigrp-toc.html)
