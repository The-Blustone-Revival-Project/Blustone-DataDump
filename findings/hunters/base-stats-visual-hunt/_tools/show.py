#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Print a line range of the extracted text."""
import os
import sys

RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_namu_raw")
tag = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3])
p = os.path.join(RAW, tag + ".text.txt")
with open(p, "r", encoding="utf-8") as fh:
    lines = fh.read().split("\n")
for i in range(max(0, start), min(len(lines), end)):
    print("%5d| %s" % (i, lines[i][:400]))