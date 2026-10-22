# Runtime acceptance checklist

Run these checks after completing the tasks. Results below are expectations, not captured live output. Initial packets can be lost while NHRP resolves addresses and IKE/IPsec SAs form; repeat tests after convergence. Use extended ping prompts if the image does not accept inline source/repeat options.

## 1. Transport and interface state

On each VPN router:

```text
show ip interface brief
show ip route 0.0.0.0
```

Ethernet0/0 and Loopback0 must be up/up. Tunnel0 should become up/up after source/mode configuration, but that state alone does not prove NHRP or encryption works. The default route must resolve through the local ISP address on Ethernet0/0, never through Tunnel0.

Ping both other NBMA addresses from each router, using `source Ethernet0/0`. For example on R31:

```text
ping 172.16.11.1 source Ethernet0/0
ping 172.16.41.1 source Ethernet0/0
```

On ISP, `show ip route connected` must show 172.16.11.0/24, 172.16.31.0/24, and 172.16.41.0/24. ISP must have no site-LAN or overlay routes. Plain transport pings are intentionally not IPsec-protected.

## 2. NHRP and EIGRP

```text
show dmvpn
show ip nhrp
show ip eigrp neighbors
show ip protocols
show ip route eigrp
```

R11 must dynamically map 192.168.100.31 → 172.16.31.1 and 192.168.100.41 → 172.16.41.1. Each spoke must have the static hub mapping 192.168.100.11 → 172.16.11.1 and a working hub session. R11 should have two EIGRP neighbors; each spoke should have one (the hub). A direct spoke data tunnel does not require a spoke-to-spoke EIGRP adjacency.

Expected remote EIGRP LAN routes:

| Router | Destination | Next hop |
|---|---|---|
| R11 | 10.3.3.0/24 | 192.168.100.31 |
| R11 | 10.4.4.0/24 | 192.168.100.41 |
| R31 | 10.1.1.0/24 | 192.168.100.11 |
| R31 | 10.4.4.0/24 | 192.168.100.41 |
| R41 | 10.1.1.0/24 | 192.168.100.11 |
| R41 | 10.3.3.0/24 | 192.168.100.31 |

Expect internal EIGRP (`D`) routes; transport prefixes must not be learned through EIGRP. The receiving spoke's remote-spoke route is learned from R11 while retaining the originating spoke as its next hop. Resolve missing remote routes through EIGRP split horizon checks; resolve incorrect hub next hops through the hub's next-hop-self setting.

## 3. All site pairs

On R11 ping 10.3.3.1 and 10.4.4.1; on R31 ping 10.1.1.1 and 10.4.4.1; on R41 ping 10.1.1.1 and 10.3.3.1. Source every test from Loopback0. For example:

```text
ping 10.4.4.1 source Loopback0 repeat 20
```

All six directed tests must succeed after convergence. For MTU verification, use extended ping with source Loopback0, a 1400-byte datagram, and the DF bit set; it should pass over Tunnel0 after convergence. TCP MSS adjustment affects TCP SYN packets, not ICMP.

## 4. Prove encryption and direct spoke forwarding

Record these outputs before and after a sustained R31 → 10.4.4.1 ping sourced from Loopback0:

```text
show crypto ikev2 sa detailed
show crypto ipsec sa
show crypto session detail
show dmvpn
show ip nhrp
```

1. Active IKEv2 sessions should reach `READY` (display details vary by image). Confirm AES-CBC-256, SHA-1 integrity, SHA-1 PRF, DH group 14, and PSK authentication in both directions in the detailed SA output. Inspect `show crypto ikev2 proposal`, `show crypto ikev2 policy`, `show crypto ikev2 profile`, and the running configuration to verify the proposal/policy/profile/keyring bindings and 86400-second profile lifetime. Local and remote identities must be the participating NBMA addresses.
2. After traffic, R31 must resolve 192.168.100.41 → 172.16.41.1 dynamically, and R41 must resolve 192.168.100.31 → 172.16.31.1. Inspect both spokes, not only the hub.
3. On R31, identify the IPsec peer **172.16.41.1**, and on R41 identify peer **172.16.31.1**. Confirm AES-256 / SHA-HMAC ESP transforms, transport mode, installed inbound/outbound SAs, and rising encapsulation/encryption and decapsulation/decryption counters during the ping. Error counters should not increase. Hub-only SAs do not prove direct spoke encryption.
4. Capture on R31–ISP in GNS3 while repeating the test. Filter `ip.addr == 172.16.31.1 && ip.addr == 172.16.41.1`. Expect ESP (IP protocol 50); IKE uses UDP 500 during negotiation. No NAT is configured in this lab. Site data and GRE must not appear in plaintext on this physical link. The inner LAN addresses should not be visible in encrypted packets.
5. The direct session's outer endpoints must be the two spokes, not R11. R11 can still carry control traffic, so its counters need not remain stationary. Do not rely on traceroute alone to prove encryption or bypass of the hub.

## 5. Save and troubleshoot

Save with `copy running-config startup-config` on each VPN router. If commands are rejected, record `show version` and the exact parser error; feature support in the installed IOU image is a separate prerequisite from file correctness.

Troubleshoot in this order: local interface state → remote NBMA reachability → matching IKEv2 proposal/policy/keyring/profile → IPsec profile attachment → NHRP hub and multicast mappings → EIGRP adjacency and next hops → direct spoke encryption. A tunnel that is up/up with no routes is not sufficient evidence of a working VPN.
