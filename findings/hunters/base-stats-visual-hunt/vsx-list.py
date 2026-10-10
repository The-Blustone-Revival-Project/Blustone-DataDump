# -*- coding: utf-8 -*-
"""vsx-list: extract the List_of_Hunters sortable-table rows (name + the
alt-text of each icon column) and reconcile against the 57 archived hero pages."""
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


def txt(s):
    return re.sub(r"[\s\u00a0]+", " ",
                  html.unescape(re.sub(r"<[^>]+>", "", s))).strip()


def tables(doc):
    out, i = [], 0
    op = re.compile(r"<table\b([^>]*)>", re.I)
    cl = re.compile(r"<(/?)table\b[^>]*>", re.I)
    while True:
        m = op.search(doc, i)
        if not m:
            break
        d, j = 1, m.end()
        while d and j < len(doc):
            m2 = cl.search(doc, j)
            if not m2:
                break
            d += -1 if m2.group(1) else 1
            j = m2.end()
        end = j - len(m2.group(0)) if d else j
        out.append((doc[m.end():end], m.group(1)))
        i = end if d else j + 1
    return out


def main():
    pages = [f for f in os.listdir(RAW)
             if f.startswith("https_vsfan_net_wiki_List_of_Hunters__")]
    print("List_of_Hunters captures on disk: %d" % len(pages))
    if not pages:
        return
    fn = sorted(pages)[-1]
    d = io.open(os.path.join(RAW, fn), "rb").read().decode("utf-8", "replace")
    print("using %s  (%d bytes)" % (fn, len(d)))
    oids = sorted(set(re.findall(r"oldid=(\d+)", d)))
    print("oldid(s): %s" % oids)

    best = None
    for inner, attrs in tables(d):
        if 'class="sortable"' in attrs or "sortable" in attrs:
            rows = re.findall(r"<tr\b[^>]*>(.*?)</tr>", inner, re.I | re.S)
            if best is None or len(rows) > len(best[0]):
                best = (rows, inner)
    if not best:
        print("no sortable table found; table attrs seen:")
        for inner, attrs in tables(d):
            print("   %s" % attrs.strip()[:110])
        return
    rows = best[0]
    print("sortable <tr> count (incl. header): %d" % len(rows))

    recs = []
    for row in rows:
        # MediaWiki sortable rows put the hunter name in a row-header <th>
        # followed by <td> icon/data cells.
        allc = re.findall(r"<t[dh]\b[^>]*>(.*?)</t[dh]>", row, re.S | re.I)
        if not allc:
            continue
        cells = [txt(c) for c in allc]
        name = next((c for c in cells if c and not re.match(r"^[\u2605\s.%]+$", c)
                     and not re.match(r"^[\d\s.%]+$", c)), None)
        if name is None:
            name = cells[0]
        if re.search(r"Rarity|Hunter", name) and len(cells) <= 2:
            print("header row: %s" % cells)
            continue
        alts = []
        for c in allc:
            alts += re.findall(r'alt="([^"]*)"', c)
        rar = next((ICON2[a] for a in alts if a in ICON2), None)
        role = next((ROLE[a] for a in alts if a in ROLE), None)
        elem = next((ELEM[a] for a in alts if a in ELEM), None)
        if not any((rar, role, elem)):
            continue          # navbox/footer row, not a data row
        rest = [c for c in cells if c and c != name]
        recs.append({"name": name, "rarity": rar, "role": role,
                     "element": elem, "cells": rest})
    print("data rows: %d" % len(recs))
    print()
    for r in recs:
        print("  %-18s rar=%-4s role=%-9s elem=%-9s | %s"
              % (r["name"], r["rarity"], r["role"], r["element"],
                 " / ".join(r["cells"])[:66]))

    names = [r["name"] for r in recs]
    print()
    print("distinct names: %d" % len(set(names)))
    dups = [n for n, c in Counter(names).items() if c > 1]
    print("duplicated names: %s" % dups)

    PAGES = ["Acerola", "Akasha", "Apollon", "Athena", "Balian", "Bear", "Beckhen",
             "Bibi", "Bright", "Bruce Bang", "Calibur", "Captain", "Crocus",
             "Denali", "Diana", "Dino", "Dumble", "Edward", "Gerard", "Gullveig",
             "Harley", "Hecate", "Heidi", "Hermes", "Joy", "Juno", "Kain", "Karl",
             "Karl Steiner", "Lantern", "Lapis", "Levi", "Lily & Lyla", "Locke",
             "Metis", "Mowgli", "Natalia", "Nene", "Octavia", "Pansy", "Papillon",
             "Patrone", "Rebecca", "Riko", "Robin", "Santa Clauster", "Scar",
             "Sienna", "Sunny", "Sylvester", "Teddy Bomber", "TeddyBomber",
             "Therapy", "Tyltyl", "Vincent", "Windblade", "Yuri"]
    # characters = collapse the two duplicate page pairs
    chars = [p for p in PAGES if p not in ("Karl", "TeddyBomber")]  # keep Steiner/Bomber spelling
    chars = sorted(set(chars))
    print()
    print("=== reconciliation ===")
    print("archived hero PAGES            : %d" % len(PAGES))
    print("distinct characters           : %d" % len(chars))
    print("List_of_Hunters data rows     : %d" % len(recs))
    ln = set(names)
    print("in hero pages but NOT in list : %s" % sorted(set(chars) - ln))
    print("in list but NOT a hero page    : %s" % sorted(ln - set(chars)))
    with io.open(os.path.join(HERE, "_wf1_cache", "list-of-hunters.json"), "w",
                 encoding="utf-8") as f:
        json.dump({"file": fn, "oldids": oids, "rows": recs}, f,
                  ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()