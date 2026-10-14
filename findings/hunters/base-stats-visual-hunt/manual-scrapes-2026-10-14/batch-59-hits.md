# Batch 59 hits (idx 2901-2950)

Lane: `findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/`
Crops: `hits/batch-59-2901.png`, `hits/batch-59-2905.png`,
`hits/batch-59-2908.png`, `hits/batch-59-2911.png`,
`hits/batch-59-2915.png`, `hits/batch-59-2940.png`,
`hits/batch-59-2941.png` (7 HITs).
Zooms (lane folder, provenance only): `z59_2901_ribbon` /
`z59_2905_ribbon` / `z59_2908_ribbon` / `z59_2911_ribbon` /
`z59_2915_ribbon` (recruit star ribbons, all 3 white stars),
`z59_2940_badge` / `z59_2941_badge` (5-star blue badges +
Lv.MAX / Lv.1 ribbons), `z59_2940_str` / `z59_2941_str`
(Strength 32088 / 16813), `z59_2939_result` (Yuri
transcendence delta), `z59_2906_delta`, `z59_2942_promo`.
OCR (lane folder): `_tmp59_ocr/` (full-frame tesseract
`--tessdata-dir` `%TEMP%/opencode/tessdata`, `-l eng`;
stylized splash fonts mostly fail so zoom wins; Yuri
result OCR confirms 12706/1044/766/1583/1134/831/1714;
Bibi strength OCR-anchor "Strength 3..88").
Write script: `_tmp59_write.py` (kept in lane folder per rules).

## HITs: 7/50 (5 recruit rule + 2 train rule)

### idx 2901: Experiment 2 Sunny, Lv.1, 3-star (catalog 022)
- File: `Screenshot_20180911-201121-05387c5c963ee6f5.png`
  (720x1280). Crop: `hits/batch-59-2901.png`.
- Recruited splash; 3 white stars on dark navy chevron
  (zoom-verified `z59_2901_ribbon`); Support + Ice icons;
  coins +1000; See Details / Okay / Share.
- GRADE NOTE: ribbon shows 3 stars vs catalog 022 base
  grade 2.

### idx 2905: Elite Messenger Hermes, Lv.1, 3-star (catalog 023)
- File: `Screenshot_20180917-072459-bdb2d4ae05299623.png`
  (1080x1920). Crop: `hits/batch-59-2905.png`.
- Recruited splash; 3-star gold ribbon (zoom-verified
  `z59_2905_ribbon`); Offense + Fire icons; +1000.
- Title/name match catalog 023 exactly.

### idx 2908: Singing Poet Apollon, Lv.1, 3-star (catalog 055)
- File: `Screenshot_20180920-222322-9e164b5e4d54e177.png`
  (1080x1920). Crop: `hits/batch-59-2908.png`.
- Recruited splash; 3 white stars (zoom-verified
  `z59_2908_ribbon`, leftmost clipped by crop); Bomber +
  Fire icons; +1000.
- Title/name match catalog 055 exactly.

### idx 2911: Windy Soul Windblade, Lv.1, 3-star (catalog 052)
- File: `Screenshot_20180923-114334-fa63b7d0ea4bd167.png`
  (1080x1920). Crop: `hits/batch-59-2911.png`.
- Recruited splash; 3 white stars on green-chevron banner
  (zoom-verified `z59_2911_ribbon`; full-view first read
  4-star corrected by zoom, zoom wins); element worded
  "Electricity"; Offense; +1000.
- GRADE NOTE: ribbon shows 3 stars vs catalog 052 base
  grade 4. ELEMENT NOTE: client "Electricity" vs catalog
  "Lightning".

### idx 2915: Animal Lover Pansy, Lv.1, 3-star (catalog 057)
- File: `Screenshot_20180929-063934-a6b265ebb4246b2b.jpg`
  (1080x1920). Crop: `hits/batch-59-2915.png`.
- Recruited splash; 3 full white stars on gold ribbon
  (zoom-verified `z59_2915_ribbon`); Support + Ice icons;
  +1000.
- Title/name match catalog 057 exactly.

### idx 2940: Wolf Child Bibi, Master Hunter Lv.30, 5-star, Strength 32088 (catalog 040)
- File: `Screenshot_20181028-165229-e877fa5868f92d60.jpg`
  (1080x1920). Crop: `hits/batch-59-2940.png` (full frame).
- Train screen; 5-star blue badge + Lv.MAX ribbon
  (zoom-verified `z59_2940_badge`); Strength 32088
  (zoom-verified `z59_2940_str`, OCR-anchor); sword-class
  + support-hand icons; 5 skill icons; Advance grayed.
- Title matches catalog 040.

### idx 2941: Ice Skating Fairy Yuri, Master Hunter Lv.1, 5-star, Strength 16813 (catalog 045)
- File: `Screenshot_20181028-194654-addc978862309aa4.png`
  (1080x1920). Crop: `hits/batch-59-2941.png` (full frame).
- Train screen; 5-star blue badge + Lv.1 ribbon
  (zoom-verified `z59_2941_badge`); Strength 16813
  (zoom-verified `z59_2941_str`); sword-class + ice icons;
  Train button red.
- Title matches catalog 045. Yuri intra-batch arc: pull
  gold 2931 (bunny look) -> transcendence 2939 -> train
  2941.

## Near-hits (hit=no per bar rules)

### Advancement setup without identity (hit=no)
- idx 2906: Proficient Hunter Lv.MAX 12165 -> Master
  Hunter Lv.1 14564 (+2399, x1.198); New Skill Unlocked:
  Predator's Intuition (zoom `z59_2906_delta`); no hero
  name shown.

### Transcendence result without star rank (hit=no)
- idx 2939: Ice Skating Fairy Yuri (catalog 045),
  Strength 11448 -> 12706 (+1258, x1.110); ATK 1044 ->
  1134 (+90); Defense 766 -> 831 (+65); HP 1583 -> 1714
  (+131); Successfully transcended! (zoom
  `z59_2939_result`, OCR-confirmed). Stat labels
  ATK/Defense/HP.

### 4-star pull without nameplate (hit=no)
- idx 2937: 4-star green-centered Joy (white/blue bunny)
  + 5 silver + 5 brown; only 4-star pull of the batch.

## Cross-batch pairing notes

- LuckyBinder31 trail: idx 2907 fight-club (1201 Point,
  rank ~3956, Lv.46, Silver 5/6) -> idx 2944 (1538,
  rank 906, Lv.61, Metron 6/6) -> idx 2947 (1915, rank
  552, Lv.63, Mandarin 3/6).
- 53NP41 trail: idx 2918 (Lv.43, 75631, Area 166) ->
  idx 2925 (Lv.48, 90041, Area 169).
- Maeko trail: idx 2904 profile (Lv.64, 121824) ->
  idx 2934/2935 forum posts (Witch Riko plea).
- Ruins trio: idx 2916 (Hermes, 00:59:45) -> idx 2919
  (Natalia, 00:59:45) -> idx 2927 (Lantern, 00:59:43);
  2928 mission result drops Lantern x10.
- Roster contrast: idx 2920 (33/45) -> idx 2929 (42/45,
  7932 -> 8198); vs 2945 (40/54), 2948 (32/57,
  batch-high 21680), 2950 (81/72 over-cap growth/merge
  artifact).
- Pull ladder (same Oct-19 session): 2930 (2/2/7) ->
  2931 (1/2/8) -> 2932 (2/2/7) -> 2936 (2/3/6) ->
  2937 (4-star Joy) -> 2938 (0/5/6 gold-less).
- Shop flow: idx 2942 promo (2603 -> 5093, PLN 19.99)
  -> idx 2943 purchase success (1600%, coin x80000).

## Most valuable economy/mechanic readings

- Transcendence delta (idx 2939, Yuri): +1258 Strength
  (x1.110); ATK +90 / Defense +65 / HP +131.
- Advancement delta (idx 2906, unknown): 12165 -> 14564
  (+2399, x1.198), Predator's Intuition unlock.
- Promo advancement (idx 2942): 2603 -> 5093 (x1.957),
  USD 9.99 -> PLN 19.99, 00:57:24 expiry.
- Purchase success (idx 2943): 1600% bonus, coin
  x80000, Veteran Point Gift Certificate x3.
- Chichi rate-up (idx 2949): 1000% UP, first recruit
  +1 transcendence, 10 traces via 10+1, wallet 88 gems /
  0 scrolls / 9 traces, 234:01:50 left.
- Mileage ladder (idx 2926): 3 / 10 / 25 / 40 pulls per
  step.
- Mission result (idx 2928): Volcanic Abyss level 3/4,
  Team Level 56, Rupees +2000, Lantern x10.
- Fight-club compression: 1915/1914 band at ranks
  551-554 (2947) vs 1201 band at 3953-3957 (2907).
- Roster endpoints: batch-high 21680 (2948, 32/57);
  over-cap 81/72 (2950); rookie tails Lv.1 (2903/2945).

## Element / title wording tallies

- "Electricity" (worded, idx 2911 Windblade) vs catalog
  "Lightning" (052) - first worded-electricity case in
  lane; Bibi catalog Lightning appears icon-only (2940).
- No "Flame of the Battlefield" / "Patrone" variants in
  batch; tier-list contaminant uses client "Patrone"
  (2922), matching batch-56 splash spelling.
- Titles match catalog exactly: Experiment 2 (022),
  Elite Messenger (023), Singing Poet (055), Windy Soul
  (052), Animal Lover (057), Wolf Child (040), Ice
  Skating Fairy (045).

## Contaminants

- idx 2909: Google Play Store page, Russian locale
  (update Sep 19 2018: Diana & Heidi fates, Lily & Lyla
  skill fix).
- idx 2922/2923/2924: Chrome Google Sheets "Meta top
  50" tier list (15 tabs, 20% battery).
- idx 2933: art-only splash, no UI digits.
- idx 2934/2935: Naver forum post + Natara reply
  (2018.10.01 17:03, sic "greatful").

## Sic list

- "Electricity" (2911, client wording vs catalog
  "Lightning").
- Ribbon 3 stars on Sunny (2901) vs catalog 022 base
  grade 2; ribbon 3 stars on Windblade (2911) vs catalog
  052 base grade 4 (zooms win).
- "greatful" (2934, forum sic).
- "Can't we talk this out?" / "It's a good day... for
  your funeral." / "Big boobies" / "Do you have the
  guts to fight me?" (fight-club greetings verbatim).
- "Yahallo, nice to meet you:3 Nyanpasu!" (2918) /
  "Riko & Crocus x Maeko. Don't touch, mine!" (2904)
  greetings verbatim.
- "Guarantees you with at least one" (2949, cut
  sentence).
- "Show off now!" (2943).
