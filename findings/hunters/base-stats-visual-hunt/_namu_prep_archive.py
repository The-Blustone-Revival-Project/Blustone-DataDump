# -*- coding: utf-8 -*-
"""Read-only prep for the namu 헌터 cross-check. Touches nothing outside the
TSV it reads. Emits a compact JSON of the 2019 JP archive rows so the namu
element/grade comparison can be made mechanically rather than by eye."""
import csv, io, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
TSV = os.path.join(HERE, "archived-hunter-database-2019.tsv")

rows = []
with io.open(TSV, encoding="utf-8", newline="") as fh:
    for r in csv.DictReader(fh, delimiter="\t", quoting=csv.QUOTE_ALL):
        rows.append(r)

out = {
    "row_count": len(rows),
    "columns": list(rows[0].keys()) if rows else [],
    "ids": sorted({r["catalog_id"] for r in rows if r["catalog_id"]}),
    "elements": sorted({r["element_ja"] for r in rows if r["element_ja"]}),
    "roles": sorted({r["role_ja"] for r in rows if r["role_ja"]}),
    "rarities": sorted({r["rarity_on_draw"] for r in rows if r["rarity_on_draw"]}),
    "numeric_ok": sum(1 for r in rows if r["fetch_status"] == "ok"),
}

# Per-hero compact records for cross-check.
heroes = []
for r in rows:
    heroes.append({
        "id": r["catalog_id"],
        "name_ja": r["listed_name"],
        "role_ja": r["role_ja"],
        "element_ja": r["element_ja"],
        "rarity": r["rarity_on_draw"],
        "hp": r["hp"], "atk": r["atk"], "def": r["def"], "spd": r["speed"],
        "power": r["combat_power"],
        "status": r["fetch_status"],
    })
out["heroes"] = heroes

OUT = os.path.join(os.environ.get("TEMP", "."), "namu_archive.json")
with io.open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    fh.write(json.dumps(out, ensure_ascii=False, indent=1))
print("rows=%d numeric_ok=%d ids=%d" % (out["row_count"], out["numeric_ok"], len(out["ids"])))
print("elements =", [e.encode("unicode_escape").decode() for e in out["elements"]])
print("roles =", [e.encode("unicode_escape").decode() for e in out["roles"]])
print("rarities =", out["rarities"])
print("wrote", OUT)
