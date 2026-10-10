"""Probe 6: extract the namu ITEM page's structured tables around traces and
the grade-gated search table, plus the exact 5.x section headers.

Read-only. UTF-8/LF out.
"""
import html
import re
import sys

P = r"analysis/research/base-stats-visual-hunt/_tools/_namu_raw/it-d-아이템.utf8.txt"
OUT = r"analysis/research/base-stats-visual-hunt/_namu_item_trace_tables.txt"

t = open(P, encoding="utf-8").read()
out = []
out.append("chars %d  U+FFFD %d" % (len(t), t.count("\ufffd")))

out.append("\n" + "=" * 76 + "\nSECTION 5 HEADERS (헌터 흔적 ladder)\n" + "=" * 76)
for m in re.finditer(r"<a id='(s-5(?:\.\d+)?)'[^>]*>(.*?)</a>", t):
    out.append("  %-10s %s" % (m.group(1), re.sub(r"<[^>]*>", "", m.group(2))))

out.append("\n" + "=" * 76 + "\nSECTION 5 INTRO (the grade-axis sentence)\n" + "=" * 76)
i = t.find("id='s-5'")
seg = t[i - 400:i + 900]
seg = re.sub(r"<[^>]*>", "", seg)
out.append(html.unescape(seg))

out.append("\n" + "=" * 76 + "\nALL TABLES ON THE ITEM PAGE, in document order\n" + "=" * 76)
t2 = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", t)
tabs = list(re.finditer(r"(?is)<table\b.*?</table\s*>", t2))
out.append("tables: %d" % len(tabs))
for k, m in enumerate(tabs):
    body = m.group(0)
    rows = []
    for tr in re.findall(r"(?is)<tr\b.*?</tr>", body):
        cells = []
        for cm in re.finditer(r"(?is)<t[dh]\b[^>]*>(.*?)</t[dh]\s*>", tr):
            txt = re.sub(r"(?is)<[^>]*>", " ", cm.group(1))
            cells.append(re.sub(r"\s+", " ", html.unescape(txt)).strip())
        rows.append(cells)
    flat = " ".join(c for r in rows for c in r)
    # keep only tables that mention trace / grade / search vocabulary
    rel = any(kw in flat for kw in ("흔적", "헬륨", "수색", "★", "성"))
    out.append("\n--- TABLE %d : %d rows %s ---" % (k, len(rows), "" if rel else "(not trace/grade related)"))
    if rel:
        for r in rows:
            out.append("   " + " | ".join(r))

out.append("\n" + "=" * 76 + "\nGRADE-GATED SEARCH TABLE context (헬륨/수색)\n" + "=" * 76)
for kw in ("헬륨 소비량", "수색 가능 횟수", "최소 2개", "최대 8개", "3성 이상 헌터들의 흔적"):
    out.append("\n--- %r : %d hit(s) ---" % (kw, t.count(kw)))
    for m in re.finditer(re.escape(kw), t):
        a = max(0, m.start() - 600)
        b = min(len(t), m.end() + 600)
        seg = re.sub(r"<[^>]*>", " ", t[a:b])
        out.append("   ..." + re.sub(r"\s+", " ", html.unescape(seg)) + "...")

open(OUT, "w", encoding="utf-8", newline="\n").write("\n".join(out))
sys.stdout.write("wrote %s\n" % OUT)