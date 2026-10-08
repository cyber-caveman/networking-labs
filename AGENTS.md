# Project defaults for GNS3 labs

Use these user-selected device models for GNS3 labs created or converted in this
repository, unless the user specifies otherwise. Target GNS3 **2.2.56.1**.
The user successfully imported and ran the converted OSPF Authentication portable
project. Preserve that compatible project format and startup-config packaging.

## IOU L3 routers

- Node type: `iou`
- Image: `x86_64_crb_linux-adventerprisek9-ms.bin`
- MD5: `4a2fce8de21d1831fbceffd155e41ae7`
- Template ID: `b3b10b90-adfb-43f8-b289-b68bcf322ad8`
- Ethernet adapters: **4**
- Serial adapters: **4**
- RAM: **768 MB**
- NVRAM: **128 KB**
- Symbol: `:/symbols/classic/router.svg`
- Width: 66; height: 45

## IOU L2 switches

Use this model when replacing CLI-configurable switches. Preserve unmanaged
("dumb") switches that do not support CLI configuration, hubs, and Frame Relay
switches as their original device types; do not replace them with IOU L2 switches.

- Node type: `iou`
- Image: `i86bi-linux-l2-adventerprisek9-15.2d.bin`
- MD5: `f16db44433beb3e8c828db5ddad1de8a`
- Template ID: `87fd8b26-489a-424e-a7de-1e590da4ccc6`
- Ethernet adapters: **4**
- Serial adapters: **0**
- RAM: **256 MB**
- NVRAM: **32 KB** (user override of the example's 16 KB)
- Symbol: `:/symbols/classic/multilayer_switch.svg`
- Width: 51; height: 48

## Available C3640 appliance

The user also has this appliance installed on the GNS3 VM running on a remote
server. Its supplied working node uses `compute_id: local`. This availability
update does not supersede the preferred IOU models or request existing lab changes.

- Node type: `dynamips`
- Platform: `c3600`; chassis: `3640`
- Image: `c3640-a3js-mz.124-25d.image`
- Image MD5: `493c4ef6578801d74d715e7d11596964`
- Template ID: `b7a0bd2a-0e7d-4ea8-8c93-3b580f78971e`
- RAM: **192 MB**; NVRAM: **256 KB**; `iomem`: `5`
- `idlepc`: `0x6050b114`; `idlemax`: `500`; `idlesleep`: `30`
- `clock_divisor`: `4`; `exec_area`: `64`
- `mmap`: `true`; `sparsemem`: `true`; `auto_delete_disks`: `false`
- `disk0`: `0`; `disk1`: `0`; `aux`: `null`; `usage`: empty string
- `system_id`: `FTX0945W0MY`
- `port_name_format`: `Ethernet{0}`; `port_segment_size`: `0`
- Symbol: `:/symbols/classic/router.svg`; width: 66; height: 45
- The example has `slot0` through `slot3` set to `null`. Select appropriate
  modules for the lab's required links when using this appliance; do not assume
  the example has network interfaces installed.
- Assign distinct node UUIDs, Dynamips IDs, and MAC addresses rather than copying
  the example's instance identifiers. Allocate console ports automatically.
- Use Dynamips-specific startup-config packaging when using this appliance;
  the IOU configuration directory convention below applies only to IOU nodes.

## Shared IOU settings and conversion conventions

- `compute_id`: `local`
- `console_type`: `telnet`
- `console_auto_start`: `false`
- `custom_adapters`: `[]`
- `first_port_name`: `null`
- `port_name_format`: `Ethernet{segment0}/{port0}`
- `port_segment_size`: `4`
- `l1_keepalives`: `false`
- `use_default_iou_values`: `true`
- `usage`: empty string
- Assign unique node UUIDs and IOU application IDs per topology. Allocate console
  ports automatically rather than copying a sample's fixed console port.

## Conversion conventions for all device types

- Adapt interface names, link endpoints, and startup and solution configurations
  together. Preserve the exercise's addressing and intended initial state.
- Whenever startup configurations change, update the corresponding solution
  configurations (including `final-configs`) accordingly. Verify that each
  updated solution is functionally equivalent to its original solution after
  accounting for the device and interface changes. Check the lab-relevant
  addressing, connectivity, protocol behavior, authentication, and other solution
  requirements; syntax or interface-name checks alone are insufficient. Report
  the verification performed and distinguish configuration analysis from live
  testing, explicitly identifying any behavior that could not be verified.
- Configuration changes to Frame Relay switches or routers are authorized only
  when required to preserve the lab's operation after existing switches or routers
  are replaced. Limit these changes to what is necessary for that compatibility;
  otherwise preserve their configurations.
- Bundle IOU router and switch startup configs under
  `project-files/iou/<node-id>/startup-config.cfg`; include these with
  `project.gns3` in portable `.gns3project` archives.
- These defaults govern subsequent lab work. A request to remember settings alone
  does not request a bulk conversion of existing labs or containerlab artifacts.
