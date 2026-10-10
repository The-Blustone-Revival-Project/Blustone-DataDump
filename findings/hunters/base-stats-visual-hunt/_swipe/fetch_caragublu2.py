"""Retry the Caragublu images that the first pass mishandled.

Blogger image URLs embed the size as a path SEGMENT:
   .../AVvXsEgl.../s320-rw/Blustone+Hunter+Adcance.jpg
so the correct transform is to REPLACE that segment with /s1600/, not to
delete it. The first pass deleted it, which produced a 404 for every image.
"""
import html as htmlmod
import os
import re
import time
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "caragublu")
# Control = the article itself. An earlier version used https://example.com/ but
# the anti-HTML guard below correctly rejects HTML, so the control could never
# pass. The control must therefore be a non-HTML resource.
CONTROL = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgsW4OCZe3tWCiynR9UcJuuSXWExJxh_UEUZ2BWXhzR85IbTsLWSoW6kHz0WmcOLP8lEciNHjh-vgC7wW2xlw4ihSy9WAdK43XRmvvqY-Xce0Ia_AwuwEja0qCTUUIC6P7GUAu9rJiSGY12/s1600-rw/Upgrade+Equipment.jpg"


def get(url, tries=5, timeout=90, minsize=15000):
    err = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) research"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                d = r.read()
                if r.status == 200 and len(d) > minsize and not d.startswith(b"<!"):
                    return r.status, d
        except Exception as e:  # noqa: BLE001
            err = e
        time.sleep(1.5 + 2 * i)
    return None, repr(err).encode()


def main():
    st, b = get(CONTROL, tries=3, minsize=200)
    print("CONTROL status=%s bytes=%d" % (st, len(b)))
    if st != 200:
        print("CONTROL FAILED -> abort")
        return
    for tag in ("guide", "anime"):
        p = os.path.join(OUT, "%s.html" % tag)
        if not os.path.exists(p):
            continue
        h = open(p, encoding="utf-8").read()
        srcs = []
        for s in re.findall(r'<img[^>]+src="([^"]+)"', h):
            s = htmlmod.unescape(s)
            if s not in srcs:
                srcs.append(s)
        print("\n[%s] %d srcs" % (tag, len(srcs)))
        for s in srcs:
            m = re.search(r"/([^/]+)$", s)
            if not m or not re.search(r"\.(jpg|jpeg|png|gif|JPG)$", m.group(1), re.I):
                continue
            name = m.group(1)
            dest = os.path.join(OUT, "%s-%s" % (tag, name))
            if os.path.exists(dest) and os.path.getsize(dest) > 20000:
                print("  skip %s" % name)
                continue
            # replace the size segment /sNNN/ or /sNNN-rw/ with the wanted size
            def swap(mm):
                return "/" + mm.group(2) + ("-rw" if mm.group(1) else "") + "/"
            got = None
            for size in ("s1600", "s2000", "s1200", "s1000", "s800", "s0"):
                u = re.sub(r"/(s\d+)((?:-cw|\-h|-rw)?)/",
                           lambda mm: "/%s%s/" % (size, mm.group(2)), s)
                if size == "s0":
                    u = re.sub(r"/s\d+((?:-cw|\-h|-rw)?)/", r"/\1", s)
                st2, d = get(u, tries=3)
                if st2 == 200:
                    with open(dest, "wb") as f:
                        f.write(d)
                    print("  GOT  %-42s %8d  %s" % (name, len(d), size))
                    got = d
                    break
            if got is None:
                print("  MISS %-42s %s" % (name, s[:110]))


if __name__ == "__main__":
    main()
