"""Re-parse the saved wiki captures. The table rows carry TWO label/value pairs
per <tr>, so a regex that stops after one pair silently drops Attack and
Attack Speed. This parser walks every <tr> and returns all cell values in order.

It also records, for the 8 heroes the previous pass called "partial", the exact
proof that no Life/Attack/Defense cell exists in ANY archived revision.
"""
import glob
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
W = os.path.join(HERE, "wiki")

LABELS = ["Life", "Attack", "Defense", "Attack Speed",
          "Critical Damage Chance", "Critical Damage", "Armor Penetration",
          "Block Chance", "Block Resistance", "Damage Reduction Block",
          "Strengthen Elemental Attributes",
          "Elemental Attack Resistance", "Life Regeneration"]

TR = re.compile(r"<tr[^>]*>(.*?)</tr>", re.S | re.I)
TD = re.compile(r"<t[dh][^>]*>(.*?)</t[dh]>", re.S | re.I)
TAGS = re.compile(r"<[^>]+>")


def cell(t):
    t = re.sub(r"<style.*?</style>", "", t, flags=re.S | re.I)
    t = TAGS.sub("", t)
    t = t.replace("&nbsp;", " ").replace("&#160;", " ").replace("&amp;", "&")
    return re.sub(r"\s+", " ", t).strip()


def main():
    out = {}
    for p in sorted(glob.glob(os.path.join(W, "*.html"))):
        base = os.path.basename(p)[:-5]
        hero, ts = base.rsplit("-", 1)
        html = open(p, encoding="utf-8", errors="replace").read()
        cap = re.search(r"<caption>(.*?)</caption>", html, re.S | re.I)
        caption = re.sub(r"\s+", " ", cell(cap.group(1))) if cap else None
        # Locate the wikitable that contains "Character Attributes"
        tables = re.findall(r"<table[^>]*wikitable.*?</table>", html, re.S | re.I)
        rows = None
        for t in tables:
            if "Character Attributes" in t:
                rows = []
                for tr in TR.findall(t):
                    cells = [cell(c) for c in TD.findall(tr)]
                    cells = [c for c in cells if c != ""]
                    if cells:
                        rows.append(cells)
                break
        if rows is None:
            out.setdefault(hero, {})[ts] = {"caption": caption,
                                           "table": None, "error": "no stat table"}
            continue
        # pair label->value in document order
        flat = {}
        order = []
        for r in rows:
            i = 0
            while i + 1 < len(r):
                lab = r[i]
                val = r[i + 1]
                if lab in LABELS:
                    flat.setdefault(lab, val)
                    order.append(lab)
                i += 2
        out.setdefault(hero, {})[ts] = {
            "caption": caption,
            "rows": rows,
            "flat": flat,
            "has_LAD": all(k in flat for k in ("Life", "Attack", "Defense")),
        }
    for hero in sorted(out):
        for ts in sorted(out[hero]):
            d = out[hero][ts]
            print("== %s  @%s  caption=%r  has_LAD=%s"
                  % (hero, ts, d.get("caption"), d.get("has_LAD")))
            if d.get("flat"):
                for k in ["Life", "Attack", "Defense", "Attack Speed"]:
                    if k in d["flat"]:
                        print("     %-22s %s" % (k, d["flat"][k]))
    with open(os.path.join(W, "_parsed.json"), "w", encoding="utf-8",
              newline="\n") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    print("\nwrote _parsed.json")


if __name__ == "__main__":
    main()
