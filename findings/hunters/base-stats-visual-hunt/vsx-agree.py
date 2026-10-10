# -*- coding: utf-8 -*-
"""vsx-agree: field-by-field comparison of the retrieved wiki stat tables
against archived-hunter-database-2019.tsv, on the same basis as the prior
lane (same label->JP-column mapping, same unit convention)."""
import csv, io, json, os, re, sys
from collections import OrderedDict

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "_wf1_cache")

# wiki label -> JP column
MAP = OrderedDict([
    ("Life", "hp"), ("Attack", "atk"), ("Defense", "def"),
    ("Attack Speed", "speed"),
    ("Critical Damage Chance", "crit"), ("Critical Damage", "crit_damage"),
    ("Armor Penetration", "penetration"), ("Block Chance", "block"),
    ("Block Resistance", "block_damage_reduction"),
    ("Damage Reduction Block", "block_damage_reduction"),
    ("Strengthen Elemental Attributes", "element_enhance"),
    ("Elemental Attack Resistance", "element_resistance"),
    ("Life Regeneration", "hp_regen"),
])


def norm(v):
    """Strip a trailing percent sign and whitespace.  The prior lane established
    that the wiki writes '14%' where the JP table writes the unitless '14'."""
    v = (v or "").strip().replace("\u00a0", "")
    v = v.rstrip("%").strip()
    return v


def num(v):
    v = norm(v)
    try:
        f = float(v)
        return int(f) if f == int(f) else f
    except Exception:
        return None


def main():
    jp = {}
    with io.open(os.path.join(HERE, "archived-hunter-database-2019.tsv"),
                 encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f, delimiter="\t", quotechar='"'):
            jp.setdefault(r["catalog_id"], r)

    with io.open(os.path.join(CACHE, "stats-tables.json"), encoding="utf-8") as f:
        st = json.load(f)

    rows, cmp_total, cmp_equal, diffs = [], 0, 0, []
    for page, v in st.items():
        cat = v["catalog"]
        for rev in v["revisions"]:
            for t in rev["tables"]:
                if rev is not v["revisions"][0]:
                    continue  # one comparison per page (revisions are identical)
                jr = jp.get(cat)
                present, absent = [], []
                for lab, val in t["labels"].items():
                    if lab in ("Character Attributes",
                               "Stat Details: Attack",
                               "Stat Details: Defense"):
                        continue
                    col = MAP.get(lab)
                    if not col:
                        continue
                    w = num(val)
                    j = num(jr.get(col)) if jr else None
                    present.append((lab, col, val.strip(), jr.get(col, "?").strip()
                                    if jr else "?"))
                    if w is not None and j is not None:
                        cmp_total += 1
                        if w == j:
                            cmp_equal += 1
                        else:
                            diffs.append((page, cat, lab, col, val.strip(),
                                          jr.get(col).strip(), w, j))
                # canonical fields absent from this table
                miss = [f for f in ("Life", "Attack", "Defense", "Attack Speed")
                        if f not in t["labels"]]
                rows.append({"page": page, "catalog": cat, "caption": t["caption"],
                             "labels_present": sorted(t["labels"]),
                             "core_absent": miss, "fields": present})

    with io.open(os.path.join(CACHE, "agreement.json"), "w", encoding="utf-8") as f:
        json.dump({"comparisons": cmp_total, "equal": cmp_equal,
                   "differences": diffs, "rows": rows},
                  f, ensure_ascii=False, indent=1)

    print("hero pages compared: %d" % len(rows))
    print("field comparisons  : %d ; equal %d ; DIFFERENT %d"
          % (cmp_total, cmp_equal, cmp_total - cmp_equal))
    print()
    print("--- caption census ---")
    for r in rows:
        print("  %-10s cat=%s caption=%-24r core_absent=%s"
              % (r["page"], r["catalog"], r["caption"], r["core_absent"]))
    print()
    print("--- every DIFFERENCE (with ratio where both numeric) ---")
    for page, cat, lab, col, wv, jv, w, j in diffs:
        r = ("%.4f" % (w / j)) if (j and isinstance(w, (int, float))
                                   and isinstance(j, (int, float)) and j) else "n/a"
        print("  %-8s %-4s %-24s wiki=%-8s jp=%-8s ratio=%s" % (page, cat, col, wv, jv, r))
    print()
    print("--- per-page field readings (verbatim wiki text | JP value) ---")
    for r in rows:
        print("### %s (cat %s) caption=%r" % (r["page"], r["catalog"], r["caption"]))
        for lab, col, wv, jv in r["fields"]:
            same = "" if num(wv) == num(jv) else "   <-- DIFF"
            print("    %-30s %-8s | jp %s%s" % (lab, wv, jv, same))
        print()


if __name__ == "__main__":
    main()