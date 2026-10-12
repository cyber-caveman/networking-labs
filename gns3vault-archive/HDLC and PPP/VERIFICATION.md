# HDLC and PPP: verification index

4 projects checked on 2026-10-10. All installed GNS3 schema, endpoint/port, device-preference and archive-integrity checks passed. IOU NVRAM is 512 KB. Startup/final configuration analysis checks command contexts, effective bandwidth/delay, administrative state and mapped connectivity. Earlier conversions received a settings refresh without changing config text.

**No live testing:** command acceptance, services, protocol behavior, convergence, hardware-dependent features and forwarding require testing on the target server. Source limitations and reconstruction assumptions are listed per lab; preserving a source solution is not proof it satisfies every exercise goal.

| Lab review | Final configs | Notes |
| --- | ---: | --- |
| [multilink-ppp-over-frame-relay](multilink-ppp-over-frame-relay/VERIFICATION.md) | 2 | Configuration comparison passed; runtime untested. |
| [ppp-advanced-authentication](ppp-advanced-authentication/VERIFICATION.md) | 2 | Configuration comparison passed; runtime untested. |
| [ppp-authentication](ppp-authentication/VERIFICATION.md) | 2 | Configuration comparison passed; runtime untested. |
| [ppp-over-ethernet-pppoe](ppp-over-ethernet-pppoe/VERIFICATION.md) | 2 | Poseidon: missing startup recovered as addressing-only from final-configs/R1.cfg; exercise routing/services were not inferred unless specified below. Artemis: missing startup recovered as addressing-only from final-configs/R2.cfg; exercise routing/services were not inferred unless specified below. |
