# OSPF Single Area

![Network Topology](./topology-ospf-single-area.jpg)

## Scenario

AsianFish inc. is expanding their business towards Europe so they need to expand their network as well. You are responsible for the performance of the network and decided that OSPF would be a suitable candidate for a routing protocol. Because the network at this moment is still small, you decided a single area OSPF should be enough. It's up to you to make it work!

## Goal

* All IP addresses have been preconfigured for you.
* The following loopback interfaces have been configured:
  - HongKong: 1.1.1.1 /24
  - Amsterdam: 2.2.2.2 /24
  - Barcelona: 3.3.3.3 /24
* HongKong: Configure OSPF (process-id 1) and advertise all networks by using a single network statement. Use area0
* Amsterdam: Configure OSPF (process-id 1) and advertise all networks by using 2 network statements, area0.
* Barcelona: Configure OSPF (process-id 1) and advertise all networks by using 3 network statements, area0.
* Optional: the loopback interfaces appear as /32's in the routing table, make sure they appear as /24's just as you configured them.
* Amsterdam: change the router-id to 22.22.22.22, make sure you see this change from Barcelona by using show commands.
* Traffic from Barcelona to HongKong should use the link between Amsterdam-Barcelona, use the cost command to achieve this.
* Remove the previous change with the cost-command, achieve the same goal by using the bandwidth command.
* Enable clear-text authentication between Amsterdam and HongKong. Use "vault" as a password.
* Enable MD5 authentication between Barcelona and HongKong. Use "Safe" as a password.
* Change the OSPF timers on the link between Amsterdam and Barcelona so hello packets are being sent every 5 seconds.
* The HongKong router will have access to the Internet in the future, you need to advertise a default route in OSPF so Amsterdam and Barcelona will send traffic for unknown networks to HongKong.

## GNS3 2.2.56.1

Import `OSPF Single Area IOU.gns3project` with **File > Import portable project**.
The archive includes the startup configs and the original topology illustration.
For direct opening, keep `OSPF Single Area.gns3` beside `project-files`.

Exercise routers use `x86_64_crb_linux-adventerprisek9-ms.bin`
(MD5 `4a2fce8de21d1831fbceffd155e41ae7`), 768 MB RAM, 128 KB NVRAM,
four Ethernet adapters and four serial adapters. Console ports are allocated automatically.

Startup and solution configs use the mapped IOU interfaces. Ethernet interfaces
retain the original bandwidth values in Kbit/s so OSPF metrics preserve the exercise.
Original reference images and legacy `.net` files may show the old interface names;
the converted `.gns3` project is the runnable topology.

| Router | Original interface | IOU interface |
| --- | --- | --- |
| HongKong | FastEthernet0/0 | Ethernet0/0 |
| HongKong | FastEthernet1/0 | Ethernet0/1 |
| Amsterdam | FastEthernet0/0 | Ethernet0/0 |
| Amsterdam | FastEthernet1/0 | Ethernet0/1 |
| Barcelona | FastEthernet0/0 | Ethernet0/0 |
| Barcelona | FastEthernet1/0 | Ethernet0/1 |

Source solution caveat: `final-configs/Amsterdam.cfg` contains a HongKong
configuration in the original archive. It is retained as supplied, with interface
names adapted; it is not an Amsterdam solution.

Containerlab files are independent and unchanged. Structure, config packaging and
interface mappings were validated; boot and protocol behavior require the target
GNS3 server and the specified images.

## Topology

## Video Solution

http://www.youtube.com/watch?v=ugAqUqZdGkM

## Configuration verification

Barcelona’s bandwidth 100 Kbit/s (cost 1000), MD5, hello interval 5 and network statements retained; HongKong plaintext/MD5 and default origination retained.

Amsterdam.cfg is a duplicate HongKong config in the source, so the provided set is not a valid three-router solution. Its missing Loopback0 declaration was repaired; the misidentified solution is otherwise preserved.

These findings come from configuration analysis against the original files.
Boot, command support, adjacencies, routing tables and packet forwarding were not
tested live. See [the full verification report](../VERIFICATION.md) in the repository
(or `VERIFICATION.md` included in the portable archive).
