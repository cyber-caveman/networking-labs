# OSPF labs for GNS3

All 24 labs target GNS3 **2.2.56.1**, using the device preferences in the repository
`AGENTS.md` and the tested OSPF Authentication portable-project format.

Import the `.gns3project` archive in each lab with **File > Import portable project**.
The archive supplies `project.gns3`, bundled startup configs, available solution
configs, exercise instructions and the original topology picture. IOS images are
provided by your GNS3 installation.

- 79 exercise routers use IOU L3, four Ethernet adapters, four serial adapters,
  768 MB RAM and 128 KB NVRAM.
- Four unmanaged Ethernet switches retain their original device type.
- Six preconfigured Frame Relay switching routers retain C3640 Dynamips and
  `c3640-a3js-mz.124-25d.image`; their PVC configurations are unchanged.
- Interface mappings appear in each lab’s instructions. Serial IOU ports start at
  `Serial4/0` because adapters 0–3 are Ethernet. FastEthernet/Gigabit bandwidth
  values are retained explicitly for the OSPF metric exercises.
- Startup configs preserve the exercise’s addressing and initial protocol state.
  Three Frame Relay exercises missing startup files use the matching blank
  starting state from the non-broadcast exercise.

| Lab | Import archive |
| --- | --- |
| [ospf-authentication](ospf-authentication/ospf-authentication.md) | [Portable project](ospf-authentication/OSPF%20Authentication%20IOU.gns3project) |
| [ospf-auto-cost-reference-bandwidth](ospf-auto-cost-reference-bandwidth/ospf-auto-cost-reference-bandwidth.md) | [Portable project](ospf-auto-cost-reference-bandwidth/OSPF%20Auto%20Cost%20Reference%20Bandwidth%20IOU.gns3project) |
| [ospf-demand-circuit](ospf-demand-circuit/ospf-demand-circuit.md) | [Portable project](ospf-demand-circuit/OSPF%20Demand%20Circuit%20IOU.gns3project) |
| [ospf-dr-bdr-election](ospf-dr-bdr-election/ospf-dr-bdr-election.md) | [Portable project](ospf-dr-bdr-election/OSPF%20DR%20BDR%20Election%20IOU.gns3project) |
| [ospf-flood-reduction](ospf-flood-reduction/ospf-flood-reduction.md) | [Portable project](ospf-flood-reduction/OSPF%20Flood-Reduction%20IOU.gns3project) |
| [ospf-intermediate](ospf-intermediate/ospf-intermediate.md) | [Portable project](ospf-intermediate/OSPF%20Intermediate%20IOU.gns3project) |
| [ospf-lsa-type-3-summarization](ospf-lsa-type-3-summarization/ospf-lsa-type-3-summarization.md) | [Portable project](ospf-lsa-type-3-summarization/OSPF%20LSA%20Type%203%20summarization%20IOU.gns3project) |
| [ospf-lsa-type-5-summarization](ospf-lsa-type-5-summarization/ospf-lsa-type-5-summarization.md) | [Portable project](ospf-lsa-type-5-summarization/OSPF%20LSA%20Type%205%20summarization%20IOU.gns3project) |
| [ospf-md5-authentication-rotating-key](ospf-md5-authentication-rotating-key/ospf-md5-authentication-rotating-key.md) | [Portable project](ospf-md5-authentication-rotating-key/OSPF%20MD5%20Authentication%20Rotating%20Key%20IOU.gns3project) |
| [ospf-nssa-not-so-stubby-area](ospf-nssa-not-so-stubby-area/ospf-nssa-not-so-stubby-area.md) | [Portable project](ospf-nssa-not-so-stubby-area/OSPF%20Nssa%20IOU.gns3project) |
| [ospf-over-frame-relay-broadcast](ospf-over-frame-relay-broadcast/ospf-over-frame-relay-broadcast.md) | [Portable project](ospf-over-frame-relay-broadcast/OSPF%20P2MP%20Network%20IOU.gns3project) |
| [ospf-over-frame-relay-non-broadcast](ospf-over-frame-relay-non-broadcast/ospf-over-frame-relay-non-broadcast.md) | [Portable project](ospf-over-frame-relay-non-broadcast/OSPF%20P2MP%20Network%20IOU.gns3project) |
| [ospf-over-frame-relay-point-to-multipoint](ospf-over-frame-relay-point-to-multipoint/ospf-over-frame-relay-point-to-multipoint.md) | [Portable project](ospf-over-frame-relay-point-to-multipoint/OSPF%20P2MP%20Network%20IOU.gns3project) |
| [ospf-over-frame-relay-point-to-multipoint-non-broadcast](ospf-over-frame-relay-point-to-multipoint-non-broadcast/ospf-over-frame-relay-point-to-multipoint-non-broadcast.md) | [Portable project](ospf-over-frame-relay-point-to-multipoint-non-broadcast/OSPF%20P2MP%20Network%20IOU.gns3project) |
| [ospf-over-frame-relay-point-to-point](ospf-over-frame-relay-point-to-point/ospf-over-frame-relay-point-to-point.md) | [Portable project](ospf-over-frame-relay-point-to-point/OSPF%20over%20FrameRelay%20PointtoPoint%20IOU.gns3project) |
| [ospf-per-neighbor-cost](ospf-per-neighbor-cost/ospf-per-neighbor-cost.md) | [Portable project](ospf-per-neighbor-cost/OSPFperNeighborCost%20IOU.gns3project) |
| [ospf-single-area](ospf-single-area/ospf-single-area.md) | [Portable project](ospf-single-area/OSPF%20Single%20Area%20IOU.gns3project) |
| [ospf-stub-area](ospf-stub-area/ospf-stub-area.md) | [Portable project](ospf-stub-area/ospf-stub-startup-configs%20IOU.gns3project) |
| [ospf-summarization-discard-route](ospf-summarization-discard-route/ospf-summarization-discard-route.md) | [Portable project](ospf-summarization-discard-route/OSPF%20Summarization%20Discard%20Route%20IOU.gns3project) |
| [ospf-suppress-forward-address](ospf-suppress-forward-address/ospf-suppress-forward-address.md) | [Portable project](ospf-suppress-forward-address/OSPF%20Suppress%20Forward%20Address%20IOU.gns3project) |
| [ospf-totally-nssa](ospf-totally-nssa/ospf-totally-nssa.md) | [Portable project](ospf-totally-nssa/ospf-totally-nssa-startup-configs%20IOU.gns3project) |
| [ospf-totally-stub](ospf-totally-stub/ospf-totally-stub.md) | [Portable project](ospf-totally-stub/ospf-totally-stub-startup-configs%20IOU.gns3project) |
| [ospf-virtual-link](ospf-virtual-link/ospf-virtual-link.md) | [Portable project](ospf-virtual-link/OSPF%20Virtual%20Link%20IOU.gns3project) |
| [ospf-virtual-link-and-summarization](ospf-virtual-link-and-summarization/ospf-virtual-link-and-summarization.md) | [Portable project](ospf-virtual-link-and-summarization/ospf-vl-and-summarization-startup-configs%20IOU.gns3project) |

## Validation and source notes

See [the per-lab configuration verification report](VERIFICATION.md) for the
comparison of all 76 supplied final configs, lab-specific requirements, original
solution defects and the distinction between configuration analysis and live testing.

All topologies and router properties passed the installed GNS3 JSON schemas.
Checks also passed for unique node/application IDs, adapter limits, link/config
interface alignment, startup address preservation, unchanged Frame Relay switch
configs, archive integrity and bundled config consistency. The format uses revision
9 as specified by the [GNS3 file format documentation](https://api.gns3.net/en/2.2/file_format.html).
Boot, IOS command support and routing behavior have not been tested on the target
GNS3 server.

The original `ospf-single-area/final-configs/Amsterdam.cfg` is a misidentified
HongKong configuration; it remains documented as a source defect. A missing
Loopback0 declaration in the supplied HongKong configs was restored. The
non-broadcast Frame Relay and suppress-forward-address labs have no supplied
completed solution configs.

Legacy `.net` files and topology images remain reference material. Containerlab
implementations and labs outside this folder are unchanged.

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
