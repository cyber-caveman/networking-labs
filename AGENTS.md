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

## Shared settings and conversion conventions

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
- Adapt interface names, link endpoints, and startup and solution configurations
  together. Preserve the exercise's addressing and intended initial state.
- Bundle router and switch startup configs under
  `project-files/iou/<node-id>/startup-config.cfg`; include these with
  `project.gns3` in portable `.gns3project` archives.
- These defaults govern subsequent lab work. A request to remember settings alone
  does not request a bulk conversion of existing labs or containerlab artifacts.
