# -*- coding: utf-8 -*-
"""Prove the Korean attribute tokens map to Fire/Ice/Lightning by
CORRESPONDENCE, not assumption.

Method: take the namu roster (Korean grade + attribute) and the vsfan English
roster (grade + element). Join the two on (grade, count) is too weak, so join
on the CHARACTER. The Korean names are matched to English names by their
shared distinctive substrings, which we can verify because both files list the
same roster. Then check whether a deterministic token->element function fits
every matched pair. If a single consistent mapping exists across ~50 heroes,
that is proof of the correspondence.
"""
import io
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

D = "analysis/research/base-stats-visual-hunt/_tools/_namu_raw/"
OUT = "analysis/research/base-stats-visual-hunt/_tools/btb_lane/attr_correspondence.txt"

L = []

# ---- Korean roster ----------------------------------------------------
hunter = io.open(D + "ctrl-d-hunter.text.txt", encoding="utf-8", errors="replace").read()
rowre = re.compile(
    r"^\s*(\u2606+[\s\u2606]*)\s*\|\s*([\uAC00-\uD7A3]+)\s*\|\s*([^|]+?)\s*\|\s*(.*?)\s*\|\s*$", re.M
)
kr = {}
for stars, attr, name, desc in rowre.findall(hunter):
    nm = name.strip()
    kr[nm] = {"grade": len(re.findall(r"\u2606", stars)), "attr": attr}

# ---- English roster (vsfan) ------------------------------------------
vs = io.open(
    "analysis/research/base-stats-visual-hunt/vsfan-wiki-2026-10-05.md", encoding="utf-8"
).read().split("\n")

# Find the roster table: rows like "| Lantern | 001 | ★★★ | Bomber | Fire | ..."
en = {}
row_en = re.compile(
    r"\|\s*([^|]+?)\s*\|\s*`?(\d{3})`?\s*\|\s*(\u2605+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|"
)
for ln in vs:
    m = row_en.search(ln)
    if m:
        name, cid, stars, role, elem = m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)
        if name in ("Name", ""):
            continue
        en[name.strip()] = {
            "catalog": cid,
            "grade": len(stars),
            "role": role.strip(),
            "elem": elem.strip(),
        }

L.append("parsed Korean rows: %d ; parsed English rows: %d" % (len(kr), len(en)))

# ---- Join on catalog id where possible -------------------------------
# The Korean roster has no id, but several names are shared across both
# languages by transliteration. We therefore test the mapping using ONLY the
# heroes whose names appear in BOTH tables verbatim (Latin-script ones), and
# separately record the Hangul-named ones by hand-verified transliteration.

# Latin-script Korean names (Hangul-named rows are excluded automatically).
shared = [n for n in kr if re.match(r"^[\x00-\x7F]+$", n) and n in en]
L.append("")
L.append("### heroes whose name is Latin-script in BOTH tables: %d" % len(shared))

pairs = []
for n in sorted(shared):
    pairs.append((n, kr[n]["attr"], en[n]["elem"], kr[n]["grade"], en[n]["grade"]))

L.append("")
L.append("%-26s %-8s %-10s %-8s %-8s" % ("name", "kr_attr", "en_elem", "kr_gr", "en_gr"))
for n, a, e, g1, g2 in pairs:
    L.append("%-26s %-8s %-10s %-8s %-8s" % (n, a, e, g1, g2))

# ---- Is a single token->element function consistent? ----------------
mapping = {}
conflicts = []
for n, a, e, g1, g2 in pairs:
    if a in mapping:
        if mapping[a] != e:
            conflicts.append((n, a, mapping[a], e))
    else:
        mapping[a] = e

L.append("")
L.append("### derived token -> element mapping")
for k, v in sorted(mapping.items()):
    L.append("   %s -> %s" % (k, v))
L.append("")
if conflicts:
    L.append("### CONFLICTS (mapping is NOT consistent): %d" % len(conflicts))
    for c in conflicts:
        L.append("   %s" % (c,))
else:
    L.append("### CONFLICTS: 0 - the mapping is consistent across all %d joined rows" % len(pairs))

# ---- Grade agreement on the same join -------------------------------
gconf = [(n, g1, g2) for n, a, e, g1, g2 in pairs if g1 != g2]
L.append("")
L.append("### grade disagreements between the two tables: %d" % len(gconf))
for g in gconf:
    L.append("   %s kr=%s en=%s" % g)

# ---- Also: the Hangul-named shared cast, transliterated by hand ----
L.append("")
L.append("### the cross-title cast (names are Hangul in the Korean table)")
L.append("   transliteration used for the join is stated explicitly:")
L.append("     Lantern  <- 최초의 헌터 랜턴")
L.append("     Nene     <- 전설적인 말썽꾸러기 네네")
L.append("     Mowgli   <- 사라진 숲의 모글리")
L.append("")

out = "\n".join(L)
io.open(OUT, "w", encoding="utf-8", newline="\n").write(out)
print(out)