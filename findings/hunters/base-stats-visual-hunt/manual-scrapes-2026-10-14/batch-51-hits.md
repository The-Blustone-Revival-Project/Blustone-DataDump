# Batch 51 hits (idx 2501-2550)

Lane: `findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/`
Crops: `hits/batch-51-2542.png` (1 HIT).
Zooms (lane folder, provenance only): `z51_2518_str`,
`z51_2519_str` (top Strength), `z51_2518_strength`,
`z51_2519_strength` (Defense), `z51_2518_top`, `z51_2519_top`
(Attack), `z51_2528_zero` (zero-digit), `z51_2542_badge`
(4-star green ring + Lv.1).
OCR (lane folder): `_tmp51_ocr/` (full-frame tesseract
`--tessdata-dir` `%TEMP%/opencode/tessdata`, `-l eng`, plus
zoom-crop OCR for 2518/2519/2528/2542).
Write/verify scripts: `_tmp51_dims.py`, `_tmp51_ocr.py`,
`_tmp51_zoom.py` through `_tmp51_zoom7.py`, `_tmp51_write.py`,
`_tmp51_verify.py` (kept in lane folder per rules).

## HITs: 1/50

### idx 2542: Elite Messenger Hermes, Proficient Hunter Lv.1, 4-star, Strength 4626 (catalog 023)
- File: `Screenshot_20180407-200700-55af6313df4cf8ba.png`
  (1440x2560). Crop: `hits/batch-51-2542.png`.
- Train Teammate; sword-class + fire-element icons; 4-star
  green-ring badge + Lv.1 ribbon (zoom-verified
  `z51_2542_badge`; OCR "Lu. 1" vs visual "Lv. 1", zoom
  wins); Train / Transcendence / Skill Training /
  Upgrade Equipment / Story.
- STAR NOTE: the Train badge shows a 4-star green ring,
  but the recruit-confirm frame idx 2549 shows Hermes
  with a 3-star gold badge (intra-batch star-display
  difference, recorded verbatim); catalog 023 lists star
  value 3.

## Near-hits (full numbers, hit=no per bar rules)

### idx 2518/2519: Wandering Fighter Proficient Hunter Lv.30 training pair, 8656 -> 9028
- Files: `Screenshot_2018-04-02-19-37-43-1bfeabed0ad694a9.png`
  / `Screenshot_2018-04-02-19-37-54-42ea1bec71401071.png`
  (540x960). 3-star badge + Lv.30 ribbon (full-view);
  sword-class + fire-element icons; red Advance button,
  Transcendence greyed.
- Strength 8656 -> 9028 (+372, zoom-verified
  `z51_2518_str` / `z51_2519_str`, header-overlapped last
  digit; first visual read 8654/9024 corrected by zoom).
  Life 1273 -> 1320; Attack 808 -> 838 (zoom-verified
  `z51_2518_top` / `z51_2519_top`); Defense 585 -> 607
  (zoom-verified `z51_2518_strength` /
  `z51_2519_strength`); Attack Speed 8; sub-stats
  unchanged 31 / 214 / 0 / 13 / 40 / 0 / 0 / 23
  (OCR cross-check `_tmp51_ocr/2518.txt` confirms all
  but Strength, which OCR missed under the header).
- No hero name on frame (title "Wandering Fighter" is
  the character title, not a name); catalog blank.
  Hit=no.
- OCR-vs-zoom: OCR "ing Fightey" vs visual "Wandering
  Fighter"; OCR "o" for 0 in Armor Penetration /
  Strengthen / Elemental Resistance.

### Recruit splashes with level + stars, no stats (all hit=no)
- idx 2510: Noble Spear Natalia, 3-star, Lv.1, Offense +
  Ice, +1000 (catalog 037).
- idx 2511: Robot Engineer Edward, 3-star, Lv.1, Defense
  + Electricity, +1000 (catalog 041). ELEMENT NOTE:
  client "Electricity" vs catalog "Lightning" (extends
  the batch-29/30/32/34/38/40/43/48 Electricity arc).
- idx 2538: Death Metal Preacher Bruce Bang, 1-star,
  Lv.1, Support + Ice, +1000 (catalog 016); sic:
  "BRUSB" mirrored-brand guitar-headstock print.
- idx 2540: Strange Twins Lily & Lyla, 4-star (green),
  Lv.1, Offense + Fire, +1000 (catalog 047).
- idx 2544: The Frost Witch Octavia, 3-star, Lv.1,
  Offense + Ice, +1000 (catalog 028). TITLE NOTE:
  client "The Frost Witch" vs catalog "Frost Witch".
- Recruit-confirm chain (no level ribbons, hit=no):
  idx 2548 Immortal One Karl Steiner, 3-star gold,
  Offense + Electricity (catalog 012; Karl-class exact
  match; Electricity vs Lightning); idx 2549 Elite
  Messenger Hermes, 3-star gold, Offense + Fire
  (catalog 023); idx 2550 The Frost Witch Octavia,
  3-star gold, Offense + Ice (catalog 028).

## Cross-batch pairing notes

- Wandering Fighter training pair: idx 2518 (8656,
  1273/808/585/8 + full sub-stats) -> idx 2519 (9028,
  1320/838/607/8, sub-stats unchanged). Before->after
  every stat recorded.
- Skill-training 4-tab chain (same mats 1/5 + 76/5 +
  37/3, coins 114156, Begin Training 900, all
  Lv.40/40): idx 2505 Reckless Charge (Damage
  2819 -> 2845) -> idx 2506 Immunity (Duration
  2.69Sec. -> 2.73Sec.) -> idx 2507 Instinctive Attack
  (Damage 12.00% -> 12.30%) -> idx 2508 Reduced Enemy
  Defense (Defense 26.0% -> 26.40%).
- Hunter-list scroll seq (37/51, same account): idx
  2529 (18662 head ... bottom Lv.1 x3 cut) -> 2530
  (3956 ... 2284 triple-dupe + 2248 bear pair) ->
  2531 (2241 ... 2032 dupe ... 380, empty slots).
  Roster endpoints 18662 -> 380.
- Build-team scroll pairs: idx 2514 -> 2515 (top team
  14383/11578/7826/2970, rookie tail
  2381/2191/2060/2027/1809); idx 2526 -> 2527 (top
  team 13981/15344, locked mid-ladder 6963-2767).
- Duplicate frames (same timestamp, different hash):
  idx 2523 = 2524 (Hunter List 27/51); idx 2533 = 2534
  (Hunter List 13/45).
- 32/51 scroll pair (perf-overlay account): idx 2536
  (14119 head, overlay C:40 B:32 M:1335MB 1709MHz) ->
  2537 (2824 ... 2231 dupe ... 842 dupe, overlay C:44
  B:32 M:1354MB 1306MHz).
- Hermes intra-batch arc: idx 2542 Train (4-star green
  badge, Lv.1, Strength 4626, HIT) -> idx 2549
  recruit-confirm (3-star gold badge, no level).
- Octavia intra-batch arc: idx 2544 splash (3-star,
  Lv.1) -> idx 2550 confirm (3-star gold).
- Trace payouts: idx 2512 (7x: 4/5/5/4/3/3/3) /
  idx 2543 (10x: 4/5/3/3/5/4/3/5/4/3); counts 3/4/5
  only, both "large number of hunter traces".
- Zero-digit promo: idx 2528 Legendary Selection
  Request, Current Amount 0 (zoom-crop OCR "0" beats
  full-frame OCR "O"); 28-day consecutive-attendance
  collection note.

## Most valuable economy/mechanic readings

- Skill-training cost curve (idx 2505-2508): Lv.40/40
  training costs 900 coins with mats 1/5 + 76/5 +
  37/3 and wallet 114156 coins; effect deltas are
  last-level-scale (+26 damage, +0.04Sec.,
  +0.30%, +0.40%).
- Manda-price promo (idx 2520): Limited Time Hot Deal,
  Fuel 1400 for 180 -> 116 Manda, one-shot purchase,
  00:47:46 timer; wallet fuel 18/60 + 2/10.
- Supply-office ladder (idx 2516): Lottery Mouse likes
  walnuts! x40 / x3 / x4 / x2 trace rows; Attendance
  / Activity / Special Supply tabs.
- Missing-hunter gating (idx 2517): Electric Abyss
  UNIQUE (Levko, 0day 00:59:17, 61/80) + Giant
  Shelter RARE (0day 00:06:42, 61/80); fuel 153/60;
  sic "0day" (zero) on both timers.
- Wandering Fighter train deltas (idx 2518/2519,
  zoom-verified): Strength 8656 -> 9028; Life
  1273 -> 1320; Attack 808 -> 838; Defense 585 ->
  607; Attack Speed 8 fixed; sub-stats fixed.
- Hermes HIT baseline (idx 2542): Proficient Hunter
  Lv.1, Strength 4626, 4-star green-ring badge.
- Mission ledgers: idx 2513 Non-melting Forest Area 6,
  Team Level 30, 8649 / 488 / 419 / 463, Rupees +136,
  items 1/1/1/1; idx 2546 Forest of the Wanderers
  Area 1, Team Level 33, 14158 / 5686 / 6314 / 504,
  Rupees +159, blue crystal x1.
- Rank-ladder help (idx 2539): Yuri (Korea) 1191 Point
  Lv.40 1st vs Bibi (Italy) 1185 Point Lv.62 2nd
  (My Rank); three-league ranking explainer.
- 11-pull result (idx 2522): 4x 1-star / 2x 2-star /
  4x 3-star / 1x 4-star (green bunny); "One more
  time! 300".

## Non-ASCII names (transliterated, for searchability)

- idx 2503: McGue. idx 2505: RoninV. idx 2506:
  WolfyBear. idx 2510: Natalia. idx 2511: Edward.
  idx 2517: Levko. idx 2532: Moon_Shadow. idx 2535/
  2539: Bibi. idx 2538: Bruce Bang (BRUSB sic).
  idx 2540: Lily & Lyla. idx 2541: Sunny. idx 2542/
  2549: Hermes. idx 2544/2550: Octavia. idx 2547:
  Estelle. idx 2548: Karl Steiner. idx 2539: Yuri.
  No Korean-script names in batch.

## Contaminants

- None. Zero-contaminant batch: no OS overlays, no
  external photos. (Third-party perf-overlay digits
  on idx 2536/2537 are on-device overlay text over
  game content, transcribed verbatim, not game data.)

## Sic list

- "Would you like to recruit the followi-g hunter?"
  (idx 2548/2549/2550, line-wrap split, kept
  verbatim).
- "BRUSB" (idx 2538, mirrored-brand guitar-headstock
  print, kept verbatim).
- "0day" x2 (idx 2517, zero not letter O, both
  abyss/shelter timers, kept verbatim).
- "Through launching a powerful charge, reduce your
  enemy defense." (idx 2508, no possessive on enemy,
  verbatim).
- "Collect it when you attend 28 days consecutively"
  (idx 2528, collection copy, frame-cut tail).
- "You know, fishing in blustone would be fun"
  (idx 2532, lowercase game name in player mail,
  verbatim).
- "Experiment #2" (idx 2541, client hash-form vs
  catalog 022 "Experiment 2").
- "The Frost Witch" (idx 2544/2550, client article vs
  catalog 028 "Frost Witch").
