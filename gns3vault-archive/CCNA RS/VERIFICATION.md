# CCNA RS: verification index

4 projects checked on 2026-10-10. All installed GNS3 schema, endpoint/port, device-preference and archive-integrity checks passed. IOU NVRAM is 512 KB. Startup/final configuration analysis checks command contexts, effective bandwidth/delay, administrative state and mapped connectivity. Earlier conversions received a settings refresh without changing config text.

**No live testing:** command acceptance, services, protocol behavior, convergence, hardware-dependent features and forwarding require testing on the target server. Source limitations and reconstruction assumptions are listed per lab; preserving a source solution is not proof it satisfies every exercise goal.

| Lab review | Final configs | Notes |
| --- | ---: | --- |
| [eigrp-for-ccna-1](eigrp-for-ccna-1/VERIFICATION.md) | 5 | Configuration comparison passed; runtime untested. |
| [icnd1-assesment-lab](icnd1-assesment-lab/VERIFICATION.md) | 3 | Godzilla: missing startup recovered as addressing-only from final-configs/R1.cfg; exercise routing/services were not inferred unless specified below. Nessie: missing startup recovered as addressing-only from final-configs/R2.cfg; exercise routing/services were not inferred unless specified below. KingKong: missing startup recovered as addressing-only from final-configs/R3.cfg; exercise routing/services were not inferred unless specified below. |
| [icnd2-assessment-lab](icnd2-assessment-lab/VERIFICATION.md) | 3 | Configuration comparison passed; runtime untested. |
| [ospf-for-ccna-1](ospf-for-ccna-1/VERIFICATION.md) | 6 | Configuration comparison passed; runtime untested. |
