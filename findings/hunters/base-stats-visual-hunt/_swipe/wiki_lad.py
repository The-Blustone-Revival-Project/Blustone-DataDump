"""The vsfan wiki has 11 hero `Character Attributes` tables; 8 lack the
Life/Attack/Defense rows. Those rows are absent from the wikitext of the
2019-08/09 captures. This script checks whether the Wayback Machine holds
OTHER captures of the same pages (an earlier/later revision) that DO contain
them.

Positive control first: the CDX API must return rows for a URL the previous
pass proved has captures.
"""
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "wiki")
CDX = ("http://web.archive.org/cdx/search/cdx?url=%s&matchType=exact"
       "&output=json&limit=200&collapse=timestamp:8")
CONTROL_URL = "vsfan.net/wiki/Bear"
HEROES = ["Bear", "Diana", "Joy", "Kain", "Lantern", "Pansy", "Patrone", "Scar",
          "Captain", "Hermes", "Riko"]


def fetch(url, tries=8, timeout=90, minsize=200):
    err = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) research"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                d = r.read()
                if r.status == 200 and len(d) > minsize:
                    return r.status, d
        except Exception as e:  # noqa: BLE001
            err = e
        time.sleep(2 + 3 * i)
    return None, repr(err).encode()


def cdx(urlkey):
    st, d = fetch(CDX % urllib.parse.quote(urlkey, safe=""), minsize=20)
    if st != 200:
        return None, d.decode("utf-8", "replace")
    try:
        j = json.loads(d.decode("utf-8", "replace"))
    except Exception as e:  # noqa: BLE001
        return None, "parse: %r" % (e,)
    if not j:
        return [], ""
    hdr = j[0]
    rows = [dict(zip(hdr, r)) for r in j[1:]]
    return rows, ""


ROW = re.compile(r"<tr>\s*<td>(Life|Attack|Defense|Attack Speed)</td>\s*"
                 r"<td[^>]*>([^<]*)</td>", re.I)
CAP = re.compile(r"<caption>(.*?)</caption>", re.S | re.I)


def main():
    os.makedirs(OUT, exist_ok=True)
    # ---- control ----
    rows, err = cdx(CONTROL_URL)
    ok = rows is not None and len(rows) > 0
    print("CONTROL cdx %s -> rows=%s %s" % (CONTROL_URL,
                                           len(rows) if rows is not None else err,
                                           "PASS" if ok else "FAIL"))
    if not ok:
        print("CONTROL FAILED -> abort; zeros would be uninterpretable")
        return 2

    summary = []
    for h in HEROES:
        uk = "vsfan.net/wiki/%s" % urllib.parse.quote(h)
        rows, err = cdx(uk)
        if rows is None:
            print("%-10s CDX ERROR %s" % (h, err[:60]))
            continue
        caps = sorted({r.get("timestamp", "")[:14] for r in rows})
        print("\n=== %s : %d rows, captures %s" % (h, len(rows), caps))
        found = {}
        for ts in caps:
            w = ("https://web.archive.org/web/%sid_/https://vsfan.net/wiki/%s"
                 % (ts, h))
            st, d = fetch(w, tries=6, minsize=3000)
            if st != 200:
                print("   %s  fetch %s bytes=%s" % (ts, st, len(d)))
                continue
            html = d.decode("utf-8", "replace")
            with open(os.path.join(OUT, "%s-%s.html" % (h, ts)), "wb") as f:
                f.write(d)
            m = CAP.search(html)
            cap = re.sub(r"\s+", " ", m.group(1)).strip() if m else "(no caption)"
            lad = {k: v.strip() for k, v in ROW.findall(html)}
            print("   %s  caption=%-24s LAD=%s" % (ts, cap, lad if lad else "{}"))
            found[ts] = (cap, lad)
            if lad:
                break        # found what we came for on this hero
            time.sleep(1)
        summary.append({"hero": h, "captures": caps,
                        "found": {k: v for k, v in found.items() if v[1]}})
    with open(os.path.join(OUT, "_lad.json"), "w", encoding="utf-8",
              newline="\n") as f:
        json.dump(summary, f, indent=1, ensure_ascii=False)
    print("\nwrote _lad.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
