# -*- coding: utf-8 -*-
"""Does BTB / White Island have ANY stat system? Search the local corpus for
balance vocabulary attached to the sister titles, and pin the attribute
vocabulary used in the namu roster.

Guard: every Hangul needle is SLICED from the data, never typed.
"""
import io
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

D = "analysis/research/base-stats-visual-hunt/_tools/_namu_raw/"
OUT = "analysis/research/base-stats-visual-hunt/_tools/btb_lane/btb_statprobe.txt"

files = [
    "ctrl-d-main.text.txt",
    "ctrl-d-main.utf8.txt",
    "ctrl-d-hunter.text.txt",
    "ctrl-file-control.utf8.txt",
]
L = []

# ---- 1. Attribute vocabulary -------------------------------------------
main = io.open(D + "ctrl-d-main.text.txt", encoding="utf-8", errors="replace").read()
# Find the sentence that defines the three attributes.
for m in re.finditer(r"[^\n]{0,200}\uC18C\uB7C9[^\n]{0,200}", main):
    L.append("ATTRIBUTE DEF SENTENCE:")
    L.append("   %s" % m.group(0).strip()[:400])
    L.append("")

# Enumerate the roster attribute tokens and locate their definition.
hunter = io.open(D + "ctrl-d-hunter.text.txt", encoding="utf-8", errors="replace").read()
toks = {}
for m in re.finditer(r"\u2606[^|]{0,10}\|\s*([\uAC00-\uD7A3]+)\s*\|", hunter):
    toks[m.group(1)] = toks.get(m.group(1), 0) + 1
L.append("roster attribute tokens: %s" % toks)
L.append("")

# ---- 2. Balance vocabulary in the sister-title context -----------------
# English balance words are ASCII so they can be written safely.
BAL = [
    "stat",
    "stats",
    "level",
    "LEVEL",
    "Max level",
    "max level",
    "experience",
    "EXP",
    "damage formula",
    "attack power",
    "HP",
    "ATK",
    "DEF",
    "transcend",
    "Transcend",
    "upgrade",
    "grade",
]
L.append("### balance vocabulary co-occurring with a sister-title mention")
for w in BAL:
    for fn in files:
        t = io.open(D + fn, encoding="utf-8", errors="replace").read()
        for m in re.finditer(re.escape(w), t):
            s = max(0, m.start() - 260)
            e = min(len(t), m.end() + 260)
            seg = re.sub(r"<[^>]+>", " ", t[s:e])
            seg = re.sub(r"\s+", " ", seg)
            if "BTB" in seg or "\ube44\uc698\ub4dc" in seg or "\ud558\uc5b8\uc11c" in seg:
                L.append("  [%s] %r" % (fn, w))
                L.append("      ...%s..." % seg)
                L.append("")

# ---- 3. Any BTB-specific game-mechanic claims -------------------------
L.append("### level / stat claims near the sister titles")
for m in re.finditer(r"[^\n]{0,160}(?:BTB|\ube44\uc698\ub4dc|\ud558\uc5b8\uc11c)[^\n]{0,160}", main):
    s = m.group(0)
    if re.search(r"\uB9C8\ub7A9|\uC218\uce58|\uD48D\uBC30|\uB2E8\uACC4", s):
        L.append("   %s" % s.strip()[:400])
        L.append("")

out = "\n".join(L)
io.open(OUT, "w", encoding="utf-8", newline="\n").write(out)
print(out[:6000])