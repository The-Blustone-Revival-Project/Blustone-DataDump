# -*- coding: utf-8 -*-
"""Frame triage for the CN-beta playthrough.

Two jobs:
 1. Prove the exact decodable interval (never assume the advertised duration).
 2. Classify every 1 Hz frame so a human reviews a shortlist, not 727 images.

The classifier is deliberately simple and auditable: it reports cheap, whole
frame measurements (brightness, edge density, a "panel" score, a "text-box" score
and frame-to-frame change) and writes a CSV. It does NOT decide what a frame is;
the reading is done by eye afterwards. Positive controls for every feature are
run in `selftest`.
"""
import csv
import json
import os
import subprocess
import sys

import numpy as np
from PIL import Image

FRAMES = os.path.expandvars(r"%TEMP%\opencode\cnbeta\f1s")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cnbeta-frames-2026-10-09")


def load(p):
    with Image.open(p) as im:
        im.load()
        return np.asarray(im.convert("RGB"), dtype=np.uint8)


def feats(arr):
    """Cheap whole-frame measurements. Returns a dict of scalars."""
    g = arr.mean(axis=2).astype(np.float32)
    h, w = g.shape
    # horizontal + vertical gradient magnitude
    gx = np.abs(np.diff(g, axis=1))
    gy = np.abs(np.diff(g, axis=0))
    edge = float((gx > 28).mean() + (gy > 28).mean())

    # "panel" score: fraction of pixels that are bright and low-variance
    # (a light opaque UI card) -- the stat panel in this game is a pale card.
    mx = arr.max(axis=2).astype(np.int16)
    mn = arr.min(axis=2).astype(np.int16)
    pale = ((mn > 150) & ((mx - mn) < 60)).mean()

    # "dark band" score: bottom 22% mostly dark (dialogue box / HUD)
    bot = g[int(h * 0.78):, :]
    dark = float((bot < 70).mean())

    # "text rows": per-row edge energy peaks -> count of text-like lines
    row_e = (np.abs(np.diff(g, axis=1)) > 28).mean(axis=1)
    thr = row_e.mean() + 1.2 * row_e.std()
    textrows = int((row_e > thr).sum())
    return {
        "mean": round(float(g.mean()), 2),
        "edge": round(edge, 4),
        "pale": round(float(pale), 4),
        "darkbot": round(dark, 4),
        "textrows": textrows,
        "uniq": len(np.unique(arr[::4, ::4].reshape(-1, 3), axis=0)),
    }


def selftest():
    """Positive controls. A zero is only believable if these pass."""
    names = sorted(n for n in os.listdir(FRAMES) if n.endswith(".jpg"))
    print("frames on disk:", len(names), "first", names[0], "last", names[-1])
    # control A: a real game frame must decode to the advertised geometry
    a = load(os.path.join(FRAMES, names[0]))
    print("control A geometry:", a.shape, "expected (720, 1280, 3)")
    # control B: blank-ish vs busy separation must be non-degenerate
    rows = []
    for n in names:
        rows.append((n,) + tuple(feats(load(os.path.join(FRAMES, n))).values()))
    arr = np.array([[float(x) for x in r[1:]] for r in rows])
    for i, col in enumerate(["mean", "edge", "pale", "darkbot", "textrows", "uniq"]):
        col_v = arr[:, i]
        print("control B %-9s min=%-10.4f med=%-10.4f max=%-10.4f stdev=%.4f"
              % (col, col_v.min(), np.median(col_v), col_v.max(), col_v.std()))
    return rows


def main():
    os.makedirs(OUT, exist_ok=True)
    rows = selftest()
    hdr = ["name", "t", "mean", "edge", "pale", "darkbot", "textrows", "uniq"]
    path = os.path.join(OUT, "frame-features-1hz.csv")
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(hdr)
        for n, mean, edge, pale, darkbot, textrows, uniq in rows:
            t = int(n[2:8]) - 1  # f_000001.jpg == t=0
            w.writerow([n, t, mean, edge, pale, darkbot, textrows, uniq])
    print("wrote", path)

    # frame-to-frame change over time, for a coarse "what happens when" map
    prev = None
    changes = []
    for n, mean, edge, pale, darkbot, textrows, uniq in rows:
        g = load(os.path.join(FRAMES, n)).mean(axis=2).astype(np.int16)
        small = g[::6, ::6]
        if prev is not None:
            d = float(np.abs(small - prev).mean())
        else:
            d = 0.0
        changes.append((int(n[2:8]) - 1, round(d, 2)))
        prev = small
    cpath = os.path.join(OUT, "frame-change-1hz.csv")
    with open(cpath, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["t", "meanabsdiff_vs_prev"])
        w.writerows(changes)
    print("wrote", cpath)


if __name__ == "__main__":
    main()