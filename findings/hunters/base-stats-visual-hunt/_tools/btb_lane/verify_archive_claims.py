# -*- coding: utf-8 -*-
"""Verify the two archival claims in the report before signing off:
  (1) 132 distinct URLs under btb.visualshower.com
  (2) the four documentation pages exist in that census
Both are read back from the saved CDX census, not from memory.
"""
import io
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

P = "analysis/research/base-stats-visual-hunt/_tools/btb_lane/net/btb_site_urls.json"
d = json.loads(io.open(P, encoding="utf-8").read())

for host, rows in d.items():
    print("=== %s ===" % host)
    print("  distinct URLs recorded : %d" % len(rows))
    if host != "btb.visualshower.com":
        continue
    print()
    print("  documentation pages cited in the report:")
    for want in ["character_ko", "game_ko", "help_desk_ko", "world_ko", "event_ko"]:
        hits = [r for r in rows if want in r["original"]]
        for h in hits:
            print("     %-14s ts=%s status=%s  %s" % (want, h["ts"], h["status"], h["original"]))
    print()
    ext = {}
    for r in rows:
        ext[r["original"].rsplit(".", 1)[-1].lower() if "." in r["original"].rsplit("/", 1)[-1] else "(none)"] = (
            ext.get(r["original"].rsplit(".", 1)[-1].lower() if "." in r["original"].rsplit("/", 1)[-1] else "(none)", 0) + 1
        )
    print("  by extension:", dict(sorted(ext.items(), key=lambda kv: -kv[1])))
    html = [r for r in rows if r["original"].endswith((".html", ".php", "")) or "?" in r["original"] or r["original"].count("/") <= 3]
    print("  page-like (non-asset) URLs: %d" % len(html))