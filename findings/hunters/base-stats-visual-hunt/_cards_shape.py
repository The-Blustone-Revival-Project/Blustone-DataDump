"""Probe 4: shape of cards.json + grade/rarity fields available.

Read-only, print to a UTF-8 file (GUARD Rule 2: never trust the console).
"""
import json
import sys

d = json.load(open(r"analysis/catalogue/data/cards.json", encoding="utf-8"))
out = []
out.append("cards: %d" % len(d))
out.append("first record keys: %s" % sorted(d[0].keys()))
out.append("")
for r in d[:6]:
    out.append(json.dumps(r, ensure_ascii=False)[:400])
out.append("")
# what key holds grade/rarity, and its distribution
for k in ("rarity", "grade", "rank", "star", "stars", "birth_grade", "rarity_on_draw"):
    vals = [r.get(k) for r in d]
    if any(v is not None for v in vals):
        from collections import Counter
        out.append("KEY %-14s present=%d dist=%s" % (k, sum(v is not None for v in vals), Counter(vals).most_common()))
out.append("")
out.append("names of the 44 forum heroes vs ids:")
NAMES = ["Acerola", "Akasha", "Athena", "Balian", "Bear", "Bibi", "Bruce Bang", "Captain",
         "Denali", "Diana", "Edward", "Gerard", "Gullveig", "Hecate", "Hermes", "Joy", "Kain",
         "Karl Steiner", "Lantern", "Lapis", "Levi", "Locke", "Metis", "Mowgli", "Natalia",
         "Nene", "Octavia", "Papillon", "Patrone", "Rebecca", "Riko", "Robin", "Scar",
         "Sienna", "Sylvester", "Teddy Bomber", "Tyltyl"]
bym = {}
for r in d:
    nm = (r.get("name") or "").strip()
    bym.setdefault(nm, []).append(r)
for nm in NAMES:
    hit = bym.get(nm, [])
    out.append("  %-14s -> %s" % (nm, [((h.get("base") or {}).get("id"), h.get("rarity"), h.get("element"), h.get("role")) for h in hit]))

open(r"analysis/research/base-stats-visual-hunt/_cards_shape.txt", "w", encoding="utf-8", newline="\n").write("\n".join(out))
sys.stdout.write("ok\n")