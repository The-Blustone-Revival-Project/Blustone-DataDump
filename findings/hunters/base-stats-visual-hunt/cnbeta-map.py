# -*- coding: utf-8 -*-
"""Print a coarse structural map of the decodable interval from the 1 Hz
features + change series. Segments are cut where the frame-to-frame change
drops below a threshold for a run (a static screen) or spikes (a cut).
"""
import csv
import os

import numpy as np

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cnbeta-frames-2026-10-09")
ch = {}
with open(os.path.join(D, "frame-change-1hz.csv"), encoding="utf-8") as fh:
    for row in csv.DictReader(fh):
        ch[int(row["t"])] = float(row["meanabsdiff_vs_prev"])
fe = {}
with open(os.path.join(D, "frame-features-1hz.csv"), encoding="utf-8") as fh:
    for row in csv.DictReader(fh):
        fe[int(row["t"])] = {k: float(v) for k, v in row.items() if k not in ("name", "t")}

ts = sorted(ch)
print("decodable t range: %d .. %d  (%d frames at 1 Hz)" % (ts[0], ts[-1], len(ts)))

# static screens: change < 1.0 for >= 8 s in a row
STATIC = 1.0
MINLEN = 8
runs = []
i = 0
while i < len(ts):
    if ch[ts[i]] < STATIC:
        j = i
        while j + 1 < len(ts) and ch[ts[j + 1]] < STATIC:
            j += 1
        if j - i + 1 >= MINLEN:
            runs.append((ts[i], ts[j]))
        i = j + 1
    else:
        i += 1
print("\n== static screens (change<%.1f for >=%ds) : %d ==" % (STATIC, MINLEN, len(runs)))
for a, b in runs:
    m = [fe[t] for t in range(a, b + 1) if t in fe]
    if not m:
        continue
    print("  t=%4d..%4d (%3ds) mean=%6.2f edge=%.4f pale=%.4f darkbot=%.3f textrows=%3d uniq=%5d"
          % (a, b, b - a + 1,
             np.mean([x["mean"] for x in m]), np.mean([x["edge"] for x in m]),
             np.mean([x["pale"] for x in m]), np.mean([x["darkbot"] for x in m]),
             np.mean([x["textrows"] for x in m]), np.mean([x["uniq"] for x in m])))

# candidate "pale panel" frames: an opaque light card occupies a lot of screen
print("\n== top 40 frames by 'pale' (opaque light card) ==")
top = sorted(fe.items(), key=lambda kv: -kv[1]["pale"])[:40]
for t, f in top:
    print("  t=%4d pale=%.4f mean=%6.2f edge=%.4f darkbot=%.3f textrows=%3d d=%6.2f"
          % (t, f["pale"], f["mean"], f["edge"], f["darkbot"], f["textrows"], ch.get(t, -1)))

print("\n== top 40 frames by 'edge' (most text/UI structure) ==")
top = sorted(fe.items(), key=lambda kv: -kv[1]["edge"])[:40]
for t, f in top:
    print("  t=%4d edge=%.4f pale=%.4f mean=%6.2f darkbot=%.3f textrows=%3d d=%6.2f"
          % (t, f["edge"], f["pale"], f["mean"], f["darkbot"], f["textrows"], ch.get(t, -1)))

print("\n== largest frame-to-frame jumps (scene cuts) ==")
jumps = sorted(ch.items(), key=lambda kv: -kv[1])[:30]
for t, d in jumps:
    print("  t=%4d d=%6.2f  mean=%6.2f edge=%.4f pale=%.4f"
          % (t, d, fe[t]["mean"], fe[t]["edge"], fe[t]["pale"]))

print("\n== darkest frames (possible black/end) ==")
dk = sorted(fe.items(), key=lambda kv: kv[1]["mean"])[:12]
for t, f in dk:
    print("  t=%4d mean=%6.2f edge=%.4f uniq=%5d" % (t, f["mean"], f["edge"], f["uniq"]))