# Conversion verification

## 2026-10-10 settings refresh

All IOU devices now use 512 KB NVRAM. Other device settings were checked against `AGENTS.md`. Config text is byte-for-byte unchanged from the previously converted working tree; startup and solution behavior was not altered by this memory-setting change. Switch port lists were normalized where needed so GNS3’s port indices match the saved link endpoints. Projects pass the installed schemas and real port-factory checks; portable archives were rebuilt and checked against loose files. Prior source limitations remain. No live router testing was performed.
