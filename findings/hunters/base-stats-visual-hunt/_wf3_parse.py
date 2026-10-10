# -*- coding: utf-8 -*-
"""WF3: parse the cached hero-page revisions.

For every revision of every hero page:
  * locate the table whose header cell reads 'Character Attributes'
  * record whether a <caption> exists and its EXACT text
  * record every label present in the table, and every label from the canonical
    stat vocabulary that is ABSENT
  * record raw HTML of the table so the reading can be checked by eye

Nothing is inferred.  Absence is reported as absence.
"""
import io, json, os, re, sys, html
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "_wf1_cache")
RAW = os.path.join(CACHE, "raw")

# Canonical field vocabulary, in the order the wiki table presents them.
FIELDS = ["Life", "Attack", "Defense", "Attack Speed",
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
    """Yield (inner_html, attrs) for each <table>..</table>, nesting-aware."""
    out, i, n = [], 0, len(doc)
    while True:
        m = re.compile(r"<table\b([^>]*)>", re.I).search(doc, i)
        if not m:
            break
        depth, j = 1, m.end()
        pat = re.compile(r"<(/?)table\b[^>]*>", re.I)
        while depth and j < n:
            m2 = pat.search(doc, j)
            if not m2:
                break
            depth += -1 if m2.group(1) else 1
            j = m2.end()
        out.append((doc[m.end():j - len(m2.group(0))] if depth else doc[m.end():j],
                    m.group(1)))
        i = j if depth else j + 1
    return out


def cells(row_html):
    out = []
    for m in re.finditer(r"<(td|th)\b([^>]*)>(.*?)</\1>", row_html, re.I | re.S):
        out.append((m.group(1).lower(), m.group(2), txt(m.group(3))))
    return out


def parse_stats_table(inner):
    cap = None
    cm = re.search(r"<caption\b[^>]*>(.*?)</caption>", inner, re.I | re.S)
    if cm:
        cap = txt(cm.group(1))
    labels, values, rows = OrderedDict(), [], []
    for rm in re.finditer(r"<tr\b[^>]*>(.*?)</tr>", inner, re.I | re.S):
        cs = cells(rm.group(1))
        if not cs:
            continue
        rec = {"cells": [{"tag": t, "attrs": a.strip(), "text": x} for t, a, x in cs]}
        rows.append(rec)
        if len(cs) == 1 and cs[0][0] == "th":
            continue
        if len(cs) >= 2:
            labels.setdefault(cs[0][2], cs[1][2])
        if len(cs) == 4:
            labels.setdefault(cs[2][2], cs[3][2])
        if len(cs) == 1:
            labels.setdefault(cs[0][2], "")
    return cap, labels, rows


def load_all():
    docs = []
    for fn in sorted(os.listdir(RAW)):
        if not fn.endswith(".html"):
            continue
        with io.open(os.path.join(RAW, fn), "rb") as f:
            b = f.read()
        docs.append((fn, b.decode("utf-8", "replace")))
    return docs


if __name__ == "__main__":
    docs = load_all()
    print("cached revisions on disk: %d" % len(docs))
    # map filename slug -> list of (ts, doc)
    index = {}
    for fn, d in docs:
        m = re.match(r"(.*)__(\d{14})\.html$", fn)
        if not m:
            continue
        index.setdefault(m.group(1), []).append((m.group(2), d))
    result = {}
    for page, cat in HEROES:
        slug = "https_vsfan_net_wiki_" + page
        revs = index.get(slug, [])
        entries = []
        for ts, d in sorted(revs):
            hits = []
            for inner, attrs in tables(d):
                if "Character Attributes" in inner:
                    cap, labels, rows = parse_stats_table(inner)
                    hits.append({"caption": cap, "labels": labels, "rows": rows,
                                 "attrs": attrs.strip()})
            if hits:
                # oldid from footer
                om = re.findall(r"oldid=(\d+)", d)
                entries.append({"timestamp": ts, "oldids": sorted(set(om)),
                                "tables": hits,
                                "bytes": len(d)})
        result[page] = {"catalog": cat, "revisions_on_disk": len(revs),
                        "with_stats_table": entries}
    with io.open(os.path.join(CACHE, "stats-tables.json"), "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=1)

    pages_with = [p for p, v in result.items() if v["with_stats_table"]]
    print("hero pages with >=1 Character Attributes table: %d" % len(pages_with))
    for p in pages_with:
        v = result[p]
        revs = [(e["timestamp"], e["oldids"], e["tables"][0]["caption"],
                 sorted(e["tables"][0]["labels"].keys()))
                for e in v["with_stats_table"]]
        caps = set(r[2] for r in revs)
        labs = set(tuple(r[3]) for r in revs)
        print("\n=== %s (cat %s)  disk-revs=%d  stats-revs=%d" %
              (p, v["catalog"], v["revisions_on_disk"], len(revs)))
        for ts, oids, cap, keys in revs:
            print("    %s oldid=%s caption=%r" % (ts, ",".join(oids), cap))
        print("    distinct label-sets across revisions: %d" % len(labs))
        for l in labs:
            print("      %s" % (list(l),))