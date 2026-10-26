# IP SLA: IOS 17.12.1 correction

Reviewed on 2026-10-26 for the user-reported Cisco IOS Software [Dublin],
`X86_64BI_LINUX-ADVENTERPRISEK9-M`, version **17.12.1 (fc5)**.
**Configuration analysis only; no live router tests were performed.**

## Cause and corrections

The earlier device conversion retained the source's obsolete IP SLA command
family. Its command-preservation checks did not validate acceptance on the
running IOS version. That previous verification was insufficient for this lab.

- Replaced `ip sla monitor` with `ip sla`, including schedules and responders.
- Replaced legacy `type echo protocol ipIcmpEcho`, `type dns target-addr`,
  `type jitter dest-ipaddr ... dest-port` and `type http operation get url`
  with the documented `icmp-echo`, `dns`, `udp-jitter` and `http get` forms.
- Replaced zero timeouts with 5000 ms. Both codec probes use explicit 20 ms
  packet spacing and repeat every 60 seconds, allowing the default 1000-packet
  burst (about 20 seconds) plus timeout to finish. This intentionally corrects
  the source's one-second operation frequency.
- Corrected Cucumber's DNS frequency from 9 to 8 seconds to match the goal.
- Corrected Lettuce's HTTP destination from the public website to
  `http://192.168.34.4/`, explicitly repeating every 60 seconds as requested.
- Preserved operation IDs, forever schedules, ICMP target/frequency, DNS query
  name/server, UDP targets/ports, codecs/payload sizes and responder placement.

These are deliberate syntax and exercise corrections, rather than a claim of
byte-for-byte equivalence with the broken source SLA settings.

## Checks performed

All four final files were checked for removal of legacy syntax and zero timeouts.
All five operation definitions and schedules were checked for matching IDs,
targets, timings and forever lifetimes. Codec destinations correspond to the
loopback addresses of responder-enabled Cucumber and Pickle. Their packet bursts
fit within the new operation frequency.

A comparison with the pre-fix configs confirmed that all non-SLA statements are
unchanged, including addressing, interfaces, bandwidth/delay, OSPF and administrative
state. The DNS/HTTP service additions described below intentionally change
application-service settings. Startup configs, the topology and device
settings are unchanged. The portable project's final configs and documentation
match the loose files; all other archive members retain their original bytes.
The archive passed ZIP integrity checks.

## Runtime limits and existing service prerequisites

The reported release identifies the intended syntax, but this review cannot prove
that every operation is implemented in that particular IOU build. Check live
command acceptance, OSPF reachability, responder control traffic and operation
results with the `show ip sla` commands listed in the lab guide.

The previously missing services are now included in the final configs:

- Lettuce: `ip domain lookup`, a static host record mapping www.gns3vault.com to
  192.168.34.4, and `ip dns server`. Cucumber's DNS operation still queries
  Lettuce's 1.1.1.1 address every eight seconds.
- Tomato: HTTP enabled with local authentication, a dedicated privilege-1
  `sla-http` account and HTTP access class 99 permitting only 1.1.1.1.
- Lettuce operation 5: an authenticated HTTP RAW **GET** for Tomato's built-in
  `/level/1/exec` page, explicitly sourced from 1.1.1.1. The matching Basic
  Authorization header prevents an unauthenticated request from being rejected.
  The target IP, 5000 ms timeout, 60-second frequency and forever schedule remain.

The built-in page avoids a dependency on an HTML file in flash. No external
server, DNS resolver or Internet connection is needed by this configuration.
The actual availability of the IOS HTTP page and the DNS/RAW features on this
specific IOU image remains untested. No successful DNS/HTTP results are claimed.

Additional static checks confirmed that the DNS answer matches Tomato's address,
the HTTP source matches Lettuce's loopback and Tomato's ACL, the decoded Basic
credentials match the local account, and the RAW request terminates with the
required CRLF sequence. Addressing/routing/interface settings, Cucumber/Pickle
final configs, all startup configs and topology bytes were preserved during the
service addition. The rebuilt portable archive matches the loose configs/docs.

## Cisco references

- [IP SLA DNS and HTTP command syntax](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/ipsla/command/sla-cr-book/sla_a1.html)
- [UDP jitter codec options and timeout guidance](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/ipsla/command/sla-cr-book/sla_s2.html)
- [Configuring UDP jitter operations for VoIP](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/ipsla/configuration/12-2sr/sla-12-2sr-book/Configuring_Cisco_IOS_IP_SLAs_UDP_Jitter_Operations_for_VoIP.pdf)
- [Cisco DNS server configuration](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/ipaddr_dns/configuration/15-sy/dns-15-sy-book/Configuring-DNS.html)
- [Authenticated IP SLA HTTP RAW requests](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/ipsla/configuration/xe-16/sla-xe-16-book/sla-http.html)
- [IOS HTTP local authentication and access controls](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/https/configuration/xe-16-12/https-xe-16-12-book/HTTP_1-1_Web_Server_and_Client.html)
- [Built-in IOS web interface and privilege-level URLs](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/fundamentals/configuration/xe-16/fundamentals-xe-16-book/fundamentals-xe-16-book_chapter_01000.html)
