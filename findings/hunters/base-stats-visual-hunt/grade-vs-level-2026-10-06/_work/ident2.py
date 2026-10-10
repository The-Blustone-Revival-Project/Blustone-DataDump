"""Identity evidence sheet: rank2 hero (star3/4 numbers) vs IMG_5729 hero (star4/5)."""
import os
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
PRIOR = os.path.abspath(os.path.join(HERE, '..', '..',
                                      'hero-panel-level-images-2026-10-06'))
OUT = os.path.abspath(os.path.join(HERE, '..', 'img'))

JOBS = [
    (os.path.join(PRIOR, 'rank2-1024x911.jpg'), (185, 95, 305, 250),
     'rank2 review hero  (star3/LvMAX 3311 -> star4/Lv.1 4907)'),
    (os.path.join(PRIOR, 'rank2-1024x911.jpg'), (795, 350, 905, 500),
     'rank2 SUCCESS hero  (same hero, star4/Lv.1 = 4907)'),
    (os.path.join(OUT, '2019-03_IMG_5729-e1551694819888_20190331221452.png'),
     (270, 5, 430, 205),
     'IMG_5729 hero      (star4/Lv.MAX -> star5/Lv.1, NO numbers)'),
    (os.path.abspath(os.path.join(OUT, '_x2_IMG_5729.png')), (290, 10, 430, 210),
     'IMG_5729 (2019/03) hero  -- same art'),
    (os.path.join(PRIOR, '0d40a5e4a645fc6b96e767d64ac0878e-1-1024x904.jpg'),
     (200, 100, 300, 250),
     'review#2 hero  (DIFFERENT: blue eyes / ponytail)'),
    (os.path.join(PRIOR, 'rank1-1024x911.jpg'), (600, 150, 980, 560),
     'Kain 029 (DIFFERENT: adult male) 3311 @ star3 Lv.30'),
]

tiles = []
for p, box, cap in JOBS:
    if not os.path.exists(p):
        print('MISSING', p)
        continue
    im = Image.open(p).convert('RGB').crop(box)
    k = 320.0 / max(im.size)
    im = im.resize((max(1, int(im.width * k)), max(1, int(im.height * k))),
                   Image.LANCZOS)
    tiles.append((cap, im))

W = max(t[1].width for t in tiles) + 24
H = sum(t[1].height + 28 for t in tiles)
sheet = Image.new('RGB', (W, H), (18, 18, 22))
dr = ImageDraw.Draw(sheet)
y = 0
for cap, im in tiles:
    dr.text((8, y + 6), cap, fill=(255, 226, 120))
    sheet.paste(im, (12, y + 22))
    y += im.height + 28
out = os.path.join(OUT, '_identity_evidence.png')
sheet.save(out)
print('wrote', out, sheet.size)