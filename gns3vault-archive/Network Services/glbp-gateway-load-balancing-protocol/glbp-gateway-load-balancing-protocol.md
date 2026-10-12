# Gateway Load Balancing Protocol (GLBP)

![Network Topology](./topology-glbp-gateway-load-balancing-protocol.jpg)

## Scenario:

As an employee for a top-secret Government organization you are responsible for their advanced network. Several employees need to have access to send data, no matter what happens to the network. To enhance the reliability of the network you decide to configure GLBP (Gateway Load Balancing Protocol), in addition you want to configure load-balancing to make optimal use of the resources you have. Get the job done and you can get back to sipping Martinis...shaken not stirred.

## Goal:

* All IP addresses have been preconfigured for you.
* OSPF has been configured between router Dalton, Moore and MoneyPenny.
* Router MoneyPenny has a loopback0 interface (IP address 5.5.5.5) which is advertised into OSPF. This can be used for testing your configuration.
* Router Connery and Brosnan have 'ip routing' disabled. Their default-gateway is set to 7.7.7.7.
* Change the mac-addresses on Router Dalton and Moore on their F0/0 interfaces:
  - Dalton: 0000.0000.0001
  - Moore: 0000.0000.0002
* Configure GLBP between router Dalton and Moore on their F0/0 interfaces, the virtual IP address should be 7.7.7.7. Use group number 7.
* Enable GLBP plaintext authentication. Use the password 'vault'.
* Change the GLBP load-balancing so packets are forwarded based on the host.
* Change the GLBP priority of Router Dalton to 120.
* Enable GLBP preempt on both Routers.
* Change the GLBP timers so hello packets are sent every 50 msec, the holddown timer should be 500 msec.
* Enable interface tracking on router Dalton for Serial 1/0, you need to check for the line-protocol.
* The starting weight for Router Dalton should be 120. When the loopback0 interface goes down it should decrement by 50.
* When the weight drops below 80 Router Dalton should no longer be the AVF (Active Virtual Gateway). The weight should be at least 90 before Router Dalton can become the AVF again.

## Additional Resources:

## GNS3 2.2.56.1

Import [glbp-startup-configs IOU.gns3project](glbp-startup-configs%20IOU.gns3project) using **File > Import portable project**. To open `glbp-startup-configs.gns3` directly, keep it beside `project-files`.

IOU L3 routers use `x86_64_crb_linux-adventerprisek9-ms.bin`, 768 MB RAM, **512 KB NVRAM**, four Ethernet and four serial adapters. CLI switches use the preferred IOU L2 image `i86bi-linux-l2-adventerprisek9-15.2d.bin`, 256 MB RAM, **512 KB NVRAM**, four Ethernet adapters and no serial adapters. Images, checksums, templates and shared settings follow `AGENTS.md`; consoles allocate automatically. Startup configs are bundled under `project-files/iou/<node-id>/startup-config.cfg`.

Unmanaged Ethernet and built-in Frame Relay switches retain their device types and VLAN/PVC settings. Connected IOU interfaces use ANSI LMI for the built-in Frame Relay switch.

Startup and supplied final configurations use the interface mappings below. Effective bandwidth, delay, administrative state and routing/policy command contexts were compared against their source. Obsolete hardware-only commands are removed. Ports omitted to fit the selected model are unused hardware-only ports, listed in the verification notes.

| Device | Source interface | Current interface |
| --- | --- | --- |
| Dalton | FastEthernet0/0 | Ethernet0/0 |
| Dalton | Serial1/0 | Serial4/0 |
| Dalton | Serial1/1 | Serial4/1 |
| Dalton | Serial1/2 | Serial4/2 |
| Dalton | Serial1/3 | Serial4/3 |
| Moore | FastEthernet0/0 | Ethernet0/0 |
| Moore | Serial1/0 | Serial4/0 |
| Moore | Serial1/1 | Serial4/1 |
| Moore | Serial1/2 | Serial4/2 |
| Moore | Serial1/3 | Serial4/3 |
| Connery | FastEthernet0/0 | Ethernet0/0 |
| Brosnan | FastEthernet0/0 | Ethernet0/0 |
| MoneyPenny | Serial0/0 | Serial4/0 |
| MoneyPenny | Serial0/1 | Serial4/1 |
| MoneyPenny | Serial0/2 | Serial4/2 |
| MoneyPenny | Serial0/3 | Serial4/3 |

See [verification, reconstruction and source limitations](VERIFICATION.md). Portable archives contain the initial state and supplied solution files separately; final configs are not loaded at startup. Original `.net` files and diagrams are reference material. Containerlab artifacts are unchanged.

## Topology:

## Video Solution:

http://www.youtube.com/watch?v=n_l_Xa5IYHY
