# Technical references

Consulted when authoring the lab. Cisco IOS/IOS XE documentation supports the design, but does not establish feature support in a particular IOU binary.

- [Cisco 300-410 ENARSI exam](https://www.cisco.com/site/us/en/learn/training-certifications/exams/enarsi.html): official 90-minute exam duration. The workbook's estimates and scoring are independently designed training targets.
- [Cisco OSPF command reference: area, authentication and area range](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/command/iro-cr-book/m_ospf-a1.html): ABR ranges, configured costs, suppression, area types and authentication defaults.
- [Cisco OSPF command reference: summary-address](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/command/iro-cr-book/m_ospf-s1.html): external aggregation, tags, and suppression.
- [Cisco NSSA configuration](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/6208-nssa.html): Type-7 origin and translation at the NSSA boundary.
- [Cisco OSPF message-digest-key reference](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/command/iro-cr-book/ospf-i1.html): MD5 key rollover behavior.
- [Cisco OSPFv2 cryptographic authentication](https://www.cisco.com/c/en/us/td/docs/routers/ios-xe/ip-routing/b-ip-routing/m_iro-ospfv2-crypto-authen.html): key-chain configuration, HMAC-SHA-256 and operational verification.
- [RFC 5709](https://www.rfc-editor.org/info/rfc5709/): OSPFv2 HMAC-SHA authentication.

All topology, task wording, addressing, fault tickets, configurations and timing estimates are original to this lab. No official exam questions or purported exam dumps were used.

VRF revision references:

- [Cisco OSPF support for Multi-VRF on CE routers](https://spg.xgslb-v3.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_ospf/configuration/15-mt/iro-15-mt-book/iro-sup-vrf.html): VRF-bound OSPF and VRF-Lite capability suppressing PE-specific checks.
- [Cisco IPv4/IPv6 VRF CLI](https://www.cisco.com/c/en/us/td/docs/ios/12_2sr/12_2srb/feature/guide/sr_mpvrf.html): interface binding changes remove existing addresses, which must be reapplied.

These references support the configuration design; they do not establish tested behavior of the selected IOU binary.
