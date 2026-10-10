#!/usr/bin/env python3
"""Search a saved HTML page for numeric tables near transcendence/stat keywords.

Used on Korean/English wiki HTML. Prints table blocks whose text contains any
of the keyword sets, so a stat table with a transcendency label can be read
verbatim rather than inferred.
"""
import html
import re
import sys

TAG = re.compile(r"<[^>]+>")


def detag(s):
    return re.sub(r"\s+", " ", html.unescape(TAG.sub(" ", s))).strip()


def main():
    path = sys.argv[1]
    groups = [g for g in sys.argv[2:]]
    t = open(path, encoding="utf-8", errors="replace").read()
    print(f"file={path} chars={len(t)}")
    tables = re.findall(r"<table[^>]*>.*?</table>", t, re.S | re.I)
    print(f"tables found: {len(tables)}")
    hits = 0
    for i, tb in enumerate(tables):
        txt = detag(tb)
        low = txt.lower()
        if any(g.lower() in low for g in groups):
            hits += 1
            print(f"\n===== TABLE #{i}  ({len(tb)} chars) =====")
            rows = re.findall(r"<tr[^>]*>(.*?)</tr>", tb, re.S | re.I)
            for r in rows[:30]:
                cells = [detag(c) for c in re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", r, re.S | re.I)]
                cells = [c for c in cells if c != ""]
                if cells:
                    print("  | " + " | ".join(cells))
            if len(rows) > 30:
                print(f"  ... (+{len(rows)-30} rows)")
    print(f"\ntables matching {groups}: {hits}")

    # Also: any prose sentences containing a transcendence term AND a digit+percent
    print("\n===== prose lines with transcendence keyword and a number =====")
    plain = detag(t)
    for m in re.finditer(r"[^.]{0,220}(?:transcend|자기극복|초월|capacit)[^.]{0,220}\.", plain, re.I):
        s = m.group(0).strip()
        if re.search(r"\d", s):
            print("  * " + s[:400])


if __name__ == "__main__":
    main()
