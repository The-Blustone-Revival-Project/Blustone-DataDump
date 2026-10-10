# Level-factor test — is the 2019 archive a level-N reading? (2026-10-05)

**Purpose.** Test the **replacement hypothesis** proposed by
[`transcendence-multiplier-2026-10-05.md`](transcendence-multiplier-2026-10-05.md)
§2.3: that the `≈1.72` scalar on the Beckhen `051` "Lv.30 / no equipment" panel is
most plausibly a **per-level compound of 1.0185–1.0193**, and that the 2019
archive rows are therefore **Lv-N readings rather than base values**.

**Answer in one line.** The hypothesis **fails as a level claim** — but **not**
for the reason it might be expected to. It fails because the Japanese source page
labels the block `基本能力値` ("basic ability values"), i.e. it is *declared* a base
table, and because the archive's own numbers contain no level ladder. The scalar
is real and is **not** a transcendence factor; it is **not** cleanly a level factor
either. See §1.6 for the new finding that actually settles the 1.72, and §2.1.

**Files touched.** New: this file only. `polluted-observations.md` **not
appended** (parent mirrors). `coverage.md`, `README.md`, all TSVs, all
`analysis/catalogue/**` files **not edited** — §2.5 proposes corrections and does
not apply them. `server-ts`, fixtures, seeds, APK, emulator and phone **untouched**.
The Ghidra project was not opened.

**New primary-source reads this pass** (Wayback, `id_` raw form, all HTTP 200,
byte lengths matching the `vsfan-wiki` §1.4 ledger exactly):

| file | capture | bytes | ledger match |
|---|---|---:|---|
| `Hermes` (oldid 7349) | 2019-08-26 08:11:15 | 113 204 | ✔ 113 204 |
| `Riko` (oldid 2615) | 2019-08-21 03:04:11 | 87 653 | ✔ 87 653 |
| `Guide_to_Blustone` (7465) | 2019-09-23 07:20:38 | 56 316 | ✔ 56 316 |
| `List_of_Hunters` (7480) | 2019-08-26 08:27:17 | 210 780 | ✔ 210 780 |
| `List_of_Blustone_Items` (5115) | 2019-08-21 02:41:34 | 104 950 | ✔ 104 950 |
| `Hunter` (2091) | 2019-08-26 07:21:45 | 45 425 | ✔ 45 425 |
| `Hunters` (2091) | 2019-08-21 01:22:52 | 45 750 | ✔ 45 750 |

`Captain` (2323) was already in `_wf1_cache` and was re-read from disk.
Japanese `blustone.jp` profiles re-fetched: `009`, `017`, `023`, `024`, `036`,
`051` — six pages, all `基本能力値` present, **no numeric level statement on any
of them**.

---

# 1. PURE

## 1.1 The prior note's arithmetic, reproduced and extended

Recomputed from the TSV and the transcribed FAQ integers:

| field | archive `051` | FAQ panel (Lv.30, no equip) | ratio | per-level compound over 29 steps | flat per-level add |
|---|---:|---:|---:|---:|---:|
| HP | 1678 | 2879 | **1.715733** | 1.018790 | 41.414 |
| ATK | 864 | 1471 | **1.702546** | 1.018519 | 20.931 |
| DEF | 660 | 1149 | **1.740909** | 1.019301 | 16.862 |
| **SUM** | **3202** | **5499** | **1.717364** | 1.018823 | — |

The three-field compound spread is **0.4 %**, as the prior note states. That part
reproduces exactly.

**New this pass: the SUM follows the same scalar to the unit.**
`round(3202 × 1.717364) = 5499` — the panel's HP+ATK+DEF **exactly**. This is a
genuine additional coherence check and it slightly strengthens the "one uniform
scalar on the three core stats" reading.

## 1.2 The 2.25 % field-to-field spread is NOT rounding noise

This is the first place the "single clean level factor" story is tested properly.

Relative uncertainty on each ratio induced by ±0.5 integer rounding on **both**
the archive and the panel value:

| field | rounding-induced uncertainty on its ratio |
|---|---:|
| HP | 0.0345 % |
| ATK | 0.0671 % |
| DEF | 0.0874 % |
| **worst** | **0.0874 %** |

Observed spread between the three ratios (`1.740909 / 1.702546`): **2.253 %**.

> **2.253 % is 25.8× the worst rounding uncertainty.** The three fields do **not**
> share one scalar at integer precision. Any single-`M` story for the 051 pair is
> already broken before considering levels.

Least-absolute-integer-error search over `M` confirms it: the best single `M` for
the 051 triple is **1.715436** with total error **28 units** (hp `+0`, atk `+11`,
def `−17`). No `M` is exact for all three.

**This result is independent of the level hypothesis** and refutes the prior
note's own §1.4-style "single M" framing as applied to `051` — a framing the prior
note applied only to the wiki trio.

## 1.3 The decisive structural test — is the archive band a level ladder?

If the archive's 62 HP values were rungs of a level curve, consecutive rungs
would sit at a near-constant **ratio** (a geometric ladder). Measured:

| | value |
|---|---|
| distinct HP values | 20 (over 62 rows) |
| consecutive-ratio range | **1.0046 – 1.0924** |
| ratio spread | **8.7 %** |
| population stdev | **0.02106** |
| a true 1.9 %/level ladder would predict | all ratios ≈ 1.019, spread ≈ 0 % |

**The archive HP band is not a level ladder.** It is a set of independent
per-hero values. The 8.7 % ratio spread is ~25× the ~0.35 % spread a compound
`g = 1.019` ladder would produce across 20 rungs.

The band also quantises heavily — **13 HP values are shared by ≥2 rows, covering
55 of 62 rows**; `1624` alone is shared by **seven** heroes (`002, 005, 009, 021,
024, 032, 034`) and `1750` by **eleven**. Independent per-hero values do not tie
55 of 62 times by chance. This is a designed lookup table.

## 1.4 The implied-level sweep is degenerate — and that is the finding

Task asked: *compute what base and level the archive rows would imply, and
whether the implied levels are sane.*

Let `N` = the level the archive is read at, `g` the per-level compound, so
`g^(30−N) = 1.715733` (HP).

| archive at | steps | implied `g` | implied flat-`k` | implied base HP/ATK/DEF |
|---|---:|---:|---:|---|
| Lv.1 | 29 | 1.018790 | 0.024680 | 1678.0 / 857.4 / 669.7 |
| Lv.2 | 28 | 1.019467 | 0.025562 | 1678.0 / 857.4 / 669.7 |
| Lv.5 | 25 | 1.021828 | 0.028629 | 1678.0 / 857.4 / 669.7 |
| Lv.10 | 20 | 1.027360 | 0.035787 | 1678.0 / 857.4 / 669.7 |
| Lv.20 | 10 | 1.055468 | 0.071573 | 1678.0 / 857.4 / 669.7 |
| Lv.25 | 5 | 1.114012 | 0.143147 | 1678.0 / 857.4 / 669.7 |
| Lv.29 | 1 | 1.715733 | 0.715733 | 1678.0 / 857.4 / 669.7 |

**The implied base is numerically identical for every `N`** — that is forced
algebra (`hP / g^steps ≡ hA` when `g^steps = hP/hA`). **The base cannot
discriminate `N`.** The only free parameter is `g`.

So the "archive HP range 1277–2033 over a plausible base" test **cannot be run as
posed**: the base is not independently known, and the panel/ archive pair supplies
no constraint on `N`. Sweeping `N` and asking "is the implied base plausible"
returns "plausible" for all `N` because it is the same number every time.

What the sweep *does* bound: **`g` must lie in `[1.0188, 1.716]`** and the total
Lv.1→Lv.30 growth must lie in `[1.716×, 14.5×]`. Only `N = 1` gives a growth rate
any game designer would ship. That is a plausibility argument for `N = 1`, **not a
measurement of it** — and §1.3 independently shows the band is not a ladder at
all.

## 1.5 "The panel sits above the archive band" is an artefact, not evidence

The prior note (§1.7, §2.3) offers as support that "the panel's HP `2879` sits
**above the archive maximum** `2033` — *"exactly where a levelled-up card should
belong."*

Measured: `panel / archive_max = 2879 / 2033 = 1.4161`, and this ratio is
**identical at every `N`** (1.4161 at Lv.1, Lv.5, Lv.10, Lv.20, Lv.29). The
observation is a pure restatement of "the panel is bigger than every archive row."
It carries **zero** information about the archive's level. It cannot support the
level reading and is withdrawn as support for it.

The archive's rarity bands are also cleanly graded (`★1` 1277–1624, `★2`
1395–1624, `★3` 1521–1968, `★4` 1923–2033) and its roles partition as expected
(Bombers low HP / high ATK, Supports narrow). A level-N reading of a level-1
table would produce exactly the same banding. **The banding does not
discriminate.**

## 1.6 THE NEW FINDING — the Japanese source labels the block `基本能力値`

This is the result that settles the question, and it was **not** in the prior
note's evidence base.

Re-fetched `blustone.jp` profiles carry the literal label **`基本能力値`**
immediately before the HP/ATK/DEF/SPD block, and **`詳細能力値`** before the nine
sub-stat blocks. Verbatim, `051` Beckhen:

```
排出時の★ ★3  戦闘力 8709  ベッケンの基本能力値  HP 1678 攻撃力 864 防御力 660 攻撃スピード 8
ベッケンの詳細能力値：攻撃力  致命打率 33  致命打ダメージ量 200  貫通力 0
ベッケンの詳細能力値：防御力  ブロック率 14  ブロックダメージ減少量 42  属性強化 5  属性耐性 5  HP再生力 42
```

| reading | `基本能力値` | numeric level stated |
|---|---|---|
| `009` Captain | ✔ | **no** |
| `017` Lapis | ✔ | **no** |
| `023` Hermes | ✔ | **no** |
| `024` Riko | ✔ | **no** |
| `036` Bear | ✔ | **no** |
| `051` Beckhen | ✔ | **no** |

Two things follow, and they point in **opposite** directions:

1. **`基本能力値` = "basic / fundamental ability values" — a declaration that this
   block is the BASE table.** Combined with `排出時の★` ("★ at draw"), the page
   is explicit that these are the card's as-drawn base abilities at its draw
   rarity. **This is the source labelling its own data as base**, which is
   stronger than any inference this project could draw from a single Lv.30
   comparison.

2. **No page states a level — and none can.** The page labels the block *base*;
   it does not print "Lv.1", because a base table is by definition not
   level-indexed. **The `level: not shown` column in the TSV is not a gap to be
   filled — it is the correct reading of a page that publishes base values.** The
   prior note's §2.5 item 4 ("any archived page that states a level for the
   reference table") asks for a field that, on this evidence, does not exist.

**Therefore: the archive rows are BASE values, declared as such by the source.**
They are **not** level-N readings. The level-factor hypothesis is **refuted at its
premise**, not merely unsupported.

## 1.7 The wiki pages state no level either — Task 2's discriminator, answered

Task asked: *do the `Transcendence Level: 3` pages also state a level anywhere?*

**No. Established, on all three complete-table heroes, across every layer:**

| layer | Captain `009` | Hermes `023` | Riko `024` |
|---|---|---|---|
| infobox `<b>` labels | `Rarity`, `Role`, `Type` (+`Gender`,`Race` on 023) | same | `Rarity`, `Role`, `Type` |
| infobox has a `Level` field | **NO** | **NO** | **NO** |
| `<caption>` | `Transcendence Level: 3` | `Transcendence Level: 3` | `Transcendence Level: 3` |
| categories | `Blustone`, `Hunters`, `Sapiens` | `Blustone`, `Hunters`, `Coffee Rabbit` | `Blustone`, `Hunters`, `Werewolves` |
| full-text `level`/`Lv` tokens | 1 (`Transcendence Level: 3`) + 2 `Lv. 50` skill labels | 1 + 4 `Lv. 50` | 1 + 2 `Lv. 50` |
| **numeric character level** | **NONE** | **NONE** | **NONE** |
| any element whose entire text is `Level`/`Lv` | only `Lv.50 15.00%`, `Lv.50 7.54%` (skill magnitudes) | only `Lv.50 …` (4) | only `Lv.50 …` (2) |

The `Lv. 50` tokens are **skill-effect** magnitudes (`Increase defense Lv. 50
15.00%`), not character levels. Categories are race/series only. The corpus-wide
scan of all 43 cached hero captures found **zero** character-level statements
anywhere; every surviving `level`/`Lv`/`Max` token is `toclevel-1` CSS,
`Template:Max` markup, a skill `Lv. 50` label, or skill prose.

Six guide pages were additionally re-read for a stated reference level:
`Guide_to_Blustone` (56 KB), `Hunter_Gym`, `List_of_Hunters` (210 KB),
`List_of_Blustone_Items`, `Hunter`, `Hunters`. **None states the level of the
`Character Attributes` tables.** `Guide_to_Blustone` documents skill-cost level
bands, cruise area levels (36–40, 96–100) and transcendence costs — never the stat
table's level.

> **Task 2 verdict: the level is NOT recoverable for any of the three complete-table
> heroes.** The clean `wiki/LP ÷ archive/LP` ratio measurement is therefore
> **unavailable**, and the `1.274`/`1.300` clusters cannot be tested as
> level ratios. §2.4 states what would be needed instead.

## 1.8 The level-integer test on the wiki cluster, and why it is vacuous

Because §1.7 kills the level, one can still ask whether the wiki ratios look like
integer powers of a plausible `g`. At the 051-calibrated `g = 1.018790`:

| hero | field | ratio | implied steps `n = ln(ratio)/ln(g)` | nearest int | frac |
|---|---|---:|---:|---:|---:|
| `009` | hp | 1.274015 | 13.0094 | 13 | **0.0094** |
| `009` | def | 1.278835 | 13.2123 | 13 | 0.2123 |
| `009` | atk | 1.168790 | 8.3786 | 8 | 0.3786 |
| `023` | hp | 1.300000 | 14.0941 | 14 | 0.0941 |
| `023` | atk | 1.299893 | 14.0897 | 14 | 0.0897 |
| `023` | def | 1.298622 | 14.0371 | 14 | 0.0371 |
| `024` | hp | 1.274015 | 13.0094 | 13 | **0.0094** |
| `024` | atk | 1.272727 | 12.9551 | 13 | −0.0449 |
| `024` | def | 1.275274 | 13.0625 | 13 | 0.0625 |

The 8 non-outlier fields imply **13–14 steps**. This is *superficially* striking,
and it is reported here precisely so it is not rediscovered as a discovery later.

**It is a coincidence, and §1.2 shows why.** The interval test is the correct
form: a single `M` reproducing eight integers has probability ≈ (mean interval
width)^8. Free-`M` scan minimising Σ(frac)² over 8 fields returns a best fit of
**`M = 1.300` for Hermes** — i.e. the scan recovers the *transcendence* factor
the corpus already documents, not a level factor. The `n`-integer framing is
simply `M = g^n` re-expressed; with `g` free, every cluster near any `M` can be
written as an integer power of something. A random-ratio control (20 000 trials,
ratios drawn uniform on `[1.2, 1.4]`) confirms near-integer `n` is reachable by
construction — 0/20000 reached the tight `0.01` rms, but that is a statement
about the free parameter, not evidence.

**No level claim is licensed.** §1.6 (`基本能力値`) is the actual answer, and it
says *base*.

## 1.9 What the 1.72 actually is — a fourth finding, independent of level

The archive's 051 row and the FAQ panel 051 have **byte-identical substats**:
`speed 8, crit 33, crit_damage 200, pen 0, block 14, blockred 42, ee 5, er 5,
hp_regen 42`. Verified field-by-field this pass. That makes a clean test possible.

Fit the archive's own `combat_power` law on all 62 rows
(`cp ~ 1 + hp + atk + def + 9 substats`, OLS; `hp 3.049, atk 5.112, def 5.809`;
max residual 236 = 2.7 % of mean), then feed it the **panel's** core stats and the
**panel's own substats**:

| input | model prediction | actual | error |
|---|---:|---:|---:|
| archive `051` 1678/864/660 | 8 731 | 8 709 | −22 ✔ |
| **panel `051` 2879/1471/1149** | **18 336** | **24 068** | **+5 732 (+31.3 %)** |

The simpler `cp = 4.54293·(sum) − 6026.7` law gives 18 955 vs 24 068 (+5 113).

**Strength/Combat-Power does not follow the core-stat scalar.**
`24068 / 8709 = 2.7636` while the core three move `1.7025–1.7409`. Required
marginal slope for the 051 step is **6.687** cp per point of stat-sum; the
archive-wide measured slopes on substat-matched pairs are **4.52, 5.76, 5.82,
6.25, 8.92** — 6.687 sits inside that spread, so the *ratio* is not anomalous, but
the fitted *law* still under-predicts by 31 %. The archive's cp is a function of
the substat vector as well as the core three, and the panel's Strength moves
faster than any single-scalar account of the core stats permits.

So `1.72` describes **the three core stats only**. It is not a property of the
card's whole stat block, and the prior note's framing of "the `≈1.72` scalar"
as a card-level quantity is too broad by construction.

## 1.10 Summary of every scalar measured this pass

| scalar | value | status |
|---|---:|---|
| HP 1678→2879 | 1.715733 | measured |
| ATK 864→1471 | 1.702546 | measured |
| DEF 660→1149 | 1.740909 | measured |
| **SUM 3202→5499** | **1.717364** | measured, **exact to the unit** |
| Strength 8709→24068 | **2.7636** | measured, **not** the core scalar |
| per-level compound if archive@Lv.1 | 1.0185–1.0193 | conditional, premise refuted (§1.6) |
| total Lv.1→Lv.30 growth if archive@Lv.1 | 1.716× (+71.6 %) | conditional |
| archive HP consecutive-ratio spread | 8.7 % | measured — **not a ladder** |
| field spread vs rounding noise | 2.253 % vs 0.087 % | measured — **25.8×** |
| wiki T3 cluster | 1.27273–1.30000 | unchanged; **not** the 051 scalar (32–35 % apart) |

---

# 2. UNPURE

## 2.1 Verdict on the replacement hypothesis

**The hypothesis is refuted at its premise, and the prior note's own supporting
observation is withdrawn.**

| claim | verdict | basis |
|---|---|---|
| the 051 scalar is a **transcendence** factor | **NO — refuted** | prior note §2.3; `1.716` is 32 % above the corpus's own measured T3 max of `1.300` |
| the 051 scalar is a **per-level compound** | **NOT LICENSED** | §1.6: the archive is labelled `基本能力値` = base, so there is no level gap for a level factor to fill |
| "panel HP above the archive band supports the level reading" | **WITHDRAWN** | §1.5: the ratio is 1.4161 at *every* `N`; it is an artefact, not evidence |
| "archive HP band 1277–2033 is explained by a level factor over a plausible base" | **UNTESTABLE AS POSED** | §1.4: implied base is algebraically identical for all `N`; it cannot discriminate |
| the ~1.72 is **something other than transcendence** | **SUPPORTED, mechanism unknown** | §1.6 + §1.9: not a base-vs-level gap, and not a whole-card property |
| the archive rows are **level-N readings** | **NO** | §1.6: source labels them base; §1.3: band is not a ladder |

**The prior note's "most plausible" reading should be withdrawn as
"most plausible".** Its own arithmetic showed the panel HP `2879` exceeds the
archive band; §1.5 shows that observation is uninformative, and §1.6 shows the
premise is false. The defensible statement is narrower and negative: **the
`1.72` is a measured, unexplained, non-transcendence difference between two
sources' readings of `051`'s core stats. Its mechanism is UNKNOWN.**

This is a **retraction of a hypothesis, not an adoption of a replacement**. The
project should record the gap as open rather than re-describe it.

## 2.2 What this means for the 62 "base stat" claims — a MAJOR reclassification, flagged not applied

Task asked what happens if the archive rows turn out to be level-N readings.

**They do not — and that is the finding. But the consequence is still a
reclassification, in the opposite direction, and it is large.**

`基本能力値` is a **source-side declaration of base-ness** on 6 of the 62 verified
pages. If the project's coverage definition requires a base stat, this is
*positive* evidence the corpus did not previously have. It is **not** applied
here, for reasons that must be recorded:

1. **Only 6 of 62 pages were re-fetched and verified for the label this pass.**
   Extending it to all 62 requires re-fetching the other 56 URLs. Until then the
   label is established for a **sample**, not the table.
2. **`基本能力値` is a Japanese term of art on a fan/portal site, not a client
   string.** It has not been located in any shipped client resource or native
   string table. It is strong provenance, not `[RECOVERED]` client evidence.
3. **Era remains unquantified.** The verified pages carry capture timestamps
   **2019-10-15 … 2019-12-16**, i.e. **POST** the 2019-09-05 rebalance, while
   `051`'s panel is **2018-12-22-era PRE**. Per
   [`stat-version-context.md`](stat-version-context.md) the rebalance changed
   **equipment/crystal** stats. Whether it touched base character HP/ATK/DEF is
   **unmeasured** — the prior note assumed the two corpora being on opposite
   sides was a confound; §1.9's 31 % cp mis-prediction is consistent with a
   post-rebalance power-formula change and is **not** diagnostic of one.
4. **The gear dimension is still open for the other 61 rows.** `051`'s panel is
   explicitly no-equipment. `基本能力値` says the *card's own* abilities, which
   is a gear-free claim, but the pages do not say so in those words and no second
   gear-separated reading exists to cross-validate the convention the way
   `24068 + 6291 = 30359` does for `051`.

**Consequence if the parent's adjudication accepts `基本能力値` as base-ness:**
the 62 rows move from *level-ambiguous raw candidates* to *source-labelled base
rows with gear state asserted*. That is a **coverage change the parent must
decide explicitly**, and it must not happen by quiet reading of this note.
Until it does, **`coverage.md` stays 1/113 / 1/100 / 0/22** and the 62 rows stay
outside strict coverage.

**Do not** retro-label the TSV, `coverage.md` or any catalogue file on the
strength of this note. §2.5 lists the corrections as proposals only.

## 2.3 The Captain-ATK anomaly is *not* dissolved by any of this

`734 / 628 = 1.16879` remains 8.2 % below its cluster. Nothing in §1.3–§1.9
touches it, and §1.2 shows the 051 triple has an analogous field-specific
deviation (2.25 % spread, 25.8× rounding noise). **The corpus's one large
anomaly stays anomalous and stays the only evidence a field-specific rule might
exist.** It must not be smoothed away, and it must not be re-explained as a
level effect now that the level reading is refuted.

## 2.4 Confidence ledger

| claim | confidence | basis |
|---|---|---|
| `基本能力値` labels the archive core block on `009/017/023/024/036/051` | **high** | 6 verbatim re-fetches this pass |
| the archive rows are **base**, not level-N | **medium-high** | source label + §1.3 non-ladder + §1.6; *not* verified on all 62, and the term is a portal label |
| the wiki T3 pages state **no character level** | **high** | infobox/caption/category/full-text layers, all 3 heroes, 6 guide pages |
| the wiki/archive ratio test as a **level ratio** is unavailable | **high** | follows from the above |
| the 051 field spread is **not** rounding noise | **high** | 2.253 % vs 0.087 %, arithmetic |
| the archive HP band is **not** a level ladder | **high** | 8.7 % ratio spread, stdev 0.021 |
| implied-base test **cannot** discriminate `N` | **high** | algebra; reproduces for all `N` |
| Strength does **not** follow the core-stat scalar | **medium-high** | 31 % under-prediction; confounded by era + possible quantity mismatch |
| the `1.72` mechanism is **unknown** | **stated as open** | §2.1 |
| wiki `1.274`/`1.300` clusters are **not** the 051 scalar | **high** | 32–35 % apart, arithmetic |
| the wiki clusters are **transcendence** (not level) | **unchanged, `medium`** | prior note §2.1; `基本能力値` removes the level alternative but does not *prove* transcendence |

## 2.5 Proposed corrections — NOT applied

| # | file | proposal | why not applied |
|---|---|---|---|
| 1 | `archived-hunter-database-2019.md:61` | it calls `051` "Lv.30, **5★**". `051.md` and the FAQ read **3★** on the badge, the archive says `rarity_on_draw 3`, and the prior note's §2.3 argument rests on **3★**. The `5★` looks like a transcription slip. | catalogue/TSV file — report only |
| 2 | `archived-hunter-database-2019.md` | add `基本能力値` as the source's own base-ness declaration, with the 6 verified URLs | needs all 62 re-fetched first (§2.2.1) |
| 3 | `coverage.md:23` | re-adjudicate whether a source-labelled base row satisfies the base-tuple definition | **parent's call**; changes a threshold |
| 4 | `coverage.md:100` | the Natalia `2480 → 3323` Lv.1→Lv.30 Strength pair is a **fourth** scalar: ratio **1.339919**, per-level **1.010141**, steps-equivalent **15.7** at `g=1.0188`. Inconsistent with Beckhen's 29 steps — gear/rank unresolved, as already flagged. | not appended, per instruction |
| 5 | `transcendence-multiplier-2026-10-05.md` §1.7 / §2.3 | withdraw "the panel HP above the archive band is the reading the archive's own HP band supports" (§1.5 here) | superseded by this file |

## 2.6 What would settle the question next

Ordered by value per unit cost. Items 1–2 are now the only ones that can change
the `1.72`'s status.

1. **Re-fetch the remaining 56 `blustone.jp` profile URLs and confirm
   `基本能力値` on every one.** Cheap, mechanical, and it converts §1.6 from a
   6-page sample to a table-wide fact — or finds an exception, which would be
   equally informative. **Highest value, lowest cost.**
2. **Locate `基本能力値` (and `戦闘力`) in a shipped client resource or the native
   string table.** If the client itself prints a "basic ability values" heading
   above the HP/ATK/DEF block on the in-game stat panel, the base-ness claim
   becomes `[RECOVERED]` client evidence rather than portal prose, and the 62 rows
   become usable without further qualification. The project's native string dumps
   (`analysis/native-all-strings.tsv`) are the place to look. **This is the single
   highest-value probe in the whole lane.**
3. **Recover the client's own `combat_power` formula from native code.** §1.9
   shows the archive's 62 `cp` values are *not* a function of the core three
   alone (twelve duplicate `(hp,atk,def)` triples carry ten different `cp`
   values), and the fitted law under-predicts the panel by 31 %. A native
   `CalcTotalPower`/`CalcTotalBP` read would give the real weights and would
   either explain the `2.7636` Strength scalar or rule it out decisively.
4. **One Lv.1 and one Lv.30 reading of the SAME hero, same grade, no equipment,
   from one era.** This is the only measurement that yields a real per-level
   curve. The corpus has **no** such pair: `051` pairs a 2018 Lv.30 panel with a
   2019 base row (cross-era), and Natalia's `2480→3323` is Strength-only with
   gear unresolved (§2.5.4). Until this exists, **no per-level factor should be
   implemented anywhere** — the server's level curve stays a declared fixture.
5. **A dated pre-2019-09-05 `blustone.jp` capture.** The era confound is
   unquantified and is the largest remaining limit on every number in §1.10. A
   Wayback capture of `blustone.jp/hunter/` from mid-2019 or earlier, compared
   against the verified October rows, would measure the rebalance's effect on
   base stats directly. **CDX-probeable; the 2019 wildcard harvest in
   `archived-hunter-database-2019.md` already proved alternates resolve.**
6. **The `Lv. 50` skill magnitudes, cross-checked.** If a Lv.50-referenced skill
   percentage can be tied to a level-stated stat panel for one hero, it would
   bound the level axis indirectly. Low value: §2.11 of `vsfan-wiki` already
   records the `Lv. 50` label is unqualified.

## 2.7 Standing prohibitions

- **Do not implement a per-level stat factor.** Not `1.0188`, not `1.716`, not
  any interpolated `g`. The premise (`基本能力値` = base) is refuted and the
  corpus has no same-hero two-level pair. The server's hunter level curve remains
  a **declared local fixture** (`server-ts/src/hunter-levels.ts` shape, unchanged).
- **Do not write "1.72 is a level factor".** It is measured; its mechanism is
  unknown. `1.0185–1.0193` is conditional on an archive level of 1 that the
  source contradicts.
- **Do not withdraw the `1.716×` transcendence reading without replacing it.** The
  replacement is an *unexplained non-transcendence difference*, which is a weaker
  result, not a stronger one.
- **Do not quietly upgrade the 62 rows.** See §2.2. The `基本能力値` label is
  real evidence and the parent should adjudicate it explicitly, but the
  reclassification is not this note's to make and the coverage thresholds must
  not move by inference.
- **Do not treat §1.8's 13–14-step table as a level result.** It is `M = gⁿ`
  re-expressed with `g` free; the scan recovers the documented transcendence `M`,
  not a level.
- **Do not smooth Captain's ATK** (§2.3).

---

## 3. Files touched

- **New:** this file only.
- **Re-fetched (read-only, Wayback `id_` / plain):** `Hermes` (7349), `Riko`
  (2615), `Guide_to_Blustone` (7465), `List_of_Hunters` (7480),
  `List_of_Blustone_Items` (5115), `Hunter` (2091), `Hunters` (2091);
  Japanese `blustone.jp` profiles `009`, `017`, `023`, `024`, `036`, `051`.
- **Read:** `Captain` (2323) and all 43 `_wf1_cache` hero captures from disk;
  `transcendence-multiplier-2026-10-05.md`, `vsfan-wiki-2026-10-05.md`,
  `archived-hunter-database-2019.tsv`, `catalogue/stats/051.md`,
  `candidate-hero-bases-2026-10-05.md`, `episode-stat-adjudication-2026-10-05.md`,
  `coverage.md`, `stat-version-context.md`, `exp-ladder-corroboration-2026-10-05.md`
  (all read-only).
- **Proposed corrections, NOT applied:** the five in §2.5.
- **Not touched:** `polluted-observations.md` (**not appended**), `coverage.md`,
  `README.md`, all TSVs, `analysis/catalogue/**`, `server-ts`, fixtures, seeds,
  the APK, the emulator, the physical phone, the Ghidra project.
