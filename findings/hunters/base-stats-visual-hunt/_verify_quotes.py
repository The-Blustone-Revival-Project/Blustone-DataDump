"""FINAL VERIFICATION (fast): every Hangul span typed into the deliverable must
byte-match a primary source.

The real danger is not console mojibake in an existing file -- it is that I
TYPED Korean from console output. If the console mangled it, the deliverable is
wrong while looking plausible. This checks each span against the primary bytes.
"""
import glob
import html
import os
import re
import sys

DELIV = r"analysis/research/base-stats-visual-hunt/trace-cost-adjudication-2026-10-08.md"
D = r"analysis/research/base-stats-visual-hunt/_tools/_namu_raw"
FORUM = r"recovered-assets/forum-en-2026-10-05/pass2/body"
T199 = r"C:/Users/shaha/AppData/Local/Temp/opencode"

d = open(DELIV, encoding="utf-8").read()
out = []


def w(s=""):
    out.append(s)


def plain(x):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"(?is)<[^>]*>", " ", x)))


parts = []
for f in glob.glob(os.path.join(D, "*.utf8.txt")):
    parts.append(plain(open(f, encoding="utf-8").read()))
for f in glob.glob(os.path.join(FORUM, "*.html")):
    parts.append(plain(open(f, encoding="utf-8", errors="replace").read()))
for f in glob.glob(os.path.join(T199, "se199711*.html")):
    parts.append(plain(open(f, encoding="utf-8", errors="replace").read()))
corpus = re.sub(r"\s+", " ", " \n ".join(parts))

w("#" * 78)
w("# Hangul spans typed into the deliverable, checked against primary bytes")
w("#" * 78)
w("corpus files : %d namu dumps + forum HTML + 199711 HTML" % len(parts))
w("corpus chars : %d" % len(corpus))
w("")

spans = sorted(set(re.findall(r"[\uAC00-\uD7A3][\uAC00-\uD7A3]*", d)))
bad = [s for s in spans if s not in corpus]
w("distinct Hangul spans in deliverable : %d" % len(spans))
w("spans NOT byte-matching the corpus  : %d" % len(bad))
for s in bad:
    w("   MISMATCH: %s" % s)
w("")
w("RESULT: %s" % ("every Hangul span byte-matches a primary source"
                   if not bad else "%d spans need correction" % len(bad)))

w()
w("#" * 78)
w("# Load-bearing quotations, present/absent in corpus and deliverable")
w("#" * 78)
LOAD = [
    "각 등급별로 필요한 흔적 수는 다음과 같다",
    "(2^n)×10개",
    "한 명당 흔적 20개가 필요한 1성 헌터를",
    "각 흔적은 등급(★)별로 나눈 다음에 한국어 어순으로 정리했다",
    "★4헌터 흔적의 구매 가격은 훈장 700당 흔적 8개이며",
    "★3헌터 흔적의 구매 가격은 훈장 350당 흔적 8개다",
    "수집 시 해당 헌터 획득 가능",
    "3성 헌터 흔적",
    "미라주",
    "신기루",
    "Total scrolls spent: 1056",
    "Total traces returned: 4208",
    "Golden Hunter Traces (1st Priority) | 150 for 2",
    "375개로 5개",
    "20 / 100 / 300",
    "20/100/300",
]
for q in LOAD:
    w("  corpus=%-5s deliverable=%-5s  %s" % (q in corpus, q in d, q))

w()
w("NOTE: '미라주' must be corpus=False (it is the proven absence).")
w("      '20 / 100 / 300' must be corpus=False (vsfan, a different wiki).")

open(r"analysis/research/base-stats-visual-hunt/_trace_cost_quotecheck.txt",
     "w", encoding="utf-8", newline="\n").write("\n".join(out))
sys.stdout.write("done\n")