#!/usr/bin/env python
"""Build labelled contact sheets so a whole screenshot corpus can be triaged
for stat panels in a small number of image reads.

Usage: montage.py <out_prefix> <cols> <cell_w> <img1> <img2> ...
"""
import os, sys, math
from PIL import Image, ImageDraw

out_prefix = sys.argv[1]
cols = int(sys.argv[2])
cell_w = int(sys.argv[3])
paths = sys.argv[4:]
if not paths:
    print('no inputs')
    sys.exit(0)

cells = []
for p in paths:
    try:
        im = Image.open(p)
        im = im.convert('RGB')
        r = cell_w / im.width
        im = im.resize((cell_w, max(1, int(im.height * r))), Image.LANCZOS)
        cells.append((os.path.basename(p), im))
    except Exception as e:
        print('skip', p, e)

per = 12
sheets = math.ceil(len(cells) / per)
for s in range(sheets):
    chunk = cells[s * per:(s + 1) * per]
    if not chunk:
        break
    rows = math.ceil(len(chunk) / cols)
    ch = max(c[1].height for c in chunk) + 16
    W = cols * cell_w
    H = rows * ch
    sheet = Image.new('RGB', (W, H), (20, 20, 24))
    d = ImageDraw.Draw(sheet)
    for i, (name, im) in enumerate(chunk):
        cx, cy = (i % cols) * cell_w, (i // cols) * ch
        sheet.paste(im, (cx, cy + 16))
        d.rectangle([cx, cy, cx + cell_w - 1, cy + 15], fill=(200, 30, 30))
        d.text((cx + 3, cy + 3), name[:60], fill=(255, 255, 255))
    out = '%s-%d.png' % (out_prefix, s + 1)
    sheet.save(out)
    print('saved', out, sheet.size, [c[0][:40] for c in chunk])
