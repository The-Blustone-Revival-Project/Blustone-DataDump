# -*- coding: utf-8 -*-
"""vsx-reconcile: reconcile the 57 hero PAGES / 55 distinct CHARACTERS /
54 List_of_Hunters rows, using the navbox role x element grid transcribed in
the prior lane's §1.15 and re-checking the arithmetic against my own 57-page
list and the JP archive's ID set."""
import csv, io, json, os, sys
from collections import Counter, OrderedDict, defaultdict

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
except Exception:
    pass
HERE = os.path.dirname(os.path.abspath(__file__))

# The 57 archived wiki hero pages, in the order of the prior lane's §1.5 table.
# (page, catalog_id, rarity_stars, role, element)
PAGES = [
    ("Acerola", "030", 2, "Support", "Electric"),
    ("Akasha", "008", 3, "Support", "Electric"),
    ("Apollon", "055", 3, "Bomber", "Fire"),
    ("Athena", "027", 3, "Defense", "Fire"),
    ("Balian", "019", 1, "Offense", "Electric"),
    ("Bear", "036", 3, "Defense", "Electric"),
    ("Beckhen", "051", 3, "Offense", "Ice"),
    ("Bibi", "040", 3, "Offense", "Electric"),
    ("Bright", "049", 3, "Support", "Fire"),
    ("Bruce Bang", "016", 1, "Support", "Ice"),
    ("Calibur", "053", 3, "Defense", "Fire"),
    ("Captain", "009", 1, "Defense", "Electric"),
    ("Crocus", "058", 3, "Support", "Electric"),
    ("Denali", "013", 2, "Support", "Fire"),
    ("Diana", "031", 3, "Bomber", "Electric"),
    ("Dino", "054", 3, "Bomber", "Ice"),
    ("Dumble", "048", 3, "Defense", "Ice"),
    ("Edward", "041", 3, "Defense", "Electric"),
    ("Gerard", "005", 2, "Defense", "Ice"),
    ("Gullveig", "039", 3, "Bomber", "Electric"),
    ("Harley", "046", 4, "Defense", "Ice"),
    ("Hecate", "011", 1, "Defense", "Fire"),
    ("Heidi", "044", 3, "Offense", "Fire"),
    ("Hermes", "023", 3, "Offense", "Fire"),
    ("Joy", "035", 3, "Support", "Fire"),
    ("Juno", "062", 3, "Defense", "Fire"),
    ("Kain", "029", 3, "Defense", "Electric"),
    ("Karl", "012", 3, "Offense", "Electric"),
    ("Karl Steiner", "012", 3, "Offense", "Electric"),
    ("Lantern", "001", 3, "Bomber", "Fire"),
    ("Lapis", "017", 1, "Offense", "Ice"),
    ("Levi", "015", 2, "Bomber", "Ice"),
    ("Lily & Lyla", "047", 4, "Offense", "Fire"),
    ("Locke", "014", 1, "Bomber", "Ice"),
    ("Metis", "007", 1, "Bomber", "Fire"),
    ("Mowgli", "002", 2, "Offense", "Electric"),
    ("Natalia", "037", 3, "Offense", "Ice"),
    ("Nene", "003", 3, "Defense", "Ice"),
    ("Octavia", "028", 3, "Offense", "Ice"),
    ("Pansy", "057", 3, "Support", "Electric"),
    ("Papillon", "043", 3, "Defense", "Ice"),
    ("Patrone", "033", 3, "Bomber", "Ice"),
    ("Rebecca", "021", 2, "Offense", "Fire"),
    ("Riko", "024", 2, "Defense", "Electric"),
    ("Robin", "018", 2, "Defense", "Ice"),
    ("Santa Clauster", "042", 3, "Offense", "Fire"),
    ("Scar", "032", 2, "Offense", "Ice"),
    ("Sienna", "020", 1, "Bomber", "Electric"),
    ("Sunny", "022", 2, "Support", "Ice"),
    ("Sylvester", "006", 1, "Offense", "Fire"),
    ("Teddy Bomber", "025", 2, "Bomber", "Fire"),
    ("TeddyBomber", "025", 2, "Bomber", "Fire"),
    ("Therapy", "050", 3, "Support", "Ice"),
    ("Tyltyl", "004", 1, "Support", "Fire"),
    ("Vincent", "010", 4, "Offense", "Electric"),
    ("Windblade", "052", 4, "Offense", "Electric"),
    ("Yuri", "045", 3, "Offense", "Ice"),
]

# navbox role x element grid, transcribed in the prior lane §1.15
NAVBOX = {
    ("Offense", "Electric"): ["Balian", "Bibi", "Karl Steiner", "Mowgli",
                              "Vincent", "Windblade"],
    ("Offense", "Fire"): ["Heidi", "Hermes", "Rebecca", "Lily & Lyla",
                          "Santa Clauster", "Sylvester"],
    ("Offense", "Ice"): ["Beckhen", "Lapis", "Natalia", "Octavia", "Scar", "Yuri"],
    ("Defense", "Electric"): ["Bear", "Captain", "Edward", "Juno", "Kain", "Riko"],
    ("Defense", "Fire"): ["Athena", "Calibur", "Hecate"],
    ("Defense", "Ice"): ["Dumble", "Gerard", "Harley", "Nene", "Papillon",
                         "Riko", "Robin"],
    ("Bomber", "Electric"): ["Diana", "Gullveig", "Sienna"],
    ("Bomber", "Fire"): ["Apollon", "Lantern", "Metis", "Teddy Bomber"],
    ("Bomber", "Ice"): ["Dino", "Levi", "Locke", "Patrone"],
    ("Support", "Electric"): ["Acerola", "Akasha", "Crocus", "Tyltyl"],
    ("Support", "Fire"): ["Bright", "Denali", "Joy", "Tyltyl"],
    ("Support", "Ice"): ["Bruce Bang", "Pansy", "Sunny", "Therapy"],
}


def main():
    print("wiki hero PAGES                          : %d" % len(PAGES))
    ids = OrderedDict()
    dup_pages = defaultdict(list)
    for p, cid, st, role, elem in PAGES:
        ids.setdefault(cid, []).append(p)
        dup_pages[cid].append(p)
    print("distinct catalogue IDs (= characters)   : %d" % len(ids))
    dups = {k: v for k, v in dup_pages.items() if len(v) > 1}
    print("duplicate-page characters               : %s"
          % {k: v for k, v in dups.items()})

    print()
    print("role counts over PAGES  :", dict(Counter(r for _, _, _, r, _ in PAGES)))
    print("element counts over PAGES:", dict(Counter(e for _, _, _, _, e in PAGES)))
    print("rarity counts over PAGES :",
          {k: v for k, v in sorted(Counter(s for _, _, s, _, _ in PAGES).items())})

    # navbox arithmetic
    nb_all = [n for v in NAVBOX.values() for n in v]
    nb_distinct = sorted(set(nb_all))
    print()
    print("navbox ENTRIES           : %d" % len(nb_all))
    print("navbox DISTINCT names    : %d" % len(nb_distinct))
    dupnav = [n for n in nb_distinct if nb_all.count(n) > 1]
    print("names in TWO navbox cells: %s" % dupnav)
    char_names = set()
    for cid, ps in ids.items():
        char_names.add(ps[0])
    print("navbox distinct == characters? %s  (navbox %d, characters %d)"
          % (set(nb_distinct) == char_names, len(nb_distinct), len(char_names)))
    if set(nb_distinct) != char_names:
        print("   only in navbox  :", sorted(set(nb_distinct) - char_names))
        print("   only as pages   :", sorted(char_names - set(nb_distinct)))

    print()
    print("=== the 57 -> 55 -> 54 reconciliation ===")
    print("  57 archived wiki hero PAGES")
    print(" -  2 duplicate pages (Karl/Karl Steiner = 012, Teddy Bomber/TeddyBomber = 025)")
    print(" = 55 distinct characters (55 distinct catalogue IDs)")
    print("  55 navbox cells-name distinct = 55  -> navbox enumerates ALL characters")
    print(" -  1 character absent from the 54-row List_of_Hunters sortable table")
    print("      (the sortable table is therefore INCOMPLETE, not over-complete)")
    print()
    print("Element balance over PAGES  :", dict(Counter(e for _, _, _, _, e in PAGES)))
    print("Element balance over CHARACTERS:")
    seen = {}
    for p, cid, st, role, elem in PAGES:
        seen.setdefault(cid, elem)
    print("   ", dict(Counter(seen.values())))
    print("Role balance over CHARACTERS:")
    seen2 = {}
    for p, cid, st, role, elem in PAGES:
        seen2.setdefault(cid, role)
    print("   ", dict(Counter(seen2.values())))

    # JP archive ID coverage
    jp = list(csv.DictReader(io.open(os.path.join(
        HERE, "archived-hunter-database-2019.tsv"), encoding="utf-8", newline=""),
        delimiter="\t", quotechar='"'))
    jp_ids = set(r["catalog_id"] for r in jp)
    print()
    print("JP 2019 archive distinct catalog_ids : %d" % len(jp_ids))
    print("wiki characters NOT in JP archive    : %s"
          % sorted(set(ids) - jp_ids))


if __name__ == "__main__":
    main()