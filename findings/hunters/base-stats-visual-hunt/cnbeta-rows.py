# -*- coding: utf-8 -*-
"""Find *small, tight* coloured text rows (the numeric HUD readouts) and emit a
zoom crop for each.

The whole-image colour bbox is dominated by character art. What we want is a
ROW PROFILE: for each y, count strongly-cyan / strongly-red pixels; the HUD
numbers form short runs of tall counts. This localises them robustly.

Controls: a known prep frame must yield cyan+red runs; a dialogue frame must
yield none in the mid-screen band.
"""
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, "cnbeta-frames-2026-10-09")
FRAMES = os.path.expandvars(r"%TEMP%\opencode\cnbeta\f1s")
L, T, R, B = [int(v) for v in open(os.path.join(D, "active-box.txt"), encoding="utf-8").read().split()]


def load(t):
    with Image.open(os.path.join(FRAMES, "f_%06d.jpg" % (t + 1))) as im:
        im.load()
        return im.convert("RGB").crop((L, T, R, B))


def runs(profile, thresh, minlen, gap=6):
    idx = np.where(profile >= thresh)[0]
    if len(idx) == 0:
        return []
    out = []
    s = idx[0]; p = idx[0]
    for v in idx[1:]:
        if v - p <= gap:
            p = v
        else:
            out.append((s, p)); s = v; p = v
    out.append((s, p))
    return [(a, b) for a, b in out if b - a + 1 >= minlen]


def main():
    t = int(sys.argv[1])
    a = load(t)
    arr = np.asarray(a, dtype=np.int16)
    R_, G_, B_ = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]
    cyan = (B_ > R_ + 45) & (G_ > R_ + 30) & (B_ > 120)
    red = (R_ > G_ + 70) & (R_ > 130)
    for nm, m in (("cyan", cyan), ("red", red)):
        prof = m.sum(axis=1)
        rr = runs(prof, 4, 6)
        print("%-5s row-runs (y0,y1,h,px):" % nm,
              [(int(x), int(y), int(y - x + 1), int(prof[x:y + 1].max())) for x, y in rr])
    # emit a generous mid-screen strip for visual reading
    img = a
    crop = img.crop((0, 240, 818, 720))
    out = os.path.join(D, "probe-t%d-midstrip.png" % t)
    up = crop.resize((crop.width * 2, crop.height * 2), Image.LANCZOS)
    up.save(out)
    print("wrote", os.path.basename(out), up.size)


if __name__ == "__main__":
    main()