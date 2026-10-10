# The client itself ships the archive's "base stat" heading — base-ness is now client-attested

**Written:** 2026-10-06. **Origin:** the `level-factor-test-2026-10-05.md` lane
re-fetched six `blustone.jp` profiles, found a label the prior note had never seen,
and correctly **refused** to reclassify the 62 archive rows on 6-of-62 evidence.
It named the decisive next probe. This file reports that probe.

**This does NOT edit `coverage.md`.** That file is the authoritative count and owns
the definition of "counted". The reclassification is put to adjudication in §5
with a recommendation, not applied.

---

> ## RETRACTED 2026-10-06 — the load-bearing inference is REFUTED
>
> This file's §1 established two things that **stand**:
>
> 1. The client ships the heading — `UI_TEXT_RO[329]`/`[567]` `TR_캐릭터 기본 능력치`
>    → EN **"Base Stat"** / JA `基本能力값`, rendered at `UI_JSON_RO[10756]`
>    `캐릭터 기본 능력치|TX_ST_TL1`, SIZE 28, and `TX_ST_TL1` occurs **exactly 5
>    times with exactly one label**.
> 2. The archive uses **both** of the game's headings byte-identically, and the
>    block's contents are **exactly HP / DEF / ATK / Attack-Speed**
>    (`RE_CH_DI1` under `TX_ST_TL1`, `UI_XML_RO[275]`).
>
> **What is REFUTED is the inference this file drew from them.** The claim
> *"therefore the 62 rows are gear-free **base** values"* does **not** follow.
> Full hostile analysis: `adversarial-heading-check-2026-10-06.md` (verdict
> **SURVIVES-WITH-CAVEAT** — the evidence survives, the inference does not).
> Three independent grounds, all verified by the parent:
>
> - **The same block is used on the equipment screens.** `TX_ST_TL1` + `RE_CH_DI1`
>   occurs in **four** layouts — `UI_XML_RO[275]` `SR_COMMON/1_UI_CM_CH` plus
>   **[367] `SR_ENHANCE/3_SR_EN_CH`**, **[376]
>   `SR_ENHANCE/3_SR_EN_CH/TR_TEAMMATE`**, **[402] `SR_EQUIP/EQUIP_MAIN`**. Three
>   of four are gear screens, and `[376]` also carries `RE_LEVEL_GAUGE`, so the
>   block is **level-bearing**.
> - **`기본 능력치` is a live, buffable combat pool.** `SKILL_REF_RO[554]`
>   (`051|5|0`) "Increases the basic ability of self by 10% during a Fight Club
>   battle"; `SKILL_REF_RO[784]` the same for teammates in Guild Blitz;
>   `TAG_REF_RO[14]` `BLITZ_TEAM_BONUS` and `[54]` `FIGHTCLUB_BOUNS` both "+10 %
>   basic stat"; `UI_TEXT_RO[418]` (Awakening) "Your basic stats will increase".
> - **EN "Base" is a generic adjective.** `UI_TEXT_RO[68]` renders bare `기본` as
>   EN "Base" for a *skill tag*. Gear-exclusion vocabulary is **0** in KO/EN/JA.
>
> **`gear_state` therefore remains `not established` on 63/63 rows, and hero
> coverage STAYS 1/113.** §5's recommendation to upgrade to 62/113 is
> **withdrawn**. The one bound that does survive: equipment unlocks at ★4, so
> gear contamination is structurally impossible for **57 of 62** rows and live
> only for the 5 four-star rows.
>
> Two further corrections to this file, from `rarity-column-audit-2026-10-06.md`:
> **§2.1's "monotone and near-disjoint" is overstated** (2★ sits wholly inside 1★
> with zero separation; ATK and DEF are not monotone at all), and the suspected
> `009` rarity defect is **exonerated** — the rarity is right and the *stat row*
> is a near-copy (12 of 13 fields shared with `005`).


## 1. PURE — the client ships both archive headings, verbatim, in all five locales

Source: `analysis/recovered-data/leveldb-tables/all-tables.json`
(`UI_TEXT_RO` 1 589 entries, `UI_JSON_RO` 12 351 entries — `summary` key).

### 1.1 The core-stat block heading

| file:index | key | KO | **EN** | **JA** | SC | TC |
|---|---|---|---|---|---|---|
| `UI_TEXT_RO[329]` | `TR_캐릭터 기본 능력치` | 기본 능력치 | **Base Stat** | **基本能力値** | 基本能力值 | 基本能力值 |
| `UI_TEXT_RO[567]` | `능력치` | 기본 능력치 | **Base Stat** | **基本能力値** | 基本能力值 | 基本能力值 |

### 1.2 It is rendered as a **stat-block title widget**, not body text

`UI_JSON_RO[10756..10760]`, key `캐릭터 기본 능력치|TX_ST_TL1|{EN,JA,KO,SC,TC}`:

```
TEXT "Base Stat"  SIZE 28  B_RECT 25|25  B_SIZE 400|40  ALIGN left|center
```

`TX_ST_TL1` reads as *stat title 1* — the game titles a statistics block with
this string. Size 28 against body text is a section heading.

### 1.3 The sub-stat block has its **own, different** heading

| file:index | key | EN | JA |
|---|---|---|---|
| `UI_TEXT_RO[324]` | `TR_능력치 상세 정보` | **Stat Details** | **詳細能力値** |
| `UI_TEXT_RO[323]` | `TR_공격 세부 능력치` | Attack Stat Details | 攻撃詳細能力値 |
| `UI_TEXT_RO[325]` | `TR_방어 세부 능력치` | Defense Stat Details | 防御詳細能力値 |

**This is the load-bearing part.** The game has exactly two stat headings —
`基本能力値` ("Base Stat") and `詳細能力値` ("Stat Details") — and the 2019 JP
archive pages use **both, byte-identically**: `基本能力値` above the HP/ATK/DEF
block and `詳細能力値` above the sub-stat blocks.

So the portal was not inventing a label or translating one. It was transcribing
**the game's own two stat-block headings**, and the core triple it recorded sits
under the one the client calls **"Base Stat"**.

> ~~**Verdict: base-ness is [RECOVERED] client-side evidence, not a portal claim.**~~ **RETRACTED 2026-10-06 — see the banner above.** The heading exists and matches; it does **not** imply gear-exclusion.
> The prior caveat — that `基本能力値` is "a portal term not yet located in any
> client string table" — is **retracted**. It is in `UI_TEXT_RO` and rendered by
> `UI_JSON_RO`.

---

## 2. PURE — the archive rows carry the core triple, and rarity for every row

`analysis/research/base-stats-visual-hunt/archived-hunter-database-2019.tsv`.
Columns include `combat_power hp atk def speed crit crit_damage penetration block
block_damage_reduction element_enhance element_resistance hp_regen level
gear_state`.

| measure | value |
|---|---|
| data rows | **63** |
| rows with numeric `hp`+`atk`+`def` | **62** |
| the 63rd | `056` Genovia, `fetch_status = non-numeric-core-stats`, `hp = '???'` |
| distinct `catalog_id` | **63**, none empty |
| distinct `level` values | `{"not shown": 63}` |
| distinct `gear_state` values | `{"not established": 63}` |
| `rarity_on_draw` populated | **63 / 63** |
| distinct `hp` values | **20** across 62 rows |

`rarity_on_draw` distribution: **1★ 12, 2★ 11, 3★ 34, 4★ 6** (63 total,
including the placeholder).

### 2.1 The base table indexes on **rarity** — bands are monotone and near-disjoint

| `rarity_on_draw` | n | HP range | ATK range | DEF range |
|---|---:|---|---|---|
| 1★ | 12 | 1277 – 1624 | 576 – 944 | 540 – 893 |
| 2★ | 11 | 1395 – 1624 | 628 – 1014 | 580 – 893 |
| 3★ | 34 | 1521 – 1968 | 689 – 1058 | 653 – 1284 |
| 4★ | 5 | 1923 – 2033 | 755 – 1032 | 718 – 1070 |

Monotone in HP with only slight overlap at the 1★/2★ and 3★/4★ seams, and
**only 20 distinct HP values serve 62 rows**. That is the signature of a
**designed lookup table keyed on (hero, rarity)** — not a level ladder.

This independently corroborates `level-factor-test-2026-10-05.md`'s arithmetic
negative (consecutive HP ratios span 1.0046–1.0924, so no ~1.9 %/level compound),
and explains it: the column is not indexed by level at all. It also explains the
heavy tuple reuse that lane found — e.g. `005` Gerard and `009` Captain both read
`1624/628/893` — which is a lookup table hitting a shared row, not a transcription
error.

---

## 3. UNPURIFIED — what is still not established

1. **`level` is `not shown` on all 63 rows.** Natively, hero stats *are*
   level-indexed (`/reference/GetLevel.card` is per-level, per-rank). So these
   triples sit at an unstated level. §2.1 argues the column is rarity-keyed
   rather than level-keyed, which would make level irrelevant for the *base*
   row — but that is inference from band structure, **not proof**.
2. **`gear_state` is `not established` on all 63 rows.** The heading being
   "Base Stat" makes gear-exclusion *likely* — the game has a separate
   gear/stat-delta presentation, and prior project work calibrated that
   white-stat/green-delta layout. But a portal could still have transcribed
   geared values into that block. **This is the single largest residual risk.**
3. **Portal transcription fidelity.** One corpus-wide control supports it: the
   vsfan wiki and this archive agree on **97 of 108** overlapping sub-stat
   fields, which is strong evidence both transcribe the same source correctly.
   It is not proof for the core triple specifically.
4. **Era.** Captures are 2019-10-15, before the **2019-09-05** rebalance? No —
   *after* it, by ~40 days, so post-rebalance. Hero base stats are not among the
   announced rebalance axes (equipment +50 %, crystal stats, upgrade gains after
   equipment Lv.20), so these should be current-era. Recorded as reasoning, not
   proof.
5. **`combat_power` is on every row** and remains unexplained — see §6.

---

## 4. A probe that was void, recorded so it is not repeated

The obvious first move — grep the native string tables for `기본능력값` — is
**structurally incapable of succeeding**, and I ran it before checking:

```
POSITIVE CONTROL: total Hangul chars in analysis/native-all-strings.tsv  ->  0
                  native-evidence.tsv                                    ->  0
```

Both tables are **printable-ASCII exports**. All eight Hangul term searches
returned `hits=0`, and every one of those zeros was a **false negative**. The
correct locus is `UI_TEXT_RO` / `UI_JSON_RO`, which are the locale-bearing
tables. This is the §5 "run a positive control before reading a zero" rule
paying out on a probe I ran myself.

---

## 5. Adjudication requested — `coverage.md` hero count

**Recommendation: upgrade hero base-stat coverage from 1/113 to 62/113**, on the
grounds that base-ness is now client-attested (§1) and the column is
rarity-keyed (§2.1).

**Against, and why the call is not mine:** `coverage.md` defines what "counted"
means, and the honest gap is §3.1 — **level is unstated on every row**. If the
definition requires a stated level, these do not qualify and the count stays
1/113. If "base stat" is taken to mean the gear-free triple regardless of level,
they qualify.

This is precisely the kind of definitional call that belongs to the file that
owns the definition. **I have not edited `coverage.md`, `README.md`, or any
TSV.** No stat value anywhere has been altered by this work.

---

## 6. Correction to an existing file

`archived-hunter-database-2019.md:61` describes `051` Beckhen as **"Lv.30,
5★"**. The archive row for `051` gives `rarity_on_draw = 3`, and the FAQ badge
and `051.md` also say **3★**. The "5★" is a **transcription slip**.

This matters beyond bookkeeping: the T3 refutation argument in
`transcendence-multiplier-2026-10-05.md` and `level-factor-test-2026-10-05.md`
rests on `051` being **3★** (a 3★ hero can reach at most T1). The slip was in the
direction that would have *broken* that argument, so correcting it strengthens
an existing retraction. Not edited here — flagged for the owning lane.

---

## 7. Reproduction

Scripts (read-only, no writes outside temp):
`%TEMP%\opencode\probe_basic_label.py` (void-probe + its control),
`probe_en_heading.py` (term sweep), `extract_basestat.py` (path extraction),
`final_basestat.py` (chain + TSV completeness), `check051.py` (rarity bands).
All indices above are `all-tables.json` array indices into `tables.<NAME>` and
re-derive exactly.

Unchanged by this work: `server-ts`, fixtures, APK, seeds, emulator, phone,
Ghidra, the native library, and all coverage counts.
