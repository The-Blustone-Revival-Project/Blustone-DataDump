#!/usr/bin/env python3
"""Analyze /archives/ CDX rows: list every distinct capture, dedupe by digest,
and classify. Also verify the 051 TSV values were reproduced in the control body.
"""
import io
import json
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HERE, "_archives_work")
BASE = os.path.join(HERE, "..", "..", "..")

rows = json.load(open(os.path.join(OUT, "cdx-archives.json"), encoding="utf-8"))
print(f"archives-prefix rows: {len(rows)}")

# timestamp original statuscode mimetype digest length
by_url = {}
for r in rows:
    f = r.split(" ")
    if len(f) < 4:
        continue
    by_url.setdefault(f[1], []).append(f)

print(f"distinct original URLs in prefix query: {len(by_url)}")

def decode(u):
    from urllib.parse import unquote
    return unquote(u)

# classify
plain, oembed, attach = [], [], []
for u, v in by_url.items():
    if "wp-json/oembed" in u:
        oembed.append(u)
    elif "/attachment/" in u:
        attach.append((u, v))
    else:
        plain.append((u, v))

print(f"  plain archive pages : {len(plain)}")
print(f"  oembed query rows   : {len(oembed)}")
print(f"  attachment pages    : {len(attach)}")

print("\n=== ATTACHMENT pages (full detail) ===")
for u, v in sorted(attach):
    print(f"\n{u}")
    for f in v:
        print(f"    ts={f[0]} status={f[2] if len(f)>2 else '?'} mime={f[3] if len(f)>3 else '?'} len={f[5] if len(f)>5 else '?'} digest={f[4][:20] if len(f)>4 else ''}")

print("\n=== PLAIN archive pages ===")
for u, v in sorted(plain, key=lambda kv: kv[0]):
    dgs = sorted({(f[4][:12] if len(f) > 4 else "") for f in v})
    sts = sorted({(f[2] if len(f) > 2 else "") for f in v})
    print(f"{decode(u)[:80]:80s} caps={len(v)} digests={dgs} status={sts}")

json.dump({"plain": [u for u, _ in plain], "attach": [u for u, _ in attach],
           "oembed": oembed},
          open(os.path.join(OUT, "archives-urllist.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)

# control verification against the TSV
print("\n=== CONTROL cross-check vs archived-hunter-database-2019.tsv ===")
tsv = os.path.join(BASE, "analysis", "research", "base-stats-visual-hunt",
                   "archived-hunter-database-2019.tsv")
rows_t = open(tsv, encoding="utf-8").read().split("\n")
hdr = rows_t[0].split("\t")
print("header:", hdr)
for line in rows_t[1:]:
    if not line.strip():
        continue
    f = line.split("\t")
    if f and f[0] == "051":
        print("051 row:", f)
        break
html = open(os.path.join(OUT, "control-beckhen.html"), encoding="utf-8", errors="replace").read()
for tok in ["1,678", "864", "660", "8,709", "33", "200", "42", "44"]:
    print(f"  token {tok!r} in control html: {tok in html}")