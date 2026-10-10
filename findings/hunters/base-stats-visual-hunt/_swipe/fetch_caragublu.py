"""Fetch the two Caragublu Blustone articles and download the largest available
image variant of every embedded image, so the originals can actually be viewed.
"""
import html as htmlmod
import os
import re
import sys
import time
import urllib.parse
import urllib.request

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "caragublu")
PAGES = [
    ("guide", "https://www.caragublu.com/2018/12/blustone-game-guide.html"),
    ("anime", "https://www.caragublu.com/2018/12/blustone-game-anime-action-rpg.html"),
]
CONTROL = "https://example.com/"


def get(url, tries=4, timeout=60):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) research"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, r.read()
        except Exception as e:  # noqa: BLE001
            err = e
            time.sleep(2 + 2 * i)
    return None, repr(err).encode()


def main():
    os.makedirs(OUT, exist_ok=True)
    st, b = get(CONTROL)
    print("CONTROL %s -> status=%s bytes=%d" % (CONTROL, st, len(b)))
    if st != 200 or len(b) < 100:
        print("CONTROL FAILED -> abort")
        sys.exit(2)

    for tag, url in PAGES:
        st, b = get(url)
        print("%s: status=%s bytes=%d" % (tag, st, len(b)))
        if st != 200:
            continue
        html = b.decode("utf-8", "replace")
        with open(os.path.join(OUT, "%s.html" % tag), "wb") as f:
            f.write(b)
        # collect img srcs, including blogger CDN /2-w/ and /s1600/ forms
        srcs = re.findall(r'<img[^>]+src="([^"]+)"', html)
        seen = []
        for s in srcs:
            s = htmlmod.unescape(s)
            if s not in seen:
                seen.append(s)
        print("  %d unique img srcs" % len(seen))
        n = 0
        for s in seen:
            base = re.sub(r"/s\d+(-c)?/", "/", s)
            base = re.sub(r"/w\d+(-h\d+)?/", "/", base)
            base = re.sub(r"/s\d{2,4}(?:-c)?/", "/", base)
            m = re.search(r"/([^/]+)$", base)
            if not m:
                continue
            name = m.group(1)
            if not re.search(r"\.(jpg|jpeg|png|gif|webp)$", name, re.I):
                continue
            fname = "%s-%s" % (tag, name)
            dest = os.path.join(OUT, fname)
            if os.path.exists(dest) and os.path.getsize(dest) > 20000:
                print("  skip (have) %s %d" % (fname, os.path.getsize(dest)))
                continue
            ok = False
            for variant in ("/s1600/", "/s1000/", "/s800/", ""):
                u = base.replace("/images/", variant + "images/") if variant else base
                st2, d = get(u)
                if st2 == 200 and len(d) > 20000 and not d.startswith(b"<!DOCTYPE"):
                    with open(dest, "wb") as f:
                        f.write(d)
                    print("  GOT %-52s %8d  %s" % (fname, len(d), variant or "(orig)"))
                    ok = True
                    break
            if not ok:
                print("  MISS %-50s %s" % (fname, s))
            n += 1
    print("done")


if __name__ == "__main__":
    main()
