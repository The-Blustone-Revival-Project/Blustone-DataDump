#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crosswalk the item names recovered from the namu gear pages against the
shipped CHAR_STR accessory table (charstr-items-2026-10-06.tsv, column 5 =
accessory_ko, column 3 = accessory_en).

Terms are passed in a UTF-8 file so no codepoint is ever hand-typed.
"""
import io
import os
import sys

BASE = r"C:\Users\shaha\Documents\ChatGPT\Blustone\analysis\research\base-stats-visual-hunt"
TSV = os.path.join(BASE, "charstr-items-2026-10-06.tsv")


def main():
    rows = []
    with io.open(TSV, encoding="utf-8") as fh:
        head = fh.readline().rstrip("\n").split("\t")
        for ln in fh:
            ln = ln.rstrip("\n")
            if not ln.strip():
                continue
            rows.append(ln.split("\t"))
    print("columns:", head)
    print("rows:", len(rows))
    terms_file = sys.argv[1]
    with io.open(terms_file, encoding="utf-8") as fh:
        terms = [l.strip() for l in fh if l.strip()]
    print("\ncrosswalk of %d namu gear names:\n" % len(terms))
    for t in terms:
        found = []
        for r in rows:
            if len(r) < 7:
                continue
            cells = {"num": r[0], "accessory_en": r[3],
                     "accessory_ja": r[4], "accessory_ko": r[5]}
            if t == cells["accessory_ko"] or t in cells["accessory_ko"]:
                found.append(cells)
        if found:
            for c in found:
                print("  HIT   %-14s -> num %s | en %-28s | ja %s"
                      % (t, c["num"], c["accessory_en"], c["accessory_ja"]))
        else:
            print("  MISS  %-14s -> no accessory_ko match" % t)
    # also report the shipped KO column so a human can eyeball near-misses
    print("\nfull accessory_ko column (%d rows):" % len(rows))
    for r in rows:
        if len(r) >= 6:
            print("   %s  %-28s %s" % (r[0], r[3], r[5]))


if __name__ == "__main__":
    main()