#!/usr/bin/env python3
"""Dump the readable text of an archived Naver-cafe post body, so numerals in
prose or table cells can be read verbatim rather than inferred."""
import html
import re
import sys
import time
import urllib.error
import urllib.request

UA = "Mozilla/5.0 (compatible; blustone-research/1.0)"


def fetch(url, timeout=180, tries=5):
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


def strip_quoted(t):
    # Naver cafe bodies are quoted-printable with soft line breaks
    t = re.sub(r"=\r?\n", "", t)
    try:
        t = t.encode("latin-1", "ignore").decode("utf-8", "ignore")
    except Exception:
        pass
    return t


def main():
    url = sys.argv[1]
    st, b = fetch(url)
    print(f"http={st} bytes={len(b)}  {url}")
    if st != 200:
        return 1
    t = strip_quoted(b.decode("utf-8", "replace"))

    # Isolate the article body if we can, else whole page.
    m = re.search(r'id="naver_cafegoods_tarea_?[^\"]*"(.*?)</div>', t, re.S | re.I)
    body = m.group(1) if m else t
    if not m:
        m2 = re.search(r'<div[^>]*class="[^"]*posting_view[^"]*"[^>]*>(.*)', t, re.S | re.I)
        if m2:
            body = m2.group(1)

    print("\n================ TABLES (verbatim cells) ================")
    for i, tb in enumerate(re.findall(r"<table[^>]*>.*?</table>", body, re.S | re.I)):
        cells = re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", tb, re.S | re.I)
        txt = [re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", c))).strip() for c in cells]
        txt = [c for c in txt if c]
        if len(txt) > 3:
            print(f"\n-- table {i}:")
            for c in txt:
                print("   | " + c)

    print("\n================ BODY TEXT ================")
    plain = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", body, flags=re.S | re.I)
    plain = re.sub(r"<br\s*/?>", "\n", plain, flags=re.I)
    plain = re.sub(r"</(p|div|tr|h\d|li)>", "\n", plain, flags=re.I)
    plain = re.sub(r"<[^>]+>", " ", plain)
    plain = html.unescape(plain)
    lines = [re.sub(r"[ \t ]+", " ", l).strip() for l in plain.split("\n")]
    for l in lines:
        if l:
            print("  " + l[:400])
    return 0


if __name__ == "__main__":
    sys.exit(main())
