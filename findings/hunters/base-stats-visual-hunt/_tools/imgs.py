#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Print every <img> src / srcset found in a fetched page, plus the visible text."""
import os
import re
import sys

RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_namu_raw")
tag = sys.argv[1]
p = os.path.join(RAW, tag + ".utf8.txt")
d = open(p, encoding="utf-8").read()
srcs = []
for m in re.finditer(r"<img[^>]+>", d):
    t = m.group(0)
    s = re.search(r"src=[\"']([^\"']+)[\"']", t)
    d2 = re.search(r"data-src=[\"']([^\"']+)[\"']", t)
    if s:
        srcs.append(("src", s.group(1)))
    if d2:
        srcs.append(("data-src", d2.group(1)))
print("IMG TAGS:", len(srcs))
for k, v in srcs:
    print("  %-9s %s" % (k, v[:220]))
# text
txt = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", d)
txt = re.sub(r"(?s)<[^>]+>", " ", txt)
txt = re.sub(r"\s+", " ", txt)
print("\nTEXT:", txt[:1600])