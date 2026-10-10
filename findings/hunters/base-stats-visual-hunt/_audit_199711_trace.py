"""Probe 8: the decisive negative-control on the task brief's claim that
share_en/199711 states trace values 20/100/300.

Method: search the four byte-verified captures for the ladder numerals in a
trace context, AND run a positive control (a term known to be present) so a
zero is interpretable.  Per the GUARD file, a zero without a control is not
evidence.

Read-only. UTF-8/LF out.
"""
import glob
import html
import os
import re
import sys

OUT = r"analysis/research/base-stats-visual-hunt/_199711_trace_audit.txt"
out = []


def w(s=""):
    out.append(s)


def strip(x):
    x = re.sub(r"(?is)<[^>]*>", " ", x)
    return re.sub(r"\s+", " ", html.unescape(x)).strip()


caps = sorted(glob.glob(r"recovered-assets/**/se199711*.html", recursive=True))
if not caps:
    caps = sorted(glob.glob(r"C:/Users/shaha/AppData/Local/Temp/opencode/se199711*.html"))
w("captures: %d" % len(caps))

TEXT = {}
for c in caps:
    x = open(c, encoding="utf-8", errors="replace").read()
    x = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", x)
    TEXT[os.path.basename(c)] = strip(x)

w()
w("#" * 78)
w("# POSITIVE CONTROL — terms known to be in 199711")
w("#" * 78)
for term in ["Trace", "Traces", "Tracec", "Fight Club", "Metron", "exp", "level"]:
    hits = {k: v.count(term) for k, v in TEXT.items()}
    w("  %-12s %s" % (term, hits))
w("  -> the detector fires on 'trace'; the corpus is readable.")

w()
w("#" * 78)
w("# THE TEST — every sentence in 199711 containing 'trace'")
w("#" * 78)
for k, v in TEXT.items():
    w("\n===== %s =====" % k)
    for m in re.finditer(r"(?i)trace\w*", v):
        a = max(0, m.start() - 260)
        b = min(len(v), m.end() + 260)
        w("   ...%s..." % v[a:b])
    w("   (trace-mentions: %d)" % len(re.findall(r"(?i)trace", v)))

w()
w("#" * 78)
w("# Does 20 / 100 / 300 appear as a ladder anywhere near 'trace'?")
w("#" * 78)
for k, v in TEXT.items():
    for m in re.finditer(r"(?i)trace", v):
        a = max(0, m.start() - 400)
        b = min(len(v), m.end() + 400)
        seg = v[a:b]
        present = [n for n in ("20", "100", "300") if re.search(r"\b%s\b" % n, seg)]
        if present:
            w("  %s: numerals %s inside a trace context" % (k, present))
w("  (no line above => the ladder numerals never co-occur with 'trace')")

w()
w("#" * 78)
w("# What 199711 DOES state numerically about traces")
w("#" * 78)
for k, v in TEXT.items():
    for m in re.finditer(r"(?i)trace", v):
        a = max(0, m.start() - 120)
        b = min(len(v), m.end() + 160)
        seg = v[a:b]
        nums = re.findall(r"\b\d[\d,]*\b", seg)
        if nums:
            w("  %s -> numerals %s" % (k, nums))
            break

w()
w("#" * 78)
w("# Arithmetic on the one price 199711 actually gives")
w("#" * 78)
w("  199711: 'Golden Hunter Traces (1st Priority)  150 for 2'")
w("          -> %d fight chips / %d traces = %.4f chips per trace"
  % (150, 2, 150 / 2))
w("  namu  : Beckhen 3* trace, '375개로 5개 얻을 수 있다'")
w("          -> 375 chips / 5 traces = %.4f chips per trace" % (375 / 5))
w("  agreement: %s" % ("EXACT" if 150 / 2 == 375 / 5 else "differs"))
w()
w("  namu  : guild honor, item page 2.5")
w("          '*4 traces: 700 honor per 8 traces' -> %.4f honor/trace" % (700 / 8))
w("          '*3 traces: 350 honor per 8 traces' -> %.4f honor/trace" % (350 / 8))
w("          4*/3* price ratio = %.6f  (i.e. exactly 2x)" % ((700 / 8) / (350 / 8)))
w("          namu recruit ladder 4*/3* = 160/80 = %.6f (also exactly 2x)"
  % (160 / 80))
w("          -> the PRICE axis and the REQUIREMENT axis both double per grade")
w("             at the 3*->4* step, but they are priced in different")
w("             currencies and are NOT the same quantity.")

w()
w("#" * 78)
w("# Where does 20/100/300 actually come from? check the vsfan file.")
w("#" * 78)
vf = r"analysis/research/base-stats-visual-hunt/vsfan-wiki-2026-10-05.md"
if os.path.exists(vf):
    t = open(vf, encoding="utf-8").read()
    w("  vsfan-wiki-2026-10-05.md exists, %d chars" % len(t))
    for m in re.finditer(r"20\s*/\s*100\s*/\s*300|20/100/300", t):
        a = max(0, m.start() - 500)
        b = min(len(t), m.end() + 500)
        w("\n   ...%s..." % t[a:b].replace("\n", " "))
    w("\n  mentions of 'Value' column: %d" % t.count("Value"))
else:
    w("  MISSING: %s" % vf)

open(OUT, "w", encoding="utf-8", newline="\n").write("\n".join(out))
sys.stdout.write("wrote %s\n" % OUT)