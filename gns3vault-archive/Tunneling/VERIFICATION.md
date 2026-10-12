# Tunneling: verification index

4 projects checked on 2026-10-10. All installed GNS3 schema, endpoint/port, device-preference and archive-integrity checks passed. IOU NVRAM is 512 KB. Startup/final configuration analysis checks command contexts, effective bandwidth/delay, administrative state and mapped connectivity. Earlier conversions received a settings refresh without changing config text.

**No live testing:** command acceptance, services, protocol behavior, convergence, hardware-dependent features and forwarding require testing on the target server. Source limitations and reconstruction assumptions are listed per lab; preserving a source solution is not proof it satisfies every exercise goal.

| Lab review | Final configs | Notes |
| --- | ---: | --- |
| [encrypted-gre-tunnel](encrypted-gre-tunnel/VERIFICATION.md) | 3 | Legacy .net topology converted; the original .net file remains a reference. |
| [gre-over-ipsec](gre-over-ipsec/VERIFICATION.md) | 3 | Legacy .net topology converted; the original .net file remains a reference. |
| [gre-tunnel-basic](gre-tunnel-basic/VERIFICATION.md) | 3 | Configuration comparison passed; runtime untested. |
| [site-to-site-ipsec-vpn](site-to-site-ipsec-vpn/VERIFICATION.md) | 3 | Legacy .net topology converted; the original .net file remains a reference. Godzilla: missing startup recovered as addressing-only from final-configs/Godzilla.cfg; exercise routing/services were not inferred unless specified below. KingKong: missing startup recovered as addressing-only from final-configs/KingKong.cfg; exercise routing/services were not inferred unless specified below. Nessie: missing startup recovered as addressing-only from final-configs/Nessie.cfg; exercise routing/services were not inferred unless specified below. |
