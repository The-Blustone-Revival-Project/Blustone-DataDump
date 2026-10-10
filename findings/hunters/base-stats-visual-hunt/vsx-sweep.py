# -*- coding: utf-8 -*-
"""vsx-sweep: exhaustive, cell-aware sweep of EVERY cached revision.

Question: does ANY table anywhere in the archived wiki corpus contain a
Life / Attack / Defense (or synonym) LABEL paired with a NUMERAL, on any hero
page, in any surviving revision -- including in a table that is not the
'Character Attributes' table?

Approach: for every <table>, for every <tr>, pair each label cell with the
numerals that follow it in that row.  Reports label -> values found.
"""
import io, json, os, re, sys, html
from collections import OrderedDict, defaultdict

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "_wf1_cache", "raw")
TAG = re.compile(r"<[^>]+>")
WS = re.compile(r"[\s\u00a0]+")

# label -> canonical field.  Synonyms included so a relabelled wiki column
# cannot slip through unnoticed.
SYNONYMS = {
    "life": "hp", "hp": "hp", "health": "hp", "vitality": "hp",
    "stamina": "hp", "maximum life": "hp", "max life": "hp", "max hp": "hp",
    "attack": "atk", "atk": "atk", "atp": "atk", "attack power": "atk",
    "defense": "def", "def": "def", "defence": "def", "dr": "def",
}
NUMS = re.compile(r"-?\d[\d,]*(?:\.\d+)?")


def txt(s):
    return WS.sub(" ", html.unescape(TAG.sub("", s))).strip()


def cells(row):
    return [txt(m.group(2))
            for m in re.finditer(r"<(td|th)\b[^>]*>(.*?)</\1>", row, re.I | re.S)]


def main():
    files = sorted(f for f in os.listdir(RAW) if f.endswith(".html"))
    # Domain-parking pages: all 15 copies are byte-identical (sha256 prefix
    # bd97685e4e171255310be44c), 3357 bytes, 0 tables, <title>域名停靠</title>
    # ("domain parked") -- the 2021-07-29 post-mortem capture, not wiki content.
    PARK = re.compile(r"<\s*title[^>]*>\s*(?:&nbsp;|\s)*\u57df\u540d\u505c\u9760\s*<", re.I)
    stats = OrderedDict()
    park, real = [], 0
    for fn in files:
        b = io.open(os.path.join(RAW, fn), "rb").read()
        d = b.decode("utf-8", "replace")
        if PARK.search(d):
            park.append((fn, len(b)))
            continue
        real += 1
        page = fn.split("__")[0].replace("https_vsfan_net_wiki_", "")
        ts = fn.split("__")[1][:-5]
        found = defaultdict(list)
        # every row of every table, pairing a label cell with following numerals
        for tr in re.finditer(r"<tr\b[^>]*>(.*?)</tr>", d, re.I | re.S):
            cs = cells(tr.group(1))
            for i, c in enumerate(cs):
                key = SYNONYMS.get(c.strip().lower())
                if not key:
                    continue
                rest = " ".join(cs[i + 1:])
                nums = NUMS.findall(rest)
                if nums:
                    found[key].append((c.strip(), nums, " | ".join(cs)))
        if found:
            stats.setdefault(page, []).append({"ts": ts, "found": {k: v for k, v in found.items()}})

    with io.open(os.path.join(HERE, "_wf1_cache", "lad-sweep.json"), "w",
                 encoding="utf-8") as f:
        json.dump({"pages": stats, "parking": park}, f, ensure_ascii=False, indent=1)

    print("cached files            : %d" % len(files))
    print("domain-parking captures : %d  (excluded, no wiki content)" % len(park))
    print("real article captures   : %d" % real)
    print()
    print("pages where SOME row pairs a Life/Attack/Defense label with a numeral:")
    if not stats:
        print("   (none)")
    for page, revs in stats.items():
        print("### %-16s  %d capture(s)" % (page, len(revs)))
        seen = set()
        for r in revs:
            for k, vs in r["found"].items():
                for lab, nums, row in vs:
                    sig = (k, tuple(nums))
                    if sig in seen:
                        continue
                    seen.add(sig)
                    print("    %-4s %-10s -> %-12s   row: %s" % (r["ts"], k, ",".join(nums), row[:90]))
        # also confirm which capture had NO hit at all
        for r in revs:
            if not r["found"]:
                print("    %s  NO Life/Attack/Defense row with a numeral" % r["ts"])


if __name__ == "__main__":
    main()