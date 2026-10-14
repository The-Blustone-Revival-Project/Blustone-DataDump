# Batch 53 hits (idx 2601-2650)

Lane: `findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/`
Crops: `hits/batch-53-2607.png` (993x1575), `hits/batch-53-2610.png`
(993x1575), `hits/batch-53-2615.png` (993x1575),
`hits/batch-53-2640.png` (663x1050), `hits/batch-53-2641.png`
(1325x2428), `hits/batch-53-2647.png` (1080x1820),
`hits/batch-53-2649.png` (497x788) — 7 HITs.
Zooms (lane folder, provenance only): `z53_2607_badge`
(gold 3-star + Lv.1), `z53_2610_badge`, `z53_2615_badge`,
`z53_2640_badge`, `z53_2641_badge`, `z53_2647_badge` (blue
5-star ring + Lv.15), `z53_2649_badge`, plus cut-digit zooms
`z53_2620_bottom` (Lv.1 1954 / Lv.1 784), `z53_2629_bottom`
(Lv.24 2892 / Lv.MAX 2730 / Lv.MAX 2704), `z53_2632_bottom`
(5976 / 5593 Locked / Lv.1 4141), `z53_2633_top` (Lv.MAX 2984
bear Locked / 2676 Locked / Lv.MAX 2533).
OCR (lane folder): `_tmp53_ocr/` (full-frame tesseract
`--tessdata-dir` `%TEMP%/opencode/tessdata`, `-l eng` on 2644
+Manda 299 agree+ and 2645 +headline/Metron/600 confirmed,
timer+198 OCR-missed, visual wins+).
Write/verify scripts: `_tmp53_dims.py`, `_tmp53_dims.tsv`,
`_tmp53_zoom.py`, `_tmp53_ocr.py`, `_tmp53_write.py`,
`_tmp53_verify.py` (kept in lane folder per rules).

## HITs: 7/50

### idx 2607: Yuri, Ice Skating Fairy, Lv.1, 3-star, Offense + Ice (catalog 045)
- File: `Screenshot_20180414-232447-7c4733b3cf2ddc14.png`
  (1080x1920). Crop: `hits/batch-53-2607.png`.
- Recruited; 3-star gold badge + Lv.1 ribbon (zoom-verified
  `z53_2607_badge`: gold ring, 3 gold stars, Lv.1 ribbon +
  ice-fist pip); +1000 coins; Share; See Details / Okay.
- Chain: recruit 2607 -> advancement 2608 (Experienced
  Lv.MAX 2552 -> Proficient Lv.1 4238, Triple Lutz).

### idx 2610: Karl Steiner, Immortal One, Lv.1, 3-star, Offense + Electricity (catalog 012)
- File: `Screenshot_20180415-143911-8a77c93ca27e4f9d.png`
  (1080x1920). Crop: `hits/batch-53-2610.png`.
- Recruited; 3-star gold badge + Lv.1 ribbon
  (`z53_2610_badge`); +1000 coins.
- Element wording: game shows "Electricity", catalog 012
  lists Lightning. DUPLICATE pair with idx 2615 (same
  art/text, next day).

### idx 2615: Karl Steiner, Immortal One, Lv.1, 3-star (duplicate of 2610)
- File: `Screenshot_20180416-002049-df32980642e3d52e.png`
  (1080x1920). Crop: `hits/batch-53-2615.png`.
- Same recruit frame as 2610 (zoom `z53_2615_badge`).

### idx 2640: Lily & Lyla, Strange Twins, Lv.1, 4-star, Offense + Fire (catalog 047)
- File: `Screenshot_2018-04-20-04-41-51-2e62aab5ce068190.png`
  (720x1280). Crop: `hits/batch-53-2640.png`.
- Recruited; 4-star GREEN-ring badge + Lv.1 ribbon;
  +1000 coins.
- STAR NOTE: 4-star green ring on a recruit frame (3-star
  gold is the norm for confirms in this batch, e.g. 2607 /
  2610 / 2641 / 2649); matches catalog 047 star value 4.
- Recruit chain: 2640 -> 2641 (Kain) -> 2649 (Bibi).

### idx 2641: Kain, Steely Bodyguard, Lv.1, 3-star, Defense + Electricity (catalog 029)
- File: `Screenshot_20180420-112523_Blustone-65b77dc3ccc3dd1e.jpg`
  (1440x2960). Crop: `hits/batch-53-2641.png`.
- Recruited; 3-star gold badge + Lv.1 ribbon
  (`z53_2641_badge`); +1000 coins.
- Element wording: game "Electricity" vs catalog Lightning.

### idx 2647: Octavia, The Frost Witch, Master Hunter Lv.15, 5-star, Strength 13541 (catalog 028)
- File: `Screenshot_20180422-012105_Blustone-5b9864ba7b94e62a.jpg`
  (1080x2220). Crop: `hits/batch-53-2647.png`.
- Train Teammate; sword-class + ice-element icons; 5-star
  blue-ring badge + Lv.15 ribbon (zoom-verified
  `z53_2647_badge`: cyan-blue ring, 5 white stars, Lv.15
  ribbon); crown + lock icons; Train / Transcendence /
  Skill Training; Upgrade Equipment greyed; Story.
- Title discrepancy: game title "The Frost Witch" vs
  catalog 028 "Frost Witch"; idx 2637 unlocks skill
  "Frost Witch" (no article) on the same hero.
- Chain: 2637 advancement (7254 MAX -> 10206 Lv.1 Master)
  -> 2647 Master Lv.15 13541.

### idx 2649: Bibi, Wolf Child, Lv.1, 3-star, Offense + Electricity (catalog 040)
- File: `Screenshot_2018-04-23-17-54-10-76eda1fe4d6dd4f4.png`
  (540x960). Crop: `hits/batch-53-2649.png`.
- Recruited; 3-star gold badge + Lv.1 ribbon
  (`z53_2649_badge`); +1000 coins.
- Element wording: game "Electricity" vs catalog Lightning.

## Near-hits (hit=no, recorded for trails)
- 2608 Yuri advancement (2552 MAX -> 4238 Lv.1, Triple
  Lutz): no star/HP-ATK-DEF line, rankup frame.
- 2621 bunny advancement (7778 MAX -> 10051 Lv.1, Blue
  Speed): nameless.
- 2623 eyepatch Advancement Match (1424 -> 1424, fee 0):
  nameless, zero-fee economy.
- 2626 Halloween Witch Riko card-detail: name+title but no
  level/stars/stats; catalog blank (024/024_1 mismatch).
- 2627/2628 orange-braid Advancement Match chain
  (2570 -> 2783 across frames, fee 0): nameless.
- 2637 dark-wolf advancement (7254 -> 10206, Frost Witch
  skill): nameless but chained to HIT 2647.
- 2636 Electric Abyss result: team levels shown but
  before->after stat pairs absent.
