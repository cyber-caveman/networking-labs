# Security: verification index

23 projects checked on 2026-10-10. All installed GNS3 schema, endpoint/port, device-preference and archive-integrity checks passed. IOU NVRAM is 512 KB. Startup/final configuration analysis checks command contexts, effective bandwidth/delay, administrative state and mapped connectivity. Earlier conversions received a settings refresh without changing config text.

**No live testing:** command acceptance, services, protocol behavior, convergence, hardware-dependent features and forwarding require testing on the target server. Source limitations and reconstruction assumptions are listed per lab; preserving a source solution is not proof it satisfies every exercise goal.

| Lab review | Final configs | Notes |
| --- | ---: | --- |
| [aaa-authentication](aaa-authentication/VERIFICATION.md) | 0 | The source project was empty. Rebuilt the diagram’s Lock–Fuzz link and addresses. The fictional AAA server and unspecified Fuzz Loopback0 address must be supplied for live AAA tests. No completed final configs were supplied; none were invented. |
| [aaa-command-authorization](aaa-command-authorization/VERIFICATION.md) | 0 | The source project was empty. Rebuilt the diagram’s Lock–Fuzz link and addresses. The fictional AAA server and unspecified Fuzz Loopback0 address must be supplied for live AAA tests. No completed final configs were supplied; none were invented. |
| [aaa-exec-authorization](aaa-exec-authorization/VERIFICATION.md) | 0 | The source project was empty. Rebuilt the diagram’s Lock–Fuzz link and addresses. The fictional AAA server and unspecified Fuzz Loopback0 address must be supplied for live AAA tests. No completed final configs were supplied; none were invented. |
| [acl-selective-ip-options-drop](acl-selective-ip-options-drop/VERIFICATION.md) | 2 | Configuration comparison passed; runtime untested. |
| [basic-zone-based-firewall](basic-zone-based-firewall/VERIFICATION.md) | 3 | Legacy .net topology converted; the original .net file remains a reference. |
| [control-place-policing](control-place-policing/VERIFICATION.md) | 3 | Configuration comparison passed; runtime untested. |
| [dynamic-access-list-lock-and-key](dynamic-access-list-lock-and-key/VERIFICATION.md) | 3 | Configuration comparison passed; runtime untested. |
| [extended-access-list](extended-access-list/VERIFICATION.md) | 3 | Configuration comparison passed; runtime untested. |
| [ios-firewall-cbac](ios-firewall-cbac/VERIFICATION.md) | 3 | Configuration comparison passed; runtime untested. |
| [ios-login-enhancements](ios-login-enhancements/VERIFICATION.md) | 2 | Configuration comparison passed; runtime untested. |
| [ip-fragment-filtering](ip-fragment-filtering/VERIFICATION.md) | 3 | Configuration comparison passed; runtime untested. |
| [ip-source-tracker](ip-source-tracker/VERIFICATION.md) | 9 | Configuration comparison passed; runtime untested. |
| [ip-traffic-export](ip-traffic-export/VERIFICATION.md) | 4 | Configuration comparison passed; runtime untested. |
| [named-access-list](named-access-list/VERIFICATION.md) | 3 | Configuration comparison passed; runtime untested. |
| [policy-based-routing-traffic-filtering](policy-based-routing-traffic-filtering/VERIFICATION.md) | 3 | Configuration comparison passed; runtime untested. |
| [reflexive-access-list](reflexive-access-list/VERIFICATION.md) | 3 | Configuration comparison passed; runtime untested. |
| [role-based-cli-access](role-based-cli-access/VERIFICATION.md) | 1 | Configuration comparison passed; runtime untested. |
| [standard-access-list](standard-access-list/VERIFICATION.md) | 3 | Configuration comparison passed; runtime untested. |
| [tcp-intercept](tcp-intercept/VERIFICATION.md) | 0 | No completed final configs were supplied; none were invented. |
| [tcp-intercept-watch-mode](tcp-intercept-watch-mode/VERIFICATION.md) | 3 | Configuration comparison passed; runtime untested. |
| [time-based-access-list](time-based-access-list/VERIFICATION.md) | 2 | Configuration comparison passed; runtime untested. |
| [transparent-ios-firewall](transparent-ios-firewall/VERIFICATION.md) | 3 | Configuration comparison passed; runtime untested. |
| [unicast-reverse-path-forwarding-urpf](unicast-reverse-path-forwarding-urpf/VERIFICATION.md) | 3 | Configuration comparison passed; runtime untested. |
