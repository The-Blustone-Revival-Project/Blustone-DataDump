# -*- coding: utf-8 -*-
"""Extract every White Island page's content so the engine/season claim and any
balance-relevant statement is on the record, not paraphrased from memory.
"""
import io
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

P = "analysis/research/base-stats-visual-hunt/_tools/btb_lane/net/wi_fandom/pages"
OUT = "analysis/research/base-stats-visual-hunt/_tools/btb_lane/wi_pages_dump.txt"

L = []
for f in sorted(os.listdir(P)):
    t = io.open(os.path.join(P, f), encoding="utf-8").read()
    t = re.sub(r"\s+", " ", t).strip()
    L.append("=" * 90)
    L.append("### %s   (%d chars)" % (f, len(t)))
    L.append(t[:1800])
    L.append("")

out = "\n".join(L)
io.open(OUT, "w", encoding="utf-8", newline="\n").write(out)
print(out[:6000])