#!/usr/bin/env python3
"""Fetch and analyse the FULL (uncollapsed) vsfan /wiki/ revision inventory.

Why: `collapse=urlkey` yields one row per URL (1,223), which is what the prior
lane used. Uncollapsed it yields every archived revision (8,887 rows), i.e.
revisions that were never retrieved and could carry Life/Attack/Defense rows
absent from the revision that WAS read.

Prints an explicit HTTP status + byte count for every request so a transport
failure can never be mistaken for a negative.
"""
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict

UA = "Mozilla/5.0 (compatible; blustone-research/1.0)"
CDX = "https://web.archive.org/cdx/search/cdx?"


def fetch(url, timeout=180, tries=4):
    last = None
    for attempt in range(tries):
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, r.read(), time.time()
        except urllib.error.HTTPError as e:
            body = e.read()
            if e.code in (502, 503, 504) and attempt < tries - 1:
                last = (e.code, body)
                time.sleep(4 * (attempt + 1))
                continue
            return e.code, body, time.time()
        except Exception as e:
            last = (None, str(e).encode())
            if attempt < tries - 1:
                time.sleep(4 * (attempt + 1))
                continue
            return None, str(e).encode("utf-8", "replace"), time.time()
    return last


def get_cdx(params, label, out=None):
    url = CDX + urllib.parse.urlencode(params)
    st, body, t0 = fetch(url)
    text = body.decode("utf-8", "replace")
    lines = [l for l in text.split("\n") if l.strip()]
    rows = lines[1:] if lines and lines[0].startswith("net,") else lines
    print(f"[{label}] http={st} bytes={len(body)} datarows={len(rows)} secs={t0-t0:.0f}", flush=True)
    if st != 200:
        print("    FIRST BYTES:", text[:200])
        return None
    if out:
        with open(out, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        print(f"    saved -> {out}", flush=True)
    return rows


def parse(rows):
    """-> list of dicts: ts, url, status, mime, length"""
    out = []
    for l in rows:
        p = l.split(" ")
        if len(p) < 7:
            continue
        # CDX text order: urlkey timestamp original mimetype statuscode digest length
        out.append({
            "ts": p[1],
            "url": p[2],
            "mime": p[3],
            "status": p[4],
            "digest": p[5] if len(p) > 5 else "",
            "length": int(p[6]) if p[6].isdigit() else 0,
        })
    return out


def main(outdir):
    import os
    os.makedirs(outdir, exist_ok=True)

    # ---- CONTROL: a URL the prior ledger proves is retrievable ----
    st, body, _ = fetch("https://web.archive.org/web/20190821024308id_/https://vsfan.net/wiki/Beckhen")
    print(f"[CONTROL Beckhen id_ fetch] http={st} bytes={len(body)} (ledger says 88572)", flush=True)

    # ---- CONTROL: exact-match CDX that previously returned 3 rows ----
    ctl = get_cdx({"url": "https://vsfan.net/wiki/Akasha", "output": "text", "limit": "50"},
                  "CONTROL CDX Akasha")
    if ctl:
        for l in ctl[:6]:
            print("    " + l[:220])

    # ---- TARGET: every /wiki/ revision, uncollapsed ----
    rows = get_cdx({"url": "vsfan.net/wiki/", "matchType": "prefix", "output": "text", "limit": "50000"},
                   "TARGET /wiki/ ALL revisions", out=os.path.join(outdir, "cdx-wiki-all-revisions.tsv"))
    if not rows:
        print("ABORT: no target rows"); return 1
    recs = parse(rows)
    print(f"    parsed {len(recs)} revision rows")

    by_title = defaultdict(list)
    for r in recs:
        title = r["url"].split("/wiki/", 1)[1] if "/wiki/" in r["url"] else ""
        by_title[title].append(r)

    print(f"    distinct titles: {len(by_title)}")
    multi = {t: v for t, v in by_title.items() if len(v) > 1}
    print(f"    titles with >1 archived revision: {len(multi)}")

    # Which titles have the most revisions?
    top = sorted(by_title.items(), key=lambda kv: -len(kv[1]))[:25]
    print("\n  === titles with most archived revisions ===")
    for t, v in top:
        codes = ",".join(sorted({x["status"] for x in v}))
        print(f"    {len(v):4d}  [{codes}]  {t[:70]}")

    with open(os.path.join(outdir, "vsfan-revision-inventory.json"), "w",
              encoding="utf-8", newline="\n") as f:
        json.dump({t: v for t, v in sorted(by_title.items())}, f, indent=1)
    print(f"\n  saved inventory -> {outdir}/vsfan-revision-inventory.json")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
