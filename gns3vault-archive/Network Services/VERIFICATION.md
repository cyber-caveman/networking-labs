# Network Services: verification index

39 projects checked on 2026-10-10. All installed GNS3 schema, endpoint/port, device-preference and archive-integrity checks passed. IOU NVRAM is 512 KB. Startup/final configuration analysis checks command contexts, effective bandwidth/delay, administrative state and mapped connectivity. Earlier conversions received a settings refresh without changing config text.

**No live testing:** command acceptance, services, protocol behavior, convergence, hardware-dependent features and forwarding require testing on the target server. Source limitations and reconstruction assumptions are listed per lab; preserving a source solution is not proof it satisfies every exercise goal.

| Lab review | Final configs | Notes |
| --- | ---: | --- |
| [dhcp-authorized-arp](dhcp-authorized-arp/VERIFICATION.md) | 3 | Configuration comparison passed; runtime untested. |
| [dhcp-proxy](dhcp-proxy/VERIFICATION.md) | 3 | Configuration comparison passed; runtime untested. |
| [dhcp-relay](dhcp-relay/VERIFICATION.md) | 4 | Configuration comparison passed; runtime untested. |
| [dhcp-server](dhcp-server/VERIFICATION.md) | 2 | Configuration comparison passed; runtime untested. |
| [dhcp-server-on-demand-addres-pool](dhcp-server-on-demand-addres-pool/VERIFICATION.md) | 2 | Configuration comparison passed; runtime untested. |
| [distribute-list-filtering](distribute-list-filtering/VERIFICATION.md) | 3 | Configuration comparison passed; runtime untested. |
| [dns-server](dns-server/VERIFICATION.md) | 4 | Configuration comparison passed; runtime untested. |
| [floating-static-routes](floating-static-routes/VERIFICATION.md) | 2 | Configuration comparison passed; runtime untested. |
| [glbp-gateway-load-balancing-protocol](glbp-gateway-load-balancing-protocol/VERIFICATION.md) | 5 | Configuration comparison passed; runtime untested. |
| [hot-standby-routing-protocol](hot-standby-routing-protocol/VERIFICATION.md) | 5 | Configuration comparison passed; runtime untested. |
| [icmp-router-discovery-protocol-irdp](icmp-router-discovery-protocol-irdp/VERIFICATION.md) | 4 | Configuration comparison passed; runtime untested. |
| [integrated-routing-and-bridging](integrated-routing-and-bridging/VERIFICATION.md) | 3 | Configuration comparison passed; runtime untested. |
| [ip-directed-broadcast](ip-directed-broadcast/VERIFICATION.md) | 3 | Configuration comparison passed; runtime untested. |
| [ip-event-dampening](ip-event-dampening/VERIFICATION.md) | 3 | Configuration comparison passed; runtime untested. |
| [ip-output-packet-accounting](ip-output-packet-accounting/VERIFICATION.md) | 3 | Wodan: missing startup recovered as addressing-only from final-configs/Wodan.cfg; exercise routing/services were not inferred unless specified below. |
| [ip-precedence-and-mac-address-accounting](ip-precedence-and-mac-address-accounting/VERIFICATION.md) | 3 | Wodan: missing startup recovered as addressing-only from final-configs/Wodan.cfg; exercise routing/services were not inferred unless specified below. |
| [ip-service-level-agreement-sla](ip-service-level-agreement-sla/VERIFICATION.md) | 4 | Configuration comparison passed; runtime untested. |
| [longest-prefix-match-routing](longest-prefix-match-routing/VERIFICATION.md) | 2 | Configuration comparison passed; runtime untested. |
| [nat-and-route-map](nat-and-route-map/VERIFICATION.md) | 4 | Configuration comparison passed; runtime untested. |
| [nat-dynamic](nat-dynamic/VERIFICATION.md) | 4 | Configuration comparison passed; runtime untested. |
| [nat-extendable](nat-extendable/VERIFICATION.md) | 3 | Configuration comparison passed; runtime untested. |
| [nat-overlapping-networks](nat-overlapping-networks/VERIFICATION.md) | 4 | Legacy .net topology converted; the original .net file remains a reference. |
| [nat-pat-overload](nat-pat-overload/VERIFICATION.md) | 4 | Legacy .net topology converted; the original .net file remains a reference. |
| [nat-port-forwarding](nat-port-forwarding/VERIFICATION.md) | 4 | Configuration comparison passed; runtime untested. |
| [nat-static](nat-static/VERIFICATION.md) | 3 | Configuration comparison passed; runtime untested. |
| [nat-tcp-load-balancing](nat-tcp-load-balancing/VERIFICATION.md) | 5 | WWW2: source config hostname WWW2 is duplicated; original topology label retained. WWW3: source config hostname WWW2 is duplicated; original topology label retained. |
| [nat-virtual-interface](nat-virtual-interface/VERIFICATION.md) | 3 | Configuration comparison passed; runtime untested. |
| [odr-on-demand-routing](odr-on-demand-routing/VERIFICATION.md) | 3 | Configuration comparison passed; runtime untested. |
| [policy-based-routing](policy-based-routing/VERIFICATION.md) | 5 | Configuration comparison passed; runtime untested. |
| [prefix-list-filtering](prefix-list-filtering/VERIFICATION.md) | 2 | Configuration comparison passed; runtime untested. |
| [proxy-arp](proxy-arp/VERIFICATION.md) | 5 | Configuration comparison passed; runtime untested. |
| [recursive-routing-failure](recursive-routing-failure/VERIFICATION.md) | 3 | Configuration comparison passed; runtime untested. |
| [router-on-a-stick](router-on-a-stick/VERIFICATION.md) | 3 | Configuration comparison passed; runtime untested. |
| [server-load-balancing-slb](server-load-balancing-slb/VERIFICATION.md) | 5 | Configuration comparison passed; runtime untested. |
| [static-pat-port-forwarding](static-pat-port-forwarding/VERIFICATION.md) | 5 | Configuration comparison passed; runtime untested. |
| [tclsh-scripting](tclsh-scripting/VERIFICATION.md) | 0 | Missing startup addresses reconstructed from the supplied diagram; routing to the loopbacks is left as an exercise goal. No completed final configs were supplied; none were invented. |
| [udp-forwarding](udp-forwarding/VERIFICATION.md) | 3 | Configuration comparison passed; runtime untested. |
| [vrrp-virtual-router-redundancy-protocol](vrrp-virtual-router-redundancy-protocol/VERIFICATION.md) | 5 | Configuration comparison passed; runtime untested. |
| [web-cache-communication-protocol-wccp-v1](web-cache-communication-protocol-wccp-v1/VERIFICATION.md) | 4 | Client: missing startup recovered as addressing-only from final-configs/Client.cfg; exercise routing/services were not inferred unless specified below. Internet: missing startup recovered as addressing-only from final-configs/Internet.cfg; exercise routing/services were not inferred unless specified below. Redirector: missing startup recovered as addressing-only from final-configs/Redirector.cfg; exercise routing/services were not inferred unless specified below. WebCache: missing startup recovered as addressing-only from final-configs/WebCache.cfg; exercise routing/services were not inferred unless specified below. |
