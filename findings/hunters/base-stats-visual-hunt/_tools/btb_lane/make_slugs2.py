# -*- coding: utf-8 -*-
"""Slice the exact BTB Korean title out of the client table key, then encode."""
import io
import json
import sys
from urllib.parse import quote

sys.stdout.reconfigure(encoding="utf-8")

KEYS = "analysis/recovered-data/leveldb-tables/all-tables.json"
doc = json.loads(io.open(KEYS, encoding="utf-8").read())

stems = set()
for tname, tbody in doc["tables"].items():
    items = tbody.values() if isinstance(tbody, dict) else tbody
    for r in items:
        if isinstance(r, dict):
            k = r.get("key", "") or ""
            j = r.get("json")
            t = (j.get("TEXT", "") if isinstance(j, dict) else "") or ""
            blob = k + " " + t
            if "BTB" in blob or "Beyond the Bounds" in blob:
                stems.add(k.split("|")[0])

for s in sorted(stems):
    # The BTB title is the leading phrase before the particle.
    head = s.split("\uc758 \uc601")[0] if "\uc758 \uc601" in s else s
    print("full stem  :", s)
    print("slug(full) :", quote(s))
    print("slug(head) :", quote(head))
    print()