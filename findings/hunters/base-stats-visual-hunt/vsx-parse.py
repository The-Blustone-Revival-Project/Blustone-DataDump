# -*- coding: utf-8 -*-
"""vsx-parse: extract every 'Character Attributes' table from the cached hero
page revisions, exactly as written.  Absence is recorded as absence.

Emits:
  _wf1_cache/stats-tables.json      structured, per page per revision
  stdout                            human-readable census
"""
import io, json, os, re, sys, html
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "_wf1_cache")
RAW = os.path.join(CACHE, "raw")

CANON = ["Life", "Attack", "Defense", "Attack Speed",
         "Critical Damage Chance", "Critical Damage", "Armor Penetration",
         "Block Chance", "Block Resistance", "Damage Reduction Block",
         "Strengthen Elemental Attributes", "Elemental Attack Resistance",
         "Life Regeneration"]

HEROES = [
    ("Acerola", "030"), ("Akasha", "008"), ("Apollon", "055"), ("Athena", "027"),
    ("Balian", "019"), ("Bear", "036"), ("Beckhen", "051"), ("Bibi", "040"),
    ("Bright", "049"), ("Bruce_Bang", "016"), ("Calibur", "053"), ("Captain", "009"),
    ("Crocus", "058"), ("Denali", "013"), ("Diana", "031"), ("Dino", "054"),
    ("Dumble", "048"), ("Edward", "041"), ("Gerard", "005"), ("Gullveig", "039"),
    ("Harley", "046"), ("Hecate", "011"), ("Heidi", "044"), ("Hermes", "023"),
    ("Joy", "035"), ("Juno", "062"), ("Kain", "029"), ("Karl", "012"),
    ("Karl_Steiner", "012"), ("Lantern", "001"), ("Lapis", "017"), ("Levi", "015"),
    ("Lily_%26_Lyla", "047"), ("Locke", "014"), ("Metis", "007"), ("Mowgli", "002"),
    ("Natalia", "037"), ("Nene", "003"), ("Octavia", "028"), ("Pansy", "057"),
    ("Papillon", "043"), ("Patrone", "033"), ("Rebecca", "021"), ("Riko", "024"),
    ("Robin", "018"), ("Santa_Clauster", "042"), ("Scar", "032"), ("Sienna", "020"),
    ("Sunny", "022"), ("Sylvester", "006"), ("Teddy_Bomber", "025"),
    ("TeddyBomber", "025"), ("Therapy", "050"), ("Tyltyl", "004"), ("Vincent", "010"),
    ("Windblade", "052"), ("Yuri", "045"),
]

TAG = re.compile(r"<[^>]+>")
WS = re.compile(r"[\s\u00a0]+")


def txt(s):
    return WS.sub(" ", html.unescape(TAG.sub("", s))).strip()


def tables(doc):
    out, i = [], 0
    openre = re.compile(r"<table\b([^>]*)>", re.I)
    close = re.compile(r"<(/?)table\b[^>]*>", re.I)
    while True:
        m = openre.search(doc, i)
        if not m:
            break
        depth, j = 1, m.end()
        while depth and j < len(doc):
            m2 = close.search(doc, j)
            if not m2:
                break
            depth += -1 if m2.group(1) else 1
            j = m2.end()
        end = j - len(m2.group(0)) if depth else j
        out.append((doc[m.end():end], m.group(1)))
        i = end if depth else j + 1
    return out


def cells(row):
    return [(m.group(1).lower(), m.group(2).strip(), txt(m.group(3)))
            for m in re.finditer(r"<(td|th)\b([^>]*)>(.*?)</\1>", row, re.I | re.S)]


def parse(inner):
    cm = re.search(r"<caption\b[^>]*>(.*?)</caption>", inner, re.I | re.S)
    cap = txt(cm.group(1)) if cm else None
    labels, rows, order = OrderedDict(), [], []
    for rm in re.finditer(r"<tr\b[^>]*>(.*?)</tr>", inner, re.I | re.S):
        cs = cells(rm.group(1))
        if not cs:
            continue
        rows.append([{"tag": t, "colspan": (re.search(r"colspan=[\"']?(\d+)", a).group(1)
                                             if re.search(r"colspan=[\"']?(\d+)", a) else ""),
                      "text": x} for t, a, x in cs])
        if len(cs) == 1 and cs[0][0] == "th":
            order.append(("SECTION", cs[0][2]))
            continue
        if len(cs) == 1:
            labels[cs[0][2]] = ""
            order.append((cs[0][2], ""))
        elif len(cs) == 2:
            labels[cs[0][2]] = cs[1][2]
            order.append((cs[0][2], cs[1][2]))
        elif len(cs) == 4:
            labels.setdefault(cs[0][2], cs[1][2])
            labels.setdefault(cs[2][2], cs[3][2])
            order.append((cs[0][2], cs[1][2]))
            order.append((cs[2][2], cs[3][2]))
    return cap, labels, order, rows


def main():
    files = sorted(f for f in os.listdir(RAW) if f.endswith(".html"))
    result = {}
    for page, cat in HEROES:
        slug = "https_vsfan_net_wiki_" + page
        revs = []
        for fn in files:
            if not fn.startswith(slug + "__"):
                continue
            ts = fn[len(slug) + 2:-5]
            with io.open(os.path.join(RAW, fn), "rb") as fh:
                doc = fh.read().decode("utf-8", "replace")
            hits = []
            for inner, attrs in tables(doc):
                if "Character Attributes" in inner:
                    cap, labels, order, rows = parse(inner)
                    hits.append({"caption": cap, "labels": labels,
                                 "order": order, "rows": rows,
                                 "table_attrs": attrs.strip(),
                                 "raw_table": re.sub(r"\s+", " ", inner)[:4000]})
            if hits:
                revs.append({"timestamp": ts, "bytes": len(doc),
                             "oldids": sorted(set(re.findall(r"oldid=(\d+)", doc))),
                             "tables": hits})
        result[page] = {"catalog": cat, "revisions": revs}
    with io.open(os.path.join(CACHE, "stats-tables.json"), "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=1)

    have = [p for p, v in result.items() if v["revisions"]]
    print("cached revisions parsed: %d" % len(files))
    print("hero pages carrying >=1 'Character Attributes' table: %d / %d"
          % (len(have), len(HEROES)))
    print()
    for page, cat in HEROES:
        v = result[page]
        if not v["revisions"]:
            continue
        print("### %-15s cat=%s  stats-revisions=%d" % (page, cat, len(v["revisions"])))
        for r in v["revisions"]:
            for t in r["tables"]:
                print("    %s oldid=%-8s caption=%r  n_labels=%d"
                      % (r["timestamp"], ",".join(r["oldids"]), t["caption"],
                         len(t["labels"])))
        sets = set()
        caps = set()
        for r in v["revisions"]:
            for t in r["tables"]:
                sets.add(tuple(t["order"]))
                caps.add(t["caption"])
        print("    distinct ORDER-tuple across revisions: %d ; captions: %s"
              % (len(sets), sorted(str(c) for c in caps)))
        for s in sorted(sets):
            print("      %s" % (list(s),))
        print()


if __name__ == "__main__":
    main()