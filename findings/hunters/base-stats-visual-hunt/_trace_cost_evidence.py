"""Probe 7: last evidence pass.
  (a) what 199711 actually says about traces (quote the captured text, not a
      downstream summary);
  (b) namu per-grade trace PURCHASE prices (FC chips, guild honor);
  (c) is 신기루 the same thing as the project's "Mirage"?
  (d) the '3성 헌터 흔적' shop sentence in full.

Read-only, UTF-8/LF out.
"""
import glob
import html
import os
import re
import sys

OUT = r"analysis/research/base-stats-visual-hunt/_trace_cost_evidence.txt"
out = []
D = r"analysis/research/base-stats-visual-hunt/_tools/_namu_raw"


def w(s=""):
    out.append(s)


def strip(x):
    x = re.sub(r"<[^>]*>", " ", x)
    return re.sub(r"\s+", " ", html.unescape(x)).strip()


w("#" * 78)
w("# (d) '3성 헌터 흔적' — the ONE hit, full sentence")
w("#" * 78)
t = open(os.path.join(D, "ctrl-d-main.utf8.txt"), encoding="utf-8").read()
m = re.search("3성 헌터 흔적", t)
seg = strip(t[max(0, m.start() - 900):m.end() + 400])
w(seg)

w()
w("#" * 78)
w("# (b1) guild honor trace prices, item page 2.5")
w("#" * 78)
ti = open(os.path.join(D, "it-d-아이템.utf8.txt"), encoding="utf-8").read()
for kw in ("★4헌터 흔적", "★3헌터 흔적", "훈장 700", "훈장 350"):
    w("\n--- %r : %d hit(s) in it-d-아이템 ---" % (kw, ti.count(kw)))
    for mm in re.finditer(re.escape(kw), ti):
        w("   " + strip(ti[max(0, mm.start() - 350):mm.end() + 250]))

w()
w("#" * 78)
w("# (b2) FC fight-chip trace price, hunter page")
w("#" * 78)
th = open(os.path.join(D, "raw-d-헌터.utf8.txt"), encoding="utf-8").read()
for kw in ("375", "파이트칩 코너", "백헨", "릴리&랄라의 흔적", "할리"):
    w("\n--- %r : %d hit(s) in raw-d-헌터 ---" % (kw, th.count(kw)))
    for mm in list(re.finditer(re.escape(kw), th))[:4]:
        w("   " + strip(th[max(0, mm.start() - 320):mm.end() + 320]))

w()
w("#" * 78)
w("# (b3) is 신기루 the project's 'Mirage'? search the namu dumps")
w("#" * 78)
for f in sorted(glob.glob(os.path.join(D, "*.utf8.txt"))):
    try:
        x = open(f, encoding="utf-8").read()
    except Exception:
        continue
    a, b = x.count("신기루"), x.count("미라주")
    if a or b:
        w("  %-34s 신기루=%-4d 미라주=%d" % (os.path.basename(f), a, b))
w("  (searching for co-occurrence of the two terms in one file:)")
for f in sorted(glob.glob(os.path.join(D, "*.utf8.txt"))):
    try:
        x = open(f, encoding="utf-8").read()
    except Exception:
        continue
    if "신기루" in x and ("미라주" in x or "유적" in x):
        w("   CO-OCCURS: %s" % os.path.basename(f))

w()
w("#" * 78)
w("# (a) 199711 captured text — every trace sentence")
w("#" * 78)
cands = glob.glob(r"C:/Users/shaha/AppData/Local/Temp/opencode/se199711*")
w("temp captures found: %s" % [os.path.basename(c) for c in cands])
cands += glob.glob(r"recovered-assets/**/se199711*", recursive=True)
w("repo captures found : %s" % [os.path.basename(c) for c in cands])
hit = 0
for c in cands:
    if not c.lower().endswith((".html", ".txt")):
        continue
    try:
        x = open(c, encoding="utf-8", errors="replace").read()
    except Exception as e:
        w("  [unreadable %s: %s]" % (c, e))
        continue
    if "trace" not in x.lower():
        continue
    hit += 1
    w("\n===== %s =====" % os.path.basename(c))
    xs = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", x)
    for mm in re.finditer(r"(?i)trace", xs):
        s = strip(xs[max(0, mm.start() - 400):mm.end() + 400])
        w("   ...%s..." % s)
    w("   (total trace-mentions: %d)" % len(re.findall(r"(?i)trace", xs)))
w("\ncaptures with the word 'trace': %d" % hit)
if hit == 0:
    w("NO 199711 capture carrying 'trace' was found in the searched paths.")
    w("That is a NEGATIVE for local availability, not proof 199711 lacks it.")

open(OUT, "w", encoding="utf-8", newline="\n").write("\n".join(out))
sys.stdout.write("wrote %s\n" % OUT)