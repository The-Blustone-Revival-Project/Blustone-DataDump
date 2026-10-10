# -*- coding: utf-8 -*-
"""Extract the exact BTB Korean title by anchoring on the ASCII 'BTB' token
that immediately follows it in the namu source text, then percent-encode."""
import io
import re
import sys
from urllib.parse import quote

sys.stdout.reconfigure(encoding="utf-8")

SRC = "analysis/research/base-stats-visual-hunt/_tools/_namu_raw/ctrl-d-main.text.txt"
txt = io.open(SRC, encoding="utf-8").read()

# The Korean article writes: <title>(이하 BTB)와
for m in re.finditer(r"([\uAC00-\uD7A3][\uAC00-\uD7A3 ]*?)\(?\uc774\ud558 BTB\)", txt):
    print("anchored title:", repr(m.group(1)))
    print("   slug:", quote(m.group(1).strip()))
    print()

for m in re.finditer(r"([\uAC00-\uD7A3][\uAC00-\uD7A3 ]*?)BTB", txt):
    cand = m.group(1).strip()
    if cand:
        print("loose before BTB:", repr(cand[-30:]), "->", quote(cand[-30:].strip()))
print()
# white island
for m in re.finditer(r"([\uAC00-\uD7A3]{2,6})\uc2dc\uc874 2", txt):
    print("season2 title:", repr(m.group(1)), "->", quote(m.group(1)))