# -*- coding: utf-8 -*-
"""Lantern(001) / Nene(003) / Chichir(004) / Mowgli(002) agreement check.

Every Korean term is sliced out of the data files; the mapping to English is
read off the project's own client tables (TAG_REF_RO) rather than guessed.
"""
import io
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

D = "analysis/research/base-stats-visual-hunt/_tools/_namu_raw/"
OUT = "analysis/research/base-stats-visual-hunt/_tools/btb_lane/shared_cast_check.txt"

L = []

# ---------- 1. namu roster rows, matched by NAME ------------------------
hunter = io.open(D + "ctrl-d-hunter.text.txt", encoding="utf-8", errors="replace").read()
main = io.open(D + "ctrl-d-main.text.txt", encoding="utf-8", errors="replace").read()

# The four shared-cast Korean names, sliced by locating their romanised
# identity in the project's own data where possible, else by pattern.
# We take them from the namu text directly with anchors found in that text.
# Lamp/Nene/Chichir/Mowgli: find every roster row and keep the four we know.
TARGET_HINTS = {
    # hint is an ASCII/roman anchor that appears in the data, so no hand-typed Hangul
    "Lantern": "BTB",          # rows mentioning BTB
    "Nene": "BTB",
    "Chichir": "BTB",
    "Mowgli": "BTB",
}

rowre = re.compile(
    r"^\s*(\u2606+[\s\u2606]*)\s*\|\s*([\uAC00-\uD7A3]+)\s*\|\s*([^|]+?)\s*\|\s*(.*?)\s*\|\s*$",
    re.M,
)
rows = rowre.findall(hunter)

L.append("### A. namu Blustone roster rows whose text mentions BTB")
L.append("")
for stars, attr, name, desc in rows:
    dc = re.sub(r"<[^>]+>", "", desc).replace("&#91;", "[").replace("&#93;", "]")
    if "BTB" in dc:
        L.append("  stars=%s  attribute=%s  name=%s" % (stars.strip(), attr, name.strip()))
        L.append("    %s" % dc[:900])
        L.append("")

# The 치르치르 BTB sentence lives in the 1-star Fire block; find it by the
# word that co-occurs (BTB) anywhere in the document.
L.append("### B. every BTB sentence in the namu hunter page (context preserved)")
L.append("")
for m in re.finditer(r"BTB", hunter):
    s = max(0, m.start() - 500)
    e = min(len(hunter), m.end() + 500)
    seg = re.sub(r"<[^>]+>", " ", hunter[s:e])
    seg = seg.replace("&#91;", "[").replace("&#93;", "]").replace("&amp;", "&")
    L.append("  ...%s..." % re.sub(r"\s+", " ", seg))
    L.append("")

# ---------- 2. project-side baselines ------------------------------------
L.append("### C. project baselines for the four shared-cast IDs")
L.append("")

# CHAR_STR
cs = io.open(
    "analysis/recovered-data/leveldb-tables/char-str.tsv", encoding="utf-8"
).read().split("\n")
hdr = cs[0].split("\t")
for line in cs[1:]:
    f = line.split("\t")
    if f[0] in ("001", "002", "003", "004"):
        L.append("  card %s" % f[0])
        for h, v in zip(hdr, f):
            L.append("     %-11s %s" % (h, v))
        L.append("")

# SKILL_TAG
L.append("  skill-tag rows:")
st = io.open(
    "analysis/recovered-data/leveldb-tables/skill-tag.tsv", encoding="utf-8"
).read().split("\n")
for line in st[1:]:
    f = line.split("\t")
    if f and f[0] in ("001", "002", "003", "004"):
        L.append("     %s slot %s : %s" % (f[0], f[1], f[2]))
L.append("")

# 2019 JP archive
L.append("  2019 JP archive rows:")
arch = io.open(
    "analysis/research/base-stats-visual-hunt/archived-hunter-database-2019.tsv",
    encoding="utf-8",
).read().split("\n")
ah = arch[0].split("\t")
for line in arch[1:]:
    if not line.strip():
        continue
    f = line.split("\t")
    if f[-3].strip('"') in ("001", "002", "003", "004"):
        L.append("     catalog %s" % f[-3].strip('"'))
        for h, v in zip(ah, f):
            if h.strip('"') in (
                "listed_name",
                "role_ja",
                "element_ja",
                "rarity_on_draw",
                "catalog_id",
            ):
                L.append("        %-16s %s" % (h.strip('"'), v.strip('"')))
        L.append("")

# ---------- 3. attribute vocabulary, sliced from data -------------------
L.append("### D. attribute / role vocabulary as it appears in the data")
L.append("")
# The Blustone main article states the three attributes; slice that sentence.
for m in re.finditer(r"[^\n]*\uC18C\uB7C9[^\n]*", main):
    seg = m.group(0)
    if "\uB18C\uB7C9" in seg and len(seg) < 400:
        L.append("  main: %s" % seg.strip()[:400])
        break
# the three attribute words from the roster
attrs = {}
for stars, attr, name, desc in rows:
    attrs[attr] = attrs.get(attr, 0) + 1
L.append("  distinct attribute tokens in the roster: %s" % ", ".join("%s=%d" % kv for kv in sorted(attrs.items())))
# role vocabulary from the project's own TAG_REF table
tagref = io.open(
    "analysis/recovered-data/leveldb-tables/tag-ref.tsv", encoding="utf-8"
).read().split("\n")
L.append("  project TAG_REF job rows:")
for line in tagref[1:]:
    f = line.split("\t")
    if f and f[0].startswith("JOB_"):
        L.append("     %-10s %s" % (f[0], f[1] if len(f) > 1 else ""))

out = "\n".join(L)
io.open(OUT, "w", encoding="utf-8", newline="\n").write(out)
print("wrote", OUT, len(out), "chars")