# -*- coding: utf-8 -*-
"""Enumerate the BTB official site captures in the Wayback archive.

Guard rule 17: matchType=domain truncates ~170-207 rows. So we page with a
small limit and walk until an empty page, and we ALSO re-crawl by prefix.
Guard rule 16: sequential + sleeps; archive.org refuses bursts.
"""
import io
import json
import re
import sys
import time
from urllib.parse import quote

import requests

sys.stdout.reconfigure(encoding="utf-8")

OUT = "analysis/research/base-stats-visual-hunt/_tools/btb_lane/net/btb_site_urls.json"

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)
s = requests.Session()
s.headers.update({"User-Agent": UA, "Accept": "*/*"})


def cdx(params, sleep=6.0, tries=3):
    url = "http://web.archive.org/cdx/search/cdx?" + params
    for a in range(tries):
        try:
            r = s.get(url, timeout=45)
            if r.status_code == 200:
                return r.text
            print("   retry %d status %s" % (a + 1, r.status_code))
        except Exception as e:  # noqa: BLE001
            print("   retry %d err %s" % (a + 1, e))
        time.sleep(12)
    return ""


def rows(txt):
    out = []
    for line in txt.splitlines():
        f = line.split(" ")
        if len(f) >= 3:
            out.append({"ts": f[1], "original": f[2], "status": f[3] if len(f) > 3 else ""})
    return out


allrows = {}

for host in ["btb.visualshower.com", "beyondthebounds.com"]:
    seen = {}
    print("=== %s ===" % host)
    # paged exact-domain walk
    for page in range(0, 6):
        params = (
            "url=%s&matchType=domain&limit=200&collapse=urlkey&page=%d"
            % (quote(host, safe=""), page)
        )
        t = cdx(params)
        rs = rows(t)
        print("  page %d -> %d rows" % (page, len(rs)))
        if not rs:
            break
        new = 0
        for r in rs:
            if r["original"] not in seen:
                seen[r["original"]] = r
                new += 1
        if new == 0:
            print("  no new rows, stop")
            break
        time.sleep(6)
    allrows[host] = sorted(seen.values(), key=lambda r: r["original"])
    print("  TOTAL unique URLs: %d" % len(allrows[host]))

    for r in allrows[host][:200]:
        print("    %s  %s  %s" % (r["ts"], r["status"], r["original"][:110]))

io.open(OUT, "w", encoding="utf-8", newline="\n").write(
    json.dumps(allrows, ensure_ascii=False, indent=1)
)
print("\nwrote", OUT)