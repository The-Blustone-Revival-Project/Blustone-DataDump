# -*- coding: utf-8 -*-
"""Measure the true active (non-pillarbox) region of the CN-beta video.

The stream is 1280x720 but the phone recording is portrait and pillarboxed, so
the real game viewport is far narrower. Every downstream reading must be done on
a crop of the active region, upscaled -- otherwise digits are unreadable.

Positive controls: the black bars must be *uniformly* black while the active
region must not be. A wrong crop produces a "blank" reading.
"""
import csv
import os

import numpy as np
from PIL import Image

FRAMES = os.path.expandvars(r"%TEMP%\opencode\cnbeta\f1s")
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cnbeta-frames-2026-10-09")

SAMPLES = [60, 120, 180, 300, 360, 420, 480, 540, 600, 660, 700]


def active_box(t, thresh=12):
    with Image.open(os.path.join(FRAMES, "f_%06d.jpg" % (t + 1))) as im:
        im.load()
        a = np.asarray(im.convert("L"), dtype=np.uint8)
    colmax = a.max(axis=0)
    rowmax = a.max(axis=1)
    cols = np.where(colmax > thresh)[0]
    rows = np.where(rowmax > thresh)[0]
    if len(cols) == 0 or len(rows) == 0:
        return None, a
    return (int(cols[0]), int(rows[0]), int(cols[-1]) + 1, int(rows[-1]) + 1), a


def main():
    boxes = []
    print(" t   active box (l,t,r,b)          w x h    centre content check")
    for t in SAMPLES:
        b, a = active_box(t)
        boxes.append(b)
        l, tp, r, bo = b
        inner = a[tp:bo, l:r]
        outer = np.concatenate([a[:, :l].ravel(), a[:, r:].ravel(),
                                a[tp:tp + 2, :].ravel(), a[bo - 2:, :].ravel()])
        print("%4d  %-28s %4d x %4d   inner mean=%6.2f  bar mean=%6.2f"
              % (t, str(b), r - l, bo - tp, inner.mean(), outer.mean()))
    L = min(b[0] for b in boxes)
    T = min(b[1] for b in boxes)
    R = max(b[2] for b in boxes)
    B = max(b[3] for b in boxes)
    print("\nUNION active box:", (L, T, R, B), "=> %d x %d" % (R - L, B - T))
    with open(os.path.join(D, "active-box.txt"), "w", encoding="utf-8") as fh:
        fh.write("%d %d %d %d\n" % (L, T, R, B))
    print("wrote active-box.txt")

    # second control: crop a known-content frame and save an upscaled version
    t = 480
    b, _ = active_box(t)
    l, tp, r, bo = b
    with Image.open(os.path.join(FRAMES, "f_%06d.jpg" % (t + 1))) as im:
        im.load()
        crop = im.convert("RGB").crop(b)
        up = crop.resize((crop.width * 3, crop.height * 3), Image.LANCZOS)
        p = os.path.join(D, "control-crop-t480-x3.png")
        up.save(p)
        print("control crop", os.path.basename(p), up.size)


if __name__ == "__main__":
    main()