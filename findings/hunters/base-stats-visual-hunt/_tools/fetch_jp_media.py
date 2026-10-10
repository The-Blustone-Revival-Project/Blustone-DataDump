#!/usr/bin/env python3
"""Fetch the media referenced by the Japanese /育成論/ section, especially the
キャパ超越 (Cap Transcendence) guide images capa1 / capa2 / capa / 1542365xxx,
and the per-rank rank1..rank4 images.

CONTROLS (both must PASS before any 404 is a negative):
  1. web.archive.org root -> 200 / >100,000 bytes
  2. a known-good image on this very host (rankup.jpg) -> 200 + JPEG signature
"""
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (compatible; blustone-research/1.0)"
SIGS = {b"\xff\xd8\xff": "JPEG", b"\x89PNG": "PNG", b"GIF8": "GIF", b"BM": "BMP"}


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


def sig(b):
    for s, n in SIGS.items():
        if b.startswith(s):
            return n
    return None


# (label, original url) -- try every archived capture via the wayback timemap
MEDIA = [
    ("capa-1-e1542352374554", "https://blustone.jp/wp-content/uploads/2018/11/capa-1-e1542352374554.jpg"),
    ("capa",                   "http://blustone.jp/wp-content/uploads/2018/11/capa.jpg"),
    ("capa1-1024x911",         "https://blustone.jp/wp-content/uploads/2018/11/capa1-1024x911.jpg"),
    ("capa2-1024x911",         "https://blustone.jp/wp-content/uploads/2018/11/capa2-1024x911.jpg"),
    ("capa2-300x267",          "https://blustone.jp/wp-content/uploads/2018/12/capa2-300x267.jpg"),
    ("capa2-300x267b",         "https://blustone.jp/wp-content/uploads/2018/11/capa2-300x267.jpg"),
    ("att1542365712",          "https://blustone.jp/wp-content/uploads/2018/11/1542365712-300x267.jpg"),
    ("att1542365835",          "https://blustone.jp/wp-content/uploads/2018/11/1542365835-300x267.jpg"),
    ("rank1-1024x911",         "https://blustone.jp/wp-content/uploads/2018/11/rank1-1024x911.jpg"),
    ("rank2-1024x911",         "https://blustone.jp/wp-content/uploads/2018/11/rank2-1024x911.jpg"),
    ("rank3-1024x911",         "https://blustone.jp/wp-content/uploads/2018/11/rank3-1024x911.jpg"),
    ("rank4-1024x911",         "https://blustone.jp/wp-content/uploads/2018/11/rank4-1024x911.jpg"),
    ("IMG_9719",               "http://blustone.jp/wp-content/uploads/2018/11/IMG_9719.jpg"),
    ("d",                      "https://blustone.jp/wp-content/uploads/2018/11/d.jpg"),
    ("traning",                "https://blustone.jp/wp-content/uploads/2018/11/traning.png"),
    ("traning1",               "https://blustone.jp/wp-content/uploads/2018/11/traning1.jpg"),
    ("traning2",               "https://blustone.jp/wp-content/uploads/2018/11/traning2.jpg"),
    ("att1542365925",          "https://blustone.jp/wp-content/uploads/2018/11/1542365925-300x267.jpg"),
    ("att1542366108",          "https://blustone.jp/wp-content/uploads/2018/11/1542366108-300x267.jpg"),
    ("att1542366153",          "https://blustone.jp/wp-content/uploads/2018/11/1542366153-300x267.jpg"),
    ("att1542366172",          "https://blustone.jp/wp-content/uploads/2018/11/1542366172-300x267.jpg"),
    ("att1542366194",          "https://blustone.jp/wp-content/uploads/2018/11/1542366194-300x267.jpg"),
    ("att1542366264",          "https://blustone.jp/wp-content/uploads/2018/11/1542366264-300x267.jpg"),
]


def captures(url):
    q = ("https://web.archive.org/cdx/search/cdx?"
         + urllib.parse.urlencode({"url": url, "output": "text", "limit": "200"}))
    s, b = fetch(q)
    if s != 200:
        return []
    rows = [l for l in b.decode("utf-8", "replace").split("\n") if l.strip()][1:]
    out = []
    for r in rows:
        f = r.split(" ")
        if len(f) >= 7 and f[4] == "200":
            out.append((f[1], f[2]))
    return out


def main(outdir):
    os.makedirs(outdir, exist_ok=True)

    st, b = fetch("https://web.archive.org/")
    c1 = st == 200 and len(b) > 100000
    print(f"[CONTROL 1] web.archive.org http={st} bytes={len(b)} -> {'PASS' if c1 else 'FAIL'}")
    st, b = fetch("https://web.archive.org/web/20190403182150id_/"
                  "http://blustone.jp/wp-content/uploads/2018/11/rankup.jpg")
    c2 = st == 200 and sig(b) == "JPEG"
    print(f"[CONTROL 2] rankup.jpg http={st} bytes={len(b)} sig={sig(b)} -> {'PASS' if c2 else 'FAIL'}")
    if not (c1 and c2):
        print("ABORT.")
        return 2

    saved = 0
    for label, url in MEDIA:
        caps = captures(url)
        print(f"\n### {label}")
        print(f"    url={url}")
        print(f"    CDX 200-captures: {len(caps)}  {[c[0] for c in caps][:6]}")
        got = False
        for ts, orig in caps:
            for form in ("id_", "im_"):
                arc = f"https://web.archive.org/web/{ts}{form}/{orig}"
                s, body = fetch(arc)
                sg = sig(body)
                print(f"      {form} {ts}: http={s} bytes={len(body)} sig={sg}")
                if sg and s == 200:
                    p = os.path.join(outdir, f"{label}_{ts}_{sg}.bin")
                    with open(p, "wb") as f:
                        f.write(body)
                    saved += 1
                    got = True
                    print(f"        *** SAVED {p}")
        if not got:
            print("      NOT RECOVERED (0 archives with 200, control passed)")

    print(f"\n=== MEDIA RECOVERED: {saved} ===")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
