# -*- coding: utf-8 -*-
"""Diagnose the 429 and establish which instruments actually work today.

Guard: a positive control must PASS before any negative is recorded. This
script probes several independent namespaces so a single host's rate limit is
not mistaken for a content negative.
"""
import io
import json
import sys
import time

import requests

sys.stdout.reconfigure(encoding="utf-8")

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)


def sess():
    s = requests.Session()
    s.headers.update({"User-Agent": UA, "Accept": "*/*"})
    return s


TARGETS = [
    # (tag, url, note)
    ("web.archive-root", "http://web.archive.org/", "archive root (http only)"),
    ("archive-root-https", "https://web.archive.org/", "archive root (https)"),
    ("wayback-cdx", "http://web.archive.org/cdx/search/cdx?url=namu.wiki&limit=3", "CDX"),
    ("blustone-jp", "http://blustone.jp/", "known-live 2019 site, http"),
    ("example", "http://example.com/", "generic control"),
    ("wikipedia", "http://ko.wikipedia.org/wiki/" + "%EB%A7%88%EB%94%94%EB%A9%94", "ko wiki http"),
]

s = sess()
res = []
for tag, url, note in TARGETS:
    t0 = time.time()
    try:
        r = s.get(url, timeout=25)
        res.append(
            {
                "tag": tag,
                "url": url,
                "note": note,
                "status": r.status_code,
                "bytes": len(r.content),
                "secs": round(time.time() - t0, 2),
                "head": r.text[:200].replace("\n", " "),
            }
        )
    except Exception as e:  # noqa: BLE001
        res.append(
            {
                "tag": tag,
                "url": url,
                "note": note,
                "status": "ERR",
                "error": "%s: %s" % (type(e).__name__, e),
                "secs": round(time.time() - t0, 2),
            }
        )
    time.sleep(2.0)  # be gentle; archive.org refuses bursts

for r in res:
    print(
        "%-20s %-6s %8s  %s"
        % (r["tag"], r.get("status"), r.get("bytes"), r.get("note", ""))
    )
    if r.get("status") == 429:
        print("      body:", r.get("head", "")[:160])

io.open(
    "analysis/research/base-stats-visual-hunt/_tools/btb_lane/net/ctl_diag.json",
    "w",
    encoding="utf-8",
    newline="\n",
).write(json.dumps(res, ensure_ascii=False, indent=1))