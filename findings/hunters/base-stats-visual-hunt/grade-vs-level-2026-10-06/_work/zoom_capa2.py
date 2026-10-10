import os
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(HERE, '..', '..',
                                   'hero-panel-level-images-2026-10-06',
                                   'capa2-1024x911.jpg'))
OUT = os.path.abspath(os.path.join(HERE, '..', 'img'))

JOBS = [
    ((545, 590, 1010, 700), 'capa2 success: 攻撃力/防御力/HP  before -> after'),
    ((600, 145, 1010, 200), 'capa2 success: 戦闘力 2326 -> 2704'),
    ((20, 300, 470, 360), 'capa2 review: 戦闘力 2326 -> 2704'),
    ((20, 195, 300, 240), 'capa2 target badge: Bear 036 star3 / Lv.1'),
    ((20, 460, 300, 580), 'capa2 material: 2326 / 2326 at Lv.1'),
]

tiles = []
for box, cap in JOBS:
    im = Image.open(SRC).convert('RGB').crop(box)
    k = 1000.0 / max(im.size)
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
out = os.path.join(OUT, '_zoom_capa2_core_stats.png')
sheet.save(out)
print('wrote', out, sheet.size)