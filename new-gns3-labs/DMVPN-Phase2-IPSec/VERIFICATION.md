# Delivery verification

Performed on 2026-10-22. Run `python3 validate.py` from this directory to repeat the offline checks. Result: **PASS**.

## Checked offline

- Portable ZIP integrity, exact archive file inventory, project JSON equality, and byte equality between each packaged startup file and its readable copy. Solutions are not injected into the unsolved archive.
- Existing repository project structure retained: topology revision 9, schema version 2.2.0 (not the application patch version), `project.gns3`, and `project-files/iou/<UUID>/startup-config.cfg`. Target application is GNS3 2.2.56.1.
- Four distinct node UUIDs and IOU application IDs, automatic console allocation, preferred IOU image/template/memory/adapter settings, and valid non-reused physical endpoints.
- Startup commands checked against a strict IP-only allowlist. Site addresses, LAN /24s, and overlay subnet from the supplied diagram are retained. Startup and solution interface addressing match exactly; ISP configuration is unchanged.
- Each Ethernet link has matching transport subnets and different endpoint addresses. Each solution default next hop is the adjacent ISP address. ISP has connected routes to all three NBMA networks, providing bidirectional underlay paths without any overlay knowledge.
- Each solution enables EIGRP on only its local LAN and the overlay. LAN interfaces are passive; only Tunnel0 forms adjacencies. Transport prefixes and defaults are not redistributed. Hub split-horizon suppression is disabled so it can relay spoke routes, and next-hop-self is disabled so remote-spoke tunnel addresses remain next hops. These conditions support the six expected LAN route entries listed in VALIDATION.md without recursive routing of NBMA destinations into the tunnel.
- Hub dynamic NHRP/multicast configuration and spoke static hub mappings/NHS selection agree. No preconfigured remote-spoke mappings are present. Every router uses mGRE and matching tunnel key/network ID/authentication, allowing dynamic spoke resolution.
- All VPN routers have matching AES-CBC-256/SHA-1 integrity/SHA-1 PRF/DH14 IKEv2 proposals and policies, local and remote pre-shared authentication, the same wildcard keyring passphrase and identity selector, matching ESP AES-256/HMAC-SHA-1 transport transforms, explicit local NBMA identities, correctly named IKEv2/IPsec profile references, and Tunnel0 protection. This provides compatible configured proposals and credentials for every pair, including R31–R41.

The checks combine file assertions with configuration analysis; they do not execute IOS routing, NHRP, or cryptography. The validator is intentionally lab-specific and is not a general-purpose Cisco configuration parser.

## Not verified live

No GNS3 server or IOU process was started. GNS3 import, exact-image syntax/feature support (including IKEv2 support, keyring/profile binding and DH14), NHRP registration, EIGRP convergence, encrypted forwarding, SA counters, packet captures, and MTU behavior remain unverified. A filename and appliance template do not prove feature support. VALIDATION.md supplies the required runtime acceptance procedure. Do not describe these files as live-tested until that procedure passes on the installed image.

## Design and syntax references

- [Cisco: Dynamic Multipoint IPsec VPNs](https://www.cisco.com/c/en/us/support/docs/security-vpn/ipsec-negotiation-ike-protocols/41940-dmvpn.html) — mGRE/NHRP and dynamic spoke-to-spoke IPsec design.
- [Cisco: Sharing IPsec with Tunnel Protection](https://www.cisco.com/en/US/docs/ios-xml/ios/sec_conn_dmvpn/configuration/15-1mt/sec-conn-dmvpn-share-ipsec-w-tun-protect.html) — profile-based protection and transform-set syntax. This lab has only one tunnel per router and does not require the `shared` keyword.
- [Cisco: EIGRP command reference, I through R](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_eigrp/command/ire-cr-book/ire-i1.html) — interface next-hop-self behavior.
- [Cisco: Configuring IKEv2](https://www.cisco.com/en/US/docs/ios-xml/ios/sec_conn_ikevpn/configuration/15-1mt/Configuring_Internet_Key_Exchange_Version_2.html) — proposal, policy, keyring, profile, and authentication syntax.
- [Cisco: IKEv2 and Legacy VPNs](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/sec-vpn/b-security-vpn/m_sec-apx-ikev2-legacy.html) — IKEv2 integration with DMVPN tunnel protection. These references do not prove support in the installed IOU image.

The activity uses IKEv2 with an IKEv2 keyring as requested. DMVPN Phase 2 was selected to exercise EIGRP next-hop preservation and on-demand direct spoke traffic. No original solution existed to compare against; consistency was checked against this lab's addressing, requirements, and expected outcomes.

## IKEv2 revision verification

Converted all three VPN router solutions to explicit IKEv2 proposals, policies, keyrings, and profiles. Local and remote keys are identical across all three peers, and wildcard peer/identity matching permits both hub–spoke and direct spoke–spoke authentication. The IPsec profile now selects the IKEv2 profile. Updated runtime checks to inspect IKEv2 SAs and their READY state. The static validator rejects legacy IKEv1 configuration and checks the new settings and bindings.

Addressing, underlay routes, NHRP roles/mappings, EIGRP advertisements and next-hop behavior, ESP transforms, and tunnel protection attachment remain equivalent to the previous solution. IP-only startup files and the portable archive require no change because they contain no IKE configuration. Static validation passes; no live protocol or image compatibility test was performed.

## Project rename verification

The directory, GNS3 display name, canvas title, portable archive, import instructions, and validator now use `DMVPN-Phase2-IPSec`. The archive was rebuilt from the renamed project metadata and existing IP-only startup files. Node and project UUIDs are preserved so startup-config paths and link references remain valid. The internal filename remains `project.gns3`, preserving the portable format. Archive integrity, embedded project equality, node/config associations, and the full static validator pass after the rename. Live GNS3 import and IOU operation remain unverified.
