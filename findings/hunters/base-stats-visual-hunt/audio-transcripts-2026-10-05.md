# VSFan audio / transcript mining — 2026-10-05

**Scope:** mine the local `analysis/VSFan/` archive for spoken or written numerals
that could bear on the hero base-stat recovery goal.

**Method:** `ffprobe`/`ffmpeg` 8.1.2 for stream/duration/loudness facts;
`faster-whisper` 1.2.1 (CTranslate2, CPU int8) for speech detection and
transcription, using the **multilingual** `small` and `large-v3` models because
the only speech-bearing file is Korean. Audio was decoded to 16 kHz mono WAV.
Every "speech present / no speech" verdict was cross-checked against an
independent `volumedetect` level reading so that a zero-speech result could not be
blamed on a quiet source. Where the two model sizes disagreed, the disagreement
is recorded as a disagreement rather than resolved silently.

**Read-only:** nothing under `analysis/VSFan/` was modified. No APK, server,
emulator or account was touched.

**Locator caveat:** every source here is a **local archive file with no public
URL**. Locators are therefore repository-relative paths plus media timestamps,
not `https://` URLs. Where the task template asks for a URL, the path is the
authoritative locator.

**Headline result:** the archive contains **172 MP3 files and 257 videos**, of
which exactly **one file contains speech** — a 612-second Korean *launch
ceremony* room recording. The **only numerals anywhere in spoken audio are a
ceremonial countdown `10 → 1`.** The 85 dialogue-transcript JSONs contain
**zero numerals in 668 prose lines × 5 locales** (the only digit hits are RGBA
colour markup). **No hero, accessory, jewel-instance or monster base statistic
was recovered. Strict coverage is unchanged: heroes 1/113, accessories 1/100,
monsters 0/22.**

---

# SECTION 1 — PURE (verified inventory and transcribed content)

Everything in this section is a direct measurement or a verbatim quoted string.
Interpretation, disputed readings and coverage consequences are in Section 2.

## 1.1 Audio (MP3) inventory — 172 files, 1,126.033 s, 33,141,610 bytes

All 172 files probed successfully (`ffprobe` duration/size on every file).

| Group | Files | Total duration | Notes |
|---|---:|---:|---|
| `Audio/Blustone/` (curated) | 10 | 576.655 s | 320 kb/s stereo; the 10 tracks listed in `vsfan-visual-audio-material.md` |
| `Extracted Assets (2026)/1.1.2.0 (blustone.pcap, 2017-09-04)/**` | 54 | 93.960 s | `C017`–`C020` `_SND` per-character sound packages |
| `Extracted Assets (2026)/1.1.3.0 (bs_transcendence.pcap, 2017-09-08)/**` | 29 | 44.316 s | `C021`–`C028` `_SND` packages |
| `Extracted Assets (2026)/1441 (APK)/C001_SND/` | 5 | 8.869 s | Lantern (`001`) sound set |
| `Extracted Assets (2026)/1441 (APK)/C003_SND/` | 4 | 4.441 s | Nene (`003`) sound set |
| `Extracted Assets (2026)/1441 (APK)/C009_SND/` | 5 | 6.047 s | Captain (`009`) sound set |
| `Extracted Assets (2026)/1441 (APK)/SND1/` | 65 | 391.745 s | main music/SFX bank |

Speech-detection verdict per group:

| Group | Speech verdict |
|---|---|
| `Audio/Blustone/` 10 curated tracks | **0 speech segments in 10/10 files.** Levels are loud (mean −13.4 … −24.2 dB, max ≥ −8.9 dB), so this is a genuine non-speech result, **not** a VAD-on-quiet-source artifact. |
| 162 extracted MP3 | **0 speech in 155 files.** The remaining **7 produced model-dependent captions that are provably hallucinations** (Section 2.4); they are not accepted as transcripts. |
| `SND1/` 65 files | 0 accepted speech. Contains the only long music items (`274e66df` 29.94 s, `40fc1551` 54.91 s, `a4863a20` 60.55 s, `acb94924` 36.57 s, `b67dd10c` 40.41 s). |

## 1.2 Video inventory — 257 files; only 8 carry an audio stream

| Video (repository-relative) | Duration | Audio codec | Mean / max level | Speech verdict |
|---|---:|---|---|---|
| `Intro.mp4` | 30.186 s | AAC mono 44.1 k | −65.0 / −38.6 dB | effectively silent; 0 speech |
| `Research/Blustone/Blustone Launch Ceremony.mp4` | **612.088 s** | AAC mono 48 k, 64.5 kb/s | **−22.8 / −0.3 dB** | **Korean speech, `language=ko p=0.990`** |
| `Research/Blustone/Parallax Break.mp4` | 46.954 s | AAC mono 44.1 k | −64.3 / −20.0 dB | effectively silent; 0 speech |
| `Research/Beyond the Bounds/btbr/비욘드 더 바운즈 (Unicode Encoding Conflict).mp4` | 70.542 s | AAC stereo | — | 0 speech |
| `…/1441 (APK)/STORY_TUTO/0000a520.mp4` | 14.21 s | AAC | −12.0 / 0.0 dB | loud but **0 speech** (non-speech cue) |
| `…/1441 (APK)/STORY_TUTO/0393623f.mp4` | 8.17 s | AAC | −14.0 / 0.0 dB | loud but **0 speech** |
| `…/1441 (APK)/STORY_TUTO/367d39be.mp4` | 9.10 s | AAC | −12.6 / 0.0 dB | loud but **0 speech** |
| `…/1441 (APK)/STORY_TUTO/9ab4b57b.mp4` | 11.73 s | AAC | −12.8 / 0.0 dB | loud but **0 speech** |

The remaining **249 videos are silent** (no audio stream at all). This includes
all 249 EFT skill-animation clips (`C0xx_EFT`, `INGAME_EFT`, `CI`) and
`STORY_TUTO/e9b9729c.mp4`. The four `STORY_TUTO` clips with audio are loud yet
speech-free, so the "story cutscene" hypothesis is **falsified**: they carry
music/SFX, not narration.

`Blustone Launch Ceremony.mp4` video itself is 360×640 H.264 at 30 fps. A
15-frame contact sheet (t = 0, 60, 120, 180, 240, 300, 360, 420, 480, 520, 540,
555, 570, 600, 611 s) shows a dim function room: attendees, tables, balloons,
neon tube lighting and desktop monitors. Monitor content is blown out and
occupies only a few dozen pixels at the source resolution, so **no game UI and no
stat text is legible in this clip.** This confirms and extends the earlier
"sampled frames … no readable game demonstration or stat panel" note in
`vsfan-research-material.md`.

## 1.3 The one speech-bearing file: transcript inventory

`Research/Blustone/Blustone Launch Ceremony.mp4` → audio track, 612.09 s.

- Detected language **Korean**, `language_probability = 0.990` (multilingual
  `large-v3`; `small` agreed).
- `large-v3`: **90 segments, 122.4 s of speech**, spanning **3.60 s → 548.70 s**.
- The remaining ~63 s (548.70 → 612.09) is music/crowd with no recognised speech.
- A 379-second gap between 8.42 s and 388.04 s contains no recognised speech.
  Re-transcribing that gap without VAD suppression returned **27 segments of
  event-room chatter only**: champagne glasses, someone finding their seat,
  "let's do the countdown together", someone turning the lights on.
  **No gameplay commentary and no game vocabulary appear in this gap.**
- Content classification: a live *global launch* ceremony room, not a game
  demonstration. Verbatim anchors:
  - 403.85 s — "이거 유튜브 연기인거 같잖아요" ("this looks like a YouTube act")
  - 422.49 s — "라이브로도 잘 안보이네요" ("it's not even visible on live")
  - 451.86 s — "전부 사용가능으로 눌러놓고" ("pressed 'make all available'")
  - 487.28 s — "카운트다운 할까요?" ("shall we do a countdown?")
  - **520.38 s — "카운트다운 영어로 할게요 영어로" / 522.34 s — "글로벌 런칭이니까"**
    ("I'll do the countdown in English … because it's the global launch")
  - 531.96 s — "목소리 누가 제일 크지?" ("who has the loudest voice?")
  - 548.53 s — "런치~!" ("Launch!")

Two attendee names are audible in the room chatter and are **deliberately not
transcribed** (personal data in a private event recording).

## 1.4 Written transcript corpus (the "transcripts" that are actually text)

### 1.4.1 Dialogue transcripts — `DIALTU-*`, 85 JSON files

`Extracted Assets (2026)/1441 (APK)/DIALTU-{KO,EN,JP,ZH,ZT}/`, 17 hashed files
per locale (`820e904a/b/c/d/e`, `820e9070/71`, `820e9096/97`, `820e90e2/3/4`,
`820e9109`, `820e912e/2f/30`, `820e9154`). Structure per file: `Version`,
`EmphasisColor*`, and `Assets.{Actors, Items, Conversations, UserVariables,
Locations}`; conversation nodes carry `Fields[Title/Value/Hint/Type]`.

Prose-bearing field is `Dialogue Text`. Measured counts:

| Locale | Prose lines | Prose lines containing a digit |
|---|---:|---:|
| KO | 668 | 8 |
| EN | 668 | 8 |
| JP | 668 | 11 |
| ZH | 668 | 8 |
| ZT | 668 | 8 |

**Every digit-bearing prose line is RGBA colour markup, not a spoken number.**
Example, `DIALTU-EN/820e9096.json`:
`"<color='240, 20, 50, 255'>AHHHHHH!!!!!</color>"`; likewise
`820e9109` `"Cough, cough... Are they <color='240, 20, 50, 255'>Metron hunters?</color>…"`.

Non-prose digits in these files are structural only, and are the reason the
per-locale digit counts are identical: `Version "1.0.0.0"`, `EmphasisColor*`
hex values, actor `CardID` values (`009`, `010`, `047`, `052`, `056`), dialogue
node ids, and motion-script parameters such as `wait duration:0.3`,
`scr-blink cnt:2 color:(255, 255, 255, 255) blinktime:0.1`,
`scr-fade duration:0.6`, `video-player res:START scale:(1.11,1.11,1.11)`.

### 1.4.2 `UI_CSV` — 6 files, audited individually

| File | Size | Structure | Audit result |
|---|---:|---|---|
| `7adedb12.txt` | 1,198,540 B | header `#ID,ORI_TXT,LANG,TXT,TXT-SIZE,TXT-ALGN,TXT-COLOR,BOUND-POS,BOUND-SIZE,BOUND-ALIGN,FONT,LINE SPACING,TEXT SPACING`; **11,560 data rows**; 5 locales | UTF-8 **with BOM**. It is simultaneously a style table *and* the **complete 5-locale UI string table**. Its 287,345 digit characters are almost entirely layout/colour/font specs (`54|177|192|255`, `120|30`, `NOTOSANS`); only **4 EN rows** combine a stat keyword with a number (Section 2.6). Carries the canonical stat labels (1.5). |
| `e44ab8ed.txt` | 81,975 B | header `#COR,KR,EN,JP,ZH,ZH-HANT`; **820 data rows, all well-formed 6-field** | The **in-game system-message / help-label table** in 5 languages. **45 EN rows contain a digit**; all are rules, gates, limits or format strings (Section 2.6). Carries the canonical stat abbreviations (1.6). *Not previously mentioned in `vsfan-extracted-assets.md`.* |
| `3d98d128.json` | 123,987 B | localized help records | Already audited: record `CONTENTS11_8` holds all 12 jewel set-bonus families (see `vsfan-extracted-assets.md`). Re-checked here only for numerals. |
| `3d9fb02e.json` | 16,952 B | `entry_point_ko.{title,list[]}` → `CATEGORY1…N` + `*_DETAIL` goal ids | A help **index**, not content. No numeric stat. *Not previously mentioned.* |
| `300e08f5.txt` | 1,419 B | `키워드,파일명,반복,지연시간,볼륨,설명` (keyword, file, repeat, delay, volume, description); **34 rows** | The **sound-event → FX-cue table** (1.7). UTF-8 with BOM; the only numeric column is `지연시간` (delay in seconds). |
| `7f8605b6.txt` | 41,320 B | `KR,EN,JP,ZH,ZH-HANT` | A localized profanity/filter dictionary. **Contents intentionally not reproduced**; no game-stat value. Consistent with the prior note. |

### 1.4.3 Other textual assets

`MOTION/` 110 XML + 2 JSON, `GLSL/` 35 `.glsl` shaders, `FONT/` 9 `.bin`,
`LAYOUT-BASE/` 10 `.bin`, `LEVELING/` 2 `.bin`. `LEVELING` numeric rows are
shared tuning already audited elsewhere; nothing here is a per-hero or
per-monster tuple.

## 1.5 Original 12-attribute panel — verbatim EN strings (`7adedb12.txt`)

Panel title and attribute labels, quoted exactly as the original localization
table stores them:

| Key | EN string |
|---|---|
| `TX_ST_TL1` | `Character Attributes` |
| `TX_ST_SB1` | `HP` |
| `TX_ST_SB2` | `DEF` |
| `TX_ST_SB3` | `ATK` |
| `TX_ST_SB4` | `Attacking Speed` |
| `TX_ST_SB5` | `Critical Attack Chance` |
| `TX_ST_SB6` | `Critical Attack Damage` |
| `TX_ST_SB7` | `Armor Penetration` |
| `TX_ST_SB8` | `Block Chance` |
| `TX_ST_SB9` | `Damage Reduction Block` |
| `TX_ST_SB10` | `Elemental Enhancement` |
| `TX_ST_SB11` | `Elemental Resistance` |
| `TX_ST_SB12` | `Regeneration` |
| `TX_ST_TL2` | `Stat Details : Attack` |
| `TX_ST_TL3` | `Stat Details : Defense` |

That is **12 attributes**. Companion strings that identify the power/rating
family and the panel's own terms:

| Key | EN string |
|---|---|
| `TX_ST_TL` | `Strength` |
| `TX_STRE_TL`, `TX_STRE_TL_MY` | `Fight Specs` |
| `TX_POWER` | `Team Strength` |
| `TX_CH_TL`, `TX_CH_TL1` | `Strength` |
| `TX_LI_TG2` | `Sort by Strength` |
| `TX_INFO2` | `Enemy's Strength` |
| `TX_INFO3` | `Allies' Strength` |
| `TXT_INVEN_SRT3` | `Strength` |
| `STRENGTH` | `Strength` |
| `UI_TR_AT_TX`, `UI_EV_AT_TX` | `Power\nUpgraded` |

Equipment panel and Transcendence panel:

| Key | EN string |
|---|---|
| `TX_EQ_ST`, `TX_EQ_ST1` | `Strength` |
| `TX_EQ_SB1` / `TX_EQ_SB2` / `TX_EQ_SB3` | `HP` / `DEF` / `ATK` |
| `TX_EQ_SB5`…`TX_EQ_SB9` | `Critical Attack Chance`, `Critical Attack Damage`, `Armor Penetration`, `Block Chance`, `Damage Reduction Block` |
| `TRC_POWER1`, `TRC_POWER2` | `Strength` |
| `TRC_STAT1` / `TRC_STAT2` / `TRC_STAT3` | `ATK` / `Defense` / `HP` |
| `TRC_TXT` | `Successfully transcended.` |
| `TRC_TXT1` | `Successfully trained.` |

**Placeholder-only strings that must never be read as data:** `TRC_POWERNUM1`,
`TRC_POWERNUM2`, `TRC_STAT1_1`, `TRC_STAT1_2`, `TRC_STAT2_1`, `TRC_STAT2_2`,
`TRC_STAT3_1`, `TRC_STAT3_2` are all the literal design-time dummy `10000`;
`TX_ST_NM1`…`TX_ST_NM12`, `TX_SK_LI_AF`, `TX_SK_LI_BF`, `UI_LI_IF_NM` are `0`;
`TX_MD_BN_NM` is `15000`.

## 1.6 Canonical stat abbreviations (`e44ab8ed.txt`)

Nine rows carry the game's stat names in all five languages:

| Correlation key | KR | EN | JP | ZH | ZH-HANT |
|---|---|---|---|---|---|
| `생명력` | HP | `HP` | `HP` | `HP` | `HP` |
| `방어력` | DEF | `DEF` | 防御力 | 防御力 | 防禦力 |
| `공격력` | ATK | `ATK` | 攻撃力 | 攻击力 | 攻擊力 |
| `현재 체력` ("current HP") | HP | `HP` | `HP` | `HP` | `HP` |
| `공격력[개행x]` | ATK | `ATK` | 攻撃力 | 攻击力 | 攻擊力 |
| `방어력[개행x]` | DEF | `DEF` | 防御力 | 防御力 | 防禦力 |
| `최대 체력[약식]` ("max HP", short) | HP | `HP` | `HP` | `HP` | `HP` |
| `공격력[약식]` | ATK | `ATK` | 攻撃力 | 攻击力 | 攻擊力 |
| `방어력[약식]` | DEF | `DEF` | 防御力 | 防御力 | 防禦力 |

The localization table therefore distinguishes **current** HP (`현재 체력`)
from **maximum** HP (`최대 체력`). An HP tooltip definition is present:
correlation key `툴팁_수치_생명력` → EN
`The limit of your might.\nOnce your health reaches 0| you can no longer fight.`

## 1.7 Sound-event → FX-cue table (`300e08f5.txt`, 34 rows, decoded)

Numeric columns are `반복` (repeat flag), `지연시간` (delay, seconds) and
`볼륨` (volume). Selected rows verbatim:

| Keyword | FX file | repeat | delay | volume | KO description |
|---|---|---:|---:|---:|---|
| `BATTLE_WIN_START` | `FX_FC_WIN` | 0 | 0.7 | 1 | 파클승리 시작음 |
| `BATTLE_WIN_LOOP` | `FX_VICTORY` | 1 | 2 | 1 | 파클승리 결과음 |
| `MAP_STAR_COME` | `FX_STAR_COME` | 0 | 1.8 | 1 | 스테이지 별연출-별올라옴 |
| `MAP_STAR_GET` | `FX_STAR_GET` | 0 | 2.7 | 1 | 스테이지 별연출-별획득 |
| `MISSION-BRONZE` | `FX_GETITEM_N` | 0 | 0.2 | 1 | 승리보상-브론즈 |
| `MISSION-SILVER` | `FX_GETITEM_R` | 0 | 0.6 | 1 | 승리보상-실버 |
| `MISSION-GOLD` | `FX_GETITEM_U` | 0 | 0.8 | 1 | 승리보상-골드 |
| `RASE-RESULT` | `FX_GYM_TRN` | 0 | 0.7 | 1 | 훈련결과 효과음 |
| `RANKUP-RESULT` | `FX_GYM_RU2` | 0 | 0 | 1 | 승급결과 효과음 |
| `HYPER-RESULT` | `FX_GYM_TRC` | 0 | 0.5 | 1 | 초월결과 효과음 |
| `GACHA_GET1/2/3` | `FX_KID_GET1/2/3` | 0 | 0.3 | 1 | 뽑기결과 1성 / 2성 / 3성이상 |
| `FUEL-CHARGE` | `FX_UI_FUEL` | 0 | 0.3 | 1 | 연료 충전 팝업 |
| `AUTO_RESULT` | `FX_UI_AUTO` | 0 | 0.5 | 1 | 맡기기 결과 팝업 |
| `FISHING_CATCH` | `FX_FI_CATCH` | 0 | 0 | 1 | 낚아올리는 애니메이션 등장 |
| `EQUIP_SUCEESS` | `FX_GEM_WIN` | 0 | 1.3 | 1 | 장비 강화 성공 이펙트 |
| `EQUIP_LEVELUP` | `FX_GYM_SKL` | 0 | 0 | **0.3** | 장비 레벨업시 |

Notes: `RASE-RESULT` is a shipped typo for "raise". `EQUIP_LEVELUP` is the only
row whose volume is not `1`. The GYM family maps to the three progression verbs
the game distinguishes in text: 훈련 (train), 승급 (advance/rank up),
초월 (transcend/hyper). These are **audio cue timings, not game statistics.**

## 1.8 Packet captures — endpoints and versions only

`analysis/VSFan/Packet Captures/` holds 5 files: `blustone.pcap`
(128,731,909 B), `bs_transcendence.pcap` (54,929,150 B), `btba_install.pcap`
(21,496,355 B), `whiteisland.pcap` (96,353,113 B), `btba.pcap` (1,102,501 B).

The game API bodies are encrypted at the application layer, so **no numeric game
data can be read from them.** Endpoints/versions are already documented in
[`vsfan-packet-capture-findings.md`](../../revival/vsfan-packet-capture-findings.md) and
are not re-listed here. Version-relevant facts only:

- `blustone.pcap` → Blustone **1.1.2.0**; hosts `pv-prd.vshower.com` and
  `sr-prd.gshower.net`; plain `GET /_SR_PRD/<package>_<stamp>.pkg` CDN requests;
  reference routes `/reference/GetCard`, `GetCardBook`, `GetCardChain`,
  `GetCardRankUp`, `GetCardEnhancePrice`, `GetBattle`, `GetLevel`, `GetItem`,
  `GetMonster`, `GetStageMonster`, `GetArea`, `GetStage`, `GetAbyss`.
- `bs_transcendence.pcap` → Blustone **1.1.3.0**; additionally
  `/reference/GetCardOvercome`; reslist `reslist_20170908141924.list`
  (resource version `20170908141924`, 149 entries, 385,496,169 bytes) versus the
  1.1.2.0 list `reslist_20170904165634.txt` (140 entries, 379,438,483 bytes).
- `btba_install.pcap` → separate `_BTBA_PRD` product; `btba.pcap` and
  `whiteisland.pcap` are TLS-only with no recoverable route.

**Redaction:** these captures contain account/session-associated fields. No
token, cookie, `pvid`, login blob, tracking key or personal value is reproduced
in this report, and no capture body was parsed for numbers.

## 1.9 Corrections to existing VSFan notes

1. `vsfan-material-index.md` summarises the audio material as "ten MP3s" plus a
   "30-second startup capture". The actual corpus is **172 MP3 and 8
   audio-bearing videos**, and the 10 curated MP3s are now **proven non-speech**.
2. `vsfan-extracted-assets.md` describes `7adedb12.txt` as "a rendering/style
   string table (font, alignment, colors, bounds)". It is *additionally* the
   complete 5-locale UI string table and is the origin of the canonical stat
   labels in 1.5.
3. `vsfan-extracted-assets.md` does not mention `e44ab8ed.txt` (820 rows) or
   `3d9fb02e.json`. Both are audited here for the first time.
4. `vsfan-research-material.md` logged `Blustone Launch Ceremony.mp4` (612 s) and
   `Parallax Break.mp4` (47 s) on **visual** grounds only. Their **audio** had
   never been transcribed; that is resolved here (1.2, 1.3).
5. The `STORY_TUTO` cutscene videos were implicitly assumed to be narrated
   because they carry an audio stream. They are **loud but speech-free**.

---

# SECTION 2 — UNPURE (every spoken/written numeral, with uncertainty)

**All entries in this section are polluted leads. None contributes to any
coverage threshold.** They are recorded so the set is auditable in one place and
so a future pass does not have to re-derive them.

## 2.1 Confirmed spoken numerals — a ceremonial countdown, not a statistic

**Only source:** `analysis/VSFan/Research/Blustone/Blustone Launch Ceremony.mp4`,
audio track. No public URL exists for this archive file; timestamps are media
timestamps into the file's own audio stream.

| Spoken numeral | Timestamp (s) | Model(s) | Claimed field | Uncertainty |
|---|---|---|---|---|
| `10` | 535.48 – 536.18 | `large-v3`, `small` | ceremonial countdown ordinal before the global launch announcement | Crowd mic + background music; segment `avg_logprob ≈ −0.31`. Not a game field. |
| `9` | 536.18 – 537.58 | `large-v3`, `small` | same | same |
| `8` | 537.58 – 538.60 | `large-v3`, `small` | same | same |
| `7` | 538.60 – 540.34 | `large-v3`, `small` | same | same |
| `6` | 540.34 – 541.58 | `large-v3`, `small` | same | same |
| `5` | 541.58 – 542.66 | `large-v3`, `small` | same | same |
| `4` | 542.66 – 543.96 | `large-v3`, `small` | same | same |
| `3` | 543.96 – 545.06 | `large-v3`, `small` | same | same |
| `2` | 545.06 – 546.04 | `large-v3`, `small` | same | same |
| `3, 2, 1` (tail re-transcription of 545.00 – 612.09) | 545.00 – 547.26 | `large-v3` | same | Overlaps the row above; `1` is only resolved in the tail pass. |
| `런칭!` ("Launch!") | 548.00 – 548.64 (`small` full-file pass places the same shout at 548.53 – 549.41) | `large-v3`, `small` | launch cue, not a number | — |

**Claimed field, explicitly: none.** These are ordinals spoken by event
attendees during a countdown that immediately precedes a launch announcement.
The surrounding speech states the intent outright — 520.38 s
"카운트다운 영어로 할게요" and 522.34 s "글로벌 런칭이니까" ("countdown in English
… because it's the global launch") — and 531.96 s "목소리 누가 제일 크지?" ("who
has the loudest voice?").

**Consequence:** a countdown `10 → 1` is *not* an HP/ATK/DEF/Strength value, an
area/stage count, a star count, a fuel value or a currency amount. It earns
**no coverage credit** and must not be attached to any catalog entity.

## 2.2 Disputed / unreproduced numeral candidates

| Candidate | Timestamp (s) | Reported by | Status |
|---|---|---|---|
| `4!` | 547.05 – 547.45 | `small` (full-file pass) only | **UNRESOLVED — not confirmed.** It falls after `2!` and before the launch shout, which is inconsistent with a straight `10 → 0` countdown. `large-v3` does not emit a token there. Most likely a crowd overlap or a genuine miscount by the speaker, but that is inference, not evidence. Do not cite as a read numeral. |
| `하나, 둘, 셋` ("one, two, three") | 570.96 – 572.14 | `small` (full-file pass) only | **REJECTED as unreproducible.** `large-v3` transcribed 568.68 – 570.64 of the same region as a different phrase, and a `small` re-run over the 560 – 612 region produced no token there either. The two model sizes disagree with each other and with `small`'s own earlier pass. Treated as a model artifact, not a spoken count. |

## 2.3 Numeral-shaped false positives that were rejected

A naive Korean numeral scan flags the Sino-Korean digits
`일이삼사오육칠팔구십백천만억`, which produced these matches in the ceremony
transcript. All are **homographs, not numerals**, and are listed so they are not
re-raised by a future pass:

| Flagged | Actually | Example timestamp |
|---|---|---|
| `이` | 이거 "this" | 395.16 s "네 이거는" |
| `일` | 제일 "the most" | 531.96 s "누가 제일 크지?" |
| `구` | 누구 "who" | 441.44 s "누구야 아직 아닌데" |
| `사` | 사용 "use" | 455.10 s "사용가능" |
| `만` | 나만 "just me" | 393.56 s "나만하게" |
| `하나` | 하나도 "not one" | 434.10 s "안보여요 하나도" |

A Korean-language model transcribing a noisy Korean room is expected to produce
this collision class; it is a limitation to record, not a finding.

## 2.4 ASR hallucination catalogue — 7 extracted MP3 clips, no accepted transcript

These are the only extracted-MP3 files where either model produced any text.
Each returns a **generic, mutually contradictory caption**, so none is accepted
as a transcript and none contains a numeral.

| File (under `Extracted Assets (2026)/`) | Duration | Mean level | `small` caption | `large-v3` caption | Verdict |
|---|---:|---:|---|---|---|
| `1.1.3.0 (bs_transcendence.pcap, 2017-09-08)/C021_SND_20170601193747/217d201e.mp3` | 1.39 s | −9.0 dB | "Thanks for watching!" | "Thank you for watching." (`en`, p=0.27) | hallucination |
| `…/C022_SND_20170601193747/d4f45e5e.mp3` | 1.58 s | −14.3 dB | "구독과 좋아요 부탁드려요!" (`ko`, p=0.495) | "ご視聴ありがとうございました" (`ja`, **p=0.176**) | hallucination — detected language flips KO → JA on identical audio |
| `…/C022_SND_20170601193747/d4f45e5f.mp3` | 2.74 s | −15.4 dB | "구독과 좋아요 부탁드려요!" | "ご視聴ありがとうございました" | hallucination |
| `…/C028_SND_20170703154022/09bfd3e2.mp3` | 1.61 s | −27.1 dB | "Ha ha ha!" | "You're welcome." (`en`, p=0.899) | hallucination |
| `1441 (APK)/SND1/191bb3c1.mp3` | 0.97 s | −35.9 dB | "You" | "Thank you." (`en`, p=0.508) | hallucination |
| `1441 (APK)/SND1/274e66df.mp3` | 29.94 s | −14.8 dB | "BEEP" | *(no speech)* | `small` hallucination |
| `1441 (APK)/SND1/b67dd10c.mp3` | 40.41 s | −23.0 dB | "You" | "Thank you." (`en`, p=0.708) | hallucination |

Evidence that these are artifacts rather than real narration:

1. Two independent model sizes return **different text for the same audio**
   (`small` Korean vs `large-v3` Japanese on `d4f45e5e`).
2. Language confidence is very low exactly where the caption is most confident
   (`p=0.176` for the Japanese reading).
3. The same generic "thank you for watching" / "you're welcome" family recurs
   across **unrelated packages** (`C021_SND`, `C022_SND`, `C028_SND`, `SND1`).
4. The batch harness reported `speech_sec = 29.98` for files whose duration is
   1.39 – 2.74 s, i.e. the segment accounting is internally inconsistent.

**Do not claim these clips contain YouTube narration or creator speech.** Their
content is UNRESOLVED; they are recorded here only so a later pass knows the
files were tested. This is an explicit **retraction** of the naive reading that
`C021`/`C022` "SND" assets carry English/Japanese subscribe-and-like
narration.

## 2.5 Field-identification upgrades for existing polluted rows — values unchanged

The recovered original strings (1.5, 1.6) let several previously *inferred*
field attributions be grounded in the game's own wording. **No numeric value
changes, no identity is resolved, no gear/level state is established, and no
base tuple is created — every one of these rows remains polluted and earns no
credit.**

| Existing polluted row | Previous state | What the strings add | What is still unresolved |
|---|---|---|---|
| Naver Hunter List `55/114` with 12 tokens; Reddit Offense/Defense lists (`98/105`); AppStorio Hunter List `19/102` | "roster numbers likely represent a rating/power (medium confidence)" | `TX_LI_TG2 = "Sort by Strength"` and `TX_CH_TL = "Strength"` exist as original UI strings, so the sorted column is a **Strength/rating** field — not HP/ATK/DEF | Which catalog IDs each row is; level/rank; gear/jewel state. Raw tokens stay unassigned to per-hero stats. |
| Caragublu `2,628 → 3,068` / `2,628 → 3,947`; AppStorio `3,014 → 4,407`; GameAppCH `1,417 → 2,389`; FreeGame Mugen `7,092 → 11,277` | "likely the `Power Upgraded` rating field … that remains an inference" | `UI_TR_AT_TX = "Power\nUpgraded"` and `UI_EV_AT_TX = "Power\nUpgraded"` exist verbatim, so the label is original. The field is a Strength-style rating | The screenshots themselves still do not print the label; hero identity, rank/level and gear are unresolved; fodder-selection semantics unknown |
| Any screenshot printing `HP` | assumed maximum HP | `생명력`/`현재 체력` (current HP) and `최대 체력` (max HP) are **distinct** original strings, and `HP`/`DEF`/`ATK` are confirmed as the EN abbreviations | A bare `HP` on a battle HUD is still ambiguous between current and maximum; only a `TX_ST_TL1 "Character Attributes"` panel row is unambiguously the stat panel |
| The 62 archived 13-field profile rows | "13-field readings", fields unnamed | The panel has exactly **12 attributes + Strength**, ordered `HP, DEF, ATK, Attacking Speed, Critical Attack Chance, Critical Attack Damage, Armor Penetration, Block Chance, Damage Reduction Block, Elemental Enhancement, Elemental Resistance, Regeneration`, so a positional mapping is now *plausible* | The 2019 archive pages print **none** of these labels, so positional mapping is unverified; level and equipped state remain absent. No row is promoted. |

Also noted: `TX_INFO2 = "Enemy's Strength"` and `TX_INFO3 = "Allies' Strength"`
are the game's own labels for the two sides of a Fight Club comparison, and
`TX_STRE_TL = "Fight Specs"` is its label for the stats block. These give names,
not values.

## 2.6 Original rules / economy numerals recovered from the string tables — not hero stats

All from version **1.4.4.1**; all are game *rules or formats*, never a hero,
accessory, jewel-instance or monster statistic. Useful as historical rule
evidence; **no coverage credit.**

`e44ab8ed.txt` (45 EN digit-bearing rows; representative, non-exhaustive):

| Correlation key | EN string | Kind |
|---|---|---|
| `30초 이내` … `180초 이내`, `180초 이상` | `Less than 30 sec.` / `60` / `90` / `120` / `180 sec.`, `More than 180 sec.` | **Mission clear-condition time thresholds.** Historical wording for the achievement conditions the replica currently implements as local policy. |
| `미드가드 설원 10지역 클리어 필요.` | `Available when Area 10 is cleared.` | progression gate |
| `★3 달성시 활성화됩니다.` / `★4성 이상의 헌터만 …` | `Available when advanced to 3★.` / `4★` | star gates |
| `레벨 20 이하 캡틴만 입장 가능합니다.` | `Only those at level 7 or lower can enter.` | **KR/EN mismatch in the shipped table** (key says 20/21, text says 7/8). Preserve both; do not silently pick one. |
| `영웅 1단 이상의 유저만 …` | `Only those at Guru 1 or higher can enter.` | rank gate |
| `저걸로 횟수를 … 1회만 가능해.` | `… But 10 is your max for now.` | dispatch cap |
| `좀 지나면 …` | `Later on you can dispatch up to 50 times.` | dispatch cap |
| `11명의 헌터를 섭외하시겠습니까?` | `At least 1 out of 11 is guaranteed to be a 2★ or above.` | **Original 10+1 guarantee wording.** Note the 1.4.4.1 text says **2★**, whereas the replica's current local bundle policy is 3★ — a version difference to record, not to reconcile by assumption. |
| `만다를 사용하여 11개의 보석을 채굴합니다.` / `11개의 보석을 …` | `Use Manda to mine 10+1 Jewels.` / `Do you want to mine 11 Jewels?` | jewel mining |
| `해당 상품은 매월 1일 15일에 리셋 …` | `purchasable again every 1st and 15th of the month` | shop reset |
| `TR_GC9` | `Collect it when you attend 28 days consecutively!` | attendance |
| `이메일의 길이가 … (최대 64자)` / `비밀번호의 … (8~20자)` | `maximum 64 characters` / `(8~20 characters)` | input limits |
| `1 ~ 9999까지만 …` | `You can enter only 1~9999.` | nickname limit |
| `- 현재 채널은 %04d 입니다. -` | `- The current channel is %04d. -` | format string |
| `년월일` | `%m/%d/20%y` | date format |
| `RUINS_REMAIN_TIME` | `%dday %02d:%02d:%02d` | countdown format |
| `기기에 따라 … 최대 5분까지 …` | `data transfer can take 5 minutes max` | system message |
| `FILTERING_TXT` | `♥♥` (all five locales) | profanity-filter marker; explains the `♥♥` masking convention |

`7adedb12.txt` — the 4 EN rows combining a stat keyword with a number:

| Key | EN string | Kind |
|---|---|---|
| `TX_CH_RU_SP` | `Ruins' Special Effect: The damage inflicted by offensive hunters is increased by 30%.` | area modifier |
| `TX_CH_LF_INFO` | `Excavation entrances increase based on your Veteran Status and reset every day at 00:00 (GMT+9).` | **daily reset time, GMT+9** |
| `EV_INFO` | `During the event period you will receive 1 Metron Crystal each time you use the 10+1 pull!` | event currency drop |
| `EVENT_SUBNAME` | `Send Dawdly to the deepest mine to get a rare ★3~5 class Jewel.` | gacha band |

## 2.7 Coverage statement

**Strict thresholds are unchanged by this pass.**

| Dataset | Before | After |
|---|---:|---:|
| Hero base stats | 1 / 113 | **1 / 113** |
| Jewel set-bonus families | 12 / 12 observed (1 disputed) | unchanged |
| Mounted jewel panels | 6 / 6 samples | unchanged |
| Accessories | 1 / 100 | **1 / 100** |
| Monsters | 0 / 22 | **0 / 22** |

This pass adds **zero** hero base tuples, zero accessory rows, zero
jewel-instance stats and zero monster tuples. Its actual value is negative-space
plus provenance: it establishes that the archive's entire audio surface contains
no stat-bearing speech, that the dialogue transcripts contain no numerals at all,
and that the game's *own* localization strings now name the stat fields so future
screenshot readings can be labelled without guessing.
