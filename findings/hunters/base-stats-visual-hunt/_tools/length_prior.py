#!/usr/bin/env python3
"""Cheap prior: which vsfan pages actually CHANGED between archived revisions?

Rationale: the only way a T1/T2 (or T4) stat table can exist is if some
revision of some page carries a Life/Attack/Defense row or a
'Transcendence Level: 1/2/4' caption that the revision the prior lane read does
not. Fetching 4,902 never-read captures is slow, so rank by CDX `length`
delta first: a page whose archived WARC length varies a lot across captures is
a page whose content changed, and only those are worth fetching.

CDX `length` is the COMPRESSED WARC record length, so it is a proxy, not the
content size -- but a large spread means real change.
"""
import json
import re
import sys
import urllib.parse
from collections import defaultdict

LEDGER = r"C:\Users\shaha\Documents\ChatGPT\Blustone\analysis\research\base-stats-visual-hunt\vsfan-wiki-2026-10-05.md"


def ledger_map():
    """page -> (oldid, cdxlen, timestamp)"""
    txt = open(LEDGER, encoding="utf-8").read()
    out = {}
    for m in re.finditer(
            r"\|\s*`([^`]+)`\s*\|\s*(\d+)\s*\|\s*(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2})Z\s*\|\s*(\d+)\s*\|",
            txt):
        page, oldid, d, t, ln = m.groups()
        out[urllib.parse.unquote(page)] = {
            "oldid": oldid,
            "cdxlen": int(ln),
            "ts": d.replace("-", "") + t.replace(":", ""),
        }
    return out


def main(inv_path, out_tsv):
    inv = json.load(open(inv_path, encoding="utf-8"))
    led = ledger_map()
    print(f"ledger rows parsed: {len(led)}")

    changed, stable, novel = [], [], []
    for title, recs in inv.items():
        if not title or "/" in title or ":" in title or title == "Main_Page":
            continue
        caps = [r for r in recs if r["status"] == "200" and "text/html" in r["mime"]]
        if not caps:
            continue
        lens = sorted({r["length"] for r in caps})
        stamps = sorted({r["ts"] for r in caps})
        L = led.get(title)
        if L is None:
            novel.append((title, stamps, lens))
            continue
        spread = (max(lens) - min(lens)) / max(1, L["cdxlen"])
        rec = {
            "title": title, "n_caps": len(caps), "ledger_cdxlen": L["cdxlen"],
            "ledger_ts": L["ts"], "ledger_oldid": L["oldid"],
            "min_len": min(lens), "max_len": max(lens), "spread": spread,
            "stamps": stamps, "all_lens": lens,
        }
        if L["cdxlen"] not in lens or spread > 0.01:
            changed.append(rec)
        else:
            stable.append(rec)

    print(f"\npages with an HTML-200 capture:")
    print(f"  read by prior lane, content UNCHANGED across captures : {len(stable)}")
    print(f"  read by prior lane, content CHANGED / len missing     : {len(changed)}")
    print(f"  NEVER read at all (no ledger row)                     : {len(novel)}")

    print("\n=== CHANGED pages, ranked by length spread (top 60) ===")
    for r in sorted(changed, key=lambda x: -x["spread"])[:60]:
        print(f"  {r['spread']*100:6.1f}%  {r['title'][:44]:44s} ledger_len={r['ledger_cdxlen']:>6d} "
              f"caps={r['n_caps']} lens={r['all_lens'][:6]}")

    print("\n=== NEVER-READ pages (top 40 by n captures) ===")
    for t, s, l in sorted(novel, key=lambda x: -len(x[1]))[:40]:
        print(f"  caps={len(s):2d}  {t[:50]:50s} {s[:4]} lens={l[:5]}")

    with open(out_tsv, "w", encoding="utf-8", newline="\n") as f:
        for r in sorted(changed, key=lambda x: -x["spread"]):
            f.write(f"{r['spread']:.4f}\t{r['title']}\t{r['n_caps']}\t{r['ledger_cdxlen']}\t"
                    f"{r['min_len']}\t{r['max_len']}\t{','.join(r['stamps'])}\n")
    print(f"\nsaved changed-page list -> {out_tsv}  ({len(changed)} rows)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
