# -*- coding: utf-8 -*-
"""Pull Lantern(001)/Nene(003) baseline identity rows for the sister-game cross-check."""
import io
import sys

sys.stdout.reconfigure(encoding="utf-8")

ARCHIVE = "analysis/research/base-stats-visual-hunt/archived-hunter-database-2019.tsv"

lines = io.open(ARCHIVE, encoding="utf-8").read().split("\n")
hdr = lines[0].split("\t")
for raw in lines[1:]:
    if not raw.strip():
        continue
    fields = raw.split("\t")
    catalog = fields[-3].strip('"')
    if catalog in ("001", "003"):
        print("catalog", catalog)
        for h, v in zip(hdr, fields):
            print("   ", h, "=", v.strip('"'))
        print()