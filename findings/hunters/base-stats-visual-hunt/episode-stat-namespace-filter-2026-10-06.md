# Episode STAT namespace filter — the `EVCB*` category error, swept corpus-wide (2026-10-06)

**Purpose.** [`archetype-reconciliation-2026-10-05.md`](archetype-reconciliation-2026-10-05.md)
§8 caught **one** instance of a category error: the Episode `EVCB*` hero grouping in
`replica-shape-error-2026-10-05.md` was contaminated by 4 **monster** rows
(`EVCB0301_M057`, `res_id M057`, used as a hero Offense `ATK/DEF` of **22.500**).
This pass re-derives the whole partition from disk and sweeps **every** statistic in
`analysis/research/base-stats-visual-hunt/*.md` that is derived from
`EPISODE_STAT_ACTORS.json`, to find out how many further instances exist.

**Verdict: the `EVCB*` instance was the tip. There are five more, plus one false
"unaffected" claim left behind by the original fix.**

**Nothing was deleted.** Nine markdown files edited via the `edit` tool with dated
correction notes; every original value is preserved inline with `~~struck~~` plus a
replacement. `polluted-observations.md` was **not** appended and **not** edited.
No `server-ts`, fixture, seed, APK, emulator or phone action; no Ghidra; no server
restart. **Coverage effect: none** — heroes **1/113**, accessories **1/100**,
monsters **0/22**.

---

## 1. The safe filter rule (normative)

> **A row of `analysis/recovered-reference/EPISODE_STAT_ACTORS.json` is a HERO row if
> and only if `res_id` starts with `C` AND the row's `id`, looked up in the matching
> `EPISODE_COMBAT_<id>.json` record's `left`/`right` wave lists, has
> `"type": "hunter"`.**

The second clause is **not optional**, and the corpus omits it everywhere. Measured
partition of the 152-entry file (entry index **80** is a literal `{}`):

| filter | rows | distinct `ref_id` | distinct `res_id` |
|---|---:|---:|---:|
| all entries (identifiable) | 151 | 56 | 86 |
| `res_id` starts `M` — monsters | 34 | 4 | 22 |
| **`res_id` starts `C` — the corpus's "hero" set** | **117** | **55** | 64 |
| **`res_id` starts `C` AND `type == "hunter"` — SAFE** | **109** | **54** | 62 |
| `res_id` starts `C` AND `type == "monster"` | 8 | 6 | 6 |

Three facts that make the trap easy to fall into:

1. **`res_id` namespace alone admits 8 rows that are tuned and placed as enemies**:
   `CB0002_BOSS`, `CB0003_BOSS`, `CB0004_BOSS` (all `res_id C010`) and
   `CB1102_006`, `CB1102_008`, `CB1102_011`, `CB1102_018`, `CB1102_019`
   (`C006`, `C008`, `C011`, `C018`, `C019`) — the last five are the entire right
   side of `EPISODE_COMBAT_CB1102.json` at thumb `level 1 / rank 5 / hyper 2`.
2. **`ref_id` alone is worse.** 3 `M*` monster rows carry a 3-digit hero `ref_id`
   (`CB0001_M01` → `001`, `CB0001_BOSS` → `040`, `CB0002_M01` → `034`), so a
   `ref_id`-only filter silently inflates a hero statistic by 3. This is the sole
   reason one file reports "the 3 rows dropped".
3. **The id-prefix split is a red herring for monsters.** `EVCB*`/`CB*` partition
   actor ids, not `res_id`s. `EVCB0301_M057` is an `EVCB*` id with an `M*` `res_id`;
   `CB1102_018` is a `CB*` id with a `C*` `res_id`. **Never filter Episode STAT rows
   by id prefix alone.**

Distinct `res_id` (64) exceeds distinct `ref_id` (55) because 9 `ref_id`s carry two
art packs — costume/awakened variants: `008`→`C008`/`C008B`, `009`→`C009`/`C509`,
`010`→`C010`/`C510`, `028`, `036`, `049`, `051`→`C051`/`C051A`, `068`→`C068`/`C068A`,
`072`→`C072`/`C072A`. Any statistic that says "55 heroes" and any that says "64
art packs" are counting different things; say which.

---

## 2. Contaminated statistics found, and what replaces them

| # | file : line | wrong | correct | missing filter |
|---|---|---|---|---|
| 1 | `replica-shape-error-2026-10-05.md:286` | `EVCB*` family **`n = 41`** | **`n = 37` hero rows** | `EVCB*` id-prefix admitted 4 `M*` `res_id` rows |
| 2 | `replica-shape-error-2026-10-05.md:294` | Offense **`HP med 2700`**, **`ATK/HP med 0.565`**, **`ATK/DEF med 1.263`** with the note *"Median 1.263 unaffected"* | **`2400`**, **`0.536`**, **`1.250`** — the median **is** affected | same as #1; the 2026-10-05 fix corrected only the range and left 3 cells contaminated, and asserted a false invariance |
| 3 | `hero-stat-divergence-2026-10-05.md:131-138` | `CB*` family **`80 rows`**; distinct `hp` **47**, `atk` **49 (floor 100)**, `spd` **6 {4,…}**, `crt_chance` **15** | **`72 rows`**; **46**, **45 (floor 140)**, **5 {5,…}**, **12** | `res_id` namespace only; the 8 monster-typed `C*` rows are all in `CB*` |
| 3b | same table, `EVCB*` cell | distinct `hp` **13 (1700–3000)** | **13 (1700–5000)** — `EVCB0201_023` is 5000/1400/1300 | none — plain transcription error, `EVCB0201_023` overlooked |
| 4 | `episode-stat-adjudication-2026-10-05.md:25-32`, `:133`, `:267-269` | "**37 monster-like rows** = 34 `M*` + 3 monster-placed `C010`", and "fully inventoried" | **42 monster-like rows** = 34 `M*` + **8** monster-typed `C*`; hero rows **109** | `res_id` namespace only; the 5 `CB1102_*` rows were absent from the file entirely |
| 5 | `candidate-hero-bases-2026-10-05.md:68` | "The **3** rows dropped … (`CB0001_M01`, `CB0001_BOSS`, `CB0002_M01`)" | the namespace filter drops **34** rows over **22** tokens (`152 − 1 − 34 = 117`); only 3 of them carry a hero `ref_id` | `ref_id`-only reading; the "3 dropped" never reconciled with the 117 |
| 6 | `candidate-hero-bases-2026-10-05.md:69` | `CB*` **80 rows** | **`72` hunter rows** (80 = `C*`-namespace) | `res_id` namespace only |
| 7 | `candidate-hero-bases-2026-10-05.md:232-237` | §2.6.4 "**19** heroes … only 1 … **5 of 19**"; `018` cited via **`CB1102_018`** (`r` 12.61) | **18 heroes**, still **only 1** (`011`); **4 of 18** (`003`, `010`, `012`, `054`); `018`'s only *hunter* row is **`CB0701_018_1`** (`3100/1000/240`, `r` **4.167**) | the extra hero is `006`, whose sole Episode row is the **monster-typed** `CB1102_006`; and `CB1102_018` is itself monster-typed |
| 8 | `hero-identity-crosswalk-2026-10-05.md:417-422` | "the **103** Episode hero rows"; role **102/103** | the 103 pool = **100 `C*` rows + 3 `M*` rows with hero `ref_id`** ⇒ **100 rows, role 99/100**; strict pool **92 rows, role 91/92** | §1.6 never applied the `res_id` filter that §2.1 of the same file uses |
| 9 | `hero-identity-crosswalk-2026-10-05.md:488-495` | §2.1 ledger "117 rows / 55 heroes"; **31** multi-tuple / **24** single; level `L1×67, L10×11, L15×1, L20×10, L30×28` | **109 / 54**; **28** / **26**; `L1×59, L10×11, L15×1, L20×10, L30×28` | `res_id` namespace only |
| 10 | `SYNTHESIS-2026-10-05.md:352-354` | Episode table "**fully inventoried** … 37 monster-like rows" | **42**; the 5 `CB1102_*` rows omitted | as #4 |
| 11 | `monster-fullhp:80`, `m034-variance:8`, `m001-m100-insider:6` | one-line restatements of "37 monster-like rows = 34 `M*` + 3 `C010`" | annotated as an incomplete partition (**42**) | as #4 |
| 12 | `archetype-reconciliation-2026-10-05.md:313` | §9 corrections table asserts the Offense **"median preserved"** | **amended**: median is 1.250 hero-only vs 1.263 monster-mixed | the original fix's own false invariance claim |

### 2.1 Statistics checked and found CLEAN (no edit needed)

| statistic | why it survives |
|---|---|
| **`archetype-reconciliation` §8 `EVCB*` table** (Defense 8 / Support 12 / Offense 11 / Bomber 6; Offense `1.077–1.333`) | all 37 `EVCB*` `C*` rows are `hunter`-typed; namespace filter == safe filter |
| **`candidate-hero-bases` §2.5 per-role bands** (`A 17/13/20/12 · E 8/12/11/6`) | archive rows are unaffected; `E` column is `EVCB*` only, which is clean |
| **`archetype-reconciliation` §2, §3, §4, §5 archive bands** | computed from `archived-hunter-database-2019.tsv`, no Episode rows |
| **`identity-contradictions:457`** "`awk_step` on exactly 4 of 117 hero rows, all `C509`/`C510`" | identical under both filters (the 8 monster-typed rows carry no `awk_step`) |
| **`episode-res-crosswalk:56-58, 112`** "151 = 34 `M*` + 117 `C*` (64 tokens)"; "64/64 `C*` tokens match `<res_id>.jet`" | correctly namespace-scoped and explicitly labelled `C*`-shaped |
| **all `M*`-only monster findings** (22 distinct `res`, 6 multi-tuple identities, `M034` 160× spread, inert secondary fields, `2/22` catalog overlap) | draw only on `M*` rows; the 8 new rows are `C*` and change none of them |
| **`coverage.md`** | no Episode-derived numeric statistic; the `117`/`151`/`152` hits are URL substrings |

---

## 3. Questionable but NOT edited — reported, not guessed at

These are real inconsistencies, but the correct replacement could not be established
from local evidence, so per the strike-don't-delete rule they are flagged in place
rather than overwritten.

1. **`hero-identity-crosswalk:422` — `attr` "97 / 103", 6 named mismatches.** Not
   reproducible under any pool. It appears to compare `STAT.attr` against the
   archive TSV's `element_ja` via a Japanese-token translation; the archive tokens
   are **`冷気` / `火炎` / `電撃`**, *not* the `氷` / `火` / `雷` set, and the
   crosswalk's own [UNRESOLVED]-style element reading could not be replicated. Left
   verbatim. **Note:** the *role* cell in the same table was reproducible and was
   corrected; the element cell was not.
2. **`hero-identity-crosswalk:425` — "Episode `res_id` in the catalogue art list
   113 / 117; the 4 exceptions are `C509`/`C510`".** An independent token scan of
   `catalogue/INDEX.md` did not reproduce it (12 `C*` tokens unmatched, not 4). The
   original presumably used a stricter catalogue field than a regex over prose.
   Left verbatim.
3. **`candidate-hero-bases:235` — the original "5 of 19".** All four
   filter × `s`-band variants tried return **4**; the replaced figure is measured,
   but why the original said 5 is not established.
4. **`identity-contradictions:319` — "hero rows (`res_id` not `M*`) | 173 (168 after
   dropping the two monster rows that reuse a card `ref_id`)".** `173` is not
   reproducible: 240 non-empty combat actor rows resolve to exactly **168** `C*` and
   **72** `M*` (168 + 72 = 240). The parenthetical already carries the right number,
   so `173` reads as stale, and "two" should be **three** (`001`, `034`, `040`).
   Not edited because the cell's intent is ambiguous.
5. **`hero-stat-divergence` §P6 / `candidate-hero-bases` §2.6.5 — the `EVCB ÷ 1.36`
   scale hypothesis, "n = 25" / "n = 22" / "n = 23" paired heroes.** All of these draw
   on `EVCB*` rows plus the archive, so the namespace trap does not apply, and I did
   not attempt to re-derive the pairing rule (lowest-`id`-per-hero, 4 heroes with
   several rows). Flagged only because `candidate-hero-bases:539` documents the
   selection rule as an assumption rather than a measurement.
6. **`hero-identity-crosswalk:494-495` level distribution.** The published
   `L1 ×67, L10 ×11, L15 ×1, L20×10, L30×28` **is** reproducible on the 117-row
   pool using a *last-placement* thumb rule (first-placement gives
   `L1×66, L10×13`), so the original is internally consistent — but the choice of
   "last placement" over "first placement" is undocumented, and on the strict
   109-row pool both rules shift the `L1`/`L10` split. The corrected strict-pool
   value is recorded in the edit; the rule choice is left as found.

---

## 4. Live encoding hazard found alongside (NOT caused by this pass)

`polluted-observations.md` has **zero** Hangul syllables in the working tree, while
the version committed at `HEAD` contains **66** Hangul syllables + 2 CJK ideographs.
Tokens now absent from the file but present in `HEAD` include `블루스톤(근황)`,
`근황`, `기이한 노인 덤블`, `전투력`. This is precisely the destruction mode
[`GUARD-encoding-and-archive-traps.md`](GUARD-encoding-and-archive-traps.md) warns
about (a PowerShell `Get-Content`/`Set-Content` round-trip), and it matches the known
incident a previous agent suffered.

- **This pass did not cause it.** Byte-level snapshots taken before and after my edits
  are identical for that file (`sha256[:16] = 17c9c3feba8e70e1`, `fffd = 0`,
  `hangul = 0` at both points), and I neither appended to nor edited it.
- **It is not a safe `git checkout`.** `HEAD` is 297 lines / 38 343 chars; the working
  tree is 2 408 lines / 191 021 chars. Restoring `HEAD` would delete ~2 100 lines of
  later research. The correct remediation is a **surgical re-insert** of the ~68 lost
  glyphs, which is a separate careful task and **not** attempted here.
- **Every other file in the lane still carries its Hangul** (54 files, up to 3 675
  syllables in `help-2_8-sweep-2026-10-05.md`), so the damage is localised to this
  one file.

---

## 5. Method and encoding compliance

- All data reads/writes via Python with `encoding='utf-8'`; **no PowerShell
  `Get-Content`/`Set-Content`/`WriteAllLines` anywhere**. All nine markdown edits
  used the `edit` tool. No temp or scratch file was written inside the workspace;
  helper scripts live in `%LOCALAPPDATA%\Temp\opencode`.
- Verified after editing, across all 13 lane files touched or audited:
  **U+FFFD = 0** (and 0 across all 90 `.md` files in the directory),
  **CRLF count = 0** (LF-only preserved), and per-file Hangul/CJK/compatibility-kana
  counts **unchanged except where this pass deliberately added quoted Japanese
  tokens** (`守備手`, `冷気`, `火炎`, `電撃`) to `hero-identity-crosswalk-2026-10-05.md`
  (+12 CJK). A character-multiset diff confirms **zero pre-existing CJK/Hangul
  characters lost** in any file.
- **Self-correction recorded:** the first draft of the `episode-stat-adjudication`
  correction table contained `CB1102_*` HP/ATK/DEF values that I had inferred rather
  than read. They were wrong (`CB1102_006` is 3600/3200/240, not 7000/5000/250) and
  were replaced with the measured values before this report was written. Flagged
  because it is the same failure mode this whole pass is about: a plausible-looking
  number in a research table that no one re-derived from disk.
- Cross-check: the pre-existing scratch script
  `analysis/research/base-stats-visual-hunt/_ground_truth.py` (from the prior agent)
  independently reports the same partition (117 `C*`, 34 `M*`, **8 `C*` rows used as
  monster**, 109 safe, 62 distinct hero `res_id`), which corroborates this pass.
  Those `_gt*.py` scratch files were left in place, unmodified.