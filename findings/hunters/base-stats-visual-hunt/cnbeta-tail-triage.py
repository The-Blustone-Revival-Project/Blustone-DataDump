# -*- coding: utf-8 -*-
"""Triage + contact sheets for the NEVER-SEEN remainder of the CN-beta video
(t = 700 .. 1795 s), which exists only because the download was completed.

Same method as the first pass, same controls: features must be non-degenerate
and every sheet cell must decode.
"""
import csv
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, "cnbeta-frames-2026-10-09")
FR = os.path.expandvars(r"%TEMP%\opencode\cnbeta\f1s_full")
OFF = 699  # g_000001.jpg == t=700
L, T, R, B = [int(v) for v in open(os.path.join(D, "active-box.txt"), encoding="utf-8").read().split()]


def fp(i):
    return os.path.join(FR, "g_%06d.jpg" % i)


def t_of(i):
    return OFF + i


def load(i):
    # NOTE: np.asarray() on a PIL image returns a VIEW into the image buffer.
    # If the Image is closed (the `with` block) the buffer is freed and the
    # array reads garbage -- silently, with no exception. np.array(...) copies.
    with Image.open(fp(i)) as im:
        im.load()
        crop = im.convert("RGB").crop((L, T, R, B))
        return np.array(crop, dtype=np.uint8)


def feats(arr):
    g = arr.mean(axis=2).astype(np.float32)
    h, w = g.shape
    edge = float((np.abs(np.diff(g, axis=1)) > 28).mean() + (np.abs(np.diff(g, axis=0)) > 28).mean())
    mx = arr.max(axis=2).astype(np.int16); mn = arr.min(axis=2).astype(np.int16)
    pale = float(((mn > 150) & ((mx - mn) < 60)).mean())
    dark = float((g[int(h * 0.78):, :] < 70).mean())
    return edge, pale, dark, float(g.mean())


def main():
    names = sorted(n for n in os.listdir(FR) if n.endswith(".jpg"))
    n = len(names)
    print("frames:", n, names[0], "..", names[-1], "-> t", t_of(1), "..", t_of(n))
    rows = []
    for i in range(1, n + 1):
        a = load(i)
        e, p, d, m = feats(a)
        rows.append((i, t_of(i), round(m, 2), round(e, 4), round(p, 4), round(d, 4)))
    # controls
    for col, idx in (("mean", 2), ("edge", 3), ("pale", 4), ("darkbot", 5)):
        v = np.array([r[idx] for r in rows], dtype=float)
        print("control %-8s min=%-9.4f med=%-9.4f max=%-9.4f stdev=%.4f"
              % (col, v.min(), np.median(v), v.max(), v.std()))
    with open(os.path.join(D, "frame-features-tail.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh); w.writerow(["idx", "t", "mean", "edge", "pale", "darkbot"]); w.writerows(rows)

    print("\n== top 30 by edge (most UI/text) ==")
    for r in sorted(rows, key=lambda x: -x[3])[:30]:
        print("  t=%4d edge=%.4f pale=%.4f mean=%6.2f darkbot=%.3f" % (r[1], r[3], r[4], r[2], r[5]))
    print("\n== top 30 by pale (opaque light card) ==")
    for r in sorted(rows, key=lambda x: -x[4])[:30]:
        print("  t=%4d pale=%.4f edge=%.4f mean=%6.2f darkbot=%.3f" % (r[1], r[4], r[3], r[2], r[5]))


if __name__ == "__main__":
    main()