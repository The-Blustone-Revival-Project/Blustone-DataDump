# Archetype reconciliation — the four-clean-archetype claim adjudicated (2026-10-05)

**Purpose.** Resolve a live contradiction between two files that are *both* in the corpus,
by computing the role distributions from the primary sources rather than choosing between
the two narratives.

| file | position |
|---|---|
| [`hero-stat-divergence-2026-10-05.md`](hero-stat-divergence-2026-10-05.md) | four clean archetypes; role ATK/DEF bands **"do not overlap"**; Defense < Support < Offense < Bomber |
| [`replica-shape-error-2026-10-05.md`](replica-shape-error-2026-10-05.md) | **"4 clean groups"**; per-role band table; the same four ranges |
| [`candidate-hero-bases-2026-10-05.md`](candidate-hero-bases-2026-10-05.md) | **Offense/Bomber do NOT separate on ATK/DEF in either source**; the archive shares `1.382–1.581`; split by `s = (ATK+DEF)/HP`; a four-archetype model **over-reads** the evidence; replica `s = 0.150` is **5.6x below** the whole archive range |

**Verdict in one line: `candidate-hero-bases-2026-10-05.md` is right; the other two files
over-read their own evidence, and both have now been corrected in place.**

**Nothing was changed except three markdown files.** No `server-ts` file, fixture, seed,
APK, emulator or phone was touched. `polluted-observations.md` was **not** appended. The
two source data files (`archived-hunter-database-2019.tsv`, `EPISODE_STAT_ACTORS.json`)
were **read** and not modified. **Zero coverage effect:** heroes **1/113**, accessories
**1/100**, monsters **0/22** are unchanged.

---

## 1. Method

Read `archived-hunter-database-2019.tsv` with Python (`encoding='utf-8'`,
`csv.DictReader(delimiter='\t')`), kept rows where `fetch_status == "ok"` and `hp`/`atk`/`def`
parse as integers, and grouped by the `role_ja` column. That yields **62 numeric rows over
62 distinct `catalog_id`s**, matching the corpus's existing count — so every figure below is
reproducible from the TSV alone, with no dependency on either narrative file.

Two scale-free features, both defined per row so no level assumption is needed:

- `r = ATK/DEF` — the axis the four-archetype claim is made on.
- `s = (ATK+DEF)/HP` — the axis `candidate-hero-bases` proposes instead.

Encoding safety per [`GUARD-encoding-and-archive-traps.md`](GUARD-encoding-and-archive-traps.md):
all reads/writes Python `encoding='utf-8'` with explicit `newline='\n'` on write; no
PowerShell `Get-Content`/`Set-Content` anywhere; the only edits were via the `edit` tool.
Hangul/CJK in these files was never re-encoded.

---

## 2. The measured distributions (archive, n = 62)

| role | n | `r` min | `r` median | `r` max | `s` min | `s` median | `s` max |
|---|---:|---:|---:|---:|---:|---:|---:|
| **Defense** | 17 | 0.6589 | 0.7647 | 0.9167 | 0.8419 | 0.9255 | 1.2171 |
| **Support** | 13 | 0.9231 | 1.0000 | 1.1405 | 0.8912 | 0.9088 | 0.9427 |
| **Offense** | 20 | 1.1695 | 1.3396 | 1.5815 | 0.8929 | 0.9190 | 0.9691 |
| **Bomber** | 12 | 1.3815 | 1.5452 | 1.7483 | 1.1243 | 1.1366 | 1.1642 |
| **ALL** | 62 | 0.6589 | 1.1695 | 1.7483 | 0.8419 | 0.9277 | 1.2171 |

Role **medians** on `r` are strictly ordered Defense 0.7647 < Support 1.0000 < Offense
1.3396 < Bomber 1.5452 — **that part of the four-clean framing survives.**

---

## 3. Question 1 — Do Offense and Bomber truly overlap on ATK/DEF?

**Yes. Unambiguously, and at a size that invalidates a four-band lookup.**

Overlap arithmetic:

```
Offense band : 1.1695 .. 1.5815   (n = 20)
Bomber  band : 1.3815 .. 1.7483   (n = 12)
shared lower  = max(1.1695, 1.3815) = 1.3815
shared upper  = min(1.5815, 1.7483) = 1.5815
SHARED REGION : 1.3815 .. 1.5815     width = 0.2001
```

Counts inside the shared region:

- **8 of 12 Bomber rows (66.7 %)** — ids `007, 014, 025, 031, 033, 039, 054, 055`
- **9 of 20 Offense rows (45.0 %)** — ids `006, 010, 012, 017, 019, 021, 023, 038, 044`
- **17 of 62 rows (27.4 %) are unassignable on `r` alone** (14 distinct `(hp,atk,def)` tuples).

All 17, with `s` alongside:

| id | role | star | hp/atk/def | `r` | `s` |
|---|---|---:|---|---:|---:|
| `033` Patrone | Bomber | 3 | 1521/1003/726 | 1.3815 | 1.1368 |
| `044` Heidi | Offense | 3 | 1750/952/689 | 1.3817 | 0.9377 |
| `054` Dino | Bomber | 3 | 1560/1029/744 | 1.3831 | 1.1365 |
| `031` Diana | Bomber | 3 | 1521/1021/689 | 1.4819 | 1.1243 |
| `039` Gullveig | Bomber | 3 | 1521/1021/689 | 1.4819 | 1.1243 |
| `055` Apollon | Bomber | 3 | 1560/1054/708 | 1.4887 | 1.1295 |
| `038` Rebecca (Xmas) | Offense | 3 | 1790/992/668 | 1.4850 | 0.9274 |
| `012` Karl Steiner | Offense | 3 | 1750/1007/689 | 1.4615 | 0.9691 |
| `019` Balian | Offense | 1 | 1537/817/576 | 1.4184 | 0.9063 |
| `006` Sylvester | Offense | 1 | 1537/817/576 | 1.4184 | 0.9063 |
| `023` Hermes | Offense | 3 | 1750/937/653 | 1.4349 | 0.9086 |
| `010` Vincent | Offense | 4 | 1923/1032/718 | 1.4373 | 0.9100 |
| `021` Rebecca | Offense | 2 | 1624/893/580 | 1.5397 | 0.9070 |
| `025` Teddy Bomber | Bomber | 2 | 1395/978/646 | 1.5139 | 1.1642 |
| `007` Metis | Bomber | 1 | 1277/908/576 | 1.5764 | 1.1621 |
| `014` Locke | Bomber | 1 | 1277/908/576 | 1.5764 | 1.1621 |
| `017` Lapis | Offense | 1 | 1537/854/540 | 1.5815 | 0.9070 |

Note the shape of the confusion: **`s` cleanly bisects the shared region** — every Bomber
row in it reads `s ≥ 1.1243`, every Offense row `s ≤ 0.9691`.

### The published four bands are also knife-edge at the other three seams

Taking the published bands literally as a lookup (`Defense 0.659–0.917`, `Support
0.923–1.140`, `Offense 1.170–1.581`, `Bomber 1.382–1.748`), on the same 62 rows:

| failure mode | count | ids |
|---|---:|---|
| matched **no** band (rounded edge excludes a real row) | **7** | `053, 060, 037, 040, 035, 015, 020` |
| matched an **actively wrong** band | **9** | 8 Bombers read as Offense (`054, 055, 039, 031, 033, 025, 007, 014`), `017` Offense read as Bomber |
| **total wrong or ambiguous** | **16 of 62 (25.8 %)** | |

`053` (r 0.6589) falls 0.0001 below its own published floor of 0.659; `037`/`040`
(r 1.1695) fall 0.0005 below the Offense floor of 1.170; `015`/`020` (r 1.7483) fall
0.0003 above the Bomber ceiling of 1.748. **The four-archetype model is not merely
over-split — as a lookup table it is wrong for a quarter of its own evidence.**

---

## 4. Question 2 — Does `s` separate all four roles cleanly?

**No. `s` has its own, worse overlaps. It separates exactly one pair cleanly.**

Pairwise disjointness on `s`:

| pair | A range | B range | verdict |
|---|---|---|---|
| Defense vs Support | 0.8419–1.2171 | 0.8912–0.9427 | **OVERLAP** |
| Defense vs Offense | 0.8419–1.2171 | 0.8929–0.9691 | **OVERLAP** |
| Defense vs Bomber | 0.8419–1.2171 | 1.1243–1.1642 | **OVERLAP** |
| Support vs Offense | 0.8912–0.9427 | 0.8929–0.9691 | **OVERLAP** |
| Support vs Bomber | 0.8912–0.9427 | 1.1243–1.1642 | disjoint, gap 0.1816 |
| Offense vs Bomber | 0.8929–0.9691 | 1.1243–1.1642 | disjoint, gap **0.1551** |

**4 of 6 pairs overlap.** Three independent confirmations that `s` is not a four-way axis:

1. **A single row breaks the "Bomber = high `s`" rule.** `053` Calibur is a **Defense**
   hero at `s = 1.2171` — *above the entire Bomber band* (max 1.1642). Any `s`-only rule
   that assigns Bomber on `s > 1.0` misclassifies it.
2. **Defense / Support / Offense are mutually indistinguishable.** All three ranges
   contain `0.8929–0.9427`. Their `s` medians are **not monotone** in the role order
   (Defense 0.9255 > Offense 0.9190 > Support 0.9088 < Bomber 1.1366).
3. **Run counts.** Walking the 62 rows in ascending order, the number of maximal same-role
   runs is **33 along `s`** versus **14 along `r`**. `r` is by far the cleaner axis.

So `s`'s honest role is narrow and specific: **it is a tie-breaker for the top pair only**,
where it happens to be perfect (0 errors in the archive). It is not a replacement four-way
axis.

---

## 5. Question 3 — The correct minimal archetype statement

**Three distinguishable groups on `ATK/DEF`; four only as an `r`-then-`s` conjunction.**

### 5.1 What `r` alone supports — three groups

Sorted by `r`, the role sequence is:

```
Def(17) Sup(13) Off(11) Bom(1) Off(1) Bom(1) Off(5) Bom(2) Off(1) Bom(2) Off(1) Bom(2) Off(1) Bom(4)
```

**Defense and Support are each a single unbroken block, and every single role
interleaving sits inside the Offense/Bomber zone** (from index 32 onward). So `r`
partitions the table into exactly:

| group | `r` range | n | note |
|---|---|---:|---|
| Defense | `[0.6589, 0.9167]` | 17 | clean block |
| Support | `[0.9231, 1.1405]` | 13 | clean block |
| **Offense ∪ Bomber** | `[1.1695, 1.7483]` | 32 | **one group, not two** |

### 5.2 The two surviving `r` seams are very thin

| seam | lower max | upper min | gap | headroom |
|---|---:|---:|---:|---:|
| Defense \| Support | 0.916667 (`043`) | 0.923077 (`016`) | 0.006410 | **0.70 %** |
| Support \| Offense | 1.140496 (`035`) | 1.169536 (`037`) | 0.029041 | **2.55 %** |
| Offense \| Bomber | — | — | overlaps by 0.2001 | none |

The first seam is a **single integer step in DEF**: `043` reads 726/792 and `016` reads
660/715. Any gear level, rounding change, or one row's transcription error crosses it. The
ordering is real; it is not a robust classifier.

### 5.3 The minimal four-leaf statement that the evidence does support

Apply `r` first, in role order, and consult `s` only inside the top group:

```
if   r < 0.920          -> Defense      (gap to next: 0.0064)
elif r < 1.165          -> Support      (gap to next: 0.0290)
elif s  > 1.000         -> Bomber       (gap from Offense max 0.9691: 0.1551, 16.0 % headroom)
else                    -> Offense
```

- **Archive: 0 misassignments in 62.** (This is *weak* validation — `r` and role are not
  independent, the tree thresholds were chosen from these 62 rows — so it demonstrates
  consistency, not predictive power.)
- **Episode `EVCB*` hero rows (n = 37): 15 misassignments (40.5 %).** `EVCB` ATK/DEF values
  are round numbers on a coarse grid (`1000/1000` ×4, `1100/1000` ×3), so it cannot
  resolve cuts this fine. **The four-leaf model therefore does not transfer to the shipped
  source at all.** Treat the two lower cuts as archive-only.

### 5.4 So the minimal honest statement, in one sentence

> Role is a real axis and role **medians** on `ATK/DEF` are strictly ordered
> Defense < Support < Offense < Bomber; `ATK/DEF` separates **three** groups
> (Defense, Support, and a merged Offense+Bomber supergroup, the latter by two
> overlapping ranges `1.3815–1.5815` covering 27.4 % of all rows); the **fourth**
> group is recoverable only by adding the second scale-free axis
> `s = (ATK+DEF)/HP`, which splits Bomber from Offense with zero archive errors but
> overlaps on 4 of 6 role pairs and fails to transfer to the `EVCB` family.

---

## 6. Question 4 — Which file is right?

**`candidate-hero-bases-2026-10-05.md` is right on all three substantive points, and the
other two files over-read.** Specifics:

| claim | candidate file | divergence file | shape-error file | measured truth |
|---|---|---|---|---|
| Offense/Bomber overlap on `ATK/DEF` | **yes**, shared `1.382–1.581` | "do not overlap" (naming only the Bomber↔Defender pair), `:97` | "4 clean groups", `:271` | **candidate right**; 17/62 rows unassignable |
| Four clean ATK/DEF archetypes | **over-reading** | implied by `:97`; asserted as "disjoint" at `:293` | "4 clean groups" at `:271`; band list at `:560` | **candidate right** |
| Split Offense/Bomber with `s` | **yes** | absent | absent | **candidate right**, with the caveat in §4 that `s` overlaps on 4 of 6 pairs |
| Replica `s` 5.6x below the whole archive range | **yes**, headline §2.2 | absent | **absent until this pass** | **candidate right**; see §7 |

(Line numbers here are **post-edit**; §9 carries the pre-edit → post-edit mapping.)

Two honest criticisms of the candidate file, recorded so this adjudication is not one-sided:

1. **Its "Offense/Bomber must instead be split by `s`" phrasing invites the same
   over-reading one level up.** `s` does not yield four groups either (§4). It yields
   exactly one clean pair-split. The candidate file's §2.5 verdict table does state this
   correctly row-by-row, so this is a summarisation risk, not a factual error.
2. **Its §2.4 tolerance justification inherits the over-read.** It argues ±15 % "cannot
   cross a role boundary" on the strength of "the four role bands are separated by a
   0.917 to 1.382 gap". That gap is Bomber-min − Defense-max, i.e. the two **extreme**
   roles; the seams that actually sit between adjacent roles are 0.0064 and 0.0290, which
   ±15 % of `r` **does** cross. The sweep's own results (13/25 at ±15 %, rising to 20/25 at
   ±20 %) are consistent with bands being crossed, so the conclusion survives even though
   the stated justification does not.

---

## 7. The `s` replica error, now in the shape-error file's headline

`s` was **absent** from `replica-shape-error-2026-10-05.md` — its §1.5.c gap table stopped
at `ATK/HP`, `DEF/HP` and `ATK/DEF`. Added there (headline block + a row in the §1.5.c
table):

```
replica 001 :  s = (100+50)/1000 = 0.150
replica 002 :  s = (120+40)/1000 = 0.160
archive min :  s = 0.8419   (036 Bear, (755+864)/1923)
archive max :  s = 1.2171   (053 Calibur, Defense)
0.8419 / 0.150 = 5.61x below the minimum      0.8419 / 0.160 = 5.26x
invariant to the +hp_up 10 additive (R1):  (101+51)/1010 = 0.1505, still 5.60x low
```

**This is the largest factor in that table.** `ATK/DEF` overshoots by 1.14x;
`ATK/HP` undershoots by 3.71x; `s` undershoots by **5.61x**. So the replica is
simultaneously HP-dominant by ~5.6x on the combined offence+defence budget *and*
ATK-over-DEF-heavy on the one axis that is role-structured. Any option that corrects only
`ATK/DEF` — which is how O4 and O5 were previously framed — leaves the bigger error
untouched.

---

## 8. A fourth defect found while measuring (not part of the brief)

`replica-shape-error-2026-10-05.md` §1.5.b's `EVCB*` grouping is **contaminated by monster
rows**. Filtering on the `EVCB*` *id prefix* admits rows whose `res_id` is a monster
(`M*`) id:

- `EVCB0301_M057` — `res_id M057`, 4000/4500/200, `r = 22.500` ← **the `22.500` upper bound in that file's Offense range**
- `EVCB0301_M044`, `EVCB0102_M1` (`M035`), `EVCB0102_M2` (`M036`)

That is why §1.5.b reports `EVCB*` `n = 41` where the hero-row count is **37** — the four
extra rows are all monsters, all carrying the Offense role enum. Restricting to `ref_id` =
3-digit catalog id **and** `res_id` starting `C`:

| role | `EVCB*` hero rows | `r` range | `r` median | `s` range |
|---|---:|---|---:|---|
| Defense | 8 | 0.800–1.235 | 0.913 | 0.380–1.000 |
| Support | 12 | 0.833–1.143 | 1.000 | 0.792–0.957 |
| Offense | **11** | **1.077–1.333** | 1.250 | 0.540–1.050 |
| Bomber | 6 | 1.200–2.167 | 1.479 | 0.957–1.118 |

`candidate-hero-bases-2026-10-05.md` used the correct filter (37 rows) and is unaffected.
**Consequence for the archetype question: the `EVCB` Offense/Bomber `r` overlap is
`1.200–1.333`, i.e. it is real there too** — 4 of 6 `EVCB` Bomber rows (`055, 072, 059,
068`) sit at or above the `EVCB` Offense maximum. So `candidate-hero-bases`'s claim that
Offense/Bomber "does not separate in **either** source" is confirmed. **The inflated
`22.500` was a monster, not a hero.**

---

## 9. Corrections made

| file | line(s) — **post-edit** | change |
|---|---|---|
| `hero-stat-divergence-2026-10-05.md` | `:3–33` | New dated **CORRECTION** block: withdraws the four-clean claim, states the overlap, states the 3-group / 4-conjunction replacement, points here |
| `hero-stat-divergence-2026-10-05.md` | `:97` (S1 table, "Role archetype" cell) | Struck "**do not overlap** between Bomber and Defender" → replaced with the measured ranges, the 8/12 + 9/20 overlap counts, and the corrected 3-group statement |
| `hero-stat-divergence-2026-10-05.md` | `:280` (P1 heading, new amendment note) + `:293` (the struck sentence) | P1 retained and amended: median ordering, the two thin seams, the `s` tie-break |
| `hero-stat-divergence-2026-10-05.md` | `:457` (§3b item 1) | "role splits ATK/DEF" annotated: three `r` groups, not four disjoint ones |
| `replica-shape-error-2026-10-05.md` | `:3–48` | New dated **HEADLINE ADDITION**: the `s = (ATK+DEF)/HP` axis and the **5.61x-below-minimum** replica error, with the arithmetic; plus a companion block listing the three in-file over-reads |
| `replica-shape-error-2026-10-05.md` | `:319` (§1.5.c gap table) | Added the `(ATK+DEF)/HP` row (replica 0.150 vs min 0.8419 vs median 0.9277, **5.61x below the lowest of 62**), the archive min/max identities, and the note that per-role `s` medians are not monotone |
| `replica-shape-error-2026-10-05.md` | `:271` (§1.5.b) | Struck "**4 clean groups**" → "4 role *labels*, not 4 disjoint `r` groups"; the n = 17/20/12/13 counts explicitly preserved |
| `replica-shape-error-2026-10-05.md` | `:294` (§1.5.b S2 table) | Struck Offense range `1.077–**22.500**` as a **monster row**; corrected to n = 11, `1.077–1.333`; ~~median preserved~~ **AMENDED 2026-10-06: the median was NOT preserved — see §11. It is 1.250 hero-only vs 1.263 monster-mixed, and the row's HP median (2700→2400) and ATK/HP median (0.565→0.536) were also contaminated and are now corrected.** |
| `replica-shape-error-2026-10-05.md` | `:560` + `:564` (§2.5 O5) | Band list corrected: `Offense ∪ Bomber 1.17–1.75` + `s` tie-break, with an explicit note that the two published ranges intersect over `1.3815–1.5815` |
| `candidate-hero-bases-2026-10-05.md` | — | **no change required.** Its §2.5 verdict table, §2.2 `s` headline and §7 limits statement all survive measurement. Its two soft spots are recorded in §6 above rather than edited, since neither is a false statement in the file. |

Pre-edit line numbers, for anyone comparing against an older checkout:
`hero-stat-divergence` `:63` → `:97`, `:250–251` → `:293`, `:456` → `:457`;
`replica-shape-error` `:225` → `:271`, `:245` → `:294`, `:318` → `:319`, `:501` → `:560`.
The header insertions are what shift them.

**Nothing was deleted.** Every original claim is preserved inline with `~~struck~~` plus a
replacement, per the strike-don't-delete requirement.

---

## 10. Limits

- **Read-only on all data.** The TSV and the Episode JSON were read; no source file, fixture,
  server, seed, APK, emulator or phone was touched.
- **Coverage effect: none.** Heroes 1/113, accessories 1/100, monsters 0/22. Nothing here is
  a base stat; every archive row still has `level = "not shown"` and
  `gear_state = "not established"`.
- **The 2-axis tree's 0/62 archive purity is weak evidence.** `r`, `s` and role all come
  from the same 62 rows, and the three thresholds were read off those rows. It shows the
  bands are *consistent*; it does not show they *predict*. The 15/37 `EVCB` failure rate
  (§5.3) is the honest out-of-sample number, and it is poor.
- **`s` is not gear-invariant in the way `r` is.** `r` cancels under any uniform scalar and
  any growth that scales ATK and DEF together; `s` cancels only if HP scales with
  ATK+DEF. `candidate-hero-bases` §2.1 states this caveat and it stands — `s` has **no**
  `051`-style invariance proof behind it, only the archive's internal consistency.
- **One community source, unknown level.** S1 is a Wayback capture of a third-party
  Japanese site. Its strength here is internal determinism, not authenticity.
- **The 0.70 % Defense|Support seam is a single integer step in one row's DEF**
  (`043` 726/792 vs `016` 660/715). Do not build a classifier on it.

---

## 11. Second instance of the same category error: the `CB*` family, and the filter rule (2026-10-06)

§8 fixed the `EVCB*` instance. A corpus-wide sweep found **five more**, and they share
one root cause: the corpus filters Episode STAT rows on `res_id` **namespace** (`C*`)
only, never on the combat record's **`type`**.

### 11.1 The safe filter rule (normative — use this from now on)

> **A row of `analysis/recovered-reference/EPISODE_STAT_ACTORS.json` is a HERO row if
> and only if `res_id` starts with `C` AND the row's `id`, looked up in the matching
> `EPISODE_COMBAT_<id>.json` record's `left`/`right` wave lists, has `"type": "hunter"`.**
>
> The second clause is **not optional**. `res_id` namespace alone admits **8 rows that
> are tuned and placed as enemies**:
> `CB0002_BOSS`, `CB0003_BOSS`, `CB0004_BOSS` (all `res_id C010`), and
> `CB1102_006`, `CB1102_008`, `CB1102_011`, `CB1102_018`, `CB1102_019`
> (`C006`, `C008`, `C011`, `C018`, `C019`) — all five right-side in
> `EPISODE_COMBAT_CB1102.json` at thumb `level 1 / rank 5 / hyper 2`.

Measured partition of the 152-entry file (entry index 80 is a literal `{}`):

| filter | rows | distinct `ref_id` | distinct `res_id` |
|---|---:|---:|---:|
| all entries | 151 | 56 | 86 |
| `res_id` starts `M` (monsters) | 34 | 4 | 22 |
| `res_id` starts `C` (**the corpus's "hero" set**) | 117 | **55** | 64 |
| `res_id` starts `C` **and** `type == "hunter"` (**safe**) | **109** | **54** | 62 |
| `res_id` starts `C` **and** `type == "monster"` | 8 | 6 | 6 |

Distinct `res_id` exceeds distinct `ref_id` because 9 `ref_id`s carry two art packs
(costume/awakened: `008`, `009`, `010`, `028`, `036`, `049`, `051`, `068`, `072`).

### 11.2 What is and is not contaminated

| statistic | verdict |
|---|---|
| **`EVCB*` anything** | **CLEAN.** All 37 `EVCB*` `C*` rows are `hunter`-typed, so the safe filter and the namespace filter agree exactly. §8's corrected table (Defense 8 / Support 12 / Offense 11 / Bomber 6, Offense `1.077–1.333`) stands as written. |
| **`CB*` family counts / distinct-value ladders** | **CONTAMINATED** by 8 rows. `CB*` is **72** hero rows, not 80; `hp` 47→46 distinct, `atk` 49→45 (floor 100→140), `spd` 6→5 (drops `4`), `crt_chance` 15→12, `hp_regen` 21 unchanged. |
| **Episode hero identity counts** | `117 / 55` is the corpus-wide **namespace** figure and is not wrong for what it measures (hero reference rows). It is **not** the hunter-actor count, which is `109 / 54`. Both are recorded; do not mix them. |
| **monster-side findings** (`22` distinct `res`, the 6 multi-tuple identities, `M034`'s 160× spread, inert secondary fields, `2/22` catalog overlap) | **UNAFFECTED** — they draw only on `M*` rows. |
| **the "37 monster-like rows" partition** | **INCOMPLETE**, not wrong-so-far: `34 M* + 3 C010` omits the 5 `CB1102_*` rows. Exhaustive = **42**. |

### 11.3 Per-role bands over *all* hero rows, safe filter (new, for reference)

`r = ATK/DEF`, `s = (ATK+DEF)/HP`, `n = 109`:

| role | n | `r` min…max (median) | `s` min…max (median) |
|---|---:|---|---|
| Offense (1) | 36 | 0.9000…18.6957 (1.3785) | 0.1733…1.1304 (0.8519) |
| Defense (2) | 32 | 0.6400…16.4000 (0.9129) | 0.1090…2.0294 (0.7978) |
| Bomber (3) | 21 | 1.1111…17.5000 (2.0000) | 0.3880…1.3214 (1.0000) |
| Support (4) | 20 | 0.8333…15.8333 (1.1111) | 0.2849…1.1483 (0.8798) |
| **ALL** | **109** | 0.6400…18.6957 (1.3333) | 0.1090…2.0294 (0.8750) |

**Do not read these as archetype bands.** Unlike `EVCB*`, the `CB*` rows are
per-combat scripted actors whose DEF is pinned near 140–290 regardless of HP, so
their `r` ceiling is ~18.7 and their `s` floor ~0.11. Any pooled hero `r`/`s`
statistic that includes `CB*` is measuring script shape, not role shape — which is
exactly why §2.5 and `candidate-hero-bases` §2.5 pool **archive + `EVCB*` only**.
The medians above are a *filter demonstration*, not a competing band set.

### 11.4 Scope of this pass

Read-only on `EPISODE_STAT_ACTORS.json`, `EPISODE_COMBAT_*.json`,
`archived-hunter-database-2019.tsv` and `catalogue/INDEX.md`; nine markdown files
edited via the `edit` tool with dated correction notes (nothing deleted);
`polluted-observations.md` **not** appended; no `server-ts`, fixture, seed, APK,
emulator or phone action; no Ghidra. **Coverage effect: none** — heroes 1/113,
accessories 1/100, monsters 0/22. Full sweep table, including the items left
**unedited** because they could not be reproduced:
[`episode-stat-namespace-filter-2026-10-06.md`](episode-stat-namespace-filter-2026-10-06.md).