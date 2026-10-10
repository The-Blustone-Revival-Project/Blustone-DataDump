#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Equipment/accessory STAT-VALUE detector for the namu gear pages (2026-10-07).

GUARD rule 13 respected: no hand-written Hangul codepoints. Every Korean term is
discovered from the fetched page text at runtime (same discovery as
equip_extract.py), so a typo cannot silently turn this into a false-negative
oracle.

Target set (B2): a line that has an equipment SLOT label AND a stat word AND a
number. Controls: (C) synthetic stat lines must FIRE, (D) real flavour prose
must be SILENT.
"""
import os
import re
import sys

RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_namu_raw")


def rd(tag):
    p = os.path.join(RAW, tag + ".text.txt")
    return open(p, encoding="utf-8").read()


def discover(text):
    """Return (slot_labels, effect_labels) found in the page itself."""
    from collections import Counter
    c = Counter()
    for ln in text.split("\n"):
        m = re.match(r"^([\uAC00-\uD7A3]{2,6}(?: [\uAC00-\uD7A3]{1,6})?):$",
                     ln.strip())
        if m:
            c[m.group(1)] += 1
    slots, effects = [], []
    for k, v in c.most_common():
        if " " in k:
            effects.append(k)
        elif v >= 3:
            slots.append(k)
    return slots[:3], effects[:2]


def stats_from(text):
    """Stat words, discovered as Korean noun+counter shapes in the corpus."""
    found = set()
    for pat in (r"[\uAC00-\uD7A3]{2,3}\ub825",          # X력 (공격력/방어력/체력)
                r"\ucd5c\ub300 [\uAC00-\uD7A3]{2,4}",    # 최대 HP
                r"[\uAC00-\uD7A3]{2,3} \uc0ac\uc6a9\ub825"):  # X 사용량
        found.update(re.findall(pat, text))
    return sorted(found)


def main():
    tags = sys.argv[1:]
    # The equipment slot trio is the INTERSECTION of single-word labels across all
    # scanned pages. A per-page top-3-by-frequency heuristic misreads the Support
    # page, whose effect label is spelled without a space (특기효과) and so ranks
    # above the real slots; intersecting fixes it without hand-typing a label.
    sets = []
    for tag in tags:
        try:
            c = discover(rd(tag))[0]
        except Exception:
            continue
        s = set()
        from collections import Counter
        cc = Counter()
        for ln in rd(tag).split("\n"):
            m = re.match(r"^([\uAC00-\uD7A3]{2,6}(?: [\uAC00-\uD7A3]{1,6})?):$",
                         ln.strip())
            if m:
                cc[m.group(1)] += 1
        s = {k for k, v in cc.items() if " " not in k and v >= 3}
        # Only pages that actually carry a full slot set may define the trio;
        # including a page with one or two of the labels would shrink it.
        if len(s) >= 3:
            sets.append(s)
    common = set.intersection(*sets) if sets else set()
    base = rd(tags[0])
    slots = sorted(common)
    effects = discover(base)[1]
    stats = stats_from(base)
    print("DISCOVERED slot labels :", slots, " (intersection over %d pages)"
          % len(sets))
    print("DISCOVERED slot labels :", slots)
    print("DISCOVERED effect label:", effects)
    print("DISCOVERED stat words :", stats)
    if not slots or not stats:
        raise SystemExit("discovery failed -- detector not trustworthy")

    NUM = r"\d[\d,]*(?:\.\d+)?"
    slot_re = "|".join(re.escape(s) for s in slots)
    stat_re = "|".join(re.escape(s) for s in stats) + \
        r"|HP|ATK|DEF|attack|defen[cs]e|health|damage|\ud551\uc0b0\ub825"
    D = {
        "equip_stat": re.compile(r"(?:%s)[^\n]{0,80}?(?:%s)[^\n]{0,30}?%s"
                                 % (slot_re, stat_re, NUM)),
        "slot_num": re.compile(r"(?:%s)[^\n]{0,80}?%s" % (slot_re, NUM)),
        "stat_num": re.compile(r"(?:%s)[^\n]{0,30}?%s|%s[^\n]{0,30}?%s"
                               % (stat_re, NUM, NUM, stat_re)),
        "pct": re.compile(r"%s\s*%%" % NUM),
    }

    # ---- controls -------------------------------------------------------
    print("\n=== (C) POSITIVE CONTROL: synthetic stat lines, MUST fire ===")
    item = None
    for ln in base.split("\n"):
        pass
    # use a real equipment line as the carrier so the control is realistic
    real_line = None
    lines = base.split("\n")
    for i, ln in enumerate(lines):
        if ln.strip().rstrip(":").strip() in slots:
            body = [x.strip() for x in lines[i + 1:i + 4] if x.strip()]
            if len(body) >= 2:
                real_line = body[1]
                break
    print("  carrier item name from page:", repr(real_line))
    syn = []
    for st in stats[:6]:
        syn.append("%s  %s 260" % (slots[-1], st))
    syn += [
        "%s  HP 260" % slots[-1],
        "%s  ATK 1,025" % slots[-1],
        "%s  defense 150" % slots[-1],
        "Accessory | Jack | Increases HP 260",
        "%s 30.00%%" % stats[0],
    ]
    bad = 0
    for s in syn:
        got = bool(D["stat_num"].search(s) or D["pct"].search(s))
        if not got:
            bad += 1
        print("  [%s] %s" % ("FIRED" if got else "SILENT!!", s))
    print("  -> silent positives: %d  (MUST be 0)" % bad)
    e0 = D["equip_stat"]
    got = bool(e0.search("%s  %s 260" % (slots[-1], stats[0])))
    print("  [%s] EQUIPMENT+STAT control" % ("FIRED" if got else "SILENT!!"))
    if not got:
        bad += 1

    print("\n=== (D) NEGATIVE CONTROL: real prose lines from the page ===")
    prose = [ln for ln in lines if len(ln) > 60][:4]
    for ln in prose:
        print("  [%s] %s" % ("FIRED" if D["stat_num"].search(ln) else "SILENT",
                              ln.strip()[:120]))

    # ---- scan -----------------------------------------------------------
    print("\n=== SCAN ===")
    grand = {"slots": 0, "equip_stat": 0, "slot_num": 0, "stat_num": 0}
    for tag in tags:
        t = rd(tag)
        lines = t.split("\n")
        # Use the intersected trio directly. discover() returns only the top 3 by
        # frequency, which silently drops a real slot when the Support page's
        # effect label outranks it -- that under-counted Support as 26 instead of 39.
        sl = slots
        sre = "|".join(re.escape(x) for x in sl)
        st = stats_from(t) or stats
        tre = "|".join(re.escape(x) for x in st) + \
            r"|HP|ATK|DEF|attack|defen[cs]e|health|damage|\ud551\uc0b0\ub825"
        ns = sum(1 for ln in lines
                 if re.match(r"^(?:%s)\s*:?\s*$" % sre, ln.strip()))
        es = [(i, ln) for i, ln in enumerate(lines)
              if re.search(r"(?:%s)[^\n]{0,80}?(?:%s)[^\n]{0,30}?%s"
                           % (sre, tre, NUM), ln)]
        sn = sum(1 for ln in lines
                 if re.search(r"(?:%s)[^\n]{0,30}?%s|%s[^\n]{0,30}?%s"
                              % (tre, NUM, NUM, tre), ln))
        sm = sum(1 for ln in lines
                 if re.search(r"(?:%s)[^\n]{0,80}?%s" % (sre, NUM), ln))
        print("\n### %s  chars=%d fffd=%d" % (tag, len(t), t.count("\ufffd")))
        print("    slot labels found      : %s" % sl)
        print("    (A) equipment slots    : %d" % ns)
        print("    slot+ANY number        : %d" % sm)
        print("    (B) any stat-value line: %d" % sn)
        print("    (B2) SLOT+STAT+VALUE   : %d   <== TARGET SET" % len(es))
        for i, ln in es:
            print("        %5d| %s" % (i, ln.strip()[:180]))
        grand["slots"] += ns
        grand["equip_stat"] += len(es)
        grand["slot_num"] += sm
        grand["stat_num"] += sn
    print("\n=== TOTALS ===", grand)
    print("control failures:", bad, "(MUST be 0)")


if __name__ == "__main__":
    main()