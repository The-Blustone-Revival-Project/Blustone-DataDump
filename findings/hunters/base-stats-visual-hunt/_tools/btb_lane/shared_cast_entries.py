# -*- coding: utf-8 -*-
"""Read the per-hero entries for the shared cast from the namu control doc.

Section structure is by STAR TIER (1*..4*), each hero an <h4>. We locate the
hero headings and print the prose that follows, which is where role and
mechanics are described in the community's own words.
"""
import io
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

D = "analysis/research/base-stats-visual-hunt/_tools/_namu_raw/"
OUT = "analysis/research/base-stats-visual-hunt/_tools/btb_lane/shared_cast_entries.txt"

t = io.open(D + "ctrl-file-control.utf8.txt", encoding="utf-8", errors="replace").read()

# Hero headings: <h4><a id='s-2.x.y' href='#toc'>n.m.</a> NAME</h4>
heads = list(
    re.finditer(r"<h4><a id='(s-[0-9.]+)' href='#toc'>[0-9.]+</a>(.*?)</h4>", t, re.S)
)
print("hero headings found:", len(heads))

L = []
for i, h in enumerate(heads):
    name = re.sub(r"<[^>]+>", "", h.group(2)).strip()
    end = heads[i + 1].start() if i + 1 < len(heads) else len(t)
    body = t[h.end() : end]
    body_txt = re.sub(r"<[^>]+>", " ", body)
    body_txt = (
        body_txt.replace("&#91;", "[").replace("&#93;", "]").replace("&amp;", "&").replace("&#39;", "'")
    )
    body_txt = re.sub(r"\s+", " ", body_txt).strip()
    L.append("=" * 95)
    L.append("[%s]  %s" % (h.group(1), name))
    L.append("  %s" % body_txt[:2600])
    L.append("")

out = "\n".join(L)
io.open(OUT, "w", encoding="utf-8", newline="\n").write(out)
print("wrote", OUT, len(out), "chars")

# Print just the headings so we can see the roster
print()
for h in heads:
    print("  ", h.group(1), re.sub(r"<[^>]+>", "", h.group(2)).strip())