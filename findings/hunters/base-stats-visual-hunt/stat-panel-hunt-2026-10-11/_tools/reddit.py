#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fetch old.reddit post JSON (no slug needed) and list gallery images."""
import urllib.request, json, sys, html

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) BlustoneResearch/1.0"}

def get(pid):
    u = "https://old.reddit.com/r/Blustone/comments/%s/.json" % pid
    r = urllib.request.Request(u, headers=UA)
    raw = urllib.request.urlopen(r, timeout=60).read()
    return json.loads(raw)

def main():
    for pid in sys.argv[1:]:
        try:
            d = get(pid)
        except Exception as e:
            print(pid, "ERR", repr(e)[:300]); continue
        pd = d[0]["data"]["children"][0]["data"]
        print("=" * 100)
        print(pid, "|", pd.get("title", "")[:100])
        print("  author:", pd.get("author"), "| selftext_len:", len(pd.get("selftext") or ""))
        mm = pd.get("media_metadata") or {}
        print("  gallery_count:", len(mm))
        for mid, m in mm.items():
            s = (m.get("s") or {})
            url = html.unescape(s.get("u") or "")
            print("  IMG %s %s %s" % (mid, m.get("m"), url[:130]))
        print("  post_url:", pd.get("url_overridden_by_dest") or pd.get("url"))
        for c in (d[1]["data"]["children"] or [])[:6]:
            cd = c["data"]
            print("  CMT %s: %s" % (cd.get("author"), (cd.get("body") or "")[:150].replace("\n", " ")))

if __name__ == "__main__":
    main()
