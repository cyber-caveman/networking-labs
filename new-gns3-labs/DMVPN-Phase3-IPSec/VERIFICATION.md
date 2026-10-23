# Verification record

Offline validation performed on 2026-10-22: **PASS**. Reproduce with `python3 validate.py` from this directory.

## Artifact and configuration checks

- GNS3 revision 9 / schema version 2.2.0 retained from the compatible repository format; target application 2.2.56.1. Archive contains only `project.gns3` and the four matching `project-files/iou/<node-id>/startup-config.cfg` files. ZIP integrity and exact byte equality checked.
- New project/node/link/drawing UUIDs; unique IOU application IDs within the topology; automatic console allocation; preferred appliance properties. Node IDs are disjoint from Phase 2. Physical endpoints are valid and not reused, and adjacent addresses share a subnet.
- Strict startup allowlist permits only interface declarations, IP addresses, activation and configuration delimiters. Startup and final interface IP addresses match. Applying VRF membership is an intentional task; its address-removal behavior is documented.
- Scoped final-config checks confirm Ethernet0/0 is in FVRF-INTERNET, while Loopback0/Tunnel0 are global. Tunnel outer lookup and IKEv2 policy/profile select the FVRF. No static/default routes, route-target import/export, or BGP/OSPF redistribution are configured.
- Reciprocal eBGP AS numbers and neighbor activation checked. Exact local/ISP network origination and prefix-list references checked. Both sides of each import/export filter were evaluated against all transport prefixes, LAN prefixes, tunnel subnet, default, a transport /32 and a transport aggregate. Each VPN router accepts exactly the two remote transport /24s through its adjacent ISP neighbor. ISP's three connected routes provide transport forwarding. Local origins exist because the network statements match connected /24s.
- Each site runs OSPF globally on only Loopback0 and Tunnel0, with the tunnel as the only non-passive interface. Point-to-multipoint tunnel and point-to-point loopback types support hub/spoke adjacency and LAN /24 advertisement. Prefix-list evaluation confirms local OSPF installation rejects only overlay /32s while permitting all three LAN /24s and the overlay /24. The inbound filter does not remove LSAs from the database.
- Hub dynamic multicast mappings and NHRP redirects, spoke hub/NHS mappings and shortcuts, identical NHRP authentication/network IDs/tunnel keys, and mGRE sources are consistent. Before shortcuts, OSPF's point-to-multipoint graph gives each spoke the hub as next hop for the other LAN. Redirects/shortcuts are configured to optimize forwarding without requiring a direct spoke OSPF adjacency.
- Explicit matching IKEv2 encryption/integrity/PRF/DH parameters, wildcard peer selectors, identical local/remote PSKs, NBMA identities, FVRF selectors, profile references and ESP transport-mode transforms checked on all VPN routers. These provide compatible configured parameters for every pair, not proof that SAs have negotiated.

The validator is a lab-specific static consistency checker and filter evaluator, not a Cisco parser or protocol simulator. Routing and forwarding conclusions above are configuration analysis.

## Functional comparison to the source exercise

Addresses and physical links are preserved. The new project intentionally changes the service: eBGP routes in the FVRF replace global static defaults; OSPF replaces EIGRP; Phase 3 redirects/shortcuts replace Phase 2 next-hop preservation. Expected site-to-site reachability and IKEv2/ESP protection are retained, while initial spoke forwarding now uses the hub. ISP's solution adds BGP because this is required by the new exercise; the source Phase 2 project is unchanged. Every new node has a matching final config, including ISP.

## Live tests still required

No GNS3 import or IOU boot was performed. Exact-image parser support, VRF-aware IKEv2/BGP behavior, OSPF convergence, NHRP redirects/shortcuts, CEF overrides, ESP packet/counter evidence, MTU behavior, and recovery after an underlay failure remain unverified. VALIDATION.md gives expected results and the acceptance procedure. Do not treat static PASS as a live forwarding result.

## Cisco references

- [DMVPN troubleshooting](https://www.cisco.com/c/en/us/support/docs/security/dynamic-multipoint-vpn-dmvpn/111976-dmvpn-troubleshoot-00.html): Phase 3 redirect/shortcut behavior and OSPF point-to-multipoint guidance.
- [Dynamic Multipoint VPN configuration guide](https://www.cisco.com/c/en/us/td/docs/routers/ios-xe/security-vpn/security-vpn/m_sec-conn-dmvpn-dmvpn-0.html): DMVPN behavior and the OSPF point-to-multipoint tunnel /32 restriction. This lab implements local inbound OSPF RIB filtering, rather than claiming an outbound filter suppresses intra-area LSAs.
- [Troubleshoot OSPF route database issues](https://www.cisco.com/c/en/us/support/docs/ip/open-shortest-path-first-ospf/7112-26.html): distribute-list filtering can prevent local route installation while retaining LSDB information.
- [Configuring IKEv2](https://www.cisco.com/c/en/us/td/docs/routers/ios-xe/security-vpn/security-vpn/m_sec-cfg-ikev2-flex.html): proposals, policies, keyrings, profiles and FVRF selection.

The general Cisco documentation is a syntax/design reference, not proof of support in the user's specific IOU build.
