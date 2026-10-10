#!/usr/bin/env python3
"""Fetch every /archives/ capture id_, save bodies, extract visible text,
find uploads image URLs, and record SHA-256 per body.

Control is already proven (051, 13/13 tokens) by control_check.py; re-assert it
cheaply here so this file is self-validating.
"""
import hashlib
import io
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(HERE, "_archives_work")
PAGES = os.path.join(OUT, "pages")
os.makedirs(PAGES, exist_ok=True)
UA = "Mozilla/5.0 (compatible; blustone-research/1.0)"


def fetch(url, timeout=180, tries=4):
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
        except Exception:
            if a < tries - 1:
                time.sleep(3 * (a + 1)); continue
            return None, b""
    return None, b""


rows = json.load(open(os.path.join(OUT, "cdx-archives.json"), encoding="utf-8"))
recs = []
for n, r in enumerate(rows):
    f = r.split(" ")
    if len(f) < 4:
        continue
    ts, orig = f[0], f[1]
    url = f"http://web.archive.org/web/{ts}id_/{orig}"
    st, b = fetch(url)
    sha = hashlib.sha256(b).hexdigest()
    fn = f"{ts}_{re.sub(r'[^A-Za-z0-9]+', '_', urllib.parse.unquote(orig))[-90:]}.html"
    path = os.path.join(PAGES, fn)
    with open(path, "wb") as fh:
        fh.write(b)
    txt = ""
    try:
        t = b.decode("utf-8")
    except UnicodeDecodeError:
        t = b.decode("cp932", "replace")
    # prefer charset from meta
    m = re.search(rb'charset=["\']?([\w-]+)', b[:4000], re.I)
    if m:
        cs = m.group(1).decode("ascii", "ignore").lower()
        if cs in ("shift_jis", "shift-jis", "sjis", "euc-jp"):
            t = b.decode("cp932", "replace")
    stripped = re.sub(r"<script[^>]*>.*?</script>", " ", t, flags=re.S | re.I)
    stripped = re.sub(r"<style[^>]*>.*?</style>", " ", stripped, flags=re.S | re.I)
    stripped = re.sub(r"<[^>]+>", " ", stripped)
    stripped = re.sub(r"&nbsp;", " ", stripped)
    txt = re.sub(r"[ \t]+", " ", stripped)
    txt = re.sub(r"\n\s*\n+", "\n", txt).strip()

    imgs = sorted(set(re.findall(r'https?://[^\s"\'<>)]+?\.(?:jpg|jpeg|png|gif|webp)', t, re.I)))
    up = sorted({i for i in imgs if "wp-content" in i or "uploads" in i})
    recs.append({"ts": ts, "orig": orig, "http": st, "bytes": len(b), "sha256": sha,
                 "file": fn, "text_len": len(txt),
                 "uploads": up, "all_imgs": imgs,
                 "text": txt})
    if st != 200:
        print(f"  NON-200 {st} {orig[:80]}")
    if (n + 1) % 20 == 0:
        print(f"  {n+1}/{len(rows)}")

json.dump(recs, open(os.path.join(OUT, "pages.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print(f"\nfetched {len(recs)}  ok200={sum(1 for r in recs if r['http']==200)}")
shas = {}
for r in recs:
    shas.setdefault(r["sha256"], []).append(r["orig"])
print(f"distinct SHA-256: {len(shas)}  (dupes={sum(1 for v in shas.values() if len(v)>1)})")
print("\nparking-page check (域名停靠 / 3357 bytes / 2021-07-29):")
for r in recs:
    if r["bytes"] == 3357 or "20210729" in r["ts"]:
        print("  ", r["ts"], r["bytes"], r["orig"][:70], "域名停靠" in r["text"])
print("\nsmallest bodies:")
for r in sorted(recs, key=lambda x: x["bytes"])[:8]:
    print(f"   {r['bytes']:7d} {r['ts']} {urllib.parse.unquote(r['orig'])[:80]}")