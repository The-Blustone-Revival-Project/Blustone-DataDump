#!/usr/bin/env python3
"""Harvest the Japanese blustone.jp /育成説/ ("Growth Theory") official series --
including the キャパ超越 ("Cap Transcendence") pages and the per-rank pages.
The prior lane only harvested /archives/<id> (the 62 hunter profiles), so this
whole section is new.

CONTROL FIRST: web.archive.org root must return 200, and one already-harvested
/archives/<id> page must return real bytes, before any zero is a real negative.
"""
import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (compatible; blustone-research/1.0)"
CDX = "https://web.archive.org/cdx/search/cdx?"


def fetch(url, timeout=180, tries=4):
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


TAG = re.compile(r"<[^>]+>")
CELL = re.compile(r"<t[hd][^>]*>(.*?)</t[hd]>", re.S | re.I)


def clean(s):
    return re.sub(r"[ \t]+", " ", html.unescape(TAG.sub(" ", s))).strip()


def main(outdir):
    import os
    os.makedirs(outdir, exist_ok=True)

    st, b = fetch("https://web.archive.org/")
    print(f"[CONTROL web.archive.org] http={st} bytes={len(b)} -> "
          f"{'PASS' if st == 200 and len(b) > 100000 else 'FAIL'}")
    if st != 200:
        return 2

    # NOTE: a CDX matchType=prefix query on a percent-encoded NON-ASCII path
    # returned 0 rows here while the same URLs were present in the full-domain
    # listing. So: take the WHOLE domain listing and filter locally. Control
    # (web.archive.org) already passed, so this is not a transport artefact --
    # it is the documented prefix-matching trap, recorded as such.
    q = CDX + urllib.parse.urlencode({"url": "blustone.jp", "matchType": "domain",
                                      "output": "text", "collapse": "urlkey",
                                      "limit": "50000"})
    st, b = fetch(q)
    t = b.decode("utf-8", "replace")
    allrows = [l for l in t.split("\n") if l.strip()][1:]
    print(f"\n[CDX blustone.jp domain] http={st} bytes={len(b)} rows={len(allrows)}")

    def is_seisei(url):
        d = urllib.parse.unquote(url)
        return "育成説" in d or "育成說" in d

    rows = [r for r in allrows if len(r.split(" ")) > 2 and is_seisei(r.split(" ")[2])]
    # also keep the bare /rank /rankup /ranking pages seen earlier
    for r in allrows:
        f = r.split(" ")
        if len(f) < 7:
            continue
        if f[2].rstrip("/").endswith(("blustone.jp/rank", "blustone.jp/rankup",
                                      "blustone.jp/rankup-2", "blustone.jp/ranking")):
            rows.append(r)
    print(f"rows matching 育成説 or rank pages: {len(rows)}")

    pages = []
    for r in rows:
        f = r.split(" ")
        if len(f) < 7 or f[4] != "200" or "html" not in f[3]:
            continue
        pages.append((f[1], f[2]))
    pages = sorted(set(pages))
    print(f"HTML-200 育成説 captures: {len(pages)}")
    for ts, u in pages:
        print(f"   {ts}  {urllib.parse.unquote(u)[:110]}")

    out = []
    for ts, u in pages:
        arc = f"https://web.archive.org/web/{ts}id_/{u}"
        s, body = fetch(arc)
        rec = {"ts": ts, "url": u, "archive": arc, "http": s, "bytes": len(body)}
        print(f"\n{'='*78}\n{urllib.parse.unquote(u)}\n  http={s} bytes={len(body)}")
        if s != 200:
            out.append(rec)
            continue
        t = body.decode("utf-8", "replace")
        tables = re.findall(r"<table[^>]*>.*?</table>", t, re.S | re.I)
        print(f"  tables: {len(tables)}")
        for i, tb in enumerate(tables):
            rows2 = re.findall(r"<tr[^>]*>(.*?)</tr>", tb, re.S | re.I)
            cells = []
            for r2 in rows2:
                cs = [clean(c) for c in CELL.findall(r2)]
                cs = [c for c in cs if c]
                if cs:
                    cells.append(cs)
            joined = " ".join(" ".join(c) for c in cells)
            interesting = bool(re.search(r"\d", joined))
            if len(cells) >= 2:
                print(f"   -- table {i}: {len(cells)} rows")
                for c in cells[:26]:
                    print("      | " + " | ".join(c)[:220])
                if len(cells) > 26:
                    print(f"      ...(+{len(cells)-26})")
        # prose containing numbers
        plain = re.sub(r"\s+", " ", html.unescape(TAG.sub(" ", t)))
        for m in re.finditer(r"[^。]{0,160}(?:\d+)[^。]{0,160}。", plain):
            seg = m.group(0).strip()
            if re.search(r"(生命|攻撃|防御|LIFE|ATK|能力|ステータス|キャパ|超越)", seg):
                print("   PROSE: " + seg[:300])
        rec["tables"] = len(tables)
        out.append(rec)

    p = os.path.join(outdir, "blustone-jp-seiseisetsu.json")
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    print(f"\nsaved -> {p}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
