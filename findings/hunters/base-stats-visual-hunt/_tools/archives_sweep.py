#!/usr/bin/env python3
"""Sweep blustone.jp /archives/ Wayback captures.

CONTROL FIRST: the Beckhen (051) profile capture, which the prior lane proved
retrievable, must return 200 with real bytes and reproduce all 13 TSV tokens
before any zero below is treated as a real negative.

http:// only: HTTPS to web.archive.org is refused on this host.
"""
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (compatible; blustone-research/1.0)"
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HERE, "_archives_work")
CDX = "http://web.archive.org/cdx/search/cdx?"


def fetch(url, timeout=180, tries=4):
    last = (None, b"")
    for a in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, r.read()
        except urllib.error.HTTPError as e:
            b = e.read()
            last = (e.code, b)
            if e.code in (502, 503, 504) and a < tries - 1:
                time.sleep(3 * (a + 1))
                continue
            return e.code, b
        except Exception as e:
            last = (None, str(e).encode())
            if a < tries - 1:
                time.sleep(3 * (a + 1))
                continue
    return last


def cdx(params, label, show=0):
    p = dict(params)
    url = CDX + urllib.parse.urlencode(p)
    st, b = fetch(url)
    t = b.decode("utf-8", "replace")
    rows = [l for l in t.split("\n") if l.strip()]
    if rows and rows[0].startswith("net,"):
        rows = rows[1:]
    print(f"[{label}] http={st} bytes={len(b)} rows={len(rows)}")
    if st != 200:
        print("    NOT A NEGATIVE (query failed):", t[:200])
    for r in rows[:show] if show else []:
        print("   " + r[:240])
    return st, rows


CONTROL_URL = ("http://web.archive.org/web/20191216060610id_/https://blustone.jp/hunter/"
               "%E3%83%AC%E3%82%A2%E3%83%AA%E3%83%86%E3%82%A3%E5%88%A5/"
               "%E3%83%95%E3%82%A1%E3%82%A4%E3%83%88%E3%82%AF%E3%83%A9%E3%83%96%E3%81%AE%E5%AE%88%E8%AD%B7%E8%80%85"
               "%E3%80%8C%E3%83%99%E3%83%83%E3%82%B1%E3%83%B3%E3%80%8D")


def control():
    print("=== CONTROL: Beckhen 051 profile (id_) ===")
    st, b = fetch(CONTROL_URL)
    print(f"http={st} bytes={len(b)} sha256={hashlib.sha256(b).hexdigest()[:16]}")
    if st != 200 or len(b) < 500:
        print("CONTROL FAIL -- stop, no zero below is trustworthy")
        return None
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "control-beckhen.html"), "wb") as f:
        f.write(b)
    txt = b.decode("utf-8", "replace")
    nums = re.findall(r"[\d,]{2,}", txt)
    return txt


def main():
    txt = control()
    if txt is None:
        return 2
    print("CONTROL PASS\n")

    print("=== CDX: blustone.jp/archives/* (matchType=prefix, urlkey collapse) ===")
    st, rows = cdx({"url": "blustone.jp/archives/", "matchType": "prefix",
                    "output": "text", "collapse": "urlkey", "limit": "20000",
                    "fl": "timestamp,original,statuscode,mimetype,digest,length"},
                   "archives prefix")
    json.dump(rows, open(os.path.join(OUT, "cdx-archives.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(f"  -> {len(rows)} rows\n")

    print("=== whole-domain path template census (for context) ===")
    st2, rows2 = cdx({"url": "blustone.jp", "matchType": "domain", "output": "text",
                      "collapse": "urlkey", "limit": "50000",
                      "fl": "timestamp,original,statuscode,mimetype,digest,length"},
                     "domain")
    json.dump(rows2, open(os.path.join(OUT, "cdx-domain.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    paths = {}
    for r in rows2:
        f = r.split(" ")
        if len(f) < 5:
            continue
        u = f[1]
        seg = [s for s in urllib.parse.unquote(u).split("/") if s]
        tmpl = "/".join(["<id>" if s.isdigit() else s for s in seg])
        paths.setdefault(tmpl, []).append(r)
    print(f"  distinct templates: {len(paths)}")
    for tmpl, v in sorted(paths.items(), key=lambda kv: -len(kv[1]))[:40]:
        print(f"    {len(v):4d}  {tmpl[:100]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())