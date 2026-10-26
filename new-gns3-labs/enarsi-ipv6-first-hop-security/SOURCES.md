# Source notes

Checked 2026-10-24. Only Cisco technical documentation and the publicly accessible Cisco blueprint were used as technical references. Questions and scenarios are original. No exam-dump questions were used. Documentation examples contain optional bypass commands; the lab intentionally does not copy every optional command from those examples.

| Reference | What it supports |
|---|---|
| [ENARSI v1.1 exam topics](https://learningcontent.cisco.com/documents/marketing/exam-topics/300-410-ENARSI-v1.1.pdf) | Objective 3.4 describes first-hop security; 4.4 covers DHCP troubleshooting. The blueprint does not explicitly name Prefix Guard or Destination Guard in 3.4. |
| [Cisco IOS XE IPv6 Snooping](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/ipv6_fhsec/configuration/xe-16/ip6f-xe-16-book/ip6-snooping.html) | Policy attachment, learning and binding database/recovery framework. |
| [Catalyst 3560-CX/2960-CX IPv6 configuration](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst2960cx_3650cx/software/release/15-2_3_e/configuration/guide/b_1523e_consolidated_2960cx_3560cx_cg/m_1523e_ipv6_unirt_3750x_3560cx_cg.html) | Distinctions among glean, inspect and guard; binding display and classic IOS snooping syntax. |
| [Cisco IPv6 RA Guard](https://www.cisco.com/c/en/us/td/docs/routers/ios-xe/security-vpn/security-vpn/m_ip6-ra-guard.html) | Host/router roles, sender and RA-prefix checks, trust-bypass semantics. |
| [Cisco DHCPv6 Guard](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/ipaddr_dhcp/configuration/15-s/dhcp-15-s-book/ip6-dhcpv6-guard.html) | Client/server roles, source ACL match and attachment. |
| [Cisco IPv6 Source Guard and Prefix Guard](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/ipv6_fhsec/configuration/xe-16-8/ip6f-xe-16-8-book/ip6-src-guard.html) | Address versus prefix validation; RA/DHCP-PD/static sources of prefix authorization; source-policy trust bypass. |
| [Cisco IPv6 Destination Guard](https://www.cisco.com/c/en/us/td/docs/routers/ios-xe/security-vpn/security-vpn/m_ipv6-dest-gaurd-xe.html) | Guarding routed neighbor resolution, always/stressed modes and interface attachment. Its unrelated feature-information footer is not used as platform support evidence. |
| [Cisco IOS IPv6 command reference: prefix-glean and protocol](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/ipv6/command/ipv6-cr-book/ipv6-m1.html) | Prefix glean command and NDP/DHCP selection. |
| [Cisco Implementing DHCP for IPv6](https://www.cisco.com/en/US/docs/ios-xml/ios/ipv6/configuration/15-0sy/ip6-dhcp.html) | DHCPv6 pool/address-prefix concepts. |
| [Catalyst 3650 IPv6 configuration](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst3650/software/release/3se/ipv6/configuration_guide/b_ipv6_3se_3650_cg/b_ipv6_3se_3650_cg_chapter_0100.html) | Server pool configuration and client addressing support to check on the selected image. |
| [Cisco Live 2025: IPv6 Security in the Local Area](https://www.ciscolive.com/c/dam/r/ciscolive/global-event/docs/2025/pdf/BRKENT-3002.pdf) | Modern SISF device-tracking terminology versus older IPv6 snooping CLI. |

The design uses these documented semantics to construct controlled test cases. It does not infer IOU feature support from Catalyst, ASR or generic IOS XE documentation. Exact CLI and enforcement must be checked on the running image. Different command families and platform attachment restrictions require platform-specific adaptation, not blind substitution.
