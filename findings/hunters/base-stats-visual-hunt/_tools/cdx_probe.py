#!/usr/bin/env python3
"""CDX probe helper for the vsfan hunt.

Every probe prints an explicit HTTP status and byte count so a zero can be
distinguished from a transport failure, and the caller can run a known-good
positive control before believing any negative.
"""
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (compatible; blustone-research/1.0)"


def fetch(url, timeout=120):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read()
            return r.status, body, time.time() - t0
    except urllib.error.HTTPError as e:
        body = e.read()
        return e.code, body, time.time() - t0
    except Exception as e:  # transport-level
        return None, str(e).encode("utf-8", "replace"), time.time() - t0


def cdx(params):
    base = "https://web.archive.org/cdx/search/cdx?"
    return base + urllib.parse.urlencode(params)


def show(label, params, body_out=None, head=40):
    url = cdx(params)
    st, body, dt = fetch(url)
    text = body.decode("utf-8", "replace")
    lines = [l for l in text.splitlines() if l.strip()]
    print(f"[{label}] http={st} bytes={len(body)} rows={max(0,len(lines)-1)} secs={dt:.1f}")
    print(f"    query: {url}")
    for l in lines[:head]:
        print("    " + l[:300])
    if len(lines) > head:
        print(f"    ... (+{len(lines)-head} more)")
    if body_out:
        with open(body_out, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        print(f"    saved -> {body_out}")
    return st, lines


if __name__ == "__main__":
    import json
    # CONTROL: exact-match a page the ledger already proved retrievable.
    show("CTL_List_of_Hunters", {"url": "vsfan.net/wiki/List_of_Hunters", "output": "text", "limit": "50"})
    print()
    # CONTROL: exact-match a hero page with 3 known captures.
    show("CTL_Akasha", {"url": "https://vsfan.net/wiki/Akasha", "output": "text", "limit": "50"})
    print()
    # TARGET 1: every distinct /wiki/ URL, all revisions collapsed to one row per URL.
    show("T1_wiki_urls", {"url": "vsfan.net/wiki/", "matchType": "prefix",
                          "output": "text", "collapse": "urlkey", "limit": "20000"},
         body_out=sys.argv[1] if len(sys.argv) > 1 else None, head=5)
    print()
    # TARGET 2: every /wiki/ URL WITHOUT collapse -> every revision row.
    show("T2_wiki_all_revisions", {"url": "vsfan.net/wiki/", "matchType": "prefix",
                                  "output": "text", "limit": "20000"}, head=5)
