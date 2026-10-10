# ADVERSARIAL AUDIT — `HANDOFF-to-server-agent.md`

**Written:** 2026-10-09. **Role:** break the handoff, not confirm it. **Scope:** every
factual claim re-derived from the cited primary source, the document's internal
consistency, and every number recomputed mechanically.

**Auditor stance:** I ran a **positive control on my own harness before trusting any
mismatch** (see §0). Two apparent "failures" turned out to be **my own bad probes**,
not document errors; both are recorded below so nobody re-chases them.

**Standing rules honoured:** READ-ONLY on `server-ts` (no edits, no build). Two
recorded refusals checked, not merely assumed — see §D2/B2 and §D1/B1. Coverage
counters `heroes 1/113 · accessories 1/100 · monsters 0/22` confirmed unmoved in both
the handoff and `coverage.md`. This document has **not** been edited; corrections are
proposed in the project's **strike-and-date** form only. Nothing was appended to
`polluted-observations.md`.

**Encoding:** written with the `write` tool. Verified after writing: U+FFFD = 0,
CRLF = 0. No PowerShell `Get-Content`/`Set-Content` was used on any file.

---

## 0. Positive controls and harness validation (run FIRST)

The brief warns that a previous audit scored its own control 22/25 and had to
re-check whether the 3 "misses" were bad probes. So before treating any mismatch as
a document defect, I reproduced numbers I already believed.

| control | expected | recomputed | verdict |
|---|---|---|---|
| archive HP range | `1277 … 2033` (§1) | `1277 … 2033` | **PASS** |
| archive `s=(ATK+DEF)/HP` range | `0.8419 … 1.2171` (§1) | `0.8419136765 … 1.2171428571` | **PASS** |
| archive min ATK / min DEF | `576 / 540` (§1) | `576 / 540` | **PASS** |
| `EPISODE_STAT_ACTORS` partition | `151 / 34 / 117 / 109` (§6.1) | `151 / 34 / 117 / 109` | **PASS** |
| `skill-tag.tsv` tagged cards | `112 of 113`, `051` the exception (§3) | `112`, sole exception `051` | **PASS** |
| `tag-ref.tsv:55-59` JOB titles | verbatim (§3) | verbatim | **PASS** |
| `4208 = 2⁴×263` (§1(4)) | — | `[2,2,2,2,263]` | **PASS** |
| `24068 + 6291 = 30359` (§1) | — | `30359` | **PASS** |

### Two "misses" that were MY bad probes, not document errors

1. **Role-band membership.** My first pass reported `003` and `005` (Defense) as
   *out of band*. The bug was mine: I indexed `band[role][0]` on an **unsorted**
   per-role list, so "minimum" was really "first encountered". Re-run with a sorted
   list, all six candidates are in band, and the handoff's claim holds. **The handoff
   is right; my probe was wrong.**
2. **`state.ts` `clearedWave`.** A raw `grep clearedWave` returned 0 hits, which
   looked like a fabricated citation. The variable is spelled
   `receipt.wave.cleared_wave`; the citation exists. **The handoff is right about the
   site; only its line number is stale** (see A9).

I record both because an audit that hides its own probe failures is not auditable.

---

## A. NUMBERS AND CITATIONS THAT DID NOT REPRODUCE

Ordered by risk to the server agent.

### A1 — HIGH. §1(2) "arena ranking reward ladder, COMPLETE (28 rows)" is **31 rows**

The code block lists **31** rank bands, not 28. Verified three ways:

- counting the block: 31;
- the primary note `namu-item-economy-tables-2026-10-08.md` §1 table contains 31
  bands even though **its own heading also says "28 rows"** — so the error originates
  in the source note;
- **`fc-native-2026-10-05.md` §1.5 says "31 bands" three times** ("The FC rank table's
  **31 bands** (ranks 1–30000+, chips 2500…100 + bonus)").

So the corpus **internally disagrees** (namu-item 28 vs fc-native 31) and the handoff
propagated the wrong side. The ladder itself is internally perfect — 18 deltas of
−100 then 12 of −50, **zero** other deltas, so it is a genuine closed curve — which is
why the row-count error survived. Any implementer told "28 rows" builds a wrong-size
table and silently drops `2121–2750 … 30000+`.

> **Recommended correction (strike-and-date, parent applies):**
> strike `COMPLETE (28 rows)`; insert `COMPLETE (**31** rows — 2026-10-09 adversarial
> audit; the "(28 rows)" originated in namu-item-economy-tables-2026-10-08.md §1 and is
> contradicted by fc-native-2026-05 §1.5's "31 bands")`.

### A2 — HIGH. §1(2) "Two clean step regimes (−100 to rank 100, then −50)" is wrong

The −100 regime does **not** stop at rank 100. It runs from rank 1 through the
`1621–2120 → 650` band — i.e. down to **rank 2120**. The −50 regime begins at
`2121–2750 → 600`. Measured delta structure:

```
deltas: [100 ×18, 50 ×12]   other deltas: []
last −100 band: 1621-2120
```

The primary note says something even garbled — "−100 per band down to rank 100, then
−50 to rank 1250, then −50 again" — i.e. it names **three** regimes where there are
two, and misplaces the boundary twice. The handoff inherited one of the two errors.

### A3 — §1 vs §8 mutually contradict on the Beckhen spread, and 2.2 % is wrong

§1 line 79: "**ratios agreeing to ≤2.2%**".
§1 line 84: "the three fields span a **2.25% band**".

`max/min − 1 = 2.2533 %`. The 2.25 % figure is correct; "≤2.2 %" is wrong. Two
different numbers for one quantity 5 lines apart.

### A4 — §8 "(A) compounding … T3 **1.3287**" should be 1.3288

`1.0994³ = 1.328823` → **1.3288**. `1.0994² = 1.208680` → 1.2087, which the
document gets right. Inherited from `t1-measured-1.0994-2026-10-08.md` §2/§8, which
carries the same 1.3287. The **conclusion is unaffected** — 1.3288 is still far from
the measured 1.30000 — but the table is a recomputation the reader is invited to
check, and it does not reproduce.

### A5 — §2 "a per-level reading gives **29×200 = 528 cruises**" is a collapsed equation

`29 × 200 = 5800`, not 528. `528` is `⌈5800 / 11⌉` — a **second** step (11 EXP per
cruise) that the source note `exp-ladder-corroboration-2026-10-05.md` line 465 spells
out and the handoff dropped. As printed, the sentence asserts a false identity. The
conclusion (a per-level reading is absurd — 528 vs 19 cruises, 27.8×) is unaffected.

### A6 — §8 carries a figure its own source note explicitly retracted

`t1-measured-1.0994-2026-10-08.md` §6.2 states: *"Defensible bound: `g²⁹ ≤ 1.498434`,
per-level ≤ **1.013851**; Beckhen excess **1.15×, not 1.16×**."*

§8 of the handoff still prints the pre-correction pair: *"per-level **≤1.0137** …
**1.16× above the bound**"*. This is precisely the brief's "a retraction that did not
remove the claim it retracts" pattern — the correction landed in the source note and
never propagated.

Note also: **the source note's own 1.013851 does not reproduce either.**
`1.498434^(1/29) = 1.014043`; `1.498434^(1/30) = 1.013572`. `1.013851^29 = 1.490218`,
which matches neither bound. Both notes have a rounding slip here; the handoff should
cite the *bound* and let the reader compute the root.

### A7 — §1 error table mixes a two-value column with a one-value ratio

```
| ATK | 100 / 120 | — | 5.76× below minimum |
| DEF | 50 / 40   | — | 10.80× below minimum |
```

`576/100 = 5.76` ✓ but `576/120 = **4.80**`. `540/50 = 10.80` ✓ but `540/40 =
**13.50**`. The error column silently uses only the first of the two displayed replica
values while showing both. HP (`1277/1000 = 1.277 → 1.28`) and `s`
(`0.8419/0.150 = 5.613 → 5.61`) are both correct.

### A8 — §8 "T1 = 1.0994 **± 0.0012**" is an undefined error bar

Dispersion of `{1.098630, 1.099291, 1.100162}`:

| statistic | value |
|---|---|
| mean | 1.099361 |
| full range | 0.001531 |
| half-range | 0.000766 |
| population sd | 0.000627 |
| standard error | 0.000362 |

**None is 0.0012.** It is a *containing* interval (all three ratios lie in
`[1.0982, 1.1006]`) but it is not labelled as such, and a reader who assumes it is a
±1σ or half-range will overstate the precision by 2–3×. Everything else in that block
is exact: mean 1.0994, spread 0.1393 %, `|1.0994−1.10|/1.10 = 0.0545 %`,
`|1.0994−1.05|/1.05 = 4.7048 %`.

### A9 — §4 cites `state.ts:1238` for a coupling that lives at **1278**

`state.ts` contains **zero** occurrences of the bare identifier `clearedWave`; the
actual third coupling site is
`completed.receipt.wave.cleared_wave !== completed.attempt.wave_count` at
**`state.ts:1278`** (inside the `tuto/Clear 37/1` guarded recruitment path). Line 1238
is `claimActivitySupply`. The claim is real; the pointer is stale.

### A10 — §4's "flat scalar (`:214`)" contradicts §1(4) of the same document

`search-battle.ts:214` now reads
`const quantity = attempt.guided ? GUIDE_TRACE_QTY : 1;` — **not** flat. A guided
first Search win awards `collect_qty` (10); an ordinary win awards 1. §1(4) of the
handoff already relies on this ("Settled guided receipts carrying `added = 10`"), so
§4 is a stale description of code its own §1(4) describes correctly. Everything else
in §4 verifies: `won !== (clearedWave === attempt.wave_count)` at `:207`; award guard at
`:210`; `SEARCH_WAVE_COUNT = 2` with the "native registers 2,3,4 only" comment intact;
the four literal test assertions at `guided-search-recruitment.ts:34,43` and
`trace-exchange.ts:35,65`, plus the two loop trip counts at `:20` (10) and `:24` (20).

### A11 — §1's `file:line` and quoted code are both stale

Handoff: ``server-ts/src/bootstrap.ts:201 stat: ordinaryRankStats({ ...cardOneReference.stat[0] })``

Actual `bootstrap.ts:201` is a `base:` line. The `stat:` site is **line 204** and
reads `ordinaryRankStats(projectOrdinaryStats(card.id, cardOneLegacyStat))`. The
quoted code string `cardOneReference.stat[0]` **does not exist anywhere in the file**.

### A12 — §1's "additionalReferences maps **every** hero to card 001's rank-1 row verbatim" is FALSE

`ordinary-stat-projection.ts` `archiveObservations` covers **001, 002, 003 and 004**.
Under the deployed default profile:

| id | published hp/atk/def | source |
|---|---|---|
| `001` | 1521 / 1058 / 653 | own archive row |
| `002` | 1624 / 839 / 682 | own archive row |
| `003` | 1750 / 726 / 864 | **own archive row** (was 001's) |
| `004` | 1467 / 679 / 679 | **own archive row** (was 001's) |
| `005` | 1000 / 100 / 50 | still `cardOneLegacyStat` |
| `006` | 1000 / 100 / 50 | still `cardOneLegacyStat` |

So the substitution is **half-fixed**: the exact defect the section exists to report
has been closed for `003`/`004` and persists for `005`/`006`.

### A13 — §1's "No test pins a hero stat value" is FALSE

`server-ts/tests/ordinary-stat-projection.ts` pins hero stat values:

- `:50` `["1000","100","50","100"]` — *"unobserved refs must not inherit projected Lantern"*
- `:63` `003.stat.def === "864"`
- `:66-69` the full legacy triple per id
- `:73` the `099` override triple

So §1's safety argument ("zero test breakage") no longer holds as stated.

### A14 — HIGHEST IMPACT. §1's entire measured-error table now measures a **non-default profile**

§1's headline is a table of the replica's error against the archive:
HP 1000 vs 1277–2033 (1.28× low), ATK 100/120 (5.76× low), DEF 50/40 (10.80× low),
`s` 0.150 vs 0.8419 (5.61× low).

Those are the **`legacy`** profile numbers. Under the deployed default
`BLUSTONE_CARD_STAT_PROFILE = "archive-2019-projection"` (commit `531ab40f`,
**2026-10-08 06:56**, i.e. after §1 was written), `001` publishes **1521 / 1058 / 653**
with `s = 1.1249` — **inside** the archive band `[0.8419, 1.2171]`. The 5.61× error
**no longer exists in the default profile**, and §1 is presented as "ACTIONABLE".

**Consequence for the server agent:** acting on §1 as written would *re-open* a
defect that has already been fixed, and would additionally **break HP neutrality** —
§1's candidate table deliberately keeps `hp = 1000` ("HP does not move"), whereas the
deployed change moves HP to the archive value (1277–2033). §1's §10 decision item 1
("The `bootstrap.ts:201` substitution … We did not apply it") is **factually stale**,
as is the file header's "**Nothing in this document has been applied.**"

This is the one finding that can cause real damage.

---

## B. INTERNAL CONTRADICTIONS AND OVERREACH

### B1 — §5 vs §1(4): the trace factor-2 verdict is stated twice with opposite labels

- §1(4): *"**The verdict:** `collect_qty` 10/20 is contradicted **by exactly 2.0×**
  (spread `0.00e+00`). This is **stronger than the older "factor-2 NOT UPHELD"**."*
- §5: *"**The factor-2 claim therefore stays NOT UPHELD — leave `collect_qty` at
  10/20.**"*

The **recommended action agrees** (leave it); the **verdict label does not**. §5 was
never updated when §1(4) upgraded it. Recommend strike-and-date on §5's sentence.
The arithmetic in §5 does reproduce: `20/20 = 1.00`, `100/40 = 2.50`, `300/80 = 3.75`;
`20/100/300 = ×5 then ×3 = 20×(1,5,15)`.

### B2 — §1(1) "CONTRADICTED — act on these: C1 arena rating ±10 → win +15, loss −8" **violates a recorded refusal**

`fc-native-2026-10-05.md` §1.4 is explicit:

> *"Table scoring (+15 win / −8 loss / −5~6 defense loss / −8 revenge-loss /
> forfeit) is unattributed to any named parser key in the native evidence … **Verdict:
> structural seam only** (pairs exist; deltas exist); **no value binds**. **Do not set
> rating ±15/∓8 or honor awards from the table.**"*

The handoff places C1 under the header "**CONTRADICTED — act on these:**" and never
restates the refusal (a search for `fc-native`, `unbound`, `no value binds`,
`do not set` returns **nothing** in the handoff). A server agent reading only the
handoff would set `rating_point` deltas that a recorded refusal forbids — and would
have no way to know. **Recommend adding an explicit refusal line under C1**, and
re-labelling the header so C1 is not lumped with the unambiguous items.

By contrast the `exp-ladder` §4 refusal (RankUp gold vs star-advancement rupees) is
**honoured**: §2 keeps the MAX-EXP endpoint question separate and never mixes it with
`trainingPrices.rank = [1000]`. Verified in both the handoff and
`exp-ladder-corroboration-2026-10-05.md` (which likewise forbids the conflation).

### B3 — §3 still asserts "eight absolute datetimes" after correcting it to nine

§3's first `/gvg/GetRef` bullet says the response has "**eight absolute datetimes**
(teaser/register/matching/deploy/combat/calc/result/finish + `next_gvg_dtm`)" — the
parenthetical enumerates **nine**. Twenty lines later the same section says:

> *"2026-10-06 CORRECTION — there is no 'eight datetimes vs five enumerators' gap …
> `/gvg/GetRef` returns **nine** absolute datetimes (`next_gvg_dtm` is the ninth, not a
> rounding of the eighth)."*

The correction is present but the earlier bullet was **not struck**, so the document
asserts both counts. (The separate "**8** `point[]` rows" later in §3 is a different
quantity and is not affected.)

### B4 — §8 "THE MODEL IS NOW RESOLVED" / "the most implementable balance finding" vs §8 "still OPEN" and §8's standing prohibition

§8 contains, in order:

1. *"**THE MODEL IS NOW RESOLVED: rungs scale FROM BASE, not cumulatively** … **This
   is the most implementable balance finding in the handoff.**"*
2. ~250 lines later: *"**How the rungs combine is still OPEN, and this is the
   actionable part** … **A single T2 panel decides it.**"*
3. In the standing prohibitions: *"**Do not implement `1.10 / 1.20 / 1.30` as per-step
   factors** (only the T3 endpoint is measured; the fit has one degree of freedom)."*

(1) and (2)/(3) cannot both stand. The document's own caveats support (2)/(3): the
discriminating leg is *"community testimony, not a measurement — one rounded heal
value on one hunter. It cannot resolve a 0.73 % gap on its own"*. **Recommend
downgrading (1) to "the better-supported of two models"** and dropping
"most implementable".

### B5 — §8 counts one frame as "a THIRD, independent measurement"

§8's 2026-10-06 bullet: *"**a THIRD, independent measurement that fits none of them.**
180 official-guide screenshots … contain a capacity-transcendence reading for Bear
`036` at **fixed level and grade**: `戦闘力 2326 → 2704`, a factor of **×1.16251**."*

But §8's own 2026-10-08 T1 bullet attributes **the identical pair** `2326 → 2704` to
`capa2-1024x911.jpg` — *"Under the same single operation that moved all three stats by
×1.0994, `戦闘力` moved `2326 → 2704`"* — and `t1-measured-1.0994-2026-10-08.md` §3
confirms it is the same frame. So the "third **independent** measurement" is **the
same frame as the T1 reading**, and the evidence count for the 1.1625 figure is
inflated from 2 sources to 3. The underlying arithmetic is right
(`2704/2326 = 1.162511`, `+5.74 %` over 1.0994); the independence claim is not.

### B6 — §1 "62 hero base triples" re-promotes 62 rows from *refuted-as-base* to *base*

> *"Note the asymmetry: §1's update gives you **62 hero base triples**, but monsters
> remain 0/22."*

§1's update is a **6-row** candidate set, and the same document says three separate
times that the archive rows are **not** base stats: *"Do not publish the archive triple
as a settled base stat on the strength of the heading"*; *"`gear_state` remains not
established on 63/63 rows"*; *"It is a second, independent reason the archive is not a
drop-in base table"*. This is the exact promotion-to-recovery failure the brief names.
Recommend: *"§1's update gives you a **6-row candidate set**; the archive's 62 rows
remain **not established** as base stats."*

### B7 — §1 "Gear cannot explain this … **controlled** n=1" overstates its own caveat

§1 calls this a *"Controlled n=1"* test with *"Gear is the variable held constant"*, then
its own precision note (ii) concedes the pair *"differs in level and grade as well as
gear"* — and §8 concludes it is a **level** factor. Gear is therefore **not** the only
variable that moved. What the data actually shows is *uniformity across three fields*
(2.2533 %), which is suggestive of a scalar and is n=1. "Controlled" overstates it;
"n=1" is honest and should lead the sentence.

### B8 — Un-re-derived: §0's "29 shapes corroborated / ~78 numbers unrecovered"

Neither 29 nor ~78 could be re-derived from anything cited inside the handoff; both
trace to `fixture-conflict-audit-2026-10-05.md`. This is the document's **framing
sentence** (it sets the reader's expectation for everything below), so it should cite
its source or drop the numerals.

---

## C. WHAT REPRODUCED EXACTLY (so nobody re-chases it)

These were all re-derived from primary bytes and all hold.

**§1 / archive**
- HP 1277–2033, ATK min 576, DEF min 540, `s` 0.8419136765–1.2171428571.
- `50` distinct core triples over `62` numeric rows; `24` shared rows = **38.7 %**
  (24/62 = 38.71 %).
- Exactly **3** pairs identical on **all 12** stat fields (`004/026`, `001/059`,
  `024/034`) and exactly **9** pairs core-shared with differing substats
  (`007/014`, `039/031`, `019/006`, `022/030`, `005/009`, `032/002`, `060/035`,
  `048/027`, `037/040`) — 3 + 9 = 12 pairs = 24 rows.
- The rarity pattern **★1 ×2, ★2 ×2, ★3 ×4, one cross-rarity (`005` ★2 / `009` ★1)**
  matches those 9 pairs exactly.
- `005` and `009` both publish **1624/628/893**, at rarities 2 and 1 — the
  "`628 → 576` substitution is **withdrawn**" correction is correct and consistently
  applied (including §8's off-model paragraph, which still treats `009` as verified).
- `r = ATK/DEF` archive range **0.6589 – 1.7483**; replica `2.000` and `3.000` are
  both outside the entire 62-row range, as claimed.
- All six candidate rows land inside their **own** role band (Bomber 1.382–1.748,
  Offense 1.170–1.581, Defense 0.659–0.917, Support 0.923–1.140) — see §0 for my
  corrected probe.
- `s` for the six candidates = 1.125 / 0.937 / 0.909 / 0.926 / 0.937 / 0.906, all
  inside the archive band.
- **5** numeric four-star rows ⇒ `57 of 62` gear-structurally-impossible (the 6th
  four-star row, `056`, is the non-numeric placeholder — correct).
- `63` total rows / `62` numeric / 1 placeholder; `gear_state` = `not established`
  on 63/63; `level` = `not shown` on all rows.
- Beckhen implied per-level `g` = 1.018790 / 1.018519 / 1.019301, span 0.000783.

**§1(2) namu item tables**
- `1621–2120 → 650` is exactly the midpoint of 700 and 600.
- Capsule costs `5×2=10`, `4×8=32`, `2×15=30` — all three.
- Material bands: the ten trios `0/0/0, 1/0/0, 2/0/0, 3/0/0, 4/1/0, 5/2/0, 0/3/1,
  0/4/2, 0/5/3, 0/0/4`, with levels 1–4 free.
- Market corners 20000 / 500 / 1500 / 1000 / 3000 / 5 / 20.
- Tier rows Silver 100 / Emerald 150 / Mandaring 200 with Gold and Metron blank —
  verified, though the handoff omits that **Bronze is also non-numeric** (the source
  calls it "absent — you start at Bronze"), so "3 of 6 blank" is the source's count,
  not 2 as the handoff's phrasing implies.

**§2 XP ladder** — 200/400/1200/4800/24000; 2900/200 = **14.5×**;
24000/2900 = **8.28 → "8.3×"**; rung ratio 1:2:6:24:120; `min_exp: 100*index` endpoint
2900 flat across all five ranks in `hunter-levels.ts`; the CONTRADICTED verdict and the
`exp-ladder` §4 non-conflation both hold.

**§3 / §5 / §6.1 / §6.2**
- §6.1 partition `151 / 34 / 117 / 109`, distinct `ref_id` `56 / 4 / 55 / 54`, distinct
  `res_id` `86 / 22 / 64 / 62` — all exact, including the `4` for monsters (three real
  refs `001/034/040` plus the null bucket).
- The 8 unsafe `C*` rows are exactly `CB0002/0003/0004_BOSS` and the five
  `CB1102_*` right-side rows named in the document.
- §3 shipped role attestation: 112/113 tagged, `051` sole exception, `036`/`043` in
  slot 5, `tag-ref.tsv:55-59` JOB titles verbatim, **102/102** agreement with the
  catalogue (0 dissents), **51/51** uncovered-roster ids tagged, **11/11**
  Episode-only ids tagged, **15/15** awakened rows tagged and **15/15** agreeing with
  their base, **67** comma-split `TAG_KEY` values, **71** `TAG_REF` rows.
- §5 `C*` tokens → `<res_id>.jet` **64/64**; `M*` → **2/22** (`M001`, `M100` only);
  `ref_id` is a hunter-card namespace (`001/034/040` are card ids; monsters are
  `M001…M098`).
- §6.2 `native-evidence.tsv` line 2 declares `IMAGE_BASE 00010000`;
  `native-all-strings.tsv` has **no** such declaration and its first line is already a
  data row; `40 290` `[FUNCTIONS]` rows; `36 755/40 290 = 91.2 %`; `735 = 1.8 %`.

**§7 jewel rebalance** — `5→6 %` (×3 rows), `4.5 → 6 % / 5 %`, `50 → 60 %`,
`23 → 35`, `12 → 16`, "Super Block 5 %" → "Reduction Jewel 10 %", `×2.00` from EN vs
`×1.111` from KO, SC still carrying the old 9 % table. All exact.

**§4 search** — see A9/A10 for the two defects; everything else verifies.

**§1(3) fixture audit N1/N2/N4** — all still accurate against `server-ts`:
`shop-fuel.ts:5 FUEL_SHOP_AP = 10` (original 60); `game.ts:450
RESOURCE_REFRESH_SECONDS.ap = 300` and `game.ts:270 max_ap: 50` (original 360 s / 60);
`skill-training.ts` publishes `source_1..4` with empty `ref_id` and `qty: 0` in **all
200** rows. N3's `0/6/4` vs `0/0/4` → **29/30** reproduces.

**§1(4) trace hazard** — `hunter-traces.ts:9-10` collect_qty 20 (`005`) / 10 (`006`);
`search-battle.ts:8` `GUIDE_TRACE_QTY`; `state.ts:1283` calls the same exchange; the
settled-receipt allowlist is `search-battle.ts:57` → `throw "Malformed Search reward"`.
**Confirmed live hazard**: any account with a settled guided receipt carrying
`added = 10` throws on state load once the divisor changes. Still unfixed.

**Coverage** — handoff and `coverage.md` both say `1/113 · 1/100 · 0/22`;
`uncovered-archive-roster-2019.tsv` has 51 rows with **zero** overlap against the 62
archive ids (62 + 51 = 113). No withdrawn claim I could find is still asserted as
live: the gear-exclusion inference, the "1.716 transcendence factor", the `628 → 576`
Captain substitution, and the "Hermes element conflict" are each explicitly retracted in
place.

---

## D. Load-bearing but thinly evidenced — what would firm each up

| # | claim | current class | what would settle it |
|---|---|---|---|
| D1 | §1 "gear cannot explain the 5.6× error" | n=1 measurement, mislabelled "controlled" (B7) | a second gear-removed panel for a *different* hero at a stated level, or a gear-delta panel for `051` |
| D2 | §1 HP row "1.28× below the minimum" | inference promoted into a measurement table — the archive range is itself "not established" as a base range | the same gear/level anchor as D1, applied to HP |
| D3 | §1(2) 31-row arena ladder | single community wiki page, post-2019-09-05, one browser render | a second independent source (game help text, an archived official page), or an in-game settlement receipt |
| D4 | §4.2 "InitEffect registers wave totals 2, 3, 4 only" | native decomp cited only to a note; not re-derivable without Ghidra | a fresh `ResolvePcRelativeStrings` dump of `InitEffect` retained alongside |
| D5 | §1(1) C1 +15/−8 | single community source **and** a recorded refusal forbids binding it | native `rating_point` delta evidence; until then the refusal stands |
| D6 | §1(1) C2 Sunday settlement | single community source | shipped client weekday strings, or a native season-schedule parser |
| D7 | §2 MAX-EXP endpoints | [COMM] only (2 boards + 1 wiki); "CONTRADICTED" is a strong label for that | a shipped or archived official progression table |
| D8 | §0 "29 shapes / ~78 numbers" | uncited inside the handoff | cite `fixture-conflict-audit-2026-10-05.md` rows, or drop the numerals |

---

## E. SAFE FOR THE SERVER AGENT TO ACT ON

Verified, currently un-actioned, and correctly scoped. In rough priority:

1. **§1(3) N1 — `shop-fuel.ts:5 FUEL_SHOP_AP = 10`.** Original 60 for the same 5 Manda.
   Reproduced at source; four corpora, two of them shipped client help. Prices correct.
2. **§1(3) N2 — `game.ts:450` 300 s / `game.ts:270` cap 50.** Original 360 s, cap 60.
   Treat with N1 as **one change** (they mask each other).
3. **§1(3) N4 — `skill-training.ts` 200 rows with zero materials** in `source_1..4`.
   184 of 200 rows affected; levels 1–4 unaffected. Needs an owner decision on the
   **N3** band dispute (`0/6/4` vs `0/0/4`) — do not silently pick.
4. **§1(4) trace `collect_qty` 2.0×.** Contradicted by the best available evidence, not
   proven wrong. **Blocked on migration**: the settled-receipt allowlist at
   `search-battle.ts:57` throws on load for accounts that already banked `added = 10`.
   Four test literals and two loop trip counts must move together.
5. **§4 item 2 — Search wave count.** `SEARCH_WAVE_COUNT = 2` is native-legal; `4` is
   the documented original (`CONTENTS12_2`, shipped help, 5/5 locales). Raising it
   needs distinct waves, not four clones.
6. **§3 the shipped `JOB_*` role column.** Strongest single item in the document:
   game-authored, 102/102 against the community catalogue, 0 dissents. If `bootstrap.ts`
   publishes `role`, this outranks the community catalogue. `051` has no tag.
7. **§1 the residual substitution for `005` / `006` only** — see the warning below.
8. **§2 the MAX-EXP endpoint / grade-invariance question** — direction finding is sound;
   the per-level step is unrecovered, and the ladder must not be adopted as a fixture.
9. **§7 the per-locale jewel deltas** — exact, and the `×2.00` (EN) vs `×1.111` (KO)
   vs old-9 %-SC divergence is a real modelling trap. Preserve all five locales.
10. **§5 and §6.1/§6.2 negatives** — all reproduced; these correctly stop wasted effort.

### ⚠ The one thing NOT safe to act on as written

**§1's headline defect table and its 6-row candidate substitution.** Acting on it today
would:

- re-open a defect already closed for `003`/`004` by the deployed projection (A12/A14);
- **move HP** from the deployed archive value back to `1000`, reversing a deliberate
  choice and re-coupling to the monster-HP decision §1 explicitly tried to keep
  separable;
- hit four test assertions that now pin hero stat values (A13);
- apply to `005`/`006` on a stale premise about what they inherit.

If the substitution is still wanted, the correct scope is **`005` and `006` only**, at
the deployed profile's HP convention, and the parent should re-derive the numbers first.
The §1 **safety** argument ("zero state migration, zero test breakage") is no longer
true and must not be quoted.

---

## F. Correction list for the parent (strike-and-date; one writer)

1. §1 — strike `bootstrap.ts:201` + the quoted `cardOneReference.stat[0]` snippet;
   insert the current line (`204`) and note the `ordinary-stat-projection` indirection.
2. §1 — strike *"maps every hero to card 001's rank-1 row verbatim"*; note `003`/`004`
   now carry their own archive rows and only `005`/`006` inherit.
3. §1 — strike *"No test pins a hero stat value"*; list the four
   `ordinary-stat-projection.ts` assertions.
4. §1 — strike the whole measured-error table as a *current* defect; re-label it as the
   **`legacy` profile** measurement, and mark the projection as already deployed.
5. §1 — strike `62 hero base triples`; replace with the 6-row candidate set + "not
   established".
6. §1 — strike `≤2.2%`; keep `2.25 %` (2.2533 %).
7. §1 — add an explicit `fc-native §1.4` refusal line under C1 and de-group it from
   "act on these".
8. §1(2) — `28 rows` → `31 rows`; fix the step-regime boundary to rank 2120.
9. §1(4)/§5 — reconcile the factor-2 verdict label (strike §5's "stays NOT UPHELD").
10. §2 — restore `29×200 = 5800 EXP = ⌈5800/11⌉ = 528 cruises`.
11. §3 — strike the "eight absolute datetimes" bullet (superseded by its own correction).
12. §4 — `state.ts:1238` → `state.ts:1278`; strike "flat scalar (`:214`)".
13. §8 — `1.3287` → `1.3288`; drop or relabel `± 0.0012`; replace `≤1.0137 / 1.16×`
    with the corrected bound (the source note's own `1.013851` also does not reproduce —
    cite the bound, not the root); mark the 2026-10-08 `2326 → 2704` reading as the
    **same frame** as the T1 measurement, not a third independent one; downgrade "THE
    MODEL IS NOW RESOLVED / most implementable" to "better-supported of two models",
    consistent with §8's own "still OPEN" and its standing prohibition.
14. §0 — cite or drop "29 rows / ~78 rows".

---

## G. Live status at audit time (2026-10-09, re-checked after writing)

`server-ts/src/hunter-traces.ts` and `server-ts/tests/hunter-traces.ts` were being
edited **by the other agent while this audit ran**. That work adds a `VIP1` Veteran-EXP
**display** row (original `ICON_VE` thumbnail, `use_type 0`, no stack, no acquisition
link). It does **not** touch `collect_qty`. Re-verified in the live working copy:

- `local_gerard_trace` (`005`) `collect_qty: 20`, `local_sylvester_trace` (`006`)
  `collect_qty: 10` — **unchanged**, so the §1(4) contradiction and the migration
  hazard are both still open;
- `search-battle.ts:57`
  `const quantities = value.last.attempt.guided ? [1, GUIDE_TRACE_QTY] : [1];`
  — **unchanged**, so the load-time throw for accounts holding a settled guided receipt
  with `added = 10` is still reachable the moment the divisor changes.

Whoever applies §1(4) should re-read both files immediately before editing, because
that file is under concurrent edit.

---

## H. Verdict

The document is **substantially sound and unusually disciplined about its own
retractions** — the gear-exclusion inference, the `1.716` transcendence figure, the
Captain `628` substitution and the Hermes element conflict are each retracted *in
place*, with the correct surviving claim, and the coverage counters never moved. I
could not break any of §3, §5, §6.1, §6.2 or §7.

What I could break is concentrated in three places:

- **§1 is written against a `server-ts` that no longer exists.** The projection landed
  2026-10-08, after §1 was authored; the file header's "Nothing in this document has
  been applied" is now false for §1, and §1's numbers describe the `legacy` profile.
  This is the highest-risk item and it is an act-now instruction.
- **One arithmetic error with downstream consequence**: the arena ladder is 31 rows,
  not 28, and the step regime ends at rank 2120, not 100.
- **One recorded refusal is silently overridden**: C1 tells the server agent to set
  `rating_point` deltas that `fc-native` §1.4 explicitly forbids.

Two of my own apparent failures were bad probes and are documented in §0 so they are
not re-investigated. Coverage counters verified unmoved at
`heroes 1/113 · accessories 1/100 · monsters 0/22`.