# -*- coding: utf-8 -*-
"""Build the Lantern(001) / Nene(003) agreement table.

Three independent sources, compared field by field:
  A. namu.wiki (Korean community wiki, roster table: birth grade + attribute)
  B. vsfan English wiki (roster table: birth grade + role + element + race)
  C. the project's own shipped client (CHAR_STR prose + SKILL_TAG JOB_* tag)
  D. the 2019 JP archive (role_ja + element_ja + rarity_on_draw)

The Korean attribute tokens are read from the namu roster and translated only
by CORRESPONDENCE to the English elements that the SAME document uses in its
own elemental-cycle sentence - never by assumption.
"""
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

D = "analysis/research/base-stats-visual-hunt/_tools/_namu_raw/"
OUT = "analysis/research/base-stats-visual-hunt/_tools/btb_lane/agreement_table.txt"

L = []

# ---------- A. namu roster: grade + attribute for the shared cast --------
hunter = io.open(D + "ctrl-d-hunter.text.txt", encoding="utf-8", errors="replace").read()
rowre = re.compile(
    r"^\s*(\u2606+[\s\u2606]*)\s*\|\s*([\uAC00-\uD7A3]+)\s*\|\s*([^|]+?)\s*\|\s*(.*?)\s*\|\s*$", re.M
)
rows = rowre.findall(hunter)
attr_of = {}
grade_of = {}
for stars, attr, name, desc in rows:
    nm = name.strip()
    attr_of[nm] = attr
    grade_of[nm] = len(re.findall(r"\u2606", stars))

L.append("### A. namu roster (Korean), for the shared cast")
L.append("   grade = number of stars; attribute = the Korean attribute token")
L.append("")
for nm in sorted(attr_of):
    L.append("   %-28s grade=%d attribute=%s" % (nm, grade_of[nm], attr_of[nm]))

L.append("")
L.append("   distinct attribute tokens and their counts:")
toks = {}
for _, attr, _, _ in rows:
    toks[attr] = toks.get(attr, 0) + 1
for k, v in sorted(toks.items()):
    L.append("      %s = %d rows" % (k, v))

# ---------- attribute cycle sentence (pins the token meanings) ----------
main = io.open(D + "ctrl-d-main.text.txt", encoding="utf-8", errors="replace").read()
L.append("")
L.append("   the article's own elemental-cycle sentence:")
for m in re.finditer(r"[^\n]{0,120}\uD3A9\uBCF8\uC18C\uB7C9[^\n]{0,160}", main):
    L.append("      %s" % m.group(0).strip()[:300])

# ---------- B. vsfan English roster -------------------------------------
L.append("")
L.append("### B. vsfan English wiki roster rows (grade / role / element / race)")
vs = io.open(
    "analysis/research/base-stats-visual-hunt/vsfan-wiki-2026-10-05.md", encoding="utf-8"
).read().split("\n")
for i, ln in enumerate(vs):
    if re.search(r"\|\s*(Lantern|Nene|Mowgli|Leonardo)\s*\|", ln):
        L.append("   line %d: %s" % (i + 1, ln.strip()))

# ---------- C. project client -------------------------------------------
L.append("")
L.append("### C. the shipped client's own statements")
cs = io.open("analysis/recovered-data/leveldb-tables/char-str.tsv", encoding="utf-8").read().split("\n")
hdr = cs[0].split("\t")
for line in cs[1:]:
    f = line.split("\t")
    if f[0] in ("001", "002", "003"):
        L.append("   card %s" % f[0])
        for h, v in zip(hdr, f):
            if h in ("TITLE", "SUMMARY", "WEAPON"):
                L.append("      %-8s %s" % (h, v))

L.append("")
L.append("   job role tag per card (SKILL_TAG slot 3):")
st = io.open("analysis/recovered-data/leveldb-tables/skill-tag.tsv", encoding="utf-8").read().split("\n")
for line in st[1:]:
    f = line.split("\t")
    if f and f[0] in ("001", "002", "003") and f[1] == "3":
        L.append("      %s -> %s" % (f[0], f[2]))

tr = io.open("analysis/recovered-data/leveldb-tables/tag-ref.tsv", encoding="utf-8").read().split("\n")
L.append("   tag -> role dictionary:")
for line in tr[1:]:
    f = line.split("\t")
    if f and f[0].startswith("JOB_"):
        L.append("      %-10s %s" % (f[0], f[1]))

# ---------- D. JP archive ----------------------------------------------
L.append("")
L.append("### D. 2019 JP archive rows")
arch = io.open(
    "analysis/research/base-stats-visual-hunt/archived-hunter-database-2019.tsv", encoding="utf-8"
).read().split("\n")
ah = arch[0].split("\t")
for line in arch[1:]:
    if not line.strip():
        continue
    f = line.split("\t")
    if f[-3].strip('"') in ("001", "002", "003"):
        L.append("   catalog %s" % f[-3].strip('"'))
        for h, v in zip(ah, f):
            if h.strip('"') in ("listed_name", "role_ja", "element_ja", "rarity_on_draw"):
                L.append("      %-16s %s" % (h.strip('"'), v.strip('"')))

out = "\n".join(L)
io.open(OUT, "w", encoding="utf-8", newline="\n").write(out)
print(out)