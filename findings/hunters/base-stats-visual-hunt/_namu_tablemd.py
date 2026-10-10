# -*- coding: utf-8 -*-
"""Emit every parsed table of a page as markdown, verbatim rows."""
import io
import json
import os
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _namu_tables import TableParser, cell_repr  # noqa: E402

src = sys.argv[1]
dst = sys.argv[2]
html = io.open(src, encoding="utf-8").read()
p = TableParser()
p.feed(html)

out = []
for t in p.tables:
    rows = [[cell_repr(c).strip() for c in r] for r in t["grid"]]
    width = t["grid_width"]
    nonempty = [r for r in rows if any(x for x in r)]
    out.append("#### Table %d — %d rows x %d cols (%d non-empty rows)"
               % (t["index"], t["row_count"], width, len(nonempty)))
    out.append("")
    if not nonempty:
        out.append("_no data rows (page furniture)_")
        out.append("")
        continue
    for r_i, r in enumerate(rows):
        if not any(r):
            continue
        out.append("- r%02d | %s" % (r_i, " | ".join(r)))
    out.append("")

io.open(dst, "w", encoding="utf-8", newline="\n").write("\n".join(out))
print("tables=%d md_chars=%d -> %s" % (len(p.tables),
                                       sum(len(x) for x in out), dst))
