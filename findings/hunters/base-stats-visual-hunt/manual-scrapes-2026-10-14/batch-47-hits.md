# Batch 47 hits (idx 2301-2350)

Lane: `findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/`
Crops: `hits/batch-47-2312.png`, `hits/batch-47-2319.png`,
`hits/batch-47-2330.png`, `hits/batch-47-2333.png`,
`hits/batch-47-2336.png`, `hits/batch-47-2342.png`.
Zooms (lane folder, provenance only): `z47_2301_board`,
`z47_2310_board`, `z47_2312_chevron`, `z47_2312_med`,
`z47_2319_left`, `z47_2321_teams`, `z47_2330_med`,
`z47_2333_med`, `z47_2336_left`, `z47_2337_hub`,
`z47_2341_assign`, `z47_2342_med`, `z47_2347_shop`,
`z47_2349_assign`, `z47_2350_shop` (+ superseded `_plaque`,
`_badge`, `_mid`, `_low`, `_left` drafts kept in folder).
OCR: tesseract `--tessdata-dir` `%TEMP%/opencode/tessdata`, `-l eng`
(2301 season timer/medals/board; 2310 Fight Specs 184734; 2347
package panel; 2350 Hidden Shop ladder).

## HITs: 6/50

### idx 2312: Elite Messenger Hermes, Lv.1, 3-star (catalog 023)
- File: `Screenshot_2017-10-08-01-32-07-80-fbbcab9ca5b19dc0.png`
  (720x1280). Recruited plaque; 3-star gold medallion + Lv.1 ribbon
  (zoom-verified `z47_2312_chevron`/`z47_2312_med`); top chevron
  3 filled stars; Offense + Fire icons; coins 1000.
- Catalog 023 exact (Offense/Fire, Coffee Rabbit).

### idx 2319: Silent Canine Patrone, Lv.1, 5-star, Strength 37864 (catalog 033)
- File: `Screenshot_20171013-212926-2bad7d1e310afdc9.png`
  (1080x1920). Train Teammate; 5-star blue compass badge + Lv.1
  ribbon (zoom-verified `z47_2319_left`); bomber Class + blue
  Elemental icons; 5 gear slots (lattice-lit + 2 shields + pawn +
  bra).
- Catalog 033 (Bomber/Ice); 5-star transcended state on frame.

### idx 2330: Halloween Witch Riko, Lv.1, 2-star
- File: `Screenshot_2017-10-20-18-47-31-5bcb3b3002bf5c39.png`
  (1440x2560). Recruited plaque; 2-star silver medallion
  (zoom-verified `z47_2330_med`); Defense + Ice icons; coins 1000.
- Catalog blank (costume variant; base Riko 024 is "Hard-Knock
  Life"). Witch Riko is the subject of the idx 2345 whisper joke.

### idx 2333: Experiment #2 Sunny, Lv.1, 2-star (catalog 022)
- File: `Screenshot_20171021-134130-e88bf3be3bff351a.png`
  (1080x1920). Recruited plaque; 2-star silver medallion
  (zoom-verified `z47_2333_med`); Support + Ice icons; coins 1000.
- Catalog 022; TITLE NOTE client "Experiment #2" vs catalog
  "Experiment 2" (hash discrepancy).

### idx 2336: Hard-Knock Life Riko, Lv.30 MAX, 5-star, Strength 52598 (catalog 024)
- File: `Screenshot_20171022-220857-38aba71c8ef9e7e1.png`
  (1080x1920). Train Teammate; 5-star blue compass badge + Lv.MAX
  ribbon (zoom-verified `z47_2336_left`); shield Class + gold paw
  Elemental icons; 5 gear icons.
- Catalog 024 (name+title exact; 5-star transcended state). Pairs
  with idx 2311 transcend staging (same-account Riko arc).

### idx 2342: In Wonderland Tyltyl, Lv.1, 1-star
- File: `Screenshot_20171023-231835-eb0b53cc5332dcd6.png`
  (720x1280). Recruited plaque; 1-star bronze medallion + Lv.1
  ribbon (zoom-verified `z47_2342_med`); Support + Electricity
  icons; coins +1000.
- Catalog blank (costume variant; base Tyltyl 004 is 1-star Support
  but Fire element).
- ELEMENT NOTE: client "Electricity" vs catalog 004 "Fire"
  (extends the batch-29/30/32/34/38/40/43 Electricity arc).

## Near-hits (full numbers, hit=no per bar rules)

### idx 2311: Hunter Transcendence staging, Riko Lv.23
- File: `Screenshot_20171011-013102-489ba726ed1605db.png`
  (1080x1920). Fodder rule verbatim ("Only hunters above 3-star
  can be used as fodder. The hunter used to transcend will
  disappear."); fodder Riko Lv.1 5725 + 5732; Items Required
  23/25 + 380/250; Transcendence 25000; coins 16395.
- Hit=no (staging screen, no star rank + Strength on one hero).

### idx 2327: Victory screen, zero rewards
- File: `Screenshot_2017-10-20-08-11-40-0bdbe2caf2702cff.png`
  (720x1280). Victory! + nickname prompt (100 chars); Fight Chip
  Acquired 0; Winning Point 0^0 (sic caret separator, never
  normalized).
- Hit=no (no hero panel).

## Cross-batch pairing notes

- Maeko晓 account arc: idx 2328/2329 art-only name crop
  (Alaiko / Maeko晓) -> idx 2337 village hub (Maeko晓 entered
  channel 0001, fuel 93/60, Rank 1483) -> idx 2340 region select
  (same fuel 93/60, same session) -> idx 2345 whisper
  ("I'll never give you Witch Riko, Maeko").
- Riko account arc: idx 2311 transcend staging (Riko Lv.23,
  0/2 fodder) -> idx 2336 train (Riko Lv.30 MAX, 5-star,
  Strength 52598).
- Trace-result run (12 screens): 2313 (8x) -> 2315 (3x) ->
  2316 (5x) -> 2320 (3x) -> 2324 (4x) -> 2326 (2x) -> 2331 (10x)
  -> 2332 (1x) -> 2334 (7x) -> 2335 (10x) -> 2343 (6x) ->
  2346 (8x); paw-icon vs red-haired-girl icon variants recur.
- Hunter List scroll arc (2302-2309): 78/84 roster top
  (62985 MAX) -> duplicate 2303 -> mid 2304 -> 7k tail 2305 ->
  6k band 2306 -> 6276->3381 cliff 2307 -> rookie farm 2308 ->
  1269/1099/1094 tail 2309.
- Shop session pair: idx 2344 (1600% fuel x960 + 3 veteran-point
  certificates) + idx 2348 (200% coin x10000).
- Assignments pair: idx 2341 (Expert 2, 3380/5120, bonus 12/7)
  vs idx 2349 (Expert 1, 2350/2560, bonus 5/7) — two accounts.

## Most valuable economy/mechanic readings

- Hidden Shop ladder (idx 2350, zoom+OCR): gem balance 25; Fuel
  480->50 gems / Rupee 5000->12 / Challenge Invitation 20->50 /
  Metron Crystal 1->50 / Metron Fragment 50->10 / Rusty Metal
  Piece 20->10 / Broken Shell 20->10 / Cold Flamestone 20->10 /
  Withered Herb 20->10.
- IAP package ladder (idx 2347, zoom+OCR): fuel pack 3.49 GBP /
  scroll 20.99 GBP (LOCALE SIGNAL: GBP pricing); Goal
  Achievement Package ("A chance to earn 2-star+3-star hunters!
  3300 Purchase Complete"); Wealthy 3300 / Prosperous 5500 /
  Rolling in Money 11000; Expert 3, 11140/11520.
- Purchase popups: 1600% fuel x960 + Veteran Point Gift
  Certificate 3 (idx 2344); 200% coin x10000 (idx 2348).
- Assignments panels: bonus 12/7 over cap (idx 2341) vs 5/7
  greyed (idx 2349); task ladder Receive Supplies 1/2 (fuel x30)
  / Buy Item 0/1 (coins x1000) / Challenge 0/3; Check In
  Complete x1000 silver.
- Exploration regions (idx 2340): Wolf's Mouth 6day 04:40:03
  8/40 vs Emerald Canyon 13day 04:40:03 48/40 (over cap).
- Over-cap stacks recur: fuel 93/60 (2337/2340), bonus 12/7
  (2341), 48/40 region (2340).
- Fight Club: Mandarin Tier season 0 Days 16:22:48, medals 1905,
  tickets 1/6, ranks 18-20 Alaiko 2304 / Yang0123 2297 /
  BearHans 2265 (badges 63/71/71), Next League coins x2500 +
  medal x250 (idx 2301); Choose Opponent refresh 00:01:45,
  team 120183 vs row 184734, Maeko晓 243/1448 badge 36 (2686)
  vs Lesfer 225/1459 badge 33 (idx 2310); friendly StarryNigh
  vs Jasssy ticket 0 (idx 2321).
- Date/version anchors: VER. 1152 + Registration 05/17/2017
  (idx 2322, oldest anchor in batch); Marcien Level 67, Team
  Strength 141091, League Points 2036; Veteran Points
  3380/5120 (Expert 2) vs 2350/2560 (Expert 1) vs 11140/11520
  (Expert 3); village Rank 1483, stars 300/450.
- Transcend economy (idx 2311): 25000-coin fee; fodder bar
  above 3-star; items 23/25 + 380/250.

## Non-ASCII names (transliterated, for searchability)

- idx 2301: Alaiko; Yang0123; BearHans; infinitea. idx 2302:
  Enheim. idx 2307: PoopyDickFart. idx 2310: Maeko + kanji 晓
  (kept verbatim in TSV); Lesfer. idx 2311/2330/2336: Riko;
  Eryza. idx 2312: Hermes. idx 2319: Patrone; Derrik. idx 2321:
  Jasssy; StarryNigh. idx 2322: Marcien. idx 2328/2329/2337/
  2345: Alaiko; Maeko晓; VSpang. idx 2333: Sunny. idx 2342:
  Tyltyl. idx 2350: The-Lawford.

## Contaminants

- idx 2326: phone media-volume overlay on trace-result screen
  (game digits intact underneath).
- idx 2314: blank loading screen (zero text/digits, single view).
- idx 2325: partial 1080x683 hunter-list crop (mid-band only).
- idx 2345: 588x722 village whisper crop (partial frame).
- idx 2328/2329: 332x418 art-only crops (exact duplicates).
- idx 2303: duplicate frame of 2302.
