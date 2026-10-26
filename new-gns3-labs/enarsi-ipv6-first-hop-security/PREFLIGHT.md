# Platform and evidence preflight

Record `show version`, image filename/hash, GNS3 version and relevant parser output. This lab uses the classic IOS `ipv6 snooping` CLI. Some IOS XE releases use SISF `device-tracking`; do not paste one command family into the other. Translate against the exact platform guide if moving the exercise. Cisco documentation for a hardware platform does not establish IOU support.

Use a disposable imported copy. In global configuration mode, use contextual help without applying policies:

```text
ipv6 snooping ?
ipv6 nd raguard ?
ipv6 dhcp guard ?
ipv6 source-guard ?
ipv6 destination-guard ?
```

On SW1 verify policy creation and attachment on Ethernet0/0–2. Within disposable policies, check `security-level`, `protocol`, `prefix-glean`, `device-role`, RA `match` options, DHCP `match server access-list`, Source Guard `validate address` and `validate prefix`. On R1 check snooping and Destination Guard policy/attachment support specifically on routed Ethernet0/0. Check R1's DHCPv6 server pool and H1's `ipv6 address dhcp` support.

Create temporary named policies only in the disposable copy if help requires entering a policy mode. Reimport afterward. Missing commands mean that live activity is unavailable on that image. An unsupported combination of interface and feature also fails the gate, even when global policy creation works.

| Capability | Required location | Parser result | Packet enforcement result |
|---|---|---|---|
| Snooping + binding display | SW1; R1 for Activity 5 | Not tested | Not tested |
| RA Guard + source/prefix match | SW1 | Not tested | Not tested |
| DHCPv6 server/client and Guard | R1/H1/ROGUE; SW1 | Not tested | Not tested |
| Source Guard address validation | SW1 client ports | Not tested | Not tested |
| Destination Guard | R1 LAN routed interface | Not tested | Not tested |
| Prefix glean + prefix validation | SW1 branch port | Not tested | Not tested |

Find the binding-display spelling with `show ipv6 ?`. Cisco releases document variants including `show ipv6 neighbors binding` and `show ipv6 neighbor binding`. This guide writes `show ipv6 neighbors binding`; use the exact supported spelling. It means the **FHS binding database**, not plain `show ipv6 neighbors` (the IPv6 neighbor/adjacency cache). Likewise discover `show ipv6 snooping counter ?` versus `counters ?` on your release.

Pass a capability only after its positive/negative packet tests. Mark unavailable features **not tested**, not passed. The configuration-analysis and question tracks remain usable without them. No live controller connection or image was supplied to the author, so none of these gates has already passed.
