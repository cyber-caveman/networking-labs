#!/usr/bin/env python3
"""Rebuild the portable project with unsolved startup state and all lab material."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
P = Path(__file__).resolve().parent
ARCHIVE = P / 'ENARSI IPv6 First-Hop Security IOU.gns3project'
def members():
    roots = ['project.gns3', 'project-files', 'startup-configs', 'final-configs', 'solutions']
    files = [p for root in roots for p in ([P/root] if (P/root).is_file() else (P/root).rglob('*')) if p.is_file()]
    files += list(P.glob('*.md')) + list(P.glob('*.py'))
    return sorted(set(files))
if __name__ == '__main__':
    with ZipFile(ARCHIVE, 'w', ZIP_DEFLATED) as archive:
        for path in members():
            archive.write(path, path.relative_to(P).as_posix())
    print(f'Packaged {ARCHIVE.name}')
