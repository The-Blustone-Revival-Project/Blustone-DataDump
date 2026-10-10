# T1 is MEASURED (×1.0994) — and that forces an open choice between two scaling models

**Written:** 2026-10-08. **Origin:** two lanes independently found and read the
*same* previously-unread image — `capa2-1024x911.jpg`, from the official Japanese
guide (`blustone.jp`), 2018-11, **pre**-2019-09-05 rebalance. They obtained
identical numbers, which is cross-validation rather than duplication:
`transcendence-t1t2-hunt-2026-10-06.md` and `grade-vs-level-factor-2026-10-06.md`.
Parent re-derived every figure below from the raw ratios.

---

## 1. The measurement

The キャパ超越 (Capacity Transcendence) receipt screen carries three per-stat
deltas. `hero-panel-level-extraction-2026-10-06.md` had recorded only the
`戦闘力` token from this frame and listed the article as having "no stat block".
It does.

| | before | after | ratio |
|---|---:|---:|---:|
| ATK | 365 | 401 | **1.098630** |
| DEF | 423 | 465 | **1.099291** |
| HP | 619 | 681 | **1.100162** |

**T1 = 1.0994 ± 0.0012**, internal spread **0.1393 %** (re-derived: 0.1393 %).
Second-tightest consistency in this project, behind only Hermes' 0.11 %.

**It is positively labelled T1, not inferred.** The same frame's cost panel reads
crystals **9/9**, fragments **449/90**, gold **9000** — the vsfan
`Guide_to_Blustone` ★3 **T1** row (9 / 90 / 9 000) exactly, and not T2
(30/300/30 000) or T3 (80/800/80 000). The cost row is now corroborated by the
game's own receipt.

**Gear-free.** Equipment unlocks at ★4 and the hero is ★3, so gear contamination
is structurally impossible here.

**Consequence for the ladder.** Measured T1 = 1.0994 sits **0.055 %** from the
hypothesised `1.10` and **4.70 %** from `1.05`. The `1.05/1.18/1.30` degeneracy is
**excluded**. The `1.10 / 1.20 / 1.30` ladder survives — but only its T1 rung is
now measured; **T2 and T3 remain untested.**

---

## 2. The open question this creates — two models, one discriminator

The measurement does **not** settle how the rungs combine, and the two candidate
models are *not* the same function:

| model | rule | T1 | T2 | T3 |
|---|---|---:|---:|---:|
| **(A) compounding** | each rank-up multiplies the *current* value | 1.0994 | **1.2087** | **1.3287** |
| **(B) from base** | each level multiplies the *base* value | 1.0994 | **1.2000** | **1.3000** |

**What favours each:**

- **(B) fits the numbers.** Hermes' T3 table reads **×1.30000 exactly**, and Riko
  ×1.274. Under (A), T3 = 1.3287, so both would be low by 4.1 % / 2.2 %.
- **(A) fits the prose.** The article's own text says capacity transcendence is
  applied once per rank-up, max 3× — which is compounding, giving the ×1.3287
  ceiling. `grade-vs-level-factor` derived that ceiling from the article.
- **Measured T1 cannot separate them** — it is the first rung either way.

**A compounding ladder `1.10 × 1.20 × 1.30` predicts T3 = 1.7160, which is not
close to any measured T3 (1.274 / 1.300 / 1.3287).** That is the real reason the
old `1.716` figure never fit, and it is worth stating plainly: the factors are
**not** cumulative multipliers of one another. Parent-verified.

> ### ⇒ **A single T2 observation is now the highest-value target in this project.**
> It separates the models immediately: **(A) predicts 1.2087, (B) predicts
> 1.2000** — a 0.73 % gap, but a real and decidable one on a three-stat panel with
> a 0.139 % internal spread.

---

## 3. A second, independent finding: `戦闘力` is a composite, not a stat scale

Under the *same* single operation that moved all three stats by ×1.0994, `戦闘力`
moved `2326 → 2704` = **×1.162511**, i.e. **+5.744 % faster** than the stats it
must derive from. A linear function of HP/ATK/DEF cannot do that.

This **proves** `戦闘力` is not linear in the three core stats — previously only
inferable — and it retro-explains why the archive's `戦闘力` column and the
in-game one will not reconcile (ratios 0.2323 / 0.3237 / 0.6379 across three
same-rarity heroes). The `×1.162511` figure should be read as a **rating ratio**,
not a stat factor. Confidence "high" is demoted.

## 4. Narrowing the Captain `009` anomaly, not resolving it

T1 scales ATK, DEF and HP **identically** to 0.139 %. Therefore **any
field-specific ATK effect must appear only *after* T1** — a pure
"ATK scales differently" story cannot explain Captain's ATK ratio of 1.1688
against its own HP/DEF 1.2740 / 1.2788. Captain remains unresolved, but the
hypothesis space is smaller.

## 5. The sharpest negative: the archive's 62 rows may be on a *different basis*

Comparing archive `036` Bear against this in-game ★3/Lv.1 reading:

| | archive | in-game Lv.1 | ratio | implied per-level over 29 |
|---|---:|---:|---:|---:|
| HP | 1923 | 619 | **3.1066** | 1.039861 |
| ATK | 755 | 365 | **2.0685** | 1.025379 |
| DEF | 864 | 423 | **2.0426** | 1.024933 |

The three implied per-level factors span **1.0249 – 1.0399**. **No single
per-level scalar maps all three, whatever the grade does.** So the archive's
`hp/atk/def` and the in-game panel's HP/ATK/DEF are **not the same quantity**, or
the archive row is not at a single level.

This is a third independent reason the archive cannot be dropped in as a base
table, alongside the refuted gear-exclusion inference and the 38.7 % shared-block
finding. It does **not** mean the archive is worthless — it is still the only
per-hero numeric corpus — but any use of it must state the basis mapping.

## 6. Corrections this forced on prior work

1. **`rank2`'s `3311 → 4907` is the unidentified blonde child, not Kain `029`.**
   Kain's own ★3/Lv.MAX also reads 3311; the coincidence caused a misattribution.
2. **The 1.1 % spread between the two rank-ups is not noise.** At ~43× the
   rounding floor (0.025 %) it is a real hero-dependent term. Defensible bound:
   `g²⁹ ≤ 1.498434`, per-level ≤ **1.013851**; Beckhen excess **1.15×**, not 1.16×.
3. **The Beckhen 1.7157 factor may be ill-posed** — see §5.
4. **The un-cropped ★4→★5 result does not exist.** All three surviving uploads of
   `IMG_5729` are crops of one user-edited phone photo, all cut at the badge row
   where the `戦闘力` row begins. A lane recovered a *third* crop (690×388) no
   prior pass had seen; its `39554` is the rupee wallet HUD, not a stat.
5. **A third same-shape grade transition could never have separated `f` from `g`**
   — T1+T2+T3 is 3 unknowns against 2 independent equations. It would have been a
   consistency test, not a separation. Recorded because the plan was proposed as
   if it worked.

## 7. What is still missing

One number: **`戦闘力` of the blonde-child hero at ★4/Lv.MAX** — T3's left-hand
value, which the crop removes. With it, `g²⁹ = 1.4820296 × 3311 / B`, with **no**
assumption about the T3 grade factor. Second priority: **any T2 panel.**

## 8. Reproduction

`%TEMP%\opencode\verify_t1.py` re-derives every ratio, the spread, both ladders'
T3 predictions, the 3× ceiling (1.0994³ = 1.3287), the +5.744 % rating excess, and
the §5 per-level spread. Coverage counters unmoved: heroes **1/113**, accessories
**1/100**, monsters **0/22**. Note the standing convention: Captain/Hermes state
`Transcendence Level: 3`, so a post-Transcendence block is **not** a base stat.
Nothing outside this folder was written.