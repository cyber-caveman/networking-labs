# EIGRP Authentication Rotating Key

![Network Topology](./topology-eigrp-authentication-rotating-key.jpg)

## Scenario

As the senior security officer you decide all routing protocols should be configured as secure as possible. The company you work for has a single vendor policy and since you only have Cisco equipment you are running EIGRP (Enhanced Interior Gateway Routing Protocol). EIGRP has more advanced features for authentication since it uses a key-chain. The key-chain supports rotating keys which makes it more secure than having a single static key. Before implementing this for your whole organization you decide to test your enhanced security in a lab environment.

## Goal

* All IP addresses have been preconfigured for you.
* EIGRP has been preconfigured for you (AS12).
* Enable EIGRP authentication between router Jack and Johnson. Use the following parameters:
  * Key-chain should be called: **GNS3VAULT**
  * Key1: password **VAULT**
  * Key2: password **SAFE**
* Key1 should be sent until 9:00AM on the 2nd of February 2020 and should be accepted 15 minutes past this time.
* Key2 should be valid from 8:50AM on the 2nd of February 2020 and should be valid till the 1st of February 2021.
* Make sure routing adjacencies do not drop when the keys are switched.

## GNS3 2.2.56.1

Import `eigrp-authentication-rotating-key IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `eigrp-authentication-rotating-key.gns3` beside `project-files`.

Routers use the preferred IOU L3 image `x86_64_crb_linux-adventerprisek9-ms.bin`
(MD5 `4a2fce8de21d1831fbceffd155e41ae7`), template
`b3b10b90-adfb-43f8-b289-b68bcf322ad8`, 768 MB RAM, 512 KB NVRAM,
four Ethernet and four serial adapters, with automatically allocated consoles.
Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Physical interface names and link endpoints are updated together in startup and
all supplied final configs. Original bandwidth and delay are explicit where
needed to preserve EIGRP/IGP metric inputs. Source protocol settings and intended
startup state are preserved; final configs are not loaded at startup.

| Router | Original interface | IOU interface |
| --- | --- | --- |
| Jack | Serial0/0 | Serial4/0 |
| Jack | Serial0/1 | Serial4/1 |
| Jack | Serial0/2 | Serial4/2 |
| Jack | Serial0/3 | Serial4/3 |
| Johnson | Serial0/0 | Serial4/0 |
| Johnson | Serial0/1 | Serial4/1 |
| Johnson | Serial0/2 | Serial4/2 |
| Johnson | Serial0/3 | Serial4/3 |

### Source notes

No source topology/startups were supplied. Reconstructed the serial link from the diagram and final configs; startup preserves EIGRP AS12 and addressing but omits authentication/key chains.

Original key lifetimes expired in 2021. Set lab clocks to the historical exercise window before testing rollover; dates remain unchanged. The supplied Key2 lifetimes start at 08:45, while the goal specifies 08:50.

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

## Video Solution

[EIGRP Authentication Rotating Key Video Solution](http://www.youtube.com/watch?v=-a2bmuoY2Qk)
