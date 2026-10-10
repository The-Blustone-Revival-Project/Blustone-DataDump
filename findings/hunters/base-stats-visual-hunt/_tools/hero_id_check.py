#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import json
import re

BASE = r"C:\Users\shaha\Documents\ChatGPT\Blustone\analysis\catalogue\data\cards.json"
with io.open(BASE, encoding="utf-8") as fh:
    data = json.load(fh)
cards = data if isinstance(data, list) else data.get("cards", data)
print("keys of first element:", sorted(cards[0].keys()))
for c in cards:
    s = json.dumps(c, ensure_ascii=False)
    for pat in (r"Lapis", r"라피스", r"Sylvester", r"실베스터", r"Beckhen", r"백헨"):
        if re.search(pat, s):
            print("\nMATCH", pat)
            print(s[:700])
            break