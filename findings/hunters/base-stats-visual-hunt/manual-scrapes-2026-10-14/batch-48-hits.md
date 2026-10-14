# Batch 48 hits (idx 2351-2400)

Lane: `findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/`
Crops: none (0 HITs).
Zooms (lane folder, provenance only): `z48_2360_adv`, `z48_2368_trans`,
`z48_2369_train`, `z48_2391_rows`, `z48_2394_bottom`, `z48_2399_zero`,
`z48_2353_pay`.
OCR (lane folder): `_tmp48_ocr/` (2353 payout / 2399 zero-digit, tesseract
`--tessdata-dir` `%TEMP%/opencode/tessdata`, `-l eng`).
Write script: `_tmp48_write.py` (kept in lane folder per rules).

## HITs: 0/50

No frame in this batch shows named hero + level + star rank + HP/ATK/DEF
or Strength together. Recruit splashes carry name + title + level +
stars but no stats; Train/Transcendence frames carry name + level +
stats but no star badge; hunter-list rows carry level + Strength but
no names. All hit=no per bar rules.

## Near-hits (full numbers, hit=no per bar rules)

### idx 2368: Transcendence Hard-Knock Life Riko, Lv.MAX (catalog 024)
- File: `Screenshot_20171112-121610-4edaf1ee917b03d5.png` (1080x1920).
  Strength 53194 -> 59980; Attack 801 -> 868; Defense 967 -> 1047;
  Life 1910 -> 2069 (all zoom-verified `z48_2368_trans`).
- No star badge on frame. Hit=no.
- Pairs idx 2369 Train (2069/868/1047 carry over exactly).

### idx 2369: Train Teammate Master Hunter Lv.30, Strength 59980
- File: `Screenshot_20171112-152128-230bda1b7a6c68f7.png` (1080x1920).
  Life 2069 / Attack 868 / Defense 1047 / Attack Speed 7; Critical
  Damage Chance 14 / Critical Damage 185 / Armor Penetration 0;
  Block Chance 33 / Block Resistance 50 / Strengthen 0 / Elemental
  Resistance 0 / HP Regen 40 (zoom-verified `z48_2369_train`).
- Hero name "Riko" not on frame (chain-inferred from 2368 only).
  Hit=no.

### idx 2384: Train Teammate Walking Disaster Nene, Lv.1, Strength 2138
- File: `Screenshot_20171220-205057-6aebffaae589431b.png` (1080x1920).
  Experienced Hunter Lv.1; shield-class + blue-element icons;
  Train/Transcendence/Skill Training/Upgrade Equipment/Story buttons.
- Name + level + Strength present but no star badge on frame.
  Hit=no (catalog 003).

### idx 2357: Immortal One Karl Steiner recruit, 3-star, Lv.1 (catalog 012)
- File: `Screenshot_20171104-200841-3cf81c7c7106570e.png` (720x1280).
  3-star header chevron + plaque; Lv.1 ribbon; Offense + Electricity
  icons; coins +1000; wallet 170846 coins / 61 gems / 39 fuel.
- ELEMENT NOTE: client "Electricity" vs catalog 012 "Lightning"
  (extends the batch-29/30/32/34/38/40/43 Electricity arc).
- Hit=no (no stats).

### idx 2360: Proficient Hunter Lv.MAX 21012 -> Master Hunter Lv.1 33216
- File: `Screenshot_20171106-064138-afd555e1e563eb54.png` (1440x2560).
  Advancement Successful; green ring -> blue ring (zoom-verified
  `z48_2360_adv`); New Skill Unlocked Crying Sword.
- No hero name on frame; catalog blank. Hit=no.

### Recruit splashes with level + stars, no stats (all hit=no)
- idx 2370: Invincible One Gerard, 2-star, Lv.1, Defense + Ice,
  +1000 (catalog 005).
- idx 2371: Walking Infirmary Joy, 3-star, Lv.1, Support + Fire,
  +1000 (catalog 035).
- idx 2373: Walking Disaster Nene, 3-star, Lv.1, Defense + Ice,
  +1000 (catalog 003).
- Banners without level ribbons (hit=no): idx 2366 Thunder Arrow
  Diana 3-star (catalog 031); idx 2378/2400 Steely Bodyguard Kain
  3-star (catalog 029).

## Cross-batch pairing notes

- Riko transcendence chain: idx 2368 Transcendence (53194 -> 59980,
  801/967/1910 -> 868/1047/2069) -> idx 2369 Train Lv.30
  (59980 top, 2069/868/1047/7 + full sub-stats). Before->after
  every stat recorded.
- Skill-training session (5 frames, same Lv.1/40, coins 136565,
  item 1445/1, Begin Training 100): idx 2361 (Pardis toast) ->
  2362 (Majo "True true") -> 2363 (SeymourButts) -> 2364
  (Lazuline) -> 2365 (Everkun). Chat-toast sequence only; no
  training deltas on frame.
- Hunter-list scroll seq (69/81, same account): idx 2385
  (14431 head ... 2615 cut) -> 2386 (2615 ... 1793 x3 cut) ->
  2387 (1783 x2 ... 452 tail) -> 2388 (448 ... 322, empty slots).
  Roster endpoints 14431 -> 322.
- Build-team scroll pair: idx 2381 (16924/5346/6936 top, mid-tier
  grid) -> 2382 (same top, 1724 x3 / 1644 x6 rookie-dupe grid).
- 1600% promo pair: idx 2353 (red gem x80000 + Veteran Point Gift
  Certificate, "huge amount of Rupee") -> idx 2379 (fuel x960 +
  Veteran Point Gift Certificate 3, "huge amount of Fuel").
- Kain banner bookends: idx 2378 (gems 11 / scrolls 110 / 621) ->
  idx 2400 (gems 158 / scrolls 10 / 12, 10+1 300-gem pricing).
- Veteran ladder: idx 2397 Guru 1 (14730/27520, 12790 to Guru 2)
  extends the batch-43 Professional-3 ladder (idx 2137).
- Trace-payout run (7 popups): 2352 (10x: 3/3/3/4/3/3/5/3/4/5) /
  2354 (6x: 5/2/4/5/2/4) / 2355 (8x: 4/5/5/4/3/3/2/4) / 2356
  (1x gold-ring 5) / 2358 (3x: 3/4/3) / 2359 (7x:
  3/4/3/3/5/4/5) / 2372 (7x: 4/3/5/5/4/4/5).
- Art-only splash pair: idx 2389 (wolf-ears trident woman) /
  idx 2390 (roaring bear), same snowfield session, zero digits.

## Most valuable economy/mechanic readings

- Rupee shop tiers (idx 2351): purchase 10000 / 20000 / 100000
  rupees; wallet 46000 rupees / 178 gems; amount scales with Team
  Level ("How to Purchase" note verbatim).
- 1600% promos (idx 2353 zoom+OCR / 2379): gem x80000 + Veteran
  Point Gift Certificate ("huge amount of Rupee") vs fuel x960 +
  Veteran Point Gift Certificate 3 ("huge amount of Fuel"). OCR
  misread "1600%" as "41600%"; visual zoom wins per rules.
- Riko transcendence + train (idx 2368/2369, zoom-verified):
  53194 -> 59980 Strength; 801 -> 868 Attack; 967 -> 1047
  Defense; 1910 -> 2069 Life; Lv.30 sub-stats 7 / 14 / 185 / 0 /
  33 / 50 / 0 / 0 / 40.
- Advancement (idx 2360, zoom-verified): Proficient Lv.MAX 21012
  -> Master Lv.1 33216; New Skill Unlocked Crying Sword; green ->
  blue ring.
- Fight Club trace rotation (idx 2376): week of Nov 26 Bear's
  traces -> week of Dec 3 Patrone's traces; 1st x2400 medals /
  x160 traces / x1000 gems; 2nd x2200 / x120 / x600.
- Material price ladder (idx 2377): Metron Crystal 8 @1000;
  Invincible Shell 352 / Fruit-Bearing Herb 370 / Scorching
  Flamestone 331 / Unusual Metal Piece 344 @250; Burning
  Flamestone 19 @50; coins 309976.
- 200th-day event (idx 2380): 3-star recruit rate +200% for one
  day only (Dec 1st 00:00-23:59 GMT+9); Like 30.
- Abyss weekday gating (idx 2393): Cryogenic Sun/Mon/Thurs;
  Electric Sun/Tues/Fri; Volcanic Sun/Wed/Sat; Resets Left 0;
  fuel 4/60.
- Missing-hunter gating (idx 2383/2392): Volcanic Abyss UNIQUE
  8/80 + Giant Shelter 116/40 (0day 10:14:30 / 13day 18:31:35);
  Silence Forest pair 720/40 (11day) vs 362/40 (4day); Easy /
  Normal / Hard; Search vs Search Complete states.
- Veteran Guru ladder (idx 2397): Guru 1 14730/27520, 12790 to
  Guru 2; benefits Abyss Reset +1 / Fuel +12 / Rupee +12 /
  Invitations +12; Guru 2 adds Special Support Fuel +15, +14s.
- Major goals (idx 2398): Cleared Stages 233/250 (x15); Used
  Fuel 2123/2500 (x15); Amateur Hunters 5/10 (x5); Novice
  Hunters row cut.
- Zero-digit promo (idx 2399, zoom+OCR): Legendary Selection
  Request Current Amount 0; 3-star Hunter Selection Request
  ("choose a 3-star hunter you want to recruit"); Areas
  Available "Information is not available."
- Mission ledger (idx 2367): Mt. Black Rock Area 2 Victory, Team
  Level 11; 8973 / 2755 / 6627 / 5813; Rupees +73; items 1/1/2.
- Duplicate-Strength note (idx 2374): two hunters at exactly
  49467 (Lv.17 Defending + Lv.26 Exploring).

## Non-ASCII names (transliterated, for searchability)

- idx 2357: Karl Steiner. idx 2361-2365: Pardis; Majo;
  SeymourButts; Lazuline; Everkun; Silv; Carla.
  idx 2366/2378/2400: Diana; Kain. idx 2369: Lgtmagician.
  idx 2370: Gerard. idx 2371: Joy. idx 2373/2384: Nene.
  idx 2368: Riko. idx 2381: JackalMkII; Cactuar. idx 2383:
  Silverber... (cut discoverer). idx 2386: Acla... idx 2387:
  Elysia00. idx 2395: Tyltyl. No Korean-script names in batch.

## Contaminants

- None. Zero-contaminant batch: no OS overlays, no external
  photos, no avatar-only crops. (Smallest frame 1440x826 village
  wide shot is game content, kept as village.)

## Sic list

- "Total of Cleared Stages" / "Total of Used Fuel" / "Total of
  Amateur Hunters Recruited" / "Total of Novice Hunters
  Recruited" (idx 2398, client grammar verbatim).
- "Volcanic Ab yss" (idx 2383, line-wrap split, kept verbatim).
- "The Heart of the Giant Shelter" (idx 2383, no possessive on
  Giant, verbatim vs possible "Giant's Shelter").
- "1 Star!" vs "2 Stars!!" (idx 2398, singular/plural +
  punctuation asymmetry verbatim).
- "Tyltyl's What's in the Box?" / "Lottery Mouse likes walnuts!"
  (idx 2395, promo copy verbatim).
