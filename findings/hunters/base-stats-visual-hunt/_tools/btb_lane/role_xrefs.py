# -*- coding: utf-8 -*-
"""Locate the per-hero entries in the namu hunter control document and read
the ROLE each one is filed under, via the cross-reference slugs in the text.

The main document sections are star tiers (1*..4*). Role membership is only
expressed by links to the four role sub-pages
  블루스톤/헌터/공격수  (Offense)
  블루스톤/헌터/수비수  (Defense)
  블루스톤/헌터/폭격수  (BomBomber)
  블루스톤/헌터/도우미  (Support)
We therefore search the whole document for cross-links to those four slugs and
print the surrounding sentence, which is the role statement.
"""
import io
import re
import sys
from urllib.parse import unquote

sys.stdout.reconfigure(encoding="utf-8")

D = "analysis/research/base-stats-visual-hunt/_tools/_namu_raw/"
OUT = "analysis/research/base-stats-visual-hunt/_tools/btb_lane/role_xrefs.txt"

t = io.open(D + "ctrl-file-control.utf8.txt", encoding="utf-8", errors="replace").read()

L = []

# Discover the four role slugs from the document itself.
slugs = {}
for m in re.finditer(r"href='/w/([^']*/%ED%97%8C%ED%84%B0/[^'#]+)#", t):
    s = unquote(m.group(1))
    if s.count("/") == 2 and "%" not in s:
        slugs[s] = s
L.append("discovered role sub-page slugs: %s" % sorted(slugs))
L.append("")

# Map each slug to every occurrence with context.
for slug in sorted(slugs):
    enc = re.escape(slug)
    L.append("=" * 90)
    L.append("ROLE SLUG: %s" % slug)
    hits = list(re.finditer(r"title='[^']*'>([^<]{1,40})</a>", t))
    # find all anchors whose href contains the slug
    for m in re.finditer(r"href='/w/%s#[^']*'[^>]*>([^<]{1,60})</a>" % enc, t):
        nm = m.group(1)
        L.append("   link text: %s" % nm)
    L.append("")

out = "\n".join(L)
io.open(OUT, "w", encoding="utf-8", newline="\n").write(out)
print(out[:4000])