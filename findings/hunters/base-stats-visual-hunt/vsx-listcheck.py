# -*- coding: utf-8 -*-
"""vsx-listcheck: prove the List_of_Hunters name cells are LINKS, and recover
the link target.  Also compare rarity/role/element per character between the
sortable table and the hero-page infobox, and against the JP archive."""
import io, json, os, re, sys, html
from collections import Counter, OrderedDict

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "_wf1_cache", "raw")
ICON2 = {"1star-symbol.png": 1, "2star-symbol.png": 2, "3star-symbol.png": 3,
         "4star-symbol.png": 4, "5star-symbol.png": 5}
ROLE = {"AttackIcon.png": "Offense", "DefenseIcon.png": "Defense",
        "BomberIcon.png": "Bomber", "SupportIcon.png": "Support"}
ELEM = {"FireIcon.png": "Fire", "ElecIcon.png": "Electric", "IceIcon.png": "Ice"}

# the 57 hero pages, with the prior lane's transcribed infobox values
PAGES = [
    ("Acerola", "030", 2, "Support", "Electric"), ("Akasha", "008", 3, "Support", "Electric"),
    ("Apollon", "055", 3, "Bomber", "Fire"), ("Athena", "027", 3, "Defense", "Fire"),
    ("Balian", "019", 1, "Offense", "Electric"), ("Bear", "036", 3, "Defense", "Electric"),
    ("Beckhen", "051", 3, "Offense", "Ice"), ("Bibi", "040", 3, "Offense", "Electric"),
    ("Bright", "049", 3, "Support", "Fire"), ("Bruce Bang", "016", 1, "Support", "Ice"),
    ("Calibur", "053", 3, "Defense", "Fire"), ("Captain", "009", 1, "Defense", "Electric"),
    ("Crocus", "058", 3, "Support", "Electric"), ("Denali", "013", 2, "Support", "Fire"),
    ("Diana", "031", 3, "Bomber", "Electric"), ("Dino", "054", 3, "Bomber", "Ice"),
    ("Dumble", "048", 3, "Defense", "Ice"), ("Edward", "041", 3, "Defense", "Electric"),
    ("Gerard", "005", 2, "Defense", "Ice"), ("Gullveig", "039", 3, "Bomber", "Electric"),
    ("Harley", "046", 4, "Defense", "Ice"), ("Hecate", "011", 1, "Defense", "Fire"),
    ("Heidi", "044", 3, "Offense", "Fire"), ("Hermes", "023", 3, "Offense", "Fire"),
    ("Joy", "035", 3, "Support", "Fire"), ("Juno", "062", 3, "Defense", "Fire"),
    ("Kain", "029", 3, "Defense", "Electric"), ("Karl", "012", 3, "Offense", "Electric"),
    ("Karl Steiner", "012", 3, "Offense", "Electric"), ("Lantern", "001", 3, "Bomber", "Fire"),
    ("Lapis", "017", 1, "Offense", "Ice"), ("Levi", "015", 2, "Bomber", "Ice"),
    ("Lily & Lyla", "047", 4, "Offense", "Fire"), ("Locke", "014", 1, "Bomber", "Ice"),
    ("Metis", "007", 1, "Bomber", "Fire"), ("Mowgli", "002", 2, "Offense", "Electric"),
    ("Natalia", "037", 3, "Offense", "Ice"), ("Nene", "003", 3, "Defense", "Ice"),
    ("Octavia", "028", 3, "Offense", "Ice"), ("Pansy", "057", 3, "Support", "Electric"),
    ("Papillon", "043", 3, "Defense", "Ice"), ("Patrone", "033", 3, "Bomber", "Ice"),
    ("Rebecca", "021", 2, "Offense", "Fire"), ("Riko", "024", 2, "Defense", "Electric"),
    ("Robin", "018", 2, "Defense", "Ice"), ("Santa Clauster", "042", 3, "Offense", "Fire"),
    ("Scar", "032", 2, "Offense", "Ice"), ("Sienna", "020", 1, "Bomber", "Electric"),
    ("Sunny", "022", 2, "Support", "Ice"), ("Sylvester", "006", 1, "Offense", "Fire"),
    ("Teddy Bomber", "025", 2, "Bomber", "Fire"), ("TeddyBomber", "025", 2, "Bomber", "Fire"),
    ("Therapy", "050", 3, "Support", "Ice"), ("Tyltyl", "004", 1, "Support", "Fire"),
    ("Vincent", "010", 4, "Offense", "Electric"), ("Windblade", "052", 4, "Offense", "Electric"),
    ("Yuri", "045", 3, "Offense", "Ice"),
]

ALIAS = {"Sylvester Schwarzenegger": "Sylvester", "Karl": "Karl Steiner",
         "TeddyBomber": "Teddy Bomber"}


def main():
    fn = os.path.join(RAW, "https_vsfan_net_wiki_List_of_Hunters__20191114021317.html")
    d = io.open(fn, "rb").read().decode("utf-8", "replace")

    print("=== every /wiki/ link inside the sortable table ===")
    # isolate the sortable table
    m = re.search(r'<table[^>]*class="[^"]*sortable[^"]*"[^>]*>.*?</table>', d, re.S | re.I)
    body = m.group(0) if m else d
    links = re.findall(r'href="[^"]*/wiki/([^"#?]+)"[^>]*>(.*?)</a>', body, re.S | re.I)
    targets = OrderedDict()
    for tgt, label in links:
        lab = re.sub(r"<[^>]+>", "", html.unescape(label)).strip()
        lab = re.sub(r"\s+", " ", lab)
        tgt = html.unescape(tgt)
        if not tgt:
            continue
        targets.setdefault(tgt, set()).add(lab)
    for t, labs in targets.items():
        print("  %-34s displayed as: %s" % (t, sorted(labs)))
    print()
    print("distinct link targets in the table: %d" % len(targets))

    print()
    print("=== per-character agreement: sortable table vs hero-page infobox ===")
    loh = json.load(io.open(os.path.join(HERE, "_wf1_cache", "list-of-hunters.json"),
                            encoding="utf-8"))
    rows = loh["rows"]
    tbl = {}
    for r in rows:
        k = ALIAS.get(r["name"], r["name"])
        tbl.setdefault(k, []).append(r)
    page_by_char = OrderedDict()
    for p, cid, st, role, elem in PAGES:
        key = ALIAS.get(p, p)
        page_by_char.setdefault(key, (p, cid, st, role, elem))

    print("  sortable-table characters : %d" % len(tbl))
    print("  hero-page characters      : %d" % len(page_by_char))
    missing = sorted(set(page_by_char) - set(tbl))
    extra = sorted(set(tbl) - set(page_by_char))
    print("  hero pages ABSENT from sortable table : %s" % missing)
    print("  sortable rows with no hero page      : %s" % extra)

    ok = dis = 0
    print()
    print("  %-18s %-28s %-28s" % ("character", "sortable(rar/role/elem)",
                                   "infobox(rar/role/elem)"))
    for k in sorted(tbl):
        if k not in page_by_char:
            continue
        p, cid, st, role, elem = page_by_char[k]
        r = tbl[k][0]
        a = (r["rarity"], r["role"], r["element"])
        b = (st, role, elem)
        same = a == b
        ok += same
        dis += (not same)
        print("  %-18s %-28s %-28s %s"
              % (k, "/".join(map(str, a)), "/".join(map(str, b)),
                 "" if same else "  <-- DISAGREE"))
    print()
    print("  agree on all three fields: %d ; disagree: %d" % (ok, dis))
    print()
    print("  sortable rarity distribution: %s"
          % dict(sorted(Counter(v[0]["rarity"] for v in tbl.values()).items())))
    print("  sortable role distribution  : %s"
          % dict(Counter(v[0]["role"] for v in tbl.values())))
    print("  sortable element distribution: %s"
          % dict(Counter(v[0]["element"] for v in tbl.values())))


if __name__ == "__main__":
    main()