# OSPF MD5 Authentication Rotating Key

## Scenario

You work for the government as a contracted network engineer. They want you to improve their OSPF security. Instead of using a single key for all routers they want to ensure each OSPF neighbor adjacency has a different key. Let's find out if you can lock this one down.

## Goal

- All IP addresses have been preconfigured for you.
- Configure OSPF on all routers. Achieve full connectivity.
- Router Twist and Turn have to use password "PASSWORD".
- Router Twist and Rotate have to use password "VAULT".

## GNS3 2.2.56.1

Import `OSPF MD5 Authentication Rotating Key IOU.gns3project` with **File > Import portable project**.
The archive includes the startup configs and the original topology illustration.
For direct opening, keep `OSPF MD5 Authentication Rotating Key.gns3` beside `project-files`.

Exercise routers use `x86_64_crb_linux-adventerprisek9-ms.bin`
(MD5 `4a2fce8de21d1831fbceffd155e41ae7`), 768 MB RAM, 128 KB NVRAM,
four Ethernet adapters and four serial adapters. Console ports are allocated automatically.
The unmanaged Ethernet switches retain their original device type.

Startup and solution configs use the mapped IOU interfaces. Ethernet interfaces
retain the original bandwidth values in Kbit/s so OSPF metrics preserve the exercise.
Original reference images and legacy `.net` files may show the old interface names;
the converted `.gns3` project is the runnable topology.

| Router | Original interface | IOU interface |
| --- | --- | --- |
| Rotate | FastEthernet0/0 | Ethernet0/0 |
| Turn | FastEthernet0/0 | Ethernet0/0 |
| Twist | FastEthernet0/0 | Ethernet0/0 |

Containerlab files are independent and unchanged. Structure, config packaging and
interface mappings were validated; boot and protocol behavior require the target
GNS3 server and the specified images.

## Topology

![Network Topology](./topology-ospf-md5-authentication-rotating-key.png)

## Video Solution

http://www.youtube.com/watch?v=4Mi2ZxrKgbQ

## Configuration verification

One shared broadcast segment, Twist’s two key IDs and the matching individual Turn/Rotate MD5 keys retained.

Multiple-key rollover adjacency behavior requires live image testing.

These findings come from configuration analysis against the original files.
Boot, command support, adjacencies, routing tables and packet forwarding were not
tested live. See [the full verification report](../VERIFICATION.md) in the repository
(or `VERIFICATION.md` included in the portable archive).
