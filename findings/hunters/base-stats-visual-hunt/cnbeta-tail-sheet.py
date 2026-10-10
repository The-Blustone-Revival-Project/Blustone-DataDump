# -*- coding: utf-8 -*-
"""Contact sheets + single stills for the tail range (t=700..1795)."""
import os
import sys

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(HERE, "cnbeta-frames-2026-10-09")
FR = os.path.expandvars(r"%TEMP%\opencode\cnbeta\f1s_full")
OFF = 699
L, T, R, B = [int(v) for v in open(os.path.join(D, "active-box.txt"), encoding="utf-8").read().split()]


def idx_of(t):
    return t - OFF


def fp(t):
    return os.path.join(FR, "g_%06d.jpg" % idx_of(t))


def crop(t):
    with Image.open(fp(t)) as im:
        im.load()
        c = im.convert("RGB").crop((L, T, R, B))
        return Image.open if False else c.copy()   # copy: buffer must outlive the file


def sheet(ts, out, cols=4, cell=400, label=24):
    ims = [(t, crop(t)) for t in ts]
    cw = cell; ch_ = int(cw * ims[0][1].height / ims[0][1].width)
    rows = (len(ims) + cols - 1) // cols
    canvas = Image.new("RGB", (cols * cw, rows * (ch_ + label)), (18, 18, 22))
    dr = ImageDraw.Draw(canvas)
    try:
        font = ImageFont.truetype("arialbd.ttf", 18)
    except Exception:  # noqa: BLE001
        font = ImageFont.load_default()
    for i, (t, im) in enumerate(ims):
        rr, cc = divmod(i, cols); y = rr * (ch_ + label)
        dr.rectangle([cc * cw, y, cc * cw + cw, y + label], fill=(150, 20, 20))
        dr.text((cc * cw + 5, y + 3), "t=%ds" % t, fill=(255, 255, 255), font=font)
        canvas.paste(im.resize((cw, ch_), Image.LANCZOS), (cc * cw, y + label))
    canvas.save(out, quality=90)
    return canvas.size


def main():
    mode = sys.argv[1]
    if mode == "grid":
        # 8 frames per sheet, sequential across the whole tail
        sd = os.path.join(D, "sheets-tail")
        os.makedirs(sd, exist_ok=True)
        n = 0
        for start in range(700, 1796, 40):
            ts = [t for t in range(start, min(start + 40, 1796), 5)]
            if not ts:
                continue
            p = os.path.join(sd, "tail_%04d.jpg" % ts[0])
            try:
                sheet(ts, p)
                n += 1
            except Exception as exc:  # noqa: BLE001
                print("sheet failed at", ts[0], exc)
        print("sheets:", n)
    elif mode == "one":
        t = int(sys.argv[2]); out = sys.argv[3]
        crop(t).save(out, quality=96)
        print("saved", out)
    elif mode == "zoom":
        t = int(sys.argv[2]); out = sys.argv[3]; scale = float(sys.argv[4])
        x, y, w, h = ((int(v) for v in sys.argv[5:9]) if len(sys.argv) >= 9
                      else (0, 0, R - L, B - T))
        c = crop(t).crop((x, y, x + w, y + h))
        c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
        lab = Image.new("RGB", (c.width, c.height + 28), (18, 18, 22))
        lab.paste(c, (0, 28))
        dr = ImageDraw.Draw(lab)
        try:
            font = ImageFont.truetype("arialbd.ttf", 20)
        except Exception:  # noqa: BLE001
            font = ImageFont.load_default()
        dr.text((6, 4), "t=%ds rect=%s x%.1f" % (t, (x, y, w, h), scale), fill=(255, 230, 90), font=font)
        lab.save(out, quality=96)
        print("saved", out, lab.size)


if __name__ == "__main__":
    main()