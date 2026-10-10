# -*- coding: utf-8 -*-
"""Numeric census of the rendered namu 헌터 page, with a positive control.

Purpose: decide honestly whether the page carries any per-hero HP/ATK/DEF
numbers, without concluding that from a skim. The control proves the detector
fires on numbers that ARE present.
"""
import io
import os
import re
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

TXT = os.path.join(os.environ.get("TEMP", "."), "namu_hunter.txt")
HTML = os.path.join(os.environ.get("TEMP", "."), "namu_hunter.html")

# Korean stat words a per-hero stat line would have to use.
STAT_WORDS = ["체력", "생명력", "공격력", "방어력", "공격 속도", "막기", "관통력",
              "스탯", "능력치", "인연 보너스"]
NUM = re.compile(r"\d[\d,]*\.?\d*%?")


def main():
    txt = io.open(TXT, encoding="utf-8").read()
    lines = txt.split("\n")

    # --- positive control: lines that DO carry numbers must be found
    ctrl_hits = [l for l in lines if NUM.search(l)]
    print("POSITIVE CONTROL")
    print("  lines containing a numeric token: %d" % len(ctrl_hits))
    for l in ctrl_hits[:3]:
        print("    ok: " + l.strip()[:90])

    # --- target: numeric lines that ALSO mention a stat word
    stat_hits = [l for l in lines
                 if any(w in l for w in STAT_WORDS) and NUM.search(l)]
    print("STAT-WORD + NUMBER lines: %d" % len(stat_hits))
    for l in stat_hits:
        print("    " + l.strip()[:400])

    # --- bare numeric census on the four role tables only
    print("\nBARE NUMERIC TOKENS on role-table rows (per-hero numeric check):")
    n = 0
    for l in lines:
        if not l.startswith("r"):
            continue
        body = l.split("|", 1)[1] if "|" in l else l
        # drop the grade column (leading star glyphs) and the trailing prose
        toks = NUM.findall(body)
        # a trace-like / count-like token inside the name or description cell
        n += len([t for t in toks if len(t.replace(",", "").rstrip("%")) >= 1])
    print("  numeric tokens across role-table rows: %d" % n)

    # --- explicit search for a three-stat pattern (HP/ATK/DEF style)
    triple = re.compile(r"(체력|생명력)[^\d\n]{0,20}\d[^\n]{0,40}(공격력)[^\d\n]{0,20}\d[^\n]{0,40}(방어력)[^\d\n]{0,20}\d")
    print("HP+ATK+DEF triple patterns: %d" % len(triple.findall(txt)))

    # --- images: any could be an unread stat table, so count them
    html = io.open(HTML, encoding="utf-8").read()
    imgs = re.findall(r"<img\b[^>]*>", html)
    alts = re.findall(r'<img[^>]*alt="([^"]*)"', html)
    srcs = [s for s in re.findall(r'<img[^>]*\ssrc="([^"]*)"', html)]
    print("\nIMAGES: total=%d  with alt=%d  distinct-src=%d" %
          (len(imgs), len(alts), len(set(srcs))))
    caps = [a for a in alts if re.search(r"20\d\d-\d\d", a)]
    print("  alt values that look like capture screenshots: %d" % len(caps))
    for a in sorted(set(caps))[:20]:
        print("    " + a)


if __name__ == "__main__":
    main()
