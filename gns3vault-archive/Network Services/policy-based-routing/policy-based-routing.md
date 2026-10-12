# Policy Based Routing

## Scenario

After getting rid of the ring that ruled them all things have changed in Middle Earth. The hobbits have become network engineers and are interconnecting every creature in their fantasy world. OSPF is the routing protocol of choice but the hobbits have some problems since all traffic is sent down the same path. Do you think you can help them out by teaching them Policy Based Routing?

## Goal

- All IP addresses have been preconfigured for you.
- OSPF has been preconfigured for you for full connectivity.
- Do not make any changes to OSPF.
- Make changes on router Bilbo so traffic from 1.1.1.0 towards router Meriadoc is sent down the serial link.
- Make changes on router Bilbo so traffic from 192.168.12.1 towards 33.33.33.33 is sent down the serial link.
- Make changes on router Bilbo so packets that are greater than 200 bytes are sent down the serial link.
- Make changes on router Bilbo so traffic from 192.168.12.2 towards 3.3.3.3 is sent down the serial link.

## GNS3 2.2.56.1

Import [Policy Based Routing IOU.gns3project](Policy%20Based%20Routing%20IOU.gns3project) using **File > Import portable project**. To open `Policy Based Routing.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Frodo | FastEthernet0/0 | Ethernet0/0 |
| Bilbo | FastEthernet0/0 | Ethernet0/0 |
| Bilbo | FastEthernet1/0 | Ethernet0/1 |
| Bilbo | Serial2/0 | Serial4/0 |
| Bilbo | Serial2/1 | Serial4/1 |
| Bilbo | Serial2/2 | Serial4/2 |
| Bilbo | Serial2/3 | Serial4/3 |
| Pippin | FastEthernet0/0 | Ethernet0/0 |
| Pippin | FastEthernet1/0 | Ethernet0/1 |
| Merry | FastEthernet0/0 | Ethernet0/0 |
| Merry | Serial1/0 | Serial4/0 |
| Merry | Serial1/1 | Serial4/1 |
| Merry | Serial1/2 | Serial4/2 |
| Merry | Serial1/3 | Serial4/3 |
| Meriadoc | FastEthernet0/0 | Ethernet0/0 |
| Meriadoc | FastEthernet1/0 | Ethernet0/1 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology

![Network Topology](./topology-policy-based-routing.png)

## Video Solution

[http://www.youtube.com/watch?v=T-cv2H6SP5c](http://www.youtube.com/watch?v=T-cv2H6SP5c)
