#!/usr/bin/env python3

from pathlib import Path

content = Path("CONTRIBUTING.mdt")

heading_level = 0
in_comment = False
for line in content.read_text().split("\n"):
    if line.startswith("#"):
        heading_level = len(line.split(" ")[0])

    if not line.startswith("!INCLUDE"):
        print(line)
        continue

    params = line.split(" ")
    include_pattern = params[1]
    if len(params) > 2 and params[2].startswith("level="):
        heading_level = int(params[2][6:]) - 1

    for included_file in sorted(Path(".").rglob(include_pattern)):
        for iline in included_file.read_text().split("\n"):
            if iline.startswith("```"):
                in_comment = not in_comment

            if iline.startswith("#") and not in_comment:
                iline = "#" * heading_level + iline
            print(iline)
