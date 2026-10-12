# Network Management: verification index

28 projects checked on 2026-10-10. All installed GNS3 schema, endpoint/port, device-preference and archive-integrity checks passed. IOU NVRAM is 512 KB. Startup/final configuration analysis checks command contexts, effective bandwidth/delay, administrative state and mapped connectivity. Earlier conversions received a settings refresh without changing config text.

**No live testing:** command acceptance, services, protocol behavior, convergence, hardware-dependent features and forwarding require testing on the target server. Source limitations and reconstruction assumptions are listed per lab; preserving a source solution is not proof it satisfies every exercise goal.

| Lab review | Final configs | Notes |
| --- | ---: | --- |
| [access-list-logging](access-list-logging/VERIFICATION.md) | 2 | Configuration comparison passed; runtime untested. |
| [autoinstall-using-rarp-for-lan-interfaces](autoinstall-using-rarp-for-lan-interfaces/VERIFICATION.md) | 0 | Missing startup addresses recovered from the diagram. EIGRP AS 1 is an explicit reconstruction choice because no AS was supplied; Flynn remains unaddressed. AutoInstall boot behavior requires a device with no saved startup config; erase Flynn’s saved config when performing that exercise. RARP support on the selected image is unverified. No completed final configs were supplied; none were invented. |
| [backup-interface](backup-interface/VERIFICATION.md) | 4 | Configuration comparison passed; runtime untested. |
| [banners](banners/VERIFICATION.md) | 0 | No completed final configs were supplied; none were invented. |
| [buffer-tuning](buffer-tuning/VERIFICATION.md) | 2 | Configuration comparison passed; runtime untested. |
| [cdp-cisco-discovery-protocol](cdp-cisco-discovery-protocol/VERIFICATION.md) | 3 | Is: solution final-configs/Leonidas.cfg uses a different hostname; associated by matching interface addresses. Sparta: solution final-configs/Theron.cfg uses a different hostname; associated by matching interface addresses. This: solution final-configs/Gorgo.cfg uses a different hostname; associated by matching interface addresses. |
| [conditional-debug](conditional-debug/VERIFICATION.md) | 2 | Configuration comparison passed; runtime untested. |
| [configuration-archive-to-tftp](configuration-archive-to-tftp/VERIFICATION.md) | 0 | Cloud retains the source external interface names. Select the correct interface on the remote GNS3 compute before starting; external services/servers are not bundled. No completed final configs were supplied; none were invented. |
| [configuration-change-logging](configuration-change-logging/VERIFICATION.md) | 0 | No completed final configs were supplied; none were invented. |
| [eem-scripting](eem-scripting/VERIFICATION.md) | 0 | No completed final configs were supplied; none were invented. |
| [eem-scripting-event-detector](eem-scripting-event-detector/VERIFICATION.md) | 0 | No completed final configs were supplied; none were invented. |
| [exec-alias](exec-alias/VERIFICATION.md) | 0 | No completed final configs were supplied; none were invented. |
| [ios-http-server](ios-http-server/VERIFICATION.md) | 2 | Configuration comparison passed; runtime untested. |
| [ios-tftp-server](ios-tftp-server/VERIFICATION.md) | 2 | Configuration comparison passed; runtime untested. |
| [kron-task-scheduler](kron-task-scheduler/VERIFICATION.md) | 1 | Configuration comparison passed; runtime untested. |
| [logging-timestamps](logging-timestamps/VERIFICATION.md) | 0 | No completed final configs were supplied; none were invented. |
| [login-menu](login-menu/VERIFICATION.md) | 2 | Configuration comparison passed; runtime untested. |
| [ntp-network-time-protocol](ntp-network-time-protocol/VERIFICATION.md) | 5 | Configuration comparison passed; runtime untested. |
| [remote-shell](remote-shell/VERIFICATION.md) | 2 | Configuration comparison passed; runtime untested. |
| [rmon-alarms-and-events](rmon-alarms-and-events/VERIFICATION.md) | 0 | Cloud retains the source external interface names. Select the correct interface on the remote GNS3 compute before starting; external services/servers are not bundled. No completed final configs were supplied; none were invented. |
| [snmp-trap-for-syslog](snmp-trap-for-syslog/VERIFICATION.md) | 0 | Cloud retains the source external interface names. Select the correct interface on the remote GNS3 compute before starting; external services/servers are not bundled. No completed final configs were supplied; none were invented. |
| [snmpv2-server](snmpv2-server/VERIFICATION.md) | 0 | Cloud retains the source external interface names. Select the correct interface on the remote GNS3 compute before starting; external services/servers are not bundled. No completed final configs were supplied; none were invented. |
| [snmpv3-server](snmpv3-server/VERIFICATION.md) | 0 | Cloud retains the source external interface names. Select the correct interface on the remote GNS3 compute before starting; external services/servers are not bundled. No completed final configs were supplied; none were invented. |
| [syslog-server-logging](syslog-server-logging/VERIFICATION.md) | 0 | Cloud retains the source external interface names. Select the correct interface on the remote GNS3 compute before starting; external services/servers are not bundled. No completed final configs were supplied; none were invented. |
| [system-message-logging](system-message-logging/VERIFICATION.md) | 0 | No completed final configs were supplied; none were invented. |
| [tcp-keepalive](tcp-keepalive/VERIFICATION.md) | 4 | Configuration comparison passed; runtime untested. |
| [telnet-server-tuning](telnet-server-tuning/VERIFICATION.md) | 0 | No completed final configs were supplied; none were invented. |
| [virtual-terminal-line-settings](virtual-terminal-line-settings/VERIFICATION.md) | 0 | Missing startup and unrelated Buffed/Spice labels replaced with Day/Night and the addresses in the supplied diagram. No completed final configs were supplied; none were invented. |
