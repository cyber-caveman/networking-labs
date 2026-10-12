# EIGRP Summarization without Null0

## Scenario

You are applying for a job as a senior network engineer at a large ISP. They heard you passed your CCIE so they want to test you by giving a topology with an EIGRP summarization question. Let's see if you can work your way out of this one...

## Goal

- All IP addresses have been preconfigured for you.
- Configure EIGRP on all interfaces.
- Advertise a 1.1.0.0 /16 summary on router Hollywood on any interface.
- Ensure no null0 entry is installed in the routing table of router Hollywood.
- You are not allowed to use static or default routes.

## Additional Information

## GNS3 2.2.56.1

Import `eigrp-summarization-without-null0 IOU.gns3project` with **File > Import portable project**.
For direct opening, keep `eigrp-summarization-without-null0.gns3` beside `project-files`.

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
| Hollywood | FastEthernet0/0 | Ethernet0/0 |
| Bollywood | FastEthernet0/0 | Ethernet0/0 |

### Source notes

No source topology or configs were supplied. Reconstructed the two-router link and visible addresses from the diagram; routing remains unconfigured.

No completed solution configs were supplied; none were invented.

Original topology images and `.net` files are references; the converted project
and mapping table specify the current interfaces. Containerlab files are unchanged.

See `VERIFICATION.md` in this folder or portable archive for configuration analysis
and source issues. Live IOS command support, neighbor formation, route selection,
Frame Relay PVC state and packet forwarding have not been tested on the remote server.

## Topology

![Network Topology](./topology-eigrp-summarization-without-null0.png)

## Video Solution

- [YouTube Video Solution](http://www.youtube.com/watch?v=y7Lr_KjY_O4)
