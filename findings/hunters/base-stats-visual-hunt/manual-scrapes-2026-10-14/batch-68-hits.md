# Batch 68 hits (idx 3351-3400)

Lane: findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/
Hit crops (full-frame, provenance only): hits/batch-68-3385.png, hits/batch-68-3394.png
OCR probes (lane folder): z68_3374_adv.png (advancement Power panel), z68_3391_pop.png (selection-request popup);
tesseract --tessdata-dir %TEMP%/opencode/tessdata, -l eng returned garbage/blank on badge/HUD fonts - eye/zoom wins,
same precedent as batch-56/60/65.

## HITs: 2/50

- idx 3385: Animal Lover Pansy, Lv.1/30, 3 stars, Strength 1892, HP 561, ATK 369, third stat 374
  (label cut at panel edge, transcribed unlabeled - DEF presumed but NOT asserted). Elemental class.
  Catalog 057 (Support). Crop: hits/batch-68-3385.png.
- idx 3394: Frost Witch Octavia, Lv.1, 3 stars, Strength 2134, Experienced Hunter Lv.1.
  Catalog 028 (Offense). Crop: hits/batch-68-3394.png.

## Near-hits (hit=no per bar rules)

- idx 3352: Gerard, Indomitable Warrior, Lv.1 - full Base Stat block (HP 7497 / ATK 3838 / DEF 2182 /
  ATK SPD 7.0, Skill 50/50 x5) but no star rank shown. Title matches catalog Gerard (Awakened)
  005_1 (base 005 = Invincible One). Battle-prep Hunter Details panel.
- idx 3373: Recruited! Guardian of Fight Club Beckhen, Lv.1, 3 stars, Offense, Ice - full recruit
  identity (name+title+level+stars) but no HP/ATK/DEF or Strength shown. Catalog 051.
- idx 3392: Prayer Junia, Lv.1 - full Base Stat block (HP 2976 / ATK 1342 / DEF 661 / ATK SPD 7.0,
  Skill 1/40 x4 + 1 locked) but star badge not visible in this 672x955 crop. Catalog 076.
- idx 3357: Strange Twins Lily and Lyla transcend result, Lv.MAX, Strength 36875 -> 40467,
  ATK 1967 -> 2109, Defense 1522 -> 1627, HP 3778 -> 4056 - stars-unshown result, hit=no.
- idx 3383: Genius Climatologist Dino, 3 stars, Dino's Trace 0/80 - level and stats not shown.
  Catalog 054.

## Same-account trails

- 3360 + 3361: Hunter List 29/45 top and bottom halves (same roster).
- 3369 + 3370 + 3372: battle-select grid and build-team views into Hunter List 26/30
  (2405/2388/2364 trio; leader levels 2405 -> 2506 between frames).
- 3376 + 3377 + 3378: Defensive Match Settings (185563) into two Defense Team Setting views
  (185563 Eff 7; 119956 Eff 3 Bomber).
- 3380 + 3381 + 3382: Hunter List 37/39 (1524 Locked) into two 3-star->4-star Advancement
  Matches (partner candidate 1524 -> 1547; coins 63318 -> 59478; costs 1440/3840 context).
- 3395 + 3396: Hunter List 91/105 top and bottom halves (same roster, 18:03, 55%).
- 3375 + 3384: same Estelle/Midgard event ladder (100 pts and 110 pts states).

## Most valuable economy/mechanic readings

- 3353 Radiant Fatal Jewel Lv.9/15: main Critical Attack Chance +3.22; subs +1.35 / +0.62 /
  +2.20 / +3.10; 4-piece set = Critical Attack Damage 60.00%.
- 3371 Dispatch (Wolf's Mouth Area 57): 20 plays, 00:48:00 est, 120 fuel on 203/67 wallet.
- 3374/3382 Advancement costs: 2-star Level-Up Advancement 1440 coins; 3-star 3840 coins.
- 3367 Rupee Shop price list (rupees 111259): Trace Magnifier x5 5000, 1-star Trainer 9000,
  Helium Capsule x6 10000, Metron Fragment x60 2000, four x10 material rows @1000.
- 3386 Jewel Mine: Request 25 manda, 10+1 Request 250 (4-star guaranteed), Daily Free 1~4-star.
- 3388 Rupee purchase: x5000 for Manda 5, Daily Purchase 5/9, Veteran Professional 1.
- 3389 Estelle skill (MAX Special, Weaken Cont.): crit-chance -0.2%/sec stackable x5,
  elemental resistance -0.6%.
- 3383 Dino trace search: 15 torches/search, 25 held, Entrance Limit 1/1, 00:52:41 timer.
- 3355 fish sell prices: most fish @5000, Seaweed/HQ bait @1500, Avg bait @650, snail/note @10.
- 3356 login calendar: 820-day supply grid (28-day rows; day-1/8/15/22 = x10000 coin).

## Element / title wording tallies

- Element words: Ice (3373 Beckhen, 3392 Junia panel shows Ice-class icon), Elemental (3385 Pansy,
  3394 Octavia class icons), Fire/Lightning (3399 recruit role icons, no per-hero mapping).
- Title spellings verbatim: Indomitable Warrior (3352); Strange Twins (3357); Guardian of Fight
  Club (3373); Genius Climatologist (3383); Animal Lover (3385); Frost Witch (3394);
  Prayer (3392); Windy Soul / Atoner / Little Reaper / Dancing Sword / Owner of Saw Blade /
  Midgard s Finest Sword (3399 - apostrophe spacing as shown, sic); Midgard Finest Sword
  (3389 screen title drops the possessive); Midgard's Finest Sword (3375 event title, with apostrophe).
- Name spellings: Lily and Lyla (3357 panel) vs Lily and Lyla (3399 grid) - ampersand form only in
  catalog 047; Atoner Genovia (3399) vs catalog title Atoner - match.

## Non-ASCII names

- None in game UI (English client). Korean player names in rankings 3362/3363 (not transcribed
  glyph-by-glyph); Japanese video title in 3366 (not transcribed); XXX redaction boxes in
  3352/3376 (opponent names hidden).

## Contaminants

- 3364 Naver Cafe browser capture, 3365/3366 YouTube browser captures - external-web
  contaminants, one OCR-equivalent read each, identity anchors recorded, moved on.
- 3379 is a 1080x381 banner-strip crop (Bonus Goal 4/7), partial by nature.
- 3398 is a 1080x621 crop (guild conflict message), partial by nature.
- 3392 is a 672x955 detail crop (Junia Hunter Details).
- No zero-digit promo runs in this batch.
