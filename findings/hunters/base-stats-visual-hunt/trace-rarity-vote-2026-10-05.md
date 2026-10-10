# `vsfan.net` wiki trace values — commensurability adjudication against the factor-2 claim (2026-10-05)

**Question put to this lane.** Adjudicate a THIRD independent source on the live
factor-2 verdict. `vsfan-wiki-2026-10-05.md` §1.10 transcribes a **28-row Hunter
Trace table** from `List_of_Blustone_Items` (capture `20190821024134`, oldid
`5115`) with a per-row **Rarity** column and a per-row **Value** column reading
**★ = 20 / ★★ = 100 / ★★★ = 300** (§2.8 of that file). Its trace star count is a
third independent vote on hero rarity and agrees with the infobox/catalogue/JP
database on 26 of 27 heroes (Robin the outlier). Does this **change** the
`trace-threshold-2026-10-05.md` verdict that the local `collect_qty` 10/20 is
**NOT UPHELD** as a demonstrated factor-2 error?

**Answer in one line.** **No — the verdict is unchanged and stays NOT UPHELD, but
for a strengthened and now sharper reason: the wiki's 20/100/300 is a
per-trace-item RARITY VALUE ("what one trace is worth"), not a recruitment
REQUIREMENT COUNT, so it is a *different quantity* from `collect_qty` and is not
commensurable with it. Even under the counterfactual that they were the same
quantity, the wiki would *contradict NAMU* (not the fixture) by a
non-constant 1.0× / 2.5× / 3.75×, which destroys NAMU's authority as a value
source rather than corroborating the factor-2 claim.** §2.2–§2.4.

**Secondary finding, recorded because it is a real structural observation and not
a stat:** 20/100/300 is **not** `2^n × 10`, **not** geometric, and not any simple
ladder. Ratios are **×5 then ×3**; first differences are **80 then 200**; it is
`20 × (1, 5, 15)`. §2.1. There is no arithmetic rule of the doubling kind that the
factor-2 claim was built on.

**Coverage effect: zero.** Heroes 1/113, accessories 1/100, monsters 0/22 —
unchanged. No numeral in this file is a hero, accessory or monster base stat.

**Actions taken: none beyond writing this file.** No fixture, server source, seed,
state file, APK, emulator, phone or archive was touched. `polluted-observations.md`
was **deliberately NOT appended** (the parent mirrors it). No audit-row edit was
made; §4 lists what the parent may wish to re-word.

---

# 1. PURE — what each table actually measures, as transcribed

## 1.1 The wiki table, its literal column header, and its 27 numeric rows

`vsfan-wiki-2026-10-05.md` §1.10 states the header verbatim:

```
Image / Name / Description / Rarity / Areas Available / Value
```

Six columns. The numeral lives in **`Value`**, a column that sits in the **same
item catalogue** as `Metron Fragment → Value 10`, `Metron Crystal → Value 1000`
and four Hunter-Material tables at `10 / 50 / 250` per tier. Full set of 27
trace rows as stored:

| Rarity | Value | Count | Heroes (as stored) |
|---|---|---|---|
| ★ | **20** | 10 | Balian, Bruce Bang, Hecate, Lapis, Metis, Captain ("My Trace"), Robin, Sienna, Sylvester, Tyltyl |
| ★★ | **100** | 8 | Acerola, Denali, Gerard, Levi, Mowgli, Rebecca, Riko, Teddy Bomber |
| ★★★ | **300** | 8 | Akasha, Athena, Hermes, Kain, Karl Steiner, Lantern, Nene, Octavia |
| ★ | **100** ⚠ | 1 | **Locke** — breaks the wiki's own rule |

**There is no "required", "amount", "quantity", "threshold", "cost" or "exchange"
column anywhere in this table, and no column stating how many traces a hunter
costs to recruit.** The `Description` column, as stored, carries acquisition
locations and usage prose, not a threshold. This is the whole of the
classification question, and it is settled by the header, not by inference.

## 1.2 The `Value` column is demonstrably a *value*, using the wiki's own neighbours

Three internal cross-checks inside the same page, none of which requires any
outside source:

| Check | Reading | What it proves |
|---|---|---|
| `Metron Fragment → Value 10`, while the same page's skill-cost table (§1.14) spends **1–5 fragments** per level | 10 ≠ any quantity the skill table consumes | the column is not a requirement count for that item |
| `Metron Crystal → Value 1000`, and `Fight_Club_Shop` (§1.11) sells `Metron_Crystal 1 → 1000` | exact equality | the column tracks a **price/worth**, and for this row it *is* literally the shop price |
| `Hunter Materials` tiers → `10 / 50 / 250`, while skill levels consume **1–6** of a tier | value ≫ any consumed quantity | again a worth/price, not a requirement |

So `Value` is used by this wiki, on the same page, for **unit worth**. A column
with that meaning in two of its three other tables cannot be a per-hunter
requirement count in its fourth without the page saying so. It does not.

**Corroborating internal test (weak, and labelled weak).** `Fight_Club_Shop`
prices traces at **75** per 3★ trace (`Lantern's Trace 2 → 150`, `Akasha's Trace
2 → 150`) and **37.5** per 2★ trace (`2 star hunter's trace 2 → 75`). If `Value`
were a recruitment threshold, the FC shop's own ★3 trace price would be **¼** of
it (300/75 = 4) and its ★2 price **~38 %** of it (100/37.5 = 2.67) — two
different, non-round, mutually inconsistent ratios. If `Value` is a rough
worth/valuation estimate, no inconsistency arises. This favours "value", but it is
design-plausibility inference, not proof, and rests on the wiki pricing one trace
type loosely ("2 star hunter's trace") rather than per hero.

## 1.3 What `collect_qty` is, for the record

From `trace-threshold-2026-10-05.md` §1.1 (which is not re-litigated here):

- **NATIVE**: `CSRCardInfoContainer::PostProcess` `G87d348`/`G87d3c8` copies
  `INFO.collect_qty` (item row `node+0x28`) to `CardInfo+0x4c`.
- **NATIVE**: the consumer divides by it — `Gce1252 r1 = CardInfo.collect_qty`,
  `Gce1256 r0 = owned qty`, `Gce125c divide`, `Gce1262 store max exchange count`
  — so `max hunters = floor(owned_qty / collect_qty)`, and the debit is
  `count × threshold` (`Gce21b2`).
- i.e. `collect_qty` is the **number of trace units required per hunter**, a
  divisor.

**The two quantities are of different physical kinds:** `Value` is *worth per
trace unit* (a numerator-side price attribute); `collect_qty` is *traces required
per hunter* (a divisor). Nothing in either source equates them.

## 1.4 The quantity the factor-2 claim is actually about

`fixture-conflict-audit-2026-10-05.md` E8 / `trace-threshold-2026-10-05.md` §2.6
compare `local_sylvester_trace.collect_qty = 10` (rank 1) and
`local_gerard_trace.collect_qty = 20` (rank 2) against `[NAMU] §1.3`'s
**fixed-recruit trace ladder 1★ 20 / 2★ 40 / 3★ 80 / 4★ 160, "(2^n)×10"**.

Note what the two compared numbers are: both are **counts of traces needed to
recruit**, per star. The wiki's 20/100/300 is a **value per trace**, per star. The
2/20 overlap at rank 1 is **coincidence of the numeral 20**, not a shared
quantity. Anyone comparing them directly is comparing a divisor to a unit price.

## 1.5 The two other inputs to this lane, restated as constraints

- `exp-ladder-corroboration-2026-10-05.md` retracted a "four-way corroboration"
  **overcount** of the EXP ladder: rungs 1–3 have 3 transcribed voices + 2
  run-count voices; rung 4 has 2; **rung 5 has 1**. The lesson generalises: *count
  independent-sounding sources, then count how many actually state the numeral in
  question, before calling anything corroborated.* That discipline is applied
  here to the wiki's trace numerals (§2.3).
- `share-en-census-2026-10-05.md`'s player-guide fixed-recruit trace ladder is
  **20 / 40 / 80 / 160**, i.e. the **same `[NAMU] §1.3` numbers**, not an
  independent second ladder. The workspace holds exactly one transcription of
  `20/40/80/160` (`polluted-observations.md:450`, `namu` §1.3 lineage) plus
  `15672`/`69900` titles that state no numeral. **So the corpus still has exactly
  one ladder source, not two.** The vsfan wiki is a *different* ladder
  (20/100/300) for a *different* quantity, and does not increase the ladder count.

---

# 2. UNPURE — adjudication

## 2.1 What function is 20/100/300? It is not a doubling ladder

| Test | Result |
|---|---|
| Ratios | **×5, then ×3** |
| First differences | **80, then 200** |
| Second difference | 120 (a 3-point quadratic fit `60n² − 100n + 60` reproduces it, but 3 points always fit a quadratic — this is vacuous) |
| Geometric? | **No.** A geometric fit to (20,100,300) is impossible: `b = (300−100)/(100−20) = 2.5`, which predicts a third term of `100 × 2.5 = 250`, not 300. |
| `10 × 2^n`? | **No** — that ladder is 20/40/80/160, a different sequence. |
| `20 × 2^n`? | **No** — that is 20/40/80. |
| Simplest exact description | **`20 × (1, 5, 15)`** — no standard integer-sequence name fits 1, 5, 15 (it is neither triangular, nor tetrahedral, nor `2^n−1`, nor `C(2n,n−1)` = 1/4/15, nor `C(2n,n)−1` = 1/5/19). |

**Conclusion:** 20/100/300 is an **editorial three-point price list keyed to
rarity tiers**, not a generated progression. That is *itself* evidence about its
kind: the NAMU ladder's whole authority as a ladder rests on it being a formula
(`2^n×10`); the wiki's has no formula, which is what a rough price column looks
like and not what a designed threshold column looks like.

## 2.2 Commensurability verdict: **NOT COMMENSURABLE**

| Question | Verdict | Basis |
|---|---|---|
| Does the wiki table have a column stating traces **required** to recruit? | **No.** Its numeral column is `Value` | §1.1 |
| Is `Value` a per-unit worth rather than a requirement? | **Yes**, by the wiki's own use of the same column on the same page (fragment 10 vs 1–5 consumed; crystal 1000 = the literal FC shop price; materials 10/50/250 vs 1–6 consumed) | §1.2 |
| Is `collect_qty` a divisor (`floor(owned/collect_qty)`) while `Value` is a price? | **Yes** — different physical kinds | §1.1, §1.3 |
| **Therefore can 20/100/300 be compared to 10/20 at all?** | **No.** The shared numeral 20 at rank 1 is a coincidence | §1.4 |

**This is the load-bearing finding of this lane.** The task brief anticipated
exactly this trap, and it is real: had the wiki's `Value` been silently read as
`collect_qty`, this lane would have produced a spurious "contradiction" against
the local fixture at rank 2 (100 vs 20 = 5×) and a spurious "corroboration" at
rank 1 (20 vs 10 = the same 2× NAMU shows). That combination would look like a
*second independent source confirming the factor-2 error* while actually being a
category error.

## 2.3 Counterfactual: what if they *were* the same quantity?

Recorded so the conclusion is not contingent on my classification. Suppose
hypothetically that the wiki's `Value` were the recruitment threshold:

| Star | local | NAMU §1.3 | wiki `Value` | wiki ÷ NAMU | wiki ÷ local |
|---|---|---|---|---|---|
| 1★ | **10** | 20 | 20 | **1.00×** | 2.0× |
| 2★ | **20** | 40 | 100 | **2.50×** | 5.0× |
| 3★ | (40 extrapolated, unpublished) | 80 | 300 | **3.75×** | 7.5× |
| 4★ | (80 extrapolated, unpublished) | 160 | — | — | — |

Two consequences, both pointing the same way:

1. **The wiki would be attacking NAMU, not the fixture.** Its ratio to NAMU is
   **not constant** (1.00 / 2.50 / 3.75) while NAMU's ratio to the local ladder
   **is** constant (2.00 / 2.00). The "single scaling decision" signature that
   motivated the factor-2 claim lives **only** in the NAMU-vs-local pair, and this
   new source is the first thing in the corpus to break it from outside.
2. **The factor-2 claim still does not become UPHELD.** The claim is that the
   fixture is wrong by a constant factor of 2. A third source with a
   non-constant 2.0×/5.0×/7.5× profile neither confirms a constant factor nor
   supplies a replacement value. It supplies a **third inconsistent reading**.

**So under both branches the verdict is the same: NOT UPHELD.** The
classification question changes only *which* source is on trial.

## 2.4 Does the wiki's rarity vote bear on anything else in this lane?

Yes, but narrowly, and it is already recorded: the trace ★ agreeing with the
infobox/catalogue/JP database on 26 of 27 heroes (Robin the outlier, `Locke` the
value-rule breaker) is a **rarity-axis** observation. It is consistent with the
`trace-threshold` §2.1 finding that the trace tier tracks the hunter's star, and
it adds a fifth independent data point on **Robin**'s rarity (trace ★ = 1★,
against the infobox ★★). It says **nothing about magnitudes or counts.** No file's
claim about magnitudes is affected.

## 2.5 The `Locke` anomaly, as a caution against reading these rows as designed

`Locke's Trace` is marked **★** but priced **100** (§2.8 of the wiki file). One
row in 27 violates the page's own rule, in a column that is otherwise perfectly
consistent across all three tiers. In a **price/value** column a single editor
error is the ordinary explanation. In a **designed threshold** column it would be
a data error worth investigating. The file does not resolve it; neither does this
lane. It is recorded because it is the single best argument that this column was
filled in by a person estimating, not transcribed from the client.

## 2.6 Verdict table

| Question | Verdict | Basis |
|---|---|---|
| Commensurable with `collect_qty`? | **NO** — per-trace rarity **value** vs per-hunter required **count** | §1.1–§1.4 |
| What is 20/100/300? | **An editorial 3-point price list**: ×5 then ×3, `20 × (1,5,15)`, not geometric, not `2^n`, no formula | §2.1 |
| Does it bear on the factor-2 question? | **No.** It is silent about `collect_qty`; under the counterfactual it breaks the NAMU-vs-local constant ratio (1.00/2.50/3.75 vs 2.00/2.00) | §2.2, §2.3 |
| Does the factor-2 verdict change? | **NO — stays NOT UPHELD** | below |
| Does the corpus gain a second ladder source? | **No.** The share-en "fixed-recruit ladder" is the same `[NAMU]` numerals, not independent | §1.5 |
| Does the rarity vote change anything? | **No** — it is an axis observation; Robin gains a fifth reading, magnitudes untouched | §2.4 |
| Net effect on the audit | **None required.** E8/X3 wording may optionally note a third, differently-quantified reading exists | §4 |

---

# 3. Effect on the live verdict — explicit

| Item | Before | After |
|---|---|---|
| `trace-threshold-2026-10-05.md` §2.6 "Is the factor-2 claim upheld as an error?" | **NO** | **NO** — unchanged |
| `trace-threshold-2026-10-05.md` §2.6 "shape corroborated / absolute value unrecovered" | holds | holds; **strengthened** — a second, structurally different community source also fails to pin a numeral |
| `SYNTHESIS-2026-10-05.md` **C-7** | factor-2 **NOT UPHELD** | **unchanged** |
| `SYNTHESIS-2026-10-05.md` row **E8** | "Soft … factor-2 claim NOT UPHELD" | **unchanged** |
| `fixture-conflict-audit-2026-10-05.md` E8 / X3 | CONTRADICTED (already flagged inconsistent) / OPEN (contradiction) | **unchanged by this lane**; §4 offers wording only |
| Published fixtures `10` / `20` | in place | **in place, untouched** |
| Coverage | heroes 1/113 · accessories 1/100 · monsters 0/22 | **unchanged** |

**The honest headline: this new source does not bear on the factor-2 question,
because it measures a different quantity.** It does two useful things anyway —
it removes the possibility of a *third* ladder being confused with a threshold,
and it shows the first outside reading that is inconsistent with `[NAMU]` in a way
that is not explainable as a one-index shift.

---

# 4. Optional wording the parent may consider (**proposed, not applied**)

Nothing below was edited. The parent owns these files.

1. **`trace-threshold-2026-10-05.md` §2.8 token ledger**, add a clearly-labelled
   non-threshold group, e.g.

   > **Per-trace rarity VALUE (not a threshold; do not compare to `collect_qty`)**
   > — ★ 20 / ★★ 100 / ★★★ 300, `vsfan.net` `List_of_Blustone_Items`
   > (`20190821024134`, oldid 5115), 27 rows, 1 internal violation
   > (`Locke` ★ priced 100). ×5 then ×3; not geometric; no formula.
   > [COMM] / PRE-2019-09-05.

2. **`trace-threshold-2026-10-05.md` §2.6 verdict row** for the factor-2 claim,
   optional clause: *"and the only English-language wiki ladder in the corpus
   (`vsfan` 20/100/300) measures a different quantity (per-trace value), so it
   neither supports nor refutes."*

3. **`SYNTHESIS-2026-10-05.md` C-7**, optional clause noting that the
   NAMU-vs-local constant-2 ratio is now known to be **specific to that pair** —
   the corpus's other English ladder is non-constant against NAMU.

4. **Explicit anti-error note worth adding somewhere:** the numeral **20** appears
   as a 1★ *trace value* in one source and as a 1★ *trace threshold* in another.
   Any future lane that greps for `20` near "trace" must state which of the two
   quantities it found. This is the concrete mechanism by which this source could
   have produced a false corroboration.

# 5. Limits of this lane

- **Nothing was changed.** No fixture, server source, seed, state file, APK,
  emulator, phone, archive or original asset was touched. No Ghidra run, no
  network fetch; all source text was already in the workspace.
- **`polluted-observations.md` was deliberately not appended.**
- **No coverage change**, and no base-stat credit: `Value` is not HP/ATK/DEF, not
  an accessory magnitude, not a monster tuple.
- **The §2.2 classification is a reading of a column header plus the wiki's own
  use of the same column**, not a recovered statement. It is the best available
  reading and it is stated as a reading. The §2.3 counterfactual is recorded so
  the verdict does not depend on it.
- **The §1.2 FC-price cross-check is inference**, labelled as such in place.
- **I did not re-verify the 27 wiki rows against the archived page.** The rows are
  used exactly as stored in `vsfan-wiki-2026-10-05.md` §1.10. The `Locke` and
  `Robin` anomalies are inherited from that file, which is itself byte-pinned to
  the capture and oldid.
- **The share-en "second ladder" is not independent** (§1.5); no source count is
  inflated here, applying the `exp-ladder-corroboration` retraction discipline.
