# -*- coding: utf-8 -*-
"""Scene segmentation + contact sheets for the CN-beta playthrough.

Segmentation: the video cuts through full black frames (fade transitions), so
black runs are scene boundaries. Within a scene we pick evenly spaced
representatives for visual review. Every chosen frame is verified to decode.
"""
import csv
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, "cnbeta-frames-2026-10-09")
FRAMES = os.path.expandvars(r"%TEMP%\opencode\cnbeta\f1s")

fe = {}
with open(os.path.join(D, "frame-features-1hz.csv"), encoding="utf-8") as fh:
    for row in csv.DictReader(fh):
        fe[int(row["t"])] = {k: float(v) for k, v in row.items() if k not in ("name", "t")}
ch = {}
with open(os.path.join(D, "frame-change-1hz.csv"), encoding="utf-8") as fh:
    for row in csv.DictReader(fh):
        ch[int(row["t"])] = float(row["meanabsdiff_vs_prev"])

TS = sorted(fe)
BLACK = 3.0


def is_black(t):
    return fe[t]["mean"] < BLACK


def frame_path(t):
    return os.path.join(FRAMES, "f_%06d.jpg" % (t + 1))


def scenes():
    """Contiguous runs of non-black frames."""
    out = []
    start = None
    for t in TS:
        if not is_black(t):
            if start is None:
                start = t
        else:
            if start is not None:
                out.append((start, t - 1))
                start = None
    if start is not None:
        out.append((start, TS[-1]))
    return out


def sheet(ts, outpath, cols=3, cell=560, label=True):
    """Contact sheet of the given timestamps, labelled with the timestamp."""
    ims = []
    for t in ts:
        p = frame_path(t)
        with Image.open(p) as im:
            im.load()
            ims.append((t, im.convert("RGB")))
    if not ims:
        return None
    rows = (len(ims) + cols - 1) // cols
    lab = 26 if label else 0
    W = cols * cell
    H = rows * (int(cell * ims[0][1].height / ims[0][1].width) + lab)
    canvas = Image.new("RGB", (W, H), (24, 24, 28))
    dr = ImageDraw.Draw(canvas)
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except Exception:  # noqa: BLE001
        font = ImageFont.load_default()
    for i, (t, im) in enumerate(ims):
        r, c = divmod(i, cols)
        w = cell
        h = int(cell * im.height / im.width)
        canvas.paste(im.resize((w, h), Image.LANCZOS), (c * cell, r * (h + lab) + lab))
        if label:
            dr.rectangle([c * cell, r * (h + lab), c * cell + cell, r * (h + lab) + lab],
                         fill=(200, 30, 30))
            dr.text((c * cell + 6, r * (h + lab) + 3), "t=%d s" % t, fill=(255, 255, 255), font=font)
    canvas.save(outpath, quality=88)
    return canvas.size


def main():
    sc = scenes()
    print("decodable 1 Hz frames: %d  (t=%d..%d)" % (len(TS), TS[0], TS[-1]))
    print("non-black scenes: %d" % len(sc))
    print("\n idx  start   end  len  mean_lum  mean_edge  mean_pale  mean_darkbot")
    rows = []
    for i, (a, b) in enumerate(sc):
        sub = [fe[t] for t in range(a, b + 1)]
        rows.append((i, a, b, b - a + 1,
                     np.mean([x["mean"] for x in sub]), np.mean([x["edge"] for x in sub]),
                     np.mean([x["pale"] for x in sub]), np.mean([x["darkbot"] for x in sub])))
    for r in rows:
        print(" %4d %5d %5d %5d   %8.2f   %8.4f   %8.4f   %8.3f" % r)
    with open(os.path.join(D, "scenes.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["idx", "start_t", "end_t", "len_s", "mean_lum", "mean_edge", "mean_pale", "mean_darkbot"])
        w.writerows(rows)
    print("\nwrote scenes.csv")

    if len(sys.argv) > 1 and sys.argv[1] == "sheets":
        sd = os.path.join(D, "sheets")
        os.makedirs(sd, exist_ok=True)
        # one sheet per scene (or split scenes longer than 9 frames)
        made = 0
        for i, (a, b) in enumerate(sc):
            span = list(range(a, b + 1))
            for j in range(0, len(span), 9):
                chunk = span[j:j + 9]
                if not chunk:
                    continue
                # always include the last frame of the chunk
                if j + 9 < len(span):
                    chunk[-1] = chunk[-1]
                nm = os.path.join(sd, "sc%03d_%04d-%04d.jpg" % (i, chunk[0], chunk[-1]))
                size = sheet(chunk, nm, cols=3)
                made += 1
                print("  sheet", os.path.basename(nm), size)
        print("sheets written:", made)


if __name__ == "__main__":
    main()