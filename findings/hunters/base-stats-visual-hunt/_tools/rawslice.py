#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys

RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_namu_raw")
tag = sys.argv[1]
needle = sys.argv[2] if len(sys.argv) > 2 else None
span = int(sys.argv[3]) if len(sys.argv) > 3 else 2500
p = os.path.join(RAW, tag + ".utf8.txt")
d = open(p, encoding="utf-8").read()
print("file", p, "len", len(d))
for t in ["<table", "</table", "<tr", "<td", "wiki-content", 'id="content',
          "\ud2b8\uae30 \ud6a8\uacfc", "\uc7a5\ube0c \ubaa9\ub85d"]:
    print(repr(t), d.count(t))
if needle:
    i = d.find(needle)
    print("needle", repr(needle), "at", i)
    if i >= 0:
        print("----- RAW SLICE -----")
        print(d[max(0, i - span):i + span])
        print("----- END SLICE -----")