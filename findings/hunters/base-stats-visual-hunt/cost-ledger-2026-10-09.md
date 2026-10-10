# COST LEDGER — every cost in Blustone, 2026-10-09

**Purpose.** One authoritative table of every economy constant the project knows,
classified by evidence, plus a classification of every numeric economy constant
in `server-ts/src`, plus the list of costs nobody has recovered.

**Read-only.** Nothing under `server-ts/` was edited, and no build or dev server
was run. Proof in §9. This file is the **only** file written.

**Extend-don't-duplicate.** `fixture-audit-pass2-2026-10-06.md` (F1–F15) and
`fixture-audit-namu-2026-10-08.md` (N1–N9) are prior passes. Their verdicts are
carried forward by **reference**, not re-derived. Rows marked *carry* are theirs;
rows marked **NEW** are this pass.

**Standing refusals honoured.**
- `fc-native-2026-10-05.md` §1.4 forbids setting honor values from the arena
  reward tables. The 31-band ladder and the tier table are recorded in §1 as
  **evidence only** and are **not** used to set `honor` anywhere. §4.1 repeats this.
- `exp-ladder-corroboration-2026-10-05.md` §2.2 B1 forbids conflating RankUp
  gold with the star-advancement ladder. The two are kept as **separate rows**
  (§1.9, §1.10) and are never substituted for each other. §4.10 says so explicitly.

---

## 0. Method and positive controls

Mechanical extraction (Python over the TypeScript), not reading impressions. Every
zero was discharged against a positive control before being read as a real
negative. **Three of my own probes were wrong and were corrected** — recorded here
because the previous audit scored its own control 22/25 and had to chase the misses.

| # | Control | Result |
|---|---|---|
| PC1 | 15 named constants that must be present | **15/15** hit. |
| PC2 | 14 terms that must be **absent** (`fish_id`, `b_price`, `dormitory`, `helium`, `mirage_shard`, `transcend`…) | all **0** — licenses the §5 absence claims. |
| PC3 | Numeric-literal census per file (literals > 5, comments and string bodies stripped) | `state` 96, `campaign` 73, `skills` 44, `ordinary-stat-projection` 36, `bootstrap` 25, `arena` 17, `game` 14 … **380 total.** Every file cited appears here. |
| PC4 | Arithmetic re-derivation of every ratio in §2–§4 (`verify.py`) | all identities pass. **One check FAILED** — see §0.1. |
| PC5 | Route classification split `game-routes.ts` at the `mock: true` marker, so mock-decoration prefixes cannot be mistaken for refusals | 1 marker, dispatch head 35 844 B / fallback 566 B; `/shop/GachaPremium` and `/gym/RankUp` both in the head. |
| PC6 | Weekday anchors computed, not assumed | arena bucket = **Thursday**; Mirage offset = **Monday**. |

### 0.1 The three bad probes (this pass's own extraction faults)

Worth stating, because two of them would have produced **false findings** about
the replica:

1. **`route.startsWith("/reference/")` is not a refusal.** My first route classifier
   counted `/reference/` and `/lobby/` as "prefix-refused" families. They are not —
   they sit at `game-routes.ts:603-604`, **inside** the `mock: true` branch, where
   they decorate a fabricated success. That single mistake moved **11 routes** from
   "silent mock" to "correctly refused", i.e. it would have **hidden** the §5 gap.
   Fixed by splitting the file at the mock marker (PC5).
2. **"Gacha 30/300" probe missed.** I grepped for the literal `GACHA_COST = 300`.
   The source reads `recruitPriceSetting(process.env.BLUSTONE_GACHA_COST, 300)`.
   The values exist (`game.ts:326-327`); only my probe was wrong.
3. **"The four Raise tables are identical" is a source artefact, not a fixture
   property.** Carried from namu-item §3's own HONESTY FLAG. It does not license a
   server finding and is not counted as one.

### 0.2 Instrument limitation, stated rather than worked around

The brief asked for a re-read of namu.wiki's main page and item page. **namu is
browser-rendered and no browser is attached to this session** (`browser.disconnected`),
and namu 403s on plain HTTP while mirrors return a shell. So I could not re-read
those pages. I did **not** convert that into a negative: the namu tables are already
extracted by direct `table.rows` DOM walking into
`namu-item-economy-tables-2026-10-08.md` and `namu-hunter-page-2026-10-08.md`, and
this ledger uses those extractions. **The cost of that limitation is stated in §6.4**
rather than hidden.

---

## 1. THE CONSOLIDATED COST TABLE

Evidence classes:
**[RECOVERED-native]** from native decompile/constant vectors ·
**[FIRSTPARTY]** the game's own shipped text or original-client pixels ·
**[COMMUNITY]** wiki/board/player guide ·
**[FIXTURE]** replica invention ·
**[UNKNOWN]** nobody has it.

Era discipline (from `stat-version-context.md`): the 2019-09-05 rebalance raised
equipment and crystal stats. Sources dated before/after it are **different balance
eras**; a disagreement may be a patch, not an error.

### 1.1 Recruitment / gacha

| Cost | Value | Class | Source · date |
|---|---|---|---|
| Single draw | **30 Manda** | **[RECOVERED-native]** + [COMM]×2 | native constant vector `[100,300,11,30]` `CSRDataMgr::Init 8b1d60`; `CSRSceneLottery::OnClickRequestGachaByManda e40824` loads 300/count 11 and 30/count 1; namu; FAQ 16 pulls/4800 ⇒ 300/pull |
| Bundle (11) | **300 Manda** | **[RECOVERED-native]** + [COMM] | same vector; namu |
| Valid draw counts | **1 and 11 only** | **[RECOVERED-native]** | native vector. Server refuses any other count. |
| 4★ banner guarantee | after 16 pulls / 4800 Manda; grade-3+ guaranteed on a **bundle's last draw** | **[COMM]** guarantee rule; **[RECOVERED-native]** price | FAQ L175; server implements last-draw substitution |
| 4★ drop rate | 0.07% → 0.3% → 0.33% ladder | **[COMM]** | `forum-en-mining-pass2` §3.4. **Server publishes no odds at all.** |
| Gem 10-pull | 250 Manda; gem cap 300 | **[COMM]** | FAQ L368 |
| Mileage | 78 scrolls total; phases **3 / 10 / 25 / 40** | **[FIRSTPARTY]** pixels + [COMM] | FAQ image6 (R5); FAQ L291 |
| Gem gacha paid/free/mileage | — | **[UNKNOWN]** | 4 native routes, 0 values (see §5) |

### 1.2 AP fuel — **the best-evidenced contradiction in the project**

| Quantity | Original | Replica | Class of the original |
|---|---|---|---|
| Manda bundle | **5 Manda → 60 fuel** (12.0/Manda) | 5 Manda → **10** fuel (2.0/Manda) | **[FIRSTPARTY]** ×1 + [COMM] ×3 |
| **Gold tier** | **5000 coins → 60 fuel**; first 3 resets 5000, then **8000** | **100 gold → 10 fuel** | **[COMM]** ×2 posts · **NEW to this audit** |
| Cap | **60** | **50** | **[FIRSTPARTY]** |
| Regeneration | **1 fuel / 6 min**, engages below 60 | **300 s** (5 min) | **[COMM]** ×1 |
| Refill time for a full cap | **360 min** | 250 min | derived |

Sources: forum-en `369923` (60 for 5 Manda); `193383` "limit of 60 units"; FAQ
**shipped 2.8.0.1 help** — a **60-fuel ticket** and a **60-fuel guild cap**; and
`share-en-panels` §1.6.7: `189046` "**5000 Coins - 60 Fuel/1 Coupon** … you can only
buy up to three fuel recharges for 5000 coins. After that the recharge will
increase to **8000**"; `199711` "Estelle's Hunter Shop — Fuel Tickets **5 000 for 1**".

**The gold tier is the new part.** The prior pass (N1) explicitly wrote *"the gold
tier (100 gold) has **no** original counterpart in the corpus and stays
UNCONSTRAINED."* That is now **falsified**. The gold tier is **50× cheaper** in the
replica and yields **8.33× less** fuel per gold (0.100 vs 0.012 fuel/gold). N1's
"honest limit" was correct when written and is now superseded.

**Masking interaction (worth repeating).** 10-vs-60 fuel and 300s-vs-360s partly
cancel in play: the replica refills faster *and* has a smaller tank. Fixing either
alone makes the other more visible. Neither fix substitutes for the other.

### 1.3 BP (Letters)

| Quantity | Value | Class |
|---|---|---|
| Bundle | **5** | **[FIXTURE]** |
| Price | 5 Manda / 100 gold | **[FIXTURE]** |
| Daily limit | 3 shared across currencies | **[FIXTURE]** (the *shared-limit shape* is corroborated by native `UpdateText`) |

The entire BP shop is a fixture. No original BP price was found in any corpus.

### 1.4 Raise / training (강화·훈련) — **skill-training** system

Four material families, three grades each: 금속 조각 (rusty/sharp/wondrous),
등껍질 (broken/intact/immutable), 화염석 (cold/hot/blazing), 약초
(wilted/fresh/fruiting). Level bands `1~4 … 45~`:

| band | 1~4 | 5~9 | 10~14 | 15~19 | 20~24 | 25~29 | 30~34 | 35~39 | 40~44 | 45~ |
|---|---|---|---|---|---|---|---|---|---|---|
| trio low/mid/high | `0/0/0` | `1/0/0` | `2/0/0` | `3/0/0` | `4/1/0` | `5/2/0` | `0/3/1` | `0/4/2` | `0/5/3` | **`0/0/4`** |

- **Levels 1–4 cost no material.** [COMM], namu item page, 2026-08-27 DOM walk.
- **⚠ The four family tables are byte-identical.** "All four cost the same" is
  **UNVERIFIED** — could be genuine symmetry or editorial duplication. Carried
  from namu-item §3's own HONESTY FLAG. **Do not copy one row into four slots.**
- **Top band disputed.** `0/0/4` (namu DOM, newer) vs `0/6/4`
  (`SYNTHESIS-2026-10-05` A3). 9/10 trios agree; the last does not. `SYNTHESIS`'s
  claim of "30/30 cells agree" is **false as written**.
- **Band edges also disputed**: namu `1-4` vs Bahamut `1-5`. Same ladder, different
  low edges.
- **Gold: 100/source** · **[FIXTURE]**.
- **One [FIRSTPARTY] pixel row (NEW, from R8):** skill **Lv.35 → 800 rupees**, plus
  materials **4 crystals / 4 leaves / 2 berries**. Crocus `Necromancer's Might`,
  wallet 50 386. Caragublu guide image, Dec-2018.
  The replica's formula `100 × destinationLevel` gives **3600** at Lv35→36 — a
  **4.5× over-charge**. One frame, no curve inferred. **CONSTRAINED, not
  contradicted**: a single frame cannot disprove a per-level formula, but it does
  bound it — the true value at Lv35 is ≤800, so the replica's line is steeply wrong.

### 1.5 RankUp / advancement (승급)

Two quantities the project must not conflate (`exp-ladder` §2.2 B1):

**(a) Fodder count — CONFIRMED, and the replica is right.**
1★→2★ **one** 1★ · 2★→3★ **two** 2★ · 3★→4★ **three** 3★ · 4★→5★ **four** 4★.
[FIRSTPARTY] `help-2_8-sweep` §2731 (`CONTENTS4_8`, byte-identical in **both**
1.4.4.1 and 2.8.0.1) + [COMM] `share-en-guide` §2.2 + [FIRSTPARTY] same file's
prose "the higher the grade the more hunters you need".
Server `rankUpRows.src_cnt = 1/2/3/4` — **exactly matches**. The only corroborated
economy number in the training system.

**(b) Gold — a genuine ladder, NOT the per-source price.** [COMM] ×5 sources +
[TW]: 1★→2★ **1 000** · 2★→3★ **3 000** · 3★→4★ **12 000** · 4★→5★ **60 000**
(dissent: **15 000** in the earliest source). These are **per-grade all-in**
figures.

**NEW — [FIRSTPARTY] pixel frame bridges the two quantities.** Caragublu
`Blustone Hunter Adcance.jpg`, target 3★ Lv.MAX → 4★:
- 2 fodder ⇒ button **8 000**
- 3 fodder ⇒ button **12 000**

**8000 / 2 = 12000 / 3 = 4000 per source.** Two different fodder counts on one
target give the *same* per-source figure. That is what licenses the derivation:

| advance | all-in (community) | fodder | **derived per-source** |
|---|---|---|---|
| 1★→2★ | 1 000 | 1 | 1 000 |
| 2★→3★ | 3 000 | 2 | 1 500 |
| 3★→4★ | 12 000 | 3 | **4 000** ← independently witnessed in pixels |
| 4★→5★ | 60 000 | 4 | 15 000 (or 3 750 on the dissent) |

The 3★→4★ row is **corroborated across both source classes**: the community ladder
predicts 4000/source and the image frame measures it twice. The per-source value is
**not constant** (1000 / 1500 / 4000 / 15000), so the replica's flat
`trainingPrices.rank = [1000]` is wrong in **both structure and magnitude**:
1 000 vs 4 000 at 3★→4★ is **4×**.

**Honest bound.** This is still **CONSTRAINED for ranks 1 and 2** — the image frame
is a 3★→4★ target, so only the rank-4 rung is pixel-witnessed. Rungs 1 and 2 are
*derived* by division from a community table, not measured.

- **Stat bonus 5% per credited material** — **[FIXTURE]**.

### 1.6 Transcendence / awakening (자기극복 / 각성)

**Material ladder** (crystal/fragment; fragment is exactly 10× crystal in every
cell):

| grade | T1 | T2 | T3 |
|---|---|---|---|
| 1★ | 5/50 | 15/150 | 45/450 |
| 2★ | 7/70 | 25/250 | 60/600 † |
| 3★ | **9/90** | **30/300** | **80/800** |
| 4★ | 12/120 | 40/400 | 110/1100 |
| 5★ | *(no row exists)* | | |

**Gold column — recovered, and exactly linear:** `5000·crystal` at every rung:
5→5000, 15→15000, 45→45000, 7→7000, 25→25000, 60→60000, **9→9000**,
**30→30000**, **80→80000**. [COMM] ×2 for materials; gold added by vsfan.
[FIRSTPARTY] pixels: `9000` + 9 crystals + 90 fragments on a 3★ (R9), matching the
3★ **T1** row exactly and not T2 or T3.

† 2★ T3 = 60/600 is **single-sourced** to one player guide; no rule generates it.

**Gate:** ★3+ only, and the **fodder must also be ★3+** — the material costs
exactly one same-grade hunter per step, **and that hunter is consumed**
[FIRSTPARTY] shipped help `CONTENTS4_3`, identical in both versions; corroborated by
the JP `キャパ超越` walkthrough and the image frame's `only identical hunters 3★ or above`.

**Separate system — "Awakening" A1–A3** [COMM] FAQ L502-504:
A1 = **30 crystals + 30 000 rupees**; A2 = **50 + 100 000**; A3 = **100 + 150 000**;
total **180 crystals + 280 000 rupees + 9 hearts**. **Do not merge this with the
transcendence ladder above** — different gate (hearts, not a duplicate hunter),
different currency mix. Neither the hearts nor the gold column has a second source.

### 1.7 Equipment / Forge

| Quantity | Value | Class |
|---|---|---|
| Level cap | **50** | [COMM] |
| Two tiers | 개조 재료 (mod, lv1–20) → 강화 재료 (enh, lv21–50) | [COMM] |
| Gold exists at | 500 / 1000 / 5000 / 1500 — **cell alignment ambiguous** | [COMM] |
| Per-element mod material | 번개 막대 (Lightning) / 냉각수 (Ice) / 인화성 물질 (Fire) | [COMM] |
| **Gate** | requires owning a **4★ hunter** | **[FIRSTPARTY]** — "4성 헌터의 무기나 복장을 업그레이드" |
| Gold column (full table) | 1–2:500 · 3–8:500 · 9:1000 · 10:5000 · 11–18:750 · 19:1500 · 20:10000 · 20–29:5000 · 30:40000 · 30–39:15000 · 40:100000 · 40–50:30000 | [COMM] |
| Element material at each 10-boundary | Lightning 1 @lv10, 6 @lv20, 25 @lv30, 50 @lv40 | [COMM] — Ice/Fire columns are **editorial blanks**, so this is one-exemplar, not per-element |
| **[FIRSTPARTY] pixel row** | armour Lv49→50 = **50 000 rupees + 320 toolbox + 27 advanced toolbox** | Caragublu FAQ image7 (R6) |
| Slot unlock | an equipment gains a slot at **level 20** | [COMM] ×2 |

**Honest limit:** the namu table and the pixel frame **disagree for the same band**
(namu lv40–50 says 130/10 toolbox + 30 000; frame Lv49→50 says 320/27 + 50 000).
This is **not** a contradiction — namu renders one merged cell per decade and its
lv12–50 rows are editorial blanks. Two sources, neither a per-level truth.

### 1.8 Traces

| Quantity | Value | Class |
|---|---|---|
| Guarantee-recruit requirement | `(2^n)×10` = **20 / 40 / 80 / 160** by grade | [COMM] ×2 (namu + formula in prose) |
| Multi-recruit | 100 traces on a 1★ ⇒ 5 at once | [COMM] |
| **Shop price** | **75 fight chips per trace** | **[COMM]** ×2 — `199711` "Golden Hunter Traces **150 for 2**"; `189046` "375개로 5개". 150/2 = 375/5 = 75 exactly. |
| Drop distribution | a weighted draw across 44 hunters (range 4 … 358, a **90× spread**) | [COMM] ×1, poster disclaims precision |
| Mirror shop | sells **3★ traces** specifically | [COMM] |

The replica publishes `collect_qty` **10** (1★-rank ref) and **20** (2★-rank ref) —
off by **exactly 2.0×** against the 20/40 ladder, and it has **no per-hunter weight
at all** (it awards a flat 1, or 10 guided). This is pass-3's N9, restated as a
ledger row.

### 1.9 Arena / Fight Club — entry and rewards

| Quantity | Value | Class |
|---|---|---|
| Entry cost | **1 BP** | **[FIXTURE]** |
| Tier ladder | 6 tiers: Bronze, Silver, Gold, Emerald, Metron, Mandaring | [COMM] ×2 |
| Tier-up | **6 wins per tier regardless of losses** | **[COMM]** ×2 — server matches |
| Tier reward | Silver 100 / Gold 100 / Emerald 150 / Metron 150 / Mandaring 200 chips; green Manda **2** flat | [COMM] ×2 |
| Bronze/Gold/Metron blanks | namu says **"the blanks are editorial gaps, not zero rewards. Do not publish 0"** | — |
| Rating deltas | win **+15** / loss **−8**; defence loss **−5~6**; revenge-loss or forfeit **−8** | [COMM] ×2 |
| Rank rewards | **31 bands**, 2500 chips at rank 1 down to 100 at rank 30 000+ | [COMM] single transcription |
| Weekly reset | **Sunday** (namu "둘 다 일요일에 정산 및 초기화") | [COMM] ×2 |
| Rival refresh | server `price_type 2` (gold) `100` | **[FIXTURE]** |
| Arena **shop** refresh | "first 2 times **2 manda**, next 2 times **4 mandas**"; refreshes 0000/1200 | **[COMM]** ×1 — **NEW** |

**Honest limit on the shop-refresh row.** The `2 manda → 4 manda` figures are for the
**arena shop listing** refresh, not the rival refresh. Currency *and* magnitude both
differ from the server, but they are **not proven to be the same purchase**. Recorded
as a lead, not a contradiction.

### 1.10 Search / Hunter Search / Abyss

| Quantity | Value | Class |
|---|---|---|
| Capsule currency | **헬륨 캡슐 helium capsule** — explicitly *not* fuel | [COMM] + [FIRSTPARTY] (separate aircraft) |
| Entry cost by grade | 1★ **5×2=10** · 2★ **4×8=32** · 3★ **2×15=30** | [COMM] |
| Server cost | **1 capsule** flat | **[FIXTURE]** |
| Retry | **10 Manda** | **[FIXTURE]** |
| Reset | **30 Manda** — **[COMM] ×2** ("Abyss resets are 30 manda each"; "reset the Abyss at a cost of 30 000 Rupees or 30 Manda") | partially corroborated |
| Rupee alternative to reset | **30 000 rupees**, rising per reset | **[COMM]** — **the replica publishes no rupee alternative at all** |
| Ruins entry | **20 fuel** each, 4 waves, no time limit | [COMM] |
| Helper | **1** per entry | **[FIXTURE]** |
| Period | 3600 s | **[FIXTURE]** |

The 30 Manda reset is the **one Search price with community corroboration**, and it
matches. Its **missing rupee branch** is a real gap, not a contradiction.

### 1.11 Guild / GVG / dormitory

| Quantity | Value | Class |
|---|---|---|
| Fuel support | one request/day to guildmates; request total **60 fuel**, max **5 guildmates** | **[FIRSTPARTY]** shipped 2.8.0.1 help |
| Leave/rejoin lockout | 2 days (2.8.0.1 help) / "1 day" (FAQ, earlier) — **conflict** | [FIRSTPARTY] vs [COMM] |
| Rupee donation | exists, "extremely expensive, NOT recommended" | [COMM] — **no figure** |
| Guild contribution rewards | milestone-triggered, distributed to **all** members | [FIRSTPARTY] — **no figure** |
| Group advancement | ★1→★2 needs **four** ★1 hunters; ★2→★3 needs **five** ★2 | **[FIRSTPARTY]** `CONTENTS4_8` |
| Dorm capacity | raised **57 → 72** by patch 1.0.7.0 (2017-07-12) | [COMM] |
| Dorm expansion | Manda-bought (no figure) | [COMM] |
| Guild contribution track | 63 713 539 / 75 620 000; rewards 3 713 539 / 5 000 000; members 21/40 | **[FIRSTPARTY]** pixels (R10) — progress only, **no payout** |
| `/reference/GetGuildPrices` | — | **[UNKNOWN]**, route absent from the server (§5) |

**Every guild price is UNKNOWN.** Nothing is implemented and nothing is contradicted.

### 1.12 Market corners and shop

| Corner | gold | fight chips |
|---|---|---|
| Rupee | **20 000** | — |
| Fight-chip | **500** | **1500** |
| Mirage | **1000** | **3000** |
| Secret | **5** | **20** |

[COMM] ×2. The 5-gold secret corner is far below every other price — a sanity check
against any shop fixture, and a reminder that the **cheapest** price is not the
reference price.

Other shop rows: **Metron Fragment 1500 for 15** (100 each) · **Metron Crystal 1000
for 1** · **Golden Hunter Materials 75 for 3** (25 each) · popups 5000/4000 rupees,
**rising 3000 every 3 purchases** · challenge reset 5000 coins, **4000 for the first
three daily** [COMM] `199711`/`189046`.

### 1.13 Campaign and progression

| Quantity | Original | Replica | Class |
|---|---|---|---|
| Fuel per stage | **6** (areas 1–40) → 12 (171–190), region-graded | **1** flat | [COMM] wiki, `?` in 4/19 rows |
| Hunter EXP per stage | **7 … 32**, region-graded | **10** flat | [COMM] |
| Gold per first clear | — | 10 | **[FIXTURE]** |
| Team EXP per first clear | — | 30 | **[FIXTURE]** — now **consistent** between `/reference/GetStage` and settlement (§202) |
| Hunter XP endpoint by grade | **200 / 400 / 1200 / 4800 / 24000** = `200·R!` | **2900 for every grade** | [COMM] ×3, two languages |
| Ordinary level cap | **30** (2018 Lv30 MAX screenshot) — dissenting source says **20** | 30 | [COMM] conflict, unresolved |
| Interior per-level thresholds | — | `100×index` | **[UNKNOWN]** — do **not** derive from the factorial identity |
| Stars | 3 conditions | 3 | [RECOVERED-native] |
| Star thresholds | Complete / **<60 s** / **≤1 straggler** | same | **[FIXTURE]** (shape corroborated) |

---

## 2. NEW server-constant classifications (not in F1–F15 or N1–N9)

**X1 — RankUp gold is wrong in structure and magnitude. CONTRADICTED.**
`training.ts:5` `trainingPrices.rank = [1000]`, flat, charged **per source**.
Original per-source derivation from two independent source classes:
**1000 / 1500 / 4000 / 15000** (§1.5). At 3★→4★ the replica charges **1 000 where
the original charges 4 000** — **4×** — and the per-source value is **not constant**,
so no single scale factor fixes it. The 4 000 rung is **pixel-witnessed twice**
(8 000/2 and 12 000/3). *The fodder counts in the same file are confirmed correct —
the defect is confined to gold.* (§1.5(b); refusal honoured: the per-grade ladder is
never used as a per-source price on its own.)

**X2 — Skill-training gold is too steep, from a [FIRSTPARTY] frame. CONSTRAINED.**
`skill-training.ts:20` `gold: 100 * (index + 1)`. At Lv35→36 that is **3 600**
against a measured **800** — 4.5×. One frame cannot disprove a formula, but it
**bounds** it: the true cost at Lv35 is ≤800. Combined with N4 (184/200 rows publish
zero materials while the original requires them from level 5), **skill training is
wrong on both axes**. Note the frame also shows **non-zero materials at Lv35**
(4/4/2), which is direct [FIRSTPARTY] support for N4.

**X3 — The fuel gold tier is not unconstrained after all. CONTRADICTED.**
`shop-fuel.ts:7` `{ 1: 5, 2: 100 }`. Original gold tier: **5000 → 60 fuel**, first
three resets 5000 then 8000. The replica is **50× cheaper** and yields **8.33× less
fuel per gold**. This **supersedes N1's stated honest limit** ("the gold tier has no
original counterpart"). Class of the original: [COMM] ×2 posts, PRE-2019 — the era
caveat applies, the price tier is not era-neutral.

**X4 — The Search reset's rupee branch does not exist. NOT IMPLEMENTED.**
`hunter-search.ts:22` publishes `reset_price: { price: 30, price_type: 1 }` only.
Two independent community sources give a **two-currency** price: **30 000 rupees OR
30 Manda**, rising per reset. The Manda figure is correct; the rupee branch is
**absent from the wire shape**, so a client that reads both gets nothing for rupees.
Not a contradiction — the server never claims a rupee price.

**X5 — Arena shop refresh: currency and magnitude both differ. LEAD, not a finding.**
Server `arena-service.ts:9` `{ price_type: 2, price: 100 }` (gold). Community: arena
**shop** refresh **2 manda ×2 then 4 manda ×2**, twice daily. Different purchase;
recorded so a future lane does not "correct" 100 → 2 on this evidence.

**X6 — XP endpoint wrong in both directions at once. carry (N7).**
`hunter-levels.ts:8` `min_exp: 100 * index` ⇒ every grade ends at 2 900.
Original `200·R!` = 200 / 400 / 1200 / 4800 / 24000. **14.5× too expensive at 1★,
8.3× too cheap at 5★.** A single scale factor is wrong at both ends.

**X7 — `group_exp` advertised-vs-paid is now closed. RESOLVED by §202.**
`campaign-reward-policy.ts` `LOCAL_CAMPAIGN_FIRST_CLEAR_TEAM_EXP = 30` is now used by
both the bootstrap preview and the settlement. **Pass-2 F4 no longer applies.** Both
numbers remain fixtures.

---

## 3. What is still UNCONSTRAINED (explicitly not findings)

Kept separate so a later lane does not re-hunt these. Most economy values live here.

- `GACHA_STARTING_BALANCE 300 000` — a preserved research allowance, not balance.
- `LOGIN_BONUS_DAYS 28` / `LOGIN_BONUS_GOLD 100` / `LOGIN_BONUS_VIP_EXP 20` — the
  **20 VIP EXP is [RECOVERED-native]** (native captures a 20 `SRREWARD` delta); the
  day count and gold are not. Official attendance was Manda 30/day × 9 days —
  a different currency, window and trigger, so **not contradicted**.
- `SPECIAL_CLEAR_GOLD 10`, chest `gold 300/200/100`, `card_inven_max 100`,
  `max_gdp 100`, `gdp 0`, login `level: 30`, `login_day_count: 0`.
- Monster `hp 100 / atk 10 / def 5`, all `attr_enhance/resist "0"` — and note the
  elemental cycle Fire > Lightning > Ice is now **doubly sourced** (§ pass-3 §c),
  so the zeros are an actionable omission, not just an absence.
- Arena synthetic rival ids, `rank 1`, `season_no 1`, honour +10, rating ±10 —
  rating/honour **must not** be set from the reward tables (`fc-native` §1.4).
- Search helper serial `900000001`, `max_join/play/retry_cnt 1`, `period 3600`.
- `ARENA_BP_COST 1` — no original BP entry cost recovered.
- BP shop 5 / 5 Manda / 100 gold / 3-per-day — the entire BP economy.
- `DEFAULT_MISSION_START_IDEMPOTENCY_SECONDS 30` — a declared policy decision.

---

## 4. Standing refusals, restated where they bind

**4.1 `fc-native` §1.4 — honour from arena tables is forbidden.**
§1.9 records the 31-band ladder and the tier table as *evidence*. Neither is used to
set `honor`, and `arena.ts:96` still publishes `honor: 0` on all six league rows.
The namu "blanks are editorial gaps, do not publish 0" note means the replica's
zeros are a **gap**, not a wrong value — recorded so it is not re-raised as a
contradiction.

**4.2 `exp-ladder` §2.2 B1 — RankUp gold ≠ star-advancement ladder.**
§1.5 keeps fodder counts (a), the per-grade ladder (b) and the derived per-source
price (c) as three separate rows. The pixel frame is what makes (b)→(c) a *division
within one quantity* rather than a conflation. Rungs 1 and 2 remain community-derived.

---

## 5. **NOT IMPLEMENTED vs IMPLEMENTED WRONGLY** — the most useful split

27 of the 33 native **cost-bearing** routes are absent from `server-ts/src`.
Method: split `game-routes.ts` at the `mock: true` marker (PC5) so a
mock-decoration prefix can never be miscounted as a refusal.

### 5.1 NOT IMPLEMENTED at all — no number exists to be wrong

| System | Routes absent | What is missing |
|---|---|---|
| **Awakening / Overcome** | `/gym/Overcome`, `/reference/GetCardOvercome` | whole system. The server hard-refuses `awk_step > 0` in 3 places (`training.ts:24,36`, `state.ts:1540,1977`). **The A1/A2/A3 ladder (§1.6) has nowhere to live.** |
| **Transcendence** | — | `awk_step` is pinned to 0; the `9/90/9000` ladder (§1.6) is unreachable. Only *chest* Transcendence Tickets 912/913/914 exist as items. |
| **Guild economy** | `/reference/GetGuildPrices` | every guild price (§1.11). Only `/guild/GetNotifications` returns an empty array. |
| **Equipment / Forge** | `/reference/GetCardEquipmentLevelUpPrice`, `...RankUpPrice` | the `equipment: []` array means **no equipment cost can contradict anything** — this is an absence, not a defect. |
| **Skins / Boutique** | `/reference/GetSkinRef`, `/lobby/GetSkinInst`, `/skin/Buy`, `/skin/Gacha`, `/skin/PutOn`, `/skin/Seen` | whole system. Namu gives only "300만다 gacha events" and "2–3 months to reproduce"; help gives the **Boutique Ticket** loop (2 per 10+1 draw, **10** on a duplicate). |
| **Jewel Mine / crystals** | `/gem/*` — correctly **refused** (2001), not mocked | correct behaviour; no original mine price exists in any corpus (only "free once per day, Manda premium yields ≥3★"). |
| **Gem gacha** | `/reference/GetPaidGemGacha`, `...Mileage`, `...DailyFree`, `/lobby/GetGemGachaInfo` | **[COMMIT-RISK]** pass-2 F11 already flagged these falling to the mock. Still true. |
| **Gacha mileage** | `/shop/RewardGachaMileage`, `/lobby/GetGachaMileage` | the 78-scroll / 3-10-25-40 ladder (§1.1) has no route. |
| **Other gacha banners** | `/shop/GachaGeneral`, `GachaEvent`, `GachaSpecificList`, `GetGachaEventRef2` | **[COMMIT-RISK]** — `result_code: 1` on a state-changing verb. AGENTS §26 already proved a mock on a shop route renders a popup **empty**. |
| **Shop verbs** | `/shop/SellCard`, `BuyItem`, `Refresh` | `SellCard` is **contract-recovered but unimplemented** (HANDOFF §3) and the mock answers it as a success. |
| **RankUpBundle** | `/gym/RankUpBundle` | group advancement. The server has single-path RankUp only. |
| **Fishing** | `/fishing/*` — **refused** (2001) except `GetInven`/`GetRecord` empty arrays | correct behaviour. Original `fish_id`/prices unrecoverable (namu gives **names and an ordering**, no IDs). |

### 5.2 IMPLEMENTED WRONGLY — a number exists and evidence says otherwise

| # | Constant | Where | Replica | Original | Error |
|---|---|---|---|---|---|
| **X1** | RankUp gold | `training.ts:5` | 1000/source flat | 1000/1500/**4000**/15000 per source | **4× at 3★→4★**, wrong shape |
| **N1** | AP bundle | `shop-fuel.ts:5` | 10 fuel / 5 Manda | **60** | **6×** |
| **X3** | AP gold tier | `shop-fuel.ts:7` | 100 gold | **5000** | **50×**, 8.33× worse rate |
| **N2** | AP interval + cap | `game.ts:450,266` | 300 s, cap 50 | **360 s, cap 60** | 1.20× + 4 smaller |
| **N4** | Skill materials | `skill-training.ts:21-22` | 0 in all 200 rows | non-zero from level 5 | **184/200 rows** |
| **X2** | Skill gold | `skill-training.ts:20` | 100×level | 800 at Lv35 (frame) | **4.5×** |
| **N9** | Trace requirement | `hunter-traces.ts:9-10` | 10 / 20 | **20 / 40** | exactly **2.0×** |
| **N5** | AP per stage | `bootstrap.ts:1054` | 1 | 6–12 | 6–12× |
| **N6** | EXP per stage | `bootstrap.ts:1053` | 10 flat | 7–32 | outside any band |
| **X6** | XP endpoint | `hunter-levels.ts:8` | 2900 all grades | 200·R! | 14.5× / 8.3×, opposite signs |
| **N8** | Weekly anchors | `arena.ts:76`, `mirage.ts:9` | Thursday **and** Monday | **Sunday**; Mirage daily | 2 systems, 2 different wrong days |
| **N3** | Skill ladder top band | corpus, not server | — | `0/0/4` vs `0/6/4` | corpus integrity, **not** a server defect |

### 5.3 The distinction that matters most

**Not implemented** means there is **nothing to fix** — the number simply does not
exist, and the correct action is to recover it (or leave it absent). Eleven of the
twelve absent systems fall here, and **every one of them has no original value
recovered either**, so in most cases "not implemented" and "unknown" are the same
fact seen from two ends.

**Implemented wrongly** means the replica has published a value, an owner will
naturally treat it as real, and it is wrong. These are the eleven rows that will
actually mislead someone. **They are also the only ones where a fix is possible
today**, because in every case the original number is known.

The dangerous middle ground is §5.1's four **[COMMIT-RISK]** rows: a state-changing
verb answering `result_code: 1` is not "absent" — it is a **fabricated success**, and
it is the one class that corrupts state silently. `SellCard`, the three gem-gacha
references and the four unlisted gacha banners are in that state now.

---

## 6. The missing-cost list

### 6.1 Explicitly hunted for, and the answer

| Target | Verdict |
|---|---|
| **Awakening (각성)** | **FOUND** — A1/A2/A3 = 30/50/100 crystals + 30k/100k/150k rupees + 9 hearts [COMM]. The **hearts** requirement and the heart *prices* are UNKNOWN. |
| **Transcendence (자기극복)** | **FOUND and substantially complete** — 4 grades × 3 steps, crystals/fragments/gold; gold exactly `1000×crystals` at every rung. 2★ T3 single-sourced; **no 5★ row exists**. |
| **Guild** | **NOT FOUND.** Structure and cadence only (fuel support 60, contribution rewards, group-advance counts). **Every guild price is UNKNOWN.** |
| **Dormitory** | **PARTIAL** — capacity 57→72 (one patch note), Manda-bought expansion (no price), dorm fuels **Raise** materials (§1.11 note). |
| **RankUp** | **FOUND** — fodder counts [FIRSTPARTY], gold ladder [COMM], per-source derived and pixel-corroborated (§1.5). |
| **Skill training** | **PARTIAL** — level ladder + 4-family material bands; gold only from ONE frame (§1.4). |
| **Jewel Mine / crystals** | **NOT FOUND.** Free daily + Manda premium ≥3★ only. No price. |
| **Boutique skins** | **NOT FOUND.** Ticket loop recovered (2 per 10+1, 10 on duplicate); **no skin price.** |

### 6.2 Additional gaps this pass surfaced

- **Fuel gold tier escalating 5000 → 8000** after three daily resets. Never recorded
  before. It implies the gold tier is *not* flat, which changes what a correct
  `FUEL_SHOP_PRICES` would even look like.
- **Shop popup escalation**: +3000 every 3 purchases; challenge reset 4000 for the
  first three. A **volume-discount ladder** the replica has no concept of.
- **Arena shop refresh 2 → 4 manda**, twice daily, at 0000/1200.
- **Guild fuel support is itself a 60-fuel transfer** — the third independent place
  60 appears as the fuel quantum, which strengthens N1.
- **Awakening's 9 hearts** — a material family the project has no item reference for.

### 6.3 Still UNKNOWN, and worth saying plainly

Interior per-level XP thresholds · awakening heart prices · every guild price ·
Jewel Mine price · skin price · fish `fish_id`/prices/grades · gem gacha prices ·
gacha odds in the server · the 45– band of the skill ladder · the four-family
identity question · the 20-vs-30 level cap · 4★→5★ at 60 000 vs 15 000 · the 255
mandaring anomaly.

### 6.4 Cost of the instrument limitation (§0.2)

Because namu could not be re-read, two things are **not** independently re-verified
in this pass: the four-family byte-identical flag, and the equipment table's
cell-alignment ambiguity. Both are carried from the existing DOM extractions with
their original honesty flags intact. **No new claim in this ledger depends on
either being re-read.**

---

## 7. Limits

- **No route was exercised.** Everything is read off the source and the corpora. No
  tester report, emulator, adb or Ghidra was used, and no new native evidence was
  derived. Native citations are attributed to AGENTS.md and the named contract
  files rather than independently re-derived.
- **Era is uneven.** The fuel gold tier and the shop ladders are PRE-2019-09-05; the
  Raise and transcendence ladders are namu post-rebalance. A pre/post disagreement may
  be a patch rather than an error — stated per row, never resolved.
- **Most economy values remain unconstrained, not wrong.** §3 is larger than §2 on
  purpose.
- **No retune is recommended.** Every row is a statement about evidence or about
  internal disagreement. X1–X3 identify what is wrong; they do not propose the edit.
- **X1's per-source ladder for ranks 1–2 is derived by division**, not measured. Only
  the 3★→4★ rung is pixel-witnessed.
- **Zero coverage effect.** Heroes 1/113, accessories 1/100, monsters 0/22 — all
  unmoved. Nothing here is a base stat.

---

## 8. Files

**Written:** this file only.

**Read:** `fixture-audit-pass2-2026-10-06.md`, `fixture-audit-namu-2026-10-08.md`,
`fc-native-2026-10-05.md`, `fc-economy-2026-10-05.md`, `exp-ladder-corroboration-2026-10-05.md`,
`namu-item-economy-tables-2026-10-08.md`, `namu-first-party-mechanics-2026-10-08.md`,
`namu-hunter-page-2026-10-08.md`, `namu-tables-2026-10-05.md`,
`result-screens-2026-10-05.md`, `rewards-economy-2026-10-05.md`,
`share-en-panels-2026-10-05.md`, `share-en-guide-2026-10-05.md`,
`help-2_8-sweep-2026-10-05.md`, `GUARD-encoding-and-archive-traps.md`,
`rewards-economy` / `share-en-census` cross-references, and all 37 `server-ts/src/*.ts`
files.

**Working artefacts** (outside the repo, approved temp dir `…\Temp\opencode\cost-ledger\`):
`extract.py`, `econ.py`, `all-literals.py`, `routes.py`, `routes2.py`, `routes3.py`,
`absence.py`, `verify.py`, `extract.json`, `econ_lines.json`. Run with
`PYTHONIOENCODING=utf-8` (namu text contains `★`; CP-1252 crashes without it — the
project's standing encoding guard).

---

## 9. Read-only confirmation

- **Edits made: one file, this report**, written with the `write` tool as UTF-8.
- **`server-ts/` — zero modifications by me.** Measured at three points:
  - **start**: `git status --porcelain -- server-ts` = **4 lines**
    (`M bootstrap.ts`, `M state.ts`, `M tests/mission-complete.ts`,
    `?? campaign-reward-policy.ts`) — the **other agent's** §202 work, HEAD `7ead0a79`.
  - **end**: **0 lines**, HEAD `105b7d7a` "Align campaign EXP reference and trace
    native auto-selection". The other agent **committed** those four files during my
    run; that is their commit, not mine.
  - **Across the whole run I issued zero writes under `server-ts/`.** Every tool call
    touching server source was `read`/`grep`. The build and dev server were never run.
- **`analysis/recovered-reference/`:** `git status --porcelain` **0 lines** throughout.
- **Not-touched files, verified by mtime:** `coverage.md`, `polluted-observations.md`,
  `README.md`, `uncovered-archive-roster-2019.tsv`,
  `archived-hunter-database-2019.tsv` all last modified **11:34**, hours before my
  single write at **20:54**. I authored none of them.
- **Not run:** `npm run build`, `npm test`, `npm run dev`. No server started. No
  emulator, adb, Ghidra, APK, seed, state file, TSV, fixture or Docker action. No
  append to `polluted-observations.md`; `coverage.md` untouched.
- **Encoding verified after write:** U+FFFD = 0, CRLF = 0, Hangul and CJK present.