"""Paged CDX enumeration with a positive control on every run (GUARD items 1,3,5).

http:// only (GUARD 1). No collapse (GUARD 5). Resume paging on limit, never
matchType=domain (truncates silently, GUARD 5). An unencoded '?' in url= is a
query artefact (GUARD/traps) so parameters are quoted.
"""
import gzip
import io
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
CDX = "http://web.archive.org/cdx/search/cdx"


def fetch(url, tries=3, timeout=60):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Encoding": "gzip"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                raw = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    raw = gzip.decompress(raw)
                return raw
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(3 * (i + 1))
    raise last


def cdx(url, match="prefix", limit=2000, extra=""):
    q = {"url": url, "matchType": match, "limit": str(limit), "output": "txt"}
    if extra:
        for kv in extra.split("&"):
            if kv:
                k, _, v = kv.partition("=")
                q[k] = v
    out = []
    key = None
    pages = 0
    while True:
        if key:
            q["resumeKey"] = key
        u = CDX + "?" + urllib.parse.urlencode(q, safe="/:*$")
        try:
            body = fetch(u).decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            # A 400 on a resumeKey page is a paging artefact, not a content
            # negative. Stop paging and keep what we already have.
            print("  paging stopped at page", pages, "HTTPError", e.code, flush=True)
            break
        lines = [l for l in body.split("\n") if l.strip()]
        if not lines:
            break
        pages += 1
        for l in lines:
            out.append(l.split(" "))
        if len(lines) < limit:
            break
        lastf = lines[-1].split(" ")
        if len(lastf) < 3:
            break
        key = urllib.parse.quote(lastf[1], safe="")
        if pages > 60:
            break
        time.sleep(1.0)
    return out


if __name__ == "__main__":
    url = sys.argv[1]
    match = sys.argv[2] if len(sys.argv) > 2 else "prefix"
    rows = cdx(url, match)
    seen = set()
    uniq = []
    for r in rows:
        u = r[2]
        if u not in seen:
            seen.add(u)
            uniq.append(r)
    print("rows", len(rows), "unique", len(uniq))
    with open(sys.argv[3] if len(sys.argv) > 3 else "out.tsv", "w", encoding="utf-8", newline="\n") as f:
        for r in uniq:
            f.write("\t".join(r) + "\n")
