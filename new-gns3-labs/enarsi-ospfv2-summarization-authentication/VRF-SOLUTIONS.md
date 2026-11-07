# VRF solutions — spoilers

Complete answers for all routers are in `final-configs/`. This guide explains the new parts; [SOLUTIONS.md](SOLUTIONS.md) explains BLUE's original OSPF requirements. Expected results are analytical predictions, not captured device output.

## V1: VRF lifecycle and addressed-interface migration

The starter defines `ip vrf BLUE` with `rd 65000:10` everywhere and RED with RD 65000:20 on R1/R2/R4/R5. Every tenant interface has its binding **before** the address. VRF containers and interface bindings are already supplied so overlapping addresses can be installed in the starter. They are not a completed OSPF solution.

R1 migration, after recording the global route:

```text
configure terminal
ip vrf STAGING
 rd 65000:99
exit
interface Loopback900
 ip vrf forwarding STAGING
 ip address 198.18.0.1 255.255.255.255
end
show ip vrf interfaces
show ip route vrf STAGING 198.18.0.1
show ip route 198.18.0.1
```

After capturing the intermediate state:

```text
configure terminal
interface Loopback900
 ip vrf forwarding BLUE
 ip address 198.18.0.1 255.255.255.255
exit
no ip vrf STAGING
end
```

On R5, bind Loopback900 to BLUE and restore 198.18.0.5/32. Create process 10 bound to BLUE, enable `capability vrf-lite` and passive-by-default, then activate these loopbacks in area 0 during Activity 1. Changing VRF membership clears an existing IP address; changing the description or RD does not bind an interface. VRF names identify local contexts; names are not negotiated in OSPF packets. Separate connected interfaces and routing tables supply isolation. An RD does not encrypt packets or provide a security ACL, and matching/differing RDs do not by themselves leak routes. This design has no VPNv4 BGP route exchange in which route targets could implement import/export policy.

Every BLUE process begins with `router ospf 10 vrf BLUE`, every RED process with `router ospf 20 vrf RED`. Use `capability vrf-lite` in both to suppress PE-specific checks inappropriate for this CE VRF-Lite design. Distinct locally configured process IDs are required to manage these separate IOS OSPF processes; process IDs are locally significant and need not match a neighbor's ID in general. Router IDs are explicit and distinct across both tenants here, to make the evidence unambiguous.

## V2: RED configuration and distinguishing evidence

RED uses dedicated Ethernet1/x ports. R1 e1/0–R2 e1/0 and R1 e1/1–R5 e1/0 use area 0. R2 e1/1–R4 e1/0 use area 10. Transit addresses are the same as the corresponding BLUE links; contexts and physical ports differ. RED Loopback1000 duplicates BLUE Loopback0 addresses. R4 Loopbacks1100–1103 duplicate BLUE campus 10.10.0.0/24–3.0/24; R5 Loopbacks1100–1103 duplicate BLUE external 172.20.16.0/24–19.0/24. Loopback1900 on R5 is the unique RED marker 198.51.100.5/32.

All RED processes use router ID 20.20.20.r, passive-by-default, and only their Ethernet1/x links unpassived. Ethernet cost is 10; Ethernet and internal /24 loopbacks use point-to-point OSPF network type. R5 service loopbacks are selected for connected redistribution and have no interface OSPF activation. Use area-default MD5 in area 0 with interface key 20 / RedCore20, and area-default simple authentication in area 10 with interface secret RedPlain. The eight-character simple secret is different from BLUE's A10plain.

R2 RED policy:

```text
router ospf 20 vrf RED
 capability vrf-lite
 area 10 range 10.10.0.0 255.255.252.0 cost 70
```

R5 RED policy:

```text
ip prefix-list RED-EXT-R5 seq 10 permit 172.20.16.0/24
ip prefix-list RED-EXT-R5 seq 20 permit 172.20.17.0/24
ip prefix-list RED-EXT-R5 seq 30 permit 172.20.18.0/24
ip prefix-list RED-EXT-R5 seq 40 permit 172.20.19.0/24
route-map RED-CONNECTED-R5 permit 10
 match ip address prefix-list RED-EXT-R5
router ospf 20 vrf RED
 capability vrf-lite
 redistribute connected subnets metric 60 metric-type 2 route-map RED-CONNECTED-R5
 summary-address 172.20.16.0 255.255.252.0 tag 1505
```

The process's VRF scopes the connected routes available for redistribution. Prefix-lists/route-maps are globally named configuration objects; dedicated names prevent unintended policy reuse. A selector matching a duplicated prefix does not import it from another VRF.

| R1 observation | BLUE / process 10 | RED / process 20 |
|---|---|---|
| Campus aggregate | 10.10.0.0/22 | 10.10.0.0/22 |
| Installed O IA metric, normal state | 60 | 80 |
| Summary advertising router | 2.2.2.2 preferred, 3.3.3.3 alternate | 20.20.20.2 only |
| Immediate campus next hop | 10.255.12.2 on e0/0 | 10.255.12.2 on e1/0 |
| R5 external aggregate | 172.20.16.0/22 | 172.20.16.0/22 |
| Installed external type/metric | E1 / 50 | E2 / 60 |
| External LSA metric/tag | 40 / 505 | 60 / 1505 |
| External advertising router | 5.5.5.5 | 20.20.20.5 |
| R5 egress interface | e0/2 | e1/1 |
| 198.18.0.5/32 | Present after migration | Absent |
| 198.51.100.5/32 | Absent | Present |
| 10.10.8.0/24 | Present | Absent |

Expected neighbor counts: BLUE R1=4/R2=3/R3=4/R4=2/R5=1/R6=2/R7=1/R8=1; RED R1=2/R2=2/R4=1/R5=1. Total 12 adjacencies and 24 table entries. RIBs, LSDBs and CEF lookups must be scoped; success to 172.20.16.1 in both tenants reaches two different local service interfaces.

## V3: minimum repairs

T6 moves R5 Loopback900 into RED and activates it in process 20. On R5:

```text
configure terminal
interface Loopback900
 no ip ospf 20 area 0
 ip vrf forwarding BLUE
 ip address 198.18.0.5 255.255.255.255
 ip ospf 10 area 0
end
```

After convergence, RED must lose the .5/32 and BLUE must regain it. Do not repair by importing RED routes into BLUE. Verify the address was restored after the binding changed.

T7 removes only R2's RED /22 area range. Restore it under `router ospf 20 vrf RED` with cost 70. Confirm RED specifics disappear outside area 10, R1's RED metric returns to 80, and BLUE still uses cost 60 with both of its aggregates. Modifying process 10 would be a wrong-context repair.

T8 replaces the RED secret on R1 e1/1 with BLUE's CoreNew20. Restore `ip ospf message-digest-key 20 md5 RedCore20` on R1 e1/1. The key ID was already correct; the secret was not. Check RED neighbor recovery and BLUE e0/2 uptime. Allow the dead interval when injecting an authentication fault into an existing adjacency.

## V4: verification and failure independence

Useful scoped commands on R1:

```text
show ip vrf
show ip vrf interfaces
show ip ospf 10
show ip ospf 20
show ip ospf 10 neighbor
show ip ospf 20 neighbor
show ip ospf 10 database summary
show ip ospf 20 database summary
show ip ospf 10 database external
show ip ospf 20 database external
show ip route vrf BLUE
show ip route vrf RED
show ip route
show ip cef vrf BLUE 172.20.16.1 detail
show ip cef vrf RED 172.20.16.1 detail
ping vrf BLUE 198.18.0.5 source 198.18.0.1
ping vrf RED 198.51.100.5 source 10.255.0.1
ping vrf RED 198.18.0.5 source 10.255.0.1
ping vrf BLUE 198.51.100.5 source 10.255.0.1
```

The first two pings should succeed; the last two should fail with no corresponding tenant route. Also test BLUE's 10.10.8.1 from BLUE and RED as specified in the candidate matrix. In the final global table none of the addressed lab interfaces or tenant routes should appear. Check exact route masks as well as longest-prefix lookups. Do not mistake local/connected entries for OSPF learning.

Shutting R1 e1/1 disconnects R5 only in RED. R1/R2/R4 RED must lose R5-originated service reachability; R5 retains its own connected routes and may retain a self-originated external LSA locally. BLUE's e0/2 link, E1 aggregate and forwarding continue normally. Restore e1/1 and recheck RED routes. On R4, use `ping vrf BLUE 172.20.16.1 source 10.10.0.1` and the corresponding RED command for each of the four service destinations. BLUE returns through its campus summary; RED returns through its own summary on R2. Capture traffic on R1–R5 e0/2 versus e1/1 to establish the tenant actually used.

These checks show control-plane and forwarding-context separation. They do not test an MPLS provider network or a cross-tenant firewall. No route leak is intended or needed. Complete the original BLUE NSSA/stub and summary failure tests as well; RED has no NSSA or stub area and must not inherit BLUE defaults.
