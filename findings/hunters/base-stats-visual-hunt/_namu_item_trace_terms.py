"""Probe 5: does the namu ITEM page organise traces as 5.1/5.2/5.3/5.4, and
does the literal item name '3성 헌터 흔적' exist anywhere in the recovered
namu dumps?  Both are claims in the task brief; neither may be taken on trust.

Read-only, writes UTF-8/LF.
"""
import glob
import os
import re
import sys

D = r"analysis/research/base-stats-visual-hunt/_tools/_namu_raw"
out = []
out.append("Positive control first: a term known to exist in the hunter page.")
TERMS = [
    "3성 헌터 흔적",
    "헌터 흔적",
    "흔적",
    "5.1",
    "미라주",
    "확정 섭외",
]
files = sorted(glob.glob(os.path.join(D, "*.utf8.txt")))
out.append("scanned %d namu dump files" % len(files))

for term in TERMS:
    out.append("")
    out.append("=" * 74)
    out.append("TERM %r" % term)
    out.append("=" * 74)
    total = 0
    for f in files:
        try:
            t = open(f, encoding="utf-8").read()
        except Exception as e:
            out.append("  [unreadable %s: %s]" % (os.path.basename(f), e))
            continue
        n = t.count(term)
        if n:
            total += n
            out.append("  %-34s %d hit(s)" % (os.path.basename(f), n))
    out.append("  TOTAL: %d" % total)

# Now dump the trace section of the ITEM page, which is where 5.1..5.4 would live
out.append("")
out.append("#" * 78)
out.append("# ITEM PAGE 흔적 context (it-d-아이템)")
out.append("#" * 78)
p = os.path.join(D, "it-d-아이템.utf8.txt")
t = open(p, encoding="utf-8").read()
out.append("chars %d  U+FFFD %d" % (len(t), t.count("\ufffd")))
for m in re.finditer("흔적", t):
    a = max(0, m.start() - 400)
    b = min(len(t), m.end() + 400)
    out.append("\n  ...%s..." % t[a:b].replace("\n", " / "))

# explicit hunt for a "5.x" heading ladder near 흔적
out.append("")
out.append("#" * 78)
out.append("# any 5.N heading ladder in the ITEM page")
out.append("#" * 78)
for m in re.finditer(r"5\.\d", t):
    a = max(0, m.start() - 120)
    b = min(len(t), m.end() + 120)
    out.append("  ...%s..." % t[a:b].replace("\n", " / "))

open(r"analysis/research/base-stats-visual-hunt/_namu_item_trace_terms.txt",
     "w", encoding="utf-8", newline="\n").write("\n".join(out))
sys.stdout.write("ok\n")