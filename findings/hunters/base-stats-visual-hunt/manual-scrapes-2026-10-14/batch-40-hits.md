# Batch 40 hits (idx 1951-2000)

Lane: `findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/`
Crops: none (0 HITs).
Zooms (lane folder, provenance only): `z1961_header`, `z1961_title`,
`z1961_top`, `z1962_title`, `z1962_top`, `z1968_header`, `z1968_title`,
`z1968_top`, `z1966_panel`, `z1966_items`, `z1985_level`, `z1995_mat`,
`z1952_rows`, `z1954_grid`, `z1977_rows`, `z1988_rows`, `z1989_rows`,
`z1992_rows`, `z1953_top`, `z1963_top`, `z1965_bottom`.
OCR (lane folder): `_tmp40_ocr/` (50 files, tesseract `--tessdata-dir`
`%TEMP%/opencode/tessdata`, `-l eng`; binary capture + UTF-8 decode).

## HITs: 0/50

No frame in this batch shows named hero + level + star rank + HP/ATK/DEF
or Strength together. No level ribbon appears anywhere in the batch, so
every stat-bearing hero frame below is hit=no per bar rules.

## Near-hits (full numbers, hit=no per bar rules)

### idx 1961: Walking Disaster Nene Train panel, level unshown (catalog 003)
- File: `Screenshot_20170731-122922-68d95ee287193bc7.png` (1080x1920).
  Title "Walking Disaster" + name "Nene" (behind badge) zoom-verified
  (`z1961_title`, `z1961_top`); Experienced Hunter 3-star badge;
  Strength header digits occluded by home icon (zoom-verified
  `z1961_top`, lead 81 visible, tail cut, never invented); Advance
  button; Life 483 / Attack 297 / Defense 354 / Attack Speed 7;
  crit 12 / 200 / 0; block 29 / 50 / strengthen 0 / elem-res 0 /
  regen 16.
- Hit=no (no level).

### idx 1962: Athena Train panel, level unshown, name shaded (catalog 027)
- File: `Screenshot_20170731-123001-5d1f3c5c348f9177.png` (1080x1920).
  Name fragment "Athena" zoom-verified (`z1962_top`) under a Media
  volume shade; client title "Flame of the Battlefield ..." vs catalog
  027 "Flame of Battlefield" (the-discrepancy); Experienced Hunter
  3-star; Fire icon; Advance button (max-advance state); 5 filled
  light-blue diamonds; Life 570 / Attack 336 / Defense 461 /
  Attack Speed 7 (zoom-verified); crit 12 / 200 / 0; block 29 / 50 /
  strengthen 3 / elem-res 3 / regen 15 (OCR-verified).
- Hit=no (no level).

### idx 1968: Steely Bodyguard Kain Train panel, level unshown (catalog 029)
- File: `Screenshot_20170801-012916-bfb027092b94c972.png` (1080x1920).
  Title + "...ain" zoom-verified (`z1968_title`, `z1968_top`);
  Experienced Hunter 3-star; Defense + Electricity icons; Strength
  header occluded by home icon (zoom-verified `z1968_top`, lead 81
  visible, tail cut, never invented); Life 483 / Attack 278 /
  Defense 374 / Attack Speed 7 (zoom-verified); crit 12 / 205 / 0;
  block 29 / 50 / strengthen 5 / elem-res 5 / regen 15.
- ELEMENT NOTE: client "Electricity" vs catalog 029 "Lightning"
  (extends the batch-29/30/32/34/38 Electricity arc).
- Hit=no (no level).

### idx 1969: Steely Bodyguard Kain 4-star Train panel, level unshown (catalog 029)
- File: `Screenshot_20170801-130130-a864fe4bb257fe4f.png` (720x1280,
  downscaled source). Defense + Electricity; Proficient Hunter 4-star
  (green badge); Strength 14472; Train / Skill Training buttons;
  attribute block below cut.
- 4-star trained state vs 3-star recruit state (idx 1984 broadcast:
  Ariaen -> Kain). Hit=no (no level).

### Recruit splashes with name+title+stars but no level (hit=no)
- idx 1975 / idx 1986: First Ever Hunter Lantern, 3-star, Bomber +
  Fire (catalog 001 exact); coins +1000 each (duplicate-art pair).
- idx 1979: Flame of the Battlefield Athena recruit-request, 3-star
  (catalog 027, client the-wording); wallet gems 54 / scrolls 5;
  Apply to Recruit (1 scroll); Request for Trace Collection 1.
- idx 1987: Flame of the Battlefield Athena, 3-star, Defense + Fire
  (catalog 027); coins +1000. Pairs idx 1979 request -> 1987 result.
- idx 1980: Maiden of Gods Akasha, 3-star, Support + Electricity
  (catalog 008; Electricity vs catalog Lightning); coins +1000.
- idx 1981 / idx 1982: Elite Messenger Hermes, 3-star, Offense +
  Fire (catalog 023); coins +1000; same-frame duplicate pair
  (same timestamp, different hash).
- idx 1974: Biologist Acerola 7/40 Items Collected (tiny 655x668
  trace-board crop; catalog 030 via unique name+title).

### Advancement before->after with stars but no identity/level (hit=no)
- idx 1995: Advancement Match 3-star -> 4-star; Power Upgraded
  6685 -> 10469 (zoom-verified `z1995_mat`); wallet 381665;
  materials 5175 / 5175 / 7029 (zoom-verified) + bottom row cut;
  fee Level-Up Advancement 12000; spent-hunter dormitory warning
  verbatim.

## Cross-batch pairing notes

- Kain chain: idx 1965 trace board (Steely Bodyguard Kain 0/0
  Recruit) -> idx 1967 skill (Steely Bodyguard Lv.1/30, Kain flavor
  text) -> idx 1966 skill (Iron Fortress Lv.1/30, shared 1093/1
  stack, fee 100, wallet 279856) -> idx 1968 Train (3-star,
  483 / 278 / 374) -> idx 1969 Train (4-star, Strength 14472) ->
  idx 1984 broadcast (Ariaen recruits Kain).
- Nene arc: idx 1961 Train (3-star, 483 / 297 / 354) + idx 1965
  trace (Nene 35/80) + idx 1971 balance notice (Nene 5th skill
  20% regen -> 20% total life) + idx 1983 broadcasts (Searing and
  VSpang recruit Nene).
- Athena arc: idx 1962 Train (3-star Advance state,
  570 / 336 / 461) -> idx 1965 trace (Athena 17/80) -> idx 1979
  recruit request (5 scrolls) -> idx 1987 recruit splash ->
  idx 1983 broadcasts (Fixerdin and VSpang recruit Athena).
- Rank-board pair: idx 1951 -> idx 1956 (same five names; Trigg
  takes My Rank 2534, Majo drops 2632 -> 2513).
- Fight-club seq: idx 1957 -> idx 1958 (Majo vs HoZhihui,
  16.04 -> 0.86, damage resolves 10/10/5 vs 12/20/20).
- Same-frame pairs: idx 1981/1982 (Hermes recruit).
- Moogle/Moogle trail: idx 1984 chat ("Moogle ... I know DAT
  feeling") -> idx 1985 profile (client "Moogle", Level 51).
- Story run: idx 1994 Hermes Midgard monologue -> idx 1996-2000
  Octavia/Kain 5-frame exchange.
- Electricity wording arc: idx 1968 Kain + idx 1980 Akasha
  (client "Electricity" vs catalog "Lightning" 029/008).
- Athena the-wording arc: client "Flame of the Battlefield"
  (idx 1962/1965/1979/1987) vs catalog 027 "Flame of Battlefield".
- dosaljang trail: idx 1951/1953/1956 here (rank + Victory!
  screen) extends the batch-38 translate/Chest context.

## Most valuable economy/mechanic readings

- Skill-training ladders, Lv.1/30 base tier (idx 1966/1967): Iron
  Fortress ("The defender must have a high defense in order to
  protect the team.") and Steely Bodyguard ("Kain's body is built
  to protect others through countless trainings and battles."),
  both Defense 0.30% -> 0.60% (+0.30pp), shared blue-orb stack
  1093/1, fee 100, wallet 279856. Zoom `z1966_panel`/`z1966_items`
  overrules tesseract ("7/30", "1093/7") on both counts.
  Plus idx 1970: Lv.50/50 Instinctive Attack ("The offense needs
  to attack enemies with incredible precision."), Damage 15.00%
  maxed, wallet 96112.
- Advancement pricing (idx 1995): 3-star -> 4-star, Power
  6685 -> 10469 (+3784, +56.6%), fee 12000, wallet 381665;
  twin-chibi material art; spent hunter leaves dormitory.
- Event economy (idx 1976): "Karl Steiner and Akasha
  Disappeared?!" / Electric Abyss; 21:18:16 remaining; Set's
  Feathers 17 / total 2337 / My Rank 5; 40 feathers -> 4 Karl
  Steiner's Trace or 5 Akasha's Trace (Karl 25% dearer).
- Trace board (idx 1965): Defense 6/7, Defense Bonus 6.0% ->
  7.0%; over-collected Riko 163/40, Gerard 144/40, Hecate 45/20
  (all Recruit-ready) vs Nene 35/80, Athena 17/80, Kain 0/0.
- Nene/Athena/Kain attribute blocks: Nene 483 / 297 / 354 /
  AS 7 (crit 12 / 200 / 0; block 29 / 50 / 0 / 0 / regen 16);
  Athena 570 / 336 / 461 / AS 7 (crit 12 / 200 / 0; block
  29 / 50 / 3 / 3 / regen 15); Kain 483 / 278 / 374 / AS 7
  (crit 12 / 205 / 0; block 29 / 50 / 5 / 5 / regen 15).
- Balance notice (idx 1971): all helpers base stats up, combat
  points +about 7%; Nene 5th skill 20% regen -> 20% total life;
  Captain separate-rules explainer.
- Auto-combat debug overlay (idx 1990): Android 7.0 Moto G (4);
  AppID com.vshower.prd_sr; Engine Peppermint_170712_1930;
  Locale es_MX; 1080x1798; per-battle loot (x134+x1 down to
  scroll+trace drops); All Battles Completed In 00:21:36
  (OCR-verified); Finish Now 22.
- Roster bands: 45.0K/42.1K/40.8K top (idx 1952, 35/39) and
  44.4K/42.9K/41.7K (idx 1988, 42/45) and 44.2K/41.3K/40.2K
  (idx 1989, 51/66, garbled) down to 1.0K rookies (idx 1954:
  1244/1094s) and mid ladder 17.6K-3.2K (idx 1992, 32/42,
  locks on 6912/5175); 57/72 board (idx 1977, Ibuki chat).
- Fight-club mechanics: Mandarin Tier Ready-to-Battle
  (idx 1993: 4/6 tickets, Ally 4 MAX vs 3 + ? slot, barbogyu,
  1-ticket entry); battle damage pairs (idx 1958: 10/10/5 vs
  12/20/20; idx 1978: 180/180 at 89.52).
- Village state (idx 1963): fuel 13/60, mail 0/6, 360/360,
  Trigg, Limited + EVENT boards, Supplies button.
- Title/element/spelling notes: client "Electricity" vs catalog
  "Lightning" (Kain 029, Akasha 008); client "Flame of the
  Battlefield" vs catalog "Flame of Battlefield" (Athena 027);
  profile "Moogle" vs chat "Moogle"; "Flame of the
  Battlefield" shade-occluded fragment (idx 1962); sic list:
  "July 21th/31th" (idx 1973).
- Date/version anchors: profile Version 1051 + Registration
  06/03/2017 (idx 1985); Discord Aug 1 / Aug 10 2017
  (idx 1991); Community Star Jul 21-31 window (idx 1973);
  KST-timestamped filenames Jul 29 - Aug 12 2017; Spanish
  crash dialog (idx 1960, es locale corroborates idx 1990
  es_MX).

## Non-ASCII names (verbatim, for searchability)

- idx 1951/1953/1956: Majo; kasutorato; Trigg; kwang;
  dosaljang. idx 1955: HoZhihui; Zedd. idx 1957/1958/1978:
  HoZhihui. idx 1959/1978: Trigg. idx 1961: Nene.
  idx 1962/1979/1987: Athena. idx 1968/1969: Kain.
  idx 1974: Acerola. idx 1975/1986: Lantern. idx 1976: Karl
  Steiner; Akasha; Set (Set's Feathers). idx 1980: Akasha.
  idx 1981/1982: Hermes. idx 1983: IceBlade; Searing;
  Tsuyoshi; Fixerdin; VSpang; Kiandel; Rozare-Kun. idx 1984:
  Ariaen; Silverberg; Moogle. idx 1985: Moogle. idx 1993:
  barbogyu. idx 1977: Ibuki.

## Contaminants

- idx 1960: phone home screen + Spanish Blustone crash dialog
  (Blustone-related OS UI, zero game digits).
- idx 1971/1972: phone-browser captures (balance-modifications
  notice with real mechanic value; event-results page).
- idx 1973: Facebook VisualShower promo post (Community Star
  results, sic date suffixes).
- idx 1991: Discord #slots capture (Tatsumaki BOT, game-external).
- idx 1981/1982: same-frame duplicate Hermes pair (kept as
  pair anchors).
- idx 1989: heavy text-garble render artifact (top rows
  medium-confidence).
- idx 1953: motion-blurred Victory! frame (wallet illegible,
  never invented).
