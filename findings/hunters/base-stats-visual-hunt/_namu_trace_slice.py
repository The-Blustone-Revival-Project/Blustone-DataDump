"""Probe 3: slice the namu hunter-page raw dump for the recruitment section
and every occurrence of 흔적 (trace), so the trace claims are read from the
canonical render rather than from a downstream transcription.

Read-only. Writes UTF-8 + LF.
"""
import html
import re
import sys

SRC = r"analysis/research/base-stats-visual-hunt/_tools/_namu_raw/raw-d-헌터.utf8.txt"
OUT = r"analysis/research/base-stats-visual-hunt/_namu_trace_slices.txt"

t = open(SRC, encoding="utf-8").read()

# namu markup -> readable text
t = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", t)
t = re.sub(r"(?is)<br\s*/?>", "\n", t)
t = re.sub(r"(?is)</(p|div|li|h[1-6]|tr|td|th)>", "\n", t)
t = re.sub(r"(?is)<[^>]*>", "", t)
t = html.unescape(t)
t = re.sub(r"[ \t\xa0]+", " ", t)
t = re.sub(r"\n\s*\n\s*\n+", "\n\n", t)

out = []
out.append("TOTAL chars: %d   U+FFFD: %d" % (len(t), t.count("\ufffd")))

# --- section 1.4 섭외 ---
out.append("\n" + "=" * 78 + "\nSECTION 1.4 섭외 (and neighbours 1.3 / 1.5)\n" + "=" * 78)
for tag in ("s-1.3", "s-1.4", "s-1.5"):
    i = t.find('id="%s"' % tag)
    if i < 0:
        i = t.find("#" + tag)
    if i < 0:
        out.append("\n[%s NOT FOUND]\n" % tag)
        continue
    j = t.find('id="s-', i + 10)
    out.append("\n--- %s  (offset %d..%s) ---\n" % (tag, i, j))
    out.append(t[i:j if j > i else i + 4000].strip()[:6000])

# --- every 흔적 occurrence with context ---
out.append("\n" + "=" * 78 + "\nEVERY 흔적 OCCURRENCE WITH CONTEXT\n" + "=" * 78)
n = 0
for m in re.finditer("흔적", t):
    n += 1
    a = max(0, m.start() - 260)
    b = min(len(t), m.end() + 260)
    out.append("\n[%03d @%d] ...%s..." % (n, m.start(), t[a:b].replace("\n", " ⏎ ")))
out.append("\nTOTAL 흔적 occurrences: %d" % n)

# --- the (2^n)x10 formula neighbourhood ---
out.append("\n" + "=" * 78 + "\nNEIGHBOURHOOD OF THE FORMULA (2^n)\n" + "=" * 78)
for m in re.finditer(r"\(2\^n\)", t):
    a = max(0, m.start() - 1500)
    b = min(len(t), m.end() + 1500)
    out.append("\n@%d\n%s\n" % (m.start(), t[a:b]))

# --- 등급에 따라 ... 개수 ---
out.append("\n" + "=" * 78 + "\nSEARCH: 등급에 따라 / 일정 개수 / 정해진 개수\n" + "=" * 78)
for pat in ("등급에 따라", "일정 개수", "정해진 개수", "3성 헌터 흔적", "미라주", "12개", "20개"):
    out.append("\n--- %r : %d hits ---" % (pat, t.count(pat)))
    for m in re.finditer(re.escape(pat), t):
        a = max(0, m.start() - 300)
        b = min(len(t), m.end() + 300)
        out.append("   ...%s..." % t[a:b].replace("\n", " ⏎ "))

open(OUT, "w", encoding="utf-8", newline="\n").write("\n".join(out))
sys.stdout.write("wrote %s (%d chars)\n" % (OUT, len("\n".join(out))))