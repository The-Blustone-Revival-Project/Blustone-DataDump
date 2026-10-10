# -*- coding: utf-8 -*-
"""Fetch every page of the BTB Fandom wiki and extract its prose.

The census already enumerated 26 titles, so this is a bounded fetch with a
known denominator - we can prove completeness rather than infer it.
"""
import hashlib
import io
import json
import os
import sys
import time

import requests

sys.stdout.reconfigure(encoding="utf-8")

OUTDIR = "analysis/research/base-stats-visual-hunt/_tools/btb_lane/net/btb_fandom"
TXT = OUTDIR + "/pages"
HOST = "beyond-the-bounds-game.fandom.com"

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)
s = requests.Session()
s.headers.update({"User-Agent": UA, "Accept": "application/json"})

pages = json.loads(io.open(OUTDIR + "/_allpages.json", encoding="utf-8").read())
os.makedirs(TXT, exist_ok=True)

log = []
ok = 0
for i, title in enumerate(pages):
    url = (
        "https://%s/api.php?action=parse&page=%s&prop=wikitext&format=json&formatversion=2"
        % (HOST, requests.utils.quote(title, safe=""))
    )
    try:
        r = s.get(url, timeout=40)
        rec = {"title": title, "status": r.status_code, "bytes": len(r.content)}
        if r.status_code == 200:
            d = r.json()
            wt = d.get("parse", {}).get("wikitext", "")
            fn = "%s/%02d_%s.txt" % (TXT, i, title.replace(":", "-").replace("/", "-")[:40])
            io.open(fn, "w", encoding="utf-8", newline="\n").write(wt)
            rec["file"] = os.path.basename(fn)
            rec["chars"] = len(wt)
            rec["sha256"] = hashlib.sha256(wt.encode("utf-8")).hexdigest()[:16]
            ok += 1
        else:
            rec["head"] = r.text[:150]
        log.append(rec)
        print(
            "%-46s %-5s %8s  %s"
            % (title[:46], r.status_code, len(r.content), rec.get("chars", ""))
        )
    except Exception as e:  # noqa: BLE001
        log.append({"title": title, "status": "ERR", "error": str(e)})
        print("%-46s ERR %s" % (title[:46], e))
    time.sleep(2.5)

print("\nfetched %d/%d pages OK" % (ok, len(pages)))
io.open(OUTDIR + "/_page_log.json", "w", encoding="utf-8", newline="\n").write(
    json.dumps(log, ensure_ascii=False, indent=1)
)