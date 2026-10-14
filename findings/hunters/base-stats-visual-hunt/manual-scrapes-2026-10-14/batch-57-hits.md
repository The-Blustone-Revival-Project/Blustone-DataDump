# Batch 57 hits (idx 2801-2850)

Lane: `findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/`
Crops: `hits/batch-57-2809.png`, `hits/batch-57-2820.png`,
`hits/batch-57-2821.png`, `hits/batch-57-2824.png` (4 HITs).
Zooms (lane folder, provenance only): `z57_2809_badge`
(Windblade 4-star green ring + Lv.10), `z57_2820_badge`
(Lantern 3-star gold + Lv.1), `z57_2821_badge` (Dino 3-star
gold + Lv.28), `z57_2824_badge` (Bruce Bang 5-star blue +
Lv.30/Lv.MAX), `z57_2829_lorked` (8144 Locked),
`z57_2846_lorked` (24487 Locked), `z57_2825_prices` (Fight
Chips 375s), `z57_2836_bottom` (4233/4073/cut),
`z57_2840_fuel` (flavor text, digits missed).
OCR (lane folder): `_tmp57_ocr/` (badge zooms + fuel +
prices, tesseract `--tessdata-dir` `%TEMP%/opencode/tessdata`,
`-l eng`; badge art returns blank, fuel reads flavor text
only, prices blank).
Write scripts: `_tmp57_dims.py`, `_tmp57_zoom.py`,
`_tmp57_ocr.py`, `_tmp57_write.py`, `_tmp57_hits.py`,
`_tmp57_dims_check.py` (kept in lane folder per rules).

## HITs: 4/50

### idx 2809: Windy Soul Windblade, Proficient Hunter Lv.10, 4-star, Strength 7342 (catalog 052)
- File: `Screenshot_20180721-002834_Blustone-f6b94f397ed622a8.jpg`
  (720x1480). Crop: `hits/batch-57-2809.png`.
- Train Teammate; 4-star green-ring badge + Lv.10 ribbon
  (zoom-verified `z57_2809_badge`; first-glance 3-star
  read rejected by zoom, zoom wins); Class + Elemental
  icons; Train / Transcendence / Skill Training /
  Upgrade Equipment / Story.
- Samsung Bixby Vision / Draw / Crop / Share bottom bar
  is screenshot-app UI (external, not game).
- OCR-vs-zoom: tesseract blank on star art, visual star
  count wins.

### idx 2820: First Ever Hunter Lantern, Experienced Hunter Lv.1, 3-star, Strength 1909 (catalog 001)
- File: `Screenshot_20180727-064901-c9dbc4ebf24eb689.png`
  (720x1280). Crop: `hits/batch-57-2820.png`.
- Train Teammate; 3-star gold badge + Lv.1 ribbon
  (zoom-verified `z57_2820_badge`); Class + Elemental
  icons.
- Title matches catalog 001.
- Same-account trio 2820 -> 2821 -> 2822 (Lantern 1909
  Lv.1 reappears in the 2822 build-team grid).

### idx 2821: Genius Climatologist Dino, Experienced Hunter Lv.28, 3-star, Strength 2596 (catalog 054)
- File: `Screenshot_20180727-065019-e2c0cb27dfd629f3.png`
  (720x1280). Crop: `hits/batch-57-2821.png`.
- Train Teammate; 3-star gold badge + Lv.28 ribbon
  (zoom-verified `z57_2821_badge`); skill icons row.
- Same-account trio (Dino 2596 Lv.28 Offense Team in the
  2822 grid; recruit splash of the same Dino in idx
  2804).

### idx 2824: Death Metal Preacher Bruce Bang, Master Hunter Lv.30, 5-star, Strength 10307 (catalog 016)
- File: `Screenshot_20180727-135926-879d42d63ecb8941.png`
  (1080x1920). Crop: `hits/batch-57-2824.png`.
- Train Teammate; 5-star blue-ring badge (large center
  star + 4 small) with Lv.MAX mini-ribbon + Lv.30 text
  (zoom-verified `z57_2824_badge`); Class (heart) +
  Elemental (ice) icons; Advance greyed out /
  Transcendence / Skill Training / Upgrade Equipment /
  Story; 5 skill icons; lock + card icons top-right.
- Title matches catalog 016. Reconnecting-to-Chat-Server
  banner; Android nav buttons (external).
- OCR-vs-zoom: tesseract blank on star art, visual star
  count wins.

## Near-hits (full numbers, hit=no per bar rules)

### Recruit splashes with level + stars, no stats (all hit=no)
- idx 2803: The Revenant Calibur, 3-star gold badge +
  Lv.1 ribbon, Defense + Fire, +1000 (catalog 053).
  TITLE NOTE: client "The Revenant" vs catalog
  "Revenant" (article).
- idx 2804: Genius Climatologist Dino, 3-star, Lv.1,
  Bomber + Ice, +1000 (catalog 054). Same-account pair
  with the idx 2821 Train screen.
- idx 2817: Robot Engineer Edward, 3-star, Lv.1,
  Defense + Electricity, +1000 (catalog 041). ELEMENT
  NOTE: client "Electricity" vs catalog "Lightning".

### Transcendence setup with level + Strength preview, no star rank (hit=no)
- idx 2844: Hunter Transcendence Noble Spear Natalia,
  Lv.MAX, Strength 22111 -> 24372 (+2261, x1.102);
  fodder 3x Lv.1 2508 identical (3/3); "only identical
  hunters who are 3-star or above can be used as
  fodder"; mats 98/80 + 1672/800; Transcendence cost
  80000; wallet 83757. Title matches catalog 037.

### 11-pull results, star counts only (hit=no)
- idx 2831: 6x 2-star (silver) / 5x 1-star (brown);
  "One more time! 300".
- idx 2841: 6x 1-star / 2x 2-star / 2x 3-star (gold) /
  1x 4-star (green, white-bunny, i-badge); "One more
  time! 300".

## Cross-batch pairing notes

- Same-account trio: idx 2820 (Lantern Train, 1909) ->
  2821 (Dino Train, 2596) -> 2822 (build team with
  Lantern 1909 Lv.1 + Dino 2596 Lv.28 in grid, rookie
  floor 282).
- Near-duplicate Build Team pair: idx 2812 -> 2813
  (same 6278/3622/2588/3074 team, "The team is full."
  toast).
- Build-team trail (16/30 account): idx 2810 (top team
  4657/3611/2456/3380) -> 2816 (Hunter List 16/30 with
  3611/2456/2401 repeat).
- Hunter-list scroll pair (42/57, same account): idx
  2829 (head 19433 ... 7309 Locked) -> 2830 (tail with
  4289/3340/2638 dupe pairs ... floor 2435). Roster
  endpoints 19433 -> 2435.
- Hunter-list scroll quad (61/66, same account): idx
  2836 (head 21025 ... bottom 4233/4073/cut) -> 2837
  (4233/4072/3904 ...) -> 2838 (2435 x5 + 2410 dupe)
  -> 2839 (2354 quad + 2389/2152 dupes ... floor 921).
  Full span 21025 -> 921. OS status-bar + nav-button
  contaminants on all four.
- Hunter-list scroll quad (107/126, same account): idx
  2846 (head 29926 ... 23289) -> 2847 (22967 ...
  19359) -> 2848 (19262 ... 9887 rookie dip) -> 2849
  (floor 9829 ... 2935). Full span 29926 -> 2935 (batch
  max roster).
- Fight-club pair (1/6 tickets, Begin Battle 1, same
  5x Lv.MAX ally team): idx 2833 (Silver Tier,
  Diplodok) / idx 2834 (Metron Tier, Korean-named
  opponent).
- Equipment ladder (Upgrade Equipment chrome, HP/ATK/
  DEF labels): idx 2808 (skates Lv.30 set, +1317) /
  idx 2818 (full 8-slot Lv.30/30/29 set, +5425) / idx
  2819 (Lv.20 twin-dagger set, +3556).

## Most valuable economy/mechanic readings

- Fight Chips ladder (idx 2825, top-5 zoom-verified):
  Beckhen's / Lantern's / Akasha's / Diana's /
  Octavia's Traces x5 375 each (Fight Chips icon +
  375 pills in `z57_2825_prices`); Heidi's Traces row
  "Purchase complete"; wallet 835; list refresh
  03:59:50; bottom row Elite/Special Request + Metron
  Crystal (prices cut).
- Trace stock ladder (idx 2845, Inventory Hunter
  Traces): Harley's Traces 60 @ 1000 (premium) vs
  Yuri 5 / Bibi 49 / Therapy 1 / Dumble 4 / Natalia
  58 / Calibur 162 @ 200; Papillon 3 / Patrone 24
  (prices cut); wallet 3426. Singular "Trace" vs
  plural "Traces" asymmetry verbatim.
- Transcendence setup (idx 2844, Natalia): 3/3
  identical fodder (Lv.1 2508 x3), mats 98/80 +
  1672/800, 80000 coins, wallet 83757. Delta +2261
  (x1.102).
- Fuel price ladder (idx 2840): x60 fuel for 5000
  Rupees / 1 Coupon / 5 Manda; wallet 224192 / 257 /
  0; Current Amount 82/0 (zero-digit); Veteran
  Professional 2; Daily Purchase 8/8.
- Over-cap fuel readings: 564/60 (9.4x, idx 2815),
  60/60 full (idx 2827), fuel cap 82 (idx 2832),
  78/82 (idx 2832).
- 11-pull pricing (idx 2831/2841): 300 gems per pull.
- Event promo (idx 2850): Tyltyl's What is in the Box,
  Golden Chest per 15,000 rupees spent; Rupees Spent
  12,300/15,000 (2700 to next chest); timer
  63:47:03.
- Recruit hub (idx 2806): 10+1 for 300 gems (2-star+
  guarantee); Request ladders 2~4-star x5 / 3~4-star
  x3; wallet 173 / 49 / 0; Recruitment Mileage 2
  gold stars.
- Fate-story buffs (idx 2823): HP/ATK/DEF +12% each;
  fate rows The Dummy / Please Stop / My Muse /
  Absolute pitch, "Less than 30 sec." each.
- Battle costs: Begin Battle 9 fuel (Area 115, idx
  2815); Select Partner 25 fuel (Volcanic Abyss Area
  3, idx 2827).

## Non-ASCII names (verbatim, for searchability)

- idx 2801/2802: H20 (OS carrier string). idx 2803:
  Calibur. idx 2804/2821: Dino. idx 2806: Diana.
  idx 2809: Windblade. idx 2812/2813: OsNologia.
  idx 2817: Edward. idx 2820:
  Lantern. idx 2823: lneafnb. idx 2824:
  Bruce Bang. idx 2826: Karl Steiner; Hermes;
  Octavia; Natalia; Bibi; Yuri. idx 2828:
  AzraelxLacy; Windy. idx 2832: xROiD;
  cloudinknight. idx 2833: Diplodok. idx 2834:
  할인 (Korean). idx 2844: Natalia. idx 2845:
  Harley; Yuri; Bibi; Therapy; Dumble; Natalia;
  Calibur; Papillon; Patrone. idx 2850: Tyltyl.
  No Korean-script hunter names in batch.

## Contaminants

- idx 2801: Google Play store page (OS-level, not
  game UI).
- idx 2802: phone home-screen folder (OS-level).
- idx 2809: Samsung Bixby Vision / Draw / Crop /
  Share screenshot bar (external).
- idx 2824/2836/2837/2838/2839/2845/2846/2847/2848/
  2849: Android nav buttons (external); 2836-2839
  also OS status-bar strings (C:51/53 B:35/38
  M:714/581/520/521MB 430/807/480MHz) transcribed
  and flagged non-game.
- idx 2826/2828/2831: photo-collage chat avatars
  (external photos); 2827: chat dog avatar covering
  the 3rd opponent slot (game number lost, recorded
  as Lv.?).
- idx 2842: VIVA.co.id Indonesian browser article
  (external, non-game).
- No wiki/Discord contaminants, no error pairs.

## Sic list

- "The Revenant" Calibur (idx 2803, client article
  vs catalog 053 "Revenant").
- "Electricity" (idx 2817, client element vs
  catalog "Lightning").
- "0day" x2 (idx 2832, zero not letter O).
- "Wolf's Mouth" WITH apostrophe (idx 2832,
  wording variant vs "Wolfs Mouth" elsewhere).
- "Tyltyl`s" (idx 2850, backtick for apostrophe).
- "rupees" lowercase (idx 2850, vs "Rupee"
  elsewhere); "Rupees Spent 12,300/15,000".
- "할인" (idx 2834, Korean opponent name verbatim).
- "The Frost Witch" Octavia (idx 2826, client
  article vs catalog 028 "Frost Witch"; extends
  batch-54 arc).
- "Beckhen's Traces" / "Lantern's Trace" /
  "Akasha's Trace" possessive-trace naming (idx
  2825, zoom-verified); "Trace" vs "Traces"
  singular/plural asymmetry (idx 2825/2845).
- "Calibur's" spelling (idx 2845, matches catalog
  "Calibur").
- Blur-not-sic: "Lorked" first-glance reads (idx
  2829 8144 row / idx 2846 24487 row) rejected by
  2-3x zoom, both read "Locked"; not recorded as
  sic (extends batch-52 precedent).
- OCR-not-sic: tesseract blanks on star-badge art
  (idx 2809/2820/2821/2824) and flavor-text-only on
  the fuel zoom (idx 2840); visual reads win, not
  recorded as sic.
