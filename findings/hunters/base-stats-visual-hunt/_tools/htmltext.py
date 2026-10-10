#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Extract readable text + tables from the fetched namu gear pages."""
import os
import re
import sys
import html as htmlmod

RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_namu_raw")


def strip_tags(s):
    s = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", s)
    s = re.sub(r"(?i)<br\s*/?>", "\n", s)
    s = re.sub(r"(?i)</(p|div|tr|li|h[1-6]|table)>", "\n", s)
    s = re.sub(r"(?i)</t[dh]>", " | ", s)
    s = re.sub(r"(?s)<[^>]+>", "", s)
    s = htmlmod.unescape(s)
    s = re.sub(r"[ \t\u00a0]+", " ", s)
    s = re.sub(r"\n\s*\n+", "\n", s)
    return s.strip()


def main():
    tag = sys.argv[1]
    src = os.path.join(RAW, tag + ".utf8.txt")
    with open(src, "r", encoding="utf-8") as fh:
        doc = fh.read()
    txt = strip_tags(doc)
    outp = os.path.join(RAW, tag + ".text.txt")
    with open(outp, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(txt)
    print("TAG", tag, "chars", len(txt), "lines", txt.count("\n") + 1)
    print("fffd", txt.count("\ufffd"))
    # outline: headings
    for m in re.finditer(r"(?m)^(.{0,60})$", txt):
        pass
    hits = [i for i, ln in enumerate(txt.split("\n"))
            if re.search(r"장비|장비\s*레벨|공격력|방어력|최대\s*체력|능력치", ln)]
    print("equipment-ish lines:", len(hits))
    for i in hits[:80]:
        print("  %5d| %s" % (i, txt.split("\n")[i][:200]))


if __name__ == "__main__":
    main()