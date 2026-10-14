# Batch 64 hits (idx 3151-3200)

Lane: `findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/`
Crops: `hits/batch-64-3151.png`, `hits/batch-64-3158.png`,
`hits/batch-64-3163.png` (3 HITs, full frames).
Zooms (lane folder, provenance only): `z64_3151_badge`
(green ring, 4 gold stars, Lv.1 ribbon), `z64_3158_badge`
(blue ring, 5 light-blue stars, Lv.MAX ribbon),
`z64_3163_badge` (blue ring, 5 light-blue stars, Lv.MAX
ribbon), `z64_3175_badge` (Teresa popup, green 4-star
ring), `z64_3168_mid`/`z64_3168_nums`/`z64_3169_top`/
`z64_3169_bot` (HUD provenance), `z64_3151_left`/
`z64_3158_left`/`z64_3163_left`/`z64_*_band` (badge
search trail).
OCR (tesseract `--tessdata-dir` `%TEMP%/opencode/tessdata`,
`-l eng`; badge art + stylized HUD fonts blank/garbled so
zoom/eye wins): Kamala frame OCR confirms Lv.1/30, 7060,
HP 1323, ATK 613, 892, 1/40 row; HUD zoom OCR blank.
Write scripts: `_tmp64_work.py`, `_tmp64_write.py`
(kept in lane folder per rules).

## HITs: 3/50 (all Train views, zoom-verified badges)

### idx 3151: Kamala, Leader of the White Forest, Lv.1/30, 4-star (catalog 083)
- File: `Screenshot_20200116-140043.png`
  (720x1280). Crop: `hits/batch-64-3151.png` (full frame).
- Train view; green ring + 4 gold stars + Lv.1 ribbon
  (zoom-verified `z64_3151_badge`; OCR blank on badge art,
  zoom wins); Strength 7060; HP 1323; ATK 613; DEF 892;
  skills 1/40 x4 (one locked); Defense shield + Ice-blue
  crystal Elemental icons (client shows icons only, no
  element name text).
- Role/element match catalog 083 exactly.

### idx 3158: Karl Steiner, Immortal One, Lv.30/30, 5-star (catalog 012)
- File: `Screenshot_20200126-013542-97628b245a6f2bfc.png`
  (720x1280). Crop: `hits/batch-64-3158.png` (full frame).
- Train view; blue ring + 5 light-blue stars + Lv.MAX
  ribbon (zoom-verified `z64_3158_badge`); Strength 37977;
  HP 3574; ATK 2083; DEF 1439; skills 50/50 x5; Offense
  swords + yellow-hand Elemental icons.
- Catalog 012 base is 3-star Lightning Offense, so the
  blue 5-star badge = transcended 5-star.

### idx 3163: Heidi, Girl with Two Faces, Lv.30/30, 5-star (catalog 044)
- File: `Screenshot_20200205-185007-ac5c8419a22464be.png`
  (1080x2160). Crop: `hits/batch-64-3163.png` (full frame).
- Train view; blue ring + 5 light-blue stars + Lv.MAX
  ribbon (zoom-verified `z64_3163_badge`); Strength 28390;
  HP 2864; ATK 1679; DEF 1296; skills 50/50 x5.
- Catalog 044 base is 3-star Fire Offense, so the blue
  5-star badge = transcended 5-star.

## Near-hits (hit=no per bar rules)

- idx 3152: Kamala Stat Details popup (Base HP 1323 ATK
  613 DEF 892 SPD 7; crit 13/207; pen 0; elem enh 0;
  block 28/45; elem res 9; regen 30); popup shows no
  badge itself, identity carried from 3151.
- idx 3160: 4-star recruit menu (Geranium / Judith /
  Selene / Audrey / Blondie with full titles); no
  levels/stars/stats per card.
- idx 3175: Teresa dispatch popup, zoom-verified green
  4-star badge, Trace 150/160, Entrance 0/3; no level or
  HP/ATK/DEF.
- idx 3178-3200 (23x): recruit splash crops only, no
  names/levels/stars in frame.
