"""Namu mirror fetcher. namu.wiki 403s; m/d/dark.namu.moe work with a browser UA.
Search term is sliced out of the URL-encoded request (GUARD 13: never hand-write
codepoints for a search term)."""
import html
import re
import sys
import time
import urllib.parse
import urllib.request

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
MIRRORS = ["https://m.namu.moe", "https://d.namu.moe", "https://dark.namu.moe"]


def get(path, tries=3, timeout=60):
    last = None
    for i in range(tries):
        for m in MIRRORS:
            try:
                req = urllib.request.Request(
                    m + path, headers={"User-Agent": UA, "Accept-Language": "ko,en;q=0.8",
                                       "Referer": m + "/"})
                with urllib.request.urlopen(req, timeout=timeout) as r:
                    return r.read().decode("utf-8", "replace")
            except Exception as e:  # noqa: BLE001
                last = e
        time.sleep(2 * (i + 1))
    raise last


def doc(name):
    return get("/w/" + urllib.parse.quote(name))


def text(h):
    h = re.sub(r"<script.*?</script>", " ", h, flags=re.S)
    h = re.sub(r"<style.*?</style>", " ", h, flags=re.S)
    h = re.sub(r"<[^>]+>", "\n", h)
    return html.unescape(h)


def links(h):
    out = set()
    for m in re.finditer(r'href="(/w/[^"#?]+)"', h):
        out.add(urllib.parse.unquote(m.group(1)))
    return out


if __name__ == "__main__":
    name = sys.argv[1]
    h = doc(name)
    print("LEN", len(h))
    t = text(h)
    t = re.sub(r"\n{2,}", "\n", t)
    sys.stdout.reconfigure(encoding="utf-8")
    print(t[: int(sys.argv[2]) if len(sys.argv) > 2 else 6000])
    print("=" * 40, "LINKS")
    for l in sorted(links(h)):
        print(l)
