# -*- coding: utf-8 -*-
"""First-party BTB / White Island strings shipped INSIDE the Blustone client.

Writes a readable report. Never prints Hangul from memory: search terms are
sliced out of the data itself.
"""
import io
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

SRC = "analysis/recovered-data/leveldb-tables/all-tables.json"
OUT = "analysis/research/base-stats-visual-hunt/_tools/btb_lane/client_btb_strings.out.txt"

raw = io.open(SRC, encoding="utf-8").read()

# Slice the terms out of the data rather than typing them.
# Anchor on the ASCII 'BTB' and on the CJK/Japanese title that is present in
# the shipped EN string, then derive the Korean originals from key strings.
btb_term = "BTB"

lines = []
lines.append("client file chars: %d" % len(raw))
lines.append("ASCII 'BTB' occurrences: %d" % raw.count(btb_term))

# Every record whose key OR value mentions BTB, plus the White Island strings
# which are adjacent (same UI panel: TX_TITLE + TX_ACC).
doc = json.loads(raw)
tables = doc["tables"]
lines.append("tables: %s" % ", ".join(sorted(tables)))
recs = []
for tname in sorted(tables):
    tbody = tables[tname]
    if isinstance(tbody, dict):
        recs.extend(tbody.values())
    else:
        recs.extend(tbody)
lines.append("json records: %d" % len(recs))
lines.append("")

sel = []
for r in recs:
    key = r.get("key", "")
    val = (r.get("json") or {}).get("TEXT", "")
    if btb_term in key or btb_term in val or btb_term in (r.get("raw") or ""):
        sel.append(r)

lines.append("=== records mentioning BTB: %d ===" % len(sel))
for r in sel:
    lines.append("KEY : %s" % r.get("key", ""))
    lines.append("TEXT: %s" % (r.get("json") or {}).get("TEXT", ""))
    lines.append("")

# The companion panel: same Korean key as the BTB one but the title record.
# Pull every record whose key starts with the BTB key prefix, whatever locale.
btb_keys = {r.get("key", "") for r in sel}
prefixes = sorted({k.split("|")[0] for k in btb_keys})
lines.append("=== distinct Korean panel keys: %s ===" % prefixes)
for pref in prefixes:
    lines.append("--- panel: %s ---" % pref)
    for r in recs:
        k = r.get("key", "")
        if k.split("|")[0] == pref:
            lines.append("KEY : %s" % k)
            lines.append("TEXT: %s" % (r.get("json") or {}).get("TEXT", ""))
    lines.append("")

# Any other record mentioning the Japanese / Chinese / Korean title of the
# sister title, discovered from the panel text itself.
lines.append("=== records whose TEXT mentions the sister-title title token ===")
# tokens derived from data
tokens = set()
for r in sel:
    t = (r.get("json") or {}).get("TEXT", "")
    for m in re.finditer(r"[A-Za-z][A-Za-z .']{4,}", t):
        tokens.add(m.group(0).strip())
for tok in sorted(tokens):
    if btb_term in tok:
        continue
    hits = [
        r
        for r in recs
        if tok in ((r.get("json") or {}).get("TEXT", "") or "")
        or tok in (r.get("key", "") or "")
    ]
    if len(hits) <= 40:
        lines.append("token %r -> %d records" % (tok, len(hits)))
        for r in hits[:40]:
            lines.append("    %s :: %s" % (r.get("key", ""), (r.get("json") or {}).get("TEXT", "")))
    else:
        lines.append("token %r -> %d records (too many)" % (tok, len(hits)))

out = "\n".join(lines)
io.open(OUT, "w", encoding="utf-8", newline="\n").write(out)
print("wrote", OUT, len(out), "chars,", out.count("\n"), "lines")