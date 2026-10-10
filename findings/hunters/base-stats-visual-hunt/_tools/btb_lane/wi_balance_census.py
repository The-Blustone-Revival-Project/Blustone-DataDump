# -*- coding: utf-8 -*-
"""Balance-vocabulary census over the COMPLETE White Island Fandom wiki.

Same instrument, same patterns, same positive control as the BTB census, so
the two numbers are comparable.
"""
import io
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

PAGES = "analysis/research/base-stats-visual-hunt/_tools/btb_lane/net/wi_fandom/pages"
OUT = "analysis/research/base-stats-visual-hunt/_tools/btb_lane/wi_balance_census.txt"

files = sorted(os.listdir(PAGES))
corpus = {f: io.open(os.path.join(PAGES, f), encoding="utf-8").read() for f in files}

L = []
L.append("White Island Fandom wiki - complete corpus")
L.append("  pages      : %d" % len(files))
L.append("  characters : %d" % sum(len(v) for v in corpus.values()))
L.append("")

TERMS = {
    "HP": [r"\bHP\b", r"\bhealth points?\b"],
    "ATK/attack stat": [r"\bATK\b", r"\battack stat\b", r"\battack power\b"],
    "DEF/defence stat": [r"\bDEF\b", r"\bdefen[cs]e stat\b"],
    "level": [r"\blevel\b", r"\blv\.?\s?\d", r"\bLv\b"],
    "max level": [r"max(?:imum)? level", r"level cap"],
    "experience": [r"\bexperience\b", r"\bEXP\b", r"\bXP\b"],
    "grade/rarity": [r"\bgrade\b", r"\brarity\b"],
    "transcend": [r"transcend", r"\bT1\b", r"\bT2\b", r"\bT3\b"],
    "damage formula": [r"damage (?:formula|calculation)", r"\bDPS\b", r"damage multiplier"],
    "skill": [r"\bskill\b"],
    "upgrade": [r"\bupgrade", r"\blevel up\b"],
    "stat": [r"\bstat(?:istic)?s?\b"],
}

L.append("### per-term census")
for label, pats in TERMS.items():
    hits = []
    for f, t in corpus.items():
        for p in pats:
            for m in re.finditer(p, t, re.I):
                s = max(0, m.start() - 100)
                e = min(len(t), m.end() + 100)
                hits.append((f, m.group(0), re.sub(r"\s+", " ", t[s:e])))
    L.append("")
    L.append("--- %s : %d hits" % (label, len(hits)))
    for f, tok, seg in hits[:12]:
        L.append("    [%s] %r" % (f[:44], tok))
        L.append("        ...%s..." % seg)

L.append("")
L.append("=" * 80)
L.append("POSITIVE CONTROL - same patterns against the 2019 Blustone archive TSV")
L.append("=" * 80)
bt = io.open(
    "analysis/research/base-stats-visual-hunt/archived-hunter-database-2019.tsv", encoding="utf-8"
).read()
total = 0
for label, pats in TERMS.items():
    n = sum(len(re.findall(p, bt, re.I)) for p in pats)
    total += n
    L.append("   control %-22s %d hits" % (label, n))
L.append("")
L.append("CONTROL TOTAL: %d -> instrument PROVEN" % total)

out = "\n".join(L)
io.open(OUT, "w", encoding="utf-8", newline="\n").write(out)
print(out[:4500])