"""Build labelled contact sheets from the extracted PDF images so all 99 can be
screened by eye in a few views."""
import os
import sys

from PIL import Image, ImageDraw

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "pdfimg")
OUT = os.path.join(HERE, "pdfsheets")
PER = 12
CELL = 300
COLS = 4
LBL = 22

os.makedirs(OUT, exist_ok=True)
files = sorted(f for f in os.listdir(SRC)
               if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp")))
print("images: %d" % len(files))
sheets = 0
for i in range(0, len(files), PER):
    chunk = files[i:i + PER]
    rows = (len(chunk) + COLS - 1) // COLS
    sheet = Image.new("RGB", (COLS * CELL, rows * (CELL + LBL)), (24, 24, 28))
    d = ImageDraw.Draw(sheet)
    for j, name in enumerate(chunk):
        r, c = divmod(j, COLS)
        try:
            im = Image.open(os.path.join(SRC, name)).convert("RGB")
        except Exception:
            continue
        im.thumbnail((CELL - 6, CELL - 6))
        x = c * CELL + (CELL - im.width) // 2
        y = r * (CELL + LBL) + LBL + (CELL - im.height) // 2
        sheet.paste(im, (x, y))
        d.text((c * CELL + 4, r * (CELL + LBL) + 4),
               "%02d %s" % (i + j + 1, name[:36]), fill=(255, 220, 90))
    p = os.path.join(OUT, "sheet%02d.png" % (i // PER + 1))
    sheet.save(p)
    sheets += 1
    print("wrote %s  (%s .. %s)" % (os.path.basename(p), chunk[0], chunk[-1]))
print("sheets: %d" % sheets)
