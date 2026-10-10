#!/usr/bin/env python3
"""Exhaustively probe the 6 attachment images of share_en post 215324
(Lana's Guidebook Ch. 8, Transcendence) -- the official before/after stat
screenshots for Diana's FIRST transcendence.

Paths tried per file:
  1. exact-URL CDX (every capture timestamp that exists)
  2. Wayback id_ (raw bytes) at each capture
  3. Wayback im_ (rewritten) at each capture
  4. the LIVE cafe host
  5. the ./relative form the cafe itself emits

CONTROL FIRST: an image the prior lane proved retrievable
(75605/303/534/001/725a8e...jpg -> 200 / 57,414 bytes, image/jpeg).
Without that PASS, no 404 below is a real negative.
"""
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (compatible; blustone-research/1.0)"
CDX = "https://web.archive.org/cdx/search/cdx?"

FILES = [
    "3d32517fe07a6e6e141c427f6d31b52f.jpg",
    "785fa1a1f60d180bf7f571c492535a5f.PNG",
    "dd43982990eaa77c7901d7e89dfd8b61.PNG",
    "f665e07c6f2a331d692dedee3439417a.PNG",
    "b9bddbea17d8be7e72bdf569a3b06e29.jpg",
    "3365176cc9964d2fd00c11e3d7e0653d.PNG",
]
BASE = "http://bs.visualshower.com/files/attach/images/565/324/215/"

CTRL = ("https://web.archive.org/web/20210903030305id_/http://bs.visualshower.com/"
        "files/attach/images/75605/303/534/001/725a8e175454a533e96dac68fc5fdb49.jpg")


def fetch(url, timeout=150, tries=4):
    for a in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, r.read(), r.headers.get("Content-Type", "")
        except urllib.error.HTTPError as e:
            b = e.read()
            if e.code in (502, 503, 504) and a < tries - 1:
                time.sleep(3 * (a + 1)); continue
            return e.code, b, ""
        except Exception:
            if a < tries - 1:
                time.sleep(3 * (a + 1)); continue
            return None, b"transport", ""
    return None, b"transport", ""


SIGS = {b"\xff\xd8\xff": "JPEG", b"\x89PNG": "PNG", b"GIF8": "GIF",
        b"BM": "BMP", b"\x00\x00\x01\x00": "ICO"}


def looks_like_image(b):
    for s, n in SIGS.items():
        if b.startswith(s):
            return n
    return None


def main(outdir):
    import os
    os.makedirs(outdir, exist_ok=True)

    st, b, ct = fetch(CTRL)
    ok = (st == 200 and len(b) == 57414)
    print(f"[CONTROL known-good image] http={st} bytes={len(b)} ct={ct} "
          f"sig={looks_like_image(b)} -> {'PASS' if ok else 'FAIL'}")
    if not ok:
        print("ABORT: control failed; nothing below is a negative.")
        return 2

    hits = 0
    for fn in FILES:
        url = BASE + fn
        print(f"\n########## {fn}")
        # 1. exact-URL CDX
        q = CDX + urllib.parse.urlencode({"url": url, "output": "text", "limit": "200"})
        st2, b2, _ = fetch(q)
        t = b2.decode("utf-8", "replace")
        rows = [l for l in t.split("\n") if l.strip()][1:]
        print(f"  CDX exact: http={st2} rows={len(rows)}")
        stamps = []
        for r in rows:
            f = r.split(" ")
            if len(f) < 7:
                continue
            print(f"     {f[1]} {f[3]} {f[4]} len={f[6]}  {f[2][:110]}")
            stamps.append((f[1], f[2]))

        # 2/3. fetch each capture in id_ and im_ form
        for ts, orig in stamps:
            for form in ("id_", "im_"):
                u = f"https://web.archive.org/web/{ts}{form}/{orig}"
                s, body, c = fetch(u)
                sig = looks_like_image(body)
                print(f"     {form} {ts}: http={s} bytes={len(body)} sig={sig} ct={c}")
                if sig and s == 200:
                    hits += 1
                    p = os.path.join(outdir, f"RECOVERED_{ts}_{form}_{fn}")
                    with open(p, "wb") as f:
                        f.write(body)
                    print(f"       *** SAVED {p}")

        # 4. live cafe host
        for scheme in ("http", "https"):
            s, body, c = fetch(f"{scheme}://bs.visualshower.com/files/attach/images/565/324/215/{fn}")
            sig = looks_like_image(body)
            print(f"     LIVE {scheme}: http={s} bytes={len(body)} sig={sig} ct={c}")
            if sig and s == 200:
                hits += 1
                p = os.path.join(outdir, f"LIVE_{scheme}_{fn}")
                with open(p, "wb") as f:
                    f.write(body)
                print(f"       *** SAVED {p}")

    print(f"\n\n=== IMAGES RECOVERED: {hits} ===")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
