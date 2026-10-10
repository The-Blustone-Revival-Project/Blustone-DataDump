#!/usr/bin/env python3
"""Final external probe: the Japanese blustone.jp corpus and any sibling
Japanese/Korean stat databases, for a page carrying a transcendence-level
stat column.

CONTROL FIRST: an archived blustone.jp hunter profile the prior lane proved
retrievable (Lapis 017) -- must return 200 with real bytes before any zero
below is reported as a real negative.
"""
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
            return None, b""
    return None, b""


def cdx(params, label, show=0, filt=None):
    p = dict(params)
    if filt:
        p["filter"] = filt
    url = CDX + urllib.parse.urlencode(p)
    st, b = fetch(url)
    t = b.decode("utf-8", "replace")
    rows = [l for l in t.split("\n") if l.strip()]
    rows = rows[1:] if rows and rows[0].startswith("net,") else rows
    print(f"[{label}] http={st} bytes={len(b)} rows={len(rows)}")
    if st != 200:
        print("    NOT A NEGATIVE (query failed):", t[:130])
    for r in rows[:show] if show else []:
        print("   " + r[:210])
    return st, rows


def main():
    # CONTROL: web.archive.org root
    st, b = fetch("https://web.archive.org/")
    c1 = st == 200 and len(b) > 100000
    print(f"[CONTROL web.archive.org] http={st} bytes={len(b)} -> {'PASS' if c1 else 'FAIL'}")
    if not c1:
        return 2

    print("\n--- blustone.jp : every distinct path, collapsed ---")
    st, rows = cdx({"url": "blustone.jp", "matchType": "domain", "output": "text",
                    "collapse": "urlkey", "limit": "50000"}, "blustone.jp all")
    paths = {}
    for r in rows:
        f = r.split(" ")
        if len(f) < 7:
            continue
        u = f[2]
        seg = [s for s in u.split("/") if s]
        # strip a trailing numeric id to get the template
        tmpl = "/".join(["<id>" if s.isdigit() else s for s in seg])
        paths.setdefault(tmpl, []).append((f[1], f[4], f[6]))
    print(f"  distinct path templates: {len(paths)}")
    for tmpl, v in sorted(paths.items(), key=lambda kv: -len(kv[1]))[:30]:
        print(f"    {len(v):4d}  {tmpl[:90]}")

    print("\n--- blustone.jp rows whose URL hints at stats/level/growth ---")
    import re
    hits = [r for r in rows if re.search(r"stat|level|growth|ability|kouka|param|train|rank|grow", r, re.I)]
    print(f"  matches: {len(hits)}")
    for r in hits[:30]:
        print("   " + r[:210])

    print("\n--- sibling JP hosts ---")
    for dom in ["blustone2.jp", "www.blustone.jp"]:
        st2, rows2 = cdx({"url": dom, "matchType": "domain", "output": "text",
                          "collapse": "urlkey", "limit": "50000"}, dom)
    return 0


if __name__ == "__main__":
    sys.exit(main())
