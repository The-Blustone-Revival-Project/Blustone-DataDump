# Batch 38 hits (idx 1851-1900)

Lane: `findings/hunters/base-stats-visual-hunt/manual-scrapes-2026-10-14/`
Crops: none (0 HITs).
Zooms (lane folder, provenance only): `z1852_header`, `z1852_name`,
`z1861_header`, `z1894_header`, `z1894_name`, `z1866_bottom`,
`z1882_bottom`, `z1853_rows`, `z1858_rows`, `z1892_rows`, `z1893_rows`,
`z1885_plates`, `z1885_plates2`.
OCR (lane folder): `_tmp38_ocr/` (50 files, tesseract `--tessdata-dir`
`%TEMP%/opencode/tessdata`, `-l eng`; binary capture + UTF-8 decode).

## HITs: 0/50

No frame in this batch shows named hero + level + star rank + HP/ATK/DEF
or Strength together. No level ribbon appears anywhere in the batch, so
every stat-bearing hero frame below is hit=no per bar rules.

## Near-hits (full numbers, hit=no per bar rules)

### idx 1852: Walking Disaster Nene Train panel, level unshown (catalog 003)
- File: `Screenshot_20170628-031422-5c0aadd2d96512b6.png` (1080x1920).
  Title fragment "Walking Disaster" zoom-verified (`z1852_name`);
  Defense + Ice icons; Strength 3062x (5th digit occluded by home icon,
  zoom-verified `z1852_header`, never invented); Master Hunter 5-star
  badge; 5 empty diamond slots; Life 1785 / Attack 769 / Defense 926 /
  Attack Speed 7; Critical Damage Chance 14 / Critical Damage 206 /
  Armor Penetration 0; Block Chance 33 / Block Resistance 50 /
  Strengthen Elemental Attributes 0 / Elemental Attack Resistance 0 /
  Life Regeneration 45.
- Identity via zoom-verified title + bear-ear art matching the Nene
  recruit splash (idx 1890) and unnamed 5-star splash (idx 1883).
  Role Defense + Ice match catalog 003 exactly.
- Hit=no (no level).

### idx 1861: Proficient Hunter Train panel, level unshown, name obscured
- File: `Screenshot_20170701-095517-0c15c580b2308c25.png` (540x1110,
  downscaled source). Proficient Hunter 4-star badge; Strength 1286x
  (5th digit occluded, zoom-verified `z1861_header`); 1 filled + 4 empty
  diamonds; Life 1071 / Attack 530 / Defense 717 / Attack Speed 7;
  crit 13 / 206 / 0; block 31 / res 50 / strengthen 4 / elem-res 4 /
  regen 24.
- Role/element icons not legible, so catalog blank. Hit=no (no level).

### idx 1867: Immortal One Karl Steiner Train panel, level unshown (catalog 012)
- File: `Screenshot_20170702-212117-2143a2cd807726e9.png` (1080x1920).
  Offense + Electricity icons; Strength 39184; Master Hunter 5-star
  badge; 5 filled diamonds; Train / Skill Training / Upgrade Equipment
  / Story; no level ribbon.
- ELEMENT NOTE: client "Electricity" vs catalog 012 "Lightning"
  (extends the batch-29/30/32/34 Electricity arc).
- Chains to idx 1868/1869 skills (Karl chain) and idx 1870/1871
  scrolled Train (same 39184). Hit=no (no level).

### idx 1870/1871: Karl Steiner scrolled Train pair, level unshown (catalog 012)
- Files: `Screenshot_20170702-212446-8e6de9961fb50982.png` /
  `Screenshot_20170702-212446-eddb1db55a0b5a39.png` (both 1080x1920,
  same timestamp = same-frame pair). Strength 3918x (last digits cut by
  home icon, never invented); Life 2056 / Attack 1124 / Defense 852 /
  Attack Speed 7; crit 33 / 211 / 0; block 14 / 50 / strengthen 0 /
  elem-res 0 / regen 41; 5 filled diamonds.
- Hit=no (no level).

### idx 1894/1895: Karl Steiner scrolled Train pair, level unshown (catalog 012)
- Files: `Screenshot_20170712-113934-2689b5427dcfd01a.png` /
  `Screenshot_20170712-115218-851fb6771ea9b83b.png` (both 1080x1920,
  same timestamp = same-frame pair). Title "Immortal One ...arl
  St...ner" zoom-verified (`z1894_name`); Strength 4156x (last digit
  cut, zoom-verified `z1894_header`); Life 2127 / Attack 1174 /
  Defense 885 / Attack Speed 7; crit 33 / 212 / 0; block 14 / 50 / 0 /
  0 / regen 41; 5 filled diamonds.
- Hit=no (no level). Same stat shape as idx 1870/1871 at higher
  Strength (4156x vs 3918x cut).

### Recruit splashes with name+title+stars but no level (hit=no)
- idx 1855: Maiden of Gods Akasha, 3-star (catalog 008); Lottery Mouse
  recruit text; Apply to Recruit (1 scroll); wallet gems 0 / scrolls 16.
- idx 1862: Athena, 3-star, Defense + Fire (catalog 027 via unique name
  + role/element; title unshown); coin +1000.
- idx 1878: Immortal One Karl Steiner, 3-star, sword Class icon +
  Offense Electricity labels (catalog 012; 3-star recruit state vs
  5-star trained state idx 1867/1870).
- idx 1890: Walking Disaster Nene, 3-star, Defense + Ice (catalog 003;
  title+role+element exact); coin +1000.
- idx 1891: Elite Messenger Hermes, 3-star (catalog 023); coin +1000.
- idx 1873: unnamed 5-star red-haired spear-woman splash (possibly
  Octavia per Frozen Chest context, never claimed); catalog blank.
- idx 1883: unnamed 5-star splash whose art matches Nene (bear ears,
  goggles, orange scarf) but name unshown; catalog blank.

## Cross-batch pairing notes

- Nene arc: idx 1852 Train (5-star, Strength 3062x cut, title
  zoom-verified) -> idx 1890 recruit splash (3-star, 003 exact) ->
  idx 1883 unnamed 5-star splash (art match, catalog blank).
- Karl arc: idx 1866 roster (39184) -> idx 1867 Train (Strength 39184,
  5 filled diamonds) -> idx 1868/1869 skills (shared 462/5 + 21/6
  stacks, fee 1000, wallet 118259) -> idx 1870/1871 scrolled Train
  (3918x cut) -> idx 1872 defensive team (39184, Team Strength 111383)
  -> idx 1878 recruit splash (3-star) -> idx 1894/1895 scrolled Train
  (4156x cut, 2127 / 1174 / 885).
- Octavia Frozen Chest arc: idx 1859 supply-office rewards (2x ticket,
  scroll, Octavia trace card, 2000 coins) -> idx 1860 chest contents
  (Octavia's Traces 1, 2 lottery tickets, fuel, evaluation, challenge
  invite, 2,000 rupees) -> idx 1900 event page (160 Manda / 15,000
  rupees per chest; 159,600 banked).
- Rupee-shop pair: idx 1879 (219545 holdings, 4/12) -> idx 1884
  (256642 holdings, 12/12 capped), both Veteran Expert 1.
- Rank Boards pair: idx 1864 -> idx 1865 (~4.5h later, VanLaser #1
  at 5066, up from 4930).
- Same-frame pairs: idx 1870/1871 (Karl Train); idx 1894/1895
  (Karl Train); idx 1887/1888/1889 (transcendence scroll seq,
  headed by partial-load idx 1886).
- Mowgli spelling arc: sell-trace "Mowgli's Trace" (idx 1893)
  extends the batch-34 client "Mowgli" (vs catalog 002 "Mowgli").
- TylTyl casing arc: "TylTyl's Trace" sell row (idx 1893) vs shop
  "TylTyl's" (batch-34 idx 1690) vs catalog 004 "Tyltyl".
- HoZhihui trail: Rank Boards plate idx 1864 (extends batch-34
  idx 1682 chat + idx 1864 here).
- Vexus pin: idx 1872 defensive log (Defeat, "boop") extends the
  batch-34 Vexus story/chat arc.
- v1.0.7.0 (idx 1896) explains idx 1898: daily assignments replace
  "Living the Hunter Life".

## Most valuable economy/mechanic readings

- Transcendence rules verbatim (idx 1887): fuse two same-hunter same-
  grade; once at 3-star, twice at 4-star, thrice at 5-star; 1 + 2 + 3
  hunters per tier (+ additional material each tier); 6 of the same
  hunter total for 3rd transcendence.
- v1.0.7.0 Patch Notes (idx 1896): daily fuel 30 -> 45; dorm max
  57 -> 72; expedition/fight-club progress shown in town; building
  names; story skip; mail from player info page; ad rewards; forum
  Events tab; last-area shortcut; combat points on results; inventory;
  manage-hunter; chat rooms; daily assignments replace Living the
  Hunter Life. Fixes: call black-screen, auto-combat fuel glitch
  (+3rd line cut: abnormal experience...).
- Skill-training ladder (idx 1868/1869): Lv.46/50 Damage
  13.80% -> 14.10% (+0.30pp), Lv.45/50 Crit Chance 13.50% -> 13.80%
  (+0.30pp); shared 462/5 + 21/6 (+ 4/4) stacks, fee 1000, wallet
  118259. Plus idx 1856: Lv.40/40 Supporting Gunman Damage
  8.00% -> 8.20% (+0.20pp), 357/5 stack, fee 900, wallet 50115.
- Nene attribute block (idx 1852): 1785 / 769 / 926 / AS 7; crit
  14 / 206 / 0; block 33 / 50 / 0 / 0 / regen 45; Strength 3062x cut.
- Karl attribute blocks: 2056 / 1124 / 852 / AS 7 (idx 1870/1871,
  Strength 3918x cut); 2127 / 1174 / 885 / AS 7 (idx 1894/1895,
  Strength 4156x cut); shared crit 33 / ~211-212 / 0 and block
  14 / 50 / 0 / 0 / regen 41.
- Bomber trace board (idx 1892): Bomber 6/6, Attack Bonus
  6.0% -> 7.0%; Lantern 70/80, Levi 37/40, Teddy Bomber 0/40
  (Items Collected) vs over-collected Metis 70/20, Locke 55/20,
  Sienna 84/20.
- Sell-trace price list (idx 1893): wallet 221746; Mowgli 12 @100;
  Sienna 90 / Bruce Bang 89 / Hecate 40 / Sylvester 296 / Robin 69
  @20; TylTyl 5 / Locke 55 / Metis 80 (prices cut, pattern 20).
- Frozen Chest economy (idx 1900): Chest of the Void per 160 Manda;
  Frozen Chest per 15,000 rupees; banked 0/160 Manda, 159,600/15,000
  rupees (= 10.6 chests).
- Rupee shops (idx 1879/1884): holdings 219545 -> 256642; Veteran
  Expert 1; Daily Purchase 4/12 -> 12/12 capped; x5000 + Manda-10
  options; wallet gems 0 / tickets 0 both.
- Fuel ladder (idx 1881): 08:00-12:00 x30 (+Manda 1 claimable) /
  12:00-16:00 / 16:00-20:00 / 20:00-24:00 all Received; next supply
  in 11:38:05. Plus idx 1880: Dawdly's "suprise visit" (sic) fuel x240.
- Assignments board (idx 1898): Recruit Hunters 0/2 (fuel x30);
  Train Skills Complete w/ Korean flavor (scroll x1); Buy Items 0/3
  (blue ore x10, Receivable); Challenge x3 attempts (coins x1000);
  Veteran Expert 1, 1310/2560.
- Fight Club (idx 1875): rotation 00:02:51; tickets 0/6; own specs
  112575 vs 파란하늘하얀달 147075 (Rank 376) and 신핵구 70239
  (Rank 383), messages verbatim. Defense logs: Team Strength
  111383 (idx 1872) and 131608 (idx 1899); revenge-pending defeats
  incl. Korean "ㅋ" message.
- Roster bands: 39.1K/35.4K top (idx 1866) down to 1.0K rookies
  (idx 1858: 1099s/1094s/1092s/1080s); 26/42, 37/42, 38/39, 39/39
  list counts.
- Title/element/spelling notes: client "Electricity" vs catalog
  "Lightning" (Karl 012, idx 1867/1878); client "Mowgli" vs catalog
  "Mowgli" (002); "TylTyl's" vs catalog "Tyltyl" (004); title-art
  "Octavia`s" (backtick, idx 1900) vs "Octavia's" body text;
  sic list: "suprise" (1880), "dosaljang" romanization (1897).
- Date/version anchors: v1.0.7.0 patch (93% 11:56 AM, idx 1896);
  Jul 02 16:15/20:48 boards; 07.02 18:58 + 07.12 logs; 02:09
  translate stamp.

## Non-ASCII names (verbatim, for searchability)

- idx 1852/1890: Nene. idx 1855: Akasha. idx 1862: Athena.
  idx 1867-1871/1878/1894/1895: Karl Steiner. idx 1891: Hermes.
  idx 1892: Lantern; Levi; Teddy Bomber; Metis; Locke; Sienna.
  idx 1893: Mowgli; Sienna; Bruce Bang; Hecate; Sylvester; Robin;
  TylTyl; Locke; Metis.
- idx 1859/1860/1900: Octavia (`Octavia`s` title art at idx 1900).
  idx 1864/1865: Vitor; 호삼량; HoZhihui; xSephirothx; VanLaser;
  크툴루; 재프. idx 1872: Vexus. idx 1875: 파란하늘하얀달; 신핵구.
  idx 1880: Dawdly. idx 1885: Asu; Alexin; limit; Norin.
  idx 1897: 도살장; dosaljang. idx 1898: 하루 세 번,
  특기 훈련도 잊지 말게. idx 1899: KAJEKIRITO; ㅋ; Rozare-Kun.

## Contaminants

- idx 1851/1874/1876/1877: Fate/Grand Order captures
  (game-external: battle HUD, party setup, support setup; Tamamo Cat,
  Saber Lily, Heracles, Altria, Elisabeth, Jeanne; lower provenance).
- idx 1854: phone-browser capture (Delphi Technology, Princeton NJ;
  zero game digits; lower provenance).
- idx 1897: Google Translate capture (Korean dosaljang; zero game
  digits; lower provenance).
- idx 1870/1871, idx 1894/1895: same-frame duplicate Train pairs
  (kept as pair anchors).
- idx 1886-1889: same-article scroll seq (idx 1886 partial load;
  idx 1887/1888/1889 full-text duplicates).
