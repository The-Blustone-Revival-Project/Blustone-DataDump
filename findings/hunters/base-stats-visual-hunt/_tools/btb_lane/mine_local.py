# -*- coding: utf-8 -*-
"""Mine the LOCAL namu dumps for every BTB / sister-title passage.

Guard rule 13: every search term is SLICED OUT OF THE DATA, never typed from
memory. We anchor on the ASCII token 'BTB' (which appears literally in the
Korean source) and on the Korean names of the two protagonists as they are
spelled in that same file.
"""
import io
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

D = "analysis/research/base-stats-visual-hunt/_tools/_namu_raw/"
OUT = "analysis/research/base-stats-visual-hunt/_tools/btb_lane/local_btb_mining.txt"

files = [
    "ctrl-d-main.text.txt",
    "ctrl-d-main.utf8.txt",
    "ctrl-d-hunter.text.txt",
    "ctrl-file-control.utf8.txt",
    "ctrl-final.utf8.txt",
]

L = []

# ---- 1. Discover the protagonist names from the data -----------------------
main = io.open(D + "ctrl-d-main.text.txt", encoding="utf-8").read()

# The Korean article writes "<title>(이하 BTB)와" - take the title from there.
m = re.search(r"([\uAC00-\uD7A3][\uAC00-\uD7A3 ]*?)\(?\uc774\ud558 BTB\)", main)
btb_title = m.group(1).strip() if m else None
L.append("BTB Korean title sliced from data: %r" % btb_title)

# Lantern / Nene: harvest every Hangul name that co-occurs with BTB or with
# the hunter table context. We take the set of 2-3 syllable names appearing in
# the same sentence as 'BTB' in any dump.
names = {}
for fn in files:
    try:
        t = io.open(D + fn, encoding="utf-8", errors="replace").read()
    except FileNotFoundError:
        continue
    # sentences containing the ASCII anchor
    for sent in re.split(r"(?<=[\.\?\u2026])\s+|\n", t):
        if "BTB" not in sent and btb_title not in sent:
            continue
        for nm in re.findall(r"[\uAC00-\uD7A3]{2,4}", sent):
            names.setdefault(nm, []).append((fn, sent.strip()[:400]))

L.append("Hangul tokens appearing in a BTB sentence: %d" % len(names))
L.append("")

# ---- 2. Every BTB sentence, grouped by dump -------------------------------
L.append("=" * 100)
L.append("EVERY SENTENCE MENTIONING BTB (grouped by source file)")
L.append("=" * 100)
for fn in files:
    try:
        t = io.open(D + fn, encoding="utf-8", errors="replace").read()
    except FileNotFoundError:
        continue
    sents = []
    for sent in re.split(r"(?<=[\.\?\u2026])\s+|\n", t):
        s = sent.strip()
        if not s:
            continue
        if "BTB" in s or (btb_title and btb_title in s):
            sents.append(s)
    if not sents:
        continue
    L.append("")
    L.append("### %s  -> %d BTB sentences" % (fn, len(sents)))
    for i, s in enumerate(sents):
        L.append("  [%02d] %s" % (i + 1, s[:1200]))
    L.append("")

out = "\n".join(L)
io.open(OUT, "w", encoding="utf-8", newline="\n").write(out)
print("wrote", OUT, len(out), "chars")
print("BTB sentences found:", out.count("  ["))