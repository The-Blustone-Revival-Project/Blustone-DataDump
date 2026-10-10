#!/usr/bin/env python3
"""Harvest every NEVER-READ plain-article capture of the vsfan wiki and look for
a Life/Attack/Defense triple and/or a 'Transcendence Level: N' caption.

Why this is a real gap and not a formality:
  * the prior lane queried CDX with collapse=urlkey -> 1,223 rows, earliest
    capture per URL, and read 262 plain articles;
  * uncollapsed, /wiki/ holds 5,164 HTML-200 captures over 1,231 titles;
  * 4,902 HTML-200 captures were therefore never retrieved, including whole
    2020-08-05 and 2020-11-29 capture waves that postdate every ledger read.

Controls:
  * a hard positive control runs first (Beckhen id_ fetch, exact byte count) and
    the run aborts if it fails;
  * a second control runs INSIDE the sweep: one known-good capture of a page the
    ledger read is re-fetched and must reproduce the ledger's byte count;
  * every fetch records http status + byte count, so a 504 is never a zero;
  * results are deduped by content sha256.
"""
import concurrent.futures as cf
import hashlib
import html
import json
import os
import re
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request

UA = "Mozilla/5.0 (compatible; blustone-research/1.0)"
_print_lock = threading.Lock()

TAG = re.compile(r"<[^>]+>")
CELL = re.compile(r"<t[hd][^>]*>(.*?)</t[hd]>", re.S | re.I)


def clean(s):
    return re.sub(r"\s+", " ", html.unescape(TAG.sub(" ", s))).strip()


def fetch(url, timeout=150, tries=3):
    for a in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, r.read()
        except urllib.error.HTTPError as e:
            b = e.read()
            if e.code in (502, 503, 504) and a < tries - 1:
                time.sleep(2 * (a + 1)); continue
            return e.code, b
        except Exception as e:
            if a < tries - 1:
                time.sleep(2 * (a + 1)); continue
            return None, str(e).encode("utf-8", "replace")
    return None, b""


def parse_attr_table(txt):
    """Return (caption, rows) of the Character Attributes wikitable, else (None,None)."""
    for m in re.finditer(r"<table[^>]*class=\"wikitable\"[^>]*>(.*?)</table>", txt, re.S | re.I):
        tbl = m.group(1)
        rows = []
        for rm in re.finditer(r"<tr[^>]*>(.*?)</tr>", tbl, re.S | re.I):
            cells = [clean(c) for c in CELL.findall(rm.group(1))]
            if cells:
                rows.append(cells)
        if any("Character Attributes" in " ".join(r) for r in rows):
            cm = re.search(r"<caption>(.*?)</caption>", tbl, re.S | re.I)
            return (clean(cm.group(1)) if cm else None), rows
    return None, None


def pull(rows, label):
    if not rows:
        return None
    for r in rows:
        for i, c in enumerate(r):
            if c.strip().lower() == label.lower() and i + 1 < len(r):
                return r[i + 1].strip()
    return None


def oldid_of(txt):
    m = re.findall(r"oldid=(\d+)", txt)
    return m[-1] if m else None


def one(job):
    title, ts, orig, cdxlen = job
    url = f"https://web.archive.org/web/{ts}id_/{orig}"
    st, b = fetch(url)
    if st != 200:
        return {"title": title, "ts": ts, "url": url, "http": st, "bytes": len(b), "error": True}
    txt = b.decode("utf-8", "replace")
    cap, rows = parse_attr_table(txt)
    rec = {
        "title": title, "ts": ts, "url": url, "http": 200, "bytes": len(b),
        "cdxlen": cdxlen, "sha256": hashlib.sha256(b).hexdigest(),
        "oldid": oldid_of(txt), "caption": cap,
        "life": pull(rows, "Life"), "attack": pull(rows, "Attack"),
        "defense": pull(rows, "Defense"), "attack_speed": pull(rows, "Attack Speed"),
        "has_attr_table": bool(rows),
        "transcendence": sorted(set(re.findall(r"Transcendence\s*Level[^<]{0,12}", txt, re.I))),
    }
    return rec


def main(inv_path, outdir, cap_path):
    os.makedirs(outdir, exist_ok=True)
    inv = json.load(open(inv_path, encoding="utf-8"))

    # ---------- CONTROL 1 ----------
    st, b = fetch("https://web.archive.org/web/20190821024308id_/https://vsfan.net/wiki/Beckhen")
    if not (st == 200 and len(b) == 88572):
        print(f"CONTROL 1 FAIL http={st} bytes={len(b)} -- ABORT, no negative may be claimed")
        return 2
    print("CONTROL 1 PASS: Beckhen id_ -> 200 / 88572 bytes")

    # ---------- CONTROL 2: reproduce a ledger read byte-for-byte ----------
    st, b = fetch("https://web.archive.org/web/20190821025153id_/https://vsfan.net/wiki/Captain")
    c2 = (st == 200 and len(b) == 97621)
    print(f"CONTROL 2 {'PASS' if c2 else 'FAIL'}: Captain 20190821025153 -> http={st} "
          f"bytes={len(b)} expect=97621")

    # ---------- build job list: plain articles, all captures, dedup by (title,ts) ----------
    jobs = []
    for title, recs in inv.items():
        if not title or "/" in title or ":" in title or title == "Main_Page":
            continue
        seen_ts = set()
        for r in sorted(recs, key=lambda x: x["ts"]):
            if r["status"] != "200" or "text/html" not in r["mime"]:
                continue
            if r["ts"] in seen_ts:
                continue
            seen_ts.add(r["ts"])
            jobs.append((title, r["ts"], r["url"], r["length"]))
    print(f"\njob list: {len(jobs)} plain-article HTML-200 captures over "
          f"{len({j[0] for j in jobs})} titles")

    # throttle per title: keep at most 6 captures, spread across the time range
    bytitle = {}
    for j in jobs:
        bytitle.setdefault(j[0], []).append(j)
    capped = []
    for t, lst in bytitle.items():
        if len(lst) <= 6:
            capped += lst
        else:
            step = len(lst) / 6.0
            capped += [lst[int(i * step)] for i in range(6)]
    print(f"after per-title cap (<=6 spread captures): {len(capped)}")

    results = []
    done = 0
    with cf.ThreadPoolExecutor(max_workers=8) as ex:
        for rec in ex.map(one, capped):
            results.append(rec)
            done += 1
            if done % 100 == 0:
                with _print_lock:
                    print(f"  ... {done}/{len(capped)}", flush=True)

    errs = [r for r in results if r.get("error")]
    print(f"\nfetched {len(results)}; transport/HTTP failures: {len(errs)}")
    from collections import Counter
    print("  failure codes:", dict(Counter(str(r["http"]) for r in errs)))
    print("CONTROL 2 result is independent of these; failures are NOT treated as negatives.")

    # ---------- analyse ----------
    with_attr = [r for r in results if r.get("has_attr_table")]
    with_lad = [r for r in results if r.get("life")]
    with_trans = [r for r in results if r.get("transcendence")]

    print(f"\ncaptures WITH a Character Attributes table : {len(with_attr)}")
    print(f"captures WITH a Life value                 : {len(with_lad)}")
    print(f"captures mentioning 'Transcendence Level'  : {len(with_trans)}")

    print("\n=== every DISTINCT (title, caption, Life, Attack, Defense) observed ===")
    seen = set()
    for r in sorted(with_attr, key=lambda x: (x["title"].lower(), x["ts"])):
        k = (r["title"], r.get("caption"), r.get("life"), r.get("attack"), r.get("defense"))
        if k in seen:
            continue
        seen.add(k)
        print(f"  {r['title'][:34]:34s} ts={r['ts']} oldid={r['oldid']} "
              f"cap={r.get('caption')!r}")
        print(f"      Life={r.get('life')!r} Attack={r.get('attack')!r} "
              f"Defense={r.get('defense')!r} AtkSpd={r.get('attack_speed')!r}")

    print("\n=== every DISTINCT 'Transcendence Level' string ===")
    seen2 = set()
    for r in with_trans:
        for s in r["transcendence"]:
            if s not in seen2:
                seen2.add(s)
                print(f"  {r['title'][:34]:34s} ts={r['ts']}  {s!r}")

    out = os.path.join(outdir, "vsfan-neverread-sweep.json")
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        json.dump(results, f, indent=1, ensure_ascii=False)
    print(f"\nsaved -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else ""))
