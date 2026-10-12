# EIGRP Debug AS number

## Scenario

One of your colleagues is on vacation and forgot to document the EIGRP topology before he left. You need to add another EIGRP router but you have no idea what the autonomous system (AS) number is of the other routers. Unfortunately you are unable to look it up but you do know that authentication is not enabled. With a bit of luck you might be able to debug your way out of this one!

## Goal

- All IP addresses have been preconfigured for you.
- EIGRP has been preconfigured for you on router John.
- Use a debug command on router Jack to retrieve the EIGRP AS number.

## GNS3 2.2.56.1

Import `EIGRP Debug AS IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `EIGRP Debug AS.gns3` beside `project-files`.

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
| Jack | FastEthernet0/0 | Ethernet0/0 |
| John | FastEthernet0/0 | Ethernet0/0 |

### Source notes

No completed solution configs were supplied; none were invented.

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-eigrp-debug-as-number.png)

## Video Solution

http://www.youtube.com/watch?v=pD91zMiF_CE
