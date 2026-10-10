#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""List every internal /w/ link found in a fetched namu page, so the whole
subpage namespace can be enumerated from the source rather than guessed."""
import os
import re
import sys
import urllib.parse

RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_namu_raw")
tag = sys.argv[1]
filt = sys.argv[2] if len(sys.argv) > 2 else ""
p = os.path.join(RAW, tag + ".utf8.txt")
d = open(p, encoding="utf-8").read()
seen = []
for m in re.finditer(r"href=[\"']([^\"']+)[\"']", d):
    h = m.group(1)
    if "/w/" not in h:
        continue
    path = urllib.parse.unquote(h.split("/w/", 1)[1].split("#")[0])
    if filt and filt not in path:
        continue
    if path and path not in seen:
        seen.append(path)
print("links", len(seen))
for s in seen:
    print(s)