#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Equipment-block extractor for the four namu role pages.

Discovers the slot labels from the page itself (GUARD rule 13), then prints, per
hero, the three slot blocks verbatim: label, flavour prose, item name. Also
counts how many skill-effect slots exist and how many are FILLED, which is the
control that proves the pages were really parsed rather than skimmed.
"""
import os
import re
import sys
import json

RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_namu_raw")


def rd(tag):
    p = os.path.join(RAW, tag + ".text.txt")
    return open(p, encoding="utf-8").read()


def labels(text):
    from collections import Counter
    c = Counter()
    for ln in text.split("\n"):
        m = re.match(r"^([\uAC00-\uD7A3]{2,6}(?: [\uAC00-\uD7A3]{1,6})?):$", ln.strip())
        if m:
            c[m.group(1)] += 1
    return c


def main():
    tags = sys.argv[1:]
    # The three equipment slot labels are the single-word labels common to the
    # role pages; they are discovered, never hand-typed (GUARD rule 13). Pages
    # whose most frequent label is a skill-effect label (Support page markup)
    # would otherwise be mis-parsed, so the trio is intersected across pages.
    sets = []
    for tag in tags:
        c = labels(rd(tag))
        sets.append({k for k, v in c.items() if " " not in k and v >= 3})
    common = set.intersection(*sets) if sets else set()
    out = {}
    for tag in tags:
        t = rd(tag)
        lines = t.split("\n")
        c = labels(t)
        slots = sorted(common)
        sk = [k for k in c if " " in k and c[k] >= 5]
        print("\n##### %s" % tag)
        print("  discovered slot labels : %s" % slots)
        print("  discovered effect label: %s (count %d)"
              % (sk, c[sk[0]] if sk else 0))
        if sk:
            filled = [ln for ln in lines
                      if ln.strip().startswith(sk[0]) and len(ln.strip()) > len(sk[0]) + 1]
            print("  effect slots: %d   FILLED: %d   EMPTY: %d"
                  % (c[sk[0]], len(filled), c[sk[0]] - len(filled)))
            for ln in filled[:10]:
                print("     FILLED EXAMPLE: %r" % ln.strip()[:140])
        rows = []
        headings = {ln.strip() for ln in lines
                    if re.match(r"^\d+(\.\d+)*\.\s", ln.strip())}
        for i, ln in enumerate(lines):
            s = ln.strip().rstrip(":").strip()
            if s in slots:
                flavour, name = "", ""
                for j in range(i + 1, min(len(lines), i + 6)):
                    nxt = lines[j].strip()
                    nkey = nxt.rstrip(":").strip()
                    if not nxt or nkey in slots or nkey in headings:
                        break            # next slot/heading => this is EMPTY
                    if not flavour:
                        flavour = nxt
                    else:
                        name = nxt
                        break
                filled = bool(name) and name.rstrip(":").strip() not in slots
                filled = filled and name not in headings
                rows.append({"line": i, "slot": s, "flavour": flavour,
                             "name": name, "filled": filled})
        out[tag] = rows
        nf = sum(1 for r in rows if r["filled"])
        print("  equipment SLOTS: %d   FILLED (has item name): %d   EMPTY: %d"
              % (len(rows), nf, len(rows) - nf))
        for r in rows:
            if r["filled"]:
                print("     FILLED  %s\t%s\t%s" % (r["slot"], r["name"][:40],
                                                   r["flavour"][:70]))
    with open(os.path.join(RAW, "_equipment_rows.json"), "w",
              encoding="utf-8", newline="\n") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()