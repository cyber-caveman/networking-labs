# Verification record

## Scope and result

Created using the repository root `AGENTS.md` and the previously working OSPF Authentication IOU portable-project structure. The user's confirmed choice is IOU hardware with IOS XE–checked BGP syntax. No changes were made to existing labs.

Validation run: **PASS — 234 static assertions**, covering four routers, three links, and six reciprocal peer definitions.

Static validation is provided in `validate.py`. It reads the actual startup and solution files and resolves template inheritance rather than checking names alone. Its acceptance assertions cover physical subnet consistency, reciprocal peers and AS numbers, matching inherited passwords/timers, exact connected origination routes, inbound test-prefix rejection, outbound isolation, return-route availability, and local-preference ordering. The modeled common-prefix ranking is R2 (200), R3 (150), R4 (100); all are directly connected external next hops. This is configuration analysis, not measured convergence or data-plane testing.

The portable ZIP uses root `project.gns3`, format revision 9 / version 2.2.0 (the known working serialization for the target GNS3 2.2.56.1), with IOU configs under `project-files/iou/<node-id>/startup-config.cfg`. Node UUIDs and application IDs are unique; console ports are null for automatic allocation. Canvas SVG drawings contain only the title and addressing labels. Exercise instructions are in `README.md`. All startup and full solution configs are bundled separately.

## README consistency review

Compared the README with all four startup configs, all four full solution configs, and the topology link endpoints. Confirmed interface addresses, router IDs, AS numbers, neighbor addresses, session template inheritance, timers/password, policy assignments and sequences, prefix lists, route maps, originated networks, and expected filtering/failover behavior. Startup and solution configs were unchanged by the removal of canvas instructions. Clarified that a branch ping to the shared service address can terminate locally; use the prescribed R1 test for service failover.

## IOS XE syntax review

Reference: Cisco [IOS XE 17.x — Configuring a Basic BGP Network](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_irg-basic-net-0.html), sections “Configuring Peer Session Templates,” “Configuring Peer Policy Templates,” and their examples.

Reviewed commands/modes:

| Construct | Placement used |
|---|---|
| `template peer-session NAME` / `exit-peer-session` | Router BGP / session template |
| `timers 10 30`, `password EnarsiBGP` | Session template |
| `inherit peer-session NAME` | Child session template |
| `neighbor IP remote-as ASN` followed by `neighbor IP inherit peer-session NAME` | Router BGP |
| `template peer-policy NAME` / `exit-peer-policy` | Router BGP / policy template |
| `prefix-list NAME in/out`, `maximum-prefix 10`, `route-map NAME in` | Policy template |
| `inherit peer-policy NAME SEQUENCE` | Child policy template |
| `neighbor IP activate`, `neighbor IP inherit peer-policy NAME` | IPv4 unicast address family |

Templates are defined before use. Session inheritance has one parent; policy inheritance uses explicit sequences. No neighbor combines templates with peer-group membership. Review distinguishes template inheritance sequencing from attaching a policy directly to a neighbor, which has no sequence argument.

The local-preference route-map command was also checked against Cisco’s [IOS XE 17 protocol-independent command reference](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/iproute_pi/command/iri-cr-book/iri-cr-s1.html).

## Pending live verification

No GNS3 server or device session was connected for this task. Thus project import, image boot, IOU feature support, actual IOS XE parser acceptance, effective runtime policies, TCP authentication, negotiated timers, maximum-prefix enforcement, convergence and pings remain unverified. The exact installed IOU binary may differ in CLI support from IOS XE. `VALIDATION.md` supplies explicit pass/fail checks and controlled negative tests; do not treat those expected outputs as collected evidence.

An actual IOS XE run would additionally require a licensed installed CSR1000v/C8000v appliance and platform-specific interface mapping/startup packaging. This deliverable intentionally retains the confirmed IOU defaults.
