# OSPF conversion verification

Configuration analysis completed for all **24 labs** against the original repository
files at commit `77b0f0bab21189c65fb0f7a951220b3bc3e671ca`. This is a comparison of configuration behavior,
not a record of live router tests.

## Device and packaging checks

- 79 IOU exercise routers match every L3 setting in `AGENTS.md`, including the
  selected image/checksum/template, four Ethernet and four serial adapters, RAM,
  NVRAM, symbol, dimensions, automatic consoles and shared IOU options.
- Four unmanaged switches and six C3640 Frame Relay switching devices retain
  their device roles and types. Existing Frame Relay switch configuration files
  are byte-for-byte unchanged.
- All 24 topologies and all 85 configurable router property sets pass the installed
  GNS3 schemas. Node UUIDs and application IDs are unique within each topology.
- Original link peer and port identities were compared with the converted topology.
  Intermediate’s four links were checked against its original `topology.net`.
- Startup addressing and initial routing-process presence are preserved. Three
  missing Frame Relay startup sets were recovered from the matching non-broadcast
  lab; blank exercise routers remain blank.
- Each archive’s project and config files match the loose files. Every IOU startup
  config uses `project-files/iou/<node-id>/startup-config.cfg`. All archives pass
  ZIP integrity checks. Containerlab files are unchanged.

## Solution equivalence analysis

All **76 supplied final configs** were compared in their command contexts after
applying the documented interface mappings. The comparison includes all addressing,
OSPF processes and network/area statements, authentication modes and keys,
virtual-link peers, priorities, timers, network types, summaries, redistribution,
filters, static routes, default origination, Frame Relay maps and DLCIs. Interface
administrative states and effective bandwidth values were compared separately.
OSPF costs were recomputed from the reference bandwidth and interface bandwidth,
including explicit cost overrides. Logical interface names and attached peers were
checked together. Hardware-only commands removed for IOU were excluded.

The lab-relevant configuration behavior is preserved, subject to IOS support and
defaults on the target image. One explicit source repair adds the missing
`interface Loopback0` header in the misidentified single-area `Amsterdam.cfg`;
this is a repair of an invalid source stanza, not evidence that the Amsterdam
solution is correct. Existing incomplete or incorrect original solutions were
identified below rather than silently changing their intended exercise behavior.

Preserving a source configuration does **not** certify it as a complete solution
to every exercise goal. The per-lab review distinguishes conversion equivalence
from those original shortcomings.

| Lab | Supplied final configs | Configuration review | Limits or source defects |
| --- | ---: | --- | --- |
| [ospf-authentication](ospf-authentication/ospf-authentication.md) | 4 | Area 0 MD5, Area 1 plaintext, paired virtual-link MD5 and Area 2 attachment retained. | Live authenticated adjacencies and virtual-link establishment not tested. |
| [ospf-auto-cost-reference-bandwidth](ospf-auto-cost-reference-bandwidth/ospf-auto-cost-reference-bandwidth.md) | 4 | Reference bandwidth 10000 Mbit/s retained; FastEthernet 100000 Kbit/s gives cost 100 and Gigabit 1000000 Kbit/s gives cost 10. Addresses and linked peers match the source. | Selena’s link toward Emily is unaddressed and shut in the source startup and final configs; retained. |
| [ospf-demand-circuit](ospf-demand-circuit/ospf-demand-circuit.md) | 2 | Matching serial /24, loopbacks, area 0 and demand-circuit on both endpoints retained. | Hello suppression and demand-circuit support on the chosen image need live testing. |
| [ospf-dr-bdr-election](ospf-dr-bdr-election/ospf-dr-bdr-election.md) | 5 | Both broadcast segments, Marge priority 100, Bart priority 90 and other priorities retained. | Homer/Maggie DR/BDR selection depends on startup/election order; the source configs alone do not enforce it. |
| [ospf-flood-reduction](ospf-flood-reduction/ospf-flood-reduction.md) | 3 | Both routed links, area 0 and flood-reduction on each participating interface retained. | LSA refresh suppression requires live observation. |
| [ospf-intermediate](ospf-intermediate/ospf-intermediate.md) | 4 | Reference bandwidth 1500, 2000 Kbit/s R1–R2 bandwidth (cost 750), other Ethernet costs 15, matching authentication/dead timers, final R4–R2 shutdown, NSSA, /22 range and default origination retained. | Source final configs omit R1 router-id 1.1.1.2 and R4 Loopback14; R4 priority 200 favors R4 rather than the requested R3 DR. These pre-existing differences remain. |
| [ospf-lsa-type-3-summarization](ospf-lsa-type-3-summarization/ospf-lsa-type-3-summarization.md) | 5 | Area 0/1/2 assignments and ABR ranges 172.16.0.0/22 and 10.10.0.0/21 retained; ranges cover the configured loopback prefixes. | Actual Type 3 LSAs and routing tables not observed. |
| [ospf-lsa-type-5-summarization](ospf-lsa-type-5-summarization/ospf-lsa-type-5-summarization.md) | 3 | Sam’s connected redistribution and two /22 summary-address statements retained. | Harry has no OSPF process in the source final config, preventing the intended end-to-end OSPF exchange; retained as a source defect. |
| [ospf-md5-authentication-rotating-key](ospf-md5-authentication-rotating-key/ospf-md5-authentication-rotating-key.md) | 3 | One shared broadcast segment, Twist’s two key IDs and the matching individual Turn/Rotate MD5 keys retained. | Multiple-key rollover adjacency behavior requires live image testing. |
| [ospf-nssa-not-so-stubby-area](ospf-nssa-not-so-stubby-area/ospf-nssa-not-so-stubby-area.md) | 3 | Serial peer addressing, Area 3 NSSA, connected redistribution, 172.16.0.0/23 external summary, reciprocal Area 2 virtual links and Area 4 172.16.2.0/23 range retained. | Loopback network-type settings remain exactly as supplied; full advertised-mask behavior was not established live. |
| [ospf-over-frame-relay-broadcast](ospf-over-frame-relay-broadcast/ospf-over-frame-relay-broadcast.md) | 4 | PVC routes, paired DLCIs, static broadcast maps, common /24, broadcast OSPF, spoke priority 0 and loopbacks retained. | DLCI/LMI status, IOU-to-Dynamips serial interoperability and actual flooding require live testing. |
| [ospf-over-frame-relay-non-broadcast](ospf-over-frame-relay-non-broadcast/ospf-over-frame-relay-non-broadcast.md) | 0 | Blank addressed-router exercise state and preconfigured Frame Relay switch retained. | No final-configs supplied; there is no original completed solution to compare or verify. |
| [ospf-over-frame-relay-point-to-multipoint](ospf-over-frame-relay-point-to-multipoint/ospf-over-frame-relay-point-to-multipoint.md) | 4 | Available final files and the original switch PVC configuration retained after router serial mapping. | Files supplied as final configs contain no router IP addressing or OSPF process; they are incomplete source solutions. |
| [ospf-over-frame-relay-point-to-multipoint-non-broadcast](ospf-over-frame-relay-point-to-multipoint-non-broadcast/ospf-over-frame-relay-point-to-multipoint-non-broadcast.md) | 4 | Available final files and the original switch PVC configuration retained after router serial mapping. | Files supplied as final configs contain no router IP addressing or OSPF process; they are incomplete source solutions. |
| [ospf-over-frame-relay-point-to-point](ospf-over-frame-relay-point-to-point/ospf-over-frame-relay-point-to-point.md) | 4 | Point-to-point subinterfaces, 102↔201 and 103↔301 DLCIs, separate /24 subnets, loopbacks and area 0 retained. | DLCI/LMI status and point-to-point adjacency formation not tested live. |
| [ospf-per-neighbor-cost](ospf-per-neighbor-cost/ospf-per-neighbor-cost.md) | 4 | Common /24, point-to-multipoint OSPF, equal 1.1.1.1/32 spoke loopbacks and Herring neighbor cost 10 retained. The unchanged 1544 Kbit/s serial default implies cost 64 before that override. | Inverse ARP and dynamically learned Frame Relay mappings, as used by the source, need live verification. |
| [ospf-single-area](ospf-single-area/ospf-single-area.md) | 3 | Barcelona’s bandwidth 100 Kbit/s (cost 1000), MD5, hello interval 5 and network statements retained; HongKong plaintext/MD5 and default origination retained. | Amsterdam.cfg is a duplicate HongKong config in the source, so the provided set is not a valid three-router solution. Its missing Loopback0 declaration was repaired; the misidentified solution is otherwise preserved. |
| [ospf-stub-area](ospf-stub-area/ospf-stub-area.md) | 2 | Area 1 stub on both ends, Algrim’s external connected prefixes and backbone loopback retained; stub behavior should replace external LSAs with a default. | Default route installation and filtering of external LSAs not tested live. |
| [ospf-summarization-discard-route](ospf-summarization-discard-route/ospf-summarization-discard-route.md) | 3 | Area assignments, 3.3.3.0/24 and ABR range 3.0.0.0/8 retained. | Source Shapeir final config lacks no discard-route internal; the requested suppression of the Null0 summary route is not implemented in that source solution. |
| [ospf-suppress-forward-address](ospf-suppress-forward-address/ospf-suppress-forward-address.md) | 0 | All five startup routers, Ethernet/serial links and original addressing retained. | No final-configs supplied; NSSA, RIP redistribution, prefix filtering and suppress-fa have no original completed solution to verify. |
| [ospf-totally-nssa](ospf-totally-nssa/ospf-totally-nssa.md) | 3 | Backbone prefixes, connected redistribution, Area 1 nssa no-summary, RIP v2 and RIP-to-OSPF redistribution retained. | Type 7 translation, default-route behavior and reachability need live testing. |
| [ospf-totally-stub](ospf-totally-stub/ospf-totally-stub.md) | 2 | Original interface addressing and administrative state retained. | Both supplied final configs lack OSPF and the additional loopbacks; they are incomplete source solutions. |
| [ospf-virtual-link](ospf-virtual-link/ospf-virtual-link.md) | 4 | Transit Area 1, reciprocal Chicken–Fish and Chicken–Pork virtual links and backbone/Area 2 networks retained. | Beef’s 2.2.2.2 loopback is not advertised by the source final config; full loopback reachability cannot be claimed. |
| [ospf-virtual-link-and-summarization](ospf-virtual-link-and-summarization/ospf-virtual-link-and-summarization.md) | 3 | Area 1 virtual-link peer identities, Area 2 attachment, four /24 loopbacks and the 172.16.0.0/22 range retained. | Dewey’s virtual-link router ID is selected automatically from its active interfaces, as in the source; virtual-link establishment and resulting LSAs require live testing. |

## Live behavior not verified

No routers were booted and no live pings, neighbor/LSDB/routing-table checks,
packet captures or restart/election tests were performed in this update. The
selected IOU image’s acceptance of the converted commands, actual interface
defaults and MTUs, IOU–Dynamips serial/LMI/PVC operation, authenticated neighbor
formation, DR/BDR election order, virtual-link establishment, summary/default
route installation, NSSA translation, demand-circuit hello suppression and
flood-reduction refresh suppression still require GNS3 **2.2.56.1** and the
specified images. No successful live protocol behavior is claimed.

## C3640 appliance compatibility

All six Frame Relay switching routers use the user-provided working C3640 appliance:
`c3640-a3js-mz.124-25d.image`, MD5 `493c4ef6578801d74d715e7d11596964`,
template `b7a0bd2a-0e7d-4ea8-8c93-3b580f78971e`, 192 MB RAM,
256 KB NVRAM, clock divisor 4 and idle-PC `0x6050b114`.
Other runtime settings match that appliance example.

Slot 0 retains `NM-4T` because the Frame Relay topology requires Serial0/0–0/2;
the example's empty slots would provide no serial ports. The existing node UUID,
project-local Dynamips ID and matching startup-config filename are retained.
Console allocation and MAC-address generation are left to GNS3 rather than copying
the example's console port or MAC address. Startup/final configs and PVCs are unchanged.

Re-import this updated `.gns3project` archive to apply the appliance settings.
Existing imported copies are not updated by edits to this repository.
Local schema, runtime port construction, link lookup, archive and configuration
consistency checks passed. Opening and booting on the remote server remain untested;
the precise cause of the previously reported empty canvas has not been confirmed.
