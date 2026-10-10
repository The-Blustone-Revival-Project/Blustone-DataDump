# -*- coding: utf-8 -*-
"""Census + full fetch of the White Island Fandom wiki.

White Island is the more likely sister title to carry stat data (it is
described as an RPG and has seasons / episodes), so it gets the same
treatment: full page enumeration FIRST (so a later zero is a real census
zero), then a bounded fetch of every page.
"""
import hashlib
import io
import json
import os
import sys
import time

import requests

sys.stdout.reconfigure(encoding="utf-8")

OUTDIR = "analysis/research/base-stats-visual-hunt/_tools/btb_lane/net/wi_fandom"
TXT = OUTDIR + "/pages"
HOST = "whiteisland.fandom.com"

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)
s = requests.Session()
s.headers.update({"User-Agent": UA, "Accept": "application/json"})

os.makedirs(OUTDIR, exist_ok=True)
os.makedirs(TXT, exist_ok=True)


def api(params, tag, sleep=2.5):
    url = "https://%s/api.php?%s" % (HOST, params)
    try:
        r = s.get(url, timeout=40)
        print("%-18s %-5s %8s" % (tag, r.status_code, len(r.content)))
        time.sleep(sleep)
        return r.text if r.status_code == 200 else None
    except Exception as e:  # noqa: BLE001
        print("%-18s ERR %s" % (tag, e))
        time.sleep(sleep)
        return None


# ---- POSITIVE CONTROL --------------------------------------------------
ctl = api("action=query&meta=siteinfo&siprop=general&format=json", "CONTROL")
ctl_ok = bool(ctl and '"query"' in ctl)
print("CONTROL PASSED:", ctl_ok)
if not ctl_ok:
    raise SystemExit("control failed - refusing to record negatives")

# ---- enumerate every page ---------------------------------------------
pages = []
cont = ""
for i in range(25):
    q = "action=query&list=allpages&aplimit=500&format=json" + (
        "&apcontinue=" + cont if cont else ""
    )
    txt = api(q, "allpages-%d" % i)
    if not txt:
        break
    d = json.loads(txt)
    batch = d.get("query", {}).get("allpages", [])
    pages.extend(p["title"] for p in batch)
    cont = d.get("continue", {}).get("apcontinue", "")
    if not cont:
        break

pages = sorted(set(pages))
print("\nWHITE ISLAND WIKI TOTAL PAGES: %d" % len(pages))
for p in pages:
    print("   ", p)

io.open(OUTDIR + "/_allpages.json", "w", encoding="utf-8", newline="\n").write(
    json.dumps(pages, ensure_ascii=False, indent=1)
)

# ---- fetch every page --------------------------------------------------
ok = 0
log = []
for i, title in enumerate(pages):
    url = (
        "https://%s/api.php?action=parse&page=%s&prop=wikitext&format=json&formatversion=2"
        % (HOST, requests.utils.quote(title, safe=""))
    )
    try:
        r = s.get(url, timeout=40)
        if r.status_code == 200:
            wt = r.json().get("parse", {}).get("wikitext", "")
            fn = "%s/%03d_%s.txt" % (
                TXT,
                i,
                "".join(c if c.isalnum() or c in " -_" else "-" for c in title)[:46],
            )
            io.open(fn, "w", encoding="utf-8", newline="\n").write(wt)
            log.append({"title": title, "file": os.path.basename(fn), "chars": len(wt)})
            ok += 1
        else:
            log.append({"title": title, "status": r.status_code})
    except Exception as e:  # noqa: BLE001
        log.append({"title": title, "status": "ERR", "error": str(e)})
    time.sleep(1.6)

print("\nfetched %d/%d" % (ok, len(pages)))
io.open(OUTDIR + "/_page_log.json", "w", encoding="utf-8", newline="\n").write(
    json.dumps(log, ensure_ascii=False, indent=1)
)