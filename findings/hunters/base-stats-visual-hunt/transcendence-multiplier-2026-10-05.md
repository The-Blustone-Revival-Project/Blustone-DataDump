# Transcendence multiplier — adjudication (2026-10-05)

**Purpose.** Adjudicate the first quantified transcendence multiplier found in this
project: is there **one game-wide multiplier** on HP/ATK/DEF, does a **clean step
ladder** fit, and is the **`1.716` link on Beckhen `051` meaningful or
numerological**.

**Inputs.**

| Tag | Source | Date / era | Role here |
|---|---|---|---|
| **[WIKI-T3]** | `vsfan.net/wiki/{Captain,Hermes,Riko}`, Wayback, `oldid` 2323 / 7349 / 2615 | captures 2019-08-21 / 2019-08-26 / 2019-08-21 — **PRE** the 2019-09-05 rebalance | the **numerator**: three `Life/Attack/Defense` tables captioned `Transcendence Level: 3` |
| **[JP19]** | `archived-hunter-database-2019.tsv`, `blustone.jp/hunter`, 62 numeric rows | captures 2019-10-15 … 2019-12-16 — **POST** the rebalance | the **denominator**: unboosted values |
| **[BAHAMUT]** | `snA=56` (2018-01-30) player prose | 2018, PRE | "each breakthrough ≈ +10 % of the three stats"; seven total copies; rank retained on rank-up |
| **[COST]** | `transcendence-skill-cost-2026-10-05.md` §1.1 | 2017 / undated | the 3-step T1/T2/T3 **cost** matrix (costs only — it says nothing about stat growth) |
| **[051]** | `analysis/catalogue/stats/051.md` | FAQ screenshots dated **2018-12-22** era | the Lv.30 / no-equipment panel |

**Method.** All arithmetic below was recomputed this pass in Python from the TSV
and the transcribed integers; every interval and intersection is reproducible.
Three of the four `[WIKI-T3]` pages were additionally **re-fetched from the
Wayback `id_` copy this pass** and their `Stats` tables read directly — the
values below are re-verified against the primary source, not inherited from a
prior note.

**Nothing was changed.** No `server-ts`, fixture, seed, APK, state file, emulator
or physical phone was touched. `polluted-observations.md` was **not** appended.
The Ghidra project was not opened. No coverage count moves: heroes **1/113**,
accessories **1/100**, monsters **0/22**.

---

# 1. PURE — measured tables and arithmetic

## 1.1 Primary-source re-verification of the three T3 tables

`[WIKI-T3]` re-fetched 2026-10-05, `id_` (un-rewritten) form. All three carry
the literal caption `<caption>Transcendence Level: 3</caption>`.

| | Captain `009` | Hermes `023` | Riko `024` |
|---|---|---|---|
| oldid | 2323 | 7349 | 2615 |
| capture (UTC) | 2019-08-21 02:51:53 | 2019-08-26 08:11:15 | 2019-08-21 03:04:11 |
| **caption** | `Transcendence Level: 3` | `Transcendence Level: 3` | `Transcendence Level: 3` |
| **Life** | **2069** | **2275** | **2069** |
| **Attack** | **734** | **1218** | **868** |
| **Defense** | **1142** | **848** | **1047** |
| Attack Speed | 7 | 8 | 7 |
| Crit Chance | 14 % | 33 % | 14 |
| Crit Damage | 180 % | 200 % | 185 |
| Armor Pen | 1 % | 0 % | 0 |
| Block Chance | 33 % | 14 % | 33 |
| Block Resistance | 52 % | 40 % | 50 |
| Elem enhance / resist | 0 % / 0 % | 2 % / 2 % | 0 % / 0 % |
| Life Regeneration | 40 | 44 | 40 |
| infobox Rarity | **★ (1)** | **★★★ (3)** | **★★ (2)** |
| infobox Role | **Defense** | **Offense** | **Defense** |

The `[JP19]` denominator rows, verbatim from the TSV:

| | `009` | `023` | `024` |
|---|---|---|---|
| hp / atk / def | 1624 / 628 / 893 | 1750 / 937 / 653 | 1624 / 682 / 821 |
| `rarity_on_draw` | **1** | **3** | **2** |
| `capture_timestamp` | 20191015065805 | 20191210182657 | 20191015065805 |

**The infobox rarities and the archive's `rarity_on_draw` agree for all three.**
So the two corpora are at the same star grade and the ratio is not a rank
artefact.

## 1.2 CORRECTION to `vsfan-wiki-2026-10-05.md` §1.6/§1.7 — one transcribed cell is wrong

> **[2026-10-06 — THIS SUB-SECTION'S CENTRAL CLAIM IS RETRACTED. Its PRIMARY-SOURCE
> READING WAS CORRECT; its reading of `vsfan-wiki-2026-10-05.md` was not.]**
>
> ~~"Re-running the §1.7 tally from the primary pages gives **95 equal / 13
> different**, not the recorded **97 / 11**."~~ — **withdrawn.**
> ~~"`vsfan-wiki` §1.6 records `0` / `0`"~~ — **withdrawn. It records `5` /
> `5`.** The archived page and `vsfan-wiki` §1.6 **agree**; there was never a
> transcription error to correct, and the recorded **108 comparisons / 97 equal /
> 11 different** was right from the start.
>
> **Primary source consulted.** `vsfan-wiki-2026-10-05.md` §1.6 **re-fetched
> 2026-10-06** after two positive controls (`https://web.archive.org/` → HTTP
> 200 / 145,187 bytes; exact-match CDX on `vsfan.net/wiki/List_of_Hunters` →
> HTTP 200 / 3 rows). All eleven `Character Attributes` tables were re-fetched
> in Wayback `id_` form at the §1.4 ledger captures — including
> `https://web.archive.org/web/20190826075547id_/https://vsfan.net/wiki/Patrone`,
> capture **2019-08-26 07:55:47Z**, `oldid` **7439**, **122,245** bytes,
> sha256 `b78fab30a81f35bc3e69b10dc1eb652785fcf234c569a247ee0b0953a4620460`.
> Every fetch returned HTTP 200, every byte count equalled the ledger, and every
> page's footer `oldid=` equalled its ledger `oldid`.
>
> **Recomputed independently from the re-fetched bytes, not from either note:
> `108 comparisons · 97 equal · 11 different`** — 9 Life/Attack/Defense
> (Captain `009`, Hermes `023`, Riko `024`) plus 2 `hp_regen` off-by-ones
> (Captain `40` vs `41`, Riko `40` vs `41`). A control over the nine sub-stats
> alone returns **99 / 97 equal / 2 different**, the two being exactly those
> `hp_regen` cells. All 120 cells transcribed in `vsfan-wiki` §1.6 across the
> eleven tables were checked and **0 are wrong**, including the
> `Block Resistance` vs `Damage Reduction Block` label split, the caption
> presence/absence, the absence of `Life`/`Attack`/`Defense` on the eight partial
> tables, and the `%`-on-Captain/Hermes formatting. A new §1.6.1 in
> `vsfan-wiki-2026-10-05.md` records this audit; **the correct reading of this
> file's own §1.7 was already the right one.**
>
> **What survives unchanged in this section:** the `Patrone` primary reading
> (`5 / 5 / 38`), the nine T3 integers in §1.1, and the `97/108`
> "same underlying table" conclusion in §2.1 — which now stands on re-fetched
> bytes **and** on an independent recount, rather than on one of the two notes'
> transcriptions. **Do not edit the `Patrone` row to `0/0`.**

Re-running the §1.7 tally from the primary pages gives **95 equal / 13
different**, not the recorded **97 / 11**. The two extra differences are both on
**Patrone `033`**:

| field | `vsfan-wiki` §1.6 records | archived page (re-read this pass) | `[JP19]` |
|---|---|---|---|
| `033` Strengthen Elemental Attributes | `0` | **`5`** | `5` |
| `033` Elemental Attack Resistance | `0` | **`5`** | `5` |

The archived `Patrone` `Stats` table reads `…5 / 5 / 38` for those three rows
verbatim. **The wiki page agrees with the archive; the `vsfan-wiki` note's
transcription does not.** With `033` corrected to `5/5` the tally returns to the
recorded **108 comparisons / 97 equal / 11 different**, and the recorded
composition (9 Life/Attack/Defense + 2 `hp_regen`) is then exactly right.

**Consequence: the 97/108 "same underlying table" result stands, and it stands on
re-fetched bytes rather than on a transcription.** This correction does **not**
touch any of the nine T3 integers used below. ~~`vsfan-wiki-2026-10-05.md` §1.6's
Patrone row should be amended; that amendment is **proposed, not made here**.~~
**[2026-10-06: withdrawn — §1.6's Patrone row needs no amendment. See the
retraction at the head of §1.2.]**

## 1.3 The measured ratios and their additive form

| hero | field | wiki T3 | JP19 base | ratio | delta | delta % |
|---|---|---:|---:|---:|---:|---:|
| Captain `009` | hp | 2069 | 1624 | **1.27401** | +445 | +27.40 % |
| Captain `009` | atk | 734 | 628 | **1.16879** | +106 | +16.88 % |
| Captain `009` | def | 1142 | 893 | **1.27884** | +249 | +27.88 % |
| Hermes `023` | hp | 2275 | 1750 | **1.30000** | +525 | +30.00 % |
| Hermes `023` | atk | 1218 | 937 | **1.29989** | +281 | +29.99 % |
| Hermes `023` | def | 848 | 653 | **1.29862** | +195 | +29.86 % |
| Riko `024` | hp | 2069 | 1624 | **1.27401** | +445 | +27.40 % |
| Riko `024` | atk | 868 | 682 | **1.27273** | +186 | +27.27 % |
| Riko `024` | def | 1047 | 821 | **1.27527** | +226 | +27.53 % |

- all nine: min 1.16879, max 1.30000
- excluding Captain `atk`: min **1.27273**, max **1.30000**, spread **0.02727**
- per-hero internal spread: Captain 0.11005 (8.87 % of its mean), **Hermes
  0.00138 (0.11 %)**, **Riko 0.00255 (0.20 %)**

`[BAHAMUT]`'s "≈ +10 % of the three stats" per step, taken as a flat per-step
bonus on the base, predicts exactly **+30 % at T3** for ATK/DEF/HP. That is
Hermes to five significant figures, and it is within 2.1 % for 8 of 9 fields.

## 1.4 The exact-integer test — which single M can reproduce which integers

For a single multiplier `M`, a field with base `b` and reading `w` is satisfied
by `floor(b·M) == w` exactly when `M ∈ [w/b, (w+1)/b)`. Intersecting these:

| selection | interval (floor) | verdict |
|---|---|---|
| all 9 fields | `[1.30000, 1.17038)` | **EMPTY** |
| all 9 minus Captain `atk` | `[1.30000, 1.27419)` | **EMPTY** |
| Captain `009` alone | `[1.27884, 1.17038)` | **EMPTY** |
| Hermes `023` alone | `[1.30000, 1.30015)` | **NON-EMPTY**, width 1.5 × 10⁻⁴ |
| Riko `024` alone | `[1.27527, 1.27419)` | **EMPTY** |
| Captain `hp`+`def` only | `[1.27884, 1.27463)` | **EMPTY** |
| Riko `hp`+`atk` only | `[1.27401, 1.27419)` | NON-EMPTY, width 1.8 × 10⁻⁴ |
| all three, `round()` mode | — | **EMPTY for all three heroes** |

**Hermes is exactly `floor(1.30 × base)` on all three integers.** The window is
1.5 × 10⁻⁴ wide; hitting it three times independently is not a coincidence, so
**×1.30 is a real, integer-exact factor for `023`**.

**Riko's intersection is empty by 1.1 × 10⁻³, yet its fit is the best of the
three.** At `M = 1.275`:

| field | base | wiki | 1.275 × base | err |
|---|---:|---:|---:|---:|
| `024` hp | 1624 | 2069 | 2070.60 | **+1** |
| `024` atk | 682 | 868 | 869.55 | **+1** |
| `024` def | 821 | 1047 | 1046.77 | **−1** |

All three within one unit. So the empty intersection is a **rounding-level**
inconsistency, not evidence of a different rule: `024`'s three readings are
consistent with one multiplier at the ±1-integer level.

Least-absolute-integer-error search over the 8 non-outlier fields puts the best
single `M` at **1.2755** (mean 11.25 units/field over the whole set, dominated by
Hermes, which sits 16–44 units *below* 1.275). `M = 1.30` scores 140; `M = 1.275`
scores 92. **No single `M` is simultaneously integer-exact and low-error across
the corpus.**

## 1.5 The Captain ATK anomaly, re-derived

`734 / 628 = 1.16879`. Against 1.27273–1.30000 for every other field it is
**8.2 % below** the low end of the cluster. Candidate single-digit repairs,
computed by scanning every integer the JP denominator might have held:

- if the JP `009` **atk** were **576** instead of 628, `M ∈ [1.27431, 1.27604)` —
  which reconciles Captain `atk` with his own `hp`/`def` and with `024`.
- 576 is **not** a hypothesis out of thin air: it is the **minimum ATK in the
  whole 62-row archive**.
- no single wiki-side value for Captain `atk` in 700–769 reconciles him.

So Captain's ATK is either a transcription error on either side, or the only
evidence of a field-specific rule. **Unresolved.**

## 1.6 The identical `2069` — duplication error or forced?

Captain `009` and Riko `024` both read wiki HP `2069` and both have archive HP
`1624`. Measured structure of the archive's HP column:

- **62 rows carry only 20 distinct HP values**; 13 of those values are shared,
  covering **55 of the 62 rows**.
- `1624` is shared by **seven** heroes: `002, 005, 009, 021, 024, 032, 034`.
- `1624 × 1.27401 = 2069.0` exactly.
- Captain and Riko **also share** archive `hp_regen 41`, and both wiki rows read
  `40` — the `hp_regen` off-by-one lands on exactly these two heroes.

**Verdict: this is a forced consequence, not a wiki duplication error.**

1. HP in the archive is **quantised** — a shared base value maps to a shared
   reading under any common multiplier, so identical HP is *expected* for 55 of
   62 heroes.
2. A whole-row copy is **excluded**: Captain `atk 734 / def 1142` versus Riko
   `atk 868 / def 1047`, and their nine sub-stats differ in four fields
   (`crit_damage 180/185`, `pen 1/0`, `block_resist 52/50`).
3. The two heroes are of **different grades** (`★` and `★★` on the infobox) and
   **different roles are not the cause** — both are Defense — yet they share
   base HP. That is exactly what the lattice predicts.
4. The `hp_regen` off-by-one landing on the same pair is consistent with one
   *shared edit event* on those two rows in one of the two corpora, and is
   recorded as open in `vsfan-wiki` §2.4. **It does not license re-using one
   hero's HP for the other** — the ratio identity is what carries.

**A separate, genuine identity is not implied**: nothing here says Captain and
Riko have the same *nude* HP in the shipped game; it says the two recovered
corpora agree they do.

## 1.7 The 1.716 question, measured

`[051]`: archive `1678 / 864 / 660` (level `not shown`, gear `not established`,
rarity_on_draw 3) against the panel `2879 / 1471 / 1149`.

| field | panel / archive | deviation from 1.716000 |
|---|---:|---:|
| hp | 2879 / 1678 = **1.715733** | **−0.016 %** |
| atk | 1471 / 864 = **1.702546** | −0.784 % |
| def | 1149 / 660 = **1.740909** | +1.452 % |

- `1.10 × 1.20 × 1.30 = 1.716000`.
- The three scalars occupy `[1.70255, 1.74091]`, a **2.25 % band**. The
  defensible 3-s.f. summary is **≈1.720 ± 1.1 %**, not "1.716".
- Shape ratios, which is what `[replica-shape-error]` §1.5.d actually used:
  `atk/hp 0.51490 → 0.51094 (−0.77 %)`, `def/hp 0.39333 → 0.39910 (+1.47 %)`,
  `atk/def 1.30909 → 1.28024 (−2.20 %)`.

If the archive row is a level-1 table and the panel is Lv.30, the same
three numbers read as a **level** factor, not a transcendence factor:

| field | per-level compound over 29 steps | flat per-level add |
|---|---:|---:|
| hp | 1.01879 | 41.41 |
| atk | 1.01852 | 20.93 |
| def | 1.01930 | 16.86 |

Three independent fields landing on a per-level compound of **1.0185–1.0193**
(0.4 % spread) is itself a coherent reading, and it is the reading the archive's
own HP band supports: the archive spans **1277–2033** over 62 rows, and the
panel's 2879 sits **above the archive maximum**, exactly as a levelled-up card
should.

---

# 2. UNPURE — the multiplier as a rebalance token

Everything in §2 is inference. **Era: `[WIKI-T3]` is PRE the 2019-09-05
rebalance (2019-08 captures); `[JP19]` is POST (2019-10 … 2019-12 captures); the
Bahamut prose is 2018; the 051 panel is 2018-12-22-era.** The two corpora being
on opposite sides of a balance patch is an unquantified confound and is the
single largest limitation on every number above.

## 2.1 Q1 verdict — one game-wide multiplier, or hero-specific?

**There is no single game-wide multiplier, and no single-`M` explanation is
required to describe the data. The defensible statement is a two-cluster one.**

| cluster | members | factor | strength |
|---|---|---|---|
| **A** | Hermes `023` (all 3) | **exactly `×1.30`**, integer-exact 3/3 | strongest single result in the corpus; window 1.5 × 10⁻⁴ |
| **B** | Riko `024` (all 3), Captain `009` hp/def | **≈ ×1.274–1.279**, ±1 integer at 1.275 | tight internally (0.11–0.20 % spread) |
| **outlier** | Captain `009` atk | 1.169 | 8.2 % below cluster B |

**Is a corpus wrong?** **Neither is wholesale wrong, and that is provable.**
`[WIKI-T3]` and `[JP19]` agree on **97 of 108** fields including all nine sub-stats
of all eleven compared heroes — they are demonstrably transcribing the same
underlying table. Only the nine Life/Attack/Defense fields differ, and those are
precisely the fields the `Transcendence Level: 3` caption claims are boosted. So
neither corpus is garbage; the disagreements are localised exactly where the
caption predicts.

**Which reading survives?**

1. **One global `×1.30`, with `009`/`024` off by ~2 %.** Supported by the
   integer-exactness of Hermes and by `[BAHAMUT]`'s "+10 % × 3 steps = +30 %".
   Requires ~2 % of unexplained error on four fields and a whole 13 % error on a
   fifth.
2. **Role-conditional** (`Defense ≈ 1.274`, `Offense = 1.300`). **Measured, but
   n = 2 vs n = 1.** Note this is *not* rank: `009` is ★, `024` is ★★ and both
   read 1.274, while `023` is ★★★ and reads 1.300 — so the split tracks **role**,
   which is the axis the archive and the shipped Episode rows both independently
   structure. **Recorded as a hypothesis, explicitly not a finding.**
3. **Per-field rules.** Not supported — 8 of 9 fields are one scalar within
   rounding; only Captain `atk` resists.

**Honest position:** cluster A (`×1.30`) is *established for Hermes and
plausible game-wide*; cluster B (`≈1.274`) is *established for `024` and
Captain's hp/def*; the difference between them is **2.0 % and unexplained**;
Captain's ATK is a **13 % anomaly**. **Do not implement `×1.30`. Do not implement
`×1.274` either.** A per-hero or per-role table is the only shape the evidence
tolerates, and a *single* scalar is not licensed by any arithmetic performed
here.

## 2.2 Q2 verdict — does a clean step ladder fit?

**`T1 = 1.10, T2 = 1.20, T3 = 1.30` fits — as a FLAT per-step ladder, so that
`T3 = 1.30`. The CUMULATIVE PRODUCT `1.10 × 1.20 × 1.30 = 1.716` does not fit,
and is refuted by a factor of ~25 %.**

| candidate interpretation of "1.10 / 1.20 / 1.30" | T3 value | worst err (9) | within 2.1 % | within 0.5 % | fits? |
|---|---:|---:|---:|---:|---|
| flat +10/+20/+30 **of base** | **1.30** | 10.09 % | **8/9** | **3/9** | **YES** |
| compounded ×1.10 three times | 1.331 | 12.19 % | 0/9 | 0/9 | no |
| **cumulative product 1.10·1.20·1.30** | **1.716** | **31.89 %** | **0/9** | 0/9 | **NO** |
| flat +10 % | 1.10 | 18.18 % | 0/9 | 0/9 | no |
| flat +20 % | 1.20 | 8.33 % | 0/9 | 0/9 | no |
| compounded ×1.10 twice | 1.21 | 7.44 % | 0/9 | 0/9 | no |

Against the 8 non-outlier fields only, `T3 = 1.30` scores worst **2.10 %**,
mean **1.22 %**; `T3 = 1.716` scores worst **25.83 %**, mean **25.16 %**.

**The two readings of "1.10 / 1.20 / 1.30" must never be conflated again.** They
differ by **32 %**, and the whole project turns on which one a note means. The
Bahamut prose — "each breakthrough ≈ +10 % **of the three stats**" — is the flat
reading (`+30 %` at T3), and the `大約` ("approximately") is load-bearing.

**Three limits that travel with "a flat ladder fits":**

1. **Only the T3 endpoint is measured.** The other eight `[WIKI-T3]` tables have
   **no `Life`/`Attack`/`Defense` row at all** — the rows are *absent from the
   wikitext*, not blank. So there are **zero T1 observations and zero T2
   observations in this project**. `1.10` and `1.20` are **untested**, not
   confirmed. A ladder with `1.10 / 1.20 / 1.30` and a ladder with
   `1.05 / 1.18 / 1.30` predict identical T3 values and are **indistinguishable
   on the available evidence**.
2. **The step ladder and the measured ratio are the same three numbers.** Fitting
   a ladder to a single endpoint cannot validate the ladder's shape. This is a
   one-degree-of-freedom fit dressed as a three-point confirmation.
3. **`[COST]` constrains nothing here.** It supplies the 3-step **cost** matrix
   (grade × T1/T2/T3 crystal/fragment/rupee/duplicate counts) and its own §2.2
   note says the source is about stat growth only in the sense that it is
   silent. Nothing in it implies a stat multiplier.

## 2.3 Q3 verdict — is the 051 panel transcended?

**The coincidence is not meaningful. It is numerological, and the corpus
refutes it.**

**How the 051 panel is actually labelled** — checked in every place it appears:

| place | how it is labelled |
|---|---|
| `analysis/catalogue/stats/051.md` | heading **"Measured at: Lv.30, no equipment"**; rarity **3 stars**; identity exact-string matched (`TITLE/WEAPON/ARMOR/ACCESSORY` all four on-screen); era **2018-12-22-era FAQ** |
| same file, the gear-removed derivation | **not an assumption** — Strength `24068 + 6291 gear = 30359` matches the separate fully-geared card page **exactly**, and the six jewel sub-stats independently sum to the same green delta (DEF `102+11+11+29 ≈ 154`, HP `260+58+21+58+18+21 ≈ 437`, etc.) |
| `analysis/catalogue/stats/README.md` §5, `010_1.md` | "Both cards are Offense / Ice at Lv.30"; no transcendence state is asserted |
| `analysis/research/base-stats-visual-hunt/polluted-observations.md` | the gear-removed *UI convention* is asserted for Beckhen (line 179); Beckhen's own entry (line 291+) is skill-effect context, **not** a stat-state claim |
| `reddit-memorial-galleries.md` | **no Beckhen / `051` entry at all** (grep: no matches) |

**The panel is explicitly a "no equipment" reading and says nothing about
transcendence.** The `2879/1471/1149` white column is a *gear* statement.

**Three independent reasons the 1.716 link fails:**

1. **It is refuted by the corpus that defines the quantity.** If T3 were `1.716`,
   the three pages *literally captioned* `Transcendence Level: 3` would show
   `≈1.716`. They show `1.16879 … 1.30000`. **The maximum measured T3 ratio in
   this project is 1.30000.** `1.716` is **31.9 % above** it and cannot be a T3
   factor under any reading of the evidence.
2. **The card could not be T3 anyway.** `[051]`'s rarity is **3 stars**.
   `[COST]` §1.3 and the original 1.4.4.1 help `CONTENTS4_3` both put the T1 floor
   at **★3**; `[EN-2017]`'s step gate is **T1 ≥3★, T2 ≥4★, T3 ≥5★**. A 3★ badge
   therefore reaches **at most T1**, and no ladder step in either reading of
   §2.2 is anywhere near `1.716` (`1.10`, or `1.21` compounded). `[BAHAMUT]`'s
   "rank retained on rank-up" only makes this *tighter*: a card transcended at
   ★3 and advanced to ★5 keeps **T1**, not T3.
3. **The arithmetic is a point estimate with a ±1.1 % half-width, chosen after the
   fact.** The three scalars span `1.70255 … 1.74091`. Stating the scalar as
   "1.716" — to four significant figures — reports one draw from a 2.25 % band
   as though it were a constant, and then matches it to a four-significant-figure
   product. `1.10 × 1.20 × 1.30 = 1.716000` is **constructed**, not recovered:
   the corpus contains one number near `1.716` and the ladder was fitted to it.

**What the 1.716 actually is, most plausibly:** a **level** factor, because
`[JP19]`'s `level` column reads `not shown` for all 62 rows while `[051]` is
**Lv.30**. Three independent fields give a per-level compound of
**1.0185–1.0193** over 29 steps (0.4 % spread), and the panel's HP `2879` sits
**above the archive's entire 62-row HP band of 1277–2033** — exactly where a
levelled-up card belongs. That reading also requires no new mechanism and no
exception for one hero.

**Consequence for `[replica-shape-error-2026-10-05.md`:** its §1.5.d use of the
`051` pair is **unaffected and still sound** — the claim there is *ratio
invariance* under a magnitude change (≤2.2 %), and that is a ratio claim, not a
multiplier claim. Only the word **"1.716×"** in its prose needs softening to
**"≈1.72×"**, and it must not be described as a transcendence factor. That file
was **not** edited here; the correction is proposed.

## 2.4 Confidence ledger

| claim | confidence | basis |
|---|---|---|
| `[WIKI-T3]` numerators are correct and captioned T3 | **high** | three `id_` re-fetches this pass, verbatim |
| `×1.30` is integer-exact for Hermes `023` | **high** | 3/3 exact, window 1.5 × 10⁻⁴ |
| the nine T3 ratios span 1.16879–1.30000 | **high** | arithmetic only |
| no single `M` reproduces all nine integers | **high** | interval intersection empty, both floor and round |
| `024` is consistent with one `M` to ±1 integer | **high** | all three fields within 1 unit at 1.275 |
| identical `2069` is forced by a shared base `1624`, not a wiki copy error | **medium-high** | 55/62 archive rows sit in an HP tie; row-copy excluded by differing atk/def/sub-stats |
| a **flat** ladder fits, `1.716` does not | **high** | 8/9 within 2.1 % vs 0/9; refuted by the T3 captions themselves |
| `1.10` and `1.20` are the per-step factors | **low — UNTESTED** | zero T1/T2 observations exist |
| `1.274` vs `1.300` is role-conditional | **low** | n = 2 vs n = 1; a hypothesis |
| Captain `atk` is a transcription error | **low-medium** | a single-digit JP repair (628 → 576, the archive minimum) reconciles him; unproven |
| the 051 panel is *not* transcended | **high** | 3★ badge vs a ★5 T3 gate; explicit "no equipment" label; corpus shows T3 = 1.30 max |
| the 051 `1.72` scalar is a level factor | **medium** | three fields agree to 0.4 %; panel HP exceeds the archive band |

## 2.5 What would settle the open items

1. **A fourth and fifth `[WIKI-T3]` table.** The eight partial tables have the
   rows absent from the wikitext; a **page revision** that adds them (the wiki is
   MediaWiki with per-page `oldid`s, so `action=history` on e.g. `Bear` or `Lapis`
   is the cheap probe) would give T1/T2 observations and turn §2.2's ladder from
   untested to tested. **Highest value, lowest cost.**
2. **A T1- or T2-captioned page**, which would break the `1.10/1.20/1.30`
   degeneracy directly.
3. **A `Life/Attack/Defense` panel for a 5★ hero**, which is the only state that
   could legally be T3 under the step gate — and would say whether `1.30` holds
   at a different rank.
4. **Any archived page that states a level for the reference table.** The
   `level: not shown` column is what makes every ratio here a compound of
   *unknown level difference* × *unknown transcendence factor*. Closing it
   separates the two.
5. **A second Defense hero with a complete table**, which would take §2.1's
   role hypothesis from n = 2 to n = 3 and make it testable.

## 2.6 Standing prohibitions

- **Do not implement `×1.30`**, and do not implement `×1.274`. Neither is
  licensed: no single `M` fits, and the corpus cannot distinguish one global
  factor from a role-conditional one.
- **Do not implement `1.10 / 1.20 / 1.30` as per-step factors.** Only the `T3`
  endpoint is measured; the first two are untested and the fit has one degree of
  freedom.
- **Never write "1.10 × 1.20 × 1.30" as a transcendence figure.** It is refuted by
  a factor of ~26–32 % against the corpus's own T3 captions. If a note wants the
  cumulative product, it must state that it is refuted.
- **Do not credit any of this as a base stat.** Heroes stay **1/113**,
  accessories **1/100**, monsters **0/22**. These are progression-state
  multipliers with an unstated level and an unstated era on both sides.
- **Do not smooth Captain's ATK away.** It is the corpus's one large anomaly and
  it is the only evidence that a field-specific rule might exist.

---

## 3. Files touched

- **New:** this file only.
- **Read:** `vsfan-wiki-2026-10-05.md` §1.6/§1.7/§2.2,
  `bahamut-remaining-2026-10-05.md` §2, `transcendence-skill-cost-2026-10-05.md`,
  `replica-shape-error-2026-10-05.md` §1.5.d, `analysis/catalogue/stats/051.md`,
  `analysis/catalogue/stats/010_1.md`, `analysis/catalogue/stats/README.md` §5,
  `polluted-observations.md` (read-only), `archived-hunter-database-2019.tsv`.
- **Re-fetched (read-only, Wayback `id_`):** `Patrone` (oldid 7439),
  `Hermes` (7349), `Riko` (2615), `Captain` (2323).
- **Proposed corrections, NOT applied:** ~~`vsfan-wiki-2026-10-05.md` §1.6 Patrone
  row (`0/0` → `5/5`)~~ **[2026-10-06: WITHDRAWN — §1.6 already records `5/5`;
  the proposed change would have corrupted correct data. See §1.2.]**
  `replica-shape-error-2026-10-05.md` §1.5.d "1.716×" →
  "≈1.72×" and its description as a magnitude rather than a transcendence factor.
- **Not touched:** `polluted-observations.md` (**not appended**), `coverage.md`,
  `README.md`, all TSVs, `server-ts`, fixtures, seeds, the APK, the emulator,
  the physical phone, the Ghidra project.
