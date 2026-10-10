# BLUSTONE stat hunt — round 2

**Agent:** stat-hunting agent
**Date:** 2026-10-03
**Owns:** `analysis/catalogue/stats/`, and this README
**Did not touch:** `server-ts/`, `tools/`, `recovered-assets/`, `analysis/ghidra-*`,
`instrumentation/`. No adb, no Ghidra, no Docker, no server, **no Git**.

Round 1 (`analysis/research/catalogue-report.md`) swept all text sources and
returned **zero** base stats. Round 2 went after images and video. It returned
**two cards and a fully quantified equipment system**.

---

## 1. The bottom line

| | cards | monsters |
|---|---|---|
| rows in the catalogue | 121 | 22 |
| with **any** recovered numeric stat | **3** (`051`, `010_1`, `010` partial) | **0** |
| with a **complete** stat line | **1** (`051`, 13 stats) | **0** |
| fully qualified with level | **2** | **0** |

Per-file:

| file | what is in it |
|---|---|
| [`051.md`](051.md) | Beckhen — **complete 13-stat line at Lv.30**, plus the exact equipment delta. The single most useful result of the round. |
| [`010_1.md`](010_1.md) | Vincent awakened — Strength/HP/ATK/DEF at Lv.30. Plus the HP:ATK:DEF ratio finding. |
| [`010.md`](010.md) | Vincent — one armour's DEF at Lv.49/50 and the Strength delta. Plus an unidentified orphan card. |
| [`GEAR.md`](../../equipment/GEAR.md) | The equipment system: main stats per slot at level cap, six Lv.15 jewel-panel samples, 12 jewel set bonuses, upgrade costs. |
| [`found/`](found) | The 17 source images. |

**Monsters: still exactly zero, and I now think that is structural, not a gap in
searching.** See §4.

### 2026-10-05 follow-up — archived Japanese hunter database

Wayback captures of the 2019 Japanese hunter database add complete 13-field
`基本能力値` tables for Lapis (`017`), Hermes (`023`), and Heidi (`044`), plus an independent
Beckhen (`051`) stat line. The pages give rarity-on-draw but print no level and
do not establish equipment state; the new rows are preserved in
[`analysis/research/base-stats-visual-hunt/archived-hunter-database-2019.md`](../../../findings/hunters/base-stats-visual-hunt/archived-hunter-database-2019.md).
Strict coverage remains **1/113** identified heroes because Lapis, Hermes, and Heidi's
level/gear context is missing. Treat their numbers as raw basic-stat anchors,
not as verified level-1 values until the archive's schema is corroborated.

The archive-index harvest extends this raw pool: 62 complete numeric profiles
crosswalk to 62 catalog IDs, of which 58 add candidate IDs beyond the four
previously documented candidates. The capture also has one placeholder profile.
All readings, crosswalk evidence, and exact URLs are in
[`archived-hunter-database-2019.tsv`](../../../findings/hunters/base-stats-visual-hunt/archived-hunter-database-2019.tsv).
These remain source-backed basic-ability readings with unknown level and gear
state; they do not change the round-2 image counts or strict coverage.

---

## 2. What was installed

Into the project venv `tools/python-venv` (Python 3.12.10):

- `pillow` **12.3.0** — image decode / crop / upscale
- `pytesseract` — Python wrapper
- `yt-dlp` **2026.08.19** — video discovery + download

Plus two system-level binaries, both of which were already present:

- **Tesseract OCR 5.4.0.20240606** — installed with
  `winget install UB-Mannheim.TesseractOCR` to `C:\Program Files\Tesseract-OCR`.
  This is a **system-wide install**, not a local dir. The Python wrapper alone
  does nothing without this binary.
- **ffmpeg** — already at `%LOCALAPPDATA%\Microsoft\WinGet\Links\ffmpeg.exe`
  (pre-existing, not installed by me).

Validation: OCR of `faq-image18` reproduced **every one of the 23 numbers** on that
screen at `--psm 4`/`--psm 6`. It also misread `33.00` as `"e .00"` and `61815`
(another image) as `671815` — so OCR was used to **triage and cross-check**, and
every reported figure was additionally **read by eye at 2–5x zoom**. Nothing here
rests on OCR alone.

---

## 3. What was searched, and what each vector paid

### Vector 1 — the community FAQ's embedded screenshots. **This is where everything came from.**

`recovered-assets/community-notes-2026-09-30/Blustone Guide FAQ.md` is 13 MB and
contains **27 base64 PNGs** of real in-game screens. Round 1 correctly declined to
read numbers off them but recorded them as unread.

**The reason round 1 got zero from this file is a parsing bug, not an absence of
data.** The FAQ stores images as *reference-style* markdown — `![][imageN]` with the
data URIs in `[imageN]: <data:image/png;base64,…>` definitions at the **end** of the
file. An inline `!\[...\]\(data:image/...\)` regex matches **0 of 27**. Once
extracted with the right pattern, 6 of the 27 are stat screens.

`catalogue-report.md` §10 step 7 ("OCR the FAQ's stat screenshots") was the correct
next step and it was right. Vector 1: **paid off completely.**

| image | content |
|---|---|
| 5 | card `010_1` Vincent awakened — **card stat screen** |
| 7 | card `010` Vincent — equipment screen (EN) |
| 8 | unidentified card — equipment screen (KO) |
| 16 | card `051` Beckhen — **card page, Lv.30, 3★** |
| 17, 18 | card `051` — **full 13-stat line**, general + detail |
| 19, 20, 21 | Beckhen's weapon / armour / accessory at Lv.50 — **main stat values** |
| 22–27 | six jewel panels at Lv.15 — **sub-stat values** |
| 10, 11 | jewel set-bonus list (12 families, including Offensive Jewel) |

The remaining images are loot tables (1–4), the mileage ladder (6), gem-type lists
(9–11), a guild screen (12–13) and skin galleries (14–15) — no stats.

### Vector 2 — miraheze wiki images. **Zero. Confirmed exhaustively.**
All **881** images enumerated via `action=query&list=allimages` (paginated).
Composition: 96 `Portrait_*`, 96 `Icon_*`, and 689 emotion sprites
(`*_Angry / _Idle / _Joy / _Sad / _Shock`) plus `CG_*`. A regex for
`stat|table|tier|chart|graph|power|level|balance|screen|data` over all 881 names
returns **0 hits**. The wiki publishes no stat graphics.

### Vector 3 — YouTube frame extraction + OCR. **Zero, across 4 videos / ~1,400 frames.**
Pipeline: `ytsearch` → `yt-dlp` download ≤720p → `ffmpeg fps=1/2` → Tesseract
`--psm 4` per frame → rank frames by numeric density + stat keyword density.

| video | frames | result |
|---|---|---|
| `qtXrVbFQ9fA` *Become a Legendary Captain!* | 434 | 2 hits, both a player-profile screen. No stats. |
| `pXWN5m0yqOo` *Awakened Power Genovia & Capitan* | 322 | 0 hits — pure combat, buff/debuff text only |
| `i1YTS0KL8Ps` *tracing Diana and Bear* | 121 | 0 hits — recruiting screens |
| `cnMBlXFd5W4` *20+ Hunters Recruiting* | 537 | 3 hits — gacha/mileage screens |

Note the **search-space problem**: "blustone" is swamped by *Bluestone* (the LoL
item, Minecraft, Dokkan, Smite). "블루스톤 능력치" returns Solo Leveling, Blue Lock
and Bloodborne. Finding real Blustone videos needs the exact title vocabulary.

Combat frames *do* show transient HP over units (e.g. `3612`, `8203`, `3133`,
`5649`, `4900`) and a battle timer (`TIME LEFT 82.52`). **Neither is usable**: a
mid-fight HP value has no monster identity, no level and no max, and the timer is
already recovered as `play_time` from `LEVELING.jet`.

### Vector 4 — documents / spreadsheets. **Zero.**
Google Sheets tier list was already **410 Gone** in round 1. Fandom is 403 and
near-empty. namu.wiki 403. No new host surfaced.

---

## 4. Why monsters are still zero — and why that is now a *fact*, not a failure

I checked the one vector I had not: **monster HP is drawn on screen during
combat.** It exists — but every frame carrying it is a **transient current-HP
value with no monster id, no level and no maximum**, so it cannot populate
`/reference/GetMonster`. There is no screen in this game that shows a monster's
*base* stats, which is consistent with `catalogue-report.md` §5: monster data is
**server-authoritative** and never shipped in the APK.

**Monsters remain unrecoverable in principle from any public source.** The only
thing that would yield them is a captured original-server response, and there is
none. The server must keep synthesising them — correctly labelled, exactly as
`INDEX.md` §7.2 already says. **Do not let a future agent re-run this sweep hoping
for a different answer.**

---

## 5. Are stats per-card or curve-derived? — the honest answer

**Undetermined, and two points cannot settle it.** What the two cards do show:

Both are **Offense / Ice at Lv.30**, so `LEVELING.jet`'s role multipliers cancel:

| | `051` 3★ | `010_1` 5★ awakened | ratio |
|---|---|---|---|
| HP | 2879 | 4980 | 1.730 |
| ATK | 1471 | 2634 | 1.791 |
| DEF | 1149 | 1992 | 1.734 |
| Strength | 24068 | 61815 | **2.568** |

- **HP/ATK/DEF scale by a near-constant scalar** (3.5% spread, consistent with
  rounding). That is weak evidence for a **single per-card scalar over a common
  shape** — i.e. one number per card rather than three independent ones.
  [DERIVED, n=2]
- **Strength does not follow that scalar.** It weights rarity and/or skill level
  separately — and Vincent's skills are 50/50 while Beckhen's are unknown, so skill
  level is an unresolved confound. **[UNKNOWN]**

**Practical read for the server:** a per-card table is *not* contradicted by
anything, and a curve is not established. Two Lv.30 points cannot separate
rarity, level curve and skill level. The honest position is that **the curve is
unrecovered**, `051` is a real anchor to calibrate any invented curve against, and
`010_1`'s 61815 must **not** be reproduced by an HP/ATK/DEF-derived formula.

---

## 6. Coverage table

| entity | file | stats recovered | level | confidence |
|---|---|---|---|---|
| `051` Beckhen | [051.md](051.md) | **all 13** + gear delta | Lv.30 | [OCR-CONFIDENT] |
| `010_1` Vincent (Awakened) | [010_1.md](010_1.md) | 4 of 13 | Lv.30 | [OCR-CONFIDENT] |
| `010` Vincent | [010.md](010.md) | armour DEF only | Lv.49/50 | [OCR-CONFIDENT] |
| *(unidentified)* | [010.md](010.md) | 5 of 13 | **[UNKNOWN]** | identity [OCR-UNCERTAIN] |
| equipment system | [GEAR.md](../../equipment/GEAR.md) | main stats @cap, 6 jewel-panel samples, 12 set-bonus families, costs | Lv.50 / Lv.15 | [OCR-CONFIDENT] |
| remaining **118** cards | — | 0 | — | [UNKNOWN] |
| all **22** monsters | — | 0 | — | [UNKNOWN] |

Denominator: 121 card rows, 22 monsters. **Cards with stats: 3/121 (2.5%).
Monsters: 0/22.**

---

## 7. Global findings that are not per-entity

1. **Base Attacking Speed is 8.00 on two different cards** → plausibly a
   game-wide constant. [DERIVED, n=2]
2. **Equipment contributes the large majority of a maxed card's stats.** At
   Lv.50/50/50 + Lv.15 jewels, gear adds +437 HP / +317 ATK / +154 DEF to a base of
   2879 / 1471 / 1149 — roughly **13% / 22% / 13%**. Base stats therefore dominate,
   so getting them approximately right matters more than getting gear right.
3. **Strength is not derivable from HP/ATK/DEF** (§5).
4. **`LEVELING.jet` chunk 19's `power` column is NOT the on-screen "Strength".**
   Beckhen 3★ Lv.30: chunk 19 says `31200`, screen says `30359` geared /
   `24068` nude. Vincent 5★ awakened Lv.30: chunk 19's nearest is `660000`
   (rank 5, hyper 3), screen says `61815` — off by ~10x. **Do not wire chunk 19's
   `power` into a Strength field.** [DERIVED]
5. **Every figure is a 2018–2019 era snapshot** (the FAQ dates itself against
   patch 2.0.5.0 and 22/12/2018). May be pre- or post-balance versus 2.8.0.1.

---

## 8. What I would try next

Ranked by expected value. The first is the only one with real upside.

1. **Mine more player-generated Korean/English guides of the same species as the
   FAQ.** That file was 13 MB of screenshots wrapped in a terse English guide, and
   it held *every* numeric thing in the whole offline corpus. Its author credits
   individual players ("Photo by: Vinh-Diesel", "Photo by Taebin/Kitemoon") —
   **those names are a lead.** Search Naver cafes / Naver blog / Tistory / Inven
   / DCInside for guides by those users, and for the same *style* of writeup.
   Any one of them with 6 stat screens beats everything else in this document.
2. **Inven / DCInside gallery images** for character builds — never OCR'd, and
   Korean communities post stat screenshots as routine. Needs an image-capable path
   since text search returns nothing.
3. **Long-form YouTube *build/guide* content, not gameplay.** 4 gameplay videos
   produced nothing; the hit rate depends on the video containing a card detail
   page. Search by **exact** title vocabulary (`블루스톤` + `장비`/`각성`/`빌드`)
   and prefer channels that do gear guides. Low yield, high cost — I would not
   spend more than ~2 more videos on it.
4. **Nothing else.** Do not re-sweep namu (403), Fandom (403, and demonstrably
   wrong — see `catalogue-report.md` §8), the local LevelDB, or the `.jet` packages.
   Those are exhausted and independently confirmed exhausted.

---

## 9. Reproduction

The FAQ images are recoverable with no tooling beyond Python's stdlib:

```python
# 27 images; an inline ![][data:...] regex matches ZERO of them.
defpat = re.compile(r"^\[(image\d+)\]:\s*<data:image/(\w+);base64,([^>]+?)>\s*$", re.M)
```

Filenames in `found/` record the FAQ's own `imageN` ids and what each one turned
out to be, so the mapping back to the source file is unambiguous.
