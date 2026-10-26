# IP Service Level Agreement (SLA)

## Scenario

As the senior network engineer for "Groceries 'r' Us" you are responsible for all routing within the company. Every now and then you have links that are still in the up/up state but you are unable to send any IP packets over them. You also would like something that could generate different traffic streams like RTP to simulate VoIP or HTTP. You heard good things about IP SLA so you decide to build a lab and test some things...

## Goal

- All IP addresses have been preconfigured for you.
- OSPF has been configured for full connectivity.
- Configure router Lettuce to send ICMP echo packets to IP address 4.4.4.4 every 9 seconds. It should never stop.
- Configure router Cucumber to send DNS request packets to IP address 1.1.1.1 every 8 seconds. It should never stop.
- Configure router Pickle to send G711 packets to IP address 2.2.2.2 port 16384 with a codec-size of 160 bytes with an interval of 20ms. It should never stop.
- Configure router Cucumber to respond to the G711 packets.
- Configure router Tomato to send G729 packets to IP address 3.3.3.3 port 16374 with a codec-size of 20 bytes. It should never stop.
- Configure router Pickle to respond to the G729 packets.
- Configure router Lettuce to send HTTP GET packets to IP address 192.168.34.4 every 60 seconds.

## GNS3 2.2.56.1

Import [IP SLA IOU.gns3project](IP%20SLA%20IOU.gns3project) using **File > Import portable project**. To open `IP SLA.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Cucumber | FastEthernet0/0 | Ethernet0/0 |
| Cucumber | FastEthernet1/0 | Ethernet0/1 |
| Lettuce | FastEthernet0/0 | Ethernet0/0 |
| Lettuce | FastEthernet1/0 | Ethernet0/1 |
| Pickle | FastEthernet0/0 | Ethernet0/0 |
| Pickle | FastEthernet1/0 | Ethernet0/1 |
| Tomato | FastEthernet0/0 | Ethernet0/0 |
| Tomato | FastEthernet1/0 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## IOS 17.12.1 solution syntax

The running image was reported as `X86_64BI_LINUX-ADVENTERPRISEK9-M`,
Cisco IOS Software [Dublin] **17.12.1**. The final configs now use `ip sla`,
`ip sla responder`, `icmp-echo`, `dns`, `udp-jitter` and `http get`.
The older `ip sla monitor` / `type ...` syntax has been removed.

| Router / operation | Probe | Timing |
| --- | --- | --- |
| Lettuce / 1 | ICMP echo to 4.4.4.4 | Every 9 seconds |
| Cucumber / 2 | Resolve www.gns3vault.com using DNS server 1.1.1.1 | Every 8 seconds |
| Pickle / 3 | G.711 A-law to Cucumber 2.2.2.2:16384, 160-byte codec payload | 20 ms packet spacing; operation every 60 seconds |
| Tomato / 4 | G.729A to Pickle 3.3.3.3:16374, 20-byte codec payload | 20 ms packet spacing; operation every 60 seconds |
| Lettuce / 5 | Authenticated HTTP GET to 192.168.34.4 (`/level/1/exec`) | Every 60 seconds |

All five operations run with `life forever` and a 5000 ms timeout. Codec probes
retain the default 1000 packets per operation: approximately 20 seconds of traffic
at 20 ms spacing. The 60-second operation frequency allows that burst and timeout
to complete; it is separate from the inter-packet interval. Cucumber and Pickle
have the responder enabled for the corresponding incoming jitter probes.

### Applying and checking the solutions

On a fresh lab, apply each matching final config. If an operation already exists,
remove its schedule with `no ip sla schedule <id>` and then remove the operation
with `no ip sla <id>` before applying its replacement. Use IDs 1 and 5 on Lettuce,
2 on Cucumber, 3 on Pickle and 4 on Tomato. Editing an already scheduled operation
in place can fail.

Check `show ip sla configuration`, `show ip sla statistics` and `show ip sla
summary`; on Cucumber and Pickle also check `show ip sla responder`. Allow OSPF to
converge before evaluating probe results.

### Included DNS and HTTP services

Apply Tomato's final config before evaluating Lettuce's HTTP probe. Apply
Lettuce's final config before evaluating Cucumber's DNS probe.

- **Lettuce** enables its DNS server and resolves `www.gns3vault.com` to
  `192.168.34.4` using a static host record. Cucumber queries Lettuce at
  `1.1.1.1`; no public DNS service or Internet access is required.
- **Tomato** enables HTTP with local authentication. Its built-in level-1 EXEC
  page (`/level/1/exec`) supplies the response, so no HTML file needs uploading.
  The dedicated account is `sla-http`, privilege 1, with lab password
  `SlaLabHTTP1`. HTTP access list 99 permits only Lettuce's `1.1.1.1` address.
- **Lettuce operation 5** sources its HTTP request from `1.1.1.1` and uses an
  HTTP RAW operation to send an explicit **GET** with a Basic Authorization
  header matching that account. The lab's GET target, 60-second frequency and
  forever schedule are retained. RAW allows the authentication header; a plain
  unauthenticated GET could receive HTTP 401 instead of a successful response.

The password and encoded Authorization header are lab fixtures. If you change
one, update the other. Keep the literal `\r\n` text in the `http-raw-request`
lines, including the final line that contains only `\r\n` (apart from indentation).
That terminates the HTTP headers. The request uses HTTP/1.0 as required by the
Cisco RAW-operation documentation.

After applying the configs and allowing OSPF to converge:

| Device | Command | What to check |
| --- | --- | --- |
| Lettuce | `show hosts` | Static www.gns3vault.com record points to 192.168.34.4 |
| Cucumber | `show ip sla statistics 2` | DNS operation's latest return code and successful operation count |
| Tomato | `show ip http server status` | HTTP enabled, local authentication, access class 99 |
| Tomato | `show access-lists 99` | Requests match Lettuce's permitted source |
| Lettuce | `show ip sla statistics 5` | HTTP operation's latest return code and successful operation count |

Expected successful return codes are `OK`, but they have not been observed on
this IOU build. A DNS failure warrants checking the DNS service and static record;
HTTP 401/403 warrants checking the account, Authorization header and source ACL;
a 404 warrants checking whether the build exposes the documented level-1 page.
The IOS HTTP server, DNS service and RAW-operation support still need live validation.

See [verification and Cisco command references](VERIFICATION.md). The syntax was
reviewed against Cisco documentation; it has not been executed on your router.

## Topology

![Network Topology](./topology-ip-service-level-agreement-sla.png)

## Video Solution

http://www.youtube.com/watch?v=TZFUCwoQjx4
