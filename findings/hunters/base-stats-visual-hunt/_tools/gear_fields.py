#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import json

BASE = r"C:\Users\shaha\Documents\ChatGPT\Blustone\analysis\catalogue\data\cards.json"
with io.open(BASE, encoding="utf-8") as fh:
    cards = json.load(fh)
for c in cards:
    if c.get("card_id") in ("017", "006", "017_1", "006_1"):
        print("card_id", c["card_id"], "|", c.get("name"))
        for k in ("weapon", "weapon_desc", "armor", "armor_desc",
                  "accessory", "accessory_desc", "rarity", "role"):
            print("   %-15s = %r" % (k, c.get(k)))