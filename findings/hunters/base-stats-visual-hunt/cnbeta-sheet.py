# -*- coding: utf-8 -*-
"""Contact sheets built from the ACTIVE 818x720 region only.

The full 1280x720 frame wastes 64% of the area on pillarbox, which halves the
effective resolution of every label. Cropping first and then downscaling to a
fixed cell makes the sheet genuinely more readable than the source video.

Every cell is verified to decode; a cell that fails is reported, not silently
skipped.
"""
import csv
import os
import sys

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, "cnbeta-frames-2026-10-09")
FRAMES = os.path.expandvars(r"%TEMP%\opencode\cnbeta\f1s")
L, T, R, B = [int(v) for v in open(os.path.join(D, "active-box.txt"), encoding="utf-8").read().split()]
BOX = (L, T, R, B)


def fp(t):
    return os.path.join(FRAMES, "f_%06d.jpg" % (t + 1))


def sheet(ts, outpath, cols=4, cell_w=400, label=24):
    ims, bad = [], []
    for t in ts:
        try:
            with Image.open(fp(t)) as im:
                im.load()
                ims.append((t, im.convert("RGB").crop(BOX)))
        except Exception as exc:  # noqa: BLE001
            bad.append((t, repr(exc)))
    if not ims:
        return None, bad
    cw = cell_w
    ch_ = int(cw * ims[0][1].height / ims[0][1].width)
    rows = (len(ims) + cols - 1) // cols
    canvas = Image.new("RGB", (cols * cw, rows * (ch_ + label)), (20, 20, 24))
    dr = ImageDraw.Draw(canvas)
    try:
        font = ImageFont.truetype("arialbd.ttf", 18)
    except Exception:  # noqa: BLE001
        font = ImageFont.load_default()
    for i, (t, im) in enumerate(ims):
        r, c = divmod(i, cols)
        y = r * (ch_ + label)
        dr.rectangle([c * cw, y, c * cw + cw, y + label], fill=(190, 25, 25))
        dr.text((c * cw + 5, y + 2), "t=%ds" % t, fill=(255, 255, 255), font=font)
        canvas.paste(im.resize((cw, ch_), Image.LANCZOS), (c * cw, y + label))
    canvas.save(outpath, quality=90)
    return canvas.size, bad


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "sheets"
    if mode == "sheets":
        sc = []
        with open(os.path.join(D, "scenes.csv"), encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                sc.append((int(row["idx"]), int(row["start_t"]), int(row["end_t"])))
        sd = os.path.join(D, "sheets-crop")
        os.makedirs(sd, exist_ok=True)
        made, allbad = 0, []
        for i, a, b in sc:
            span = list(range(a, b + 1))
            for j in range(0, len(span), 8):
                chunk = span[j:j + 8]
                nm = os.path.join(sd, "sc%03d_%04d-%04d.jpg" % (i, chunk[0], chunk[-1]))
                size, bad = sheet(chunk, nm, cols=4)
                if bad:
                    allbad += bad
                made += 1
        print("sheets:", made, "undecodable cells:", len(allbad), allbad[:5])
    elif mode == "one":
        # single full-resolution still: no downscale at all
        t = int(sys.argv[2])
        out = sys.argv[3]
        with Image.open(fp(t)) as im:
            im.load()
            c = im.convert("RGB").crop(BOX)
        c.save(out, quality=96)
        print("saved", out, c.size)
    elif mode == "zoom":
        # zoom a sub-rectangle of the ACTIVE region.
        # usage: zoom <t> <out> <scale> [x y w h]   (x,y,w,h default to whole)
        t = int(sys.argv[2])
        out = sys.argv[3]
        scale = float(sys.argv[4])
        if len(sys.argv) >= 9:
            x, y, w, h = (int(v) for v in sys.argv[5:9])
        else:
            x, y, w, h = 0, 0, R - L, B - T
        x = max(0, min(x, R - L - 1)); y = max(0, min(y, B - T - 1))
        w = min(w, R - L - x); h = min(h, B - T - y)
        with Image.open(fp(t)) as im:
            im.load()
            c = im.convert("RGB").crop((L + x, T + y, L + x + w, T + y + h))
        c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
        c.save(out, quality=96)
        print("saved", out, c.size, "from active-rect", (x, y, w, h), "scale", scale)


if __name__ == "__main__":
    main()