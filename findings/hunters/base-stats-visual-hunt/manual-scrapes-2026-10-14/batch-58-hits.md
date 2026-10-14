# Batch 58 hits (idx 2851-2900)

Lane: `findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/`
Crops: `hits/batch-58-2857.png`, `hits/batch-58-2890.png` (2 HITs).
Zooms (lane folder, provenance only): `z58_2857_badge`
(Bibi 4-star green ring + Lv.MAX), `z58_2890_badge` (Bibi
4-star green ring + Lv.MAX), `z58_2857_strength`,
`z58_2890_strength`, `z58_2859_promo`, `z58_2851_badge`,
`z58_2854_badge`, `z58_2865_badge`, `z58_2881_badge`,
`z58_2889_badge` (badge-region crops; 2851/2881/2889 crops
missed the badge so those rows rest on full-view only).
OCR (lane folder): tesseract `--tessdata-dir`
`%TEMP%/opencode/tessdata`, `-l eng` on the two strength
strips + promo crop (`.txt` beside each zoom). OCR is
unreliable on the italic game font (2857 strength missed,
2890 partial, 2859 promo "1600%" misread as "41600%");
visual zoom wins everywhere.
Write script: `_tmp58_write.py` (kept in lane folder per rules).

## HITs: 2/50

### idx 2857: Wolf Child Bibi, Proficient Hunter Lv.30, 4-star, Strength 9444 (catalog 040)
- File: `Screenshot_20180814-214023-8c28e37cb1203493.png`
  (1080x1920). Crop: `hits/batch-58-2857.png`.
- Train Teammate; 4-star green-ring badge + Lv.MAX ribbon
  (zoom-verified `z58_2857_badge`); Class sword + Elemental
  hand icons; crown + lock icons; Advance / Transcendence /
  Skill Training / Upgrade Equipment / Story.
- Title matches catalog 040.

### idx 2890: Wolf Child Bibi, Proficient Hunter Lv.30, 4-star, Strength 10127 (catalog 040)
- File: `Screenshot_20180901-203803-460daf7d2fa677df.png`
  (1080x1920). Crop: `hits/batch-58-2890.png`.
- Same hero/level/stars as 2857 but Strength 10127
  (+683, OCR partial "en th 10127", visual wins);
  zoom-verified `z58_2890_badge`.
- Re-train pair 2857 -> 2890: identical Proficient Hunter
  Lv.30 4-star Bibi at 9444 then 10127 (gear/skill
  difference, no advancement between frames).

## Near-hits (full numbers, hit=no per bar rules)

### Recruit splashes with level + stars, no stats (all hit=no)
- idx 2851: Strange Twins Lily & Lyla, 4-star green ring,
  Lv.1, Offense + Fire, +1000 (catalog 047, title matches).
- idx 2854: Robot Engineer Edward, 3-star gold, Lv.1,
  Defense + Electricity, no +1000 bubble on frame
  (catalog 041, title matches).
- idx 2865: Windy Soul Windblade, 4-star green ring, Lv.1,
  Offense + Electricity, +1000 (catalog 052, title matches).
- idx 2889: Walking Disaster Nene, 3-star gold, Lv.1,
  Defense + Ice, +1000 (catalog 003, title matches).
  Splash pairs with the 2881 art-only flash.
- idx 2881: recruit art flash, 4-star green ring + Lv.1,
  no name/title text (Nene-like bear-ears goggles art but
  unstated; hero/catalog blank, confidence medium).

### 11-pull results (star counts only, hit=no)
- idx 2853: 6x 1-star / 4x 2-star / 1x 3-star (white-bunny
  gold); "One more time! 300".
- idx 2882: 7x 1-star / 1x 2-star / 3x 3-star (white-wolf,
  pink-bunny Heidi, black-red-horns golds).
- idx 2883: 7x 1-star / 4x 2-star / 0x 3-star (no-gold pull,
  companion to 2882).
- idx 2886: mid-reveal: 5 gear-face-down + 5x 2-star +
  1x 3-star (black hair green eyes); Reveal All.
- idx 2898: 8x 1-star / 3x 2-star / 0x 3-star (no-gold pull).
- idx 2891 (embedded in Discord #announcements, FenixLua):
  8x 1-star + 1x 2-star + 1x 3-star.

### Trace-collection library (hit=no)
- idx 2856 (Defense 11/12, 11.0% -> 12.0%): Harley 60/160,
  Calibur 162/80 (over-collected 2x), Kain 4/80, Bear 0/80,
  Edward 0/80, Nene 14/80. TITLE NOTE: "The Revenant" vs
  catalog 053 "Revenant".
- idx 2860 (Bomber 9/10, 9.0% -> 10.0%): Dino 20/80,
  Apollon 0/80, Patrone 51/80 (nearest), Gullveig 17/80,
  Diana 28/80, Lantern 22/80. SPELLING NOTE: "Gullveig"
  vs catalog 039 "Gullveig".

### Trace-inventory ladders (other class, hit=no)
- 246812-wallet chain (Captain_Kirk): idx 2874 (Harley 60
  @1000; 8 rows @200: Apollon 25, Nene 20, Gullveig 21,
  Hermes 5, Yuri 10, Athena 47, Patrone 34, Bibi 4) ->
  idx 2875 (Therapy 2, Kain 8, Dumble 21, Akasha 11,
  Lantern 3, Heidi 29, Calibur 11, Joy 17, Karl Steiner 6)
  -> idx 2876 (Calibur 11, Joy 17, Karl 6 @200; Octavia 17,
  Papillon 12 @200; Mowgli 37 @100; silver-ring row cut).
  Tiers 1000 vs 200 (5x), floor 100.
- 1135-wallet account (different account): idx 2878
  (Harley 3 @1000; Lantern 3, Beckhen 5, Patrone 3,
  Hermes 10, Calibur 4, Natalia 5, Bibi 21, Akasha 3 @200)
  -> idx 2879 (Therapy 4, Yuri 8, Bear 4, Dino 2, Athena 2,
  Gullveig 5 @200; Rebecca 30, Mowgli 6, Denali 15,
  silver tier, prices cut).
- NAME GAP: Beckhen (rooster art, idx 2878) matches no
  catalog entry.

## Cross-batch pairing notes

- Bibi re-train pair: idx 2857 (Strength 9444) -> idx 2890
  (Strength 10127), same Wolf Child / Proficient Hunter /
  Lv.30 / 4-star green ring + Lv.MAX.
- Nene arc: idx 2881 art-only 4-star flash -> idx 2889
  Walking Disaster Nene 3-star splash (+1000); note the
  star mismatch (4-star art card vs 3-star splash) so the
  link is art-similarity only, not a confirmed chain.
- Hunter-list scroll pairs (same accounts): idx 2868
  (26/39 head, 8737 Leader) -> idx 2869 (26/39 tail, 1795
  dupe, rookie tail 2088 -> 1507); idx 2870 (64/75 head,
  26587) -> idx 2871 (64/75 tail, sic "Lorked").
- Promo ladder: idx 2859 = idx 2880 (1600% x80000, Veteran
  Point Gift Certificate 3) vs idx 2900 (200% x10000):
  8x ratio on both legs (1600/200, 80000/10000).
- Mine-cart ape battle pair: idx 2884 (HP 16853 x2, wallet
  0 + 50) -> idx 2885 (19 / 291 / 25000 + obscured heal);
  same session, device screenshot-editor overlay on both.
- Abyss reset run (idx 2862): 0 / 0 / 1 (Golden 0, top-row
  0, Metron 1); fuel 62/105.
- Rupee-shop wallet gap (idx 2863): wallet 59966 vs Special
  Request x1 60000 (34 short of the top item).
- Fight-club profile (idx 2873): Maeko, Level 61, reg.
  08/19/2017, Attacking Power 117777, League 1520,
  tickets 7; Riko name uncatalogued.
- Mission results: idx 2861 (Metron Abyss Area 8 Victory,
  Team 76, 31017/25215/18972/25095, +150, herbs 8 +
  berries 5) vs idx 2899 (Emerald Canyon Search finished,
  level 2/2, Team 42, 9417/10193/8392/7378, +300,
  trace 40 + scroll 1).
- Battle HUD damage ladder: 2861-area context; 2888
  (669 / 53567, 3 + 2250, 4/4 WAVE); 2893 (338 / 80554 +
  heal 1915, 0 + 60); 2894 (38 + 316/372/372 + 7978x cut +
  heal 1916, editor overlay); 2895-embedded (190 / 920 /
  259159 + green 1645, 3 + 2250, 4/4 WAVE).

## Most valuable economy/mechanic readings

- Gear-strength accounting (idx 2897, Upgrade Equipment,
  Channel 0003): daggers Lv.20 + cape Lv.20 + pouch Lv.20
  (gold) + 6 green-ring gems (Lv.3/Lv.6/Lv.3/Lv.3/Lv.4/
  Lv.3); Strength 23558 +4120; HP 2843 +170; ATK 1510
  +336; DEF 1086 +94; Attacking Speed 8.00 +0. Stat labels
  are HP/ATK/DEF.
- Trace price tiers (2874-2879): Harley 1000 vs standard
  200 (5x premium) vs Mowgli 100 floor; Rebecca 30 /
  Heidi 29 / Bibi 21 largest stacks.
- Trace-collection costs: Defense tab 160 (Harley 60/160)
  vs 80 (Calibur 162/80 over-collected 2x, Kain 4, Bear 0,
  Edward 0, Nene 14); Bomber tab all /80 (Patrone 51/80
  nearest, Dino 20/80).
- Rupee-shop ladder (idx 2863): 60000 / 6000 / 5000 / 5000
  / 3000 / 1000 (bottom-row prices cut); refresh
  01:40:39.
- Promo ladder: 1600% x80000 (huge amount) vs 200% x10000
  (large amount).
- Skill training (idx 2858): Elegant Discipline Lv.50/50,
  Enemy/Weaken, Damage 571.20, "Maximum value you can
  train now", wallet 516942. Skill-title gap (no catalog
  match, no hero name).
- Mirage Ruins Floor 122 (idx 2896): LAST + STAGE 8/7/6
  COMPLETE, STAGE 5 cut, Trade button.
- Blog luck anecdote (idx 2892): Vixent LV6, 10+1
  simultaneous-pull story (Maeko, crocus, two star, three
  vet tickets), 6 likes.
- Build-team checked quad (idx 2855): 3360/3191/2821/2582
  all Lv.MAX Defending, 1st-crown on 3360.
- Over-cap roster heads: 26587 (2870, 64/75), 20783
  (2866, 18/27).

## Non-ASCII names (transliterated, for searchability)

- idx 2851: Lily & Lyla. idx 2853: Nocturna1. idx 2854:
  Edward. idx 2856: Harley, Calibur, Kain, Bear, Edward,
  Nene. idx 2857/2890: Bibi. idx 2860: Dino, Apollon,
  Patrone, Gullveig, Diana, Lantern. idx 2865: Windblade.
  idx 2867: joe1230:spotify. idx 2870: Captain 123neo.
  idx 2873: Maeko, Riko. idx 2874: Captain_Kirk, Harley,
  Apollon, Nene, Gullveig, Hermes, Yuri, Athena, Patrone,
  Bibi. idx 2875: Therapy, Kain, Dumble, Akasha, Lantern,
  Heidi, Calibur, Joy, Karl Steiner. idx 2876: Calibur,
  Joy, Karl Steiner, Octavia, Papillon, Mowgli. idx 2878:
  Harley, Lantern, Beckhen, Patrone, Hermes, Calibur,
  Natalia, Bibi, Akasha. idx 2879: Therapy, Yuri, Bear,
  Dino, Athena, Gullveig, Rebecca, Mowgli, Denali.
  idx 2887: Azercell lock screen (no hunter names).
  idx 2889: Nene. idx 2891: FenixLua. idx 2892: Vixent,
  Maeko. idx 2896: Skaiza. No Korean-script names in
  batch (idx 2873 CJK greeting + Riko x Maeko line not
  transcribed as names beyond Riko/Maeko).

## Contaminants

- idx 2863/2864/2866/2867/2868/2869: OS status bars
  (time/battery/percent), transcribed and flagged non-game.
- idx 2884/2885/2894: device screenshot-editor overlay
  (Draw / Crop / Share + thumbnail), transcribed and
  flagged non-game.
- idx 2887: full-frame phone lock screen (Azercell, Baku
  weather, Russian charging note) - non-game, noted.
- idx 2891: Discord #announcements wrapper (FenixLua)
  around an embedded 11-pull; app chrome flagged,
  embedded game numbers transcribed.
- idx 2895: Discord #blustone-cafe wrapper around an
  embedded ULTRA battle; same treatment.
- idx 2892: in-game Blog community screen (Vixent post);
  game-adjacent, classified other.

## Sic list

- "Lorked" (idx 2871, middle Locked tag, verbatim).
- "disable enemies immunity" (idx 2858, grammar kept).
- "The Revenant" Calibur (idx 2856, client article vs
  catalog 053 "Revenant").
- "Gullveig" (idx 2860/2874/2879, single-l vs catalog 039
  "Gullveig"); "Calibur" (idx 2875/2876/2878, single-l vs
  library "Calibur"); "Mowgli's" (idx 2876/2879,
  single-o vs catalog 002 "Mowgli").
- Backtick-style spacings "Apollon`s", "Calibur`s",
  "Dino`s" (idx 2874/2878/2879, transcribed with
  apostrophe, sic noted).
- "She's mine. Don't touch her!" (idx 2873, kept verbatim).
- "crocus" (idx 2892, lowercase, kept); "vet tickets".
- "7978x" (idx 2894, last digit cut at frame edge).
- "9x5" (idx 2885, green heal partially obscured).
- "160" (idx 2893, grey top-left partial).
- "Electricity" element wording (idx 2854/2865, vs
  catalog "Lightning").
- OCR misread "41600%" for visual "1600%" (idx 2859, zoom
  wins, recorded as method note).
