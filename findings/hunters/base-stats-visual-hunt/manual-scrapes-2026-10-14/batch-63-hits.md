# Batch 63 hits (idx 3101-3150)

Lane: `findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/`
Crops: `hits/batch-63-3108.png`, `hits/batch-63-3122.png` (2 HITs,
both full-frame recruit splashes).
Zooms (lane folder, provenance only): `z63_3108_name` (3-star gold
badge + Lv.1 ribbon + Beckhen nameplate) / `z63_3122_name` (4-star
green badge + Lv.1 ribbon + Teresa nameplate) / `z63_3150_stats`
(equipment stat block). OCR: tesseract `--tessdata-dir`
`%TEMP%/opencode/tessdata`, `-l eng` on `z63_3150_stats`
(Strength/HP/ATK/DEF/speed lines confirm) and `z63_3108_name`
(Beckhen/Offense/Ice confirm); zoom wins elsewhere.
Write script: `_tmp63_write.py` (+ `_tmp63_check.py`, kept in lane
per rules).

## HITs: 2/50 (both recruit rule)

### idx 3108: Guardian of Fight Club Beckhen, Lv.1, 3-star (catalog 051)
- File: `Screenshot_20190616_180423-615fbdbd3271cbfa.jpg`
  (720x1280). Crop: `hits/batch-63-3108.png`.
- Recruited splash; 3 gold stars in black circle with gold ring +
  Lv.1 ribbon (zoom-verified `z63_3108_name`); Offense (sword icon)
  + Ice (blue fist); coins +1000; Show off now! / See Details /
  Okay.
- Name/title match catalog 051 exactly; ribbon 3 = base grade 3
  (no star-vs-grade difference).

### idx 3122: Runaway Bride Teresa, Lv.1, 4-star (catalog 065)
- File: `Screenshot_20190622-204239-3bd8f7c96ccb068d.png`
  (1080x1920). Crop: `hits/batch-63-3122.png`.
- Recruited splash; 4 gold stars (2x2) in black circle with green
  ring + Lv.1 ribbon (zoom-verified `z63_3122_name`); Support
  (heart) + Fire (red peace-hand); coins +1000; Hunter Bonus HP
  6.0% toast; Show off now! / See Details / Okay.
- Name/title match catalog 065 exactly; ribbon 4 = base grade 4
  (no star-vs-grade difference). Only 4-star recruit splash of
  the batch.

## Near-hits (hit=no per bar rules)

### Equipment constellation without named hero (hit=no)
- idx 3150: weapon Lv.50 (knife) + armor Lv.50 (white coat) +
  accessory Lv.50 (black bag) + 6 green gems
  (Lv.11/Lv.9/Lv.9/Lv.12/Lv.9/Lv.9); Strength 26777 +10430; HP
  3128 +601; ATK 1425 +298; DEF 1468 +483; Attacking Speed 7.00
  +0 (zoom `z63_3150_stats`, OCR-confirmed). Stat labels
  HP/ATK/DEF.

### 11-pull equipment result without names (hit=no)
- idx 3123: 9x gold 3-star + 1x green 4-star + 1x blue 5-star
  (pink crystals); One more time! 250.

### Trace-search states without heroes (hit=no)
- idx 3101: Search Complete! level 4/4; 4x red pom-pom x1; Lily &
  Lyla's Trace 142/160.
- idx 3107: Searching Hunter map; twins card 6/160 + 00:59:42.
- idx 3115: card crop; 114/160 + 00:58:15.

## Cross-batch pairing notes

- Trace-search arc: idx 3107 map (6/160 node) -> idx 3115 crop
  (114/160) -> idx 3101 result (142/160).
- Stage-preview pair: idx 3104 (Ally 103222, 4x Lv.MAX, foe 5x
  Lv.15) -> idx 3105 (Ally 120421, +17199, foe 5x Lv.10, power
  flat 90000), 13s apart.
- Fight-club chain: idx 3112 setup (Bronze, Monrou, 57485) ->
  idx 3113 VS (18000 vs 54196, 3x gap) -> idx 3114 victory
  (+15 points, sic "wow you think your good nah your bad").
- Friendly pair (HilmMarch 135403): idx 3124 (TrojanWolf,
  no-reward/0-ticket text) -> idx 3125 (MrPolarBear) -> idx 3126
  victory (MrPolarBear Lv.53).
- TrojanWolf trail: idx 3113 (Str 54196, R193) -> idx 3114 win
  -> idx 3124 friendly -> idx 3132 (1366 Point, rank 178,
  Lv.41, My Rank).
- MrPolarBear: idx 3125 friendly -> idx 3126 victory ->
  idx 3132 rank 176 (1367, Lv.54, RU, sic emoticon).
- Muskrat pair: idx 3129 menu crop (Lv.84) -> idx 3130 card
  (Legends, muskrat#6069, 49 likes).
- Roster scroll seqs: 3133->3134 (25/48, 19s); 3139->3140
  (32/60, 5s); 3143->3144 (47/54, 11s); 3145->3146->3147
  (71/75, 33s/13s); 3148/3149 Discord-annotated reposts of
  3145 (circles/X/arrow).
- Greeting sic link: "I lob you :>" on Herrcher (3121, 1st
  2004) and RayYenSh (3138, day-zero 309-power account).

## Most valuable economy/mechanic readings

- Equipment accounting (idx 3150): Lv.50 knife/coat/bag + 6
  gems; gear contributes +10430 of 26777 Strength; HP
  3128 +601 / ATK 1425 +298 / DEF 1468 +483 / Speed 7.00 +0.
- Gem pull (idx 3123): 9/1/1 gold/green/blue split at 250
  price point.
- Chicken-for-traces (idx 3111): free chicken at 10 coupons;
  My Trace x3 at Rupees 1500; wallet 104054.
- Rupee Package (idx 3102): coin x80000 at JPY 980, fleur 1100,
  Purchasable (sic) 2/2.
- Metron fragment/trainer pair (idx 3119): Crystal 10 at 200 +
  3-star Trainer 1 at 300.
- Veteran compensation (idx 3116): unsupplied Veteran Points ->
  Reward 6Days, scroll x140.
- New-captain ladder (idx 3137): Day1 stamp x100 / Day2 10+1
  Recruit / Day3 gem x100 / Day4 Athena x1 / Day5 2-4-star
  Recruit / Day6 gem x150 / Day7 3-star Selection.
- Fight economy: Bronze ticket entry (3112) vs friendly
  no-reward 0-ticket bouts (3124/3125); victory +15 points
  (3114); 1367/1366 compression band (3132).
- Roster endpoints: batch-max head 37515 (3141, 170/198
  all-MAX wall); rookie floors 555 (3134), 2054 (3140),
  407 triple (3144), 2065 (3147); unleveled 71/75 headliners
  Lv.24/12/5/5 over 15533 (3145).

## Element / title wording tallies

- Tier-list contaminant (idx 3135) words elements "Electric"
  (Windblade, Alia, Erise) vs client "Electricity" seen in
  earlier batches; Fire/Ice elsewhere.
- Client spelling "Patrone" (3135) matches splash spelling
  from batch-56, vs "Patrone" variants nowhere in batch.
- Titles match catalog exactly: Guardian of Fight Club (051),
  Runaway Bride (065). Scar's Story chapter list (3136) left
  uncatalogued (no hero shown; cf catalog 032 Wandering
  Fighter Scar).

## Contaminants

- idx 3135: Google Sheets "Offense Team"/"Defense Team" tier
  list (Anna S., June 19 2019, 14:47); full gear-set pairings
  transcribed.
- idx 3148/3149: Discord View embed wrappers (11:47, 94%)
  reposting idx 3145 roster with red circles/X/arrow.

## Sic list

- "Purchasable 2/2" (3102).
- "wow you think your good nah your bad" (3114).
- "Forfeit Game" (3128, 3131).
- "o(--_oO)(o•_•)o" emoticon (3132; see TSV verbatim).
- "I lob you :>" (3121 Herrcher; 3138 RayYenSh).
- "Pawsitive" (3109 guild name).
- "Reward 6Days" (3116).
