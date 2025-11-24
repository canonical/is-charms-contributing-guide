#!/usr/bin/env python3

from pathlib import Path

content = Path("CONTRIBUTING.mdt")

heading_level = 0
for line in content.read_text().split("\n"):
    if line.startswith("#"):
        heading_level = len(line.split(" ")[0])

    if not line.startswith("!INCLUDE"):
        print(line)
        continue

    include_pattern = line.split(" ")[1]
    for included_file in sorted(Path(".").rglob(include_pattern)):
        for iline in included_file.read_text().split("\n"):
            if iline.startswith("#"):
                iline = "#" * heading_level + iline
            print(iline)
