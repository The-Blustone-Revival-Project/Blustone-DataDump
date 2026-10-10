# -*- coding: utf-8 -*-
"""Fetch the BTB Fandom wiki (an English-language, dedicated sister-game
resource) and its character pages.

Guard notes:
  * ONE session for the whole run (rule 15).
  * Fandom has a JSON API that avoids HTML scraping entirely; we try the API
    first because it is the instrument least likely to return a JS shell.
  * Positive control: fetch a page on the SAME host that is known to exist
    (the wiki's main page) BEFORE recording any zero about a sub-page.
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
HOST = "beyond-the-bounds-game.fandom.com"

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)
s = requests.Session()
s.headers.update({"User-Agent": UA, "Accept": "application/json, text/html;q=0.9"})

log = []


def api(params, tag, sleep=3.0):
    url = "https://%s/api.php?%s" % (HOST, params)
    t0 = time.time()
    try:
        r = s.get(url, timeout=40)
        rec = {
            "tag": tag,
            "url": url,
            "status": r.status_code,
            "bytes": len(r.content),
            "secs": round(time.time() - t0, 2),
        }
        print("%-22s %-5s %8s" % (tag, r.status_code, len(r.content)))
        if r.status_code == 200:
            rec["sha256"] = hashlib.sha256(r.content).hexdigest()[:16]
            rec["data"] = r.text
        log.append(rec)
        time.sleep(sleep)
        return r.text if r.status_code == 200 else None
    except Exception as e:  # noqa: BLE001
        print("%-22s ERR %s" % (tag, e))
        log.append({"tag": tag, "status": "ERR", "error": str(e)})
        time.sleep(sleep)
        return None


def main():
    os.makedirs(OUTDIR, exist_ok=True)

    # ---- POSITIVE CONTROL: site info from the same host ----------------
    ctl = api(
        "action=query&meta=siteinfo&siprop=general&format=json", "CONTROL-siteinfo", sleep=5
    )
    ctl_ok = bool(ctl and '"query"' in ctl)
    print("CONTROL PASSED:", ctl_ok)

    # ---- census of all pages -------------------------------------------
    allpages = None
    cont = ""
    for i in range(12):
        q = (
            "action=query&list=allpages&aplimit=500&format=json"
            + ("&apcontinue=" + cont if cont else "")
        )
        txt = api(q, "allpages-%d" % i, sleep=3.5)
        if not txt:
            break
        d = json.loads(txt)
        batch = d.get("query", {}).get("allpages", [])
        if allpages is None:
            allpages = []
        allpages.extend(batch)
        cont = d.get("continue", {}).get("apcontinue", "")
        if not cont:
            break

    pages = []
    if allpages:
        pages = sorted(p["title"] for p in allpages)
    print("\nTOTAL PAGES ENUMERATED: %d" % len(pages))
    for p in pages:
        print("   ", p)

    io.open(OUTDIR + "/_allpages.json", "w", encoding="utf-8", newline="\n").write(
        json.dumps(pages, ensure_ascii=False, indent=1)
    )
    io.open(OUTDIR + "/_log.json", "w", encoding="utf-8", newline="\n").write(
        json.dumps([{k: v for k, v in r.items() if k != "data"} for r in log], ensure_ascii=False, indent=1)
    )


if __name__ == "__main__":
    main()