# -*- coding: utf-8 -*-
"""Full local cross-title scan of the SHIPPED Blustone client tables.

Finds every record mentioning the sister titles, in every locale, without
typing any non-ASCII search term from memory (guard rule 13): the Latin tokens
'BTB' and 'Beyond the Bounds' are sliced out of the data first, then the
Korean / Japanese / Chinese titles they reveal are used as further keys.
"""
import io
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

SRC = "analysis/recovered-data/leveldb-tables/all-tables.json"
OUT = "analysis/research/base-stats-visual-hunt/_tools/btb_lane/client_cross_title.out.txt"

doc = json.loads(io.open(SRC, encoding="utf-8").read())
tables = doc["tables"]

recs = []
for tname in sorted(tables):
    tbody = tables[tname]
    items = tbody.values() if isinstance(tbody, dict) else tbody
    for r in items:
        if isinstance(r, dict):
            r["__table"] = tname
            recs.append(r)

L = []


def text_of(r):
    j = r.get("json")
    if isinstance(j, dict):
        return j.get("TEXT", "") or ""
    if isinstance(j, str):
        return j
    return ""


def scan(term):
    return [
        r
        for r in recs
        if term in (r.get("key", "") or "") or term in text_of(r) or term in (r.get("raw") or "")
    ]


# ---- Pass 1: Latin anchors that came from the data itself -------------------
latin = ["BTB", "Beyond the Bounds", "White Island"]
titles = set()
for term in latin:
    hits = scan(term)
    L.append("=== term %r -> %d records ===" % (term, len(hits)))
    for r in hits:
        L.append("  [%s] %s" % (r.get("__table"), r.get("key", "")))
        L.append("      %s" % text_of(r))
    L.append("")
    # harvest any non-ASCII title token that appears with the anchor
    for r in hits:
        t = text_of(r)
        for m in re.finditer(r"[\uAC00-\uD7A3]{2,}", t):
            titles.add(m.group(0))
        for m in re.finditer(r"[\u3040-\u30FF\u4E00-\u9FFF]{2,}", t):
            titles.add(m.group(0))

# ---- Pass 2: the Korean panel keys that are siblings of the BTB anchors ----
# Group by the Korean key stem so a whole panel (TX_TITLE/TX_ACC x 5 locales)
# is reported together.
stems = set()
for term in latin:
    for r in scan(term):
        k = r.get("key", "") or ""
        if k:
            stems.add(k.split("|")[0])

L.append("=== panel stems (Korean key before first |) ===")
for s in sorted(stems):
    L.append("  %s" % s)
L.append("")

for s in sorted(stems):
    members = [
        r for r in recs if (r.get("key", "") or "").split("|")[0] == s
    ]
    L.append("--- panel %r : %d locale rows ---" % (s, len(members)))
    for r in sorted(members, key=lambda x: x.get("key", "")):
        L.append("  [%s] %s" % (r.get("__table"), r.get("key", "")))
        L.append("      %s" % text_of(r))
    L.append("")

# ---- Pass 3: broad sweep for any OTHER sister-title-ish token ---------------
# Harvest every CJK/Hangul run of length>=2 that appears next to a Latin capital
# run, then report which of those are rare enough to be titles or names.
rare = {}
for r in recs:
    t = text_of(r)
    if not t:
        continue
    if not re.search(r"[A-Za-z]{3,}", t):
        continue
    for m in re.finditer(r"[\uAC00-\uD7A3\u3040-\u30FF\u4E00-\u9FFF]{2,}", t):
        tok = m.group(0)
        rare[tok] = rare.get(tok, 0) + 1

# Report tokens that co-occur with any sister-title anchor.
anchors = set()
for term in latin:
    for r in scan(term):
        for m in re.finditer(r"[\uAC00-\uD7A3\u3040-\u30FF\u4E00-\u9FFF]{2,}", text_of(r)):
            anchors.add(m.group(0))
L.append("=== CJK/Hangul tokens co-occurring with a sister-title anchor ===")
for a in sorted(anchors):
    L.append("  %s  (appears in %d records overall)" % (a, rare.get(a, 0)))
L.append("")

out = "\n".join(L)
io.open(OUT, "w", encoding="utf-8", newline="\n").write(out)
print("wrote", OUT, len(out), "chars,", out.count("\n"), "lines")