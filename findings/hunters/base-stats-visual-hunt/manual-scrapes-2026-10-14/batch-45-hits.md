# Batch 45 hits (idx 2201-2250)

Lane: `findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/`
Crops: none (0 HITs).
Zooms (lane folder, provenance only): `z2201_profile` (Level 69 /
Team Strength 183978), `z2208_band` (Strength 37226),
`z2231_defense` (Calamity defeat row).
OCR (lane folder): `_batch45_ocr.json` (50 frames, tesseract
`--tessdata-dir` `%TEMP%/opencode/tessdata`, `-l eng`; binary capture +
UTF-8 decode; mostly sparse on art-heavy frames).

## HITs: 0/50

No frame in this batch shows named hero + level + star rank + HP/ATK/DEF
or Strength together. Recruit splashes carry name + Lv.1 + 3 stars but no
stats; transcendence splashes carry name + Lv.MAX + full before->after
stats but no star rank; Train screens carry name + Strength but no level.
All hit=no per bar rules.

## Near-hits (full numbers, hit=no per bar rules)

### Recruits with name+title+level+stars but no stats (hit=no)
- idx 2225: Immortal One Karl Steiner, Lv.1, 3-star, Offense +
  Electricity (catalog 012; Electricity vs catalog Lightning).
  coin +1000.
- idx 2226: The Frost Witch Octavia, Lv.1, 3-star, Offense + Ice
  (catalog 028; TITLE NOTE: The Frost Witch vs catalog Frost Witch).
  coin +1000. Same-session pair idx 2232 (banner cropped).
- idx 2229: Flame of the Battlefield Athena, Lv.1, 3-star, Defense +
  Fire (catalog 027; TITLE NOTE: Flame of the Battlefield vs catalog
  Flame of Battlefield, article drift). coin +1000.
- idx 2209: Immortal One Karl Steiner, 3-star, Offense + Electricity
  (012); no level shown. coin +1000.
- idx 2232: The Frost Witch Octavia splash, Lv.1, 3-star (028);
  Recruited banner cropped, mid-transition frame of idx 2226.

### Transcendence splashes with name+level+full stats but no stars
- idx 2212: Thunder Arrow Diana, Lv.MAX (031): Strength 52412 -> 60465;
  Attack 1021 -> 1123; Defense 689 -> 757; Life 1521 -> 1673.
  Successfully transcended. Post value 60465 = idx 2214 abyss slot.
- idx 2227: Immortal One Karl Steiner, Lv.MAX (012): Strength
  47530 -> 54811; Attack 901 -> 991; Defense 689 -> 757;
  Life 1750 -> 1925. Successfully transcended.
- idx 2219: Elite Messenger Hermes setup (023), Lv.MAX; fodder 3x Hermes
  Lv.1 6702 (1/1 selected); blue orb 83/9; blue shards 35/90 (red,
  insufficient); Transcendence 9000 coins; wallet 37278. Verbatim:
  Only hunters above 3-star can be used as fodder. The Hunter that
  participated in the Transcendence will be disappeared.
- idx 2206/2208: Train Teammate Thunder Arrow Diana (031), Strength
  33150 -> 37226 (+4076, ~35 min apart); 5 hollow -> 5 filled
  light-blue diamond pips (visually observed); Master Hunter badge;
  no level shown.

### Ruins-found panels with name+stars but no level/stats
- idx 2220: Elite Messenger Hermes, 3-star badge; Time Left Until
  Closing 00:59:44 (pairs idx 2219 setup).
- idx 2230: The Frost Witch Octavia, 3-star badge; Time Left Until
  Closing 00:59:52 (pairs idx 2226 recruit).

## Cross-batch pairing notes

- Marcien trail: account profile idx 2201 (League Points 2251/3, Level
  69, Team Strength 183978, registered 2017.5.3) matches Marcien rank 1
  at 2251 on the Sept-7 board (idx 2205, viewer = Marcien, My Rank).
- Arena boards: idx 2205 (Sept 7, leader 2251, ranks 1-5) -> Sept-10
  scroll seq idx 2233-2242 (ranks 1-50 continuous, Yang0123 session,
  My Rank 18/2358, leader 2641). Shared names: HoZhihui, Jrad,
  Afterglow, Calamity, Pardis/Pardis (spelling variant within the week).
- BlackGeneral bout pair: idx 2215 (TIME LEFT 61.38, vs Kong) /
  idx 2216 (23.78, vs Kwang); BlackGeneral posts the Octavia-dungeon
  rant on the board (idx 2236, lv55).
- Necromon trail: triple-defeat opponent at idx 2231 (Rank 30/2264,
  -9/-13/-14 across 09.10 10:42-11:36) sits at rank 35/2237 in the
  same-session board (idx 2239).
- Kyzyll trail: excavation helper entry 53061 (idx 2222) = board rank 28
  at 2267 (idx 2238). Lgtmagician: idx 2202 chatter = helper entry.
- Transcend-then-clear: Diana transcend idx 2212 (60465) clears
  Cryogenic Abys 4/4 at idx 2214, following the 3/4 run at idx 2211
  (Lv.22 39404 Diana slot, rupee 80 -> 140).
- Hermes arc: transcend setup idx 2219 -> found Hermes ruins idx 2220
  (00:59:44).
- Octavia arc: recruit idx 2226 -> found Octavia ruins idx 2230
  (00:59:52); splash-frame pair idx 2226/2232.
- Maintenance pair: idx 2210 (000:00:00) / idx 2218 (000:38:48).
- Ruins-board pair: idx 2245 (fuel 7/60, Magicca 00:38:22) /
  idx 2246 (fuel 3/60, Magicca 00:05:39, Okabe Deep Abyss 00:18:43).
- Dupe pairs: Lv.1 2389 x2 (idx 2248 Build Team), Lv.1 6171 x2
  (idx 2250 Hunter List).
- Electricity arc: Karl (idx 2209/2225) extends the batch-41
  Karl/Akasha client-Electricity-vs-catalog-Lightning note.
- Octavia article arc: The Frost Witch (idx 2226/2230/2232) extends
  batch-41 idx 2044. Athena article drift is new this batch.
- Marcien discord-link chat trail across idx 2234/2236/2238/2239/2240
  (bit.ly/BlustoneDisco... -> There's a link there. -> type that link.
  -> case sensitive. x2).

## Most valuable economy/mechanic readings

- Defensive-team accounting (idx 2231): Lv.8 37324 + Lv.MAX 52099 +
  Lv.MAX 45709 + Lv.MAX 54201 = Team Strength 189333 exactly (verified
  sum); defeat log shows League Points -9/-13/-14 with Revenge buttons.
- Transcendence costs (idx 2219): 9000 coins + blue orb 83/9 + blue
  shards 35/90; fodder rule verbatim (above 3-star only, fodder
  disappears). Stat deltas: Diana +8033 Strength (+15.3%), Karl +7281
  (+15.3%); Attack ~+10%, Defense ~+10%, Life +10% on both.
- Ornithopter fuel price (idx 2223): 60 fuel = 5000 rupees or 1 coupon;
  Current 13/60 with 07:12 timer; Daily Purchase 7/11; Veteran Expert 2.
- Abyss economy (idx 2211/2214): 3/4 clear pays +80 rupees, 4/4 pays
  +140; Team Level 62 -> 70; portrait-frame items x1 per slot shown.
- Excavation helper (idx 2222): borrow-a-friend-hunter picker with 12
  entries (Kyzyll 53061 down to Lgtmagician Lv.MAX, strengths cut);
  Entrance failed. toast over Begin Battle.
- Ruins gating (idx 2245/2246): SECRET! boards first-10-hunters only
  with named Discoverer (Magicca, Okabe) and 0day ~5-38 min closers;
  open boards day-gated (Shelte 5-6day, Highland 13day).
- SIC LIST (idx 2245/2246): Cryogenic Abys (missing s) on result,
  board, and SECRET! card vs correct Cryogenic Abyss on the Deep card
  same screen; Giant's Shelte (missing r); The heart of the North
  Highland (lowercase h).
- Assignment states (idx 2224/2247/2249/2250): Exploring / Defending /
  Locked ladders; roster caps 33/42, 31/33, 17/36, 32/45, 39/45, 34/45,
  31/51 (cap varies by account: 33/36/42/45/51).
- Arena HUDs (idx 2207/2215/2216): TIME LEFT 11.11 / 61.38 / 23.78;
  damage ticks 20/11/20/20, 8s, 73/73/73/24; 3-red-1-grey kill pips.
- Expedition HUDs (idx 2217/2221/2244): fuel 3, coins 30/20/60,
  WAVE 4/4; enemy 7689, 47342 x2 (fire), 97387 x4 (ice, 158-crit x4);
  skill counters 4/4/1; ULTRA!!! gauge; SyanL fuel chat.
- Post Office (idx 2228): Clara + eagle postman; mail/chat/leave
  options; Clara = catalog 089 (dialogue name only).
- Date/version anchors: registration 2017.5.3; 09.10 10:42/11:21/11:36
  defeat stamps; 07:12 fuel timer; rupee wallet 37278 (idx 2219),
  34890 (idx 2223).

## Non-ASCII names (verbatim, for searchability)

- idx 2205: Marcien; HoZhihui; Pardis; Afterglow; Jrad.
- idx 2202: Lgtmagician. idx 2215: BlackCarry; Kong.
- idx 2207: Mingisa. idx 2216: Kwang. idx 2217: SyanL.
- idx 2222: Kyzyll; Shinobit; Uryu; Camelot; Zedd; Spondyl; Setzer;
  SeiTruth; Agent_707; Nexor; IceBlade; Lgtmagician.
- idx 2231: Calamity; Necromon. idx 2233: Castrato (Korean-script
  rendering); Kong; Trigg; Zawraith. idx 2234: Calamity; Vexus;
  Doransu; HoZhihui; Sylvester; Marcien. idx 2235: Noi; Jrad;
  Afterglow; Enheim. idx 2236: BlackGeneral; Yang0123; Enheim;
  Mingisa. idx 2237: Pardis. idx 2238: Alaiko; Premonition; Kyzyll;
  GrimrozKilborne; Marcien. idx 2239: Smn42; Jenin; Necromon; Marcien.
  idx 2240: Vitor; Shyden; Marcien. idx 2241: Jariya; zapkhiel.
  idx 2242: Naxus; Zhim. idx 2249: Memelord-420; Cyana.
- idx 2245/2246: Magicca; Okabe.
- Full Hangul forms are in batch-45.tsv rows 2233-2242 (medium
  confidence, read visually).

## Contaminants

- None in this batch (all 50 frames are in-game English-client screens;
  no browser shots, store pages, or OS prompts).
- Same-session pairs (not same-frame): idx 2206/2208 (Diana Train),
  idx 2210/2218 (maintenance), idx 2215/2216 (arena bout),
  idx 2226/2232 (recruit splash frames), idx 2245/2246 (ruins board).
- Scroll seq: idx 2233-2242 (10-frame Top-1000 ladder, 12:09:24-56).
- Cropped screenshot: idx 2224 (953x1350 assignment grid).
