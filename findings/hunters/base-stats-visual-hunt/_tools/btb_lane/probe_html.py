# -*- coding: utf-8 -*-
"""Inspect the actual HTML shape of the role tables so the extractor matches
reality instead of an assumed pattern."""
import io
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

D = "analysis/research/base-stats-visual-hunt/_tools/_namu_raw/"
t = io.open(D + "ctrl-file-control.utf8.txt", encoding="utf-8", errors="replace").read()

# Print raw HTML right after each anchor.
for num in ["s-2.1", "s-2.2", "s-2.3", "s-2.4"]:
    m = re.search(r"<a id='%s' href='#toc'>" % re.escape(num), t)
    if not m:
        continue
    print("=" * 100)
    print(num, "at", m.start())
    print(repr(t[m.start() : m.start() + 1200]))
    print()

# Also: what do the TOC hrefs look like?
print("=" * 100)
print("TOC sample hrefs:")
for m in list(re.finditer(r"href='/w/([^']*)'", t))[:15]:
    print("   ", m.group(1)[:120])