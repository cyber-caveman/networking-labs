# OSPF Authentication

![Network Topology](./topology-ospf-authentication.png)

## Scenario:

The local zoo needs your help with their OSPF network. Since a recent animal breakout the security department decides all routing protocols need authentication. You decide to implement OSPF authentication in any way you can.

## Goal:

- All IP addresses have been preconfigured for you.
- Configure OSPF on all routers. Achieve full connectivity. Ensure area 2 is directly connected by using a virtual link.
- Configure MD5 authentication for Area 0. Do not use any interface commands to activate it.
- Configure plaintext authentication in Area 1. Use interface commands to achieve this.
- Configure MD5 authentication for the virtual link.

## Additional Information:

## IOS:

- IOU L3: `x86_64_crb_linux-adventerprisek9-ms.bin`
- Image MD5: `4a2fce8de21d1831fbceffd155e41ae7`
- Uses the supplied IOU template settings: 768 MB RAM, 128 KB NVRAM,
  one Ethernet adapter (four ports), one serial adapter, and default IOU values enabled.

## Import into GNS3:

1. Select **File > Import portable project** and choose
   `OSPF Authentication IOU.gns3project` from this folder.
2. Import it into the GNS3 instance where the IOU image above already works, then
   start the routers.

The archive includes all four startup configurations in GNS3's
`project-files/iou/<node-id>/startup-config.cfg` layout. The IOS image is supplied
by your existing GNS3 installation. Nodes use `compute_id: local`, matching the
provided working router example; GNS3's portable importer may assign IOU nodes
to its configured GNS3 VM depending on the server platform.

`OSPF Authentication.gns3` is also converted to GNS3 2.2 format. If opening this
file directly, keep the accompanying `project-files` directory beside it.
Console ports are allocated automatically to avoid collisions with other labs.

Startup configurations contain the original IP addressing with connected
interfaces enabled. OSPF and authentication remain unconfigured for the
exercise. The converted completed solutions are in `final-configs` and are not
loaded at startup.

The imported canvas preserves the routers, switch, links, area shading, and
address labels. The original reference image above uses these old interface names:

| Original interface | IOU interface |
| --- | --- |
| FastEthernet0/0 | Ethernet0/0 |
| FastEthernet1/0 | Ethernet0/1 |

The C3640-specific memory command and old speed/duplex commands were removed.
The separate `containerlab` implementation remains independent of this GNS3 conversion.

Project packaging follows the [GNS3 file format documentation](https://api.gns3.net/en/2.2/file_format.html).
File structure and interface mappings were checked; boot and routing behavior
must still be verified on the target GNS3 server with the specified IOU image.

## Topology:

## Video Solution:

- [YouTube Video](http://www.youtube.com/watch?v=awytpQIOGCk)
