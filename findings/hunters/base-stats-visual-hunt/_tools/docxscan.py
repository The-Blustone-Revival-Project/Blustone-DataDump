#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Extract DOCX text (zip -> word/document.xml) and scan for gear stat lines."""
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def docx_text(path):
    with zipfile.ZipFile(path) as z:
        xml = z.read("word/document.xml")
    root = ET.fromstring(xml)
    out = []
    for p in root.iter(NS + "p"):
        t = "".join(n.text or "" for n in p.iter(NS + "t"))
        if t.strip():
            out.append(t)
    return out


GEAR = re.compile(
    r"(accessor|equipment|gear|armou?r|weapon)", re.I)
STATVAL = re.compile(
    r"(increases|max\s*hp|\+\s*\d+\s*(hp|atk|def)|hp\s*\d|"
    r"lv\.?\s*\d+\s*[|:\-]\s*\d)", re.I)
NUM = re.compile(r"\d")


def main():
    for path in sys.argv[1:]:
        try:
            lines = docx_text(path)
        except Exception as e:
            print("FAIL", path, e)
            continue
        print("\n=== %s : %d paragraphs" % (path, len(lines)))
        g = [l for l in lines if GEAR.search(l)]
        s = [l for l in lines if STATVAL.search(l)]
        n = [l for l in lines if GEAR.search(l) and NUM.search(l)]
        print("  gear-ish paragraphs      : %d" % len(g))
        print("  stat-value paragraphs    : %d" % len(s))
        print("  gear+number paragraphs   : %d   <== TARGET" % len(n))
        for l in n[:25]:
            print("      %s" % l[:190])


if __name__ == "__main__":
    main()