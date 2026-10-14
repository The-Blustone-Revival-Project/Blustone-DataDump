# Batch 50 hits (idx 2451-2500)

Lane: `findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/`
Crops: `hits/batch-50-2489.png`, `hits/batch-50-2493.png`.
Zooms (lane folder, provenance only): `z50_2457_rows`, `z50_2473_cry`,
`z50_2490_str`, `z50_2459_dbg2`, `z50_2489_badge`, `z50_2493_badge`,
`z50_2462_nums`, `z50_2484_nums`, `z50_2490_stats`, `z50_2499_pct`,
`z50_2495_check`, `z50_2496_check` (+ superseded `z50_2459_dbg`,
`z50_2495_grid`, `z50_2495_grid2` kept, not evidence).
OCR (lane folder): `_tmp50_ocr/` (2480/2486/2487/2496 zero-digit art,
2499 1600% promo, tesseract `--tessdata-dir` `%TEMP%/opencode/tessdata`,
`-l eng`).
Write script: `_tmp50_write.py` (+ `_tmp50_dims.py`, kept in lane
folder per rules).

## HITs: 2/50

### idx 2489: Wolf Child Bibi, Master Hunter Lv.1, 5-star, Strength 10159 (catalog 040)
- File: `Screenshot_2018-03-28-17-55-07-528201ceec983ec5.png` (720x1280).
  5-star blue ring + Lv.1 ribbon + Lv.1 header (all zoom-verified
  `z50_2489_badge`); Strength 10159; swords-class + yellow-hand
  Elemental icons; Train/Transcendence/Skill Training;
  Upgrade Equipment greyed / Story; chat "HASHBROWNBOI: the crowd
  is S ...".
- Crop: `hits/batch-50-2489.png`.

### idx 2493: The Girl We Love Lily & Lyla, Master Hunter Lv.16, 5-star, Strength 17295 (catalog 047)
- File: `Screenshot_2018-03-29-11-30-45-0240a745d6ab6700.png`
  (1440x2560). 5-star blue ring (zoom-verified `z50_2493_badge`);
  Lv.16; Strength 17295; red peace-hand Elemental icon (=Fire,
  matches 047); 5 skills; Upgrade Equipment greyed / Story.
- TITLE DISCREPANCY: catalog 047 title "Strange Twins" vs client
  "The Girl We Love...". Name truncated "Lily & Lyl..." on frame,
  full "Lily & Lyla" per catalog 047. 5-star ring vs base rarity 4
  (advancement).
- Crop: `hits/batch-50-2493.png`.

## Near-hits (full numbers, hit=no per bar rules)

### idx 2490: Train Teammate Proficient Hunter Lv.30 (Wandering Fighter Balian, catalog 019)
- File: `Screenshot_2018-03-29-02-05-09-63f46a4ada72a405.png`
  (540x960). 4-star green Lv.MAX badge; Life 1273 / Attack 808 /
  Defense 585 / Attack Speed 8 (zoom-verified `z50_2490_stats`);
  Critical Damage Chance 31 / Critical Damage 213 / Armor
  Penetration 0; Block Chance 13 / Block Resistance 40 /
  Strengthen Elemental Attributes 0 / Elemental Attack Resistance
  0 / HP Regen 23; "Stat Details : Attack".
- Strength 864x: 4th digit hidden behind home icon
  (zoom `z50_2490_str`) - never invented. Name partly covered by
  "Cryprobowser: Big news from t..." toast, chain-inferred from
  art + idx 2462/2484 trail. Hit=no.
- TITLE DRIFT (see below).

### idx 2462 / 2484: Balian transcendence pair (catalog 019)
- Idx 2462 (`...-07-13-20-...`, 540x960): Wandering Fighter
  Balian, Lv.16 chibi, "Successfully transcended.", Strength
  4919 -> 5536; Attack 579 -> 637; Defense 422 -> 464; Life
  909 -> 999 (before-values zoom `z50_2462_nums`).
- Idx 2484 (`...-11-34-25-...`, 540x960): same hero, Lv.MAX
  chibi, Strength 7279 -> 8016; Attack 694 -> 757; Defense
  507 -> 553; Life 1093 -> 1193 (before-values zoom
  `z50_2484_nums`). Same-account trail (leveled between).
- No star badges on frame. Hit=no.
- TITLE DRIFT: client "Wandering Fighter" vs catalog 019
  "Wandering Swordsman" (all three Balian frames: 2462/2484/2490).

### Recruit splashes with level + stars, no stats (all hit=no)
- idx 2476: Strange Old Man Dumble, 3-star, Lv.1, Defense + Ice,
  +1000 (catalog 048).
- idx 2482: Walking Disaster Nene, 3-star, Lv.1, Defense + Ice,
  +1000 (catalog 003).
- idx 2479: Notorious Jail-breaker Papillon hidden-ruins frame,
  3-star, no level ribbon (catalog 043; element icon-read only).
- 10-pull grids without names (hit=no): idx 2451/2452 (6x1-star
  + 4x2-star, identical session); idx 2481 (4x1/3x2/3x3, 2 NEW);
  idx 2500 (8x1 + 2x3 gold: bunny-cap purple hair + wolf-ears
  Bibi center).

## Cross-batch pairing notes

- Balian chain: idx 2462 Transcendence (4919 -> 5536,
  579/422/909 -> 637/464/999) -> idx 2484 Transcendence
  (7279 -> 8016, 694/507/1093 -> 757/553/1193) -> idx 2490
  Train Lv.30 (864x cut, 1273/808/585/8 + full sub-stats).
  Before->after every stat recorded except cut Strength digit.
- 1600% promo (idx 2499): coin x80000 (zoom `z50_2499_pct`) +
  Veteran Point Gift Certificate 3 ("huge amount of Rupee") -
  extends batch-48 idx 2353 (cert 1, Rupee) / idx 2379 (cert 3,
  Fuel). OCR misreads "1600%" as "41600%"; visual zoom wins
  (same as batch-48).
- X_man_20000 same-account trail: idx 2460 Fight Club win
  (+15 VP, chip x10) -> 2471 dispatch complete (24 dispatches,
  Team Lv.34, Rupees +1635) -> 2473 missing-hunter board (fuel
  103/60) -> 2495 village hub (fuel 69/60, Rank 7069) ->
  2497 Midgard story -> 2498 profile (Lv.29, reg 03/14/2018,
  35509 power, 1961/6999 league).
- Flip-recruit pair: idx 2454 (1 gold 3-star revealed) ->
  idx 2455 (2 gold dupes).
- Cryogenic wrap-split: idx 2473 "Cry-/genic Abyss"
  zoom-verified NOT a typo (cf batch-48 idx 2383 "Volcanic
  Ab yss").
- Pair-display anomaly: idx 2495/2496 pair-view labels got
  swapped; both files re-verified by single full-view reads
  (2495 = village hub, 2496 = bunny-girl art). A defense-team
  frame seen once in the bad pair matches no batch-50 file and
  is discarded as non-batch evidence (not recorded in TSV).

## Most valuable economy/mechanic readings

- Ice-hunter banner (idx 2456): 3-star ice-type chances tripled
  (+300%, 300% UP), Time Left 85:18:20; Recruit 30 / 10+1
  Recruit 300 (2-star-or-above guaranteed); wallet 34 gems /
  3 / 1 scrolls; Hunter Recruitment Mileage 3/4 stars.
- Advancement Match pricing (idx 2483): 4-star green Lv.MAX ->
  5-star blue Lv.1, Power 7892 -> 10884; 8-material board
  (4908/5843/5554/7029/3496/6652/6686/6760);
  Level-Up Advancement 60000 coins; wallet 203159. Material
  hunters "will be spent and will no longer be in the
  dormitory."
- Challenge Invitation economy (idx 2477/2478): LIMITED popup
  100 -> 59 Manda, "Available only once", timer 01:30:44;
  Fight Club shop: Current 2/10, Daily Purchase 6/10, Rupees
  5000 / Coupon 1 (greyed) / Manda 5; wallet 42677 / 57 / 0;
  "if you receive a Challenge Invite, you cannot refuse a
  fight."
- Mirage Forest event (idx 2467): Time remaining 257:11:12;
  "Using identical hunters as the mirage-hunters will help you
  clear the stage easier"; 0 fragments; My Rank 5073; Stage 5
  Lapis / Bruce Bang; Stage 10 Captain / Locke.
- Dispatch ledger (idx 2470/2471): progress board 22/32 ...
  23/40, "To dispatch 3/3"; completion: Team Lv.34,
  14285/15026/11951/5235, Rupees +1635, scroll x7, blue ore
  x25, ticket x1, green gem x2.
- Mirage victory ledger (idx 2472): Forest of Mirage Area 5,
  3 stars, Team Lv.34, 15142/1276/1305/1292, Rupees +67,
  green gem x2.
- Missing-hunter gating (idx 2473): Cryogenic Abyss UNIQUE
  2/80 (0day 00:55:05, Search Complete) + Crimson Chasm 12/40
  (1day 13:10:15, Explorations Left 2); Easy/Normal/Hard.
- Assignments pair (idx 2468/2469): Bonus Goal 6/7 vs 3/7
  boards (gem x5/meat x1/fleur x20); Check In coin x1000;
  Recruit 0/2, Train Skills 0/3; Veteran Expert 2, 4270/5120.
- Debug provenance (idx 2459): "C:42 B:33 M:1237MB 480MHz"
  (zoom-verified `z50_2459_dbg2`).
- Registration anchor (idx 2498): Level 29, 03/14/2018,
  35509 Fight Club attacking power, 1961/6999 league.
- Reddit leak (idx 2474): New Hunter Bright (Little Match Boy,
  catalog 049 text-only): Small Match Flame (Forward
  Regeneration) "continoulsy" [sic]; Camp Fire (Entire Team
  Regeneration) (4 Star Skill); Warm Light (Entire Team
  Regeneration) (5 Star Skill).

## Non-ASCII names (transliterated, for searchability)

- idx 2464: YallNeedJesus. idx 2475: 雷克萊斯 (Taiwan);
  Sister (Thailand); jimuri (Mexico); Rennnnnn (Singapore);
  小龜JAIII (Hong Kong); 霸王熊 (Taiwan). idx 2490:
  Cryprobowser. idx 2460: DXaeu. idx 2467: Lapis; Bruce Bang;
  Captain; Locke. idx 2476: Dumble. idx 2482/2500: Nene.
  idx 2488/2494: Natalia. idx 2479: Papillon. idx 2489: Bibi.
  idx 2493: Lily; Lyla. idx 2495: 瞪間永恒 (guild) + "...来的".
  idx 2496: none. idx 2500: Terrytory. idx 2481: Levko.
  idx 2451/2454: BoxHero. X_man_20000 throughout.

## Contaminants

- idx 2459: woman's-face photo overlay at right edge (external).
- idx 2461: Android volume-media overlay over minigame frame.
- idx 2474: full external Reddit screenshot (r/visualshower
  post over game art; kept as other with transcription).

## Sic list

- "continoulsy" (idx 2474, Reddit leak verbatim).
- "Stat Details : Attack" (idx 2490, spaced-colon verbatim).
- "Don't forget tomorrow's Goals!" (idx 2495, village toast).
- "Terrytory" (idx 2500, notification sender verbatim).
- "Proficient Hunter" / "Master Hunter" tier names (idx 2490 /
  2489/2493, verbatim).
