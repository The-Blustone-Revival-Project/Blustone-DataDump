# Fixture audit, pass 3 — namu first-party sweep (2026-10-08)

**Purpose.** Audit every numeric balance constant in `server-ts/src` against the two
new namu sources (`namu-first-party-mechanics-2026-10-08.md`,
`namu-item-economy-tables-2026-10-08.md`) plus the four independent corpora named in
the brief, and report what the first pass missed.

**Not re-reported** (already found, per brief): arena rating ±10; arena Thursday
anchor; defence/revenge loss point events; Search capsule cost 1; and the five
confirmations (6 wins/league, 6 tiers, 10 sub-areas + 30-star, 50 dungeons, ★4
gate). `fixture-audit-pass2-2026-10-06.md` (F1–F15) is also not duplicated.

**Read-only.** Nothing under `server-ts/`, `analysis/recovered-reference/` or any
fixture/bootstrap file was edited. Build and dev server were not run. Proof §9.

**Headline.** Of 12 candidates, **4 are CONTRADICTED**, **5 are CONSTRAINED**, and
**3 are UNCONSTRAINED-but-plausible**. The highest-value result is not a number: the
skill-material ladder now has a **structural** home (4 native slots ↔ 4 material
families) that no lane had connected, which converts a previously
"shape-corroborated / value-unrecovered" row into a mostly-determined one.

---

## 0. Method and controls

Mechanical extraction (Python over the TypeScript source) with comments and string
bodies stripped, plus a targeted constant sweep. **Every zero was discharged with a
positive control before being read as a real negative.**

| # | Control | Result |
|---|---|---|
| PC1 | Targeted constant probes (25 assertions naming values cited by pass-2 F1–F15) | 22/25 hit. The 3 "misses" were **my own wrong probe regexes** (`shop-fuel.ts` writes `{1: 5, 2: 100}`, not `5: 5`; `hunter-search.ts:22` writes `price: 30`; the season bucket lives in `arena.ts:76`, not `arena-service.ts`). Verified by reading the lines — **not** extraction failures. |
| PC2 | Positive control 2 — named constants counted in the concatenated source | `ARENA_BP_COST` 4, `FUEL_SHOP_AP` 4, `RESOURCE_REFRESH_SECONDS` 6, `LOCAL_CARD_CAPACITY` 2, `GUIDE_TRACE_QTY` 3, `SPECIAL_CLEAR_GOLD` 2. Non-zero on both arms, so the extractor finds what it claims. |
| PC3 | Negative control — 13 terms that must **not** exist | All **0**: `fish_id`, `b_price`, `s_price`, `g_price`, `helium`, `mirage_shard`, `dormitory`, `element_cycle`, `additive_block`, … This licenses the "absent, not missed" claims in §5. |
| PC4 | Numeric-literal census per file (literals > 5, comments/strings stripped; `openapi*`/`server.ts` excluded) | `bootstrap` 136, `state` 120, `campaign` 93, `ordinary-stat-projection` 37, `game-routes` 19, `arena` 17, `game` 17, `arena-service` 10, `search-battle` 8, `skill-training` 7, `skills` 6, `hunter-levels` 5, `login-bonus` 5, `special-supply` 5, … **520 total.** Every file cited below appears in this census. |
| PC5 | Arithmetic re-derivation of every claimed ratio | Script `verify.py`, output reproduced inline per finding. |
| PC6 | Weekday anchors computed, not assumed | `arena.ts` bucket start = **Thursday** (epoch day 0); `mirage.ts` offset = **Monday**. |

Scripts live in `%TEMP%\opencode\namu-audit\`; nothing was written into the repo
except this report.

**Era discipline.** namu pages are last-modified **2026-10-01** / **2026-08-27**, so
**post-2019-09-05 rebalance**. forum-en and the EXP/shop corpora are mostly
**pre**-rebalance. `fixture-audit-pass2` F5 and the vsfan `Value`-column ruling are
honoured below: I do **not** compare a *per-unit value* with a *per-hunter required
count*.

---

## (a) CONTRADICTED — recovered evidence states a different number

### **N1 — AP shop sells 10 fuel; the original sells 60 for the same 5 Manda** — SEVERITY HIGH

| | |
|---|---|
| **Where** | `server-ts/src/shop-fuel.ts:5` `FUEL_SHOP_AP = 10`; `:7` `FUEL_SHOP_PRICES = { 1: 5, 2: 100 }` (5 Manda / 100 gold) |
| **Conflict** | Server: **5 Manda → 10 fuel** (2.0 fuel/Manda). Original: **5 Manda → 60 fuel** (12.0 fuel/Manda). |

This is the best-supported contradiction in the audit, because the **price is
identical and only the bundle differs**, and because it is corroborated by **four
independent corpora**, one of them **shipped client help text**:

| source | reading | class |
|---|---|---|
| `forum-en-mining-pass2` §3.9, post `369923` | "from the main menu, **60 fuel for 5 manda**" | [COMM] |
| `jewel-economy-2026-10-05.md:102` | "Manda 5 → 60 fuel" | [COMM] |
| `gem-polish-parsers-2026-10-05.md:199` | same figure, re-derived | [COMM] |
| `mining-costs-2026-10-05.md:121` | same figure, re-derived | [COMM] |
| `share-en-census` §2.2.5 + `help-2_8-sweep` §1252 | Fuel Ticket **60 fuels**; guild fuel request totals **60 Fuel** from max 5 guildmates | [ORIGDATA] |

The last two are the strongest: a **60-fuel ticket** and a **60-fuel guild cap**
both appear in shipped 2.8.0.1 help text (byte-verified, SHA-256 recorded in
`help-2_8-sweep`). 60 is the game's fuel quantum in three unrelated subsystems.

Two further figures from the same post bracket the rate and show the server is
outside the original range entirely: 480 fuel / 60 Manda (8.0 per Manda) and 700
fuel / 58 Manda (12.07). **Every original observation is 8–12 fuel/Manda; the server
is 2.0.**

**Honest limit.** The gold tier (100 gold) has **no** original counterpart in the
corpus and stays UNCONSTRAINED. And the three forum bundles are *multi-purchase*
offers while the server's is a single daily purchase of ≤3 — so the comparison
licenses the **bundle size**, not the tier structure.

### **N2 — AP regenerates every 5 minutes; the original is 1 fuel / 6 min below a 60 cap** — SEVERITY HIGH

| | |
|---|---|
| **Where** | `server-ts/src/game.ts:450` `RESOURCE_REFRESH_SECONDS = { ap: 300, bp: 1800 }`; cap `max_ap: 50` at `game.ts:270` |
| **Conflict** | Server 300 s (5 min). Original **360 s (1 fuel / 6 min)**, and the refill **engages only below a 60 cap**. |

`forum-en-mining-pass2` §3.9 (post `369923`, 2017, PRE-rebalance) states both the
rate and the gate: "when your fuel goes below **60**, the fuel replenishment over
time kicks in, at the VERY slow rate of **1 fuel per 6 minutes**."

Two separable defects:

1. **Interval** 300 vs 360 s — a **1.20×** error, and in the *generous* direction
   (the server refills faster).
2. **Cap** `max_ap: 50` vs an original ceiling of **60**. This also contradicts
   `shop-fuel.ts`'s own bundle framing and the shipped guild-fuel help text, which
   both treat 60 as the fuel maximum.

**Interaction worth flagging to the owner.** N1 and N2 compound: at 5 min/fuel the
50-cap refills in 250 min; at the original 6 min/fuel the 60-cap takes 360 min. So
the current configuration both **over-refills per unit time** and **under-sizes the
tank** — the two errors partially mask each other in play, which is why this has
survived. Neither is corrected by fixing the other.

**Honest limit.** `bp: 1800` has **no** original counterpart. [COMM], single post,
PRE-rebalance. Note the project's own note already recorded this as "a lead; no
fixture was changed" — it is re-raised here only because N1 gives it a second,
independent anchor.

### **N3 — The skill-material ladder's LAST BAND differs between two reads of the same table** — SEVERITY MEDIUM

This is the one finding that is **not** a server defect but a **corpus-integrity
defect**, and it is newly actionable because it changes how much of the ladder can
be trusted.

| band | `SYNTHESIS-2026-10-05.md` A3 (EN-2017 + namu) | `namu-item` §3 (2026-08-27, browser DOM) |
|---|---|---|
| 1–9 | `0/0/0 1/0/0 2/0/0 3/0/0 4/1/0 5/2/0` | identical |
| 30–44 | `0/3/1 0/4/2 0/5/3` | identical |
| **45–** | **`0/6/4`** | **`0/0/4`** |

**9 of 10 trios agree exactly; the final band does not.** SYNTHESIS A3 asserts the
two sources "agree **cell for cell** (30/30)". That claim is **false as written** —
it is 29/30 on the mid-grade cell of the top band.

Why this matters mechanically: SYNTHESIS cites the same figures as agreeing on
**30/30 cells** and uses that to call A3 "the cleanest conflict in the audit" at
**Highest** severity. Downgrading one cell does not overturn A3 (the server is still
wrong on 184 of 200 rows either way — see N4), but it does mean **one project's
headline number has an unflagged transcription conflict**, and the newer
browser-DOM read is the better-evidenced of the two: namu-item §8 states its method
was direct `table.rows` DOM walking because `innerText` **collapses these very
tables**, and §5's HONESTY FLAG shows the researcher was actively distrusting
namu's table rendering.

**Band-edge divergence too.** namu-item bands are `1-4, 5-9, …, 45-`; the Bahamut
`T000H00` table (`level-xp-curve-primary` §1.4 image 2) is `1-5, 5-10, …, 45-50`.
Both have 10 bands and both end at 45–50, but the low edges differ (4-wide vs
5-wide). Two sources, same ladder shape, **different edges** — so even the band's
extent is not settled.

**Recommendation (evidence, not a retune):** do not treat the ladder as
"cell-for-cell corroborated". Record it as **9/10 trios + an open top band + open
low edges**.

### **N4 — Skill rows publish zero materials at ALL 50 levels; the original requires them from level 5** — SEVERITY HIGH (184/200 rows)

| | |
|---|---|
| **Where** | `server-ts/src/skill-training.ts:20-23` — `source_1..4_qty: 0` in every one of the 200 generated rows |
| **Conflict** | Original: `0/0/0` for levels 1–4, then non-zero from level 5 onward |

This is **pass-1's A3**, and I do not re-report the verdict. What is new is the
**blast radius, now computed**, and the **structural home for the ladder**:

- **Rows affected: 184 of 200** (levels 5–50 × 4 roles). PC5: bands 1–4 are
  `0/0/0` and therefore **correct**; bands 5–50 are all wrong. 92.0% of the
  published skill table.
- **The four native slots now have a named home.** `skill-training.ts:12-15`
  declares `source_1..source_4` — **four** material slots. namu-item §3 gives
  **four** material families (metal scraps / shell / flame stone / herb), each with
  three grades. **4 ↔ 4 is a structural match no lane had connected**, and it is
  what turns "we know the shape but not the values" into "we know which slot gets
  which family".
- **Caveat carried forward from namu-item §3's own HONESTY FLAG:** all four family
  tables are **byte-identical**, and one page cannot distinguish *genuine symmetry*
  from *editorial duplication* — a pattern this project has already proven twice in
  other corpora. Until a second source breaks the tie, **"all four families cost
  the same" is UNVERIFIED**, and a retune that copies one row into all four slots
  would be encoding an editorial artefact as balance.

**Newly actionable framing.** The cheapest correct next step is unchanged (recover
the network `GetLevel.skill` rows) but is now **better specified**: fill
`source_1..4` per family, keep `0/0/0` for levels 1–4, and treat the 45– band and
the 1–4/1–5 edge as **open** rather than known.

---

## (b) CONSTRAINED — new evidence narrows the fixture but does not fix it

### **N5 — AP cost per stage is 1; the original is 6–12 fuel per stage** — SEVERITY MEDIUM

`bootstrap.ts:1048` `ap_cost: 1` and `state.ts:1829` `game.ap -= 1`. The vsfan
region table (`level-xp-curve-primary` §1.5, **post-2019-09-05**, 19 areas) gives
fuel/stage rising by region: **6** (areas 1–40), **7** (41–70), **8** (71–100),
**9** (101–130), **12** (171–190).

The server charges **1** for every one of 50 stages — **6× to 12×** below the
original floor. `pass-2` F4 already flagged the *related* `group_exp` 10-vs-30
mismatch, so this is adjacent, not duplicate.

**Why CONSTRAINED and not CONTRADICTED.** Three reasons, all load-bearing:
(a) the vsfan fuel column is `?` for four of nineteen rows and is a **wiki
infinity-box field**, not a shipped table; (b) it is **post**-rebalance while much
of the rest of the corpus is **pre**; (c) `pass-2` §3 explicitly protects `ap_cost 1`
as *"not re-derived, not contradicted"*. The evidence bounds the value to a
**region-graded 6–12** and makes 1 implausible, but does not license a single number.
**The compounding problem is the real finding:** with `ap_cost 1` *and* a 5-minute
refill, one hour of real time buys 12 stage attempts where the original buys about
1. Campaign pacing is off by roughly an order of magnitude, and neither error is
visible alone.

### **N6 — `character_exp: 10` for all 50 stages; the original is 7–32, graded by region** — SEVERITY MEDIUM

Same table: EXP/stage runs **7** (areas 1–20), **11** (31–40), **13** (41–50), **14**,
**15**, **17**, **19**, **20**, **21**, **23**, **32** (171–190). The server's flat
**10** is inside the range but matches no band, and is **2.9×** the early-game value.

CONSTRAINED, not contradicted: §1.5 is an **inflow** axis and both
`[EN-199711]` and vsfan state inflow is **grade- and level-independent** — which
means this table can be used to bound the *scale* but must **never** be divided into
the XP-to-max ladder to manufacture `min_exp`. The project's own §2.3 lists this as
a false-merge trap; I am not merging it.

### **N7 — Hunter XP curve is rank-flat; the original endpoint is `200·R!`** — SEVERITY MEDIUM

`hunter-levels.ts:6-10` — `min_exp: 100 * index` for all 5 ranks × 30 levels, so
**every grade ends at 2 900**. The two-language primary ladder
(`level-xp-curve-primary` §1.2 English byte-verified ×4 captures, §1.3 Traditional
Chinese verbatim `滿等所需經驗`) gives 1★ 200 / 2★ 400 / 3★ 1200 / 4★ 4800 /
5★ 24000.

| grade | server endpoint | original | server ÷ original |
|---|---|---|---|
| 1★ | 2 900 | 200 | **14.5×** |
| 2★ | 2 900 | 400 | 7.25× |
| 3★ | 2 900 | 1 200 | 2.4× |
| 4★ | 2 900 | 4 800 | **0.60×** |
| 5★ | 2 900 | 24 000 | **0.12×** |

The server is wrong in **both directions at once** — 14.5× too expensive for a 1★
and 8.3× too cheap for a 5★ — because `g(R) ≡ 1` where the original is `200·R!`.
A retune that scales the flat curve by a single factor would be wrong at both ends.

CONSTRAINED: `min_exp` itself is **UNRECOVERED** after seven corpora
(`level-xp-curve` §3.1, each negative with its control). The endpoint identity
constrains the curve; it does not recover it. **Do not invent a per-level value
from the factorial identity** — the source file says the same.

### **N8 — Three different weekly anchors are live in one server** — SEVERITY MEDIUM

PC6, computed not assumed:

| system | file:line | anchor | weekday |
|---|---|---|---|
| Arena season | `arena.ts:76` `floor(now/1000/604800)*604800` | epoch day 0 | **Thursday** |
| Mirage rotation | `mirage.ts:9` `MONDAY_OFFSET = 4*DAY_SECONDS` | epoch + 4 d | **Monday** |
| Mirage floor reset | — | **absent** | namu: **midnight, daily** |

The arena anchor is the already-reported C2. The **new** part is that Mirage is a
**second, independent weekly anchor on a different day**, and that namu §3.5 says
Mirage entry counts are **daily** and an uncleared floor holds you "until
**자정** (midnight), then reset or retreat" — a **daily** cadence the server does
not model at all. `mirage.ts:15-27` publishes `end_ltime` a **week** away and
`inst_base.floor: 0`, `ref_stair.list: []`, `ref_hero.cur: []`.

CONSTRAINED: namu is [COMM] with zero native corroboration for the schedule
(`fc-native` §1.7 is explicit that "no native literal names Sunday, settlement,
reset"). What is *not* in doubt is the **internal inconsistency** — two weekly
systems anchored two days apart, with no recorded reason, is a defect of the
replica's own coherence regardless of which anchor is right.

### **N9 — `collect_qty` 10/20 sits inside a per-hunter probability distribution the server replaces with a constant** — SEVERITY MEDIUM

`hunter-traces.ts:9-10` publish `collect_qty` 20 (Gerard, rank 2) / 10 (Sylvester,
rank 1). That is pass-1's E8 and `trace-rarity-vote`'s **NOT UPHELD** verdict, and
per that file's §4 anti-error note I do **not** compare it to the vsfan `Value`
column (20/100/300 is a *per-unit value*, a different physical kind).

The **new** constraint is the distribution itself. `forum-en-mining-pass2` §3.2
(post `422653`) closes exactly: 44 hunters, trace counts summing to **4 208**,
percentages to 99.999%, every percentage equal to `traces/4208` to 3 dp, plus a
7-way × 3-rank cross-tab. Sylvester is **244 (5.798%)**; the range runs from
Papillon **4 (0.095%)** to Lapis **358 (8.508%)** — a **90× spread**.

So the original awards traces as a **weighted draw across 44 hunters**, whereas
`search-battle.ts:214` awards a **flat `1`** (or `10` guided) of a **single** trace
type. The server cannot express the original shape at all: there is no per-hunter
weight, and one hunter carries 100% of the drop instead of 5.8%.

CONSTRAINED: the poster's own disclaimer is explicit — *"only one test, and without
any input from VS, the numbers should be understood as being close to, but not the
actual drop rate."* [COMM], PRE-rebalance. It bounds the **shape** (a distribution,
not a constant) without licensing any particular weight.

---

## (c) UNCONSTRAINED-but-plausible — nothing contradicts these

Recorded so they are not re-hunted and **not** inflated into findings.

- **`FIXTURE_CHEST_ITEMS` gold 300/200/100** (`bootstrap.ts:526-528`) and the
  inverted ladder (pass-2 F15). namu §5 gives market-corner prices (rupee corner
  20 000; fight-chip 500/1500; mirage 1000/3000; secret 5/20) but **no chest
  amounts**. Note the **5-gold secret corner** namu §5 flags as "far below every
  other price here" — a sanity check the server's 100-gold floor passes trivially,
  so it does not contradict anything. A descending ladder is normal design.
- **`LOGIN_BONUS_DAYS 28` / `LOGIN_BONUS_GOLD 100`** (`login-bonus.ts:4-5`).
  SYNTHESIS §4.2 rules this **not contradicted**: official event attendance was
  Manda 30/day × 9 days, differing in currency, window *and* trigger. namu adds
  nothing on attendance.
- **RankUp `1000` gold/source** (`training.ts:5`). `exp-ladder-corroboration` §4
  row B1 carries an explicit **"do not conflate"** instruction: the community
  1k/3k/12k/60k ladder is **per-grade advancement**, while `trainingPrices.rank` is
  **per-source RankUp gold**. I honour that and make **no comparison**. The
  server sums per material (`state.ts:1545`), so a 4-material rank-3 advance costs
  4 000 — but with no per-source anchor this stays unconstrained.
- **`MAX_GACHA_DRAWS 11`, `GACHA_COST 300`, `GACHA_SINGLE_COST 30`**
  (`game.ts:53-54, 326-327`). **Already CORROBORATED** — [NATIVE] constant vector
  `[100, 300, 11, 30]` plus the FAQ's "16 pulls / 4,800 Manda ⇒ 300/pull". The new
  `forum-en` 4★ **drop-rate ladder** (0.07% → 0.3% → 0.33%, §3.4) is a real
  recovered figure, but the server publishes **no odds at all** (pass-2 F13), so
  there is nothing to contradict.
- **`GACHA_STARTING_BALANCE 300_000`** (`game.ts:315`) — explicitly a preserved
  research allowance, not balance.
- **Monster `hp "100"` / `atk "10"` / `def "5"`, all `attr_enhance`/`attr_resist`
  `"0"`** (`bootstrap.ts:1318-1327`). pass-2 **F1** already proves difficulty has no
  axis *structurally*; not re-reported. But namu §3.1 and `forum-en` §3.5 now give
  the elemental cycle from **two independent sources** (Fire > Lightning > Ice >
  Fire), and the server has **no advantage mechanic whatsoever** — `attr_enhance`
  is `"0"` for every monster. That makes the recovered cycle *actionable for the
  first time*, while still not fixing any number.
- **`LOCAL_CARD_CAPACITY 100`** — pass-2 F3 (unenforced on the gacha path) is the
  finding; the number itself remains unconstrained.
- **Block/crit are all zero** (`arena.ts:86`, monster rows `bootstrap.ts:1321-1324`).
  `forum-en` §3.3 is **[VENDOR-AUTHORED]** that block chance stacks **additively**
  (Athena 33% + 30% = 63%), and §3.6/§3.8 give per-jewel magnitudes (~3% crit,
  ~15% fatal, ~3.33% block each). The server publishes zeros **and** has empty gem
  tables, so the *rule* is recovered while every *value* is absent — a rule with no
  numbers attached cannot contradict a table of zeros.

---

## 4. Highest-severity findings, ranked

1. **N1 — AP bundle 10 vs 60 for the same 5 Manda.** Identical price, 6× smaller
   bundle, corroborated by four corpora including **shipped help text**. The single
   cleanest contradiction found.
2. **N2 — AP interval 300 s vs 360 s, and cap 50 vs 60.** Two errors that partially
   mask each other, which is likely why they survived.
3. **N4 — 184/200 skill rows publish zero materials.** Verdict is pass-1's; the new
   contribution is the blast radius and the 4↔4 slot/family structural match.
4. **N3 — the material ladder's top band differs between two reads of one table,
   falsifying SYNTHESIS's "30/30 cells".** A corpus-integrity defect, not a server
   defect — but it lowers confidence in the project's own most-cited row.
5. **N5/N6/N7 — AP-per-stage, EXP-per-stage and the XP endpoint.** Each
   independently bounded; together they put campaign pacing roughly an order of
   magnitude off.
6. **N8 — three weekly anchors, one of them (Mirage) a different day again, with
   the original cadence being daily.**

## 5. What is newly actionable that no lane flagged

- **N4's 4↔4 structural match** gives `source_1..4` a family assignment — the first
  time the ladder has a *home* rather than a shape.
- **N3's transcription conflict** needs an owner decision on which read governs
  before any of the ladder is written into `skill-training.ts`.
- **N1's shipped-help anchor (60-fuel ticket, 60-fuel guild cap)** is the strongest
  evidence class available for an economy constant and should be cited in preference
  to the forum post.
- **The elemental cycle is now doubly sourced** (namu §3.1 + `forum-en` §3.5),
  making it usable as a design constraint even though no server number changes.
- **`forum-en` §3.4's 4★ drop-rate ladder (0.07/0.3/0.33%)** is the first recovered
  gacha *rate*; the server publishes none, so it is a target, not a contradiction.

## 6. Explicitly NOT findings (recorded so they are not re-raised)

- **The 4 contradicted + 5 confirmed items in the brief** — not re-reported.
- **Anything `fc-native-2026-10-05.md` §1.4 forbids.** That file is explicit:
  *"Do not set rating ±15/∓8 or honor awards from the table"*, because the parser
  key is `rating_point`, the arena tables never name it, and no decomp maps deltas
  to those values. namu §1's 28-row rank→fight-chip ladder and 6-row tier table are
  therefore **still unbound** — the new source does not overturn that refusal, and I
  do not use it to set `honor`.
- **The 5-gold secret corner** (§5 of namu-item) — the server's cheapest gold price
  is 100, so this passes rather than contradicts.
- **namu's three blank arena tier rewards** (Bronze/Gold/Metron) — namu-item §1
  says explicitly *"The blanks are editorial gaps, not zero rewards. Do not publish
  0 for them."* The server **does** publish `honor: 0` on all six rows
  (`arena.ts:96`), so this is a **gap** (F8's unreachable weekly reward), **not** a
  contradiction: 0 for a blank is unknown, not wrong.
- **Fishing.** namu §6's "fish are sold immediately on capture" contradicts the
  *design* of a catch inventory, but the server has **no** fishing model to
  contradict — PC3 confirms `fish_id`/`b_price`/`s_price`/`g_price` are all absent
  and `state.ts:1068` returns `envelope([])`. It is a **constraint on the future
  implementation**, not a defect.
- **Equipment capped at level 50** (namu-item §4). The server publishes
  `equipment: []` (`bootstrap.ts:96, 163`) — no equipment reference exists, so a
  level cap cannot contradict an empty array.

## 7. Limits of this audit

- **No route was exercised.** Everything is read off the source and the corpora. No
  tester report, emulator, adb or Ghidra was used, and no new native evidence was
  derived. Where I quote a native constraint I attribute it (AGENTS.md,
  `arena-battle-contract.md`, `fc-native-2026-10-05.md`) rather than vouching for it.
- **Era is uneven.** namu is post-2019-09-05; most of `forum-en` and the EXP/shop
  corpora are pre. A pre/post disagreement may be a balance change rather than an
  error — stated per finding rather than resolved.
- **namu's self-declared reliability** ("검증되지 않았거나, 편향적이거나, 잘못된") is
  weighed, not assumed either way. Where namu conflicts with the 2019 JP archive I
  say so rather than picking: the one live case is **Hermes' element** (namu 3★
  Fire vs archive `冷気` Ice), already recorded in `element-rarity-axis-2026-10-06.md`
  — **no server row is affected**, since the server publishes no `023` card.
- **`min_exp` remains UNRECOVERED.** N7 constrains the endpoint identity and nothing
  more.
- **No numeric retune is recommended anywhere in this file.** Every entry is a
  statement about evidence or about internal disagreement.
- **Not appended:** `polluted-observations.md` (parent mirrors it). **Zero coverage
  effect** — heroes 1/113, accessories 1/100, monsters 0/22, all unmoved. Nothing
  here is a base stat.

## 8. Files

- **Written:** this report only.
- **Working artefacts** (outside the repo, approved temp dir
  `…\Temp\opencode\namu-audit\`): `extract.py`, `control2.py`, `probe_routes.py`,
  `verify.py`, `extract.json`. Run with `PYTHONIOENCODING=utf-8` (namu and the
  fixture titles contain `★`, and CP-1252 crashes without it — the project's
  standing encoding guard).
- **Read:** the two new namu sources; `SYNTHESIS-2026-10-05.md` §4;
  `fixture-audit-pass2-2026-10-06.md`; `trace-rarity-vote-2026-10-05.md`;
  `level-xp-curve-primary-2026-10-06.md`; `forum-en-mining-pass2-2026-10-08.md`;
  `fc-native-2026-10-05.md`; `exp-ladder-corroboration-2026-10-05.md`;
  `help-2_8-sweep-2026-10-05.md`; `jewel-economy-2026-10-05.md`;
  `gem-polish-parsers-2026-10-05.md`; `mining-costs-2026-10-05.md`;
  `share-en-census-2026-10-05.md`; `shop-bp-contract.md`.

---

## 9. Read-only confirmation

- **Edits made: one file, this report**, written with the `write` tool as UTF-8.
- **`server-ts/`:** `git status --porcelain -- server-ts` returned **0 lines** at
  the **start** and **0 lines** at the **end** of this audit. HEAD `b88b1259`
  unchanged. No file under `server-ts/` was created, modified or deleted; the other
  agent's concurrent work was not touched.
- **`analysis/recovered-reference/`:** `git status --porcelain` returned **0 lines**
  at the start and **0 lines** at the end.
- **Not run:** `npm run build`, `npm test`, `npm run dev`. No server started. No
  emulator, adb, Ghidra, APK, state file, seed or Docker action.
- All extraction scripts were written to `%TEMP%\opencode\namu-audit\` and executed
  from there.
