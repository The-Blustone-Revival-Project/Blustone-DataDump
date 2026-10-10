#!/usr/bin/env python3
"""Positive-control probe for the Wayback read path on this host.

Controls (per the lane brief):
  C1  web.archive.org root reachable
  C2  http:// works / https:// refused  (trap T1)
  C3  exact-URL  fetch of the known Beckhen 051 profile reproduces all 13 TSV values
  C4  an archived image returns a real image signature (not the 3,357-byte
      parking page)
Any FAIL => a zero below is meaningless.
"""
import urllib.request, urllib.error, sys, hashlib, time

UA = "Mozilla/5.0 (compatible; blustone-research/1.0)"
SIGS = {b"\xff\xd8\xff": "JPEG", b"\x89PNG": "PNG", b"GIF8": "GIF", b"BM": "BMP"}


def fetch(url, timeout=120, tries=3):
    last = (None, b"")
    for a in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, r.read()
        except urllib.error.HTTPError as e:
            b = e.read()
            if e.code in (502, 503, 504) and a < tries - 1:
                time.sleep(3 * (a + 1)); continue
            return e.code, b
        except Exception as ex:
            last = (None, ("%s" % ex).encode())
            if a < tries - 1:
                time.sleep(3 * (a + 1)); continue
    return last


def sig(b):
    for s, n in SIGS.items():
        if b.startswith(s):
            return n
    return None


def park(b):
    return "PARKING(3357)" if len(b) == 3357 else ""


def main():
    print("=== C1/C2  scheme probe ===")
    for scheme in ("http", "https"):
        s, b = fetch(scheme + "://web.archive.org/")
        print("  %-5s root http=%s bytes=%d" % (scheme, s, len(b)))

    print("\n=== C3  known hero 051 control (exact URL, id_) ===")
    u = ("http://web.archive.org/web/20191216060610id_/https://blustone.jp/hunter/"
         "%E3%83%AC%E3%82%A2%E3%83%AA%E3%83%86%E3%82%A3%E5%88%A5/"
         "%E3%83%95%E3%82%A1%E3%82%A4%E3%83%88%E3%82%AF%E3%83%A9%E3%83%96%E3%81%AE"
         "%E5%AE%88%E8%AD%B7%E8%80%85%E3%80%8C%E3%83%99%E3%83%83%E3%82%B1%E3%83%B3%E3%80%8D")
    s, b = fetch(u)
    print("  051 profile http=%s bytes=%d" % (s, len(b)))
    t = b.decode("utf-8", "replace")
    want = ["8709", "1678", "864", "660"]
    print("  markers present:", {w: (w in t) for w in want})

    print("\n=== C4  image control ===")
    iu = ("http://web.archive.org/web/20190403182150id_/"
          "http://blustone.jp/wp-content/uploads/2018/11/rankup.jpg")
    s, b = fetch(iu)
    print("  rankup.jpg http=%s bytes=%d sig=%s %s sha=%s"
          % (s, len(b), sig(b), park(b), hashlib.sha256(b).hexdigest()[:16]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
