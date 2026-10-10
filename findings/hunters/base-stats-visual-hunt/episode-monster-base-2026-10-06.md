# Episode `M*` monsters — ratio-invariance test (2026-10-06)

**Question tested.** If an Episode monster `res_id` appears in several combats at
different levels and its `ATK/HP` and `DEF/HP` ratios stay constant, that would
give a shared base tuple plus a scaling law — the only offline lever anyone had
found for the 0/22 monster gap.

**Verdict: the hypothesis is FALSIFIED, and cleanly.** Ratio invariance is not
merely absent — **0 of 19** same-`res_id` row pairs preserve both ratios, and the
absolute values are *also* not verbatim repeats. The 7 multi-row tokens land in a
**fourth** outcome the hypothesis's dichotomy did not contain. Separately, the
brief's premise contains a **denominator error** (§1.1) that would have made this
whole exercise look like a near-miss for coverage when it is not one at all.

**Coverage effect: none. Monsters remain 0/22.** No derived tuple in §2 is
admissible; §2 exists only as quarantine/rebalance material. No server, fixture,
APK, seed, emulator, phone or Ghidra action. `polluted-observations.md` was not
appended to or edited.

---

## 1. PURE — measured ratios, the classification, and the structure behind it

Numerals in this section are arithmetic on **shipped literals**, re-derived from
disk with per-value `file:line` citations, and are offered as *measurements*, not
as stats of any monster. **No base tuple is claimed here.** Anything resembling a
"base" is quarantined in §2.

### 1.0 Source pin and positive controls

| control | result |
|---|---|
| `EPISODE_STAT_ACTORS.json` sha256 | `f3b8cb90372c89490467e75ed0564bfc3f8a4d094370264caa2c821b0eb13b56` — matches `EPISODE_COMBAT_STAT.manifest.json` → `entries[0].sha256` exactly |
| parent pack | `R_EPISODE.jet`, sha256 `7f4362cdf80545a6da937444094837f334c8aae4f9f791d6ff4161948d98a01e`, 38 080 B (same manifest) |
| entries | 152 (entry index **80** is a literal `{}`; 151 identifiable) |
| combat records read | 61 `EPISODE_COMBAT_*.json` + 1 `..._STAT.manifest.json` (excluded) |
| **control A** — actor placements | 240 non-empty actor rows = **160 `hunter` + 80 `monster`**; 149 distinct `actor_id`; **149/149 resolve to a STAT row** |
| **control B** — empty slots | 168 `{}` slots, **all on the `left` (hero) side**, never `right` |
| **control C** — the join is real | `stat.rank` == `thumb.rank` for **33/33** placed `M*` rows. The 34th (`CB0002_M01`) has no placement at all. An incorrect join could not produce 33/33 rank agreement. |
| control D — no zero-as-real | thumb `level` genuinely varies corpus-wide: `{1:118, 5:5, 10:23, 15:6, 20:29, 30:59}`. A `level == 1` reading would have been an artefact, not a fact. |

Control C matters most: it is what licenses treating each STAT row as the tuning
actually used by that placement, which is the premise of the whole test.

### 1.1 The brief's "22 monsters" is not the coverage denominator

This is the most consequential finding in the file, and it is a premise error in
the hypothesis as briefed.

- The 22 distinct `M*` `res_id` tokens in the Episode STAT table are
  `M001, M022, M023, M024, M034, M035, M036, M040, M041, M042, M044, M046, M048,
  M049, M050, M051, M052, M054, M057, M058, M062, M100`.
- The coverage denominator is a **different** 22: `analysis/catalogue/data/monsters.json`
  = `['M001'…'M021', 'M100']`, matching `analysis/catalogue/INDEX.md:8` ("22
  files, `M001`..`M021` + `M100`") and `coverage.md:13`.
- **Overlap = 2: `M001` and `M100`.** The other **20** Episode tokens
  (`M022`…`M062`) are *not catalog monsters at all*.

So the 7 multi-row tokens this pass analyses (`M023, M034, M035, M036, M040,
M062, M100`) contain exactly **one** catalog monster, `M100` — whose two rows
already disagree (§2.2). Cross-checking: `m001-m100-insider-2026-10-05.md:3-7`
recorded the same 2/22 overlap and called `M001`/`M100` "the only two 22-catalog
monsters with Episode STAT rows"; `m001-m100-insider:196` had already recorded
that `<res>.jet` coincidence holds for only 2 of 22. This pass re-derives both
independently and agrees. **Consequence: even a fully successful version of this
hypothesis could have addressed at most 2 of 22 monsters.**

### 1.2 The 34 `M*` rows, verbatim, with citations

All 34 rows carry `role: 1`; `attr` varies. `spd` is `0`/`0.00` on every row.
`skill` is `[]` on every row except none — all 34 are empty.

| entry | actor `id` | `res_id` | `id`@line | `hp`@line | rank | HP | ATK | DEF | ATK/HP | DEF/HP |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 35 | `CB1501_M1` | M034 | 4147 | 4154 | 5 | 7000 | 6800 | 280 | 0.97143 | 0.04000 |
| 36 | `CB1501_M2` | M035 | 4170 | 4177 | 5 | 7000 | 6800 | 280 | 0.97143 | 0.04000 |
| 53 | `CB0002_M01` | M034 | 5887 | 5895 | 1 | 100 | 100 | 100 | 1.00000 | 1.00000 |
| 54 | `CB0001_BOSS` | M040 | 5911 | 5919 | 1 | 400 | 190 | 100 | 0.47500 | 0.25000 |
| 55 | `CB0001_M01` | M001 | 5935 | 5943 | 1 | 150 | 130 | 100 | 0.86667 | 0.66667 |
| 65 | `CB0102_M1` | M022 | 6593 | 6600 | 1 | 450 | 430 | 180 | 0.95556 | 0.40000 |
| 71 | `CB0201_M1` | M023 | 7055 | 7062 | 2 | 700 | 400 | 130 | 0.57143 | 0.18571 |
| 72 | `CB0602_M1` | M024 | 7078 | 7085 | 4 | 2500 | 1800 | 200 | 0.72000 | 0.08000 |
| 94 | `CB0202_M1` | M050 | 8627 | 8634 | 2 | 800 | 680 | 160 | 0.85000 | 0.20000 |
| 95 | `CB0202_M2` | M049 | 8650 | 8657 | 2 | 800 | 680 | 160 | 0.85000 | 0.20000 |
| 96 | `CB0202_M3` | M051 | 8673 | 8680 | 2 | 800 | 700 | 160 | 0.87500 | 0.20000 |
| 97 | `CB0202_BOSS` | M062 | 8696 | 8703 | 3 | 1800 | 750 | 160 | 0.41667 | 0.08889 |
| 98 | `CB0501_M1` | M046 | 8719 | 8726 | 3 | 1000 | 1200 | 180 | 1.20000 | 0.18000 |
| 99 | `CB0501_M2` | M052 | 8742 | 8749 | 3 | 1000 | 1200 | 180 | 1.20000 | 0.18000 |
| 100 | `CB0501_M3` | M048 | 8765 | 8772 | 3 | 1000 | 1200 | 180 | 1.20000 | 0.18000 |
| 101 | `CB0501_M4` | M054 | 8788 | 8795 | 3 | 1000 | 1200 | 180 | 1.20000 | 0.18000 |
| 102 | `CB0501_BOSS` | M062 | 8811 | 8818 | 4 | 2000 | 1500 | 210 | 0.75000 | 0.10500 |
| 103 | `CB0702_M1` | M058 | 8834 | 8841 | 4 | 2400 | 2600 | 200 | 1.08333 | 0.08333 |
| 104 | `EVCB0102_M1` | M035 | 8857 | 8864 | 4 | 3000 | 3500 | 200 | 1.16667 | 0.06667 |
| 105 | `EVCB0102_M2` | M036 | 8880 | 8887 | 4 | 3000 | 3500 | 200 | 1.16667 | 0.06667 |
| 106 | `CB1002_M1` | M035 | 8903 | 8910 | 5 | 5500 | 4500 | 280 | 0.81818 | 0.05091 |
| 107 | `CB1002_M2` | M036 | 8926 | 8933 | 5 | 5500 | 4500 | 280 | 0.81818 | 0.05091 |
| 108 | `EVCB0301_M044` | M044 | 8949 | 8956 | 5 | 5000 | 4000 | 250 | 0.80000 | 0.05000 |
| 109 | `EVCB0301_M057` | M057 | 8972 | 8979 | 5 | 4000 | 4500 | 200 | 1.12500 | 0.05000 |
| 110 | `CB1002_M3` | M034 | 8995 | 9002 | 5 | 13000 | 5500 | 280 | 0.42308 | 0.02154 |
| 111 | `CB1301_M1` | M035 | 9018 | 9025 | 5 | 7000 | 6000 | 300 | 0.85714 | 0.04286 |
| 112 | `CB1301_M2` | M036 | 9041 | 9048 | 5 | 7000 | 6000 | 300 | 0.85714 | 0.04286 |
| 113 | `CB1301_M3` | M034 | 9064 | 9071 | 5 | 16000 | 7000 | 300 | 0.43750 | 0.01875 |
| 122 | `CB1201_BOSS` | M100 | 9779 | 9786 | 5 | 16000 | 7000 | 300 | 0.43750 | 0.01875 |
| 123 | `CB1401_BOSS` | M100 | 9802 | 9809 | 5 | 20000 | 8000 | 280 | 0.40000 | 0.01400 |
| 124 | `CB1201_M1` | M041 | 9825 | 9832 | 5 | 6500 | 6000 | 300 | 0.92308 | 0.04615 |
| 125 | `CB1201_M2` | M040 | 9848 | 9855 | 5 | 6500 | 6000 | 300 | 0.92308 | 0.04615 |
| 126 | `CB1201_M3` | M042 | 9871 | 9878 | 5 | 6500 | 6000 | 300 | 0.92308 | 0.04615 |
| 127 | `CB0301_M1` | M023 | 9894 | 9901 | 2 | 700 | 650 | 160 | 0.92857 | 0.22857 |

Ratios are `atk/hp` and `def/hp` to 5 dp from the cited literals. Two
self-cancelling coincidences are visible and must not be misread: entries 113
(`CB1301_M3`) and 122 (`CB1201_BOSS`) are byte-identical `16000/7000/300` and are
**different actor ids in different combats**, not one monster seen twice.

### 1.3 The three-way classification — with a fourth class

| class | count | tokens |
|---|---:|---|
| **CONSISTENT-SHAPE** (ratios invariant across appearances) | **0** | — |
| **FLAT** (absolute values verbatim-identical across appearances) | **0** | — |
| **SINGLE-APPEARANCE** (no cross-check possible) | **15** | `M001, M022, M024, M041, M042, M044, M046, M048, M049, M050, M051, M052, M054, M057, M058` |
| **INCONSISTENT** — 4th class: values *and* ratios both vary | **7** | `M023, M034, M035, M036, M040, M062, M100` |

Row distribution: 15 tokens × 1 row + 7 tokens × (2,4,4,3,2,2,2 rows) = 15 + 19
= **34 rows** — reconciles with the file.

**The hypothesis's stated fallback does not describe the data.** It predicted
multi-row tokens would be either consistent-shape (a win) or verbatim-flat (an
explicit null). The truth is a third thing: the values change *and* the ratios
change, i.e. the tuples are **independently hand-tuned per encounter**.

**Direct discriminator result: of the 19 unordered same-`res_id` row pairs
(exactly the pairs the hypothesis was built on), the number preserving both
`ATK/HP` and `DEF/HP` is 0.** Enumerated pairwise:

| token | pairs | pairs preserving both ratios |
|---|---:|---:|
| `M023` | 1 | 0 |
| `M034` | 6 | 0 |
| `M035` | 6 | 0 |
| `M036` | 3 | 0 |
| `M040` | 1 | 0 |
| `M062` | 1 | 0 |
| `M100` | 1 | 0 |
| **total** | **19** | **0** |

### 1.4 No growth factor exists — and HP does not even scale with level

Rank-ordered consecutive ratios, per multi-row token (thumb levels in brackets):

| token | transition | HP | ATK | DEF |
|---|---|---:|---:|---:|
| `M023` | r2 (L5) → r2 (L30) | **×1.0000** | ×1.6250 | ×1.2308 |
| `M034` | r1 (unplaced) → r5 (L1/L20) | ×70.0000 | ×68.0000 | ×2.8000 |
| `M034` | r5 (L20) → r5 (L20) | ×1.8571 | **×0.8088** | ×1.0000 |
| `M034` | r5 (L20) → r5 (L20) | ×1.2308 | ×1.2727 | ×1.0714 |
| `M035` | r4 (L1) → r5 (L20) | ×2.3333 | ×1.9429 | ×1.4000 |
| `M035` | r5 (L20) → r5 (L20) | **×0.7857** | **×0.6618** | ×1.0000 |
| `M035` | r5 (L20) → r5 (L20) | ×1.2727 | ×1.3333 | ×1.0714 |
| `M036` | r4 (L1) → r5 (L20) | ×1.8333 | ×1.2857 | ×1.4000 |
| `M036` | r5 (L20) → r5 (L20) | ×1.2727 | ×1.3333 | ×1.0714 |
| `M040` | r1 (L1) → r5 (L10) | ×16.2500 | ×31.5789 | ×3.0000 |
| `M062` | r3 (L20) → r4 (L1) | ×1.1111 | ×2.0000 | ×1.3125 |
| `M100` | r5 (L10) → r5 (L15) | ×1.2500 | ×1.1429 | **×0.9333** |

Three hard negatives, each independently sufficient to kill the scaling law:

1. **HP is level-invariant.** `M023` is `700` HP at thumb **L5**
   (`CB0201_M1`, `CB0201`) and `700` HP at thumb **L30** (`CB0301_M1`,
   `CB0301`) — while ATK moves 400 → 650. Same level basis, same HP, different
   ATK: HP is not a function of level here.
2. **Ratios can fall.** `M100` L10 → L15 gives DEF **×0.9333** (300 → 280) while
   HP rises ×1.25. Any monotone per-level law is excluded. (Independently
   recorded at `m001-m100-insider-2026-10-05.md:173-176`.)
3. **Ratios can fall below 1.** `M035` r5→r5 gives HP **×0.7857** and ATK
   **×0.6618** at an *unchanged* thumb level (L20) — "growth" that shrinks, at
   identical displayed level.

**One common factor explains no monsters.** The 12 transitions above span HP
factors 0.7857 … 70.0. There is no shared per-level growth factor to report.

### 1.5 What actually keys the tuple — the positive explanation

Since the tuple is not keyed on `res_id`, two measurements locate what it *is*.

**(a) Identical stat tuples are shared across *different* `res_id`s** — 7 clusters,
which is only possible if `res_id` is not the stat key:

| sharing tokens | shared HP/ATK/DEF | rank |
|---|---|---:|
| `M046, M048, M052, M054` | `1000/1200/180` | 3 |
| `M040, M041, M042` | `6500/6000/300` | 5 |
| `M034, M035` | `7000/6800/280` | 5 |
| `M035, M036` | `3000/3500/200` | 4 |
| `M035, M036` | `5500/4500/280` | 5 |
| `M035, M036` | `7000/6000/300` | 5 |
| `M049, M050` | `800/680/160` | 2 |

Four different tokens carry one identical tuple; conversely one token (`M035`)
appears in three different clusters. This is mutually exclusive with `res_id`
being a stat-bearing identity, and it corroborates `m001-m100-insider:204-207`
("a grouping label inside `EPISODE_STAT_ACTORS.json`, not a resolvable monster
identity").

**(b) The combat record's own `power` field predicts it.** Over the 17 combats
that place at least one `M*` monster:

- Pearson **r(power, min non-boss monster HP) = 0.9746**
- Pearson r(power, max monster HP) = 0.8751

The tuple is therefore an **encounter-budget artefact**. Within one combat, the
non-boss mob rows usually collapse to a single tuning and the `BOSS`-named row
gets its own; 6/17 combats have exactly one non-boss tuple, and every other
combat is "one mob tuning (+1 variant) + one boss tuning". Examples: `CB1501`
(115 000) — `M034` and `M035` both `7000/6800/280`; `EVCB0102` (25 000) —
`M035`/`M036` both `3000/3500/200`; `CB1201` (95 000) — `M040`/`M041`/`M042` all
`6500/6000/300` with boss `M100` at `16000/7000/300`.

### 1.6 Thumb level is not a scale input (re-confirmed)

- `CB1501_M1` (`M034`) is thumbed **L1/R5/H0** in `EVCB0301` and **L20/R5/H2** in
  `CB1501`. One STAT row serves both.
- `CB1201_M1`/`_M3` are thumbed L10 in `CB1201` and L15 in `CB1401`, per
  `m001-m100-insider:73-78`, which this pass re-derived from the join.
- `CB0301_M1` vs `CB0201_M1`: L30 vs L5, **identical HP** (§1.4 item 1).

Level is display/progression context, not a stat input. This is why "different
levels, same ratio" never had a chance.

### 1.7 The `ref_id` values on `M` rows — a collision trap, not an identity

The brief said "4 distinct `ref_id`". **Measured: 3**, and the discrepancy is in
`episode-stat-namespace-filter-2026-10-06.md:36` (its table cell reads "4" while
its own §1 fact 2 at `:48-50` correctly lists three). I measure 3 from disk; the
table cell is the wrong one.

All three are **hero-card namespace ids**, present in `analysis/catalogue/data/cards.json`
(121 entries): `001`, `034`, `040` — all `True`. Exactly three `M*` rows carry one:

| entry | actor `id` | `res_id` | `ref_id` | in hero-card namespace? |
|---:|---|---|---|---|
| 55 | `CB0001_M01` | M001 | `001` | yes |
| 53 | `CB0002_M01` | M034 | `034` | yes |
| 54 | `CB0001_BOSS` | M040 | `040` | yes |

The other **31** `M*` rows have **no `ref_id` key at all**. So `ref_id` is **0/34
useful for monster identity** — it is a vestigial hunter-card field, exactly the
trap the filter note warns about at `:48-50`. It cannot substitute for the absent
binding table, and it cannot convert an `M*` token into a card or a monster.

### 1.8 The `C*`-namespace monsters (collision control, re-verified)

Monster-typed placements split **72 `M*` (22 tokens)** vs **8 `C*` (6 tokens)**:
`C010 ×3`, `C006`, `C008`, `C011`, `C018`, `C019` ×1 each. This reproduces
`episode-stat-namespace-filter-2026-10-06.md:39-47` and `:73` (42 monster-like
rows total = 34 + 8) exactly. Applying the normative filter
(`:25-28` — `res_id` starts `C` **and** combat `type == "hunter"`) leaves **109**
safe hero rows. No `C*` row is used anywhere in this analysis.

### 1.9 Filter discipline

The `res_id`-starts-with-`M` partition was used, **not** an id-prefix split
(`EVCB*`/`CB*` partition actor ids, not `res_id`s — `episode-stat-namespace-filter:52-55`).
All 34 rows are `M*` **and** monster-typed in combat, so the two filters agree
here; no `EVCB0301_*` row was admitted on its id prefix. Entry index 80 (the
literal `{}`) was excluded and its exclusion is stated so a future reader can
re-derive the 151/152 split.

---

## 2. UNPURIFIED — quarantined candidates. **Zero coverage credit.**

Everything below is a **per-encounter scripted actor tuning**, not a base stat.
Do not quote any of it as a monster's HP/ATK/DEF. It is retained only for future
encounter-rebalance / difficulty-curve estimates, per
`m001-m100-insider-2026-10-05.md:91-101`.

**Why no row here can be purified.** `coverage.md:13` requires a tuple "tied to an
unambiguous monster ID plus level/rank/difficulty context", and `:35` forbids
counting a monster HUD value that lacks identified monster + demonstrated full/max
HP + independently supported ATK/DEF. Every candidate below fails at the first
clause already:

- **Identity confidence: low to none.** 20 of the 22 `M*` tokens have no catalog
  monster (§1.1); the 2 that do (`M001`, `M100`) each contradict the other.
- **Level basis: not a scale basis.** Thumb level demonstrably does not drive the
  STAT (§1.6), and no row is proven unscaled at a known level.
- **Scale basis: encounter `power`, r = 0.9746** (§1.5b) — the tuning tracks the
  fight's budget, not the creature.
- **Native rendering never observed.** Episode combat rendering/combat outcome
  remains unverified (per §125/§126 of `AGENTS.md`), so no row is tied to an
  observed full-HP bar.

### 2.1 `M001` — single row, catalog monster, thinnest possible datum

`CB0001_M01`, entry 55, `id`@5935, `hp`@5943: **150 / 130 / 100**, `rank "1"`,
`attr 2`, `role 1`, `cool_time 99000`, `ref_id "001"` (hero namespace, §1.7).
Placed 4× in `CB0001` right/wave 0 at thumb L1/R1/H0/attr2, all skill slots
`[0,0,0,0,0]`; wave mate `CB0001_BOSS` (`M040`). Secondaries all zero
(`spd 0.00`, `crt_chance 25`, `crt_dmg 175`, penetration/enhance/block/resist/
regen `0`). No second appearance ⇒ no cross-check, no base. Duplicate of
`m001-m100-insider` §2.1; re-verified, not superseded.

### 2.2 `M100` — the only catalog monster with cross-checks, and it fails them

The two appearances **disagree in every field**, and DEF *falls* while level
rises:

| | `CB1201_BOSS` (entry 122, `id`@9779) | `CB1401_BOSS` (entry 123, `id`@9802) |
|---|---|---|
| placement | `CB1201` right boss, L10/R5/H2 | `CB1401` right boss, L15/R5/H2 |
| HP | 16000 (`@9786`) | 20000 (`@9809`) |
| ATK | 7000 | 8000 |
| DEF | 300 | **280** |
| ATK/HP · DEF/HP | 0.43750 · 0.01875 | 0.40000 · 0.01400 |
| `crt_dmg` / `hp_regen` | 200 / 100 | 250 / 150 |

Uncertainty: **identity is sound** (it *is* a catalog monster, §1.1) but that is
the only clean axis. There is **no growth law** — HP ×1.25, ATK ×1.1429, DEF
×0.9333 — so no collapse into one tuple is permissible. Treat as two independent
scripted boss tunings. Consistent with `m001-m100-insider` §2.4, which this pass
re-derives.

### 2.3 The five non-catalog multi-row tokens — ratios disagree pairwise

Highest spread in the table is `M034`, whose 4 rows span HP **100 → 7000 →
13000 → 16000** and ATK **100 → 6800 → 5500 → 7000** — a 160× HP spread and a
non-monotone ATK. Its `100/100/100` row (`CB0002_M01`, entry 53) is the **only**
`M*` row in the corpus with **no combat placement at all**, so its `ref_id "034"`
cannot even be checked against a thumb; it is a probable vestigial/unused entry.
`M035` additionally shows "shrinkage" at constant displayed level (§1.4 item 3).
None admits a base tuple; ratio-normalising them would invent a monster that the
data does not describe.

### 2.4 The 15 single-appearance tokens

Constrained by exactly one encounter each, and 13 of the 15 are **non-catalog**
tokens. They are the weakest material in the file — kept here only so the ledger
is complete, and explicitly **not** candidate bases. Notable co-occurrence:
`M046/M048/M052/M054` are four names for one tuning (`1000/1200/180`), which is
itself evidence that the token is a label, not an identity (§1.5a).

### 2.5 Quarantine rules (normative)

1. **Never** present any §2 numeral as a monster base stat, and never divide by
   any growth factor — §1.4 shows no factor exists.
2. **Never** collapse `M100`'s two rows; they disagree (§2.2).
3. **Never** use `ref_id` to bind an `M*` token to a card or a monster: 3/3 are
   hero-namespace collisions and 31/34 are absent (§1.7).
4. **Never** join these HP values to a video HUD token; identity, chapter,
   difficulty and full-vs-current semantics are all unproved on the video side
   (`monster-hud-observations.md`).
5. Era-tag **unknown** for every row — do not assume PRE/POST the 2019-09-05
   rebalance (`stat-version-context.md`).
6. If a future pass wants a real monster base stat, it needs a recovered binding
   table plus a level formula — a shape this file shows **does not exist** in the
   Episode data.

---

## 3. Corrections to existing files (reported, not edited)

Per house rule I did not edit other research files; these are measured and are
for the parent to apply.

1. **`episode-stat-namespace-filter-2026-10-06.md:36`** — the `res_id` starts `M`
   row reads "34 rows, **4** distinct `ref_id`, 22 distinct `res_id`". From disk
   it is **3** distinct non-empty `ref_id` (`001`, `034`, `040`); 31 of the 34
   rows have no `ref_id` key. The same file's §1 fact 2 (`:48-50`) is correct.
2. **`episode-stat-namespace-filter-2026-10-06.md:92`** — "6 multi-tuple
   identities" among the `M*` rows: measured **7** (`M023, M034, M035, M036,
   M040, M062, M100`). The count is reproducible under both `res_id`-grouping and
   the filter's own definition, so 7 is the figure. I could not establish what
   made it 6.
3. **Framing risk worth stating once.** Two unrelated 22s are now in play —
   22 Episode `M*` script tokens vs the 22 catalog monsters `M001`–`M021`+`M100`
   — overlapping on 2. Any future brief that says "the 22 monsters" for the
   Episode table will silently target the wrong denominator.

## 4. What would falsify this conclusion

This pass concludes *per-encounter literals, no base tuple, no growth law*. Each
of the following would overturn it, and none is currently true:

1. **A level-formula application stage.** If native code multiplies the shipped
   STAT by a level/rank factor at load time, the shipped literal would be a
   pre-scale value and the invariance test would be measuring the wrong thing.
   Against: `M023` is `700` HP at L5 *and* L30 (§1.4 item 1) — no single formula
   maps both onto one base. Would need native evidence, not inference.
2. **`res_id` is not the entity key.** Already *positively* demonstrated (§1.5a:
   four tokens, one tuple; one token, three tuples). If a recovered binding table
   instead showed `res_id` → distinct monster *identity*, the identity half of
   the quarantine lifts — but §1.3's ratio result would still stand, so this
   yields identity, not a base tuple.
3. **A hidden third stat axis.** If `rank`/`hyper` combine non-multiplicatively
   and the corpus simply lacks coverage of that combination, invariance could be
   masked rather than absent. Against: `M034` and `M035` both sit at R5 with the
   same `hyper` in the same combat (`CB1002`) and still differ (`13000/5500/280`
   vs `5500/4500/280`).
4. **The join is wrong.** Already excluded by control C (§1.0): `stat.rank` ==
   `thumb.rank` on 33/33 placed rows.
5. **Wrong file version.** Excluded by the sha256 pin matching the manifest
   (§1.0).

The single cleanest falsifier to keep in mind: a *second* corpus (campaign
`STAGE_MONSTER_LINK` / `GetStageMonster`) where one monster id **does** hold
ratio-constant rows at two levels. That is where the lever would have to be —
not in Episode scripted actors.

---

## 5. Method and compliance

- All reads/writes via Python with `encoding='utf-8'` and the `read`/`write`
  tools. **No PowerShell `Get-Content`/`Set-Content`/`WriteAllLines` anywhere**;
  PowerShell was used only to launch Python, writing the helper script with
  `Out-File -Encoding utf8` outside the workspace
  (`%LOCALAPPDATA%\Temp\opencode\ep_mon_*.py`).
- Scratch scripts were kept outside the workspace; no temp file was written into
  `analysis/`.
- `polluted-observations.md` **not** appended to, **not** edited. No other lane
  file edited (§3 reports, does not apply). No `server-ts`, fixture, APK, seed,
  emulator, phone or Ghidra action. No network access.
- Verified after writing: **U+FFFD = 0**, **CRLF = 0**, UTF-8 clean.
- Self-correction recorded: my first brace-scanning script mis-assigned entry
  line numbers (it mishandled the literal `{}` entry), producing citations that
  were off by one entry. Caught by read-back, discarded, and replaced with
  `id`-anchored line lookup. Every `file:line` in §1.2 was re-verified against
  the file by direct read-back of three sample rows — which is the same
  "plausible number nobody re-derived" failure mode this lane exists to prevent.