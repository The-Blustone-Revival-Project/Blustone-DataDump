# -*- coding: utf-8 -*-
"""Which namu hunter LIST (Offense / Defense / Bomber / Support) is each
shared-cast character filed under?

The role is read from the document's own structure: the TOC lists four
sub-pages in order, and the body has one <table> per role under anchors
s-2.1 .. s-2.4. Korean role names are percent-encoded in the source, so we
slice them out rather than typing Hangul (guard rule 13).
"""
import io
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

D = "analysis/research/base-stats-visual-hunt/_tools/_namu_raw/"
OUT = "analysis/research/base-stats-visual-hunt/_tools/btb_lane/role_lists.txt"

t = io.open(D + "ctrl-file-control.utf8.txt", encoding="utf-8", errors="replace").read()

L = []

# Role slugs, in TOC order, sliced from the hrefs.
roles = []
for m in re.finditer(r"/%EB%B8%94%EB%A3%A8%EC%8A%A4%ED%86%A4/%ED%97%8C%ED%84%B0/([^'%#]+)#", t):
    s = m.group(1)
    if s not in roles:
        roles.append(s)
L.append("role slugs from TOC (in document order): %s" % roles)
L.append("")

# Section anchors for the four role tables.
anchors = []
for num in ["s-2.1", "s-2.2", "s-2.3", "s-2.4"]:
    m = re.search(r"<a id='%s' href='#toc'>" % re.escape(num), t)
    if m:
        anchors.append((num, m.start()))
L.append("section anchors found: %s" % [a[0] for a in anchors])
L.append("")

rowre = re.compile(
    r"<td>\s*\u2606[^<]*</td>\s*<td>\s*([\uAC00-\uD7A3]+)\s*</td>\s*<td>\s*([^<]+?)\s*</td>",
    re.S,
)

bounds = [a[1] for a in anchors] + [len(t)]
for i, (num, pos) in enumerate(anchors):
    seg = t[pos : bounds[i + 1]]
    role = roles[i] if i < len(roles) else "?"
    rows = rowre.findall(seg)
    L.append("### section %s   role slug=%s   rows=%d" % (num, role, len(rows)))
    for attr, name in rows:
        nm = re.sub(r"<[^>]+>", "", name).strip()
        L.append("    %-8s %s" % (attr, nm))
    L.append("")

out = "\n".join(L)
io.open(OUT, "w", encoding="utf-8", newline="\n").write(out)
print(out)