#!/usr/bin/env python3

"""
Parses a markdown template file (custom schema)
to render a markdown file.

The markdown template file supports the include of files with this syntax:
  !INCLUDE <filename> level=xxx

  The script will include the content of "filename" in place adapting the
  heading level to xxx if necessary.
"""

from pathlib import Path

template = Path("CONTRIBUTING.mdt")

heading_level = 0
in_comment = False
for template_line in template.read_text().split("\n"):
    if template_line.startswith("#"):
        heading_level = len(template_line.split(" ")[0])

    if not template_line.startswith("!INCLUDE"):
        print(template_line)
        continue

    include_params = template_line.split(" ")
    include_pattern = include_params[1]
    if len(include_params) > 2 and include_params[2].startswith("level="):
        heading_level = int(include_params[2][6:]) - 1

    for included_file in sorted(Path(".").rglob(include_pattern)):
        for included_file_line in included_file.read_text().split("\n"):
            if included_file_line.startswith("```"):
                in_comment = not in_comment

            if included_file_line.startswith("#") and not in_comment:
                included_file_line = "#" * heading_level + included_file_line
            print(included_file_line)
