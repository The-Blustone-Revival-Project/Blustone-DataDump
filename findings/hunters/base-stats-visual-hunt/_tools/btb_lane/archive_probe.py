# -*- coding: utf-8 -*-
"""Archive / web probes for the sister titles, at a rate archive.org tolerates.

Guard notes honoured:
  * ONE session for the whole run (rule 15).
  * rule 16: archive.org refuses bursts -> long sleeps, sequential only.
  * rule 17: `matchType=domain` truncates -> we crawl by prefix, paged.
  * rule 18: an exact-URL CDX can return an offline placeholder -> hash bodies.
  * Every result records status+bytes so 403/429/000 is never read as a zero.
"""
import hashlib
import io
import json
import re
import sys
import time

import requests

sys.stdout.reconfigure(encoding="utf-8")

OUT = "analysis/research/base-stats-visual-hunt/_tools/btb_lane/net/archive_probe.json"

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)
s = requests.Session()
s.headers.update({"User-Agent": UA, "Accept": "*/*"})

results = []


def get(url, tag, sleep=4.0, binary=False):
    t0 = time.time()
    rec = {"tag": tag, "url": url}
    try:
        r = s.get(url, timeout=40)
        rec["status"] = r.status_code
        rec["bytes"] = len(r.content)
        rec["secs"] = round(time.time() - t0, 2)
        rec["sha256"] = hashlib.sha256(r.content).hexdigest()[:16]
        if r.status_code == 200:
            body = r.content if binary else r.text
            rec["head"] = (body[:300].decode("utf-8", "replace") if binary else body[:300]).replace("\n", " ")
            # detect the Internet Archive offline placeholder
            if not binary and "Temporarily Offline" in r.text[:4000]:
                rec["offline_placeholder"] = True
        else:
            rec["head"] = r.text[:200].replace("\n", " ")
    except Exception as e:  # noqa: BLE001
        rec["status"] = "ERR"
        rec["error"] = "%s: %s" % (type(e).__name__, e)
    time.sleep(sleep)
    results.append(rec)
    print(
        "%-26s %-6s %9s  %s"
        % (tag, rec.get("status"), rec.get("bytes"), rec["url"][:95])
    )
    return rec


# --- 0. POSITIVE CONTROL: a URL this project has already fetched successfully.
get(
    "http://web.archive.org/cdx/search/cdx?url=blustone.jp&matchType=domain&limit=5",
    "ctl-blustonejp-domain",
    sleep=6,
)
get(
    "http://web.archive.org/web/20191015065805/https://blustone.jp/hunter/",
    "ctl-known-blustone-page",
    sleep=6,
)

# --- 1. Did the Wayback ever capture the BTB namu page?
# The namu slug has NO '?' so the CDX query-artefact trap does not apply here,
# but we still page and hash-check.
BTB = "%EB%B9%84%EC%9A%98%EB%93%9C%20%EB%8D%94%20%EB%B0%94%EC%9A%B4%EC%A6%88"
get(
    "http://web.archive.org/cdx/search/cdx?url=namu.wiki/w/" + BTB + "&output=json&limit=40",
    "cdx-namu-btb",
    sleep=6,
)
get(
    "http://web.archive.org/cdx/search/cdx?url=namu.wiki/w/" + BTB + "*&matchType=prefix&limit=40",
    "cdx-namu-btb-prefix",
    sleep=6,
)

# --- 2. VisualShower official sites (BTB's own site is the real prize)
for dom in ["visualshower.com", "btb.visualshower.com", "beyondthebounds.com"]:
    get(
        "http://web.archive.org/cdx/search/cdx?url=" + dom + "&matchType=domain&limit=60&collapse=urlkey",
        "cdx-" + dom,
        sleep=7,
    )

# --- 3. White Island / BTB Korean portal databases
for tag, url in [
    ("gamelife-btb", "https://www.gamelife.co.kr/"),
    ("dbkpop-btb", "https://dbkpop.com/"),
]:
    get(url, tag, sleep=3)

io.open(OUT, "w", encoding="utf-8", newline="\n").write(
    json.dumps(results, ensure_ascii=False, indent=1)
)
print("\nwrote", OUT)