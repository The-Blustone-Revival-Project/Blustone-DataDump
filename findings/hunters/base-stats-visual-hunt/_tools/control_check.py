#!/usr/bin/env python3
"""Strict control validation: does the id_ fetch of the 051 profile reproduce
all 13 TSV tokens? If not, the read path is wrong and no zero below counts.
"""
import io
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HERE, "_archives_work")

tsv = os.path.join(HERE, "archived-hunter-database-2019.tsv")
lines = open(tsv, encoding="utf-8").read().split("\n")
hdr = [h.strip('"') for h in lines[0].split("\t")]
FIELDS = ["combat_power", "hp", "atk", "def", "speed", "crit", "crit_damage",
          "penetration", "block", "block_damage_reduction", "element_enhance",
          "element_resistance", "hp_regen"]
row = None
for l in lines[1:]:
    if not l.strip():
        continue
    f = [x.strip('"') for x in l.split("\t")]
    d = dict(zip(hdr, f))
    if d.get("catalog_id") == "051":
        row = d
        break
if row is None:
    print("051 ROW NOT FOUND -- control cannot be validated")
    sys.exit(2)

html = open(os.path.join(OUT, "control-beckhen.html"), encoding="utf-8", errors="replace").read()
print(f"control html chars={len(html)}")
print(f"row profile_title={row['profile_title']}  url={row['source_url'][:110]}")

# tokens may appear raw (no comma) since TSV stripped commas
ok = miss = 0
for f in FIELDS:
    v = row[f]
    hit = re.search(r"(?<![\d,])" + re.escape(v) + r"(?![\d,])", html)
    if hit:
        print(f"  {f:24s} {v:>8s}  FOUND")
        ok += 1
    else:
        print(f"  {f:24s} {v:>8s}  MISSING")
        miss += 1
print(f"\ncontrol: {ok}/{len(FIELDS)} tokens reproduced, {miss} missing")
print("CONTROL", "PASS" if miss == 0 else "PARTIAL")

text = re.sub(r"<[^>]+>", " ", html)
text = re.sub(r"\s+", " ", text)
for anchor in ["基本能力値", "戦闘力", "レベル"]:
    i = text.find(anchor)
    print(f"\n--- {anchor} @ {i} ---")
    if i >= 0:
        print(text[max(0, i - 120):i + 700])