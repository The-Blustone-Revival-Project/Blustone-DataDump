# -*- coding: utf-8 -*-
"""Locate coloured numeric text inside the ACTIVE region, then report its bbox.

Guessing crop rectangles is how digits get misread. This finds saturated
coloured glyph clusters (the cyan/red 战斗力 / 我方队员 numbers) and prints
their bounding boxes, so the zoom rectangle is derived from the image.

Controls: it must find the cyan and red clusters on the prep screen and NOT
find them on a frame that has none.
"""
import os
import sys

import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, "cnbeta-frames-2026-10-09")
FRAMES = os.path.expandvars(r"%TEMP%\opencode\cnbeta\f1s")
L, T, R, B = [int(v) for v in open(os.path.join(D, "active-box.txt"), encoding="utf-8").read().split()]


def load(t):
    with Image.open(os.path.join(FRAMES, "f_%06d.jpg" % (t + 1))) as im:
        im.load()
        return im.convert("RGB").crop((L, T, R, B))


def clusters(a, name):
    """Find connected-ish saturated colour blobs, report bboxes."""
    arr = np.asarray(a, dtype=np.int16)
    mx = arr.max(axis=2); mn = arr.min(axis=2)
    sat = mx - mn
    out = {}
    if name == "cyan":
        m = (arr[:, :, 2] > arr[:, :, 0] + 40) & (arr[:, :, 1] > arr[:, :, 0] + 25) & (mx > 110)
    elif name == "red":
        m = (arr[:, :, 0] > arr[:, :, 1] + 60) & (arr[:, :, 0] > 110) & (sat > 60)
    else:
        m = sat > 90
    ys, xs = np.where(m)
    if len(xs) == 0:
        return None, 0
    return (int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1, int(m.sum()))


if __name__ == "__main__":
    t = int(sys.argv[1])
    a = load(t)
    print("active size:", a.size)
    for nm in ("cyan", "red"):
        bb = clusters(a, nm)
        print("%-5s bbox=%s" % (nm, bb))
    # whole-screen saturated map, coarse
    arr = np.asarray(a, dtype=np.int16)
    sat = arr.max(axis=2) - arr.min(axis=2)
    rows = np.where((sat > 90).sum(axis=1) > 3)[0]
    print("rows with saturated pixels:", (rows.min(), rows.max()) if len(rows) else None)