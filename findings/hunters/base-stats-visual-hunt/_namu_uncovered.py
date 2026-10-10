# -*- coding: utf-8 -*-
"""How much of the 51-ID uncovered-2019 roster does namu actually cover?"""
import csv
import io
import json
import os
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.environ.get("TEMP", ".")
roster = json.load(io.open(os.path.join(T, "namu_roster.json"), encoding="utf-8"))
unc = list(csv.DictReader(
    io.open(os.path.join(HERE, "uncovered-archive-roster-2019.tsv"),
            encoding="utf-8", newline=""),
    delimiter="\t", quoting=csv.QUOTE_ALL))

by_id = {h["catalog_id"]: h for h in roster if h["catalog_id"]}
print("uncovered roster rows: %d   distinct ids: %d"
      % (len(unc), len({r['catalog_id'] for r in unc})))

hit, miss = [], []
for r in unc:
    cid = r["catalog_id"]
    h = by_id.get(cid)
    if h:
        hit.append((cid, r["name"] or r["title"], h["name_ko_clean"],
                    h["elem_en"], h["grade_stars"]))
    else:
        miss.append((cid, r["name"] or r["title"]))

print("\nCOVERED by namu (%d):" % len(hit))
for cid, en, ko, el, g in hit:
    print("  %-7s en=%-24s ko=%-22s %-9s %s*" % (cid, en, ko, el, g))
print("\nNOT covered by namu (%d):" % len(miss))
for cid, en in miss:
    print("  %-7s %s" % (cid, en))

# namu ids with no archive row at all
noarch = [h for h in roster if h["catalog_id"] and not h["archive_present"]]
print("\nnamu heroes with an id but NO 2019 archive row (%d):" % len(noarch))
for h in noarch:
    print("  %-6s %-22s %-10s %s*" % (h["catalog_id"], h["name_ko_clean"],
                                      h["elem_en"], h["grade_stars"]))
