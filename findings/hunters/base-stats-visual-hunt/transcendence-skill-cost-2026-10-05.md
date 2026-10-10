# Transcendence + skill-level cost tables: two-source reconciliation (2026-10-05)

**Purpose.** Cross-check two independent cost-table sources for the same two
systems, cell by cell, and adjudicate three specific questions: (a) does the
English guide fill the Korean wiki's empty 2★ third cell, (b) does the guide's
per-band fragment sequence resolve the wiki's five-values-for-ten-bands
pairing problem, (c) does the fragment:crystal 10:1 ratio hold in both.

**Scope and disposition.** **Evidence reconciliation only. No server fixture,
APK, seed, state file or emulator action was taken.** `server-ts`, the APK and
all LevelDB seeds are untouched. This file changes no coverage count: heroes
1/113, accessories 1/100, monsters 0/22 — unchanged, because not one of these
numerals is a hero/monster/accessory base stat. They are economy/progression
context for rebalance estimates.

**Sources, with era tags carried into every claim below:**

| Tag | Source | Era |
|---|---|---|
| **[EN-2017]** | `share_en/197745` "Guide to Blustone", author `Alaiko`, post dated **2017.11.12**, body captured 2018-02-27, English. Single-author **player prose**, no screenshot behind it (all 11 images are unrecoverable — 10/10 HTTP 404, proven with a positive control). Full transcription: [`share-en-guide-2026-10-05.md`](share-en-guide-2026-10-05.md) §1.5 | **PRE-2019-09-05** — squarely inside the older balance era per [`stat-version-context.md`](stat-version-context.md) |
| **[NAMU]** | Namu wiki 헌터/블루스톤 page, raw-HTML cell extraction, mirrors fetched 2026-10-05, Korean. Page last-modified 2026-08-13, content spans 2017–2021 | **ERA-UNRESOLVED** — undated wiki text; explicitly must not be normalized against the 2019-09-05 rebalance. Full transcription: [`namu-tables-2026-10-05.md`](namu-tables-2026-10-05.md) §2–3 |
| **[HELP-1.4.4.1]** | **Original in-game help text**, `UI_CSV` named `HELP_DATA`, extracted from the VSFan 1.4.4.1 APK: `analysis/VSFan/Extracted Assets (2026)/1441 (APK)/UI_CSV/3d98d128.json` (187,121 B, 73 `CONTENTS*` records). Read fresh in this pass | **1.4.4.1 baseline**; calendar date unstated. Strictly **earlier than the shipped 2.8.0.1 client** |
| **[REPLICA]** | This workspace's own local fixtures — read-only, for conflict flagging only | current local fixture, documented non-original |

**Headline, five findings:**

1. **The two sources are the same table.** 9 identical Transcendence cells and
   **30/30 identical skill material cells** across two languages, two sites and
   two era tags. That is 39 exact coincidences, far beyond chance or
   cross-contamination between an English forum post and a Korean wiki. Both
   almost certainly transcribe a **common original** — most plausibly the
   game's own in-game help. Neither has been shown to do so, and **neither is
   native-recovered**.
2. **(a) Yes, [EN-2017] fills the 2★ T3 cell with 60/600 — but it is
   single-sourced.** Namu's own table header declares three steps
   (`자기극복 순서 | 1 | 2 | 3`), which favours transcription omission over a
   real two-step row. 60 also preserves the column's monotonicity. No arithmetic
   rule predicts it, so it cannot be independently derived.
3. **(b) Yes, and uniquely.** [EN-2017]'s sequence `1,1,2,2,3,3,4,4,5,5`
   collapses to exactly `1,2,3,4,5`, which determines Namu's five values as
   covering **consecutive band-pairs**. That is the only simple mapping
   consistent with the guide, and it **eliminates the ambiguity**: skill-level
   fragments are a decadal step function, fully agreed by both sources for
   levels 1–49.
4. **(c) Yes, 10:1 holds in both — but only inside the Transcendence table.**
   9/9 [EN-2017] cells and 11/11 [NAMU] cells. The skill table has no crystal
   column at all, so **10:1 is table-scoped, not a global invariant**.
5. **The one real numeric conflict is a single skill level.** Bands 5 and 6
   disagree about whether **level 25** costs `4 bronze + 1 silver` or
   `5 bronze + 2 silver`. Every other level agrees. Fragments at level 25 agree
   (3) because both bands 5 and 6 carry 3.

**Bonus adjudication from an artifact already in the workspace.** The original
in-game help **[HELP-1.4.4.1]** was checked for the gate prose and settles the
apparent [EN-2017] vs [NAMU] conflict: they are not in conflict. It contains
**no cost numerals at all**, so it cannot adjudicate any number here.

---

# 1. PURE — verbatim readings, side by side, cell by cell

Nothing in §1 is inferred, reconciled or normalised. Band/level labels,
rowspans, empty cells and units are reproduced as each source stores them.

## 1.1 Transcendence / 자기극복 (self-overcoming) — both tables side by side

**[NAMU]** cell unit is `결정체/조각` = **crystal/fragment**, one cell per step,
three declared step columns, four grade rows. **[EN-2017]** publishes four
separate columns per cell plus a grade-row label reading "Natural N-star".

| Grade row | Step | [NAMU] crystal/fragment | [EN-2017] crystals | [EN-2017] rupees | [EN-2017] fragments | [EN-2017] duplicate hunters |
|---|---|---|---|---|---|---|
| 1★ | T1 | `5/50` | 5 | 5,000 | 50 | 1 |
| 1★ | T2 | `15/150` | 15 | 15,000 | 150 | 2 |
| 1★ | T3 | `45/450` | 45 | 45,000 | 450 | 3 |
| 2★ | T1 | `7/70` | 7 | 7,000 | 70 | 1 |
| 2★ | T2 | `25/250` | 25 | 25,000 | 250 | 2 |
| **2★** | **T3** | **(empty cell)** | **60** | **60,000** | **600** | **3** |
| 3★ | T1 | `9/90` | 9 | 9,000 | 90 | 1 |
| 3★ | T2 | `30/300` | 30 | 30,000 | 300 | 2 |
| 3★ | T3 | `80/800` | 80 | 80,000 | 800 | 3 |
| 4★ | T1 | `12/120` | — not published | — | — | — |
| 4★ | T2 | `40/400` | — not published | — | — | — |
| 4★ | T3 | `110/1100` | — not published | — | — | — |
| 5★ | — | **no row exists** | — | — | — | — |

[NAMU] structural facts as stored: header is `자기극복 순서 | 1 | 2 | 3`;
"2★ has only 2 steps in the source (third cell empty), all others 3"; "5★ row
does not exist in the source"; "fragment is exactly 10× crystal in every cell".

## 1.2 Skill-level training cost — both tables side by side

Band labels are **each source's own**, reproduced unaltered.

| Band # | [EN-2017] label | [NAMU] label | [EN-2017] rupees | [EN-2017] fragments | [EN-2017] bronze/silver/gold | [NAMU] low/mid/high | [NAMU] fragments |
|---|---|---|---|---|---|---|---|
| 1 | `Level 1 - 4` | `1~4` | 100 | 1 | 0/0/0 | `0/0/0` | one of `1 2 3 4 5` |
| 2 | `Level 5 - 9` | `5~9` | 200 | 1 | 1/0/0 | `1/0/0` | one of `1 2 3 4 5` |
| 3 | `Level 10 - 14` | `10~14` | 300 | 2 | 2/0/0 | `2/0/0` | one of `1 2 3 4 5` |
| 4 | `Level 15 - 19` | `15~19` | 400 | 2 | 3/0/0 | `3/0/0` | one of `1 2 3 4 5` |
| 5 | `Level 20 - 25` | `20~24` | 500 | 3 | 4/1/0 | `4/1/0` | one of `1 2 3 4 5` |
| 6 | `Level 26 - 29` | `25~29` | 600 | 3 | 5/2/0 | `5/2/0` | one of `1 2 3 4 5` |
| 7 | `Level 30 - 34` | `30~34` | 700 | 4 | 0/3/1 | `0/3/1` | one of `1 2 3 4 5` |
| 8 | `Level 35 - 39` | `35~39` | 800 | 4 | 0/4/2 | `0/4/2` | one of `1 2 3 4 5` |
| 9 | `Level 40 - 44` | `40~44` | 900 | 5 | 0/5/3 | `0/5/3` | one of `1 2 3 4 5` |
| 10 | `Level 45 - 49` | `45~50` | 1000 | 5 | 0/6/4 | `0/6/4` | one of `1 2 3 4 5` |

Band 10 is the last row in both. **[EN-2017] publishes no row covering skill
level 50.** [NAMU] covers it (`45~50`).

[NAMU] `종합 메트론 조각` row, verbatim and unsplit: **`1 | 2 | 3 | 4 | 5`** —
five values for ten band columns. Material grid, verbatim: attacker
`0/0/0 | 1/0/0 | 2/0/0 | 3/0/0 | 4/1/0 | 5/2/0 | 0/3/1 | 0/4/2 | 0/5/3 |
0/6/4`, with defender/bomber/helper rows carrying **label cells only** — the
numeric grid is rowspanned from the attacker row, so quantities are shared
across roles and only the material names differ:
공격수 `금속 조각` (녹슨/예리한/신기한), 수비수 `등껍질`
(부서진/멀정한/무적의), 폭격수 `화염석` (차가운/뜨거운/이글거리는), 도우미 `약초`
(시든/싱싱한/열매 맺은).

[NAMU] prose, verbatim: metron-based; "from skill level 5 a role material is
also required, +1 per 5 levels; hunter grade raises skill max level by 10 per
grade"; "3★+ unlock; same-grade hunter + metron per step".

## 1.3 Gate prose, both sources verbatim

| | [EN-2017] | [NAMU] |
|---|---|---|
| Step-1 floor | "Both the base hunter and the duplicate hunter must be at least 3 stars for the first transcendence." | "3★+ unlock" |
| Step-2/3 floor | "For the second and third transcendence, your base hunter needs to be at least 4-stars and 5-stars respectively." | not published |
| Fodder rule | "The duplicate hunters however only need to be 3-stars." | "same-grade hunter + metron per step" (`동등급 헌터`) |
| Skill slots | "There are 5 different skills for each hunter, and the next skill gets unlocked as you upgrade the hunter. This means at 1-star, only the first skill is available whereas all the skills are available for 5-stars hunters." | "hunter grade raises skill max level by 10 per grade" |
| Skill semantics | "The first skill is your active skill. […] The second skill is triggered and always occurs after the first skill is activated. The third skill is passive and it always applies. The fourth skill has a chance to trigger once the first skill activates. […] The fifth skill is passive and it always applies." | not published |

## 1.4 [HELP-1.4.4.1] — original in-game help, the four relevant articles

Read from `3d98d128.json`, English fields, verbatim. This is **original
first-party text**, a stronger evidence class than either prose source.

- **`CONTENTS4_3` "Transcendence"** — "Do you want to grow stronger? How about
  making a hunter stronger by matching it with the same hunter? You can
  trascened ★3 hunters or above by using the **same hunter**. Also, the hunter
  you are using as fodder needs to also be **★3 or above**. Don't forget that
  the hunter you used for transcendence will be **gone**." *(sic — "trascened")*
- **`CONTENTS4_4` "Skill Training"** — "Did you know hunters have basic skills
  and additional skills? You can use additional skills from ★4 and above and
  these are activated **by chance**. Train the skills your hunters use! …
  1st Skill — Using the 1st skill can increase damage to your opponent.
  2nd Skill — Using the 2nd skill can increase additional effect that happens
  when using the skill. 3rd Skill — Using the 3rd skill you can permanently
  increase the hunter's basic ability that is important to your hunter's role.
  4th Skill — Using the 4th skill you can increase the additional effect that
  occurs by chance. 5th Skill — Using the 5th skill you can increase each
  hunter's unique effect regularly."
- **`CONTENTS4_2` "Advancing"** — "…For advancement you need a hunter with the
  **same grade** and the higher the grade the m[ore]…"
- **`CONTENTS6_1` "What is an Abyss?"** — "The Abyss is a place where you can
  collect **Metron Crystals and skill materials** that make your hunters
  stronger. Different abysses are set to open on different days. At first, you
  can excavate 1 time on a set day, but you can do a **reset up to 3 times**
  depending on your Veteran rank."

**Existence test for cost numerals — negative, and tested rather than assumed.**
All 73 records' English fields were scanned for `Bronze`, `Gold tier`,
`tier material`, `45,000`, `5,000`, `7,000`, `9,000`, `60,000`, `Level 1`,
`1~4`, `25~29`, `45~50`, `Metron Fragment`, `800`, `450`, `1100`.
**Zero hits for every cost pattern.** `Silver` occurs once, in
`CONTENTS10_7` "Check & Sell Fish", about a fish crown. The original help
describes the **systems** and the **gates** but publishes **no cost table**.
*(Method note: the file is malformed JSON — one surplus `}` before the final
`]`. Records were therefore split on the `"id": "CONTENTS…"` key rather than
strict-parsed. The source file was not modified.)*

## 1.5 [REPLICA] — local fixtures touched by this comparison

- `server-ts/src/skill-training.ts:20` — `gold: 100 * (index + 1)` per
  **skill level index**; all four `source_N_qty` are **0**.
- `server-ts/src/skill-training.ts:20` — `rank: Math.ceil((index + 1) / 10)`,
  i.e. caps 10/20/30/40/50 per grade.
- `server-ts/src/openapi.ts` — "Gold100*destinationLevel and zero materials are
  fixtures"; "Skill caps10/20/30/40/50 are community-derived inference".

---

# 2. UNPUR[E] — reconciliation, adjudication and conflict register

Every item in §2 is inference, cross-source reasoning or conflict. Each carries
both sources and era tags. Nothing here is a verbatim reading.

## 2.1 The 39-cell coincidence, and what it does and does not license

Nine Transcendence cells ([NAMU] 1★×3, 2★×2, 3★×3) and thirty skill material
cells are **identical across both sources**, in different languages, on
different sites, under different era tags. Consequences I accept:

- **Licensed:** the two sources are not independent inventions, and neither is
  a transcription error of the other. Treating them as two votes for "some
  original said this" is reasonable.
- **Licensed:** a shared common ancestor is the parsimonious explanation —
  most plausibly the game's own help/UI text, since [HELP-1.4.4.1] already
  proves first-party prose about these exact systems shipped in the client.
- **NOT licensed:** any claim that these are *original game balance* for
  2.8.0.1. Both sources are community prose; [NAMU]'s era is unresolved and
  [EN-2017] is PRE-rebalance. A common ancestor could itself be a 2017-era
  help page that later changed.
- **NOT licensed:** "verified". The project's honesty rules (§15 of
  `AGENTS.md`) require this stay community-reported. Promoting these numerals
  to "recovered" would be a category error.

## 2.2 Answer (a) — does [EN-2017] fill the Namu 2★ T3 empty cell?

**It supplies a value; it does not corroborate one.** The cell becomes
**60 crystals / 600 fragments / 60,000 rupees / 3 duplicates** — and every one
of those four numbers is **single-sourced** to [EN-2017]. Confidence tiers:

| Claim | Status | Why |
|---|---|---|
| 2★ has a third step in the game | **supported** | Namu's own header declares three step columns; a two-step row inside a three-step table is a hole, not a rule. A mid-grade hole at 2★ while 1★/3★/4★ all get three has no structural justification. |
| That step costs 60/600 | **single-sourced, plausible** | Nothing contradicts it: it preserves T3 column monotonicity (45 < 60 < 80) and its own row monotonicity. |
| 60 is derivable | **refuted** | No arithmetic rule generates it. See §2.3. |
| Namu's empty cell is a transcription omission | **inference, not proven** | Header evidence favours it; the wiki's other known defect (rank 551–720 breaking a descending run, preserved as `255`) shows the same table has at least one author typo. It could be a second one. |

**Interpolation is not corroboration.** Linear interpolation of the T3 column
across grades 1★/2★/3★/4★ = 45/?/80/110 would put 2★ near 62–68. 60 is
inside that neighbourhood, so the fill is *consistent* — but consistency is not
evidence, and I am explicitly declining to present 60 as confirmed.

## 2.3 Correction: there is no geometric rule to lean on

[EN-2017]'s own §2.1 calls its Transcendence table a "clean geometric
progression per grade". Checked, that is **exact only for the 1★ row**:

| Row | Values | T2/T1 | T3/T2 |
|---|---|---|---|
| 1★ | 5, 15, 45 | ×3.00 | ×3.00 — exact geometric |
| 2★ | 7, 25, 60 | ×3.57 | ×2.40 |
| 3★ | 9, 30, 80 | ×3.33 | ×2.67 |
| 4★ ([NAMU] only) | 12, 40, 110 | ×3.33 | ×2.75 |

Across grades at fixed step there is no rule either: T1 = 5/7/9 (+2, +2), T2 =
15/25/30 (+10, +5), T3 = 45/60/80 (+15, +20). **Consequence:** the "geometric
progression" framing must not be used to argue the 2★ T3 cell *should* be 75 or
90, and must not be used to argue 60 is right. It supports nothing about that
cell. The corrected claim is narrower: *the 1★ row is exactly geometric and the
other rows are not.*

## 2.4 Answer (b) — does the guide's fragment sequence resolve Namu's pairing?

**Yes, and it resolves it uniquely.** [NAMU] supplies five values for ten band
columns; [EN-2017] supplies ten per-band values. The mapping is forced:

| Namu value | covers bands | [EN-2017] fragment in those bands | match |
|---|---|---|---|
| `1` | 1–2 | 1, 1 | ✔ |
| `2` | 3–4 | 2, 2 | ✔ |
| `3` | 5–6 | 3, 3 | ✔ |
| `4` | 7–8 | 4, 4 | ✔ |
| `5` | 9–10 | 5, 5 | ✔ |

The alternative candidate mappings are **eliminated**: assigning one value per
*odd* band with carry-forward is the same assignment, and any offset or
last-five mapping contradicts [EN-2017]. So **each Namu value spans exactly two
consecutive bands.**

**The level-level consequence is stronger than the band-level one.** Reading
through both sources' own band labels, the fragment cost is a **decadal step
function**, and because bands 5 and 6 *both* carry 3, the one level where the
two sources disagree about band membership (level 25) does **not** create
fragment ambiguity:

> **skill level 1–9 → 1 fragment · 10–19 → 2 · 20–29 → 3 · 30–39 → 4 ·
> 40–49 → 5** — agreed by both sources. Level 50 → 5 by [NAMU] alone
> ([EN-2017] publishes no row for it).

**Why [NAMU]'s row is structurally shorter.** The fragment row's banding is
**10 levels** while the material row's is **5 levels**. That is why a 10-column
table carries 5 fragment values: the quantity simply changes half as often.
This makes the missing cells a coherent merged-cell artefact rather than
sloppiness, and it predicts [NAMU]'s `45~50` top band (5 fragments) over
[EN-2017]'s `45~49`.

**Named "pairing" is now obsolete.** `namu-tables-2026-10-05.md` §3 and
`polluted-observations.md`'s Namu section both record "band pairing is
unresolved (recorded literally, do not split)". **That is now resolved** by an
independent dated source, and the "do not split" instruction is superseded for
the fragment row only. The literal transcription stays valid as a reading of
what the wiki stores.

## 2.5 Answer (c) — does fragment:crystal = 10:1 hold in both?

**Yes, in the Transcendence table, in both sources, without exception.**

- [EN-2017]: 9/9 cells — 5/50, 15/150, 45/450, 7/70, 25/250, 60/600, 9/90,
  30/300, 80/800. All exactly ×10.
- [NAMU]: 11/11 cells — the same nine plus 12/120, 40/400, 110/1100. All
  exactly ×10. [NAMU] additionally asserts the rule in its own header prose
  ("fragment is exactly 10× crystal in every cell"), so the rule is stated and
  observed within one source.

**Two limits that must travel with the finding:**

1. **Table-scoped, not global.** The skill table has **no crystal column at
   all**. Its fragments are absolute (1–5), not 10× anything. Do not generalise
   10:1 to Metron spending anywhere.
2. **Redundant, not corroborative.** Because fragment = 10 × crystal in *both*
   sources, the two columns are one measurement, not two. The fragment column
   adds zero independent information about the crystal column. Combined with
   §2.6, the whole 9-cell table reduces to **two** free numbers per cell
   (crystals, duplicates).

## 2.6 Derived columns — a downgrade, and a caution about apparent richness

Three of the four [EN-2017] columns are exact functions of another column:

| Column | Rule | Cells obeying | Free information |
|---|---|---|---|
| Rupees (Transcendence) | **= 1000 × crystals** | 9/9 | only the 1000:1 exchange rate |
| Fragments (Transcendence) | **= 10 × crystals** | 9/9 | nothing (see §2.5) |
| Rupees (skill table) | **= 100 × band index** | 10/10 | only the 100-rupee step |
| Duplicates | **= step number** (1/2/3) | 9/9 | nothing |
| Skill fragments | **= decadal step**, see §2.4 | 10/10 | 5 free values |

The genuinely non-derivable content in [EN-2017] is therefore: **the crystal
counts, the duplicate counts, and the material ladder** — not 36 numbers. Any
future fixture built from this source should be described as reproducing those
three structures, not as adopting 36 independent values.

## 2.7 The 30/30 material-grid agreement — the strongest result here

Every one of [NAMU]'s thirty low/mid/high cells equals the corresponding
[EN-2017] bronze/silver/gold triple, at identical band indices:

```
band        1      2      3      4      5      6      7      8      9     10
[EN-2017] 0/0/0  1/0/0  2/0/0  3/0/0  4/1/0  5/2/0  0/3/1  0/4/2  0/5/3  0/6/4
[NAMU]    0/0/0  1/0/0  2/0/0  3/0/0  4/1/0  5/2/0  0/3/1  0/4/2  0/5/3  0/6/4
```

This also **independently validates [NAMU]'s rowspan reading**: the shared-grid
interpretation that `namu-tables-2026-10-05.md` §3 flagged as a structural
inference is confirmed, cell for cell, by a source that had no reason to know
about rowspans.

**The naming is still an inference.** [NAMU] names the three qualities
per role (녹슨/예리한/신기한 for attacker metal, 부서진/멀정한/무적의 for
defender shell, …) — different words per role, so a quality ladder.
[EN-2017] calls the same quantities "Bronze tier / Silver tier / Gold tier
materials". The **numbers** are certain to be the same items; the **identity**
"bronze ≡ 녹슨" is my mapping, not a source statement.

## 2.8 The one genuine numeric conflict: skill level 25

| | [EN-2017] | [NAMU] |
|---|---|---|
| band 5 label | `Level 20 - 25` | `20~24` |
| band 6 label | `Level 26 - 29` | `25~29` |
| band 5 materials | 4 bronze, 1 silver, 0 gold | `4/1/0` |
| band 6 materials | 5 bronze, 2 silver, 0 gold | `5/2/0` |
| **level 25 therefore costs** | **4 bronze + 1 silver** | **5 bronze + 2 silver** |

- **Scope of the conflict: exactly one skill level.** Bands 1, 2, 3, 4, 7, 8, 9
  carry **identical labels in both sources**, so levels 1–24 and 26–49 have
  agreed material costs.
- **Fragments at level 25 are unaffected** (3 either way) — see §2.4.
- **Rupees at level 25 are single-sourced**: 500 by [EN-2017]; if [NAMU]'s
  banding is right it would be band 6's 600, but [NAMU] publishes no rupees.
- **Lean toward [NAMU], low confidence.** Three arguments: (i) every other band
  in both sources spans exactly 5 levels, and [EN-2017]'s 6+4 split is the only
  anomaly in either table; (ii) [EN-2017]'s **own prose** says materials drop
  only at levels ending in 1/6, 2/7, 3/8, 4/9 and **not** at levels ending in
  5 or 0 — so a well-formed band contains exactly one such level, whereas
  `20-25` contains **two** (20 and 25) and `26-29` contains **none**; (iii)
  [EN-2017] band 10 (`45-49`) leaves skill level 50 uncovered, while [NAMU]
  covers it, and 50 is the expected cap under both sources' grade/level rules.
- **Not resolved.** Era cannot arbitrate: [EN-2017] is PRE-2019-09-05,
  [NAMU] is ERA-UNRESOLVED. Two community transcriptions of the same table
  disagree about one cell edge, and no artifact in hand settles it. Recorded as
  **OPEN-1**.

## 2.9 Conflict register

| ID | Item | [EN-2017] | [NAMU] | Status |
|---|---|---|---|---|
| C1 | Skill level 25 material cost | 4 bronze + 1 silver | 5 bronze + 2 silver | **OPEN-1**, one level, mild lean [NAMU] |
| C2 | Band 10 top level | `45-49` (50 uncovered) | `45-50` | lean [NAMU]; level 50 fragment = 5 single-sourced |
| C3 | Fodder grade rule | "duplicates only need to be 3-stars" | "same-grade hunter" | **RESOLVED — false conflict**, see §2.10 |
| C4 | Base-hunter step gate | T1 ≥3★, T2 ≥4★, T3 ≥5★ | not published | **OPEN-2**, [EN-2017]-only; §2.11 |
| C5 | Skill max level vs grade | 5 slots at 5★, one per grade | +10 max level per grade | complementary, no conflict |
| C6 | Skill unlock granularity | one slot per grade | "additional skills from ★4 and above" ([HELP-1.4.4.1]) | not reconcilable into one rule; all three permit ≥2 skills at 5★ |
| C7 | Grade-row key meaning | "Natural 1/2/3-star" | `1★/2★/3★/4★` | numbers agreed (9 cells); **label single-sourced** |
| C8 | Role material ≥5★ | not published | **no 5★ row** | gap in both |
| C9 | Fragment-row structure | ten per-band values | five values, ten bands | **RESOLVED**, §2.4 |

## 2.10 C3 resolved — the original help text shows both clauses are one rule

On first read, [EN-2017] and [NAMU] appear to contradict each other on fodder:
[EN-2017] says duplicates need only be 3★, [NAMU] says the fodder is the
**same grade**. [HELP-1.4.4.1] `CONTENTS4_3` says **both, in one paragraph**:

> "You can trascened ★3 hunters or above by using the **same hunter**. Also,
> the hunter you are using as **fodder** needs to also be **★3 or above**."

So the original rule is *same-hunter* **and** *★3 floor*. They are
complementary clauses, not competing claims, and the apparent conflict was an
artefact of comparing two partial paraphrases of a two-clause rule. This is the
one place in this pass where an artifact already in the workspace settles a
cross-source disagreement, and it does so in favour of **both**.

It also confirms a third thing neither prose source states: the transcended
hunter's material is **consumed** ("will be gone"), matching the duplicate-fodder
model both tables assume.

## 2.11 What the original help does *not* settle

- **No cost numerals anywhere** (§1.4). C1 and C2 remain open; [HELP-1.4.4.1]
  cannot adjudicate a single number in these tables.
- **C4 is not corroborated.** `CONTENTS4_3` states a ★3 floor and stops. It
  describes no second or third step and no 4★/5★ requirement. [EN-2017]'s
  "second and third transcendence need 4-stars / 5-stars" is therefore
  **uncorroborated by the 1.4.4.1 help**, which is *older* than that guide.
  Plausible explanations — a later gate added after 1.4.4.1, a UI-side gate not
  in help text, or a guide error — are all open. Do not implement the 4★/5★
  step gate on [EN-2017]'s authority alone.
- ~~**Bounded extension, not done:** the shipped 2.8.0.1 `UI_CSV.jet` has more
  help sections than 1.4.4.1 — native string tables show `CONTENTS12_*`,
  `CONTENTS13_*`, `CONTENTS14_*`, `CONTENTS15_*` (e.g. `CONTENTS15_1`) that do
  not exist in the 1.4.4.1 corpus I swept. Those are unextracted and **were not
  checked for cost numerals in this pass**. That is the single cheapest next
  step for C1/C2/C4.**~~
  **CLOSED 2026-10-05 — swept, and negative.**
  [`help-2_8-sweep-2026-10-05.md`](help-2_8-sweep-2026-10-05.md) extracted all 22
  of those records (verbatim, every locale) and re-ran this file's §1.4
  cost-pattern test over the whole shipped corpus: **all 95** `CONTENTS` records,
  **20 patterns, 0 hits** (its §2.1 Q1, §2.8 C1/C2/C4 "swept and empty", §2.9).
  The 1.4.4.1 finding is **confirmed and extended, not corrected**: the shipped
  game's help describes systems and gates and never a cost table, in either
  version. **C1, C2 and C4 therefore stay OPEN and can no longer be closed by
  help sweeping** — the remaining route is the original reference rows only.

## 2.12 Impact on this project's local fixtures — flagged, NOT acted on

Recorded because a future decision needs it; **no fixture, test or server value
was changed by this pass**, and these are community figures, not recovered ones.

- **Skill price shape disagrees with [EN-2017].** [REPLICA] prices
  `100 × destinationLevel`, i.e. L1=100, L2=200, L3=300, L4=400, L5=500 …
  L50=5000. [EN-2017] prices by **band**: L1–4=100, L5–9=200, …, L45–49=1000.
  The two agree at **L1 only**; [EN-2017]'s top band is ~5× cheaper than
  [REPLICA]'s equivalent level. A native-observable difference exists here, but
  **the native price getter is recovered as `roleVector[destinationLevel-1]`**
  (per `openapi.ts`), i.e. indexed by level, which *favours* the per-level
  shape. Native evidence and community prose disagree; **this is not a bug fix
  and not a fixture change** — it is an unresolved question that needs the
  original skill reference rows, not a community table.
- **Zero materials disagrees with both sources.** [REPLICA] charges no skill
  materials; both [EN-2017] and [NAMU] say role materials are required from
  level 5. This is the **least ambiguous discrepancy in the whole comparison**:
  two independent sources agree, and the empty `source_N_qty` slots are a
  documented fixture. Still a fixture decision, not taken here.
- **Caps 10/20/30/40/50 gain a second, independent community corroboration.**
  `openapi.ts` currently marks these "community-derived inference" from a
  single 10-per-grade rule. [NAMU] states "+10 per grade" directly, and
  [EN-2017] independently implies a 5★ ceiling of 50 via its band-10 row.
  Combined with [HELP-1.4.4.1] `CONTENTS4_4`, the grade→cap ladder is now
  supported by two prose sources plus first-party text on slot semantics. This
  **raises confidence in an existing fixture; it changes nothing.**
- **Skill slot semantics are corroborated three ways.** [EN-2017]'s five-skill
  descriptions map one-to-one onto [HELP-1.4.4.1]'s (active damage / secondary
  effect / permanent base-ability passive / chance-based additional effect /
  regular unique effect). Same five-slot model, independent phrasings. Useful
  when the replica's inert `effects[]` fixtures are eventually revisited.
- **Abyss cross-check.** [EN-2017]'s "as your veteran level goes up, you are able
  to reset more times" is corroborated by [HELP-1.4.4.1] `CONTENTS6_1`
  ("reset up to 3 times depending on your Veteran rank"), and `CONTENTS6_1`
  also confirms "Metron Crystals **and** skill materials" are the two Abyss
  currencies these tables spend — i.e. **the fragment/crystal economy and the
  skill-material ladder are the same system**, which is why the two tables
  reconcile so cleanly against each other.

## 2.13 Corrections to the two source files (proposed, not yet applied)

1. `namu-tables-2026-10-05.md` §3 and `polluted-observations.md`'s Namu section:
   the metron-fragment row's "band pairing is unresolved" is **superseded** —
   resolved by [EN-2017] §2.4 of this file. Keep the literal transcription.
2. `share-en-guide-2026-10-05.md` §2.1: "form a clean geometric progression per
   grade" is **overstated** — exact for 1★ only (§2.3).
3. `namu-tables-2026-10-05.md` §2: the 2★ row should be annotated as
   **header-declared three steps with one empty cell**, so the omission reads
   as a source hole rather than a game rule.
4. Neither file records that the **original in-game help** exists locally and
   adjudicates the fodder-gate clause while containing **no cost numerals**.
   That belongs in both.

## 2.14 Limits — what this pass does not establish

- **Nothing is native-recovered.** Both tables remain community prose.
- **Era is unresolved for one of the two sources**, so no conflict here can be
  attributed to the 2019-09-05 rebalance versus an authoring error.
- **Zero coverage credit.** These are economy numerals. Heroes 1/113,
  accessories 1/100, monsters 0/22 unchanged.
- **No screenshot underlies any number.** [EN-2017]'s 11 images are a proven
  archival negative; [NAMU] is a wiki table. Both are text.
- **The C1 level-25 conflict stays open** and one more community transcription
  would probably not settle it. ~~§2.11's `CONTENTS12_*`–`CONTENTS15_*` sweep or
  a native price-row recovery is what would.~~ **[stale item closed 2026-10-05:
  that sweep is DONE and negative — `help-2_8-sweep-2026-10-05.md` §2.1 Q1, 95
  records / 20 patterns / 0 hits — so a native price-row recovery is now the
  only surviving route for C1/C2/C4.]**
- **No server, fixture, APK, seed, state or emulator action was taken.**

---

## 3. Files touched

- **New:** this file.
- **Appended:** `polluted-observations.md` — impure cross-check pointer
  (economy numerals, zero base-stat credit, conflicts left open).
- **Untouched:** `coverage.md`, `README.md`, `namu-tables-2026-10-05.md`,
  `share-en-guide-2026-10-05.md`, all TSVs, `server-ts`, the APK, all seeds.