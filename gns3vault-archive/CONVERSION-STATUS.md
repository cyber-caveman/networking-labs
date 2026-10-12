# GNS3 lab conversion status

Updated on **2026-10-10** using the current `AGENTS.md`: **325 portable projects across 20 categories**, with 512 KB NVRAM on every IOU router and CLI switch. The BGP Regular Expressions exercise remains a public route-server exercise.

## Verification performed

- 325 project schemas and all device properties/real GNS3 port endpoints checked; compatible media and unique IDs verified.
- 223 newly converted or reconstructed projects: 1,447 startup/final files compared in context, including **649 supplied final files**. 3,385 physical-interface bandwidth, delay and administrative-state comparisons passed.
- 102 previously converted projects: configuration files remain byte-for-byte unchanged, including **309 supplied final files**; NVRAM settings and archives refreshed.
- All 325 portable archives pass ZIP integrity checks and contain the matching active project/configuration files.
- Unmanaged and Frame Relay device roles/PVCs retained; external cloud interface bindings still require local selection on the remote compute. Containerlab artifacts are unchanged.

## Limits

This is configuration analysis, **not live GNS3 testing**. Some supplied source files were missing, empty, inconsistent or incomplete. Reconstructed topology/startup assumptions and original solution defects are documented per lab. Hardware-dependent and image-specific features (including some switching, QoS, serial MPLS, legacy translation and AutoInstall features) require runtime verification. Missing completed solutions were not invented.

## Categories

| Category | Projects | Supplied final files |
| --- | ---: | ---: |
| [BGP](BGP/README.md) | 49 | 167 |
| [CCNA RS](CCNA%20RS/README.md) | 4 | 17 |
| [CCNP RS](CCNP%20RS/README.md) | 1 | 0 |
| [EIGRP](EIGRP/README.md) | 23 | 48 |
| [Frame Relay](Frame%20Relay/README.md) | 13 | 35 |
| [HDLC and PPP](HDLC%20and%20PPP/README.md) | 4 | 8 |
| [IPv6](IPv6/README.md) | 9 | 34 |
| [MPLS](MPLS/README.md) | 13 | 54 |
| [Multicast](Multicast/README.md) | 12 | 53 |
| [Network Management](Network%20Management/README.md) | 28 | 31 |
| [Network Services](Network%20Services/README.md) | 39 | 135 |
| [OSPF](OSPF/README.md) | 24 | 76 |
| [Quality of Service](Quality%20of%20Service/README.md) | 24 | 76 |
| [RIP](RIP/README.md) | 13 | 39 |
| [Redistribution](Redistribution/README.md) | 6 | 18 |
| [Security](Security/README.md) | 23 | 59 |
| [Static Routing](Static%20Routing/README.md) | 1 | 2 |
| [Switching](Switching/README.md) | 18 | 53 |
| [Troubleshooting](Troubleshooting/README.md) | 17 | 41 |
| [Tunneling](Tunneling/README.md) | 4 | 12 |
