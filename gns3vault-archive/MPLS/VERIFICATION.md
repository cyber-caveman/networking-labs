# MPLS: verification index

13 projects checked on 2026-10-10. All installed GNS3 schema, endpoint/port, device-preference and archive-integrity checks passed. IOU NVRAM is 512 KB. Startup/final configuration analysis checks command contexts, effective bandwidth/delay, administrative state and mapped connectivity. Earlier conversions received a settings refresh without changing config text.

**No live testing:** command acceptance, services, protocol behavior, convergence, hardware-dependent features and forwarding require testing on the target server. Source limitations and reconstruction assumptions are listed per lab; preserving a source solution is not proof it satisfies every exercise goal.

| Lab review | Final configs | Notes |
| --- | ---: | --- |
| [advanced-mpls-vpn](advanced-mpls-vpn/VERIFICATION.md) | 12 | Legacy .net topology converted; the original .net file remains a reference. |
| [basic-mpls-vpn](basic-mpls-vpn/VERIFICATION.md) | 5 | PE1: solution final-configs/SP1.cfg uses a different hostname; associated by matching interface addresses. P: solution final-configs/SP2.cfg uses a different hostname; associated by matching interface addresses. PE2: solution final-configs/SP3.cfg uses a different hostname; associated by matching interface addresses. |
| [frame-mode-mpls](frame-mode-mpls/VERIFICATION.md) | 3 | Missing topology reconstructed from the diagram. Gepetto: missing startup recovered as addressing-only from final-configs/Gepetto.cfg; exercise routing/services were not inferred unless specified below. Figaro: missing startup recovered as addressing-only from final-configs/Figaro.cfg; exercise routing/services were not inferred unless specified below. Pinoccio: missing startup recovered as addressing-only from final-configs/Pinoccio.cfg; exercise routing/services were not inferred unless specified below. |
| [mpls-atom-pseudowire-ethernet-over-mpls-eompls](mpls-atom-pseudowire-ethernet-over-mpls-eompls/VERIFICATION.md) | 5 | Configuration comparison passed; runtime untested. |
| [mpls-atom-pseudowire-frame-relay-over-mpls-eompls](mpls-atom-pseudowire-frame-relay-over-mpls-eompls/VERIFICATION.md) | 5 | Configuration comparison passed; runtime untested. |
| [mpls-label-filtering](mpls-label-filtering/VERIFICATION.md) | 3 | Configuration comparison passed; runtime untested. |
| [mpls-ldp](mpls-ldp/VERIFICATION.md) | 4 | Configuration comparison passed; runtime untested. |
| [mpls-traffic-engineering-per-l2tpv3](mpls-traffic-engineering-per-l2tpv3/VERIFICATION.md) | 0 | No completed final configs were supplied; none were invented. |
| [mpls-traffic-engineering-per-vrf](mpls-traffic-engineering-per-vrf/VERIFICATION.md) | 0 | No completed final configs were supplied; none were invented. |
| [mpls-vpn-pe-ce-using-ospf](mpls-vpn-pe-ce-using-ospf/VERIFICATION.md) | 5 | Configuration comparison passed; runtime untested. |
| [mpls-vpn-pe-ce-using-rip](mpls-vpn-pe-ce-using-rip/VERIFICATION.md) | 5 | Configuration comparison passed; runtime untested. |
| [vrf-lite](vrf-lite/VERIFICATION.md) | 5 | Configuration comparison passed; runtime untested. |
| [vrf-routing](vrf-routing/VERIFICATION.md) | 2 | Configuration comparison passed; runtime untested. |
