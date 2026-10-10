#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Why does the strict label-only regex under-count the Support page's slots?"""
import os
import re

RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_namu_raw")
t = open(os.path.join(RAW, "g-d-\uB3C4\uc6B0\ubbf8.text.txt"), encoding="utf-8").read()
lines = t.split("\n")
slots = ["\ubb34\uae30", "\ubc29\uc5b4\uad6c", "\uc7a5\uc2e0\uad6c"]
for s in slots:
    exact = [i for i, ln in enumerate(lines)
             if re.match(r"^(?:%s)\s*:?\s*$" % s, ln.strip())]
    loose = [i for i, ln in enumerate(lines)
             if ln.strip().rstrip(":").strip() == s]
    print("%-6s strict=%d loose=%d" % (s, len(exact), len(loose)))
    if len(loose) > len(exact):
        extra = set(loose) - set(exact)
        for i in sorted(extra)[:4]:
            print("      not-strict line %d: %r" % (i, lines[i][:120]))