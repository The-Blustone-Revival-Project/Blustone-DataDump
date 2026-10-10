# -*- coding: utf-8 -*-
"""vsx-crossref: cross the wiki's 55 distinct catalogue IDs against
  (a) archived-hunter-database-2019.tsv      (62 numeric rows)
  (b) uncovered-archive-roster-2019.tsv      (51 IDs the JP archive never covered)
  (c) analysis/catalogue/data/card-catalogue.tsv
Reports exact membership, not similarity."""
import csv, io, json, os, re, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
BS = os.path.abspath(os.path.join(HERE, "..", "..", ".."))

WIKI = OrderedDict([
    ("Acerola", "030"), ("Akasha", "008"), ("Apollon", "055"), ("Athena", "027"),
    ("Balian", "019"), ("Bear", "036"), ("Beckhen", "051"), ("Bibi", "040"),
    ("Bright", "049"), ("Bruce Bang", "016"), ("Calibur", "053"), ("Captain", "009"),
    ("Crocus", "058"), ("Denali", "013"), ("Diana", "031"), ("Dino", "054"),
    ("Dumble", "048"), ("Edward", "041"), ("Gerard", "005"), ("Gullveig", "039"),
    ("Harley", "046"), ("Hecate", "011"), ("Heidi", "044"), ("Hermes", "023"),
    ("Joy", "035"), ("Juno", "062"), ("Kain", "029"), ("Karl Steiner", "012"),
    ("Lantern", "001"), ("Lapis", "017"), ("Levi", "015"), ("Lily & Lyla", "047"),
    ("Locke", "014"), ("Metis", "007"), ("Mowgli", "002"), ("Natalia", "037"),
    ("Nene", "003"), ("Octavia", "028"), ("Pansy", "057"), ("Papillon", "043"),
    ("Patrone", "033"), ("Rebecca", "021"), ("Riko", "024"), ("Robin", "018"),
    ("Santa Clauster", "042"), ("Scar", "032"), ("Sienna", "020"), ("Sunny", "022"),
    ("Sylvester", "006"), ("Teddy Bomber", "025"), ("Therapy", "050"),
    ("Tyltyl", "004"), ("Vincent", "010"), ("Windblade", "052"), ("Yuri", "045"),
])
# 57 wiki pages -> 55 distinct characters; the two duplicate pairs
DUP_PAGES = {"012": ["Karl", "Karl_Steiner"], "025": ["Teddy Bomber", "TeddyBomber"]}

STATFIELDS = ["hp", "atk", "def", "speed", "crit", "crit_damage", "penetration",
              "block", "block_damage_reduction", "element_enhance",
              "element_resistance", "hp_regen"]


def rd(path):
    with io.open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t", quotechar='"'))


def main():
    jp = rd(os.path.join(HERE, "archived-hunter-database-2019.tsv"))
    unc = rd(os.path.join(HERE, "uncovered-archive-roster-2019.tsv"))
    cat = rd(os.path.join(BS, "analysis", "catalogue", "data", "card-catalogue.tsv"))

    jp_by_id = OrderedDict()
    for r in jp:
        jp_by_id.setdefault(r["catalog_id"], []).append(r)
    unc_ids = [r["catalog_id"] for r in unc]
    unc_base = set(i.split("_")[0] for i in unc_ids)
    cat_by_id = {}
    for r in cat:
        cid = (r.get("card_id") or "").strip()
        if cid:
            cat_by_id.setdefault(cid, r)

    wiki_ids = sorted(set(WIKI.values()))
    print("wiki: 57 pages -> %d distinct catalogue IDs" % len(wiki_ids))

    # (a) wiki vs JP 2019
    in_jp = [i for i in wiki_ids if i in jp_by_id]
    not_in_jp = [i for i in wiki_ids if i not in jp_by_id]
    print("\n[a] wiki IDs present in archived-hunter-database-2019.tsv: %d/%d"
          % (len(in_jp), len(wiki_ids)))
    print("    NOT in JP archive: %s" % (not_in_jp,))

    # numeric coverage of the JP rows for the wiki heroes
    numeric = 0
    placeholder = []
    for i in in_jp:
        row = jp_by_id[i][0]
        if all(str(row[f]).strip() not in ("", "???") for f in ("hp", "atk", "def")):
            numeric += 1
        else:
            placeholder.append(i)
    print("    of those, with numeric hp/atk/def: %d ; placeholder: %s"
          % (numeric, placeholder))

    # (b) wiki vs the 51-ID uncovered roster
    print("\n[b] wiki base IDs vs the %d uncovered-2019 IDs" % len(unc_ids))
    hits = []
    for i in wiki_ids:
        if i in unc_base:
            hits.append(i)
    print("    EXACT base-ID overlap: %s" % (hits,))
    # also: is any wiki character's NAME the uncovered roster's name?
    unc_rows = {r["catalog_id"]: r for r in unc}
    name_hits = []
    for page, cid in WIKI.items():
        for uid, row in unc_rows.items():
            if row["name"].strip() and row["name"].strip().lower() == page.strip().lower():
                name_hits.append((page, cid, uid))
    print("    name-based matches (wiki page == uncovered row name): %s" % (name_hits,))

    # (c) catalogue crosswalk sanity
    print("\n[c] catalogue rows for the %d wiki IDs: %d present"
          % (len(wiki_ids), sum(1 for i in wiki_ids if i in cat_by_id)))
    hdr = cat[0].keys()
    print("    catalogue columns: %s" % (list(hdr),))
    for cid in ["001", "009", "023", "024", "030", "036"]:
        r = cat_by_id.get(cid)
        if r:
            print("      %-4s %s" % (cid, r))

    # AWAKENED-variant relationship: the uncovered roster's `_1` rows are the
    # awakened forms.  Does the wiki's base page imply its awakened row?
    print("\n[c2] uncovered-roster `_1` (awakened) rows whose BASE form has a wiki page")
    base_wiki = {}
    for page, cid in WIKI.items():
        base_wiki.setdefault(cid, page)
    for r in unc:
        uid = r["catalog_id"]
        if not uid.endswith("_1"):
            continue
        b = uid[:-2]
        print("      %-8s %-28s base=%-5s wiki_page=%s"
              % (uid, r["name"] or "(unnamed)", b, base_wiki.get(b, "-- none --")))

    # which catalogue IDs exist at all but are covered by nobody
    all_cat = sorted(cat_by_id.keys())
    jp_ids = set(jp_by_id.keys())
    print("\n[d] catalogue ID space: %d ids; JP-archive covers %d; uncovered-roster lists %d"
          % (len(all_cat), len(jp_ids), len(unc_ids)))
    neither = [i for i in all_cat if i not in jp_ids and i not in unc_base]
    print("    catalogue ids in NEITHER jp nor uncovered list (%d): %s"
          % (len(neither), neither))
    wiki_neither = [i for i in wiki_ids if i in neither]
    print("    ... of which have a wiki page: %s" % (wiki_neither,))

    out = {"wiki_ids": wiki_ids, "in_jp": in_jp, "not_in_jp": not_in_jp,
           "numeric": numeric, "placeholder": placeholder,
           "uncovered_exact": hits, "name_hits": name_hits,
           "catalogue_neither": neither}
    with io.open(os.path.join(HERE, "_wf1_cache", "crossref.json"), "w",
                 encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()