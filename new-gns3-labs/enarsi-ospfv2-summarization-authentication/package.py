#!/usr/bin/env python3
from pathlib import Path
import zipfile
P=Path(__file__).resolve().parent
out=P/'ENARSI OSPFv2 Summarization and Authentication IOU.gns3project'
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
 for f in sorted(P.rglob('*')):
  if f.is_file() and f.suffix!='.gns3project' and '__pycache__' not in f.parts:
   info=zipfile.ZipInfo(str(f.relative_to(P)),date_time=(2026,11,1,0,0,0))
   info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o644<<16
   z.writestr(info,f.read_bytes())
print(out.name)
