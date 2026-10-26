# Verification report

Date: 2026-10-24. Status: **static verification only; live acceptance pending**.

## Performed

- Checked Cisco's ENARSI v1.1 objective and feature semantics against the references in SOURCES.md. Distinguished the blueprint's describe-level objective from the added configuration activities.
- Reused the repository's established revision-9, version-2.2.0 portable-project structure for target GNS3 2.2.56.1. Applied the specified IOU images, hashes, templates, resources, interface format and console settings. Device instances have distinct UUIDs and application IDs.
- Checked all four links, enabled interfaces, VLAN membership, LAN addressing and static return paths. The intentionally unbound source has a return route, so its unprotected ping has a valid path back.
- Checked each complete solution checkpoint preserves baseline addresses and routes, defines every referenced policy/ACL/prefix list, and removes temporary rogue DHCP/client state. The prefix profile deliberately adds Loopback30, its RA prefix and its return route; it changes the branch's RA and source-validation roles together.
- Analyzed declared RA sender/prefix allowlists, DHCP server-role/source checks, source-policy attachment and binding-dependent source acceptance. Exercised positive, wrong-sender, wrong-prefix, unbound-source and wrong-port cases in a small static policy model. Its assumed bindings are fixtures, not discovered facts.
- Checked Destination Guard's always enforcement, local snooping attachment and absence of destination recovery. Its actual neighbor-resolution behavior is covered by the live procedure, not simulated by the validator.
- Checked prefix-mode validation and the retained per-address policy on H1, branch RA restrictions and return routes. Prefix Guard is not confused with RA prefix filtering.
- Checked final-configs byte equality with checkpoint 05, embedded/readable startup equality, archive CRC integrity, exact archive member set and byte equality with all delivered source files.

Run `python3 validate.py` to reproduce the static checks. The command prints its check count and explicitly identifies tests not run. These checks are specific to the lab; they are not a Cisco syntax parser or proof of forwarding correctness.

## Not performed / unresolved

No live Cisco image, GNS3 controller or console session was available in this task. No image was booted. GNS3 import, CLI acceptance, IOU support for each guard, dynamic host/prefix binding creation, DHCPv6 exchanges, enforcement counters, and packet disposition remain unverified. The configured image hashes are the user's declared defaults, not hashes calculated from supplied image files.

The main material limitation is whether these IOU builds implement the necessary features, especially prefix validation and Destination Guard on R1's routed interface. PREFLIGHT.md and VALIDATION.md make that gate explicit. Missing support requires a suitable Cisco platform/release for the live track; configuration analysis and the original questions can still be completed. Do not report an unsupported feature as passed.

All expected packet outcomes are predictions based on the documented features and stated preconditions. Paired positive/negative controls, binding inspection and captures are required before calling the lab live-validated. No authentication protocol is configured in this lab; its trust boundaries are interface roles, source allowlists and binding validation.
