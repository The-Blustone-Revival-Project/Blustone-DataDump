#!/usr/bin/env python3
"""Find the archived share_en post 215324 body and extract its <img> URLs.

CONTROL FIRST: a Naver-cafe image URL the prior lane PROVED retrievable
(75605/303/534/001/725a8e...jpg, HTTP 200 / 57,414 bytes). If that control
fails, no 404 below is a real negative.
"""
import html
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (compatible; blustone-research/1.0)"
CDX = "https://web.archive.org/cdx/search/cdx?"


def fetch(url, timeout=180, tries=4):
    for a in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, r.read()
        except urllib.error.HTTPError as e:
            b = e.read()
            if e.code in (502, 503, 504) and a < tries - 1:
                time.sleep(4 * (a + 1)); continue
            return e.code, b
        except Exception:
            if a < tries - 1:
                time.sleep(4 * (a + 1)); continue
            return None, b"transport"
    return None, b"transport"


def cdx(params, label):
    url = CDX + urllib.parse.urlencode(params)
    st, b = fetch(url)
    t = b.decode("utf-8", "replace")
    lines = [l for l in t.split("\n") if l.strip()]
    rows = lines[1:] if lines and lines[0].startswith("net,") else lines
    print(f"[{label}] http={st} bytes={len(b)} rows={len(rows)}")
    if st != 200:
        print("   NOT A NEGATIVE (query failed). first bytes:", t[:160])
    return rows


def main():
    # ---------- CONTROL ----------
    ctrl = ("https://web.archive.org/web/20210903030305id_/http://bs.visualshower.com/"
            "files/attach/images/75605/303/534/001/725a8e175454a533e96dac68fc5fdb49.jpg")
    st, b = fetch(ctrl)
    ok = st == 200 and len(b) == 57414
    print(f"[CONTROL known-good naver image] http={st} bytes={len(b)} expect=57414 "
          f"-> {'PASS' if ok else 'FAIL'}")
    if not ok:
        print("ABORT: control failed; nothing below is a negative.")
        return 2

    # ---------- locate post 215324 ----------
    print("\n--- CDX: cafe.naver.com domains containing visualshower/blustone ---")
    for dom in ["cafe.naver.com"]:
        rows = cdx({"url": dom, "matchType": "domain", "output": "text",
                    "collapse": "urlkey", "limit": "50000",
                    "filter": "original:.*(visualshower|blustone|vs_fan|vsfan).*"},
                   f"{dom} filter")
        for r in rows[:25]:
            print("   " + r[:220])

    print("\n--- CDX: bs.visualshower.com full domain (collapsed) ---")
    rows = cdx({"url": "bs.visualshower.com", "matchType": "domain", "output": "text",
                "collapse": "urlkey", "limit": "50000"}, "bs.visualshower.com")
    hits = [r for r in rows if "215324" in r]
    print(f"   rows total {len(rows)}, containing '215324': {len(hits)}")
    for r in hits[:20]:
        print("   * " + r[:240])
    return 0


if __name__ == "__main__":
    sys.exit(main())
