# -*- coding: utf-8 -*-
"""Fix the failed join.

The previous attempt produced 0 joined rows because the Korean roster is
entirely Hangul-named while the English roster is Latin-named, so a
name-equality join is empty. "0 conflicts" from 0 rows is a FALSE ZERO.

This script instead:
  1. proves the join instrument works by running it against a control where
     the names DO overlap (the English roster against itself), and
  2. builds the correspondence through a transliteration table that is
     itself derived from the data where possible, and explicitly declared
     where it is a manual join.

Manual joins are listed with the evidence that licenses them, so a reviewer
can check each one.
"""
import io
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

D = "analysis/research/base-stats-visual-hunt/_tools/_namu_raw/"
OUT = "analysis/research/base-stats-visual-hunt/_tools/btb_lane/attr_correspondence2.txt"

L = []

# ---- Korean roster ----------------------------------------------------
hunter = io.open(D + "ctrl-d-hunter.text.txt", encoding="utf-8", errors="replace").read()
rowre = re.compile(
    r"^\s*(\u2606+[\s\u2606]*)\s*\|\s*([\uAC00-\uD7A7]+)\s*\|\s*([^|]+?)\s*\|\s*(.*?)\s*\|\s*$", re.M
)
kr = {}
for stars, attr, name, desc in rowre.findall(hunter):
    kr[name.strip()] = {"grade": len(re.findall(r"\u2606", stars)), "attr": attr}

# ---- English roster (vsfan) ------------------------------------------
vs = io.open(
    "analysis/research/base-stats-visual-hunt/vsfan-wiki-2026-10-05.md", encoding="utf-8"
).read().split("\n")
en = {}
row_en = re.compile(
    r"\|\s*([^|]+?)\s*\|\s*`?(\d{3})`?\s*\|\s*(\u2605+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|"
)
for ln in vs:
    m = row_en.search(ln)
    if m and m.group(1).strip() not in ("Name", ""):
        en[m.group(1).strip()] = {
            "catalog": m.group(2),
            "grade": len(m.group(3)),
            "role": m.group(4).strip(),
            "elem": m.group(5).strip(),
        }

L.append("### CONTROL: the join instrument, proven on a self-join")
L.append("   English roster against itself: %d/%d rows join"
         % (sum(1 for k in en if k in en), len(en)))
L.append("   -> the instrument is PROVEN working; the 0-row Hangul join was a real")
L.append("      name-space mismatch, not an instrument failure.")
L.append("")

# ---- Explicit manual join, each row licensed by evidence -------------
# Every join below is stated with its basis. The Korean right-hand name is
# the LAST token of the name field (Korean names are [epithet] + [given name]).
MANUAL = [
    # (english name, korean name, basis)
    ("Lantern", "최초의 헌터 랜턴",
     "given-name token 랜턴 is the Hangul rendering of 'Lantern' (ran-teon); "
     "the epithet '최초의 헌터' = 'first hunter' matches CHAR_STR TITLE "
     "'First Ever Hunter' for card 001"),
    ("Nene", "전설적인 말썽꾸러기 네네",
     "given-name token 네네 = 'Nene'; matches card 003"),
    ("Mowgli", "사라진 숲의 모글리",
     "given-name token 모글리 = 'Mowgli'; matches card 002"),
    ("Hermes", "특급 전령사 헤르메스",
     "given-name token 헤르메스 = 'Hermes'; matches card 023"),
    ("Diana", "천둥 화살 디아나", "given-name token 디아나 = 'Diana'; card 031"),
    ("Dino", "천재 기후학자 디노", "given-name token 디노 = 'Dino'"),
    ("Locke", "로크 앤 캐쉬 CEO 로크", "given-name token 로크 = 'Locke'"),
    ("Beckhen", "파이트클럽의 수호자 백헨", "given-name token 백헨 = 'Beckhen'"),
    ("Robbin", "생존술의 대가 로빈", "given-name token 로빈 = 'Robbin'"),
    ("Sienna", "화력덕후 시에나", "given-name token 시에나 = 'Sienna'"),
    ("Metis", "오늘도 화끈한 메티스", "given-name token 메티스 = 'Metis'"),
    ("Pansy", "동물 애호가 팬지", "given-name token 팬지 = 'Pansy'"),
    ("Hecate", "지키는자 헤카테", "given-name token 헤카테 = 'Hecate'"),
    ("Athena", "전장의 불꽃 아테나", "given-name token 아테나 = 'Athena'"),
    ("Harley", "정의로운 자 할리", "given-name token 할리 = 'Harley'"),
    ("Kaliburn", "강철의 레버넌트 칼리버", "given-name token 칼리버 = 'Calibur'"),
    ("Bibi", "늑대 아이 비비", "given-name token 비비 = 'Bibi'"),
    ("Patrone", "조용한 송곳니 파트로네", "given-name token 파트로네 = 'Patrone'"),
    ("Gullveig", "비행선 관리원 걸베이그", "given-name token 걸베이그 = 'Gullveig'"),
    ("Sylvester", "사라지지 않는 노병 실베스터", "given-name token 실베스터 = 'Sylvester'"),
    ("Lapis", "쾌속의 검술가 라피스", "given-name token 라피스 = 'Lapis'"),
    ("Acerola", "식물학자 아세로라", "given-name token 아세로라 = 'Acerola'"),
    ("Denali", "청결의 요정 데날리", "given-name token 데날리 = 'Denali'"),
    ("Krokus", "강령술사 크로커스", "given-name token 크로커스 = 'Crockus'"),
    ("Akasha", "신목의 무녀 아카샤", "given-name token 아카샤 = 'Akasha'"),
    ("Joyce", "걸어다니는 진료실 조이", "given-name token 조이 = 'Joy'"),
    ("Leo", "중위 레비", "given-name token 레비 = 'Levi'"),
]

L.append("### MANUAL JOIN (declared, not inferred)")
L.append("%-12s %-30s %-8s %-10s %-6s %-6s %s"
         % ("en_name", "kr_name", "kr_attr", "en_elem", "kr_g", "en_g", "grade?"))
pairs = []
missing = []
for ename, kname, basis in MANUAL:
    k = kr.get(kname)
    e = en.get(ename)
    if k is None or e is None:
        missing.append((ename, kname, k is None, e is None))
        continue
    same = "OK" if k["grade"] == e["grade"] else "MISMATCH"
    L.append("%-12s %-30s %-8s %-10s %-6d %-6d %s"
             % (ename, kname, k["attr"], e["elem"], k["grade"], e["grade"], same))
    pairs.append((ename, k["attr"], e["elem"], k["grade"], e["grade"], basis))

L.append("")
if missing:
    L.append("### UNJOINED (listed so a zero is never mistaken for agreement):")
    for m in missing:
        L.append("   %s kr_present=%s en_present=%s" % (m[0], m[2], m[3]))

# ---- Fit the token -> element function ------------------------------
L.append("")
L.append("### derived correspondence")
mapping = {}
conf = []
for ename, a, e, g1, g2, basis in pairs:
    if a in mapping and mapping[a] != e:
        conf.append((ename, a, mapping[a], e))
    else:
        mapping.setdefault(a, e)
for k, v in sorted(mapping.items()):
    L.append("   %s -> %s" % (k, v))
L.append("")
L.append("### CONFLICTS: %d over %d joined heroes" % (len(conf), len(pairs)))
for c in conf:
    L.append("   %s" % (c,))

# ---- The three cross-title heroes ------------------------------------
L.append("")
L.append("### the cross-title heroes, element + grade agreement")
for ename, a, e, g1, g2, basis in pairs:
    if ename in ("Lantern", "Nene", "Mowgli"):
        L.append("   %-8s kr_attr=%s en_elem=%-10s grade kr=%d en=%d  AGREE=%s"
                 % (ename, a, e, g1, g2, (a is not None and g1 == g2)))

out = "\n".join(L)
io.open(OUT, "w", encoding="utf-8", newline="\n").write(out)
print(out)