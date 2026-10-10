# -*- coding: utf-8 -*-
"""Extract the FULL hunter roster table from the local namu dump, with the
BTB cross-title flags, so the Lantern/Nene agreement check has real rows.

Guard rule 13: role/element Hangul is SLICED from the data, not typed.
"""
import io
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

D = "analysis/research/base-stats-visual-hunt/_tools/_namu_raw/"
OUT = "analysis/research/base-stats-visual-hunt/_tools/btb_lane/hunter_rows.txt"

t = io.open(D + "ctrl-d-hunter.text.txt", encoding="utf-8", errors="replace").read()
print("chars:", len(t))

# The table rows look like: " ☆☆☆ | 화속 | 최고의 요리사 치르치르 | <description> | "
rowre = re.compile(
    r"^\s*(\u2606+[\s\u2606]*)\s*\|\s*([\uAC00-\uD7A3]+)\s*\|\s*([^|]+?)\s*\|\s*(.*?)\s*\|\s*$",
    re.M,
)

L = []
rows = rowre.findall(t)
L.append("matched roster rows: %d" % len(rows))
L.append("")

# Harvest any BTB mention anywhere in the document, with its owning row.
for stars, attr, name, desc in rows:
    desc_clean = re.sub(r"<[^>]+>", "", desc)
    desc_clean = desc_clean.replace("&#91;", "[").replace("&#93;", "]").replace("&amp;", "&")
    if "BTB" in desc_clean or "\ube44\uc698\ub4dc" in desc_clean:
        L.append("=" * 90)
        L.append("CROSS-TITLE ROW")
        L.append("  stars : %s" % stars.strip())
        L.append("  attr  : %s" % attr)
        L.append("  name  : %s" % name.strip())
        L.append("  text  : %s" % desc_clean[:1400])
        L.append("")

# Also: every row, condensed, so role/element can be cross-checked.
L.append("=" * 90)
L.append("ALL ROSTER ROWS (stars | attribute | name)")
L.append("=" * 90)
for stars, attr, name, desc in rows:
    L.append("  %-8s | %-6s | %s" % (stars.strip(), attr, name.strip()))

io.open(OUT, "w", encoding="utf-8", newline="\n").write("\n".join(L))
print("wrote", OUT)
print("cross-title rows:", sum(1 for x in L if x == "CROSS-TITLE ROW"))