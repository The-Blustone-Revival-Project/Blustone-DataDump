# -*- coding: utf-8 -*-
import csv, io, os, sys
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
except Exception:
    pass
HERE = os.path.dirname(os.path.abspath(__file__))
BS = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
p = os.path.join(BS, "analysis", "catalogue", "data", "card-catalogue.tsv")
rows = list(csv.DictReader(io.open(p, encoding="utf-8", newline=""),
                          delimiter="\t", quotechar='"'))
print("catalogue rows: %d" % len(rows))
aw = [r for r in rows if r["card_id"].endswith("_1")]
print("awakened (_1) rows: %d" % len(aw))
for r in aw:
    print("  %-8s %-26s rarity=%-3s owner=%-6s inferred=%-4s wiki=%r"
          % (r["card_id"], r["name"], r["rarity"], r["owner_card_id"],
             r["inferred_owner"], r["wiki"]))
print()
print("base rows for those owners:")
by = {r["card_id"]: r for r in rows}
for r in aw:
    b = by.get(r["owner_card_id"])
    if b:
        print("  %-8s %-26s rarity=%-3s role=%-9s elem=%-9s"
              % (b["card_id"], b["name"], b["rarity"], b["role"], b["element"]))