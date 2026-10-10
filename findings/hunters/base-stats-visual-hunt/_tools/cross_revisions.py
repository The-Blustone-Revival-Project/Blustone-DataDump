#!/usr/bin/env python3
"""Cross the full vsfan revision inventory against the prior lane's ledger.

The ledger in vsfan-wiki-2026-10-05.md §1.4 recorded ONE capture per page
(299 pages). The archive holds 8,887 /wiki/ revision rows over 1,231 titles,
so the vast majority of revisions were NEVER retrieved.

This prints, for every title with >1 archived revision, the timestamps and
whether the prior lane read that exact timestamp.
"""
import json
import re
import sys
from collections import defaultdict

LEDGER = r"C:\Users\shaha\Documents\ChatGPT\Blustone\analysis\research\base-stats-visual-hunt\vsfan-wiki-2026-10-05.md"


def load_ledger_timestamps():
    with open(LEDGER, encoding="utf-8") as f:
        txt = f.read()
    # rows look like: | `Page` | oldid | 2019-08-21 02:51:53Z | ... |
    ts = set()
    for m in re.finditer(r"\|\s*`([^`]+)`\s*\|\s*(\d+)\s*\|\s*(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2})Z", txt):
        page, oldid, d, t = m.groups()
        ts.add(page + "@" + d.replace("-", "") + t.replace(":", ""))
    return ts


def main(inv_path):
    with open(inv_path, encoding="utf-8") as f:
        inv = json.load(f)
    led = load_ledger_timestamps()
    print(f"ledger rows parsed: {len(led)}")

    # Titles that are plausibly hero pages: a 200 html row exists and the title
    # has no '/' (i.e. is a plain article, not a subpage).
    heroish = {}
    for title, recs in inv.items():
        if not title or "/" in title or ":" in title:
            continue
        ok = [r for r in recs if r["status"] == "200" and "text/html" in r["mime"]]
        if ok:
            heroish[title] = sorted(ok, key=lambda r: r["ts"])

    multi = {t: v for t, v in heroish.items() if len(v) > 1}
    print(f"plain article titles with >=1 HTML-200 capture: {len(heroish)}")
    print(f"   ...of which with >1 capture: {len(multi)}")

    unread_total = 0
    print("\n=== TITLES WITH >1 ARCHIVED CAPTURE (never-all-read by prior lane) ===")
    rows = []
    for t, v in sorted(multi.items(), key=lambda kv: kv[0].lower()):
        stamps = [r["ts"] for r in v]
        read = [s for s in stamps if t + "@" + s in led]
        unread = [s for s in stamps if t + "@" + s not in led]
        unread_total += len(unread)
        rows.append((t, stamps, len(read), len(unread)))
    for t, stamps, nread, nunread in rows:
        flag = "  <== MULTI" if nunread > 0 else ""
        print(f"  {t[:52]:52s} caps={len(stamps)} read={nread} UNREAD={nunread}")
        print(f"      {stamps}{flag}")
    print(f"\nTOTAL unread (title,timestamp) captures on multi-capture articles: {unread_total}")

    with open(sys.argv[2] if len(sys.argv) > 2 else "multi_capture_articles.txt",
              "w", encoding="utf-8", newline="\n") as f:
        for t, stamps, nread, nunread in rows:
            f.write(f"{t}\t{len(stamps)}\t{nread}\t{nunread}\t{','.join(stamps)}\n")


if __name__ == "__main__":
    main(sys.argv[1])
