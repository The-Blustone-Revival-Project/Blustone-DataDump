# Is `combat_power` derivable from the archive's own stat block? (2026-10-06)

**Question.** `combat_power` (`戦闘力`) appears on **all 63** rows of
[`archived-hunter-database-2019.tsv`](archived-hunter-database-2019.tsv) next to
the twelve ability fields. If it were a computable function of those twelve, it
would (a) give an independent validator for the whole corpus, (b) possibly
explain the `≈1.72` core-stat scalar that
[`level-factor-test-2026-10-05.md`](level-factor-test-2026-10-05.md) §1.9 left
open, and (c) give a principled check on any candidate stat triple.

**Answer in one line.** It is **approximate and strongly informative
(`R² = 0.9964`, median error `0.68 %` of mean `cp`), but it is **provably not
exact** — no linear law of the twelve published fields reproduces it, and the
proof uses exact integer contradictions that rounding cannot absorb — so it
**cannot serve as a validator at the resolution that would matter**, and it
**does not explain the `2.7636` Strength scalar**.

---

## 0. Method, and the two controls that make the result trustworthy

Everything below is computed from the TSV alone, read-only. Prior fits quoted in
[`level-factor-test-2026-10-05.md`](level-factor-test-2026-10-05.md) §1.9
(`hp 3.049, atk 5.112, def 5.809`, max residual `236`, and the two
`18 336 / 18 955` predictions) are **reproduced, not redone** — §5 confirms they
to within the row-set difference (62 vs 59 deduplicated rows).

**Duplication handled as instructed.** 62 numeric rows (the 63rd, `056`, is the
`???` placeholder and carries no numbers):

| ledger | count |
|---|---:|
| numeric rows | 62 |
| distinct 12-field vectors | 59 |
| **exact-duplicate pairs (all 12 fields *and* `cp` equal)** | **3** — `059`/`001` (8359), `024`/`034` (8552), `026`/`004` (6664) |
| distinct `(hp,atk,def)` triples | 50 |
| rows that repeat an earlier triple | **12** |
| triples carrying **more than one** `cp` | **7** |

All three exact-duplicate pairs are costume variants of the same role
(`059`/`001` both `爆撃手` Bomber; `024`/`034` both `守備手` Defense;
`026`/`004` both `ヘルパー` Support), so element never confounds them. The
primary model is fitted on **n = 59** (duplicates collapsed); §3.3 re-fits on all
62 as a sensitivity check. This matches the task's warning exactly: 3 identical
pairs, 12 duplicated triples.

**Control 1 — the fitting harness recovers a known law.** A synthetic
`cp = 1234 + Σ Kᵢ·statᵢ` with integer `K` was pushed through the identical OLS
path. Intercept recovered as `1234.0`, all twelve weights recovered to `1e-6`,
RMSE `3.6e-12`, and `report()` returned `exact = 62/62`. A series that *is* exact
is measured as exact.

**Control 2 — the decisive test can detect success, not just failure.** The
headline test in §2 is an *exact-integer consistency* test, and a negative
result from such a test is worthless unless the test can also return positive.
A synthetic `cp` was therefore built from **four per-role linear substat laws**
on the *same real stat vectors*, and the same exhaustive search was re-run:

| role | equations | worst error | exact subsets found | verdict |
|---|---:|---:|---:|---|
| `攻撃手` Attack | 3 | `7.1e-15` | 256 | detected |
| `守備手` Defense | 2 | `0.0` | 511 | detected |
| `爆撃手` Bomber | 2 | `7.1e-15` | 128 | detected |
| `ヘルパー` Support | 2 | `0.0` | 320 | detected |

The harness reports "consistent" for every role when consistency exists, and
recovers non-trivial weights (`18.0`, `1.75`, `5.6` …). **The negative in §2 is a
property of the data, not of the test.** (The synthetic Attack result also shows
the test detects *existence*, not *uniqueness*: its 3 equations admit many exact
solutions, so a detected law pins only what the equations pin.)

---

## 1. First result: `cp` is not a function of the core triple at all

Seven of the fifty distinct `(hp,atk,def)` triples carry **more than one**
`combat_power`:

| `(hp,atk,def)` | rows |
|---|---|
| `(1277, 908, 576)` | `007`=6624, `014`=6653 |
| `(1521, 1021, 689)` | `039`=8437, `031`=8401 |
| `(1537, 817, 576)` | `019`=7574, `006`=7558 |
| `(1584, 718, 718)` | `022`=7329, `030`=7321 |
| `(1624, 839, 682)` | `032`=8550, `002`=8587 |
| `(1710, 828, 726)` | `060`=8200, `035`=8236 |
| `(1750, 883, 755)` | `037`=9909, `040`=9888 |

> **A single-scalar law of the core triple is therefore impossible at *any*
> precision.** This is stronger than the prior `1.715436 / 28 units` finding,
> which concerned the archive→panel *stat* comparison; for `cp` no `M` exists to
> search for. Per the task's instruction — state it and move to a multi-term form
> — §2 does exactly that.

For reference, the best single scalar on the sum is `M = 2.676567`, total
absolute error `32 449` cp units; OLS gives `cp = 4.542929·(sum) − 6026.69`,
RMSE `368.5` cp (**4.2 %** of mean). Core-only linear law: RMSE `348.75`,
worst row `053` at `−871.6` cp (**−8.58 %**).

---

## 2. The rigorous negative: **no exact linear law of the twelve fields exists**

### 2.1 The test (exact integers, no regression, no OLS)

For two rows sharing an identical `(hp,atk,def)` triple, *any* law that is
additively separable in the substats forces

```
(sub_a − sub_b) · w  ==  cp_a − cp_b          w = 9 substat weights
```

`cp` is an exact integer, so each of these is an **exact integer equation**.
Twelve rows form seven such pairs, giving nine usable equations (the three
identical-vector pairs confirm `Δcp = 0` and are consistent).

### 2.2 Two contradictions that rounding cannot bridge

Grouping the equations by their substat-delta vector:

| substat delta | pairs | observed `Δcp` |
|---|---|---|
| `crit_damage +5, block_damage_reduction −2` | `037`/`040` | **+21** |
| | `019`/`006` | **+16** |
| `block_damage_reduction −2, hp_regen +4` | `032`/`002` | **−37** |
| | `007`/`014` | **−29** |

The first row of that table is airtight. In *both* pairs the two heroes have the
**same absolute values** for the differing fields — `crit_damage` `205` vs `200`,
`block_damage_reduction` `40` vs `42`. So `floor()` semantics, fractional
weights, per-role tables or anything else of the form `Σ fᵢ(statᵢ)` must return
the *same* `Δcp` for the two pairs, and returns `+21` for one and `+16` for the
other. The gap is **5 cp**; `cp` is an integer, so the tolerance is `0.5`.
**Unbridgeable.**

### 2.3 Exhaustive search over every substat subset

All `2⁹ = 511` subsets were tested for exact consistency on the nine equations:

| | |
|---|---:|
| exactly consistent subsets | **0 of 511** |
| best worst-equation error | **17.67 cp** |
| best subsets found | `{crit_damage, block_damage_reduction}` → `(8.833, 17.25)`; `{crit_damage, penetration, block_damage_reduction}` → `(8.833, 0, 17.25)` |
| subsets whose least-squares weights are all non-negative | 287 of 511; best of those still `17.67` cp |
| **a non-negative exact law exists** | **no** |

Least-squares solution to all nine equations:
`block_damage_reduction 18.000`, `crit_damage 9.133`, `hp_regen 0.750`,
`speed −3.000`, `penetration 0`, `block 0`, `element_enhance 0`,
`element_resistance 0`. The clean `18.0` is real signal (§3.2), but it cannot be
reconciled across the contradictions.

### 2.4 A rigorous bound that does not depend on the above

For any least-squares fit, `max|residual| ≥ RMSE`. The 12-field OLS RMSE is
`80.80` cp, so **no linear law of the twelve fields can have a worst-row error
below `80.8` cp.** An exact law needs `0`. A feasible-point (subgradient,
box-constrained) search returns an upper bound of `226.85` cp on the min-max, so
the true minimax lies in **`[80.8, 226.9]` cp**. The prior note's "max residual
236 = 2.7 % of mean" is the same statement at `n = 62`.

### 2.5 Precise scope of the negative — what is and is *not* refuted

| claim | status |
|---|---|
| any law **linearly separable in the nine substats**, any weights (integer, real, negative) | **REFUTED** (§2.2) |
| the same, with per-`floor()` semantics | **REFUTED** — identical absolute field values, so `floor` is identical |
| the same, with per-role or per-element weight tables | **REFUTED** for the Attack role (§3.2) |
| a law with substat **interaction** terms (e.g. `block × crit_damage`) | **not refuted** by §2 — the two contradictory pairs differ in `block` (14 vs 20) and `element_enhance/resistance` (0 vs 5) |
| a law in which `cp` also depends on state the TSV does not record | **not refuted**, and **plausible** — see below |
| any function of the twelve fields whatsoever (a 59-entry lookup) | **not refuted**, trivially |

The last row is why the negative is stated as it is. The most economical
explanation for §2.2 is that **`cp` carries state the TSV does not contain**.
Every archive page names the hero's *associated* weapon/armor/accessory and
every row carries `gear_state = "not established"`. Two heroes with identical
published base stats and different gear would then carry different `cp` — which
is exactly the observed pattern. That hypothesis is **not tested here** and must
not be asserted; it is offered only as the hypothesis that would explain §2
without inventing a formula.

---

## 3. The best form, and what it costs

### 3.1 Winner: a linear weighted sum of all twelve fields, shared across roles

`cp = −7884.12 + 3.0603·hp + 5.2060·atk + 5.8217·def + 43.5644·speed
+ 33.0842·crit + 5.2763·crit_damage + 34.0118·penetration + 31.9338·block
+ 10.1295·block_damage_reduction − 16.6714·element_enhance
+ 10.4604·element_resistance − 4.9129·hp_regen`

| metric (n = 59) | in-sample | leave-one-out |
|---|---:|---:|
| RMSE | **80.80** | **125.92** |
| mean \|residual\| | 60.70 | 87.83 |
| median \|residual\| | 48.32 | 60.02 |
| p75 / p90 / p95 \|residual\| | 98.25 / 127.59 / 163.81 | 128.21 / 165.52 / 305.31 |
| **worst row** | **226.85** (`052`, +1.97 %) | **377.99** (`062`, −3.27 %) |
| within 0.5 % / 1 % / 2 % / 5 % | 42.4 / 71.2 / **96.6** / 100 % | 37.3 / 61.0 / 86.4 / 100 % |
| exact (≤ 0.5 cp) | 3 / 59 | 3 / 59 |
| `R²` (in-sample) | **0.99639** | — |

Residual distribution (in-sample, 25 cp bins) is unimodal and centred on zero
(bias `−0.00`, `sd 80.8`); it is **not** integer-quantised (fractional parts span
`0.002 … 0.486`), so there is no hidden `floor()` convention to recover. The
model beats every non-linear alternative tried: adding `sqrt(hp)`, `hp²`,
`log(hp)`, `atk/def`, `hp·atk/1000` all *reduce* in-sample RMSE (to `69.3`) but
*worsen* LOO RMSE (to `106.5` best case, and 149–153 for the others) — they fit
noise.

### 3.2 Model comparison — role-conditional weights look good and are overfitting

| model | k | in-sample RMSE | **LOO RMSE** | LOO max |
|---|---:|---:|---:|---:|
| **shared 12 weights + intercept** | 13 | 80.80 | **125.92** | 377.99 |
| + role intercepts | 16 | 70.38 | 152.62 | 639.34 |
| + role/element intercepts | 18 | 66.68 | 120.25 | 361.51 |
| + role + element + rarity intercepts | 21 | 48.86 | 111.36 | 346.97 |
| role-specific intercepts + role-specific `(hp,atk,def)` + shared substats | 25 | 34.43 | 231.31 | 1646.50 |
| shared core + per-role substat weights | 40 | 45.23 | 337.17 | 1311.71 |
| per-role full 12-weight model | 52 | **20.27** | **294.28** | 1216.94 |

The fully role-conditional model reaches in-sample RMSE `20.27` — four times
better — and its LOO RMSE is `294.28`, **2.3× worse** than the shared model. With
59 rows and 52 parameters it is interpolating. **The honest best model is the
shared one.** Role-conditional substat weights are *licensed* by §3.3 but not
*supported* by 59 rows.

### 3.3 The within-role exact constraints — the one clean structural finding

Running the §2 test inside each role (exact integers, still no regression):

| role | equations | worst error | exact subsets | exact solution |
|---|---:|---:|---:|---|
| `守備手` Defense | 2 | `0.000` | 511 | **every substat weight is 0** (all three same-core pairs give `Δcp = 0` despite non-zero substat deltas) |
| `爆撃手` Bomber | 2 | `0.000` | 128 | `block_damage_reduction 18.000`, `hp_regen 1.750`, rest 0 |
| `ヘルパー` Support | 2 | `0.000` | 320 | `crit_damage 5.600`, `block_damage_reduction 18.000` (one of several) |
| `攻撃手` Attack | 3 | **`2.500`** | **0** | **none** |

**`block_damage_reduction = 18` recurs independently in Bomber and Support.**
That is a genuine, exactly-determined integer recovered from the data, not a
regression artefact. It is the single most concrete thing this study produces.
It is *not* a client-recovered value and must stay labelled as such.

Attack is the role that fails: `5·w_crit_damage − 2·w_block_damage_reduction`
would have to equal **both** `16` (`019`/`006`) and `21` (`037`/`040`).

### 3.4 Sensitivity: duplicates kept (n = 62)

Refitting on all 62 rows reproduces the prior note's weights
(`hp 3.0487, atk 5.1123, def 5.8088`) — hence its `18 336` in §5 — and moves
RMSE `80.80 → 82.60`, LOO `125.92 → 129.88`, worst in-sample `226.85 → 236.02`.
Deduplication changes no conclusion. (The intercept is the only unstable
coefficient: `−7884 → −7769`, a shift of `115`.)

---

## 4. Which rows fail to fit

In-sample `|residual| > 150 cp` under the §3.1 law:

| row | role | ★ | element | `cp` | predicted | residual | % |
|---|---|---:|---|---:|---:|---:|---:|
| `052` Storm | `攻撃手` | 4 | `電撃` | 11 504 | 11 277.1 | **+226.9** | +1.97 % |
| `062` Juno | `守備手` | 3 | `火炎` | 11 556 | 11 732.9 | **−176.9** | −1.53 % |
| `063` Eris | `守備手` | 4 | `電撃` | 12 725 | 12 548.1 | **+176.9** | +1.39 % |
| `026` Tyltyl | `ヘルパー` | 1 | `電撃` | 6 664 | 6 501.6 | **+162.4** | +2.44 % |

Next band (`116 … 136 cp`): `016` +136.4, `061` −130.5, `037` +126.9,
`007` +126.6.

**The residual is structured by rarity, not by row:**

| `rarity_on_draw` | n | bias | s.d. | worst \|res\| |
|---:|---:|---:|---:|---:|
| ★1 | 11 | +26.1 | 103.4 | 162.4 |
| ★2 | 10 | −10.4 | 65.5 | 116.0 |
| ★3 | 33 | −23.2 | 59.7 | 176.9 |
| **★4** | **5** | **+116.2** | 89.0 | **226.9** |

The law systematically **under-predicts the ★4 band by ~1 %**. That is the
highest-stakes band for a rebalance study and it is the band with only five rows
— so the mis-fit is neither noise nor fixable from this corpus. By role the
biases are small (Attack `+0.4`, Bomber `−10.0`, Defense `−11.8`, Support
`+24.1`). By capture date they are small and unstructured
(`20191015` n=29 bias `+5.5`; `20191209` n=4 bias `−40.5`; Welch *t* between the
October batch and all later captures is **0.50**), so **the residual is not
explained by the archive spanning multiple capture versions** — a version-change
explanation is not available.

---

## 5. The `1.72` / `2.7636` question: cp does **not** explain it

Fed the archive `051` row (1678/864/660) with its own substats, the §3.1 law
predicts **8 722** against an actual `cp` of **8 709** — error `+13`, i.e. the law
reproduces the archive row essentially exactly.

Fed the same substats with the Lv.30 panel core (`2879 / 1471 / 1149`) and the
panel's actual Strength `24 068`:

| | |
|---|---:|
| law prediction | **18 404** |
| actual | **24 068** |
| shortfall | `−5 664` = **−30.8 %** of the prediction, **−23.5 %** of the actual |
| measured Strength scalar `24068/8709` | **2.7636** |
| measured core-sum scalar `5499/3202` | **1.7174** |
| observed `Δcp / Δ(sum)` | **6.687** cp per stat point |
| the law's own marginal slope on the core sum | **14.088** cp per stat point |

The observed rate is **2.11× smaller** than the slope the law itself implies, so
**the law cannot produce the Strength step.** My `18 404` reproduces the prior
note's `18 336` (small difference from 62-vs-59 rows) and its `18 955` for the
two-term `4.54293·sum − 6026.7` law — **both prior figures stand**. Conclusion
unchanged from `level-factor-test-2026-10-05.md` §2.1: the `≈1.72` is measured,
its mechanism is **unknown**, and `cp` adds no leverage on it. `cp` is a
different quantity from the Lv.30 panel's `Strength`.

---

## 6. Can `cp` be used as an independent validator? **No, not at useful resolution**

A `cp` value can only certify a candidate triple if the law's error on that row
is smaller than half the distance to every other row's `cp`. Leaving one out:

| quantity | value |
|---|---:|
| LOO \|error\| mean / median / p90 / max | 87.8 / **60.0** / 165.5 / 378.0 cp |
| median nearest-other-`cp` gap in the corpus | **24 cp** |
| median `2 ×` LOO error | **120 cp** |
| rows where the nearest other `cp` is farther than `2 ×` own error | **14 / 59** |

So `cp` **cannot** separate heroes: `57` distinct `cp` values over `59` rows, the
adjacent-`cp` gap has median `44` and minimum `2` cp, and the law's median error
is `60` cp — roughly **three times** the typical spacing.

Worse for the stated purpose, the rows actually implicated in the §2
contradictions are **not** reliably flagged:

| row | LOO residual | flagged? |
|---|---:|---|
| `019` | −44.6 (−0.59 %) | no |
| `006` | −56.7 (−0.75 %) | no |
| `032` | −0.7 (−0.01 %) | no |
| `002` | −4.1 (−0.05 %) | no |
| `037` | +145.3 (+1.47 %) | yes |
| `040` | +123.8 (+1.25 %) | yes |
| `007` | +146.8 (+2.22 %) | yes |
| `014` | +132.6 (+1.99 %) | yes |

Four of the eight implicated rows pass cleanly. A residual-threshold "suspect
row" rule would therefore be close to a coin flip on exactly the defect class it
was proposed to catch — the same false-positive class that produced the
Captain-`009` refutation. **Recommendation: `cp` may be used only as a coarse
`±5 %` band check; it must not be used to accept or reject a specific triple, and
it must not be cited as recovered evidence for any weight.**

---

## 7. Separate check: does `(rarity, role)` determine the triple?

**No — not even approximately, and adding element does not rescue it.**

| lookup key | groups | groups holding >1 distinct triple | groups needed for an exact map |
|---|---:|---:|---:|
| `rarity` | 4 | **4** | 62 |
| `role` | 4 | **4** | 62 |
| **`(rarity, role)`** | **14** | **14** | 62 |
| `(role, element)` | 12 | 12 | 62 |
| `(rarity, role, element)` | 38 | **13** | 62 |
| `catalog_id` (trivial) | 62 | 0 | 62 |

**All 14 `(rarity, role)` cells are ambiguous.** Smallest cases hold two triples
(★1 Support `1467/660/715` vs `1467/679/679`; ★1 Bomber `1277/908/576` vs
`1277/944/540`). Largest:

| cell | n | distinct triples |
|---|---:|---:|
| ★3 `守備手` Defense | 9 | 8 |
| ★3 `攻撃手` Attack | 11 | 10 |
| ★3 `爆撃手` Bomber | 7 | 5 |
| ★3 `ヘルパー` Support | 7 | 6 |
| ★4 `攻撃手` Attack | 3 | 3 |

So the corpus is **less constrained than a small `(rarity, role)` lookup would
suggest**, and the exceptions are not a tidy minority — they are *every* cell.
`rarity` alone: ★3 alone contributes **29 distinct triples from 34 rows**.

**What *is* nearly determined is HP.** `rarity_on_draw` counts `1★ 12, 2★ 11,
3★ 34, 4★ 6` across all 63 rows; the `???` placeholder `056` is a `4★` row, so
the 62 numeric rows are `12 / 11 / 34 / 5` and the 59 deduplicated observations
are `11 / 10 / 33 / 5` (each of the three collapsed pairs is one `1★`, one `2★`
and one `3★`). `role_ja` takes exactly four values (`攻撃手` Attack,
`守備手` Defense, `爆撃手` Bomber, `ヘルパー` Support). Seven of the fourteen
`(rarity, role)` cells give a **single** HP value, and in every cell ATK and DEF
still take two or more values:

| cell | n | HP values | distinct ATK | distinct DEF |
|---|---:|---|---:|---:|
| ★1 `ヘルパー` | 3 | `[1467]` | 2 | 2 |
| ★1 `攻撃手` | 3 | `[1537]` | 2 | 2 |
| ★1 `爆撃手` | 3 | `[1277]` | 2 | 2 |
| ★2 `ヘルパー` | 3 | `[1584]` | 2 | 2 |
| ★2 `守備手` | 3 | `[1624]` | 2 | 2 |
| ★2 `攻撃手` | 3 | `[1624]` | 2 | 2 |
| ★2 `爆撃手` | 2 | `[1395]` | 2 | 2 |
| ★1 `守備手` | 3 | `[1537, 1624]` ✗ | 3 | 3 |
| ★3 `ヘルパー` | 7 | `[1710, 1742]` ✗ | 4 | 4 |
| ★3 `守備手` | 9 | `[1606, 1750, 1790, 1821, 1923, 1968]` ✗ | 6 | 6 |
| ★3 `攻撃手` | 11 | `[1678, 1750, 1790, 1821]` ✗ | 7 | 7 |
| ★3 `爆撃手` | 7 | `[1521, 1560]` ✗ | 5 | 5 |
| ★4 `守備手` | 2 | `[2019, 2033]` ✗ | 2 | 2 |
| ★4 `攻撃手` | 3 | `[1923, 1955]` ✗ | 3 | 3 |

**HP band** — **20 distinct values over 62 rows**, band `1277 … 2033`, matching
the prior note exactly. 13 values are shared by ≥2 rows, covering **55 of 62**
rows (`1750` ×11, `1624` ×7, `1710` ×6, `1521` ×5, `1537` ×5). Quantised
`HP` bands per rarity are cleanly graded and **do not** discriminate level
(`★1 1277–1624`, `★2 1395–1624`, `★3 1521–1968`, `★4 1923–2033`), confirming
the prior note §1.5. Bands per **role**, however, are strongly separated at the
low end and are the sharpest role signal in the corpus:

| role | n | HP band |
|---|---:|---|
| `爆撃手` Bomber | 12 | **1277 … 1560** |
| `ヘルパー` Support | 13 | **1467 … 1742** |
| `攻撃手` Attack | 20 | 1537 … 1955 |
| `守備手` Defense | 17 | 1537 … 2033 |

This quantifies the prior note's qualitative "Bombers low HP / high ATK,
Supports narrow": the Bomber and Attacker bands overlap only in the 23-HP window
`1537 … 1560`, and **10 of the 12 Bombers sit at `1521` or below**; Support is the
narrowest band (spread `275`, versus Bombers' `283`, Attackers' `418` and
Defenders' `496`).

---

## 8. Bottom line

1. **`combat_power` is NOT exactly derivable** from the twelve published stat
   fields. Refuted for any additively-separable-in-substats law, at any precision,
   by two pairs of heroes with identical absolute substat values and `Δcp`
   differing by 5 cp (§2.2), and confirmed by `0 / 511` consistent subsets and a
   rigorous `max|residual| ≥ 80.8 cp` bound (§2.3–2.4). This is a **negative
   result** and it closes the question as posed.
2. **It IS approximately derivable**, as a plain weighted sum of all twelve
   fields: `R² = 0.99639`, in-sample RMSE `80.80` cp, LOO RMSE `125.92` cp,
   median error `0.68 %` of mean. **Worst row: `052` Storm, `+226.9` cp
   (+1.97 %)** in-sample; `062` Juno, `−378.0` cp (−3.27 %) under leave-one-out.
   Four rows exceed `150 cp`: `052`, `062`, `063`, `026` — and the whole ★4 band
   is biased `+116.2` cp.
3. **It cannot serve as the independent validator the corpus needs.** Median
   `2 ×` LOO error (`120` cp) is three times the median spacing between distinct
   `cp` values (`44` cp); only `14 / 59` rows are separable at all; and four of
   the eight rows genuinely implicated in the contradictions pass the residual
   test cleanly.
4. **It does not explain the `1.72` / `2.7636` step.** The observed
   `Δcp/Δ(sum) = 6.687` is `2.11×` below the law's own marginal slope of
   `14.088`. The prior note's `18 336` and `18 955` predictions both reproduce.
5. **The one hard, exactly-determined artefact recovered:**
   **`block_damage_reduction = 18`** in `cp` units, derived independently and
   exactly from both the Bomber and the Support collision pairs. A portal-derived
   integer, **not** `[RECOVERED]` client evidence.
6. **`(rarity, role)` does not determine the triple** — all 14 cells are
   ambiguous; `(rarity, role, element)` still leaves 13 ambiguous groups. It
   *nearly* determines HP (7 of 14 cells single-valued). The 20-value HP band
   `1277 … 2033` is shared by 55 of 62 rows and grades cleanly by rarity but
   separates cleanly by **role** at the low end.

## 9. Recommended next probes, in order of value

1. **Recover the client's own power formula from native code.** The project
   already has two candidates in its symbol table — `CSRPlayData::CalcTotalBP`
   and (per the §16 crash-probe history) a `CalcTotalPower`-class symbol. This
   is now the *only* route to an exact law, and it would settle §3.3's
   `block_damage_reduction = 18` and the ★4-band bias at once. The 62 archive
   `cp` values then become a **test set** for the recovered weights.
2. **Test the "cp includes unrecorded gear" hypothesis** (§2.5). The archive
   pages name each hero's associated weapon/armor/accessory; if two
   same-base-stat heroes with different named gear systematically differ in
   `cp`, the negative in §2 is explained without any new formula. This is a
   bounded web check on data already cited in
   [`archived-hunter-database-2019.md`](archived-hunter-database-2019.md), and it
   decides whether `cp` can ever validate a base-stat row.
3. **Re-examine `019` and `037`** (or `006` and `040`) against their live archive
   captures. These four rows carry the §2.2 contradiction. If one transcription
   is wrong, the global negative may weaken to "no exact law found" rather than
   "no exact law exists" — which would materially change §8.1.
4. **Do not** implement any fitted weight from §3.1 as game balance. It is a
   portal-side descriptive fit with a 2.8 % worst-row error and a structural
   ★4 bias.

## 10. Files touched, and standing prohibitions

**Written:** this file only. Temporary scripts live outside the repo
(`%LOCALAPPDATA%\Temp\opencode\cpfit\`).

**Read-only:** [`archived-hunter-database-2019.tsv`](archived-hunter-database-2019.tsv),
[`archived-hunter-database-2019.md`](archived-hunter-database-2019.md),
[`level-factor-test-2026-10-05.md`](level-factor-test-2026-10-05.md),
[`GUARD-encoding-and-archive-traps.md`](GUARD-encoding-and-archive-traps.md),
[`coverage.md`](coverage.md).

**Not touched:** the TSV, `coverage.md`, `polluted-observations.md` (**not
appended**), `README.md`, any `analysis/catalogue/**` file, `server-ts`, fixtures,
seeds, the APK, the emulator, the physical phone, Ghidra.

**Standing prohibitions, carried forward.**
- Do **not** quote `block_damage_reduction = 18` as a recovered client constant.
  It is derived from a fan portal's published numbers.
- Do **not** use `cp` to accept or reject a candidate `(hp,atk,def)` triple, or
  to reconstruct a missing triple by inversion. §6 quantifies why.
- Do **not** implement a per-level stat factor. Nothing here changes
  `level-factor-test-2026-10-05.md` §2.7: the `≈1.72` is measured, its mechanism
  is unknown, and the server's level curve stays a declared local fixture.
- Do **not** treat the ★4-band bias as a rebalance signal. Five rows, portal
  data, unexplained by capture date (`t = 0.50`).
- Do **not** re-open the Captain-`009` ATK anomaly from this note. Untouched
  here; §1's result (`cp` is not a function of the core triple) says nothing
  about it either way.
