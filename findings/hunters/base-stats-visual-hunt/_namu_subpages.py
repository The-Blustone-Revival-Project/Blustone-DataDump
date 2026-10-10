# -*- coding: utf-8 -*-
"""Batch-render namu per-role sub-pages with headless Edge and emit
text + table digests, plus the page's 최근 수정 시각 (last modified)."""
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _namu_headless import render  # noqa: E402
from _namu_tables import TableParser, cell_repr  # noqa: E402
from _namu_text import main as text_main  # noqa: E402  (not called)

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

BASE = "https://namu.wiki/w/%EB%B8%94%EB%A3%A8%EC%8A%A4%ED%86%A4/%ED%97%8C%ED%84%B0"
# percent-encodings generated with urllib.parse.quote, never hand-typed
PAGES = [
    ("offense", BASE + "/%EA%B3%B5%EA%B2%A9%EC%88%98"),
    ("defense", BASE + "/%EC%88%98%EB%B9%84%EC%88%98"),
    ("bomber", BASE + "/%ED%8F%AD%EA%B2%A9%EC%88%98"),
    ("support", BASE + "/%EB%8F%84%EC%9A%B0%EB%AF%B8"),
]
OUT = os.environ.get("TEMP", ".")


def lastmod(html):
    m = re.search(r"최근\s*수정\s*시각\s*:?\s*([0-9]{4}-[0-9]{2}-[0-9]{2}[^<]{0,20})", html)
    if m:
        return m.group(1).strip()
    m = re.search(r"([0-9]{4}-[0-9]{2}-[0-9]{2}\s+[0-9]{2}:[0-9]{2}:[0-9]{2})", html)
    return m.group(1).strip() if m else "NOT FOUND"


for name, url in PAGES:
    hp = os.path.join(OUT, "namu_%s.html" % name)
    if os.path.exists(hp):
        html = io.open(hp, encoding="utf-8").read()
    else:
        html, err, rc, prof = render(url, budget_ms=35000)
        io.open(hp, "w", encoding="utf-8", newline="\n").write(html)
    p = TableParser()
    p.feed(html)
    print("=" * 90)
    print("%-8s bytes=%-8d tables=%-3d lastmod=%s"
          % (name, len(html), len(p.tables), lastmod(html)))
    for t in p.tables:
        nonempty = [r for r in t["grid"] if any(cell_repr(c).strip() for c in r)]
        print("   T%-2d rows=%-4d width=%-3d nonempty=%d"
              % (t["index"], t["row_count"], t["grid_width"], len(nonempty)))
        for r in nonempty[:4]:
            print("        " + " || ".join(cell_repr(c).strip()[:60] for c in r)[:260])
