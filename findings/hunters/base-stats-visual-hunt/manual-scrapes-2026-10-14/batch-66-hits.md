# Batch 66 hits (idx 3251-3300)

Lane: `findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/`
Crops: `hits/batch-66-3272.png`, `hits/batch-66-3280.png`,
`hits/batch-66-3281.png`, `hits/batch-66-3286.png`,
`hits/batch-66-3288.png`, `hits/batch-66-3289.png`,
`hits/batch-66-3290.png`, `hits/batch-66-3298.png`,
`hits/batch-66-3300.png` (9 HITs, full-frame copies).
Zooms (lane folder, provenance only): `z66_3272_badge`
(Gullveig 3-star gold badge + Lv.1 ribbon + nameplate) /
`z66_3280_badge` (Selene 4-star green badge + Lv.24 ribbon) /
`z66_3281_badge` (Celine 5-star blue badge + Lv.MAX ribbon) /
`z66_3289_badge` / `z66_3290_badge` / `z66_3298_badge`
(Patrone 4-star + Strength 6268 / HP 1132 confirm) /
`z66_3300_badge` / `z66_3286_badge` / `z66_3288_badge` /
`z66_3280_stats` / `z66_3289_stats` (stat blocks).
OCR: tesseract `--tessdata-dir` `%TEMP%/opencode/tessdata`,
`-l eng`. `z66_3272_badge` reads "port Officer / Gullveig"
(drops "Air"); `z66_3289_stats` reads "Deals a total of 92 /
enemies for 4 secc" (drops the 7 of 927 and most words);
`z66_3280_stats` returns nothing legible (stylized numerals).
Zoom wins everywhere; disagreements recorded, no digit taken
from OCR.
Write scripts: `_tmp66_write.py` (+ `_tmp66_verify.py`, kept
in lane per rules). Catalog: card-catalogue.tsv not present
in workspace; catalog_id left blank throughout.

## HITs: 9/50

### idx 3272: Airport Officer Gullveig, Lv.1, 3-star
- File: `Screenshot_20200714-120411_Blustone-2ff01d86d74a6f0a.jpg`
  (1080x2280). Crop: `hits/batch-66-3272.png`.
- Recruited splash; 3 gold stars (1+2) in black circle with
  gold ring + Lv.1 ribbon (zoom-verified `z66_3272_badge`);
  Bomber + Electricity (client wording Electricity, not
  Lightning); coins +1000; Show off now! / See Details /
  Okay; 12:04, 19%.

### idx 3280: White Darkness Selene, Lv.24/30, 4-star
- File: `Screenshot_20200721-210037_Blustone-0e94d51a77284757.jpg`
  (1080x2280). Crop: `hits/batch-66-3280.png`.
- Train Teammate; 4 gold stars (2x2) green ring + Lv.24
  ribbon (zoom-verified `z66_3280_badge`); Strength 8405;
  HP 1204; ATK 1031; DEF 607; skills 40/40 / 32/40 / 30/40 /
  30/40 + locked 5th (Transcendence); Class Bomber +
  Elemental blue-fist icon; Leader / Locked / Rating / Fate;
  Entered Channel 0001; 21:00, 51%.

### idx 3281: Diva of Midgard Celine, Lv.30/30 MAX, 5-star
- File: `Screenshot_20200721-220224_Blustone-58bcb7784f5d9516.jpg`
  (720x1280). Crop: `hits/batch-66-3281.png`.
- Train Teammate; 5 light-blue stars (2+1+2) blue ring +
  Lv.MAX ribbon (zoom-verified `z66_3281_badge`); Strength
  21135; HP 2734; ATK 1257; DEF 1210; skills 50/50 x5;
  Class Support (heart) + Elemental blue-fist icon; Entered
  Channel 0001; 21:00, 51%. Only 5-star of the batch.
- Same hero re-recruited at idx 3286 (+2 days).

### idx 3286: Diva of Midgard Celine, Lv.1, 4-star
- File: `Screenshot_20200723-125619_Blustone-178417ed381cfbd3.jpg`
  (1080x2280). Crop: `hits/batch-66-3286.png`.
- Recruited splash; 4 gold stars (2x2) green ring + Lv.1
  ribbon; Support + Ice (client wording Ice); coins +1000;
  Hunter Bonus HP 12.0?% toast (trailing digit cut); Show
  off now! / See Details / Okay; 12:56, 11%.

### idx 3288: Red Shadow Judith, Lv.1, 4-star
- File: `Screenshot_20200813-011650_Blustone-ee2d7ab095d95ca5.jpg`
  (1080x2280). Crop: `hits/batch-66-3288.png`.
- Recruited splash; 4 gold stars (2x2) green ring + Lv.1
  ribbon; Bomber + Fire; coins +1000; Show off now! / See
  Details / Okay; 01:16.
- Same hero trained at idx 3289 (~85 min later).

### idx 3289: Red Shadow Judith, Lv.1/30, 4-star
- File: `Screenshot_20200813-024119_Blustone-c32d6e4a93cc361e.jpg`
  (1080x2280). Crop: `hits/batch-66-3289.png`.
- Train Teammate; 4 gold stars (2x2) green ring + Lv.1
  ribbon (zoom-verified `z66_3289_badge`); Strength 5021;
  HP 994; ATK 811; DEF 532; skills 1/40 x4 + locked 5th;
  Skill Details modal: Red Rain Lv.1/40 Base, Strike All,
  Uses 4 Rage Gauge, Deals 927 Bleeding Damage to all
  enemies for 4 seconds; Class Bomber + Elemental red-fist
  (Fire); 02:41. Bleed-DoT kit verbatim.

### idx 3290: Leader of the White Forest Kamala, Lv.1/30, 4-star
- File: `Screenshot_20200814-072741_Blustone-9ec857b89644d1e0.jpg`
  (1080x2280). Crop: `hits/batch-66-3290.png`.
- Train Teammate; 4 gold stars (2x2) green ring + Lv.1
  ribbon (zoom-verified `z66_3290_badge`); Strength 5774;
  HP 1173; ATK 548; DEF 764; skills 1/40 x4 + locked 5th;
  Class Defense (shield) + Elemental blue-fist icon;
  Leader / Locked / Rating / Fate; Entered Channel 0001;
  07:27. DEF-heavy base (764 DEF vs 548 ATK).

### idx 3298: Silent Canine Patrone, Lv.1/30, 4-star
- File: `Screenshot_20200829-144620-afcd1396def77ab5.png`
  (720x1280). Crop: `hits/batch-66-3298.png`.
- Train Teammate; 4 gold stars (2x2) green ring + Lv.1
  ribbon (zoom-verified `z66_3298_badge`: Strength 6268,
  HP 1132 confirm); ATK 887; DEF 657; skills 1/40 x4 +
  locked 5th; Class Bomber + Elemental cyan-fist icon;
  Leader / Locked / Rating / Fate; Transcendence greyed.
- Client spelling "Patrone" matches the batch-63 tier-list
  contaminant spelling.

### idx 3300: Gunslinger Blondie, Lv.1, 4-star
- File: `Screenshot_20200831-223351_Blustone-a1c8dd2f9c3be1c3.jpg`
  (1080x2280). Crop: `hits/batch-66-3300.png`.
- Recruited splash; 4 gold stars (2x2) green ring + Lv.1
  ribbon (zoom-verified `z66_3300_badge`); Bomber + Fire;
  coins +1000; Show off now! / Okay; 22:33, 22%.
- Pairs with idx 3299 (same device, 6 min later: defense
  setup then recruit).

## Near-hits (hit=no per bar rules)

### Recruit menu / selector without a pulled hero (hit=no)
- idx 3273: Recruit 30 / 10+1 Recruit 300 (guaranteed
  natural-born 3-star+); 3-star Selection Requests 1;
  lens trace Collect 1 / Collect 7; Mileage 2 stars;
  wallet 257 / 0 / 7.
- idx 3294: 9-option 3-star selector (Nene, Athena, Kain,
  Bear, Edward, Papillon, Dumble, Calibur, Juno).

### 11-pull results without names (hit=no)
- idx 3271: 9x brown 1-star + 1x gold 3-star + 1x green
  4-star; One more time! 300.
- idx 3277: 8x brown 1-star + 2x green 4-star + 1x gold
  3-star (i badges); One more time! 300.

### Jewel stat block without hero (hit=no)
- idx 3276: Shiny Speed Jewel [Mounted on Armor], 4 gold
  stars, Lv.1/15; DEF +16; Damage Reduction Block +0.40;
  Critical Attack Chance +0.75; Block Chance +0.62; Set:
  Mount 4, Increase Attack Speed 1.72.

### Skill-training preview without stars (hit=no)
- idx 3283: Cursed Doll Lv.1/40, Enemy/Strike; Damage
  944 -> 963 (+19, +2.0%); 4532/1 crystals; wallet 607465;
  Begin Training 100; sic "enemy's attack power" spacing.

## Cross-batch pairing notes

- Celine arc: idx 3281 train (Lv.MAX 5-star, 21:00 07-21)
  -> idx 3286 recruit (Lv.1 4-star, 12:56 07-23).
- Judith arc: idx 3288 recruit (01:16 08-13) -> idx 3289
  train (02:41 08-13, Red Rain bleed kit).
- Roster scroll pair: idx 3274 head (36/51, 22:01:24) ->
  idx 3275 tail (36/51, 22:01:34, dup 2473 bridge).
- Same-minute pair: idx 3294 selector -> idx 3295 fight
  club (11:02, 17% battery both).
- Bear-power link: idx 3293 advancement (bear 10856 ->
  10856 flat) vs idx 3295 defense team bear at 10856.
- Defense-then-recruit: idx 3299 (22:27) -> idx 3300
  (22:33, same device).
- Dup-value pairs: 2473 x2 (3275), 2271 x2 (3279),
  746 x2 (3282), 2212 x2 (3287), 5564 x2 (3291).
- Bear-avatar trail: 10550 Defending (3278) / 2464 Lv.1
  (3287) / 6454 Defending Lv.14 (3292) / 7963 Defending
  Lv.22 (3296) / 10856 Lv.MAX defense (3295).

## Most valuable economy/mechanic readings

- Recruit ladder (idx 3273): single 30 / 10+1 300 with
  guaranteed natural-born 3-star+ / 3-star Selection
  ticket (Requests 1) / lens traces 1-vs-7 / Mileage
  2 stars.
- Advancement fee (idx 3293): Level-Up Advancement 43650;
  4-star Lv.MAX -> 5-star Lv.1 keeps Power flat at 10856.
- Skill training (idx 3283): Begin Training 100; +19
  damage (+2.0%) on Cursed Doll 944 -> 963.
- Goals equipment ladder (idx 3297): Modify Equipment 0/3
  pays elemental box trio (fire/ice/lightning x4 each);
  wallet 54569 coins / 97 gems.
- Fight-club points (idx 3295): defeats -5/-5/-6;
  (idx 3299): victories +9/+9; walls 74358 (3295) and
  all-MAX 170683 (3299).
- Build Team (idx 3282): Team Strength 24019; Team
  Effects counter 1.
- Roster endpoints: batch-max head 23401 (3291, 56/63
  annotated long screenshot); rookie floors 2017 (3275),
  2100 (3279), 2212 (3287), 3007 (3296).

## Element / title wording tallies

- Recruit splashes word elements Fire (Judith, Blondie),
  Ice (Celine), Electricity (Gullveig) — Electricity, not
  Lightning, in client.
- Train screens show class text (Bomber / Support /
  Defense) + "Elemental" fist icon in blue (Selene,
  Celine, Kamala), red (Judith), cyan (Patrone); no
  element word printed.
- Client spelling "Patrone" (3298) matches the batch-63
  tier-list contaminant; "Silent Canine" title; "Gunslinger
  Blondie"; "Red Shadow Judith"; "Diva of Midgard Celine";
  "Airport Officer Gullveig"; "Leader of the White Forest
  Kamala"; "White Darkness Selene".
- Selector list (3294): Walking Disaster Nene / Flame of
  Battlefield Athena / Steely Bodyguard Kain / Nature's
  Gift Bear / Robot Engineer Edward / Notorious
  Jail-breaker Papillon / Strange Old Man Dumble /
  Revenant Calibur / Aircraft Mechanic Juno.

## Contaminants

- idx 3285: official Blustone lifeguard promo art
  (full-body + chibi, VisualShower copyright) — not a
  screenshot; classified other.
- No YouTube/blog/Play Store contaminants in this batch.

## Sic list

- "enemy's attack power" spacing ("enemy 's", 3283).
- "The Hunter that participated in the Advancement Match
  will be spent" (3293).
- "it's tome for you to leave." (3295 Dragonpatch).
- "Show off now!" (all recruit splashes).
- Re-recruit pairs: Celine (3281/3286), Judith (3288/3289).
