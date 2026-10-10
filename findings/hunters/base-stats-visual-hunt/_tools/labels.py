#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Discovery: list every '<short-hangul-label>:' line in the fetched page text.

This exists so the detector never has to hard-code a Hangul codepoint
(GUARD rule 13). Run it, read the real labels, then pass them to statdetect.
"""
import os
import re
import sys

RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_namu_raw")
tag = sys.argv[1]
p = os.path.join(RAW, tag + ".text.txt")
t = open(p, encoding="utf-8").read()
from collections import Counter
c = Counter()
for ln in t.split("\n"):
    s = ln.strip()
    m = re.match(r"^([\uAC00-\uD7A3]{2,6}(?: [\uAC00-\uD7A3]{1,6})?):$", s)
    if m:
        c[m.group(1)] += 1
for k, v in c.most_common(60):
    print("%4d  %s" % (v, k))