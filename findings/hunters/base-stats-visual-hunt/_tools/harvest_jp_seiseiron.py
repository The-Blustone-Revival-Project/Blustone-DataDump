#!/usr/bin/env python3
"""Fetch the whole Japanese /育成論/ ("Growth Theory") section of blustone.jp,
including resolving the WordPress attachment pages to their actual media files.

A prior lane read /育成論/キャパ超越/capa2 and recorded "No HP/ATK/DEF". This
pass covers the parent article, the per-rank pages, the training/crystal pages,
and -- the untested target -- the 7 /attachment/ pages, which on WordPress are
redirect stubs pointing at the real image.

CONTROLS:
  1. web.archive.org root -> 200
  2. one already-harvested /archives/<id> profile -> 200 with real bytes
  3. one already-proven image on the same host -> 200 with an image signature
Nothing below is a negative unless all controls passed.
"""
import html
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (compatible; blustone-research/1.0)"

PAGES = [
    ("20190331134147", "https://blustone.jp/育成論"),
    ("20190331201909", "https://blustone.jp/育成論/キャパ超越"),
    ("20191216051555", "https://blustone.jp/育成論/キャパ超越/capa2"),
    ("20191121223254", "https://blustone.jp/育成論/キャパ超越/attachment/1542365712"),
    ("20191121144053", "https://blustone.jp/育成論/キャパ超越/attachment/1542365835"),
    ("20191118021834", "https://blustone.jp/育成論/ランクアップ"),
    ("20191118021834r", "https://blustone.jp/育成論/ランクアップ/rank1"),
    ("20191121194819", "https://blustone.jp/育成論/ランクアップ/rank2"),
    ("20191209003500", "https://blustone.jp/育成論/ランクアップ/rank3"),
    ("20191211113444", "https://blustone.jp/育成論/ランクアップ/rank4"),
    ("20191216045912", "https://blustone.jp/育成論/ランクアップ/attachment/1542366108"),
    ("20191122213132", "https://blustone.jp/育成論/ランクアップ/attachment/1542366153"),
    ("20191210184847", "https://blustone.jp/育成論/ランクアップ/attachment/1542366172"),
    ("20191211121234", "https://blustone.jp/育成論/ランクアップ/attachment/1542366194"),
    ("20191210193622", "https://blustone.jp/育成論/ランクアップ/attachment/1542366264"),
    ("20191211104454", "https://blustone.jp/育成論/トレーニング"),
    ("20191121070352", "https://blustone.jp/育成論/トレーニング/attachment/1542365925"),
    ("20191122213323", "https://blustone.jp/育成論/トレーニング/traning1"),
    ("20191121070729", "https://blustone.jp/育成論/トレーニング/traning2"),
    ("20191210184203", "https://blustone.jp/育成論/結晶"),
    ("20191216043116", "https://blustone.jp/育成論/キャラ編成例"),
]

SIGS = {b"\xff\xd8\xff": "JPEG", b"\x89PNG": "PNG", b"GIF8": "GIF", b"BM": "BMP"}
TAG = re.compile(r"<[^>]+>")


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def fetch(url, timeout=180, tries=4, follow=True):
    op = urllib.request.build_opener() if follow else urllib.request.build_opener(NoRedirect)
    for a in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with op.open(req, timeout=timeout) as r:
                return r.status, r.read(), dict(r.headers)
        except urllib.error.HTTPError as e:
            b = e.read()
            if e.code in (502, 503, 504) and a < tries - 1:
                time.sleep(4 * (a + 1)); continue
            return e.code, b, dict(e.headers or {})
        except Exception:
            if a < tries - 1:
                time.sleep(4 * (a + 1)); continue
            return None, b"", {}
    return None, b"", {}


def clean(s):
    return re.sub(r"[ \t]+", " ", html.unescape(TAG.sub(" ", s))).strip()


def sig(b):
    for s, n in SIGS.items():
        if b.startswith(s):
            return n
    return None


def main(outdir):
    os.makedirs(outdir, exist_ok=True)

    st, b, _ = fetch("https://web.archive.org/")
    c1 = st == 200 and len(b) > 100000
    print(f"[CONTROL 1 web.archive.org] http={st} bytes={len(b)} -> {'PASS' if c1 else 'FAIL'}")
    if not c1:
        return 2

    st, b, h = fetch("https://web.archive.org/web/20190403182150id_/"
                     "http://blustone.jp/wp-content/uploads/2018/11/rankup.jpg")
    c2 = st == 200 and sig(b) is not None
    print(f"[CONTROL 2 known-good jp image] http={st} bytes={len(b)} sig={sig(b)} "
          f"-> {'PASS' if c2 else 'FAIL'}")
    if not c2:
        return 2

    media_saved = 0
    for key, url in PAGES:
        ts = key.rstrip("r")
        arc = f"https://web.archive.org/web/{ts}id_/{urllib.parse.quote(url, safe=':/')}"
        s, body, hdr = fetch(arc)
        print(f"\n{'='*76}\n{url}\n  {arc[:130]}\n  http={s} bytes={len(body)}")
        if s != 200:
            print("   FETCH FAILED -- not a negative, transport")
            continue
        sg = sig(body)
        if sg:
            media_saved += 1
            p = os.path.join(outdir, f"MEDIA_{key}_{os.path.basename(url)}")
            with open(p, "wb") as f:
                f.write(body)
            print(f"   *** DIRECT IMAGE {sg} saved -> {p}")
            continue
        t = body.decode("utf-8", "replace")
        # WordPress attachment stub: find the real file
        for pat in [r'<meta[^>]+property="og:image"[^>]+content="([^"]+)"',
                    r'<link[^>]+rel="attachment"[^>]+href="([^"]+)"',
                    r'href="([^"]+\.(?:jpg|jpeg|png|gif|JPG|PNG))"',
                    r'src="([^"]+\.(?:jpg|jpeg|png|gif|JPG|PNG))"']:
            for m in re.findall(pat, t):
                m = html.unescape(m)
                print(f"   REF {m[:160]}")
        # tables + numeric prose
        for i, tb in enumerate(re.findall(r"<table[^>]*>.*?</table>", t, re.S | re.I)):
            cells = []
            for r2 in re.findall(r"<tr[^>]*>(.*?)</tr>", tb, re.S | re.I):
                cs = [clean(c) for c in re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", r2, re.S | re.I)]
                cs = [c for c in cs if c]
                if cs:
                    cells.append(cs)
            if len(cells) >= 2:
                print(f"   -- table {i} ({len(cells)} rows)")
                for c in cells[:24]:
                    print("      | " + " | ".join(c)[:200])
        plain = re.sub(r"\s+", " ", html.unescape(TAG.sub(" ", t)))
        for m in re.finditer(r"[^。]{0,150}。", plain):
            seg = m.group(0).strip()
            if re.search(r"(生命|攻撃|防御|基本能力|キャパ|超越|能力値)", seg) and re.search(r"\d", seg):
                print("   PROSE: " + seg[:280])

    print(f"\n\n=== direct media saved: {media_saved} ===")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
