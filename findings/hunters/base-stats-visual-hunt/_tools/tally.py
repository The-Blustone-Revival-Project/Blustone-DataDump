#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Final tally of the namu lane: attempts vs retrievals, per URL."""
import json
import os

RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_namu_raw")
p = os.path.join(RAW, "_results.json")
rows = []
with open(p, encoding="utf-8") as fh:
    for ln in fh:
        ln = ln.strip()
        if ln:
            rows.append(json.loads(ln))
print("total URL attempts recorded:", len(rows))
ok = [r for r in rows if r.get("status") == 200 and r.get("nbytes", 0) > 2000]
print("HTTP 200 with >2000 decoded bytes:", len(ok))
gear = [r for r in ok if any(k in r["url"] for k in
        ("%EA%B3%B5%EA%B2%A9", "%EC%88%98%EB%B9%84", "%ED%8F%AD%EA%B2%A9",
         "%EB%8F%84%EC%9A%B0"))]
print("GEAR pages retrieved        :", len(gear))
hosts = {}
for r in ok:
    h = r["url"].split("/")[2]
    hosts[h] = hosts.get(h, 0) + 1
print("successful pages by host    :", hosts)
print("\nGEAR page details:")
for r in gear:
    host = r["url"].split("/")[2]
    page = r["url"].split("/w/")[1]
    print("  %-16s %-40s %8d bytes  %6d chars  hangul=%d"
          % (host, page, r["nbytes"], r["n_chars"], r["hangul"]))
err = {}
for r in rows:
    if r.get("status") != 200 or r.get("nbytes", 0) <= 2000:
        err[r.get("status")] = err.get(r.get("status"), 0) + 1
print("\nnon-200 / empty by status:", err)