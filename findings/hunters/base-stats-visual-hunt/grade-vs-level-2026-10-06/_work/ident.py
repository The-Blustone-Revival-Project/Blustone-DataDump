"""Side-by-side art comparison: rank1 Kain vs rank2 review hero vs 0d40a5e4-1 hero."""
import os
from PIL import Image

SRC = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '..', '..',
    'hero-panel-level-images-2026-10-06'))
OUT = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '..', 'img'))

# (file, box) -- boxes are (l,t,r,b) in native pixels
JOBS = [
    ('rank1-1024x911.jpg', (560, 120, 1000, 560), 'rank1_Kain_member_training'),
    ('rank2-1024x911.jpg', (150, 60, 500, 350), 'rank2_left_review_hero'),
    ('rank2-1024x911.jpg', (600, 340, 900, 500), 'rank2_right_success_hero'),
    ('0d40a5e4a645fc6b96e767d64ac0878e-1-1024x904.jpg',
     (0, 0, 1024, 904), 'rankup_review_2554_3827'),
]

tiles = []
for fn, box, label in JOBS:
    p = os.path.join(SRC, fn)
    if not os.path.exists(p):
        print('MISSING', fn)
        continue
    im = Image.open(p).convert('RGB').crop(box)
    k = 300.0 / max(im.size)
    im = im.resize((max(1, int(im.width * k)), max(1, int(im.height * k))),
                   Image.LANCZOS)
    tiles.append((label, im))
    print('%-30s %s -> %s' % (label, fn, im.size))

W = max(t[1].width for t in tiles) + 20
H = sum(t[1].height + 26 for t in tiles)
sheet = Image.new('RGB', (W, H), (24, 24, 28))
y = 0
try:
    from PIL import ImageDraw
    dr = ImageDraw.Draw(sheet)
except Exception:
    dr = None
for label, im in tiles:
    if dr:
        dr.text((6, y + 4), label, fill=(255, 230, 120))
    sheet.paste(im, (10, y + 20))
    y += im.height + 26
out = os.path.join(OUT, '_compare_rank1_rank2.png')
sheet.save(out)
print('wrote', out, sheet.size)