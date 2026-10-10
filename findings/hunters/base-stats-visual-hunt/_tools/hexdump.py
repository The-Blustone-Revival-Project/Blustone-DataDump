#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Dump long hex tokens (namu file hashes) and data-* attributes from a file page."""
import os
import re
import sys

RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_namu_raw")
tag = sys.argv[1]
p = os.path.join(RAW, tag + ".utf8.txt")
d = open(p, encoding="utf-8").read()
hexes = sorted(set(re.findall(r"\b[0-9a-f]{40,120}\b", d)))
print("LONG HEX TOKENS:", len(hexes))
for h in hexes:
    print("  ", h)
print("\nDATA-* ATTRS:")
for m in re.finditer(r"\b(data-[a-z-]+)=[\"']([^\"']{6,})[\"']", d):
    print("  %s = %s" % (m.group(1), m.group(2)[:200]))
print("\nFILE.HOST MENTIONS:")
for m in re.finditer(r"[\"'(]([^\"'()\s]*(?:file|image|img)[^\"'()\s]*\.(?:jpg|jpeg|png|gif|webp))", d, re.I):
    print("  ", m.group(1)[:220])