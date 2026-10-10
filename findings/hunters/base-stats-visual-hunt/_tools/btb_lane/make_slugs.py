# -*- coding: utf-8 -*-
"""Derive percent-encoded namu.wiki slugs for the sister titles FROM THE DATA.

Guard rule 13: never hand-write Unicode for a search term. The Korean titles
are sliced out of a file that already contains them, then encoded here.
"""
import io
import re
import sys
from urllib.parse import quote

sys.stdout.reconfigure(encoding="utf-8")

SRC = "analysis/research/base-stats-visual-hunt/_tools/_namu_raw/ctrl-d-main.text.txt"
txt = io.open(SRC, encoding="utf-8").read()

# Harvest candidate Korean titles by finding the ASCII anchor 'BTB' context and
# the ASCII 'White Island' equivalent in the Korean source line.
seen = set()

# The Blustone article names BTB in Korean and in English.
for m in re.finditer(r"[\uAC00-\uD7A3][\uAC00-\uD7A3 ]{2,40}", txt):
    s = m.group(0).strip()
    if s and s not in seen:
        seen.add(s)

# We only need titles that look like a game name. Print the most plausible:
# those containing the BTB marker or that appear with '비주얼샤워'.
cands = sorted({s for s in seen if len(s) >= 3})
print("candidate Korean runs: %d" % len(cands))
for s in cands:
    if "BTB" in s or "\ubc94\uc6b4\uc9c0" in s or "\uc544\ub784\ub7ec\ub4dc" in s:
        print("TITLE-LIKE:", s)
        print("   slug:", quote(s))
print()

# Also slice directly out of the client table keys, which are authoritative.
KEYS = "analysis/recovered-data/leveldb-tables/all-tables.json"
import json

doc = json.loads(io.open(KEYS, encoding="utf-8").read())
kterms = set()
for tname, tbody in doc["tables"].items():
    items = tbody.values() if isinstance(tbody, dict) else tbody
    for r in items:
        if isinstance(r, dict):
            k = r.get("key", "") or ""
            j = r.get("json")
            t = (j.get("TEXT", "") if isinstance(j, dict) else "") or ""
            for blob in (k, t):
                if "BTB" in blob or "Beyond the Bounds" in blob:
                    for m in re.finditer(r"[\uAC00-\uD7A3][\uAC00-\uD7A3 ]{2,40}", blob):
                        kterms.add(m.group(0).strip())
print("Korean titles taken from CLIENT tables (authoritative):")
for s in sorted(kterms):
    if len(s) >= 3:
        print("  %s -> %s" % (s, quote(s)))