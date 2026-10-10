"""Fetch the share_en post 440600 Google Doc (FAQ for learners/semi experienced)
and decode its base64-embedded images.

Read-only w.r.t. everything except the local _swipe/ scratch dir.
Uses Python urllib (no PowerShell string writing).
"""
import base64
import hashlib
import os
import re
import sys
import time
import urllib.error
import urllib.request

DOC = "1O_xdOZqplSVw2XczV2nEl2_wvEZaOc_Mm9RFIY2qaXc"
BASE = "https://docs.google.com/document/d/%s/export?format=%%s" % DOC
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gdoc")

# Positive control: a URL that must return real bytes. Google Docs itself is the
# control for the txt endpoint; for the html endpoint we assert the byte count and
# that base64 image payloads exist at all (see main()).
CONTROL = "https://docs.google.com/document/d/%s/export?format=txt" % DOC


def fetch(url, tries=6, timeout=120):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) research",
                "Accept": "*/*",
            })
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, r.read()
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(2 + 3 * i)
    return None, repr(last).encode()


def main():
    os.makedirs(OUT, exist_ok=True)

    # ---- control / text ----
    st, body = fetch(CONTROL)
    print("CONTROL txt: status=%s bytes=%d" % (st, len(body)))
    if st != 200 or len(body) < 10000:
        print("CONTROL FAILED -> abort, zeros would be uninterpretable")
        sys.exit(2)
    with open(os.path.join(OUT, "faq.txt"), "wb") as f:
        f.write(body)
    print("  wrote faq.txt sha256=%s" % hashlib.sha256(body).hexdigest()[:16])

    # ---- html ----
    st, body = fetch(BASE % "html")
    print("html: status=%s bytes=%d" % (st, len(body)))
    if st != 200 or len(body) < 100000:
        print("HTML FETCH FAILED -> abort")
        sys.exit(3)
    html = body.decode("utf-8", "replace")
    with open(os.path.join(OUT, "faq.html"), "wb") as f:
        f.write(body)

    # Google export format=html wraps images as:
    #   <img alt="" src="data:image/png;base64,....." />
    pat = re.compile(r'src="data:image/(png|jpeg|jpg|gif);base64,([A-Za-z0-9+/=]+)"')
    hits = pat.findall(html)
    print("embedded base64 images found: %d" % len(hits))
    if len(hits) < 20:
        print("TOO FEW IMAGES -> abort (expected 28)")
        sys.exit(4)

    manifest = []
    for n, (ext, b64) in enumerate(hits, start=1):
        raw = base64.b64decode(b64)
        name = "faq_%02d.%s" % (n, "jpg" if ext in ("jpeg", "jpg") else ext)
        p = os.path.join(OUT, name)
        with open(p, "wb") as f:
            f.write(raw)
        # dimensions without PIL
        dims = "?"
        if raw[:8] == b"\x89PNG\r\n\x1a\n":
            w = int.from_bytes(raw[16:20], "big")
            h = int.from_bytes(raw[20:24], "big")
            dims = "%dx%d" % (w, h)
        elif raw[:2] == b"\xff\xd8":
            i = 2
            w = h = None
            while i < len(raw) - 9:
                if raw[i] != 0xFF:
                    i += 1
                    continue
                m = raw[i + 1]
                if m in (0xC0, 0xC1, 0xC2, 0xC3):
                    h = int.from_bytes(raw[i + 5:i + 7], "big")
                    w = int.from_bytes(raw[i + 7:i + 9], "big")
                    break
                if m in (0xD8, 0x01) or 0xD0 <= m <= 0xD7:
                    i += 2
                    continue
                seg = int.from_bytes(raw[i + 2:i + 4], "big")
                i += 2 + seg
            if w:
                dims = "%dx%d" % (w, h)
        manifest.append((name, len(raw), dims,
                         hashlib.sha256(raw).hexdigest()))
        print("  %-12s %8d  %-12s %s" % (name, len(raw), dims,
                                         manifest[-1][3][:16]))

    with open(os.path.join(OUT, "_manifest.txt"), "w",
              encoding="utf-8", newline="\n") as f:
        for name, n, dims, h in manifest:
            f.write("%s\t%d\t%s\t%s\n" % (name, n, dims, h))
    print("OK: %d images decoded" % len(manifest))


if __name__ == "__main__":
    main()
