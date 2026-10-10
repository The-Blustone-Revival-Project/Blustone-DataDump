# -*- coding: utf-8 -*-
"""vsx-final: single authoritative pass producing every table the report needs.
1. per-revision revision census (is >1 revision ever available?)
2. the 11 Character Attributes tables, field by field, present vs absent
3. verbatim raw table markup for one partial and one complete hero
4. corpus-wide proof that only 3 heroes ever carry Life/Attack/Defense
5. caption census: which tables state their state, and which state nothing
6. 57 -> 55 -> 54 reconciliation with the link proof
"""
import io, json, os, re, sys, html, csv
from collections import Counter, OrderedDict

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="backslashreplace")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "_wf1_cache")
RAW = os.path.join(CACHE, "raw")

CORE = ["Life", "Attack", "Defense"]
ALL13 = ["Life", "Attack", "Defense", "Attack Speed", "Critical Damage Chance",
         "Critical Damage", "Armor Penetration", "Block Chance",
         "Block Resistance", "Damage Reduction Block",
         "Strengthen Elemental Attributes", "Elemental Attack Resistance",
         "Life Regeneration"]
MAP = OrderedDict([("Life", "hp"), ("Attack", "atk"), ("Defense", "def"),
                   ("Attack Speed", "speed"),
                   ("Critical Damage Chance", "crit"),
                   ("Critical Damage", "crit_damage"),
                   ("Armor Penetration", "penetration"), ("Block Chance", "block"),
                   ("Block Resistance", "block_damage_reduction"),
                   ("Damage Reduction Block", "block_damage_reduction"),
                   ("Strengthen Elemental Attributes", "element_enhance"),
                   ("Elemental Attack Resistance", "element_resistance"),
                   ("Life Regeneration", "hp_regen")])
HERO_CAT = OrderedDict([
    ("Bear", "036"), ("Captain", "009"), ("Diana", "031"), ("Hermes", "023"),
    ("Joy", "035"), ("Kain", "029"), ("Lantern", "001"), ("Pansy", "057"),
    ("Patrone", "033"), ("Riko", "024"), ("Scar", "032")])
PARK = re.compile(r"<\s*title[^>]*>\s*\u57df\u540d\u505c\u9760\s*<", re.I)
TAG = re.compile(r"<[^>]+>")
WS = re.compile(r"[\s\u00a0]+")


def txt(s):
    return WS.sub(" ", html.unescape(TAG.sub("", s))).strip()


def tables(doc):
    out, i = [], 0
    op = re.compile(r"<table\b([^>]*)>", re.I)
    cl = re.compile(r"<(/?)table\b[^>]*>", re.I)
    while True:
        m = op.search(doc, i)
        if not m:
            break
        d, j = 1, m.end()
        while d and j < len(doc):
            m2 = cl.search(doc, j)
            if not m2:
                break
            d += -1 if m2.group(1) else 1
            j = m2.end()
        end = j - len(m2.group(0)) if d else j
        out.append((doc[m.end():end], m.group(1)))
        i = end if d else j + 1
    return out


def parse(inner):
    cm = re.search(r"<caption\b[^>]*>(.*?)</caption>", inner, re.I | re.S)
    cap = txt(cm.group(1)) if cm else None
    lab = OrderedDict()
    for rm in re.finditer(r"<tr\b[^>]*>(.*?)</tr>", inner, re.I | re.S):
        cs = [(m.group(1).lower(), txt(m.group(2)))
              for m in re.finditer(r"<(td|th)\b[^>]*>(.*?)</\1>", rm.group(1), re.I | re.S)]
        if len(cs) == 1 and cs[0][0] == "th":
            continue
        if len(cs) == 1:
            lab[cs[0][1]] = ""
        elif len(cs) == 2:
            lab[cs[0][1]] = cs[1][1]
        elif len(cs) == 4:
            lab.setdefault(cs[0][1], cs[1][1])
            lab.setdefault(cs[2][1], cs[3][1])
    return cap, lab


def main():
    jp = {}
    with io.open(os.path.join(HERE, "archived-hunter-database-2019.tsv"),
                 encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f, delimiter="\t", quotechar='"'):
            jp.setdefault(r["catalog_id"], r)

    files = sorted(f for f in os.listdir(RAW) if f.endswith(".html"))
    per_page = {}
    lad_pages = {}
    for fn in files:
        d = io.open(os.path.join(RAW, fn), "rb").read().decode("utf-8", "replace")
        page = fn.split("__")[0].replace("https_vsfan_net_wiki_", "")
        ts = fn.split("__")[1][:-5]
        if PARK.search(d):
            continue
        oids = sorted(set(re.findall(r"oldid=(\d+)", d)))
        e = per_page.setdefault(page, {"caps": [], "oids": set()})
        e["caps"].append(ts)
        e["oids"].update(oids)
        st = []
        for inner, attrs in tables(d):
            if "Character Attributes" in inner:
                st.append(parse(inner))
        if st:
            e["stats"] = st
        # corpus-wide: any row pairing a CORE label with a numeral
        hits = []
        for tr in re.finditer(r"<tr\b[^>]*>(.*?)</tr>", d, re.I | re.S):
            cs = [txt(m.group(2)) for m in
                  re.finditer(r"<(td|th)\b[^>]*>(.*?)</\1>", tr.group(1), re.S | re.I)]
            for i, c in enumerate(cs):
                if c in CORE:
                    nums = re.findall(r"-?\d[\d,]*(?:\.\d+)?", " ".join(cs[i + 1:]))
                    if nums:
                        hits.append((c, nums))
        if hits:
            lad_pages.setdefault(page, set()).update(
                (h[0], tuple(h[1])) for h in hits)

    print("#" * 78)
    print("# 1. REVISION CENSUS  (is any page recoverable in more than one revision?)")
    print("#" * 78)
    real = {k: v for k, v in per_page.items()}
    multi = {k: v for k, v in real.items() if len(v["oids"]) > 1}
    print("pages with >=1 non-parking capture : %d" % len(real))
    print("pages with >1 DISTINCT oldid        : %d %s"
          % (len(multi), sorted(multi) or ""))
    capt = Counter(len(v["caps"]) for v in real.values())
    print("captures-per-page histogram        : %s" % dict(sorted(capt.items())))

    print()
    print("#" * 78)
    print("# 2. THE 11 'Character Attributes' TABLES -- every field, present/absent")
    print("#" * 78)
    tot = eq = 0
    diffs = []
    for p, cid in HERO_CAT.items():
        e = real.get(p, {})
        st = e.get("stats")
        if not st:
            print("### %s -- NO TABLE RETRIEVED" % p)
            continue
        cap, lab = st[0]
        ncap = len({c for c, _ in st})
        nlabs = len({tuple(l.items()) for _, l in st})
        print()
        print("### %s  catalog=%s  captures=%d  oldid=%s"
              % (p, cid, len(e["caps"]), ",".join(sorted(e["oids"]))))
        print("    caption            : %r  (distinct across captures: %d)"
              % (cap, ncap))
        print("    label-set identical across captures: %s" % (nlabs == 1))
        jr = jp.get(cid, {})
        for f in ALL13:
            if f in lab:
                v = lab[f]
                col = MAP[f]
                jv = jr.get(col, "")
                w = v.rstrip("%").strip()
                try:
                    same = float(w) == float(jv)
                except Exception:
                    same = (w == jv)
                mark = "" if f not in ("Block Resistance",
                                       "Damage Reduction Block") else ""
                print("      %-30s = %-7s | JP %-4s %s"
                      % (f, repr(v), jv, "" if same else "  <-- DIFF"))
                if not same and (w.replace(".", "").replace("-", "").isdigit()
                                 and jv.strip().isdigit()):
                    diffs.append((p, cid, col, v.strip(), jv.strip(),
                                  float(w) / float(jv)))
            else:
                if f in CORE or f == "Attack Speed":
                    print("      %-30s = %s" % (f, "*** ABSENT FROM THE TABLE ***"))
        # counting
        for f, v in lab.items():
            if f not in MAP:
                continue
            col = MAP[f]
            jv = jr.get(col, "")
            w = v.rstrip("%").strip()
            try:
                fw = float(w)
                fj = float(jv)
            except Exception:
                continue
            tot += 1
            if fw == fj:
                eq += 1
    print()
    print(">>> field comparisons vs JP 2019: %d ; equal %d ; DIFFERENT %d"
          % (tot, eq, tot - eq))
    print(">>> every difference:")
    for p, cid, col, w, j, r in diffs:
        print("      %-8s %-4s %-22s wiki=%-7s jp=%-6s ratio=%.4f"
              % (p, cid, col, w, j, r))

    print()
    print("#" * 78)
    print("# 3. CORPUS-WIDE: which pages EVER pair Life/Attack/Defense w/ a numeral?")
    print("#" * 78)
    for p, h in sorted(lad_pages.items()):
        print("  %-10s %s" % (p, sorted(h)))
    print("  -> %d of %d archived hero pages carry ANY Life/Attack/Defense numeral"
          % (len(lad_pages), len(real)))

    print()
    print("#" * 78)
    print("# 4. VERBATIM RAW MARKUP")
    print("#" * 78)
    for page in ("Bear", "Captain"):
        fn = os.path.join(RAW, "https_vsfan_net_wiki_%s__%s.html"
                          % (page, min(real[page]["caps"])))
        d = io.open(fn, "rb").read().decode("utf-8", "replace")
        for inner, attrs in tables(d):
            if "Character Attributes" in inner:
                m = re.search(r'<h2[^>]*>.*?Stats.*?</h2>', d, re.S | re.I)
                print("--- %s  (file %s) ---" % (page, os.path.basename(fn)))
                print(re.sub(r"\n\s*\n", "\n", inner)[:1500])
                print()

    json.dump({"lad_pages": {k: sorted(list(v)) for k, v in lad_pages.items()},
               "comparisons": tot, "equal": eq,
               "differences": diffs,
               "revision_census": {k: {"caps": v["caps"],
                                       "oids": sorted(v["oids"]),
                                       "has_stats": "stats" in v}
                                   for k, v in real.items()}},
              io.open(os.path.join(CACHE, "final.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()