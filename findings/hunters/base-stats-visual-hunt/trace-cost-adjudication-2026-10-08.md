# Trace-cost adjudication — the four-corpus conflict on `(2^n)×10` vs `20/100/300` vs the 4,208 pool (2026-10-08)

**Question put to this lane.** Four corpora disagree about trace costs for one
system — *collect N traces → recruit a specific hunter*. Determine (1) whether
the `forum_en/422653` **4,208-trace closed system** is the pool that the other
sources divide, and whether a per-hero `collect_qty` is therefore *derivable*;
(2) whether `(2^n)×10` and `20/100/300` can both be true of different axes;
(3) whether the replica's flat `collect_qty` of **10/20** is contradicted, and
by how much; (4) whether the exchange is grade-gated.

**Answer in one line.** The four corpora are **reconcilable once each number is
placed on its own axis** — the corpus contains **three** quantities, not one
(discrete *requirement count*, *shop price per trace*, *per-trace worth*), and
the "disagreement" is almost entirely an artefact of not labelling which axis a
numeral lives on; **the 4,208 pool is NOT derivable into a per-hero cost** and is
provably a different quantity (a scroll *yield* sample, and the arithmetic runs
the wrong way); the replica's **10/20 is contradicted by a constant factor of
exactly 2.0 at both published points** — the strongest quantitative result in
this lane; and the exchange **is grade-gated**, with the grade axis independently
corroborated by two separate namu pages.

**But two premises in the task brief are factually wrong and are corrected
below** — one of them changes the source count, the other changes a system
attribution. Both were caught by direct inspection of primary bytes with a
positive control, not by re-reading the summaries.

---

## 0. Verdict table

| # | Question asked | Verdict | Basis |
|---|---|---|---|
| 1 | Is 4,208 the pool sources 1/3/4 divide? | **NO.** It is a scroll-*yield* measurement (traces returned by popping 1,056 scrolls). Per-hero cost is **not derivable**. | §2, `Q1.0`–`Q1.4` |
| 1b | Is per-hero `collect_qty` derivable from 4,208? | **NO.** 4-valued target vs a 355-valued spread; no per-hero divisor exists (residual analysis). | §2.4 |
| 2 | Can `(2^n)×10` and `20/100/300` both be true? | **YES — they are on different axes** and never actually conflicted. On the *same* axis they are incompatible (ratio 1.00/2.50/3.75, not constant). | §3 |
| 2b | Which source was mis-attributed? | **The brief.** `20/100/300` is the **vsfan** `Value` column, *not* `share_en/199711`. `199711` states no trace ladder at all. | §3.1 |
| 3 | Is the fixture's 10/20 contradicted? | **YES, by exactly 2.0× at both published points** (spread 0.00e+00). A single global scale decision, not a shape error. | §4 |
| 3b | Is it *proven* wrong? | **No.** One `[COMM]` source, and it is **post-2019-09-05 rebalance** while the fixture is untagged. Contradicted-as-best-evidence only. | §4.3 |
| 4 | Is the exchange grade-gated? | **YES**, and the grade axis is doubly attested (requirement ladder + item-page `5.1/5.2/5.3/5.4` split + grade-indexed prices). | §5 |
| 4b | Does 4,208 interact with it? | **NO.** Opposite direction (supply falls as grade rises; requirement rises). Only *pool membership* correlates. | §5.3 |

**Coverage counters unmoved: heroes 1/113, accessories 1/100, monsters 0/22.**
Nothing below is a hero/accessory/monster base stat. Trace counts, prices and
costs are economy quantities.

---

## 1. METHOD, and the positive control that licenses every negative below

Per the task's own instruction and `GUARD-encoding-and-archive-traps.md`, a
mismatch is worthless unless the harness is shown to close a figure the source
itself published as exact. So the control ran **first**, and it ran on the
*hardest* available target: rebuilding three published partitions from an
**independent** grade/role/element axis the source never saw
(`analysis/catalogue/data/cards.json`).

### 1.1 Control block — every source-published closed figure reproduced

| check | computed | published by the source | result |
|---|---|---|---|
| C1 forum `Traces Gained` column sum | **4 208** | 4 208 | **PASS** |
| C2 forum non-zero rows | **37** | 37 (44 rows, 7 explicit zeros) | **PASS** |
| C3 rank partition, rebuilt from `cards.json` `rarity` | **1★ 2 852 / 2★ 1 079 / 3★ 277** | 2 852 / 1 079 / 277 | **PASS** |
| C4 role partition, rebuilt from `cards.json` `role` | **Off 1 346 / Def 991 / Bom 1 066 / Sup 805** | 1 346 / 991 / 1 066 / 805 | **PASS** |
| C5 element partition, rebuilt from `cards.json` `element` | **Fire 1 504 / Light 1 222 / Ice 1 482** | 1 504 / 1 222 / 1 482 | **PASS** |
| C6 published `%` vs `traces/4208` | 0 mismatches at 0.0005 pp, max residual 0.000498 pp | "every % = traces/4208" | **PASS** |

**C6 control verdict: PASS.** All three published partitions rebuild **exactly**
from a grade/role/element axis the poster did not use. The harness closes figures
the source published as exact, so the mismatches reported in §2 may be believed.

This is a stronger result than the mining note claimed. `forum-en-mining-pass2`
verified that `% = traces/4208`; it did **not** verify that the rank, role and
element cross-tabs rebuild from an independent roster. They do, to the trace.

### 1.2 Sources were read from primary bytes, not summaries

| artefact | how obtained | integrity |
|---|---|---|
| `422653` + `421776` HTML | read directly from `recovered-assets/forum-en-2026-10-05/pass2/body/` | sha256 `24e28afc…` for 422653, matches the mining note exactly; `U+FFFD = 0` |
| namu hunter page §1.4 | re-sliced from the stored canonical render `_tools/_namu_raw/raw-d-헌터.utf8.txt` | `U+FFFD = 0`, 18 `흔적` occurrences enumerated |
| namu item page §2.5/§3.3/§5 | `_tools/_namu_raw/it-d-아이템.utf8.txt` | `U+FFFD = 0`, 118 `흔적` occurrences |
| `share_en/199711` | 4 byte-verified captures | detector control fired (see §3.1) |

Scripts (all `_`-prefixed, method trail, not deliverables):
`_trace_cost_probe.py`, `_trace_cost_prose.py`, `_namu_trace_slice.py`,
`_namu_item_trace_terms.py`, `_namu_item_trace_tables.py`, `_trace_cost_evidence.py`,
`_audit_199711_trace.py`, `_trace_cost_arith.py`, `_trace_cost_final.py`.
Output: `_trace_cost_final.txt` (all computed figures below).

### 1.3 Self-audit of this file's own quotations

Because Korean was **typed from console output** rather than copied from a file,
the inverse of the GUARD file's Rule 2 trap applies: a mangled console could
have produced plausible-looking but wrong text. Every Hangul span in this file
was therefore re-checked against the concatenated primary bytes (67 namu dumps
+ forum HTML + 199711 HTML, 18.07 M chars):

| check | result |
|---|---|
| distinct Hangul spans in this file | **88** |
| spans **not** byte-matching a primary source | **1** — `미라주` |
| — which is the **proven absence** this file reports, i.e. the intended negative | ✓ |
| all other 87 spans | byte-match ✓ |

Three English quotations are *joined* rather than continuous in the flattened
source (`"Total scrolls spent: 1056 / Total traces returned: 4208"` joins two
source lines with a slash; `"| 150 for 2 |"` renders one table row with pipes).
Each fragment was verified individually present — `_qcheck2.txt`. These are
presentational, not misquotations.

---

## 2. Q1 — Is the 4,208 pool the one the other sources divide? **No.**

### 2.1 What 4,208 actually is

Verbatim from `421776` prose (recovered this session from the archived bytes):

> "Total scrolls spent: **1056** / Total traces returned: **4208** …
> Data was calculated by taking the difference between initial traces and the
> traces **after popping all the scrolls**, then comparing the final individual
> amounts to the total amount of traces gained to get the percentage."

So 4,208 is a **yield measurement**: traces *returned* by opening 1,056 scrolls.
It is a **supply sample of n = 1 experiment**, self-described by its author as
approximate ("without any input from VS, the numbers should be understood as
being close to, but not the actual drop rate"). It is **not a cost budget**, and
it is not the pool a recruit price is drawn from. The per-hero numbers are
*how many of each hunter's traces the scrolls produced*.

This is the single fact that dissolves task question 1. The two corpora are
measuring **supply** and **demand cost** respectively. Nothing follows from one
to the other.

### 2.2 4,208 is arithmetically incompatible with being a cost pool

| test | result |
|---|---|
| 4 208 / 20 (1★) | 210.4000 — not exact |
| 4 208 / 40 (2★) | 105.2000 — not exact |
| 4 208 / 80 (3★) | 52.6000 — not exact |
| 4 208 / 160 (4★) | 26.3000 — not exact |
| factorisation | **4 208 = 2⁴ × 263**, and 263 is prime |

No ladder rung divides it. An exhaustive search for non-negative integer
combinations (all coefficients ≤ 400) found **zero** solutions for every
candidate ladder: `[20,40,80]`, `[20,40,80,160]`, `[20,100,300]`, `[10,20,40,80]`.

### 2.3 The decisive test: is supply the *inverse* of requirement?

If the game balanced scrolls so every hero costs the same effort, then
`drop_per_scroll × collect_qty` would be **constant**, i.e. drop share would be
proportional to `1/collect_qty`. Using `cards.json` grades for an independent
axis, and namu's `(2^n)×10` for cost:

| grade | n heroes | Σ traces | mean/hero | `collect_qty` | mean × cost | mean ÷ cost |
|---|---:|---:|---:|---:|---:|---:|
| 1★ | 11 | 2 852 | 259.27 | 20 | 2 592.7 | 25.927 |
| 2★ | 9 | 1 079 | 119.89 | 40 | 2 397.8 | 5.994 |
| 3★ | 17 | 277 | 16.29 | 80 | 651.8 | 0.407 |

`mean × cost` spans **651.8 … 2 592.7, a 3.98× spread.** A balanced design needs
**1.00×**. It is 3.98× off.

Normalised shares make the direction unmistakable:

| design | 1★ | 2★ | 3★ |
|---|---:|---:|---:|
| **OBSERVED** | **67.776 %** | **25.642 %** | **6.583 %** |
| equal cost (flat) | 33.333 % | 33.333 % | 33.333 % |
| inverse-cost `1/20 : 1/40 : 1/80` | 57.143 % | 28.571 % | 14.286 % |
| direct-cost `20 : 40 : 80` | 14.286 % | 28.571 % | 57.143 % |

Observed ratio **1 : 0.3783 : 0.0971**; inverse-cost would be **1 : 0.5 : 0.25**.
The supply pool is monotone **decreasing** in grade and roughly **2.4× steeper**
than even the inverse-cost model. It is a rarity-weighted gacha distribution, an
independent axis with its own weighting.

### 2.4 Per-hero `collect_qty` is not derivable — three independent obstructions

1. **Cardinality.** namu's `collect_qty` takes exactly **four** values
   (20/40/80/160). The pool's per-hero counts span **4 … 358** — a 355-valued
   spread. A 4-valued function cannot be recovered from a 355-valued one unless
   the mapping is stated, and it is not.
2. **No per-hero divisor exists.** Residuals of the drop counts modulo each rung
   are scattered (`mod 20` → 16 distinct residues; `mod 160` → 32 distinct).
   Nothing in the data behaves like a per-hero threshold.
3. **Wrong direction.** See §2.3. Even a fitted model would have to be
   *anti*-correlated with the requirement.

### 2.5 The trap, stated so the next lane does not fall into it

Papillon's **4** traces do **not** mean her `collect_qty` is 4. Lapis's **358**
does **not** mean 358. A hero's *absence* from `422653` does not make her
cheaper or dearer to recruit — the seven zero rows are event/special hunters the
poster **excluded from the pool**, per his own method note.

**Q1 ANSWER: the 4,208 system is the pool of *which heroes drop traces and how
often*, never the pool a recruit price divides. Per-hero `collect_qty` is NOT
derivable from it.**

---

## 3. Q2 — Can `(2^n)×10` and `20/100/300` both be true? **Yes — different axes.**

### 3.1 FIRST: the brief mis-attributes source 3, and this changes the source count

The brief states source 3 is "`share_en/199711` … trace values 20 / 100 / 300".
**It is not.** All four byte-verified captures of `199711` were searched.

**Positive control first** (per the GUARD file, so a zero is interpretable):
`Trace` = 3 hits, `Fight Club` = 7, `Metron` = 9, `level` = 11, **in every one of
the four captures**. The detector fires; the corpus is readable.

**The test:** every sentence containing `trace` in all four captures. They all
print the **Fight Club Shop** table, and the only trace price in it is:

> "Golden Hunter Traces (1st Priority) | **150 for 2** | Prioritize getting
> Akasha … You CANNOT get these traces anywhere else except scrolls"

**There is no 20 / 100 / 300 ladder anywhere in `199711`.** A targeted search for
those three numerals within ±400 chars of any `trace` occurrence returned
**nothing in any capture**.

`20/100/300` is the **vsfan** wiki `Value` column from
`List_of_Blustone_Items` (capture `20190821024134`, oldid 5115) — already
adjudicated as a per-trace worth by `trace-rarity-vote-2026-10-05.md`.

**Why this matters beyond bookkeeping:** the brief's premise was *"four
independent corpora disagree"*. With the mis-attribution removed there are **two
disagreeing numbers, not three**, and one of them (vsfan) has already been
adjudicated as a different quantity. The genuine tension the brief was pointing
at is **namu vs the replica**, not namu vs vsfan vs 199711.

### 3.2 namu's `(2^n)×10`, verified verbatim from the canonical render

Re-sliced from `_tools/_namu_raw/raw-d-헌터.utf8.txt` §1.4 섭외:

> 확 정 섭 외 … **각 등급별로 필요한 흔적 수는 다음과 같다.**
> 1성 **20개** · 2성 **40개** · 3성 **80개** · 4성 **160개**
> **(2^n)×10개, (∵n=헌터 등급, n성)**

Literally: *"the number of traces REQUIRED, per grade, is as follows."* That is
unambiguously a **requirement count**, the same physical kind as
`collect_qty`.

And namu supplies the **semantics**, not just the number — a sentence the
existing notes do not quote:

> 섭외에 필요한 흔적 수를 초과해서 보유시 섭외 횟수 또한 조절할 수 있다. 예를 들면
> **한 명당 흔적 20개가 필요한 1성 헌터를 흔적 100개로 최대 5명을 한 번에 섭외할
> 수 있다.**

*"if you hold 100 traces of a 1★ hunter that needs 20 each, you can recruit a
maximum of 5 at once."* That is **`floor(owned / collect_qty)`** — precisely the
native semantics recovered at `Gce1252`–`Gce1262` (`owned ÷ collect_qty`, store
max exchange count). namu is therefore not merely asserting a number; it is
**describing the same divisor arithmetic the client performs**, in the original
language, from the UI the player sees.

### 3.3 Three axes, not one number

| axis | unit | values | source |
|---|---|---|---|
| **1. Requirement (divisor)** | traces **per hunter** | 20 / 40 / 80 / 160 | namu §1.4, `(2^n)×10`, with `floor` semantics |
| **2. Shop price (unit price)** | **currency per trace** | **75** fight chips/trace (3★) | `199711` "150 for 2"; namu "375개로 5개" |
| **3. Worth (estimate)** | a valuation per trace | 20 / 100 / 300 | vsfan `Value` column |

**Axes 1 and 2 are cross-validated exactly.** `199711` gives 150 chips / 2
traces = **75.0000** chips per trace. namu gives, for Beckhen (3★), "375개로 5개
얻을 수 있으니" = 375 chips / 5 traces = **75.0000** chips per trace. **Exact
agreement, from a byte-verified English 2017 guide and a Korean page rendered
2026.** That is a genuine two-source, two-language corroboration of a trace
*price* — and it is new to this project.

A **third** grade-indexed price, again from namu item page §2.5:

> 참고로 ★4헌터 흔적의 구매 가격은 **훈장 700당 흔적 8개**이며 ★3헌터 흔적의
> 구매 가격은 **훈장 350당 흔적 8개**다.

→ **87.50** honor/trace (4★) and **43.75** honor/trace (3★), an exactly **2.0×**
step from 3★ to 4★.

**A trap worth naming:** the *price* step 4★:3★ = **2.0×** and the *requirement*
step 4★:3★ = 160/80 = **2.0×** are the same ratio. They are still **not** the
same quantity — different currency, different physical kind (a price you pay vs
a count you must hold). Ratio agreement is not identity, and collapsing them
would be the same class of error as the one being adjudicated.

### 3.4 Same-axis check: which is wrong, if either?

If namu and vsfan were both claiming the requirement:

| grade | local fixture | namu | vsfan | vsfan ÷ namu |
|---|---:|---:|---:|---:|
| 1★ | 10 | 20 | 20 | 1.00× |
| 2★ | 20 | 40 | 100 | 2.50× |
| 3★ | — | 80 | 300 | 3.75× |

vsfan ÷ namu is **not a constant scale factor** (spread 1.00 → 3.75), so at most
one could be the requirement. Two independent structural facts break the tie in
favour of namu:

- **namu ships a formula** — `(2^n)×10개` with `n` defined as the grade — and a
  worked example that reproduces the native `floor` divisor. **vsfan ships no
  formula**: ratios ×5 then ×3, `20 × (1,5,15)`, no standard sequence.
- **vsfan's own page contradicts its own column**: it prices FC traces at **75**
  per 3★ and **37.5** per 2★ (a 1:2 ratio) while its `Value` column says 300 and
  100 (a 1:3 ratio). A price column and a worth column cannot both be right
  about the same shop — and the `199711`/namu agreement at **exactly 75** chips
  per 3★ trace independently confirms 75 is the real FC price.

**Q2 ANSWER: yes, both can be true, because they are on different axes. The
defect was never in the sources — it was that the project was not labelling
which axis each numeral lives on, and (per §3.1) had mis-attributed one source
in the process.**

---

## 4. Q3 — Is the replica's flat 10/20 contradicted, and by how much?

### 4.1 Yes — by exactly a factor of 2.0, at both published points

Fixture, read-only from `server-ts/src/hunter-traces.ts:9-10`:

```ts
{ id: "local_gerard_trace",    cardId: "005", rank: 2, collect_qty: 20 },
{ id: "local_sylvester_trace", cardId: "006", rank: 1, collect_qty: 10 },
```

Grade check against `cards.json` (independent of the fixture's own `rank` field):
Sylvester `rarity = 1`, Gerard `rarity = 2` — **the fixture's rank field is
correct**. The fault is the magnitude, not the indexing.

| grade | fixture | namu | namu ÷ fixture | verdict |
|---|---:|---:|---:|---|
| 1★ | 10 | 20 | **2.0000** | fixture 2× low |
| 2★ | 20 | 40 | **2.0000** | fixture 2× low |
| 3★ | (none) | 80 | — | unpublished in fixture |
| 4★ | (none) | 160 | — | unpublished in fixture |

**Spread of the ratio across both points: 0.00e+00 — exactly constant.**

This is the strongest quantitative finding in the lane, and it is stronger than
the existing `factor-2 NOT UPHELD` verdict could express. That verdict was
recorded on 2026-10-05, when the only ladder source was namu and its semantics
had not been quoted. Three things have changed since:

1. namu's requirement sentence is now quoted **verbatim in the original
   language** from the canonical render, not paraphrased.
2. namu now also supplies the **`floor(owned/collect_qty)` worked example**,
   which matches native `Gce125c` — so namu is describing the *same operation*
   the client performs, not merely a similar number.
3. **A second namu page** independently organises traces by grade
   (`5.1 1★ / 5.2 2★ / 5.3 3★ / 5.4 4★`), and a third gives grade-indexed prices.

The constant-2 signature — which `trace-rarity-vote` §2.3 correctly identified as
the *motivation* for the factor-2 claim, and which that note then said only the
namu-vs-fixture pair exhibited — is now supported by a source whose semantics are
independently corroborated. **The factor-2 reading is UPHELD as the best
available reading of the evidence; it is still not a recovered original value.**

### 4.2 What a doubling would actually do inside the replica (read-only inspection)

`server-ts` was **not modified** and the build was **not run**. The following is
source inspection only, and one of my own earlier claims had to be corrected
during it.

**Self-consistent, no deadlock.** Both sides of the guided tutorial read the
*same* constant:

| site | code |
|---|---|
| `src/search-battle.ts:8` | `GUIDE_TRACE_QTY = HUNTER_TRACE_ITEMS.find(cardId==='006').collect_qty` → **10** |
| `src/search-battle.ts:214` | a guided victory awards exactly `GUIDE_TRACE_QTY` |
| `src/trace-exchange.ts:30` | `debit = count * trace.collect_qty` → **10** for `cnt:1` |
| `src/state.ts:1283` | the tutorial `Clear(37,1)` calls that same exchange |

Today: 10 awarded, 10 required. At `collect_qty = 20`: 20 awarded, 20 required.
**The guide cannot deadlock from this change.** (My first draft asserted the
opposite — that doubling would strand the tutorial. That was wrong, and reading
the call sites rather than inferring them is what caught it.)

**A real migration hazard does exist, and it is not the deadlock.**
`src/search-battle.ts:57` validates an **already-settled persisted receipt**
against an allowlist derived from the same constant:

```ts
const quantities = value.last.attempt.guided ? [1, GUIDE_TRACE_QTY] : [1];
… !quantities.includes(row.added)  →  throw "Malformed Search reward"
```

Any account that already settled a guided receipt with `added = 10` will **throw
on state load** once `GUIDE_TRACE_QTY` becomes 20, because 10 is no longer in
the allowlist. That is a hard load-time failure, not a soft economic change, and
it must be handled as a state migration.

**Second, milder effect.** An **ordinary** (non-guided) victory awards a
hardcoded literal **1** trace (`search-battle.ts:214`, else-branch). At
`collect_qty = 10` that is 10 ordinary victories per Sylvester; at 20, it is 20.
Purely economic — no code path depends on the literal.

**Blast radius, verified.** Only three production sites in two files read
`collect_qty` (`trace-exchange.ts:28`, `trace-exchange.ts:30`,
`search-battle.ts:8`). **But tests do pin the literals**, and this corrects a
second claim of mine:

| site | assertion |
|---|---|
| `tests/guided-search-recruitment.ts:34` | `trace.qty === 10` |
| `tests/guided-search-recruitment.ts:43` | `consume_result.item` `qty === 10` |
| `tests/trace-exchange.ts:35` | `trace.qty === 20` |
| `tests/trace-exchange.ts:65` | `consumed_inst_list` `qty === 20` for `cnt:2` |
| `tests/trace-exchange.ts:24-33` | loops **exactly 20** Search victories to accrue those traces |
| `tests/guided-search-recruitment.ts:20-30` | loops **exactly 10** |

So a doubling breaks **four literal assertions plus two loop trip counts** across
two test files. That is the real cost, and it belongs to whoever owns
`server-ts`.

### 4.3 What is *not* contradicted

Nothing native, nothing measured. **No `[NATIVE]` or `[ORIGDATA]` anchor for
`collect_qty` exists.** namu is `[COMM]`, **one source**, and its page is dated
**2026-10-03** — i.e. **after the 2019-09-05 rebalance** — while the fixture
carries **no era tag at all**. The 4,208 pool is 2018-02 (pre-rebalance) but
measures supply, so it cannot date the requirement either way.

**Verdict: the fixture IS contradicted by the best available evidence, by a
clean constant factor of 2.0. It is NOT proven wrong.** Per `AGENTS.md` §15 the
distinction is load-bearing, and the era gap is unresolved.

---

## 5. Q4 — Grade-gating, and the interaction with 4,208

### 5.1 The grade axis is real and is the requirement's own axis

**namu hunter page §1.4** — quoted in §3.2 — indexes the requirement *by grade*.

**namu item page**, section headers read from the stored render, plus the
organising sentence:

```
5. 헌터 흔적  [수집 시 해당 헌터 획득 가능]
  5.1. 1★   5.2. 2★   5.3. 3★   5.4. 4★
  각 흔적은 등급(★)별로 나눈 다음에 한국어 어순으로 정리했다.
```

*"each trace is split by grade (★), then sorted in Korean word order."*

**Source 2 is CORRECT** that a grade axis exists and is separate from worth.
One refinement: the grade axis is not *independent* of the requirement — it
**indexes** it. It is independent of the *worth* ladder (20/100/300), which is a
different quantity on a different axis.

### 5.2 Is the exchange grade-gated? **Yes**, on converging evidence

**CORRECTION TO THE BRIEF.** The brief says "namu says the **Mirage** shop sells
specifically 3성 헌터 흔적". Both halves were tested against all **67** recovered
namu dump files (271 `흔적` occurrences):

| term | hits |
|---|---|
| `3성 헌터 흔적` ("3★ hunter traces") | **exactly 1**, in `ctrl-d-main` |
| `미라주` ("Mirage") | **0 in all 67 files** |

The single hit, in full context, is the **신기루 유적지** (Sin-gi-ru ruins) shop:

> 이것을 모아 라피스의 마켓이나 신기루 상점에서 특급 의뢰서, 메트론 결정체, 강화
> 재료, 도구 상자, 고급 도구 상자, 결정, **3성 헌터 흔적**, **할리**[fn30: 4성
> 헌터이다]**의 흔적**을 구매할 수 있다.

The shop is **신기루 / 라피스의 마켓 (Lapis's Market)**, *not* "Mirage". The
Mirage attribution is unsupported as stated. (신기루 and the project's Mirage
Ruins are plausibly the same place, but the corpus does not say so and this lane
does not assume it.)

What the sentence *does* establish: the shop stocks a **generic "3★ hunter
traces" line** plus one **named 4★ (Harley)** at a separate line. That is
**grade-partitioned merchandise** — strong support for a grade-gated exchange,
though by itself it does not prove the exchange *rejects* a mismatched grade.

Two further independent grade-gatings, both on the item page:

| evidence | reading |
|---|---|
| §2.5: ★4 = 700 honor / 8 traces; ★3 = 350 honor / 8 traces | the **price** is grade-indexed, exactly **2.0×** |
| §3.3 Table 17: 헌터 등급 1성/2성/3성 → 헬륨 소비량 **2 / 8 / 15**, 수색 가능 횟수 **5 / 4 / 2** | the **trace search** is grade-gated *separately* from the exchange |

So grade gates the system in **three** places — requirement, purchase price, and
search cost — which is the parsimonious reading of the whole item page.

### 5.3 Does 4,208 interact with the exchange? **No**

- The pool is **rarity-weighted supply** (67.8 / 25.6 / 6.6 % by grade,
  *decreasing*); the requirement is **grade-indexed** (1 : 2 : 4 : 8,
  *increasing*). **Opposite direction** (§2.3).
- A per-hero requirement is a **4-valued** function; the pool is a **355-valued**
  spread with no recoverable mapping (§2.4).
- The pool is 2018-02 and self-described as approximate.

The only real interaction is **correlational and about membership, not cost**:
4,208 tells you *which* heroes were in the drop pool at all (37 of 44 rows; the
other 7 are event/special hunters the poster excluded by name).

---

## 6. Standing refusals — checked, not violated

| refusal | compliance |
|---|---|
| **`fc-native` §1.4** — forbids setting honor values from arena reward tables | **COMPLIANT.** This lane *used* the namu guild-honor **trace price** (700/8, 350/8). That is a **shop price for an item** read from a community wiki, **not** an arena honor award. No honor award value is proposed, derived, recommended for adoption, or applied anywhere. |
| **`exp-ladder` §4** — forbids conflating RankUp gold with the star-advancement ladder | **COMPLIANT.** Neither RankUp nor the advancement ladder is touched. Trace `collect_qty` is a third, distinct quantity. |
| **`server-ts` read-only** | **COMPLIANT.** No file under `server-ts` was edited; the build was not run. All inspection was `read`/`grep`. |
| Coverage counters | **UNMOVED** — heroes 1/113, accessories 1/100, monsters 0/22. No base stat appears in this file. |
| `polluted-observations.md` | **NOT appended**, per instruction — the parent mirrors it. |

---

## 7. What would settle each remaining ambiguity

| # | open question | what would settle it | cost |
|---|---|---|---|
| **1** | Is the fixture's factor-2 error real? | **One in-game 확정 섭외 screen.** A single native screenshot of the trace-exchange panel showing `N traces required` for a 1★ and a 2★ hunter. This reads `collect_qty` **as rendered by the original client** and would convert the whole question from `[COMM]` to `[ORIGDATA]`. | **Highest value by far.** The panel is in the 정상 game flow; a player-level capture settles it outright. |
| **2** | Pre- vs post-2019-09-05 rebalance? | The same panel from a **2018-vintage** capture (the 2019-09-05 announcement did not mention traces, which is weak negative evidence, not proof). | Archive hunting; low prior of success. |
| **3** | Does the exchange *reject* a grade mismatch? | Native `CSRAchieve`/`RequestShardExchange` decompile: does the server receive the grade, or only `item_inst_id`? If only the item, grade-gating is **server-side by item identity** and no client check exists. | Ghidra, one function. |
| **4** | Is `collect_qty` ever per-hero rather than per-grade? | The namu page gives one ladder for all grades and no per-hero modifier. A single hunter-specific trace cost in any source would falsify the grade-only reading. | Cheap to keep open; do not assume. |
| **5** | Original trace prices | The FC shop / guild-shop reference rows from the shipped client, if any survive in `REFEN/REFERENCE/GETITEM`. | Covered by the existing reference-cache scans (§145); treat as closed-negative unless a new corpus appears. |

**Nothing further in this lane can close #1.** It is a measurement the community
corpus structurally cannot supply, for the same reason the base-stat hunt could
not: the value was only ever visible inside the running client.

---

## 8. Recommended next action for the `server-ts` owner (not performed here)

**Do not change `collect_qty` yet.** The evidence justifies a *documented
decision*, not a silent edit:

1. Record the evidence state: namu is one `[COMM]` source, post-rebalance,
   self-consistent, with native-matching divisor semantics, contradicting the
   fixture by a constant 2.0×.
2. If adopting namu's ladder is wanted, it is a **3-site src change + 4 literal
   test assertions + 2 loop trip counts + a state migration** for already-settled
   guided Search receipts (`added = 10` would fail the `search-battle.ts:57`
   allowlist on load). That is a deliberate, reviewable change, not a fixture fix.
3. Do **not** attempt to derive per-hero costs from 4,208. §2 rules that out.
4. Keep the three axes labelled distinctly in any comment, so the next lane does
   not re-run this adjudication. The specific trap is recorded in §3.3: the
   *price* ratio and the *requirement* ratio are both 2.0× at 3★→4★, and
   collapsing them would be a category error.

---

## 9. Limits of this lane, stated

- **`server-ts` untouched; build not run.** Every claim about replica behaviour
  is source inspection, not execution. The test-assertion list is read from the
  test files, not from a test run.
- **The 44 forum rows were transcribed from the archived bytes by a probe
  script** and then reconciled against the mining note's table; both agree
  exactly, and C1/C2/C6 reproduce the published figures.
- **The three partitions were rebuilt from `cards.json`, which is itself
  community-sourced.** The rebuild matching the poster's cross-tab is therefore
  *strong corroboration of the grade/role/element axis*, not independent proof
  of it. It is a control on the harness and on the forum table's internal
  consistency; it is not a third source for the trace costs.
- **`20/100/300` was not re-fetched from the archived vsfan page.** It is used
  exactly as stored in `vsfan-wiki-2026-10-05.md` (byte-pinned to capture and
  oldid), and as already adjudicated by `trace-rarity-vote-2026-10-05.md`. This
  lane's contribution there is the *199711 mis-attribution*, which was tested
  against primary bytes.
- **namu re-read from stored renders, not re-fetched.** The raw dumps are
  byte-hashed in the prior lane's note; this lane verified `U+FFFD = 0` and
  enumerated every `흔적` occurrence rather than grepping for a preferred number.
- **No network fetch was performed in this lane.** All sources were already in
  the workspace, so the GUARD file's Wayback traps (HTTPS refusal, CDX false
  negatives, `im_` rewrites) were not re-encountered.
- **Era tags are the load-bearing limit on Q3.** namu = 2026-10-03 (post-rebalance);
  the forum pool = 2018-02 (pre); the fixture = untagged. A single
  era-segregated client screenshot (§7 item 1) would settle more than every
  remaining archive hunt combined.

---

*Written 2026-10-08 by a read-only adjudication lane. Coverage counters unmoved.
`server-ts` unmodified and unbuilt. `polluted-observations.md` not appended.*
