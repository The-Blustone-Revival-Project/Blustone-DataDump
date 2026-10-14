# Batch 52 hits (idx 2551-2600)

Lane: `findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/`
Crops: none (0 HITs).
Zooms (lane folder, provenance only): `z52_2565_traces`,
`z52_2580_steps`, `z52_2581_lock`, `z52_2581_rows`, `z52_2583_def`,
`z52_2579_band`.
OCR (lane folder): `_tmp52_ocr/` (2579 over-cap band, tesseract
`--tessdata-dir` `%TEMP%/opencode/tessdata`, `-l eng`).
Write scripts: `_tmp52_write.py`, `_tmp52_hits.py` (kept in lane
folder per rules).

## HITs: 0/50

No frame in this batch shows named hero + level + star rank +
HP/ATK/DEF or Strength together. The 14 recruit-confirmation
prompts carry name + title + 3-star gold medallion but no level
ribbon and no stats; the Transcendence setup (idx 2598) carries
name + level + fodder Strength but no star badge; hunter-list
rows carry level + Strength but no names. All hit=no per bar
rules.

## Near-hits (full numbers, hit=no per bar rules)

### idx 2598: Hunter Transcendence Walking Disaster Nene, Lv.27 (catalog 003)
- File: `Screenshot_20180413-194527-63464932e02e6392.png` (1080x1920).
  Main hunter Lv.27 (pink ribbon); fodder "Select a hunter." 1/1:
  Lv.1, Strength 2116, checked green; "To transcend the hunter
  above, only identical hunters who are 3-star or above can be
  used as fodder. The used hunter will disappear."; Items
  Required: blue crystal 9/9, blue blobs 245/90; Transcendence
  fee 9000 coins; wallet coins 10219.
- No star badge on frame. Hit=no.

### Recruit-confirmation prompts with title + 3-star medallion, no level, no stats (all hit=no)
- idx 2551: Noble Spear Natalia, Offense + Ice (catalog 037).
- idx 2552: Wolf Child Bibi, Offense + Electricity (catalog 040).
- idx 2553: Walking Disaster Nene, Defense + Ice (catalog 003).
- idx 2554: Flame of the Battlefield Athena, Defense + Fire
  (catalog 027).
- idx 2555: Steely Bodyguard Kain, Defense + Electricity
  (catalog 029).
- idx 2556: Nature's Gift Bear, Defense + Electricity
  (catalog 036).
- idx 2557: Robot Engineer Edward, Defense + Electricity
  (catalog 041).
- idx 2558: Notorious Jail-breaker Papillon, Defense + Ice
  (catalog 043).
- idx 2559: First Ever Hunter Lantern, Bomber + Fire
  (catalog 001).
- idx 2560: Thunder Arrow Diana, Bomber + Electricity
  (catalog 031).
- idx 2561: Silent Canine Patrone, Bomber + Ice (catalog 033).
- idx 2562: Airport Officer Gullveig, Bomber + Electricity
  (catalog 039).
- idx 2563: Maiden of Gods Akasha, Support + Electricity
  (catalog 008).
- idx 2564: Walking Infirmary Joy, Support + Fire (catalog 035).
- 10-pull grids, art-only with no names on frame (hit=no):
  idx 2599 (8x 1-star + 2x gold 3-star) / idx 2600 (6x 1-star +
  4x gold 3-star incl. brown bear center); "One more time!
  300" per pull.

### ELEMENT NOTE (extends the Electricity arc)
- Client "Electricity" vs catalog "Lightning" on 7 prompts:
  Bibi (040), Kain (029), Bear (036), Edward (041), Diana
  (031), Gullveig (039), Akasha (008). Ice/Fire prompts match
  catalog (Natalia 037, Nene 003, Papillon 043, Athena 027,
  Lantern 001, Patrone 033, Joy 035).

### TITLE DISCREPANCY
- idx 2554/2577: client "Flame of the Battlefield" vs catalog
  027 "Flame of Battlefield" (client inserts "the").

## Cross-batch pairing notes

- Recruit-prompt run (14 frames, same 540x960 prompt chrome):
  idx 2551 Natalia -> 2552 Bibi -> 2553 Nene -> 2554 Athena ->
  2555 Kain -> 2556 Bear -> 2557 Edward -> 2558 Papillon ->
  2559 Lantern -> 2560 Diana -> 2561 Patrone -> 2562 Gullveig
  -> 2563 Akasha -> 2564 Joy.
- Hunter-list scroll pair (27/45, same account): idx 2571
  (15085 head ... 2230 tail) -> 2572 (2059 ... 369 x3 tail,
  empty slots). Roster endpoints 15085 -> 369.
- Duplicate Build Team frames: idx 2573 / 2574 identical
  (6776 Leader head, duplicate 3436 pair, duplicate 1828
  pair, 1807 tail).
- Search chain (same day): idx 2568 (fuel 18/60, Electric
  Abyss 36/80 Search Complete + Giant Shelter 36/80 Search)
  -> 2569 (fuel 58/60, 36/80 Search Complete + Shelter
  0-times/1-times rows).
- Mirage Shop pair (same 9-line ladder): idx 2585 (balance
  50, timer 15:45:41) -> 2595 (balance 548, timer 14:40:50,
  about 65 min apart).
- Voidne day-over-day: idx 2594 (Level 18, power 23247,
  league 1184, Emerald Canyon - Area 86) -> 2596 (Level 19,
  power 24396 (+1149), league 1164 (-20), Recently Played
  Fight Club). Same reg date 04/12/2018.
- Harley art pair: idx 2578 (See Details, client-blurred art)
  -> 2590 (See Details, full masked-hero art).
- 10-pull pair: idx 2599 -> 2600 (300-gem "One more time!"
  pricing both frames).

## Most valuable economy/mechanic readings

- Mirage Shop ladder (idx 2585/2595, full transcription):
  Harley's Traces x3 300; Papillon's Trace x3 150;
  Gullveig's Trace x3 150; Special Request x1 3000; Metron
  Crystal x1 500; Unusual Metal Piece x10 500; Invincible
  Shell x10 500; Scorching Flamestone x10 500; Fruit-Bearing
  Herb x10 500. Balances 50 -> 548.
- Over-cap stacks (idx 2579, OCR-verified): Manda Spent
  262/30 (8.7x cap); fuel Spent 5,264/200 (26.3x cap).
- Transcendence setup (idx 2598): identical-hunter 3-star+
  fodder rule verbatim; fee 9000; mats 9/9 + 245/90; wallet
  10219.
- Skill training (idx 2591): Lv.20/40 Attack Speed Increase,
  18.00% -> 18.40% (+0.40pp); mats 174/3, 3/4 red
  shortfall, 27/1; fee 500; coins 1318.
- Maxed skill (idx 2597): Lv.50/50 Decreased Enemy Damage,
  Damage 30.0%; "Maximum value you can train now."; coins
  1307853.
- Veteran Expert ladder (idx 2586): Expert 2, 2710/5120,
  2410 to Expert 3; Fuel/Rupee/Invitations Recharge +8 each.
- Attendance ladder (idx 2570): Day1 x3000 / Day2 x1 /
  Day3 x5000 / Day4 x120 / Day5 x4 / Day6 x10 / Day7 x1, all
  Received; 20 Veteran Points per day; cumulative 0/28;
  Professional 3, 1060/1280.
- Fight Club tier rewards (idx 2566): Gold X100 + X2 /
  Emerald X150 + X2 / Metron X200 + X2 / Mandarin X100 + X2.
- Lottery Mouse walnut steps (idx 2580, zoom-verified):
  5 Stages (Dispatch counts) 1 Walnut; 1 Abyss 5 Walnuts;
  1 Search 3 Walnuts; Scroll recruit (Excludes Evaluation
  Request) 6 Walnuts; Manda recruit 40 (cut).
- Defense trace board (idx 2577): Defense 8/9, bonus
  8.0% -> 9.0%; Harley 0/160, Kain 6/80, Nene 19/80,
  Dumble 0/80, Athena 12/80, Edward 12/80.
- Ruins 83 stages (idx 2587): STAGE 6/7/8/9 COMPLETE,
  STAGE 5 cut.
- Team Tips (idx 2588): Playing Level 83, 상위 55.56%;
  130 yonghannogugu / 119 小宇宙 / 115 NwxRar / 108
  Clownbaby / 101 와따시모 / 84 Arilmes.
- Fully-Active rotation (idx 2589): Lantern / Nene /
  Mowgli / Tyltyl, 2 Days left; next Akasha / Gerard /
  Rebecca / Sylvester.
- Friend anchors: Alaiko Lv.88 reg 05/18/2017 (oldest in
  batch) power 84599 league 3313 Cryogenic Abyss - Area 7
  (idx 2592); Shin7412 Level 45 reg 03/15/2018 power 49244
  league 2595 Area 4 (idx 2593). All VER. 1354.
- Maintenance gate (idx 2575): Midgard storm countdown
  001:25:09, Go to Community.
- Trace payout (idx 2565, zoom-verified): 2 finishes ->
  3+3 traces.
- Hidden ruins (idx 2567): UNIQUE, Wolf Child Bibi 3-star,
  00:58:33, 4 loots.
- 10-pull pricing (idx 2599/2600): 300 gems per pull.

## Non-ASCII names (verbatim, for searchability)

- idx 2551-2564: Natalia; Bibi; Nene; Athena; Kain; Bear;
  Edward; Papillon; Lantern; Diana; Patrone; Gullveig;
  Akasha; Joy. idx 2568/2569: X_man_20000. idx 2588:
  상위; yonghannogugu; 小宇宙; NwxRar; Clownbaby;
  와따시모; Arilmes; Emmalyn. idx 2589: Lantern; Nene;
  Mowgli; Tyltyl; Akasha; Gerard; Rebecca; Sylvester.
  idx 2591: Biqker. idx 2592: Alaiko; Cyana; Fin; KronX.
  idx 2593: Shin7412. idx 2594/2596: Voidne. No
  Korean-script hunter names in batch.

## Contaminants

- idx 2570: OS status bar (11:06 PM, 21%) across frame top;
  game data transcribed, status-bar values noted only.
- idx 2593: real-person photo avatar on friend profile
  (external photo, kept as other with note).
- idx 2582: 307x486 event-toast crop ("Supplies have
  arrived! Supplies"), game content, kept as other.

## Sic list

- "Flame of the Battlefield" (idx 2554/2577, client title
  verbatim vs catalog "Flame of Battlefield").
- "Class Elemental" (idx 2567, collapsed labels verbatim).
- "1 Walnut" vs "5 Walnuts / 3 Walnuts / 6 Walnuts"
  (idx 2580, singular/plural asymmetry verbatim).
- "Recruit with Scroll (Excludes Evaluation Request)"
  (idx 2580, Evaluation Request client term, zoom-verified).
- "Clear 5 Stages (Dispatch counts)" (idx 2580, Dispatch
  annotation verbatim).
- "Metron Tier" / "Mandarin Tier" (idx 2566, tier-name
  spelling verbatim; Metron consistent with Mirage Shop
  "Metron Crystal").
- "Tyltyl" (idx 2589 rotation) vs "Tyltyl's What's in the
  Box?" (batch-48 idx 2395 promo copy); both verbatim.
- "A storm named 'Maintenance' is currently ravaging
  Midgard." (idx 2575, notice copy verbatim).
- Blur-not-sic: "Lorked"/"Defegding" first-glance reads
  (idx 2581/2583) rejected by zoom, read "Locked" /
  "Defending"; not recorded as sic.
