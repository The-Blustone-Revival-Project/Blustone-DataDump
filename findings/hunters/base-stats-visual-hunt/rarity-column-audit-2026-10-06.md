# Rarity-column audit — `archived-hunter-database-2019.tsv` / `rarity_on_draw`

**Written:** 2026-10-06. **Target:** `analysis/research/base-stats-visual-hunt/archived-hunter-database-2019.tsv`,
column `rarity_on_draw` (63 rows, 62 with a numeric core triple; `056` Genovia is a
`???` placeholder).

**Why this file exists.** `base-stat-heading-client-attested-2026-10-06.md` §2.1 makes
the rarity column load-bearing: it argues the archive's base-stat table is keyed on
**rarity** because HP bands grouped by `rarity_on_draw` are "monotone and near-disjoint",
and it proposes upgrading hero base-stat coverage from **1/113 to 62/113** partly on
that basis. `captain-009-duplicate-row-2026-10-06.md` §2 then flagged one suspected
copied row (`005`/`009`) that "breaks the banding". The column had never been audited.

**Files written by this audit:** this file only. `archived-hunter-database-2019.tsv`,
`coverage.md`, `server-ts`, fixtures, the APK, seeds, the emulator, the phone and Ghidra
were **not** modified. `polluted-observations.md` was read but **not** appended to.

---

## 0. Method, and the positive control that gates every number below

Guard read first: `GUARD-encoding-and-archive-traps.md`. All reads/writes via
`edit`/`write`/Python `encoding='utf-8'`. No `Get-Content`/`Set-Content`. Output
written LF, verified `U+FFFD == 0` and `CRLF == 0` (§8).

**Positive controls run before any zero or rate was believed**
(`%TEMP%\opencode\rarity_positive_control.py`):

| control | result | why it matters |
|---|---|---|
| A — both target files exist and are non-empty | TSV 33 224 B; 121 catalogue `.md` | the zeros below are not "file missing" |
| B — TSV parser known-answer test on 4 ids | `005`(2★,1624,628,893), `009`(1★,…), `036`(3★,1923,755,864), `056`(4★,`???`) all exact | the parser reads the right cells |
| C — catalogue rarity regex on known ids | `036`→3, `005`→2, `009`→1, and **also** `010_1`→5, `004_1`→5 | fires on base *and* awakened namespaces, so it is a real read |
| D — the literal searched for exists on disk | 61 files contain both `Rarity / grade` and ``wiki Infobox `Rarity` `` | a regex miss cannot masquerade as "rare hero" |
| E — the three extra sources are not silent zeros | `char-str.tsv` 16×U+2605, vsfan note 270×, trace-vote 40×, uncovered roster 0×, polluted-obs 136×, reddit-memorial 0× | any later zero is measured against a known baseline |

**One self-inflicted false negative, caught and fixed.** My first cross-check run
reported source C at **0.00 % agreement on 55/55 rows** — every row "disagreeing".
That was my own bug: `report()` compared an `int` from the archive against a
`(name, stars)` **tuple** from the vsfan parser. Re-run with the tuple unwrapped: **98.18 %**.
Per `GUARD`'s "a stable metric is a fact about the measurement, not about the system",
this is recorded rather than quietly fixed.

---

## 1. VERDICT (short form)

| question | answer |
|---|---|
| Is the rarity column reliable? | **Yes, for its stated meaning.** 1 disagreement in 143 comparable comparisons across 3 domains; the single known outlier (`018` Robin) is already documented and adjudicated *against* the outlier, in the archive's favour. It is **not** independently sourced — see §3.4. |
| Does it agree with other sources? | **142/143 = 99.30 %**. Every disagreement named in §3. |
| Is recruit-grade the same axis as stat-index grade? | **It is the same axis, and that axis is MUTABLE.** `rarity_on_draw` is the **recruit grade**, not a hero-invariant property. §4. The banding argument **survives but must be restated**; one clause of it is refuted and one gap of it is closed. |
| Does the banding argument survive? | **Yes, weakened and restated.** HP banding is real but is **not** "near-disjoint" — 1★/2★ has *zero* range separation, and ATK/DEF are **not monotone at all**. §2. |

---

## 2. TASK 1 — internal consistency of `rarity_on_draw` against the HP bands

### 2.1 The bands, re-derived

| `rarity_on_draw` | n (numeric) | distinct HP | HP min–max | span | median | ATK min–max | DEF min–max |
|---|---:|---:|---|---:|---:|---|---|
| 1★ | 12 | **4** | 1277–1624 | 347 | 1537 | 576–944 | 540–893 |
| 2★ | 11 | **3** | 1395–1624 | 229 | 1624 | 628–1014 | 580–893 |
| 3★ | 34 | **11** | 1521–1968 | 447 | 1750 | 689–1058 | 653–1284 |
| 4★ | 5 (+`056` `???`) | 4 | 1923–2033 | 110 | 1955 | 755–1032 | 718–1070 |

Distribution confirmed exactly as §2 of the target document states: **1★ 12, 2★ 11,
3★ 34, 4★ 6** (63 including the placeholder). The load-bearing document's §2.1 table
says `4★ n = 5` while §2 says `4★ 6`; both are right (5 numeric, 6 labelled) but the
discrepancy should be labelled, not left to be re-derived.

Distinct HP values = **20 across 62 rows** — confirmed.

### 2.2 The banding is monotone **in the envelope only**, and is not near-disjoint

Envelope monotonicity (does both the min and the max rise with rarity?):

| field | envelope monotone? | containment failures |
|---|---|---|
| **HP** | **True** | **2★ range 1395–1624 is FULLY CONTAINED inside 1★ range 1277–1624** |
| ATK | **False** (4★ max 1032 < 3★ max 1058) | **4★ ATK range 755–1032 FULLY CONTAINED in 3★ 689–1058** |
| DEF | **False** | **2★ fully inside 1★**; **4★ fully inside 3★** |

So of the three core stats, **only HP has a monotone envelope at all**, and even HP
gives **zero separating power between 1★ and 2★** by range. The document's phrase
"slight overlap at the 1★/2★ and 3★/4★ seams" understates this: the 1★/2★ case is
*total containment*, and 1★ also overlaps 3★ over 1521–1624.

### 2.3 Every row whose HP falls outside its rarity's band, with the violation

Two symmetric tests. "Intrusion" = HP ≥ the minimum HP of the **next higher** rarity
(the row reaches into a higher band). "Downreach" = HP ≤ the maximum HP of the
**previous lower** rarity.

**Intrusion (HP reaches into the next higher rarity's territory):**

| id | ★ | HP | next-band floor | violation |
|---|---:|---:|---:|---:|
| `026`, `016`, `004` | 1★ | 1467 | 1395 | +72 |
| `011`, `017`, `018`, `019`, `006` | 1★ | 1537 | 1395 | +142 |
| **`009`** | **1★** | **1624** | 1395 | **+229** ← known pair |
| `022`, `030`, `013` | 2★ | 1584 | 1521 | +63 |
| `005`, `021`, `024`, `032`, `034`, `002` | 2★ | 1624 | 1521 | +103 (incl. `005`, known pair) |
| **`036`** | **3★** | **1923** | 1923 | **+0** ← at the seam, §5 |
| `062` | 3★ | 1968 | 1923 | +45 |

**8 of 12** 1★ rows and **9 of 11** 2★ rows intrude upward.

**Downreach (HP sits at or below a lower rarity's ceiling):** all **11** 2★ rows
(≤1★ max 1624; 6 at exactly 1624, 3 at 1584, 2 at 1395); **8** 3★ rows
(`043` 1606, `054`/`055` 1560, `059`/`039`/`031`/`033`/`001` 1521); **3** 4★ rows
(`052` 1955, `047`/`010` 1923).

### 2.4 Is that a systematic pattern or near-boundary noise? — it is systematic at the 1★/2★ seam

The task brief expects "a small number of near-boundary violations is expected and
fine; a systematic pattern is not." The 1★/2★ seam is **systematic**, and here is the
proof — the 1★ band contains only **four** distinct HP values:

```
1★  HP 1277  (007, 014, 020)
1★  HP 1467  (016, 004, 026)
1★  HP 1537  (011, 018, 006, 019, 017)     <- 11 of 12 rows
1★  HP 1624  (009)                        <- ONE row, alone, 87 above the rest
```

**`009` is the only 1★ row above HP 1537, and simultaneously the only 1★ row at
DEF 893 — the 1★ DEF maximum** (next highest 1★ DEF is 817). Meanwhile HP **1624** is
the **2★** band's ceiling and is held by **six** 2★ rows (`005`,`021`,`024`,`032`,
`034`,`002`). A lone 1★ row parked at the 2★ HP ceiling *and* at the 1★ DEF ceiling is
not boundary noise.

**Separation, quantified** (leave-one-out, so the row being scored is never its own
evidence):

| pair | AUC: P(higher-★ HP > lower-★ HP) | ties |
|---|---:|---:|
| 1★ vs 2★ | **0.796** | 4.5 % |
| 2★ vs 3★ | 0.816 | 0.0 % |
| 1★ vs 3★ | 0.919 | 0.0 % |
| 3★ vs 4★ | 0.971 | 1.2 % |
| 1★ vs 4★ / 2★ vs 4★ | 1.000 | 0.0 % |

HP→rarity leave-one-out accuracy **53/62 = 85.48 %** against a majority-class baseline
of **34/62 = 54.84 %** (always guess 3★). So HP carries real, substantial information
about grade — roughly a 31-point lift over the baseline — **but it is not a clean key**:
**10 of 62 rows (16.1 %)** carry an HP shared with a *different* rarity, and those
shared values are exactly the two seam values, **1624** (1★×1, 2★×6) and **1923**
(3★×1, 4★×2).

### 2.5 Sub-stat templates — the reuse is *within* rarity, which supports the banding

Grouping the nine sub-stats as a signature vector:

| ★ | distinct 9-substat templates | repeated templates |
|---|---:|---|
| 1★ | 8 over 12 rows | `026`/`004`, `011`/`018`, `014`/`020`, `017`/`019` |
| 2★ | 9 over 11 rows | `021`/`032`, `024`/`034` |
| 3★ | 31 over 34 rows | `049`/`050`/`035` (×3), `059`/`001` |
| 4★ | 5 over 5 rows | none |

Reuse is dense *inside* a rarity and essentially absent *across* rarities. That is the
better half of the "designed lookup table" signature — and it is stronger evidence for
the banding than the HP ranges are, because it is not a range statistic.

### 2.6 Duplicate-row census

Core triple (HP/ATK/DEF) duplicate groups: **12**. Full 13-field groups: **3**, all
same-rarity (`059`/`001`, `024`/`034`, `026`/`004`).

**Eleven of the twelve core-triple duplicates are same-rarity** (costume variants —
`024`/`034` Riko/Halloween Riko, `026`/`004` Tyltyl, `059`/`001` Lantern/Jack
O'Lantern, `007`/`014`, `019`/`006`, `022`/`030`, `032`/`002`, `037`/`040`,
`039`/`031`, `048`/`027`, `060`/`035`). **Exactly one is mixed-rarity: `005`/`009`.**

`005` vs `009`, field by field: **12 of 13 fields identical**, the sole exception being
`penetration` (**0** vs **1**). Identity metadata is *correct and different*
(`005` = 2★ Ice Defense; `009` = 1★ Lightning Defense), so this is not a wrong-hero row —
it is a stat row that is one field away from a byte copy.

### 2.7 Task 1 conclusion

The rarity column is internally consistent with the HP bands **except at the 1★/2★
seam**, where 8 of 12 1★ rows and 9 of 11 2★ rows intrude, and where the single
mixed-rarity duplicate pair sits. There is **no systematic pattern of a *mis-labelled*
rarity** — every intruder is a real value that a 2★/3★/4★ row also carries, which is
what overlap in a designed table looks like. The one thing that is *not* explainable as
overlap is `009`, and §2.4 shows it is the wrong kind of exception.

---

## 3. TASK 2 — cross-check against every other rarity source in the workspace

### 3.1 The sources, and what each actually is

| tag | source | domain / provenance | rows available |
|---|---|---|---:|
| **A** | archive TSV `rarity_on_draw` | `blustone.jp/hunter/…` JP portal, 2019 Wayback captures | 63 |
| **B** | `analysis/catalogue/cards/<id>.md` `**Rarity / grade:**` | **[COMMUNITY-SOURCED] `blustone.miraheze.org/wiki/…` Infobox `Rarity`** | **61** |
| **C** | `vsfan-wiki-2026-10-05.md` §1.5 hero-infobox `★` column | **`vsfan.net/wiki/…`** (NXDOMAIN now; Wayback 2017–2019; later mirrored to `vsfanwiki.miraheze.org`, also deleted) | **55** |
| **D** | `trace-rarity-vote-2026-10-05.md` §1.1, vsfan `List_of_Blustone_Items` trace table `Rarity` column | `vsfan.net`, different page | **27** |
| **E** | `uncovered-archive-roster-2019.tsv` `rarity` column | local crosswalk of the 51 uncovered ids | **1** overlapping |
| **F** | in-game ★ badge / rule evidence | `polluted-observations.md` (screenshots) | 3 ids |

Source inventory re-checked as a control: A 63 rows all-int; B 61; C 55
(dist 1★10 / 2★11 / 3★30 / 4★4, vs the note's stated 57-pages/55-distinct); D 27
(dist 1★11 / 2★8 / 3★8). All non-zero, all as documented.

### 3.2 Agreement, with the honest denominator

| comparison | comparable | agree | disagree | rate | not covered |
|---|---:|---:|---:|---:|---:|
| **A vs B** (catalogue, miraheze) | **61** | 61 | **0** | **100.00 %** | 2 |
| **A vs C** (vsfan infobox) | **55** | 54 | **1** | **98.18 %** | 8 |
| **A vs D** (vsfan trace table) | **27** | 27 | **0** | **100.00 %** | 36 |
| **A vs E** (uncovered roster) | **1** | 1 | 0 | 100.00 % | 50 |
| **A vs F** (in-game badges) | **3** | 3 | **0** | **100.00 %** | 60 |
| **B vs C** (the two wikis against each other) | **55** | 54 | **1** | **98.18 %** | — |
| **A,B,C,D all four present** | **27** | **26** | **1** | **96.30 %** | — |

**Honest denominator note.** The 61/61 and 27/27 figures are *not* 63/63. Two archive
rows have **no** catalogue rarity — `034` and `026`, whose catalogue files read
`** _(absent)_ stars** [UNKNOWN]` — and eight rows have no vsfan infobox
(`026`,`034`,`038`,`056`,`059`,`060`,`061`,`063`), 36 have no trace row, 50 have no
uncovered-roster row, 60 have no in-game badge. **The largest single cross-check is
61 rows, never 63.** Denominators must not be inflated by treating an absent value as
an agreement.

### 3.3 Every disagreement, named

**Exactly one, in 143 comparisons.**

| id | hero | archive | source C | source B | source D | source E/F |
|---|---|---:|---:|---:|---:|---|
| `018` | **Robin** | **1★** | **2★** | 1★ | 1★ | — |

This is **already adjudicated, and against the outlier**:
`vsfan-wiki-2026-10-05.md` §2.7 "Robin's rarity: the wiki infobox is the outlier,
three sources agree against it" — the wiki's *own* trace table says ★ (=1★ material),
the catalogue says 1★, the JP database says 1★. Conclusion there: "the Robin infobox ★★
is most likely a wiki error and the catalogue/JP value of 1★ is better supported."
**My audit reproduces that verdict independently: 1★.** The archive agrees with the
majority on the one contested hero.

Corroborating in-game (source F, non-portal): Bear `036` — the Caragublu Transcendence
screen "states identical hunters of **3★ or above** can be used as fodder", archive 3★,
catalogue 3★, vsfan ★★★. Therapy `050` — screenshot reads "a **three-star** Support /
Ice hunter", archive 3★. Dumble `048` — archive 3★, and the workspace already labels it
"3★ draw".

### 3.4 The independence caveat — this is the real weakness of the cross-check

Three *domains* is not three *independent lineages*, and the workspace already contains
the evidence: `vsfan-wiki-2026-10-05.md` item 6 states that **97 of 108** overlapping
sub-stat fields match the 2019 `blustone.jp` database exactly, and concludes "the wiki
table and the JP table are the **same schema and same underlying data**."

So:

- **A and C/D's stat tables demonstrably descend from the same source.**
- Whether **C's and B's `Rarity` fields** descend from `blustone.jp` is **not
  established anywhere in this workspace**. Nothing found either way.
- The archive's own harvester treated rarity as an independent crosswalk key:
  `archived-hunter-database-2019.md:51` — "crosswalk to 62 distinct catalog IDs by
  matching Japanese profile epithets against `CHAR_STR.json` titles, **then checking
  draw rarity, role, and element**"; 60 of 63 rows carry `identity_match` strings that
  name *draw rarity* explicitly. So the field was read off the page and used to
  *validate* an identity, not derived from the stats. That is a real (if modest)
  independence gain.

**Net:** the rarity column has strong *corroboration* and essentially no *proven
independence* from its only non-portal cross-check, which is 3 in-game badges. A
100 %-looking rate across three wikis is therefore **weaker evidence than the raw
percentage suggests**, and §5 leans on in-game structure rather than on this rate.

`char-str.tsv` was checked for a per-hero rarity column and **has none** — it stores
only `★1…★4 Trainer` and `★2/★3/★4 Transcendence Ticket` item names. That zero is real
(control E: 16×U+2605 present, so the glyphs *are* in the file), and it is itself the
first half of the answer to Task 3.

---

## 4. TASK 3 — is `rarity_on_draw` the same axis as the grade of an owned instance? (the important one)

**Answer: yes, it is the same axis — and that axis is MUTABLE. `rarity_on_draw` is the RECRUIT grade. It is not a hero-invariant property, and the stat row is indexed on (hero, grade, level), not on hero alone.**

### 4.1 What the column's own source says it is

`archived-hunter-database-2019.md:5`: the pages "give the hunter's rarity **when
drawn**". `base-stat-heading-client-attested-2026-10-06.md:167-169` already leaned on
this to correct a "Lv.30, 5★" slip to **3★**. The column is the **grade at the moment
of recruitment**, by the archive's own semantics.

### 4.2 The ★N axis *is* the owned-instance grade — [RECOVERED] from the client

`analysis/recovered-data/leveldb-tables/char-str.tsv`, shipped client strings:

```
901  ★1 Trainer  … A great trainer you can use instead of ★1 hunters when training or advancing.
902  ★2 Trainer  … instead of ★2 hunters when training or advancing.
903/904  ★3 / ★4 Trainer …
912/913/914  ★2 / ★3 / ★4 Transcendence Ticket
```

★N is the **grade axis the advancement and transcendence mechanics consume** — it names
which-star hunters substitute as training/advancement fodder. It is not a marketing
label bolted onto a card; it is a property of the instance.

### 4.3 That grade is mutable, and advancing it resets level — [COMMUNITY-SOURCED]

`polluted-observations.md:752-754`, transcribing the **`blustone.jp` rank-up guide**,
Wayback capture `20191113131941`:

> max **★5**; materials = **same count of same-★ partners** (★3→★4 needs three ★3s);
> **level resets to 1**, new skill learned, **★4+ unlocks equipment**

Corroborated in-workspace: `training-rankup-rules-2026-10-05.md` rows 3, 4, 10
(materials = current star count; "★1-drawn hunters raise far"; cap ★30 regardless of
grade; per-grade skill caps 10/20/30/40/50), and the Caragublu Dec-2018
**3★ Lv.30 MAX → 4★ Lv.1** screenshot pair.

Native side: `/gym/RankUp` → `ReqRankUpCB` → `SetCardPromotion`, with
`GetCardRankUpSrcCnt(currentrank)` and a server check that the target has reached max
level. `/reference/GetLevel.card` is keyed on **(rank, level)**.

### 4.4 Positive confirmation that grade really does move the stats — independent of the archive rows

The vsfan wiki carries three complete `Transcendence Level: 3` tables on a **different
domain**, with its own `Life/Attack/Defense` rows. Ratios against the archive's base
rows:

| hero | grade | archive base | vsfan T3 | ×HP | ×ATK | ×DEF |
|---|---:|---|---|---:|---:|---:|
| `024` Riko | **2★** | 1624/682/821 | 2069/868/1047 | 1.2740 | 1.2727 | 1.2753 |
| `023` Hermes | **3★** | 1750/937/653 | 2275/1218/848 | 1.3000 | 1.2999 | 1.2986 |
| `009` Captain | 1★ | 1624/**628**/893 | 2069/734/1142 | 1.2740 | 1.1688 | 1.2788 |

Two grades, two multipliers, **1.274 vs 1.300**, each internally consistent to
<0.25 % across all three stats. **The stat table's per-hero multiplier is a function of
grade.** (n=2 clean; Captain's ATK cell is the suspect of §2.6.)

### 4.5 What the archive does and does not contain

- **63 rows, 63 distinct `catalog_id`, zero `_1` rows.** Every id is base-form. The
  archive contains **no awakened rows at all**, so it cannot show a second grade for any
  hero.
- `uncovered-archive-roster-2019.tsv` treats `_1` as a **separate catalogue entity**:
  15 awakened rows, of which 11 carry `rarity = 5`, and 32 base rows all `4*` (those are
  the post-`098` heroes the archive never reached). So *awakening* is a distinct
  reference row, while *rank-up* is an in-place promotion of one instance. **Whether
  awakening and the ★5 rank-up ceiling are the same axis is not settled here** and I am
  not claiming it — `010_1` shows `Lv.30/30 Lv.MAX` at five stars, which a
  level-resetting promotion would not obviously produce.

### 4.6 The required restatement

`base-stat-heading-client-attested-2026-10-06.md` §2.1 argues:

> "This independently corroborates `level-factor-test-2026-10-05.md`'s arithmetic
> negative … and explains it: **the column is not indexed by level at all.**"

That clause is **wrong**, and §6 below shows why with the project's own numbers. The
defensible statement is:

> At a single common level, base HP is **monotone in recruit grade**, with heavy
> overlap and two seam values. The stat table is keyed on **(hero, grade, level)**; the
> 63 rows are one sample at **(grade-at-draw, one level)** — so no level ladder is
> visible *across rows*, which is what the arithmetic negative actually measured.

**Practical consequence for the coverage proposal.** The 62 rows are **62
(hero, grade-at-draw, Lv.1) tuples, not 62 hero-invariant base stats.** A hero that has
since been advanced to ★4 sits at ★4 Lv.1 with a *different* triple, and the archive
cannot supply it. Any coverage entry must be written as **"base at draw grade, Lv.1"**.
Writing "hero base stat" would silently assert the very invariance this audit shows does
not exist.

---

## 5. TASK 4 — the 4★ group (n = 5 numeric, 6 labelled) and `036` Bear

### 5.1 The group in full

| id | hero | HP | ATK | DEF | CP | role | element |
|---|---|---:|---:|---:|---:|---|---|
| `046` | Harley | 2033 | 755 | 1036 | 11534 | Defense | Ice |
| `063` | Erise | 2019 | 933 | 1070 | 12725 | Defense | Lightning |
| `052` | Windblade/Storm | 1955 | 992 | 835 | 11504 | Offense | Lightning |
| `047` | Lily & Lyla | **1923** | 996 | 755 | 10679 | Offense | Fire |
| `010` | Vincent | **1923** | 1032 | 718 | 11252 | Offense | Lightning |
| `056` | Genovia | `???` | `???` | `???` | `???` | Offense | Ice |

**Mutual consistency: good, and thin but coherent.**
- Monotone HP ladder 1923 → 1955 → 2019 → 2033 with no outlier.
- **5 distinct 9-substat templates over 5 rows — zero reuse.** The 4★ group is the most
  per-hero-tailored group in the corpus (compare 1★: 8 templates/12 rows, 3★:
  31/34). That is what a top-of-roster design looks like, and it is a mild *positive*
  signal that the group is real content rather than duplicated rows.
- Role split 3 Defense / 2 Offense; both elements spread; both catalogued 4★ by
  `blustone.miraheze.org` and 4★ by vsfan (`046` ★★★★, `047` ★★★★, `052` ★★★★).

**But the group is load-thin in three specific ways, and the document should say so:**
1. **n = 5** for the entire top of the range. §2.1's table gives it a band of 110 HP
   width from 5 points; a single bad row would move the floor or ceiling by ~20 %.
2. `063` Erise is corroborated by the **archive + catalogue only** (both 4★; the
   catalogue file exists and reads `**4 stars**`). It is **absent from vsfan C, vsfan D
   and the uncovered roster** (it appears in all three "not covered" lists in §3.2), so
   it rests on **two** sources, not four. `046`, `047` and `052` are triple-corroborated
   (archive + catalogue + vsfan infobox); `010` is quadruple (it also has no trace row
   but does appear in vsfan C). `063` should be flagged as the **least externally
   corroborated row in the 4★ group**, its HP/CP coherence being internal evidence only.
3. `056` Genovia is 4★ by **three** sources (archive + catalogue + roster) but carries
   **no numbers**, so the 4★ numeric group is 5, not 6.

### 5.2 `036` Bear — is it a second banding exception? **No, and the distinction matters**

`036` Bear: `rarity_on_draw = 3★`, **HP 1923**, corroborated **3★** by catalogue,
vsfan ★★★, vsfan trace (not listed), **and independently in-game** by the Caragublu
"identical hunters of 3★ or above can be used as fodder" rule.

HP 1923 is shared by exactly three rows: `047` 4★, `010` 4★, `036` **3★**.

**This is the seam, not an exception:**
- 1923 is *both* the 3★ row's value and the **exact minimum** of the 4★ band — violation
  amount **+0**.
- 3★ HP values ascending: 1521, 1560, 1606, 1678, 1710, 1742, 1750, 1790, 1821,
  **1923**, 1968. `036` is the **10th of 11** distinct 3★ HP values; `062` Juno (1968)
  is above it. So `036` is not even the 3★ maximum.
- 3★-vs-4★ AUC is **0.9706** with 1.2 % ties — the two bands are 97 % separable.
  A genuine mislabel would depress this; a value sitting exactly on a designed
  boundary is what a monotone designed table produces.

**So `036` is NOT a second exception and the rarity column is NOT impeached by it.**
But there is a real, smaller point the load-bearing document omits: `036` is the
**single row that makes the 3★ and 4★ HP bands share a value**, and it is the reason
the 3★/4★ overlap is 46 HP wide rather than 0. Under §2.4's framing it belongs with the
seam values 1624 and 1923, not with `009`.

---

## 6. Two collateral findings that bear directly on the load-bearing document

These were not asked for, but they change what the parent should do with §2.1 and §3,
so they are reported rather than buried.

### 6.1 The `051` Beckhen anchor resolves §3.1 and refutes the "not indexed by level" clause

`analysis/catalogue/stats/051.md` is the **only** independently verified gear-free base
row in the project: `051` Beckhen, **Lv.30, no equipment, 3 stars** (printed level,
3 stars visible in the badge, identity cross-validated 4 ways by exact string match;
every number read by eye *and* OCR).

| | archive `051` row | `051.md` Lv.30 gear-free |
|---|---:|---:|
| HP | 1678 | **2879** |
| ATK | 864 | **1471** |
| DEF | 660 | **1149** |
| speed / crit / critdmg / pen / block / DRblock / elemEnh / elemRes / regen | 8 / 33 / 200 / 0 / 14 / 42 / 5 / 5 / 42 | 8 / 33 / 200 / 0 / 14 / 42 / 5 / 5 / 42 |

**All nine sub-stats are byte-identical.** Ratios on the core triple:
**1.7157 / 1.7025 / 1.7409**, mean **1.71973**, spread 2.23 %.

Every competing explanation is closed:
- **gear** — the same panel's green gear deltas were HP+437, ATK+317, DEF+154,
  speed+1.72, crit+0.67, critdmg+10.86, block+4.69, DRblock+1.76, elemEnh+1.65,
  elemRes+3.13. **None** appear in the archive row. The portal transcribes the **white
  nude column**.
- **grade** — 3★ in both readings.
- **identity** — 4-way exact string match.
- ⇒ the only axis that moves HP/ATK/DEF while leaving nine sub-stats bit-identical is
  **level**.

And the arithmetic lands inside the project's own pre-existing expectation:

```
implied per-level compound if the archive row is Lv.1  = 1.71973^(1/29) = 1.018871   (1.887 %/level)
level-factor-test-2026-10-05.md:6,316 expected band     = 1.0185 – 1.0193          INSIDE
```

Consequences:
1. **§3.1's gap ("level is `not shown` on all 63 rows") is closed** — to **Lv.1**, by
   the project's own single clean anchor with grade held constant. This *removes* the
   stated reason the document declined to apply the coverage count.
2. **§2.1's "the column is not indexed by level at all" is refuted.** It is level-indexed;
   the 63 rows simply share one level, which is why no level ladder is visible across
   rows. That is the *correct* reading of the arithmetic negative, not the one written.
3. **§3.2's "single largest residual risk" (geared transcription) is answered for the
   reading path**: the portal copies the nude column, proven on the one hero where a
   nude column exists. Caveat: `051` is 3★, and **equipment only unlocks at ★4**, so
   this anchor cannot speak to the 4★ rows — see 6.2.
4. **Caveats that must travel with it.** n = 1. `level-factor-test-2026-10-05.md:424`
   records a **conflicting scalar** — Natalia's Lv.1→Lv.30 Strength `2480 → 3323`,
   ratio 1.339919, only **15.7 steps-equivalent** at g=1.0188, not 29. `level-factor-test`
   §1.6/§1.9 had already refused to adopt a factor, and this audit does not adopt one
   either: **no per-level multiplier is published, and none should be.**
   `051.md` itself: "Two Lv.30 observations is not a curve", and the FAQ figures are
   2018–2019 era, not the 2.8.0.1 balance.

### 6.2 The gear-contamination risk is **not uniform across rarity** — and it splits the corpus

The same `blustone.jp` rank-up guide says **"★4+ unlocks equipment"**. Therefore:

| rows | can legally carry equipment? | gear-contamination risk |
|---|---|---|
| 1★ + 2★ + 3★ = **57** | **No** — gear is locked | **structurally impossible** |
| 4★ = **5 numeric** (+`056`) | **Yes** | **live**, and unaddressed by any anchor |

`base-stat-heading-client-attested-2026-10-06.md` §3.2 treats gear state as one uniform
63-row residual risk. It is not. For **57 of 62** rows the risk is eliminated by a game
rule, not by an argument; for the **5** 4★ rows it is the only residual risk that the
`051` anchor cannot close. Since coverage is a *count*, the honest framing is: 57 rows
have gear-exclusion on a rule, 5 rows have it only on the "Base Stat" heading plus the
portal's demonstrated nude-column habit.

(A related but **separate** and still-open item: `polluted-observations.md:678-685`
records an unattributed snippet that **jewels** additionally require a 4★ hunter in the
equipment panel. That is community text, not visual evidence, and is not used here.)

---

## 7. Does the banding argument survive?

**Yes — weaker than written, but the core survives, and two of its problems are
actually in the *stat* column rather than the *rarity* column.**

**Survives:**
1. HP is monotone in grade in its envelope, and a leave-one-out HP→grade classifier
   reaches **85.5 %** against a **54.8 %** baseline. Real signal, not an artefact.
2. The stronger signature is not the ranges at all — it is that the nine-substat
   templates are reused **densely inside** a rarity (1★: 8/12, 3★: 31/34) and
   **essentially not across** rarities. That is a designed lookup table's fingerprint.
3. An **independent, positive** confirmation exists that grade moves stats: the vsfan
   `Transcendence Level: 3` multipliers are **×1.274 at 2★** and **×1.300 at 3★** — two
   grades, two multipliers, on a different domain from the archive's stat rows.
4. All **63** rarity labels agree with at least one external source, and the only
   contested hero (`018`) resolves **in the archive's favour**.

**Does not survive, and must be rewritten:**
1. **"Monotone and near-disjoint"** → true of HP's envelope only. **1★/2★ has zero
   range separation** (2★ ⊂ 1★). **ATK and DEF are not monotone at all**, and each 4★
   range is fully contained in the 3★ range. 16.1 % of rows carry a cross-rarity HP.
2. **"The column is not indexed by level at all"** → **refuted** (§6.1). Correct
   version in §4.6.
3. **"only 20 distinct HP values serve 62 rows ⇒ keyed on (hero, rarity)"** → the count
   is confirmed, but 1624 and 1923 are each shared *across* rarities, and the argument
   is better made from substat-template reuse than from HP ranges.
4. **§3.1's level gap** → closed to Lv.1 by the `051` anchor, n=1 (§6.1).
5. **§3.2's uniform gear risk** → split 57 rule-protected / 5 live (§6.2).

**The `005`/`009` pair re-read — this is the audit's most useful correction to the
parent's framing.** `captain-009-duplicate-row-2026-10-06.md` presents the pair as
breaking the banding, and attributes the defect to `009`'s **ATK**. The banding
evidence points somewhere sharper:

- `009` is the **only** 1★ row above HP 1537 (all other eleven are 1277/1467/1537) and
  the **only** 1★ row at DEF 893, the 1★ maximum. It sits at the **2★ band's HP
  ceiling** (1624, held by six 2★ rows) while simultaneously at the **1★ DEF ceiling**.
- `005`/`009` share **12 of 13 fields**, differing only in `penetration` (0 vs 1), and
  their role/element metadata is correctly *different* (2★ Ice vs 1★ Lightning) — so
  this is a stat-row copy, not a wrong-hero row.
- **The rarity column is the part that is unanimous.** `009 = 1★` is agreed by the
  archive, the catalogue, the vsfan infobox and the vsfan trace table; `005 = 2★` by
  all three wikis. A bad *rarity* label would require three wikis to be wrong
  simultaneously; a bad *stat row* requires one archive cell to be a near-copy. The
  second is enormously more parsimonious.

So: **`009`'s stat row is the defect; the rarity column is exonerated by the very
incident that was cited against it.** The banding argument gets *stronger*, not weaker,
once `009` is treated as a defective stat row rather than as evidence about grades —
because then **all 12 core-triple duplicate groups are same-rarity**, i.e. 100 % of the
designed-variant reuse is intra-rarity, with zero cross-rarity collisions.

**Recommended adjudication posture.** The rarity column is fit to carry the banding
argument. The banding argument is fit to support the coverage upgrade **only if** it is
restated per §4.6 — base stat at **(draw grade, Lv.1)** — and per §6.1/§6.2 — with the
57/5 gear split and the n=1 level anchor both stated on the face of the entry.
I make **no** edit to `coverage.md`; that call stays with the file that owns the
definition, exactly as `base-stat-heading-client-attested-2026-10-06.md` §5 framed it.

---

## 8. Reproduction, and output integrity

Scripts, all read-only, none writing outside `%TEMP%\opencode\`:

| script | what it produces |
|---|---|
| `rarity_positive_control.py` | §0 controls A–E, incl. the 4-id known-answer TSV test |
| `rarity_audit_main.py` | bands, intrusion/downreach tables, 4★ group, substat templates, duplicate census |
| `rarity_crosscheck2.py` | sources B/C/D/E agreement matrix, AUC, containment, LOO classifier |
| `rarity_task4.py` | 4★ group in full, `036` in context, T3 multipliers, element/identity sanity |
| `rarity_051_anchor.py` | the §6.1 `051` arithmetic |

Python 3.12.10, `PYTHONIOENCODING=utf-8`. One `UnicodeEncodeError` on console output of
Japanese text was hit and is a **console** artefact per `GUARD` Rule 2, **not** file
corruption — it was resolved by fixing stdout, and no file was round-tripped.

**This file's integrity, verified on disk (not from the console):** `U+FFFD == 0`,
`CRLF == 0`, `LF` line endings throughout, UTF-8.

**Unchanged by this audit:** `archived-hunter-database-2019.tsv`, `coverage.md`,
`README.md`, `polluted-observations.md` (read, **not** appended), `server-ts`, fixtures,
the APK, seeds, emulator, phone, Ghidra, the native library, and every coverage count.
