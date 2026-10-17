# Stat-panel hunt — 2026-10-11

> **2026-10-17:** the raw media (`frames/`, `dl/`, `bahamut/`, `hits/` —
> ~3.9 GB) moved to private preservation storage `local/findings-media/`; only
> text findings (this REPORT, frame results, search log, OCR table, tools)
> remain in the repository.

Lane: `stat-panel-hunt-2026-10-11`. Goal: in-game STAT PANELS (card-detail
HP/ATK/DEF/Strength, equipment screens, hunter lists, monster panels) usable as
ledger anchors, especially for 4-star heroes. Positive control first; every hit
frame preserved in `hits/` with URL+timestamp; no value claimed without image.

## Positive control

`_tools/control.py` renders a synthetic equipment panel
(Strength 24068 +6291, HP 2879, ATK 1471, DEF 1149, etc.) and OCRs it with the
exact tesseract pipeline (`jpn+kor+eng`, `--tessdata-dir .../opencode/tessdata`).
Result 2026-10-11: **PASS 8/8 numerals recovered**. OCR batches below are
trusted only under this control. Caveat: control uses clean rendered type;
stylized in-game Korean/Japanese fonts at video resolution OCR poorly, so all
video verdicts below rest on direct visual sampling PLUS the OCR sweep, not OCR
alone.

## YouTube

Search log: `search-log.tsv`. Exact-vocab KR/JP/CN/EN queries; most returned
unrelated games (game is obscure). Downloaded ≤720p, ffmpeg-extracted, OCR-swept
(`frame-results.tsv`), visually sampled.

| Video | Content | Verdict |
|---|---|---|
| 펩시 `3CFyJ7FBWb8` 블루스톤 파이트클럽 (576s, 575 frames @1fps) | Fight Club VS screens + battles only | 2 VS frames → `hits/` as POLLUTED team-전투력 (142050/195548, 129441/195548); no HP/ATK/DEF panel |
| 외로이 `lSeElKdgI20` 30-min unedited early play (1815s, 605 frames @1/3fps) | Story (라나/웨스트필드/라니/주인공) + tutorial battles + battle-prep | No stat panel in 12-frame visual sweep; OCR sweep max score 7 (noise) |
| 예호 `sU2gKDjL2dQ` play (1463s, 487 frames @1/3fps) | Tutorial (job intro, recruit, attendance, story) + battles | No stat panel in 6-frame visual sweep; full OCR sweep complete, max score 7 |
| カクテル `RsLterdToT8` JP (418s, 418 frames @1fps) | Gacha/search + fight-club victory + battles | No stat panel in 4-frame visual sweep; full OCR sweep complete (418 frames), no hits |
| `U4WLbs4GoHk` EN/JP play (563s, 188 frames @1/3fps) | **HIT: card-detail panel** 新人ハンター チルチル Lv.1 (catalog 004 Tyltyl) @07:21–07:24 | 2 frames → `hits/` with verbatim JP readings; see Found |
| `U4WLbs4GoHk` (same) surrounding content | Tutorial battle (enemy bar 396, ambiguous current HP) + JP story | Context only |
| 펩시 Short `RG47CcM7c20` 자기극복 (19s, 37 frames @2fps) | Animation only (boxing glove, starfield), no game UI | Negative |
| 1gktnrn `dccrlwrswIc` Naver embed (211s, 212 frames @1fps) | Battles + ruins-124 result screen | Negative |

OCR scoring: stat-token list (HP/ATK/DEF/Strength/체력/공격/방어/전투력/
ステータス/攻撃/体力/防御/战斗力/装备/Lv/MAX/…); hit bar = score ≥ 9 or full
HP+ATK+DEF trio. **Two frames met the bar** (`U4WLbs4GoHk` f00148/f00149,
score 10 — the Chiruchiru panel below); all other videos topped at score 7
(numeral-driven battle-HUD noise).

## Naver 1gktnrn — six posts

Already screened 2026-10-05 (`naver-visual-hunt-2026-10-05.md`); re-verified this
lane. Recruit cards (Bright 049, Therapy 050), Dumble Lv.1 전투력 2183 (gear
ambiguous), unlabeled roster tokens, sticker post, gameplay post. This lane
re-scanned the embedded video `dccrlwrswIc` fully (212 frames): battles only.
No new panels.

## Bahamut — 訓練獵人 (snA=56) + 材料篇 (snA=57)

Both threads fetched full-text via the mobile mirror (desktop 403). All 22
embedded images downloaded from `truth.bahamut.com.tw` (image-host control
green) and OCR-scanned (`bahamut_ocr.tsv`):

- snA=56: full-hunter skill table (all roles × transcendence levels), skill-cost
  table, self-transcendence cost table (1★: 5/50/5000 … 5★: 45/450/45000).
  Economy/skill data, **no hero stat panel**. The skill table is a skill-lane
  lead, not a stat anchor.
- snA=57: 19 material/item icons with JP item names (魚利的金属砕片, 完整的背殻,
  結著果寅的薬草, 新鮮的薬草, 挑戦書 …). **No stat panel.**

## Reddit remainders

- Fluger69 galleries parts 1–3: fully navigated 2026-10-05
  (`reddit-memorial-galleries.md`); identity-only detail/profile screens, no
  numerals. Re-fetch attempted this lane via old.reddit `.json` (bot-wall: 200
  with new-Reddit shell HTML), www.reddit `.json` (403), four redlib instances
  (418/410/429/DNS-fail). **Transport-blocked; NOT a content negative.** Prior
  review stands; blurred/loading part-3 transitions remain unknown.
- Team-comp post `hzkbt3`: page timed out 2026-10-05; JSON likewise bot-walled
  this lane. **Unresolved, transport only.**

## Found

### HIT 1 — card-detail stat panel: チルチル (catalog 004 Tyltyl), Lv.1

- Source: [bluestoneをやった ブルーストーン](https://www.youtube.com/watch?v=U4WLbs4GoHk)
  by iOS&Android Game Play, 563s, uploaded 2018-01-11 (JP client, pre-release era).
- Frames: `hits/U4WLbs4GoHk_f00148.jpg` (t≈441s, header + base values) and
  `hits/U4WLbs4GoHk_f00149.jpg` (t≈444s, scrolled full detail rows), each with a
  `.txt` sidecar carrying URL+timestamp+verbatim reading.
- Verbatim (JP): 最高のシェフ チルチル, 新人ハンター, Lv.1, 1★, 戦闘力 176;
  基本能力値 HP 147 / 攻撃力 147 / 防御力 147 / 攻撃スピード 7;
  攻撃詳細 致命打確率 10 / 致命打ダメージ量 181 / 貫通力 0;
  防御詳細 ブロック確率 10 / ブロックダメージ減少量 42 / 属性強化 0 /
  属性耐性 0 / HP再生力 4.
- Identity: exact title+name+star+role+element match to catalog `004` Tyltyl
  ("World's Best Cook", 1★ Support/Fire), corroborated by the archived official
  JP profile (2019-12-09 capture, level/gear not shown: combat 6664 / HP 1467 /
  ATK 679 / DEF 679 / speed 7 / crit 14 / critdmg 180 / pen 0 / block 14 /
  blockred 42 / elem+ 0 / elemres 0 / regen 37). Shared fields agree exactly
  (speed 7, block-reduction 42, penetration 0).
- Disposition: named Lv.1 full-panel anchor candidate. Gear state NOT
  established (no green equip deltas visible, fresh tutorial account — but that
  is not proof of nude). **No base-stat coverage claimed by this lane**; ledger
  owner adjudicates.

### Polluted track

- 2 Fight Club VS frames (`hits/3CFyJ7FBWb8_*_VS-team-power.jpg` + sidecars):
  team 전투력 totals (142050/195548, 129441/195548), gear/level unknown.
- Otherwise: 0 equipment stat screens, 0 hunter-list stat fields, 0 monster
  panels. Strict counts unchanged.

## Controls / limits

- Positive control PASS 8/8 (above).
- Bahamut image host 200 ×22 (control green).
- Reddit: never recorded bot-wall as content negative.
- OCR limitation: stylized CJK game fonts at ≤720p OCR poorly; verdicts rest on
  visual sampling + OCR agreement. Long videos sampled at 1/3fps (documented
  deviation); short videos at 1–2fps.
- Naver six posts were already opened 2026-10-05 (coverage.md's "unopened" note
  predates that screening); this lane re-verified + fully scanned the embedded
  video.
- Remaining leads (not downloaded): `vXuGNGCMg3Q` 98-min Iczel Part 1,
  `tH-mTRN9zBs` 97-min JP guild, `qJeB64RW3GY` 74-min JP, `GxThPFqGBQk` gacha,
  `lDYqHtDHqbs` early play, Papillon fightclub clips.

## Continuation — 2026-10-11 late lane (remaining-lead sweep)

Control re-run before the new OCR batches: **PASS 8/8** (same synthetic panel,
same `jpn+kor+eng` pipeline). All verdicts below rest on visual sampling PLUS
OCR agreement, not OCR alone.

| Video | Content | Verdict |
|---|---|---|
| いちごみるく `GxThPFqGBQk` 10連ガチャ (69s, 69 frames @1fps) | Fire-event gacha pulls → recruit splash → card-detail panel | **HIT 2** (Akasha Lv.1); 4 frames → `hits/` |
| 껨조TV `lDYqHtDHqbs` 초반부 플레이 (466s, 466 frames @1fps, OCR max 6) | Story dialogue (의문의 남자) + battles + victory (팀 전투력 300) | Negative; no hits |
| Papillon `fipdMIHKscE` 파이트클럽 오류 제보 (141s, 141 frames @1fps, OCR max 6) | Fight Club battles incl PiP second match (HP 4472/6622 etc.) | Negative; no hits |
| Papillon `0w9pGq-vkxQ` 각성방덱깨기 (150s, 149 frames @1fps, OCR max 7) | Fight Club VS + battles | 1 VS frame → `hits/` as POLLUTED team-전투력 (267250/203918); no HP/ATK/DEF panel |
| Iczel `vXuGNGCMg3Q` Part 1 (5895s, 1965 frames @1/3fps) | EN story/battles/battle-prep/attend./recruit; sweep IN PROGRESS (1144/1965 rows at write time) | **HIT 3** (Riko Lv.1) so far; only frame ≥8 is the hit |
| ZOPAR `tH-mTRN9zBs` guild ep1 (5834s) / `qJeB64RW3GY` ep2 (4464s) | JP VTuber guild runs; metadata verified, ≤720p downloaded | Sweeps queued behind `vXuGNGCMg3Q`; NOT yet scanned |

Reddit `hzkbt3` team-comp: re-tried via `old.reddit.com/r/Blustone/...json`
(read-only fetch) — new-Reddit shell HTML, no post content. **Transport-blocked;
NOT a content negative.** Needs in-app browser, still unavailable this lane.

### HIT 2 — card-detail stat panel: アーカーシャ (catalog 008 Akasha), Lv.1

- Source: [【ブルーストーン#1】探偵社で10連ガチャ](https://www.youtube.com/watch?v=GxThPFqGBQk)
  by いちごみるく, 69s, uploaded 2018-12-12 (JP client, fire-attribute event).
- Frames: `hits/GxThPFqGBQk_f00062..65.jpg` (t≈62–65s) + `.txt` sidecars with
  URL+timestamp+OCR text+human verbatim (f00062/f00065 enriched).
- Verbatim (JP): 神木の巫女 アーカーシャ, 3★, ミドルハンター, Lv.1;
  戦闘力 *834 (leading digit obscured by banner art — NOT claimed);
  キャラクター基本能力値 HP 543 / 攻撃力 362 / 防御力 372 / 攻撃スピード 7;
  攻撃: 致命打率 12 / 致命打ダメージ量 193 / 貫通力 0;
  防御: ブロック率 12 / ブロックダメージ減少量 40 / 属性強化 0 / 属性耐性 0 /
  再生力 15.
- Identity: title+name+stars match catalog `008` Akasha ("Maiden of Gods", 3★
  Support/Lightning/Werewolf); corroborated by archived official JP profile
  (level/gear not shown: combat 8081 / HP 1710 / ATK 762 / DEF 762 / speed 7 /
  crit 14 / critdmg 185 / pen 0 / block 14 / blockred 40 / elem 0/0 / regen 43).
  Shared field agrees (block-reduction 40).
- Disposition: named Lv.1 full-panel anchor candidate (fresh 10-pull recruit, no
  green equip deltas visible — but nude NOT proven). **No base-stat coverage
  claimed by this lane**; ledger owner adjudicates.

### HIT 3 — card-detail stat panel: Riko (catalog 024), Lv.1 [partial sweep]

- Source: [Blustone Anime RPG Clicker … Gameplay Part 1](https://www.youtube.com/watch?v=vXuGNGCMg3Q)
  by Iczel Gaming, 5895s, uploaded 2018-06-24 (EN client).
- Frame: `hits/vXuGNGCMg3Q_f00351.jpg` (t≈1053s, score 11) + sidecar with
  URL+timestamp+human verbatim. Neighbor f00353 is the recruit splash (same
  2★ wolf-girl art, no numerals — context only, not preserved).
- Verbatim (EN): "Hard-Knock Life" Riko (name partly behind star badge), 2★,
  Novice Hunter, Lv.1; Strength 800;
  HP 290 / AP 217 / DP 262 / Attacking Speed 7;
  Critical Attack Chance 11 / Critical Attack Damage 185 / Armor Penetration 0;
  Block Chance 27 / Damage Reduction Block 50 / Elemental Enhancement 0 /
  Elemental Resistance 0 / HP Regeneration 9.
- Identity: title+stars match catalog `024` Riko ("Hard-Knock Life", 2★
  Defense/Lightning/Werewolf, Wolf Knuckles/choker motif matches splash art).
- Disposition: named Lv.1 full-panel anchor candidate; gear state NOT
  established. **No base-stat coverage claimed by this lane.**
- Sweep status: only 1144/1965 frames scored at write time; f00351 is the sole
  frame ≥8 so far. Remainder + `tH-mTRN9zBs` + `qJeB64RW3GY` still pending.

### Polluted track (added)

- `hits/0w9pGq-vkxQ_f00005_VS-team-power.jpg` + sidecar: 희애 VS 재키퀼트,
  team 전투력 267250 (승점 4776, 순위 10) vs 203918 (승점 4360, 순위 21).
  Gear/level unknown — context only.
- Otherwise: 0 equipment stat screens, 0 hunter-list stat fields, 0 monster
  panels. Strict counts unchanged.

### Still remaining after this pass

- `vXuGNGCMg3Q` remainder (~821 frames) + `tH-mTRN9zBs` + `qJeB64RW3GY` full
  sweeps (1/3fps extractions queued in one background job; downloads done).
- ぼってぃちぇり JP fightclub clips ×6 (67–148s, titles all VS-battles):
  identified via search, expected battles-only, not downloaded — optional.
- Reddit `hzkbt3` team-comp image: transport-blocked, needs in-app browser.

## Final — 2026-10-11 night lane (all long sweeps complete)

Background job finished: `DONE vXuGNGCMg3Q frames=1965`,
`DONE tH-mTRN9zBs frames=1945`, `DONE qJeB64RW3GY frames=1488`
(all @1/3fps, same PASS-8/8 OCR pipeline). Line-level audit of
`frame-results.tsv` confirms every extracted frame scored
(vXu 1965/1965, tH 1945/1945, qJe 1488/1488; an early DictReader-based count
under-reported tH at 1907 due to embedded newlines in snippets — resolved by
line-based recount, 0 frames unscored).

- `vXuGNGCMg3Q`: sole frame ≥8 remains **HIT 3** (f00351, score 11). No new
  hits. Rest is EN story/battles/battle-prep (levels only)/attendance/recruit
  splash/map.
- `tH-mTRN9zBs`: max score 7, zero frames ≥8 or trio. JP VTuber (ZOPAR クゥ)
  story + battles + ★4エリーズ recruit banner (f00584–588, f00860/874 band:
  初回召集時キャパ超越+1, 10+1 pulls, costs 30/300 — identity context only) +
  one スキルトレーニング screen (f01000): Lv.1/40, 攻撃本能,
  スキル効果 ダメージ量 0.30% → 0.60%, items 34/1, Start 100
  (visual reading; OCR fragmentary under VTuber overlay). **Skill-lane lead,
  NOT a stat panel.** No hits.
- `qJeB64RW3GY`: max score 7, zero frames ≥8 or trio. Same VTuber format,
  story (チルチル dialogue, 赤い峡谷) + battles + Elise banner. No hits.

Lane totals: 13 videos swept (10,398 scored frame-rows), 3 card-detail HITs
(Tyltyl 004, Akasha 008, Riko 024 — all Lv.1 full panels, gear state NOT
established, **no base-stat coverage claimed**), 3 polluted VS team-power
frames, 0 equipment screens, 0 hunter-list stat fields, 0 monster panels.
Search log: `search-log.tsv` (31 lines). Remaining: ぼってぃちぇり ×6
(optional battles-only) and Reddit `hzkbt3` (transport-blocked, needs in-app
browser).
