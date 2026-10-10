#!/usr/bin/env python3
"""Compute the set of vsfan (title, timestamp) HTML-200 captures that the prior
lane NEVER read, and separate them from the 299 ledger rows.

Critical method note: the prior lane queried CDX with collapse=urlkey, which
returns only the EARLIEST capture per URL. The archive holds 8,887 revision
rows over 1,231 titles. So every LATER capture of every page was silently
discarded -- including any revision that added the Life/Attack/Defense rows.
"""
import json
import re
import sys
from collections import defaultdict

LEDGER = r"C:\Users\shaha\Documents\ChatGPT\Blustone\analysis\research\base-stats-visual-hunt\vsfan-wiki-2026-10-05.md"


def ledger_stamps():
    with open(LEDGER, encoding="utf-8") as f:
        txt = f.read()
    out = set()
    for m in re.finditer(r"\|\s*`([^`]+)`\s*\|\s*(\d+)\s*\|\s*(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2})Z", txt):
        page, oldid, d, t = m.groups()
        out.add((urllib_unquote(page), d.replace("-", "") + t.replace(":", "")))
    return out


def urllib_unquote(s):
    import urllib.parse
    return urllib.parse.unquote(s)


def main(inv_path, out_tsv):
    inv = json.load(open(inv_path, encoding="utf-8"))
    led = ledger_stamps()
    print(f"ledger (title,ts) pairs: {len(led)}")

    read = []
    unread = []
    byyear = defaultdict(int)
    for title, recs in inv.items():
        if not title:
            continue
        for r in recs:
            if r["status"] != "200" or "text/html" not in r["mime"]:
                continue
            key = (title, r["ts"])
            (read if key in led else unread).append((title, r["ts"], r["length"]))
            byyear[r["ts"][:4]] += 1

    print(f"HTML-200 captures in inventory: {len(read)+len(unread)}")
    print(f"  READ by prior lane : {len(read)}")
    print(f"  NEVER READ         : {len(unread)}")
    print("  HTML-200 by year:", dict(sorted(byyear.items())))

    # The single most important subset: pages whose EARLIEST archived capture
    # is LATER than the one the ledger read -> the ledger read an earlier rev
    # and the later rev is new information. Plus: any capture from 2020+, since
    # the ledger's newest capture is 2020-08-08.
    led_by_title = defaultdict(list)
    for t, ts in led:
        led_by_title[t].append(ts)
    newer_only = []
    for title, ts, ln in unread:
        if led_by_title.get(title):
            newer_only.append((title, ts, ln))
    print(f"\nNEVER-READ captures of a page the ledger DID read: {len(newer_only)}")

    rows = sorted(set((t, ts, ln) for t, ts, ln in unread), key=lambda x: (x[0].lower(), x[1]))
    with open(out_tsv, "w", encoding="utf-8", newline="\n") as f:
        for t, ts, ln in rows:
            f.write(f"{ts}\t{ln}\t{t}\n")
    print(f"saved never-read list -> {out_tsv}  ({len(rows)} rows)")

    # Titles with the most never-read captures first (highest yield).
    cnt = defaultdict(int)
    for t, ts, ln in rows:
        cnt[t] += 1
    print("\n=== titles with most NEVER-READ html-200 captures ===")
    for t, n in sorted(cnt.items(), key=lambda kv: -kv[1])[:40]:
        stamps = sorted(ts for tt, ts, _ in rows if tt == t)
        print(f"  {n:3d}  {t[:56]:56s} {stamps}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
