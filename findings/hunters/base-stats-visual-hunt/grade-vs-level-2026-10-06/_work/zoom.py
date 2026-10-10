"""High-magnification crops of every 戦闘力 / Lv / ★ reading used in the report."""
import os
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(HERE, '..', '..',
                                   'hero-panel-level-images-2026-10-06'))
OUT = os.path.abspath(os.path.join(HERE, '..', 'img'))

# (file, (l,t,r,b), caption)
JOBS = [
    ('rank2-1024x911.jpg', (100, 330, 500, 410),
     'rank2 LEFT review: 戦闘力UP 3311 -> 4907'),
    ('rank2-1024x911.jpg', (600, 430, 900, 500),
     'rank2 RIGHT success: 3311 -> 4907 under badges'),
    ('rank2-1024x911.jpg', (110, 250, 220, 350),
     'rank2 LEFT before badge (3 stars / Lv.MAX)'),
    ('rank2-1024x911.jpg', (270, 250, 380, 350),
     'rank2 LEFT after badge (4 stars / Lv.1)'),
    ('0d40a5e4a645fc6b96e767d64ac0878e-1-1024x904.jpg', (100, 330, 500, 410),
     'review#2 LEFT: 戦闘力UP 2554 -> 3827'),
    ('0d40a5e4a645fc6b96e767d64ac0878e-1-1024x904.jpg', (600, 430, 900, 500),
     'review#2 RIGHT success: 2554 -> 3827'),
    ('rank1-1024x911.jpg', (700, 520, 1000, 620),
     'rank1 Kain member-training 戦闘力 3311'),
    ('rank1-1024x911.jpg', (520, 620, 1024, 700),
     'rank1 Kain badge ★3 / Lv. 30'),
]

tiles = []
for fn, box, cap in JOBS:
    p = os.path.join(SRC, fn)
    im = Image.open(p).convert('RGB').crop(box)
    k = 900.0 / max(im.size)
    im = im.resize((max(1, int(im.width * k)), max(1, int(im.height * k))),
                   Image.LANCZOS)
    tiles.append((cap, im))

W = max(t[1].width for t in tiles) + 24
H = sum(t[1].height + 30 for t in tiles)
sheet = Image.new('RGB', (W, H), (18, 18, 22))
dr = ImageDraw.Draw(sheet)
y = 0
for cap, im in tiles:
    dr.text((8, y + 6), cap, fill=(255, 226, 120))
    sheet.paste(im, (12, y + 24))
    y += im.height + 30
out = os.path.join(OUT, '_zoom_all_numbers.png')
sheet.save(out)
print('wrote', out, sheet.size)