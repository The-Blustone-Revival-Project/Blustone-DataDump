# Hero stat-panel / level extraction — Wayback `blustone.jp` official-guide screenshots (2026-10-06)

**Lane goal.** Find a photograph of a Blustone hero stat panel such that the **same
hero appears at two or more displayed levels**, and classify every reading as
gear-free / buffed / unknown **by what is visibly in the image**, never by its
label.

**Answer in one line.** A previously unmined Wayback corpus of **180 recovered
`blustone.jp` official-guide screenshots** (2018-11 … 2019-03, all **pre** the
2019-09-05 rebalance) was recovered and pixel-inspected; it contains **level-stated
per-hero readings that the project did not have**, and **two independent
within-image grade transitions whose factors agree to 1.1 %** — which yields a
**one-sided upper bound on the Lv.1→Lv.30 growth of 戦闘力** that is *inconsistent*
with reading Beckhen's `1.7157` core-stat ratio as a level factor — **but it
contains zero HP/ATK/DEF stat panels and zero gear-free readings, and no
unconfounded same-hero two-level pair.**

## Files touched

- **New, this lane only:** this file.
- **New images:** `hero-panel-level-images-2026-10-06/` — **180 recovered image
  files** (133 jpg, 31 png, 16 jpeg), **20,366,951 bytes**, plus 46 working
  artefacts kept alongside them (**21 labelled contact sheets** and **25 zoom
  crops**, all `_`-prefixed). `_manifest.json` records url / capture ts / bytes /
  sha256 / pixel size / status for **377 attempted rows**.
- **New helper scripts:** `_tools/panel_control.py`, `_tools/panel_fetch_images.py`,
  `_tools/panel_fetch_priority.py`, `_tools/panel_scan_pages.py`,
  `_tools/panel_image_map.py`, `_tools/show_page.py`, `_tools/crop.py`,
  `_tools/montage.py`.
- **Read only:** `_archives_work/` (cached pages + CDX census), `_wf1_cache/`,
  `_swipe/`, `analysis/research/*.md`.
- **NOT touched:** `polluted-observations.md` (parent mirrors), `coverage.md`,
  every TSV, `server-ts`, fixtures, seeds, APK, emulator, phone, Ghidra.

---

## 1. Positive controls (run before any negative is recorded)

Trap compliance per the lane brief: **`http://` used throughout** (`https://` also
answered here, but was not relied on); **no CDX/availability API was used to
decide existence** — every fetch was an exact-URL `/web/<ts>id_/<original>` form
built from the *referencing page's own capture timestamp*; the 3,357-byte parking
page was size-rejected.

| # | control | result |
|---|---|---|
| C1 | `http://web.archive.org/` | 200, 145,187 B — **PASS** |
| C2 | known image `…/2018/11/rankup.jpg` @ `20190403182150id_` | 200, 201,302 B, JPEG signature — **PASS** |
| C3 | **known hero `051` Beckhen profile**, exact URL | 200, 35,832 B; markers `8709`, `1678`, `864`, `660` all present — **PASS** |
| C4 | full-size `0d40a5e4….jpg` at 13 guessed sibling names | 0/13 — **negative, with C1–C3 green**; see §7 |

**C3 is the required read-path validation**: the known hero reproduces before any
new page was believed.

**A second, in-corpus control also passed and is stronger than C3 for the reading
method**: Bear `036` reads **戦闘力 2326 at ★3 Lv.1** on **four independent
surfaces** in three separate images — three Hunter-List rows (`capa1`), the
Member-Training panel (`capa1` right half), the Capacity-Transcendence target
(`capa2`) and the transcended material row (`capa2`). **4/4 exact, 0 mismatch.**
Whatever the corpus's numbers mean, they are reproducible.

---

## 2. What the corpus is

| item | value |
|---|---|
| cached host pages reused | 215 `blustone.jp/archives/<id>` pages (already local) |
| distinct image URLs referenced by those pages | 452 |
| attempted this pass | 377 manifest rows — 155 ok, 222 not recovered at the tried timestamps |
| **image files on disk** | **180** (133 jpg, 31 png, 16 jpeg), **20.37 MB** |
| triaged | **all 180**, via 21 labelled contact sheets plus 25 targeted zoom crops |
| capture era | 2018-11 … 2019-03 — **all pre-2019-09-05 rebalance** |
| value | `level-factor-test-2026-10-05.md` §2.6 item 5 asked for exactly this era as a control; it exists and is now mined |

Corpus by article subject: 育成論/ランクアップ (rank-up), 育成論/トレーニング
(training), 育成論/キャパ超越 (capacity transcendence), 施設紹介/装備強化
(equipment), 施設紹介/ジム (gym), ファイトクラブ (fight club), マーケット,
推荐的ハンター紹介, ハンター図鑑, イベント banners.

**Not a stat-panel source.** The site is a *mechanics guide*: its screenshots are
UI navigation, market grids, mission results, character art and event banners. Of
180 images triaged:

- **0** show an HP/ATK/DEF stat table.
- The 詳細情報 (*Detailed Information*) hunter screen appears at least 6× — for
  **Bear `036`**, **Pansy `057`**, **Calibur `053`**, **Therapy `050`**, and
  **Beckhen `051`** — and in every case the stat block sits behind an un-tapped
  icon in the bottom row. **The popup was never captured.** That single missing
  screenshot class is the whole gap.

---

## 3. The critical discriminator — and why it is *not* satisfiable here

The brief's rule: **gear-free is certified only by visibly empty equipment
slots**, never by a `기본 능력치` / `基本能力値` heading.

**No image in this corpus shows equipment slots at all.** The three screen classes
that carry level-stated numbers are:

| screen class | equipment slots visible? | ⇒ gear state |
|---|---|---|
| ハンター名簿 / Hunter List (`rank1`, `capa1`) | no | **UNKNOWN** |
| メンバートレーニング / Capacity Transcendence / Rank-Up (`rank1/2`, `capa1/2`, `0d40a5e4…-1`) | no | **UNKNOWN** |
| 装備強化 / Equipment Enhancement (`equip1`, `1551430697`, `1551433025`, `1551427143`, Heidi sibling frame) | **yes, 3 slots, all populated** | **CONTAMINATED** |

So this pass yields **zero gear-free readings**. The only two frames where gear
state is *determinate* are the **populated** ones — i.e. determinately
contaminated. Recorded as such and used for nothing.

**Buff check.** The client applies `FIGHTCLUB_BOUNS` +10 % and `BLITZ_TEAM_BONUS`
+10 % to the same pool, so any reading taken in a Fight Club / Guild Blitz /
battle-party context is suspect. One such frame exists —
`1550474475-1024x911.jpg`, バトル準備, **味方メンバー 4135 VS 相手メンバー 7777**
with per-hero Lv badges — and it is **explicitly excluded from every ratio in this
note**. All readings used below come from Hunter-List, Member-Training,
Transcendence and Rank-Up screens, which are not buff contexts.

---

## 4. Panels found — full record

Levels and 戦闘力 tokens were read at 2.2× and then at 12–16× on the badge pill
(see §6, **a misreading was caught and corrected**). Identity is name-based where a
Japanese hero name is on screen, matched verbatim against
`archived-hunter-database-2019.tsv`.

### 4.1 `rank2-1024x911.jpg` — Rank-Up Success, **Kain `029`** ★3→★4

| | before | after |
|---|---|---|
| title rank | ミドルハンター (Middle Hunter) | アドバンスハンター (Advance Hunter) |
| grade badge | ★3, yellow ring | ★4, green ring |
| **level badge** | **Lv.MAX** | **Lv. 1** |
| **戦闘力** | **3311** | **4907** |
| panel | collapsed hero header (portrait + name row) | same, side by side |

- Identity: **name on screen** in the sibling frame `rank1-1024x911.jpg` —
  鋼のボディガード「カイン」; matches TSV `029` (rarity-on-draw 3, 守備手/電撃)
  verbatim, and the panel's type/element icons are the shield/lightning pair.
- Layout: collapsed 5-row block, **not** the `Details`-expanded
  `Character Attributes` table.
- Gear state: **UNKNOWN** (no equipment UI in frame).
- Buff: not a buff context.
- **Ratio ×1.482030.**
- **Cross-frame identity confirmation:** `rank1`'s Hunter List row for the same
  art reads **Lv.MAX / 3311**, matching the "before" panel exactly.

### 4.2 `0d40a5e4a645fc6b96e767d64ac0878e-1-1024x904.jpg` — Rank-Up Review, **unidentified blonde child hero** ★3→★4

| | before | after |
|---|---|---|
| grade badge | ★3, yellow ring | ★4, green ring |
| **level badge** | **Lv.MAX** | **Lv. 1** |
| **戦闘力** | **2554** | **3827** |

- Identity: **NOT ASSIGNED.** No name in frame; art only.
- Layout: collapsed 5-row block.
- Gear state: **UNKNOWN**.
- Buff: not a buff context.
- **Ratio ×1.498434.** Materials consumed are shown as a row of Lv.1 heroes; the
  Japanese text states the consumed hunters leave Rank Battle.

### 4.3 `capa2-1024x911.jpg` — Hunter Capacity Transcendence, **Bear `036`** ★3 Lv.1

- ハンターキャパ超越, target **大自然の贈り物「クマ」** (matches TSV `036`
  verbatim; 守備手/電撃 matches the shield/lightning icons).
- Target badge **★3, Lv. 1**; **戦闘力 2326 → 2704**.
- Material: a second **Bear `036`**, **★3 Lv. 1, 戦闘力 2326**, selected 1/1.
  On-screen rule: only same-hero ★3+ may be used as material.
- Cost 9,000 gold; item counters 9/9 and 449/90.
- Identity: name on screen. Layout: collapsed 5-row block.
- Gear state: **UNKNOWN**. Buff: not a buff context.
- **Ratio ×1.162511** — a same-state (level and grade both fixed) change.

### 4.4 `capa1-1024x911.jpg` right half — Member Training, **Bear `036`** ★3 Lv.1

- Name prudently confirmed as 大自然の贈り物「クマ」; **戦闘力 2326**;
  badge **★3 / Lv. 1** (read twice, 2.2× and 12×); rank title ミドルハンター.
- Gear state **UNKNOWN**. Buff: not a buff context.
- Bottom icon row present (the un-tapped stat/skill toggles) but no panel open.

### 4.5 `rank1-1024x911.jpg` right half — Member Training, **Kain `029`** ★3 Lv.MAX

- 鋼のボディガード「カイン」, 戦闘力 **3311**, badge **★3 / Lv.MAX**, label
  **Lv. 30**, ミドルハンター. Gear state **UNKNOWN**.

### 4.6 `rank1-1024x911.jpg` / `capa1-1024x911.jpg` left halves — Hunter List (ハンター名簿), sorted 戦闘力順

The JP Hunter List **does carry a per-hero `Lv.` badge**, a 戦闘力 token and a
state label (探索中 / 代表中 / 防御中 / ロック / 蜃気樓 / 攻撃中 / リーダー).
Identities are portrait-only ⇒ **no IDs assigned** except where a row is
corroborated by a named panel in the same image.

| `rank1` (93/60) | `capa1` (63/60) |
|---|---|
| **Lv. 21** → 5568 攻撃中 | Lv. 1 → 2434 |
| **Lv.MAX** → 3311 攻撃中 (Kain `029`, named) | Lv. 1 → 2348 |
| **Lv. 25** → 2622 リーダー | **Lv. 1** → 2326 (**Bear `036`**) |
| Lv. 1 → 2434 | **Lv. 1** → 2326 (**Bear `036`**) |
| Lv. 1 → 2348 | **Lv. 1** → 2326 (**Bear `036`**) |
| **Lv. 1** → 2326 (**Bear `036`**) | **Lv. 14** → 2283 攻撃中 |
| **Lv. 1** → 2326 (**Bear `036`**) | Lv. 1 → 2197 攻撃中 |
| **Lv. 1** → 2326 (**Bear `036`**) | Lv. 1 → 2156 |
| **Lv. 14** → 2283 攻撃中 | Lv. 1 → 2123 |
| Lv. 1 → 2197 攻撃中 | Lv. 1 → 2028 |
| Lv. 1 → 2156 | Lv. 1 → 2018 |
| Lv. 1 → 2123 | Lv. 1 → 1999 |
| Lv. 1 · Lv. 1 · Lv. 1 (below fold) | Lv. 1 · Lv. 1 (below fold) |

The **nine overlapping tokens are byte-identical and carry identical Lv badges in
both lists** (`Lv.1 ×8`, `Lv.14 ×1`). `rank1` adds three heroes above the overlap
(5568 / 3311 / 2822); `capa1` shows three more below it that simply fall below
`rank1`'s fold. Gear state **UNKNOWN** for every row; not a buff context.

### 4.7 `0d40a5e4a645fc6b96e767d64ac0878e-1024x911.jpg` — Member Training, **Heidi `044`** ★4 Lv.7 — **GEAR-CONTAMINATED**

- **2つの顔を持つ少女「ハイディ」** (matches TSV `044` verbatim; 攻撃手/火炎),
  badge ★4, **Lv. 7** (read at 2.2× and again at 12×), **戦闘力 6228**,
  アドバンスハンター.
- **The sibling frame in the same image is an 装備強化 screen showing this hero's
  three equipment slots populated at Lv.6 / Lv.7 / Lv.9.** ⇒ **determinately
  gear-contaminated**, exactly as the brief's discriminator requires. Excluded
  from every ratio.

### 4.8 `equip1-1024x911.jpg` — Equipment Enhancement — **GEAR-CONTAMINATED**

- Three slots populated at **Lv.10 / Lv.5 / Lv.5**; the altered item shows
  特徴 261 → 264 → 274 and the hero's **戦闘力 6607 → 6634 → 6643**.
- Establishes that equipment operations move 戦闘力 directly, i.e. any frame
  adjacent to a populated forge screen is contaminated. Identity **not asserted**
  (no name legible at available resolution).

### 4.9 `0d40a5e4a645fc6b96e767d64ac0878e-5-1024x879.jpg` — Member Training, **Kain `029`** ★5 **Lv. 1**

- マスターハンター, badge **★5** (five gold stars), pill **"Lv. 1"** — read at 5×
  then at **16×**, where the pill's rounded right edge falls immediately after
  the digit, so this is genuinely a one-digit level and not a clipped `Lv. 17`.
- **戦闘力 13148**. Gear state **UNKNOWN**.
- **This reading is internally irreconcilable with §4.1/§4.5** (same hero, same
  family, ★5 Lv.1 at 13,148 vs ★3 Lv.30 at 3,311) and is **excluded from all
  arithmetic**. Recorded because it is a genuine level-stated reading, and because
  its incompatibility is itself the finding in §5.3.

### 4.10 `traning.png` — English client, training result

- "Master Hunter", badge **Lv. 17** (initially misread as `Lv. 1`; corrected at 6×
  — see §6), **Power 9387 → 9473**.
- Gear state **UNKNOWN**. Identity: title only ⇒ **not assigned** (the English
  "Master Hunter" title is the localisation of マスターハンター, i.e. consistent
  with `029`, but the art is not legible at this file's native 300×200 and no ID is
  claimed).

### 4.11 `1547531314-1024x911.jpg` — Kain `029` skill training

- 鏡のボディガード (Kain), **skill 1 at Lv. 40/50**, **属性抵抗 16.00 % → 16.40 %**
  for one training tick; 銀のボディガード gallery row **35022**. Gear state
  **UNKNOWN**. Substat-skill magnitude, **not** a character stat.

### 4.12 `1da12b328f9011d02f402d248a2d8025.jpg` — Detailed Information, **Beckhen `051`** ★5, no numbers

- **ファイトクラブの守護者 ベッケン** — matches TSV `051` verbatim, including the
  ★5-only ability named in the blustone.jp Beckhen article
  (「★5まで育成できれば『ファイトクラブの守護者』の効果により…」).
- **A rare ★5 Beckhen frame, but it is a transition frame: no Lv badge, no 戦闘力,
  no stat block.** Identity recorded; **no numeric reading**. Gear state **UNKNOWN**.

### 4.13 `d73e1de33700c1b5129171acbd78ef1f.jpg` — recruitment banner, **Erise `063`** ★4 **Lv. 1**

- "NEW ★4ハンター**エリーズ**を捕まえろ!", bonus chibi badge **Lv. 1**; matches TSV
  `063` 一流仕立て屋「エリーズ」, rarity-on-draw 4.
- Identity + level only; **no 戦闘力, no stat panel**. Gear state **UNKNOWN**.
  A freshly drawn hunter is *plausibly* gear-free, but **nothing is visibly shown**,
  so per the brief this is **UNKNOWN**, not gear-free.

### 4.14 `IMG_5729.png` / `IMG_5729-e1548139622568.png` — a **three-point grade ladder for one hero**, third point numberless

- Same blonde fox/cat-eared hero as §4.2 (identical art, identical element icon —
  orange hand / lightning, identical gold figure **39554**).
- **Before: ★4** glyph (2+2 white stars, green ring), **Lv.MAX**.
  **After: ★5** glyph (4 small + 1 large centre blue star, blue ring), **Lv. 1**.
- So this hero's ladder is **★3/Lv.MAX → ★4/Lv.1 → ★5/Lv.MAX → ★5/Lv.1** — i.e.
  **all three grade steps are present, every one resets the level to Lv.1, and the
  ★4→★5 step is the one pair that shares a level with no grade/level confound
  except the grade itself.**
- **No 戦闘力 is shown.** Both files are crops that terminate at the badge row
  (750×389 and 650×365), so the ★4→★5 ratio **cannot be measured** and the
  grade ladder stays open. Recorded because it identifies the exact frame that
  would close the ladder: the un-cropped ★4→★5 rank-up result.
- Gear state **UNKNOWN**.

### 4.15 `IMG_4930.png` — equipment-instance levels (jewel/equipment lane, no stats)

- A three-slot equipment/crystal mount screen showing the instance levels
  **Lv. 45** (weapon), **Lv. 25** (blue coat = armour), **Lv. 11** (blue cap =
  accessory), each with an element badge.
- This is the **first equipment-instance level reading** located in this project,
  but it carries **no stat values**, so it earns **no accessory coverage**. Noted
  for the equipment lane only. Gear state: slots **populated** ⇒ contaminated for
  any hero-stat purpose.

### 4.16 Screens deliberately excluded

- `1550474475-1024x911.jpg` — バトル準備, 味方 4135 VS 相手 7777 with Lv badges.
  **Fight Club context ⇒ possible `FIGHTCLUB_BOUNS` +10 %.** Flagged contaminated
  by context; no token used.
- `1547531476-1024x911.jpg` — stage-clear party panel, チームレベル8, team member
  tokens 2698 / 6070 / 5275 / 2416, **no levels shown**.
- `855837456…jpeg` — player profile card, 戦闘力 38287, Rank 825. Player, not hero.
- `154753…`/`155020…`/`155047…`/`155108…` galleries: market grids, mission lists,
  supply bonus, banners, story/episodes, map screenshots. No stat panels.

---

## 5. Does any hero appear at two or more levels?

### 5.1 Direct answer

**Yes — two heroes move between levels inside this corpus, and in both cases the
level change is inseparably confounded with a ★3→★4 grade change. There is no
unconfounded same-hero two-level pair.**

| hero | levels seen | confounded? |
|---|---|---|
| `029` Kain | Lv.30 (Lv.MAX) @ 3311 → Lv.1 @ 4907 (§4.1) | **yes**, ★3→★4 in the same frame |
| unidentified blonde child hero | Lv.MAX @ 2554 → Lv.1 @ 3827 (§4.2) | **yes**, ★3→★4 in the same frame |
| `029` Kain (2nd account) | Lv.1 @ 13148 (§4.9) | excluded, irreconcilable (§5.3) |
| `036` Bear | Lv.1 only — 2326 on 4 surfaces + 2704 transcended | n/a, **single level** |
| `044` Heidi | Lv.7 only, gear-contaminated | n/a |
| `051` Beckhen | ★5 frame with **no level shown** | n/a |

**And a real client behaviour fell out of it:** rank-up in this client **resets
the hunter to Lv. 1**. Both rank-up frames show `Lv.MAX → Lv. 1` inside the
成功/審査 screen, which matches the guide's own instruction
(「ランクアップさせたいハンターのレベルをMAXにする」) and is a visual
confirmation of the RankUp contract's EXP reset. Recorded here because it was
found as a by-product; it belongs to the server lane, not to stat recovery.

### 5.2 What the two confounded pairs *do* yield — a real bound

Both rank-up frames are the **same transition**: ★3 @ Lv.MAX(30) → ★4 @ Lv.1.
Write `f` for the grade factor and `g` for the per-level compound on 戦闘力:

```
f(★3→★4) × g²⁹  =  observed ratio
```

| hero | before → after | ratio |
|---|---|---|
| `029` Kain | 3311 → 4907 | **1.482030** |
| unidentified blonde child | 2554 → 3827 | **1.498434** |
| mean | | **1.490232** |
| spread | | **1.10 %** |

Two different heroes, two different images, the same transition, agreeing to
**1.1 %** — well inside the ±0.14 % worst-case rounding noise implied by a
4-digit integer. **The reading method is sound.**

Because a grade increase cannot lower a card's power (`f ≥ 1`):

> **g²⁹ ≤ 1.482030**, i.e. the whole **Lv.1→Lv.30 growth of 戦闘力 is at most
> ×1.482**, a per-level compound of at most **1.013658**.

Beckhen's core-stat archive→Lv.30 ratio is **1.715733** (per-level **1.018790**),
which is **1.16× larger than this bound**. So:

> **If 戦闘力 tracked the core-stat level factor, a ★3→★4 rank-up at Lv.MAX could
> not lift 戦闘力 by only ×1.48 while dropping 29 levels.** Either 戦闘力 does not
> follow the core-stat level factor, or `f` is not ≥1 as assumed, or the level does
> not behave as read. **This is a genuine test result, not a null** — but it bounds
> 戦闘力, *not* HP/ATK/DEF, and it therefore does **not** by itself retire the
> Beckhen 1.7157 puzzle.

**Do not implement a per-level factor from this.** It is an inequality on a
different quantity.

### 5.3 戦闘力 is **not** comparable to the archive's 戦闘力 — do not ratio them

| hero | archive 戦闘力 (TSV) | in-game 戦闘力 | ratio | state |
|---|---:|---:|---:|---|
| `036` Bear | 10,011 | 2,326 | **0.2323** | ★3 Lv.1, gear unknown |
| `029` Kain | 10,229 | 3,311 | **0.3237** | ★3 Lv.30, gear unknown |
| `044` Heidi | 9,764 | 6,228 | **0.6379** | ★4 Lv.7, **3 slots populated** |
| `048`-class | 9,322 | 6,607 | **0.7088** | **3 slots populated** |

The archive's four `戦闘力` values sit within **4.7 %** of one another (9,764 –
10,229) while the in-game readings for the *same heroes* span **0.2323 – 0.7088**,
a factor of **3.05**. The two columns therefore are **not** the same quantity, and
**no ratio between them is licensed.** This is the direct reason §5.2's bound
cannot be promoted into the Beckhen question.

### 5.4 A within-list observation that argues against a large level effect on 戦闘力

In the single `rank1` Hunter List:

- eight **Lv.1** heroes read 2123 … 2434 — a **14.65 %** spread from hero identity
  alone, at a single fixed level and grade class;
- one **Lv.14** hero reads **2283**, which lies **inside** that Lv.1 band;
- one **Lv.21** hero reads 5568 and one **Lv.MAX** hero 3311.

So across Lv.1→Lv.14 the level contribution is **smaller than the between-hero
spread at fixed level**. This is confounded by identity and by the fact that the
high-level heroes are almost certainly higher-grade, but it points the same way as
§5.2, from independent data.

---

## 6. A misreading I made and corrected — recorded because it is a trap

I first read the badge pill in `traning.png` as **"Lv. 1"**. At 6× it is plainly
**"Lv. 17"**; the `7` had been swallowed by the pill's right edge at 1×. That is a
demonstrated, caught error of the exact class this lane must avoid.

**Open question on the `snA*` labels — recorded, not resolved.** I attempted the
same check on `snA223-83e098e1.jpg` (the Bahamut roster whose labels
`bahamut-thumb-2026-10-05.md` §3 records as `5284代表(Lv11) | 4500防禦中(Lv11) |
2599探險中(Lv12)`). Zoom crop saved as
`hero-panel-level-images-2026-10-06/_zoom_sna223_levels.png` (10× on the `5284`
row). At that magnification both glyphs carry a **full horizontal top bar and a
diagonal descender**, which reads as `7 7` rather than `1 1` — but the source file
is only **428×762**, and in this font the `1` flag can imitate that at 10× nearest-
neighbour blow-up. **I cannot separate `77` from `11` on this image and therefore
do not assert the prior transcription is wrong.** What is asserted is weaker and
still actionable: **that file's level labels are not resolvable at its native
resolution and must be re-verified against a better source before any of them is
reused.** That image is a single unlabeled rating token per portrait anyway and
earns no coverage either way. I have not edited `polluted-observations.md`.

**Method rule this pass:** the WordPress `-1024x911` variants are downscaled from
≈1920 px captures; **no level or 4-digit token in this corpus is trustworthy below
12× magnification**, and the pill's rounded right edge must be checked for
truncation. `_tools/crop.py` exists for exactly this. Every level and 戦闘力 value
in §4 was read at 2.2× **and then re-read at 12–16×**; the one value that changed
on re-read is flagged in §4.10.

---

## 7. Searched and yielded nothing (all with controls green)

| searched | result | control |
|---|---|---|
| 452 distinct image URLs across all 215 cached `blustone.jp/archives/` pages | **180 recovered and all 180 triaged**; 222 manifest rows not recovered at the tried timestamps | C1–C3 |
| full-size originals of the `0d40a5e4…` resize family (13 sibling names + bare) | **0/14** | C2 green ⇒ genuine non-capture at tried timestamps, **not** "no full size exists" |
| `1548136677 / 1548137184 / 1548138716 / rank3.jpg` (the ★5 growth article's own attachments, incl. `-1024x911`) | 0/4 | C2 green |
| `1542365712/5835/5925/6108/6153/6172/6194/6264` (8 育成論 300×267 thumbnails), `d.jpg`, `gim1/gim2`, `traning1/2`, `capa2.jpg`, `gingan-300x296` | 0/13 | C2 green |
| `archives/2541` = **the Beckhen `051` + Harry acquisition article** — the single most targeted target, since `051` is the only hero with a verified gear-free Lv.30 panel | page read in full: prose only, **no stat panel**; its 7 images (`IMG_6096/6107/6117/6118-1`, `f451b5ab…`, `9d46d839…`, `0d40a5e4…`) all 404 | C2 green |
| 詳細情報 hunter screens (≥6 images): **does the stat popup ever appear open?** | **never** — this is the one screenshot class that would settle the lane and it is absent | C2 green |
| 装備強化 / ジム / キャパ超越 / ファイトクラブ articles for a gear-free panel | all either show populated slots or no stat block | C2 green |
| `blustone.jp/hunter/*` re-crawl for a second stat table | not attempted: `wayback-hunter-2026-10-05.md` establishes 63 profile URLs, ★5 section empty, no `_1` variants, and `level-factor-test` §1.6 established `基本能力値` is the only core block | prior lane, not re-litigated |
| **Bahamut (`m.gamer.com.tw`) `新手攻略之訓練獵人` / `新手攻略之材料篇` / other unopened beginner-guide threads** named in `bahamut-thumb-2026-10-05.md` §2 — the most promising named lead for training stat panels | **forum page read path is broken.** All three UAs (desktop / iPhone / curl) return the same **3,617-byte 系統訊息 system-message page**. **The image host still works**: `truth.bahamut.com.tw/s01/201802/09c0bdf…JPG` → 200, 69,918 B, `image/jpeg` (**control green**). So images are fetchable by exact URL but **threads cannot be enumerated**, and the hashes cannot be guessed. **No zero is claimed about thread content** | C: image host 200 |
| V.S.Fan `analysis/VSFan/` 220 curated images / 51 dated screenshots | already fully reviewed 2026-10-05 (`vsfan-material-index.md`, `vsfan-visual-audio-material.md`): "identity and UI context, not new base-stat tuples" | not re-tread |
| `_swipe/gdoc/faq_01..28.png`, `_swipe/caragublu/*`, the `snA*` / `Ot72M6h4OUI` / `RG47CcM7c20` locals | already reviewed; roster-token and video frames only | not re-tread |

---

## 8. Confidence ledger

| claim | confidence | basis |
|---|---|---|
| Bear `036` ★3 Lv.1 戦闘力 = 2326 | **high** | name on screen + TSV verbatim match + 4-surface exact replication |
| Bear `036` capacity-transcendence factor 2326 → 2704 = ×1.162511 | **high** | single frame, same level+grade, values re-read at 6× |
| `029` Kain ★3 Lv.MAX 3311 → ★4 Lv.1 4907 = ×1.482030 | **high** | named panel + roster row agrees on 3311; badges read at 2.2× and 12× |
| ★3/Lv.MAX → ★4/Lv.1 rank-up net factor ≈ **1.490 ± 1.1 %** | **high** | two heroes, two images, identical transition |
| rank-up **resets the hunter to Lv.1** | **high** | both rank-up frames, guide prose agrees |
| **g²⁹(戦闘力, Lv.1→Lv.30) ≤ 1.482030** | **medium-high** | arithmetic on the above + `f ≥ 1`; the `f ≥ 1` assumption is unverified |
| archive 戦闘力 ≉ in-game 戦闘力 | **high** | four heroes, archive column within 4.7 %, in-game ratio spans 0.2323–0.7088 |
| `029` Kain ★5 Lv.1 = 13148 exists and is irreconcilable with the ★3 Lv.30 = 3311 reading | **medium** | badge read at 16×; the contradiction itself is the finding |
| Heidi `044` ★4 Lv.7 戦闘力 6228 is **gear-contaminated** | **high** | sibling frame shows 3 populated slots Lv.6/7/9 |
| the only Kain ★5 visible frame (`1da12b32…`, ファイトクラブの守護者 ベッケン) carries **no numbers** | **high** | direct inspection |
| **zero gear-free readings** in this corpus | **high** | no frame shows equipment slots at all; 180 images triaged |
| **zero HP/ATK/DEF stat panels** in this corpus | **high** | 180 images triaged; 6+ 詳細情報 screens all closed |
| the `snA*` level labels already in `polluted-observations.md` may be misread | **low-medium** | 10× on `snA223-83e098e1.jpg` favours `Lv. 77` over the recorded `Lv. 11`, but the 428×762 source cannot separate the glyphs — see §6 |
| the HP/ATK/DEF per-level law | **still UNKNOWN** | nothing this pass measures it |
| one hero (unidentified blonde child) has all **three** grade rungs present, each resetting to Lv.1, but only the ★3→★4 rung carries a 戦闘力 | **high** | §4.2 + §4.14, same art/element/gold across both files |
| `IMG_4930.png` shows **equipment-instance levels 45 / 25 / 11** with no stat values | **medium-high** | single frame; earns no accessory coverage |

---

## 9. Coverage counters — UNCHANGED, deliberately

**Heroes 1/113 · accessories 1/100 · monsters 0/22.** Nothing here is a
gear-separated HP/ATK/DEF tuple with a level basis, so nothing here may be
promoted. `coverage.md` was not opened for edit. The new readings are 戦闘力
(combat-power) tokens, which §5.3 shows are not even on the archive's basis.

## 10. Recommended disposition for the parent

1. **Do not implement any per-level factor.** §5.2 is an inequality on 戦闘力 and
   §5.3 shows 戦闘力 is not the disputed quantity.
2. **Treat §5.2 as a live lead, not a resolution.** It is the first measurement in
   this project that *fights* the Beckhen 1.7157 reading rather than merely
   failing to support it. The clean way to close it is to recover the client's
   戦闘力 formula and its level term — `level-factor-test` §2.6 item 3, still
   un-attempted.
3. **Do not reuse the `snA*` roster Lv labels without re-verification** (§6). They
   sit at the edge of legibility in their source files. Those images are single
   unlabeled rating tokens per portrait and earn no coverage regardless.
4. **The one screenshot class that would settle this lane is the open 詳細情報
   stat popup.** If any further Japanese or Korean guide screenshot is found, look
   only for that popup. Do not accept a Hunter-List token in its place.
5. **Chase the un-cropped ★4→★5 rank-up result** (§4.14). One hero already has
   all three grade rungs and the ★4→★5 rung is the only one at a *shared* level
   with no grade/level confound beyond the grade itself. `IMG_5729.png` and
   `IMG_5729-e1548139622568.png` are crops that stop at the badge row; an
   un-cropped capture of the same screen would give the third ratio and, assuming
   the two consecutive grade factors are equal, **would separate `f` from `g`**
   — i.e. it would actually measure the per-level law on 戦闘力. This is the
   cheapest remaining lead found this pass.
6. **Re-open Bahamut later.** The image CDN is live and the page read path is
   currently blocked; the unopened beginner-guide threads
   (`新手攻略之訓練獵人`, `新手攻略之材料篇`) remain the best-named untried source.

---

## 11. Guard compliance

`GUARD-encoding-and-archive-traps.md` read before any fetch. All file writes went
through the `write`/`edit` tools and Python with `encoding='utf-8'`; **no
PowerShell `Get-Content`/`Set-Content` touched any non-ASCII file.** Verification
after writing: **U+FFFD = 0**, **CRLF = 0** (see §12 for the audit output).
Console mojibake was treated as a console artefact, not as file corruption, per
Rule 2.

## 12. Encoding / line-ending audit

Verified on this file immediately after the last write, by Python with
`encoding='utf-8'` (not by reading the console dump — Rule 2):

```
U+FFFD             : 0        <- must be 0
CR                 : 0
CRLF               : 0        <- must be 0 for this repo
em-dash U+2014     : > 0      <- proves non-ASCII survived
mojibake U+00C3     : 0        <- must be 0
CJK U+4E00-U+9FFF  : 353      <- must be > 0
kana U+3040-U+30FF : 295      <- must be > 0
trailing newline   : yes
HEALTH             : PASS
```

The exact `chars` total is deliberately **not** quoted here — it drifts with every
edit to this section, and a stale number is worse than none. The eight invariants
above are what matter. The mojibake counter is written as a **codepoint** rather
than the literal glyph on purpose: embedding the glyph would trip the check it
documents.

`_manifest.json` records the `sha256` of every recovered image; each file on disk
is the byte-exact HTTP body. Recompute with:

```
python _tools/panel_control.py          # controls only
Get-FileHash hero-panel-level-images-2026-10-06\*.jpg -Algorithm SHA256   # spot check
```
