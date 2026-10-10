# Episode `res` → identity crosswalk, all 22 tokens (2026-10-05)

**Purpose.** Close out the open question left by
[`m034-variance-2026-10-05.md`](m034-variance-2026-10-05.md) §2 (identity
caveat) and §2.4 item 5: *can an Episode `res` token be resolved to a monster
identity at all?* That file established the negative for `M034` only and
explicitly refused to generalise. This file tests **all 22** distinct `M*` `res`
tokens in the Episode STAT table, uniformly, and records a per-token resolution
verdict.

**Headline result.** **No.** `res` is an **opaque per-appearance script token**.
Of 22 tokens:

- **2** (`M001`, `M100`) have a local art pack **and** a catalogue row;
- **20** have neither;
- **0** of 22 resolve to a monster identity by any binding other than token
  coincidence;
- **0** of the 22 appear as a literal anywhere in `native-all-strings.tsv`;
- the `ref_id` field, the only other identifier on these rows, is a
  **hunter-card** namespace and resolves to a **card** in **120 / 120** cases.

**Coverage claim: none. Monster strict coverage remains 0/22** (unchanged; see
[`coverage.md`](coverage.md)). Nothing in this file is a base stat, and no row
here is tied to an observed HP bar, nameplate, or native Episode render
(AGENTS.md §91/§97, §96–§98 — Episode combat playback is still unverified).
**No server, APK, client, emulator, account or tutorial state was touched.**

> **Revision note.** This file was re-derived from disk and every numeric claim
> re-verified on 2026-10-05. Four claims in an earlier draft of this same file
> were wrong and are corrected here, with the superseded values listed in §3.1b
> so a reader who already read the earlier text can find them: the `C*` pack
> count, the multi-row-token census, the per-token thumb-context maximum, and
> the "tokens sharing one context" figure. All four were **conservative-direction
> or neutral** errors; none touched the headline verdict, the 2/22 vs 64/64
> asymmetry, or any tuple.

---

## 1. PURE — resolution status and placement context (no HP/ATK/DEF numerals)

Pure = identity resolution and display/placement context only. **No HP, ATK or
DEF numeral appears anywhere in §1.** All tuples are quarantined in §2.

### 1.1 Sources re-derived from disk (2026-10-05)

| Source | Fact used here |
|---|---|
| `analysis/recovered-reference/EPISODE_STAT_ACTORS.json` | SHA256 `f3b8cb90372c89490467e75ed0564bfc3f8a4d094370264caa2c821b0eb13b56`, 269 423 bytes, top-level **list** of **152** entries of which **151** are identifiable actor rows (entry index **80** is a literal `{}`) |
| `analysis/recovered-reference/EPISODE_COMBAT_*.json` | **61** combat records (47 `CB*` + 14 `EVCB*`); the 62nd prefix match is `EPISODE_COMBAT_STAT.manifest.json` |
| `analysis/extracted/assets/*.jet` | local art inventory — **774** packs total: **570** `C*`-prefixed (of which **113** are bare `C###` and **457** are suffixed forms such as `C001_Q`, `C036B`, `C051A`), **22** bare `M###` (`M001`–`M021` + `M100`), and 19 further `M`-initialed non-numeric packs (`MAIN_*`, `MAP_ZONE_1`, `MGM_FISH`, `MIRAGE`, `MISSION2`, `MOTION`, `MP4_*`) |
| `analysis/catalogue/monsters/*.md` | **22** rows, exactly `M001`–`M021` + `M100` |
| `analysis/catalogue/cards/*.md` | **121** rows |
| `analysis/native-all-strings.tsv` | 12 568 812 bytes, native literal vocabulary |
| `analysis/recovered-reference/EPISODE_S01.json` | season graph — **object of 7 keys** (`type, id, title, desc, res1, res2, childs`); contains **zero** `M\d{3}` tokens and **zero** `.jet` mentions |

Row census of the STAT table: **151** identifiable rows = **34** `M*`-token rows
(22 distinct tokens) + **117** `C*`-shaped rows (64 distinct tokens). **No row
lacks `res_id`** (0 of 151).

Placement census of the `M*` namespace: **72** placements, all of them
`side: right` (**72/72**), all `type: "monster"` (**72/72**), all with skill-slot
flags `0,0,0,0,0` (**72/72**), spread over **30** distinct thumb contexts and
**17** distinct combat records (`CB0001`, `CB0102`, `CB0201`, `CB0202`,
`CB0301`, `CB0501`, `CB0602`, `CB0702`, `CB1002`, `CB1201`, `CB1301`, `CB1401`,
`CB1501`, `EVCB0101`, `EVCB0102`, `EVCB0301`, `EVCB0303`). **The left/player side
never hosts an `M*` token** in local Episode data.

### 1.2 The master crosswalk — all 22 `res` tokens

`art` = does `analysis/extracted/assets/<token>.jet` exist. `cat/mon` = does
`analysis/catalogue/monsters/<token>.md` exist. `ref_id` = the only other
identifier carried by these rows, with what it resolves to. **Verdict** is the
identity answer.

| # | `res` token | STAT rows (actor ids) | rows | placements | host records | art | cat/mon | `ref_id` present → resolves to | **VERDICT** |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `M001` | `CB0001_M01` | 1 | 4 | `CB0001` | **yes** | **yes** | `001` → **card 001** | token + art + catalogue row exist; **no monster identity** (catalogue row is itself an admitted negative — §1.6) |
| 2 | `M022` | `CB0102_M1` | 1 | 2 | `CB0102` | no | no | — | **UNRESOLVED** |
| 3 | `M023` | `CB0201_M1`, `CB0301_M1` | 2 | 6 | `CB0201`, `CB0301` | no | no | — | **UNRESOLVED** |
| 4 | `M024` | `CB0602_M1` | 1 | 4 | `CB0602` | no | no | — | **UNRESOLVED** |
| 5 | `M034` | `CB0002_M01` (orphan), `CB1002_M3`, `CB1301_M3`, `CB1501_M1` | 4 | 5 | `CB1002`, `CB1301`, `CB1501`, `EVCB0301` | no | no | `034` → **card 034** (only on the orphan) | **UNRESOLVED** — and doubly so on the one `ref_id` row (§1.4) |
| 6 | `M035` | `CB1002_M1`, `CB1301_M1`, `CB1501_M2`, `EVCB0102_M1` | 4 | 9 | `CB1002`, `CB1301`, `CB1501`, `EVCB0102` | no | no | — | **UNRESOLVED** |
| 7 | `M036` | `CB1002_M2`, `CB1301_M2`, `EVCB0102_M2` | 3 | 9 | `CB1002`, `CB1301`, `EVCB0102`, `EVCB0301` | no | no | — | **UNRESOLVED** |
| 8 | `M040` | `CB0001_BOSS`, `CB1201_M2` | 2 | 2 | `CB0001`, `CB1201` | no | no | `040` → **card 040** (only on the tutorial boss) | **UNRESOLVED** — spans a tutorial boss and a rank-5 mob (§1.7) |
| 9 | `M041` | `CB1201_M1` | 1 | 4 | `CB1201`, `CB1401` | no | no | — | **UNRESOLVED** |
| 10 | `M042` | `CB1201_M3` | 1 | 3 | `CB1201`, `CB1401` | no | no | — | **UNRESOLVED** |
| 11 | `M044` | `EVCB0301_M044` | 1 | 2 | `EVCB0303` | no | no | — | **UNRESOLVED**; actor-id prefix lies about its record (§1.5) |
| 12 | `M046` | `CB0501_M1` | 1 | 1 | `CB0501` | no | no | — | **UNRESOLVED** |
| 13 | `M048` | `CB0501_M3` | 1 | 1 | `CB0501` | no | no | — | **UNRESOLVED** |
| 14 | `M049` | `CB0202_M2` | 1 | 1 | `CB0202` | no | no | — | **UNRESOLVED** |
| 15 | `M050` | `CB0202_M1` | 1 | 1 | `CB0202` | no | no | — | **UNRESOLVED** |
| 16 | `M051` | `CB0202_M3` | 1 | 1 | `CB0202` | no | no | — | **UNRESOLVED** |
| 17 | `M052` | `CB0501_M2` | 1 | 3 | `CB0501`, `EVCB0101` | no | no | — | **UNRESOLVED** |
| 18 | `M054` | `CB0501_M4` | 1 | 3 | `CB0501`, `EVCB0101` | no | no | — | **UNRESOLVED** |
| 19 | `M057` | `EVCB0301_M057` | 1 | 2 | `EVCB0303` | no | no | — | **UNRESOLVED**; actor-id prefix lies (§1.5) |
| 20 | `M058` | `CB0702_M1` | 1 | 4 | `CB0702` | no | no | — | **UNRESOLVED** |
| 21 | `M062` | `CB0202_BOSS`, `CB0501_BOSS` | 2 | 3 | `CB0202`, `CB0501`, `EVCB0101` | no | no | — | **UNRESOLVED** — the only token whose two rows disagree on `role` (§1.7) |
| 22 | `M100` | `CB1201_BOSS`, `CB1401_BOSS` | 2 | 2 | `CB1201`, `CB1401` | **yes** | **yes** | — | token + art + catalogue row exist; **no monster identity** (catalogue row is itself an admitted negative — §1.6) |

**Tally: 2 with art+catalogue, 20 with neither, 22 with no identity binding, 0
resolved.** Placement total across the table: **72** (sum of the column; equals
the independent whole-namespace census in §1.1).

### 1.3 The measured convention test — the C namespace *does* follow the filename rule, the M namespace does not

This is the finding that turns "opaque token" from an assertion into a
measurement. The STAT table carries **two disjoint token namespaces**, and only
one of them obeys `res_id` → `<res_id>.jet`:

| Namespace | rows | distinct tokens | tokens with a matching `<res_id>.jet` | rate |
|---|---|---|---|---|
| `C*` (`C001`, `C036B`, `C051A`, `C510`, …) | 117 | **64** | **64** | **64 / 64 = 100%** |
| `M*` (`M001` … `M100`) | 34 | **22** | **2** (`M001`, `M100`) | **2 / 22 = 9%** |

So the `<res>.jet` naming rule is real and is used by the game data — for the
`C*` namespace, which is the **hunter-card art family** (570 `C*` packs locally,
113 bare `C###` plus 457 suffixed variants such as `C001_Q` / `C001_EFT` /
`C001_SND` / `C001A`). It simply does not carry over to the `M*` namespace, where
20 of 22 tokens name nothing on this disk.

Additional hardness check, in case the failure were a near-miss typo: **no local
`.jet` stem even *contains* any of the 22 `M*` tokens as a substring.** The 20
unresolved tokens are not off-by-one spellings of packs that exist.

And a third independent negative: **none of the 22 tokens appears as a literal
in `analysis/native-all-strings.tsv`.** That table contains exactly three
`M\d{3}`-shaped literals in 12 568 812 bytes — `M263`, `M701`, `M705` — and none
of them is an Episode `res` token. Nor does `EPISODE_S01.json` mention any `M\d{3}`
token or any `.jet` filename. **There is no local binding table of any kind.**

> **Verdict.** The `M*` `res` token is an **opaque, data-only script token**. It
> is a grouping label inside `EPISODE_STAT_ACTORS.json`, not a resolvable monster
> identity. Any future join requires a **recovered binding table** (a recovered
> monster reference table, or a native `res`→art resolution path observed at
> runtime) — never filename similarity.

### 1.4 `ref_id` is a hunter-card namespace — it cannot bind an `M*` token

`ref_id` is the only other identifier on these rows, so it is the only candidate
alternative to `res`. It is disqualified by census:

| Census | Value |
|---|---|
| identifiable STAT rows carrying `ref_id` | **120** |
| …whose value resolves to a row in `analysis/catalogue/cards/` | **120 / 120 (100%)** |
| …whose value resolves to a row in `analysis/catalogue/monsters/` | **0** |
| …whose value resolves to neither | **0** |
| distinct `ref_id` values in use | **55** |
| `M*`-namespace rows carrying `ref_id` | **3 of 34** |

The three `M*` rows that carry it (slot numbers below are 0-based):

| Actor row | `res` | `ref_id` | resolves to | placement |
|---|---|---|---|---|
| `CB0001_M01` | `M001` | `001` | **hunter card 001** (Lantern, Fire/Bomber, 3★) | `CB0001` right w0 slots 0–3 of 5 |
| `CB0001_BOSS` | `M040` | `040` | **hunter card 040** (Bibi "Wolf Child", Lightning/Offense, 3★) | `CB0001` right w0 slot 4 of 5 |
| `CB0002_M01` | `M034` | `034` | **hunter card 034** ("Halloween Witch"; element/role **absent** in that catalogue entry) | **ORPHAN — zero placements** |

So the only `M*` rows with an extra identifier point at the **card** namespace,
never the monster one. `M034`'s orphan is the worst case in the table: its
`ref_id` names a hunter, its `res_id` names nothing. **Record both tokens; claim
neither.** (`M040` is the mirror-image case — a tutorial boss whose `ref_id`
names card 040 while its `res_id` names an unresolvable token.)

### 1.5 Actor-id naming lies about provenance — two more cross-record reuse instances

`res` does not leak into actor ids except in two rows, and in both the id
**prefix is false about the defining record**:

| Actor id | `res` | Placed in | Prefix implies | Never placed in |
|---|---|---|---|---|
| `EVCB0301_M044` | `M044` | `EVCB0303` right w0 slots 0, 1 of 5 | `EVCB0301` | `EVCB0301` |
| `EVCB0301_M057` | `M057` | `EVCB0303` right w0 slots 2, 3 of 5 | `EVCB0301` | `EVCB0301` |

Verified directly: enumerating `EVCB0301`'s own slots finds **no** slot holding
either id. These are the **fifth and sixth** cross-record actor-reuse instances
in the local Episode set, after the four recorded in
[`m034-variance-2026-10-05.md`](m034-variance-2026-10-05.md) §1.5. They are also
the only two rows whose actor id embeds the `res` token verbatim rather than
using the `_M1`/`_M2`/`_BOSS` ordinal convention.

`EVCB0303` (`EV03_E03_TITLE`, `power` 40000, `game_res_id` 99) is the mixed wave,
verified slot by slot: right w0 = 2×`EVCB0301_M044` (slots 0–1, thumb L1/r5/h0/attr1)
+ 2×`EVCB0301_M057` (slots 2–3, thumb L1/r5/h0/attr3) + hunter
`EVCB0301_C058B` (slot 4, thumb L1/r5/h0/attr3, skill flags `1,1,1,1,1`); left w0 =
3 `{}` placeholders (slots 0–2) + hunters `EVCB0301_C068A` (slot 3, attr2) and
`EVCB0301_C085` (slot 4, attr3), both skill flags `1,1,1,1,1`.

### 1.6 The two "resolving" tokens resolve to a *negative-result* catalogue row

Do not read `art: yes / cat: yes` for `M001` and `M100` as an identity. Both
catalogue rows are explicitly documented gaps:

- `analysis/catalogue/monsters/M001.md` — header `# M001 — [UNKNOWN] enemy
  monster`; "**Identity: [UNKNOWN].** No display name exists in any recovered
  source"; "**Base stats (hp / atk / def): [UNKNOWN].**"; "Not in
  `all-tables.json` (13 tables, 0 rows match `M\d{3}`)"; art `M001.jet`,
  **170 026** bytes on disk, texture/animation only. The `M001` = penguin
  observation is a single **by-eye** campaign capture (r016), not a data source.
- `analysis/catalogue/monsters/M100.md` — same structure; `M100.jet`,
  **584 684** bytes on disk.

Both file sizes re-measured on disk this session and matching.

The 22-row catalogue is documented in `analysis/catalogue/INDEX.md` §4.2 as a
negative result: there is **no recovered monster reference table** anywhere in
the project. `M001`/`M100` therefore resolve to *a texture pack and a placeholder
document* — which is exactly why monster coverage is 0/22.

**Do not import a false friend here.** Each catalogue row asserts
`res_prefix` = the monster id, tagged `[INFERRED from the …]`. That is the
**server** `/reference/GetMonster` `res_prefix` field, and AGENTS.md §16.2 row 4
already records `res_prefix` as an **environment id**, not an asset prefix — so
that inference is doubly unsafe. It is **not** evidence about the Episode STAT
`res_id`, which is a different field in a different table.

### 1.7 Two further identity-unbinding facts (identifier-level, no numerals)

- **`M040` spans two incompatible roles in the fiction.** It is the
  `CB0001` tutorial boss (STAT rank 1, thumb L1/r1/h0/attr2, one placement) *and*
  the `CB1201_M2` mid-rank mob (STAT rank 5, thumb L10/r5/h2/attr2). One token,
  two narrative roles, a rank-1-to-rank-5 jump. A token that spans both a
  tutorial boss and a chapter-12 mob cannot be an entity key.
- **`M062` is the only token whose two rows disagree on `role`** — `role` 1
  (`CB0202_BOSS`, STAT rank 3) versus `role` 2 (`CB0501_BOSS`, STAT rank 4).
  Both carry `attr` 1.
  - Row-count census, corrected: **7 tokens have more than one row**
    (`M023`×2, `M034`×4, `M035`×4, `M036`×3, `M040`×2, `M062`×2, `M100`×2) and
    **15 tokens have exactly one row**. Among the 7 multi-row tokens the rows
    agree on `role` for **6** of 7 (`M062` is the exception), and agree on
    `attr` for **7** of 7. They disagree on `rank` for **5** of 7 — `M034` 1/5,
    `M035` 4/5, `M036` 4/5, `M040` 1/5, `M062` 3/4 — while `M023` (both rank 2)
    and `M100` (both rank 5) agree.
- **Every `M*` placement has zero skill-slot flags** (72/72) and **every** `M*`
  STAT row ships `"skill": []`. No `M*` row scripts an encounter skill. (Contrast:
  `C*`-namespace hunter rows such as `EVCB0201_042` do carry full skill bodies.)
  The emptiness is the record.

### 1.8 Orphan and thumbnail census

- `CB0002_M01` (`res` `M034`) is the **only zero-placement row among all 151
  identifiable STAT rows** — a whole-table orphan, not merely the `M034` orphan.
  Independently corroborated by a byte-level literal grep: the ASCII bytes
  `CB0002_M01` occur in exactly **one** file under `analysis/recovered-reference/`,
  `EPISODE_STAT_ACTORS.json`, and in **zero** combat files. The `CB0002` fight it
  nominally belongs to fields only enemy-Vincent `CB0002_BOSS` + hunter
  `CB0002_C009`.
- The `M*` namespace spans **30 distinct thumb contexts** (level/rank/hyper/attr)
  across 72 placements, over displayed levels **1, 5, 10, 15, 20, 30** — from
  `(1,1,0,2)` through `(1,3,0,2)`, `(1,3,0,3)`, `(1,4,0,1)`, `(1,4,0,3)`,
  `(1,5,0,1)`, `(1,5,0,2)`, `(1,5,0,3)` up to `(30,2,0,1)` and `(30,4,0,2)`.
- **Thumb context is independent of `res`, but only mildly:** the maximum
  distinct thumb contexts for a single token is **3** (`M034`, `M035`, `M036`
  each reach 3; every other token reaches 2 or 1). Conversely the busiest single
  context is shared by only **2** tokens — `(20,3,0,3)` by `M048`/`M054`,
  `(1,4,0,1)` by `M035`/`M062`, `(10,5,2,2)` by `M040`/`M100`, `(20,3,0,2)` by
  `M046`/`M052`, `(1,1,0,2)` by `M001`/`M040`. So `res` is **not** a function of
  the thumb either, but the decoupling is much weaker than an earlier draft of
  this file claimed; see §3.1b.
- Because Episode combat has never been played or rendered on device
  (AGENTS.md §91/§97, §96–§98), **no row here is tied to an observed bar,
  nameplate or native receipt**.

---

## 2. UNPURE — scripted tuples, rebalance material only (NOT coverage)

**Impurity warning, read before the tables.** Every numeral in §2 is a
**scripted per-appearance tuning** read out of the Episode-only STAT table. It is
**not** a nude/base stat and **not** a monster reference value:

- One token spans **HP 100 → 16000 (160×)** (§2.2.1).
- Identical thumb contexts carry different tunings (§2.2.2, and
  [`m034-variance-2026-10-05.md`](m034-variance-2026-10-05.md) §1.3
  ladder-breaker).
- No row is tied to an observed full-HP bar or to native rendering.
- Identity is unbound for **20 of 22** tokens (§1).

Preserve these **only** for encounter-rebalance / difficulty-scaling estimates.
They contribute **0/22** monster coverage and **must never be quoted as base
stats**. Same-numbering with a hunter card (`M034`↔card `034`) is a **namespace
coincidence, not a binding** — §3.4 lists the trap explicitly.

**Field layout.** `rank` and every stat value are **strings** inside the nested
`stat` object; `attr` / `role` / `cool_time` are **numbers** on the actor row;
`ref_id` is optional. `stat` keys present on `M*` rows: `atk`, `attr_enhance`,
`attr_resist`, `block_chance`, `block_dec_dmg`, `crt_chance`, `crt_dmg`, `def`,
`hp`, `hp_regen`, `penetration`, `rank`, `spd`.

### 2.1 All 34 `M*` STAT rows (rebalance-only; supersedes no earlier table)

`hp` / `atk` / `def` / `spd` / `crt_chance` / `crt_dmg` / `penetration` /
`attr_enhance` / `block_chance` / `block_dec_dmg` / `attr_resist` / `hp_regen` are
transcribed as shipped.

| Actor | `res` | rank | hp | atk | def | spd | crt_chance | crt_dmg | pen | attr_enh | block_chance | block_dec | attr_resist | hp_regen | attr | role | cool_time | `ref_id` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `CB0001_M01` | M001 | `1` | `150` | `130` | `100` | `0.00` | `25` | `175` | `0` | `0` | `0` | `0` | `0` | `0` | 2 | 1 | 99000 | `001` |
| `CB0102_M1` | M022 | `1` | `450` | `430` | `180` | `0` | `20.00` | `180` | `0.00` | `0` | `10.00` | `10` | `0` | `5` | 2 | 1 | 5000 | — |
| `CB0201_M1` | M023 | `2` | `700` | `400` | `130` | `0` | `20.00` | `200` | `0.00` | `0` | `20.00` | `20` | `0` | `8` | 1 | 1 | 5000 | — |
| `CB0301_M1` | M023 | `2` | `700` | `650` | `160` | `0` | `20.00` | `200` | `0.00` | `0` | `20.00` | `20` | `0` | `10` | 1 | 1 | 5000 | — |
| `CB0602_M1` | M024 | `4` | `2500` | `1800` | `200` | `0` | `30.00` | `200` | `0.00` | `0` | `30.00` | `30` | `0` | `20` | 3 | 1 | 5000 | — |
| `CB0002_M01` **(ORPHAN)** | M034 | `1` | `100` | `100` | `100` | `0.00` | `25` | `175` | `0` | `0` | `0` | `0` | `0` | `0` | 2 | 1 | 99000 | `034` |
| `CB1002_M3` | M034 | `5` | `13000` | `5500` | `280` | `0` | `40.00` | `250` | `0.00` | `0` | `40.00` | `40` | `0` | `100` | 2 | 1 | 10000 | — |
| `CB1301_M3` | M034 | `5` | `16000` | `7000` | `300` | `0` | `40.00` | `250` | `0.00` | `0` | `35.00` | `35` | `0` | `100` | 2 | 1 | 10000 | — |
| `CB1501_M1` | M034 | `5` | `7000` | `6800` | `280` | `0` | `50.00` | `300` | `0.00` | `20` | `40.00` | `40` | `10` | `120` | 2 | 1 | 8000 | — |
| `EVCB0102_M1` | M035 | `4` | `3000` | `3500` | `200` | `0` | `30.00` | `300` | `0.00` | `0` | `30.00` | `30` | `0` | `50` | 1 | 1 | 5000 | — |
| `CB1002_M1` | M035 | `5` | `5500` | `4500` | `280` | `0` | `40.00` | `200` | `0.00` | `0` | `30.00` | `30` | `0` | `50` | 1 | 1 | 5000 | — |
| `CB1301_M1` | M035 | `5` | `7000` | `6000` | `300` | `0` | `40.00` | `200` | `0.00` | `0` | `30.00` | `30` | `0` | `50` | 1 | 1 | 5000 | — |
| `CB1501_M2` | M035 | `5` | `7000` | `6800` | `280` | `0` | `50.00` | `300` | `0.00` | `20` | `40.00` | `40` | `10` | `120` | 1 | 1 | **8000** | — |
| `EVCB0102_M2` | M036 | `4` | `3000` | `3500` | `200` | `0` | `30.00` | `300` | `0.00` | `0` | `30.00` | `30` | `0` | `50` | 3 | 1 | 5000 | — |
| `CB1002_M2` | M036 | `5` | `5500` | `4500` | `280` | `0` | `40.00` | `200` | `0.00` | `0` | `30.00` | `30` | `0` | `50` | 3 | 1 | 5000 | — |
| `CB1301_M2` | M036 | `5` | `7000` | `6000` | `300` | `0` | `40.00` | `200` | `0.00` | `0` | `30.00` | `30` | `0` | `50` | 3 | 1 | 5000 | — |
| `CB0001_BOSS` | M040 | `1` | `400` | `190` | `100` | `0.00` | `25` | `175` | `0` | `0` | `0` | `0` | `0` | `0` | 2 | 1 | 99000 | `040` |
| `CB1201_M2` | M040 | `5` | `6500` | `6000` | `300` | `0` | `40.00` | `200` | `0.00` | `0` | `30.00` | `30` | `0` | `70` | 2 | 1 | 10000 | — |
| `CB1201_M1` | M041 | `5` | `6500` | `6000` | `300` | `0` | `40.00` | `200` | `0.00` | `0` | `30.00` | `30` | `0` | `70` | 1 | 1 | 10000 | — |
| `CB1201_M3` | M042 | `5` | `6500` | `6000` | `300` | `0` | `40.00` | `200` | `0.00` | `0` | `30.00` | `30` | `0` | `70` | 3 | 1 | 10000 | — |
| `EVCB0301_M044` | M044 | `5` | `5000` | `4000` | `250` | `0` | `30.00` | `200` | `0.00` | `0` | `30.00` | `30` | `0` | `50` | 1 | 1 | 5000 | — |
| `CB0501_M1` | M046 | `3` | `1000` | `1200` | `180` | `0` | `30.00` | `200` | `0.00` | `0` | `20.00` | `20` | `0` | `20` | 2 | 2 | 5000 | — |
| `CB0501_M3` | M048 | `3` | `1000` | `1200` | `180` | `0` | `30.00` | `200` | `0.00` | `0` | `20.00` | `20` | `0` | `20` | 3 | 2 | 5000 | — |
| `CB0202_M2` | M049 | `2` | `800` | `680` | `160` | `0` | `20.00` | `200` | `0.00` | `0` | `20.00` | `20` | `0` | `15` | 2 | 1 | 5000 | — |
| `CB0202_M1` | M050 | `2` | `800` | `680` | `160` | `0` | `20.00` | `200` | `0.00` | `0` | `20.00` | `20` | `0` | `15` | 1 | 1 | 5000 | — |
| `CB0202_M3` | M051 | `2` | `800` | `700` | `160` | `0` | `20.00` | `200` | `0.00` | `0` | `20.00` | `20` | `0` | `15` | 3 | 1 | 5000 | — |
| `CB0501_M2` | M052 | `3` | `1000` | `1200` | `180` | `0` | `30.00` | `200` | `0.00` | `0` | `20.00` | `20` | `0` | `20` | 2 | 2 | 5000 | — |
| `CB0501_M4` | M054 | `3` | `1000` | `1200` | `180` | `0` | `30.00` | `200` | `0.00` | `0` | `20.00` | `20` | `0` | `20` | 3 | 2 | 5000 | — |
| `EVCB0301_M057` | M057 | `5` | `4000` | `4500` | `200` | `0` | `30.00` | `200` | `0.00` | `0` | `30.00` | `30` | `0` | `50` | 3 | 1 | 5000 | — |
| `CB0702_M1` | M058 | `4` | `2400` | `2600` | `200` | `0` | `30.00` | `200` | `0.00` | `0` | `30.00` | `30` | `0` | `50` | 2 | 2 | 5000 | — |
| `CB0202_BOSS` | M062 | `3` | `1800` | `750` | `160` | `0` | `30.00` | `200` | `0.00` | `0` | `30.00` | `30` | `0` | `25` | 1 | 1 | 5000 | — |
| `CB0501_BOSS` | M062 | `4` | `2000` | `1500` | `210` | `0` | `30.00` | `200` | `0.00` | `0` | **`20.00`** | **`30`** | `0` | `30` | 1 | **2** | 5000 | — |
| `CB1201_BOSS` | M100 | `5` | `16000` | `7000` | `300` | `0` | `40.00` | `200` | `0.00` | `0` | `30.00` | `30` | `0` | `100` | 2 | 1 | 10000 | — |
| `CB1401_BOSS` | M100 | `5` | `20000` | `8000` | **280** | `0` | `40.00` | `250` | `0.00` | `0` | `30.00` | `30` | `0` | `150` | 2 | 1 | 10000 | — |

*(String-vs-number forms are transcribed exactly as shipped. Exactly **3** rows use
the un-suffixed tutorial spelling `spd "0.00"` / `crt_chance "25"` /
`crt_dmg "175"` / `penetration "0"` / `block_chance "0"` / `block_dec_dmg "0"` —
`CB0001_M01`, `CB0001_BOSS` and the orphan `CB0002_M01`, all three from the
`combat_base: "mission"` tutorial family and the same three rows that carry an
all-zero secondary line. The other 31 use `spd "0"`, `crt_chance "N.00"`,
`penetration "0.00"`, `block_chance "N.00"`. `cool_time` is a **number** on all
34 rows.)*

**One internal inconsistency, bolded above:** `CB0501_BOSS` is the **only** row
of the 34 whose `block_chance` (`20.00`) does **not** equal its
`block_dec_dmg` (`30`). Every other row pairs them. Do not assume the pair is
always equal when modelling this table.

### 2.2 Per-token variance — what a rebalance model must not smooth over

1. **`M034` — 4 rows, 160× HP spread, non-monotone.** `100` (orphan) → `7000`
   (`CB1501_M1`) → `13000` (`CB1002_M3`) → `16000` (`CB1301_M3`). Among the
   three **placed** rows at *constant thumb* L20/r5, ATK runs `6800 → 5500 →
   7000` and DEF `280 → 280 → 300` while HP rises monotonically, and
   `block_chance` **falls** `40.00 → 40.00 → 35.00` as HP peaks. Per-combat
   scripting, not a curve.
2. **`M035`/`M036` — paired ladders with a ladder-breaker.** `M035` and `M036`
   are numerically identical within each encounter and differ only in `attr`
   1 vs 3 — `EVCB0102` `3000/3500/200` @r4, `CB1002` `5500/4500/280` @r5,
   `CB1301` `7000/6000/300` @r5. Count **per encounter**, not per row. The
   breaker is `CB1501_M2` (`M035`), which matches the `M034` row beside it
   exactly — including `cool_time` 8000 against 5000 on the other three `M035`
   rows — and differs from `CB1301_M1` at an *identical* thumb L20/r5/h2.
3. **`M040` — one token, two narrative roles.** Tutorial boss `400/190/100` @r1
   (all-zero secondaries, `cool_time` 99000) vs chapter-12 mob `6500/6000/300`
   @r5 (`crt 40.00/200`, `block 30.00/30`, `hp_regen 70`). A ~16× HP gap between a
   boss and a mob on one token.
4. **`M062` — the only `role` disagreement.** `role` 1, rank 3,
   `1800/750/160`, `block 30.00/30`, `hp_regen 25` vs `role` 2, rank 4,
   `2000/1500/210`, `block 20.00/30`, `hp_regen 30`. Identity-unbinding at the row
   level, and the row carrying the table's only `block_chance` ≠ `block_dec_dmg`
   mismatch.
5. **`M023` — identical HP, divergent offence across displayed levels.**
   `700/400/130` (`hp_regen 8`) at thumb L5 vs `700/650/160` (`hp_regen 10`) at
   thumb L30. Flat HP with rising level is the opposite of a growth curve.
6. **`M100` — DEF moves the wrong way.** `16000/7000/300` (crt `40.00/200`,
   `hp_regen 100`) at L10 → `20000/8000/280` (crt `40.00/250`, `hp_regen 150`) at
   L15: HP, ATK, crt_dmg and regen all up, DEF **down**.
7. **`M100` is built from the shared `CB1201` mob line, not from a boss line.**
   `CB1201_BOSS` shares the trio's DEF **300** exactly and the trio's
   `block 30.00/30` and `crt 40.00/200`, while carrying ~2.5× the trio's HP.
8. **Five rows are offence-weighted (ATK > HP):** the whole `CB0501` quartet
   `1000/1200` (`M046`/`M048`/`M052`/`M054`) and `M058` `2400/2600`. `M022`
   is borderline (`450/430`, ATK below HP). Do not assume a defensive HP/ATK
   ordering.
9. **The orphan `CB0002_M01` (`100/100/100`, all-zero secondaries)** is the
   weakest scripted enemy datum in the table, one of only **4** rank-1 `M*` rows
   (`CB0001_M01`, `CB0001_BOSS`, `CB0002_M01`, `CB0102_M1`) and one of only **3**
   with an all-zero secondary line (the other two being `CB0001_M01` and
   `CB0001_BOSS` — the same 3 tutorial-family rows); its `cool_time` 99000 is
   shared by 4 rows. It has **no battle context at all** and must not anchor any
   curve.
10. **Elemental defence exists on exactly 2 of 34 `M*` rows** — `CB1501_M1` and
    `CB1501_M2` (`attr_enhance 20`, `attr_resist 10`). All other 32 rows ship
    `0`/`0`.
11. **`M044`/`M057` are the only tokens whose rows are named after the token**
    and only placed in a record their name does not match (§1.5); their HP
    (`5000`, `4000`) sits between the `CB1301` and `CB1501` bands with no
    encounter ladder of its own, and both carry the same `crt 30.00/200`,
    `block 30.00/30`, `hp_regen 50` line despite different `attr` (1 vs 3) and
    different DEF (250 vs 200).

Full per-appearance placement context, the CB1201 trio, the CB0501 quartet, the
`cool_time` 99000 four-row cohort and the cross-record reuse table are in
[`m034-variance-2026-10-05.md`](m034-variance-2026-10-05.md) §1–§2 and are not
duplicated here; §2.1 above is the complete row-level source.

### 2.3 Rebalance-use caveats (normative)

1. **Never collapse same-`res` rows into one tuple without stating the rule.**
   **7 of 22 tokens have more than one row** (`M023` 2, `M034` 4, `M035` 4,
   `M036` 3, `M040` 2, `M062` 2, `M100` 2) and 15 have exactly one. **No collapse
   rule is endorsed here.**
2. **Count per encounter / per shared-tuning group, not per row**, or weights
   inflate (the CB0501 quartet would count 4× on top of wave-slot multipliers;
   the EVCB0102 pair 2×).
3. **Never join these to video bar tokens** (`2,551`, `1,253`, `276`, `351 ×2`,
   `3188`, `3264` — see
   [`monster-hud-observations.md`](monster-hud-observations.md)): identity,
   chapter/difficulty and full-vs-current semantics are all unproved on the
   video side.
4. **Never join these to a card catalogue row of the same number** (§3.4).
5. **Era-tag every row `unknown`** against the 2019-09-05 rebalance threshold
   ([`stat-version-context.md`](stat-version-context.md)): the pack is recovered
   but its balance vintage is not established locally. Do not assume PRE or POST.
6. **`res` is not an identity.** Do not publish, label, or join any of these
   rows to a monster name, art pack, or server monster id. 20 of 22 tokens name
   nothing on this disk and 0 resolve to an identity (§1.3).

---

## 3. Corrections, provenance, limits

### 3.1 Correction — the "filename convention" claim is FALSE in both parent docs

`m034-variance-2026-10-05.md` already retracted this for `M034`
(§3.3 item 1). **This file completes the retraction, and two parent documents
still carry the false claim as live text.** Corrected readings:

| Location | Superseded text | Correction |
|---|---|---|
| `episode-stat-adjudication-2026-10-05.md` **line 270** (its §3) | "**`res` → art mapping is by filename convention (`M034` ↔ `M034.jet` family)**; no local table explicitly binds combat `res` to catalog monster rows beyond the shared token." | **FALSE.** No `M034.jet` exists, and no `M0xx` pack exists for **20 of 22** tokens. The convention is real only for the `C*` namespace (**64/64**), not the `M*` namespace (**2/22**). `res` is an opaque script token (§1.3). |
| `m001-m100-insider-2026-10-05.md` **line 189** (§2.5 item 4) | "**`res` → art mapping is by filename convention (`M100` ↔ `M100.jet` family)**; no local table explicitly binds…" | **FALSE for 20 of 22 tokens.** `M100`↔`M100.jet` happens to hold, which is exactly what makes the rule look general — it is 1 of 2 survivors, not a convention. `M100` still has **no monster identity**: its catalogue row is an admitted negative (§1.6). |
| `m034-variance-2026-10-05.md` §2 identity caveat | already corrected in that file ("That is wrong: no `M034.jet` exists anywhere in this workspace") | **consistent** — this file extends the same negative to all 22 tokens. |

The true statement, which replaces both: *the `M*` Episode `res` token is an
opaque per-appearance script token. `<res>.jet` coincidence holds for 2 of 22
tokens and there is no local binding table of any kind. The `ref_id` field is a
hunter-card namespace (120/120 to cards, 0 to monsters) and cannot substitute.*

### 3.1b Corrections to an earlier draft of THIS file (self-retraction)

Re-verified 2026-10-05; four figures in the earlier draft were wrong. Recorded so
a reader who already read it does not re-import them:

| Claim in earlier draft | Correct value | Cause |
|---|---|---|
| local art inventory is "**520** `C*` packs" | **570** `C*`-prefixed packs (113 bare `C###` + 457 suffixed forms); 774 `.jet` total | loose vs suffixed `C*` undercount; the **64/64** token test is unaffected because every Episode `C*` token is a bare stem |
| "**8** of 22 tokens have >1 row … plus `M001`/`M058` single-row" | **7** tokens have >1 row (`M023`, `M034`, `M035`, `M036`, `M040`, `M062`, `M100`); **15** have exactly one | miscount, then self-contradicting tail clause |
| rank-disagreement list "several disagree on rank (`M001`×1, `M023`×2, … `M100`×2)" | **5 of 7** multi-row tokens disagree on rank (`M034` 1/5, `M035` 4/5, `M036` 4/5, `M040` 1/5, `M062` 3/4); `M023` and `M100` **agree**; `M001` is single-row and cannot disagree | listed tokens that do not disagree |
| "the same token appears at up to **6** different thumb contexts, and **12** different tokens share the single context `(20,5,2,1)`" | max **3** distinct thumb contexts for one token (`M034`, `M035`, `M036`); busiest context is shared by only **2** tokens, and `(20,5,2,1)` is held by **`M035` alone** | overstatement; the decoupling of `res` from thumb context is real but **much weaker** than claimed |

None of these affects the headline verdict (0/22 identity bindings), the
2/22-vs-64/64 asymmetry, the 72-placement census, or any tuple in §2.1.

### 3.2 Method

All values re-derived from disk on 2026-10-05 by: (1) parsing
`EPISODE_STAT_ACTORS.json` as a list and splitting rows on the `res_id` shape;
(2) enumerating **every** `actor_id`, `side`, `wave`, `slot`, `type`, `thumb` and
`skill` array across all **61** combat records and joining by actor id; (3) a
workspace-wide filename sweep for `M\d+\.jet` (**154** files, **22** unique names,
across **7** duplicated extraction trees — `analysis/extracted/assets`,
`analysis/jadx/resources/assets`, four `analysis/patched/debug-*` trees and
`recovered-assets/phone-2026-09-18/.../split_PADResource/assets`, each holding the
same 22 names, with `M100.jet` SHA256 `f133b1ae…` identical across all 7 copies —
confirming no additional M art exists in any copy); (4) a **sub-string** sweep for
each token inside every local pack stem; (5) resolving each of the 55 distinct
`ref_id` values against both catalogue directories; (6) regex sweeps of
`native-all-strings.tsv` and `EPISODE_S01.json`; (7) a byte-level literal grep for
`CB0002_M01` across `analysis/recovered-reference/*.json`.

### 3.3 Limits

- `res` → monster identity is **unbound locally**, and now known to be unbound
  *structurally* (§1.3), not merely unsearched.
- The 20 unresolved tokens are missing **from this workspace**, not proven
  missing from the original game: the original Episode resource set is not
  locally complete (AGENTS.md §94/§97 — the Episode packs serve dialogue,
  combat data and one background, and per-entity monster art is among what has
  not been recovered).
- Episode combat **rendering** remains unverified; no row is tied to an observed
  bar, nameplate or native receipt (AGENTS.md §91/§97, §96–§98).
- No difficulty/chapter parameter for these scripted rows has been recovered, so
  the reason two rows at identical thumbs differ is **not established** — only
  that they do.
- The 2/22 art survivors are file-presence facts, not render facts: nothing here
  shows `M001.jet` or `M100.jet` was ever loaded in an Episode scene.
- This file does not adjudicate the 7 `C010`-token rows (all `ref_id` `010`, i.e.
  the enemy-Vincent hunter-card token placed as `type: monster`), of which the
  parent adjudication documents 3 as ally-side and excluded. That stands
  unexamined here; they are out of the `M*` namespace and out of this file's scope.

### 3.4 The false-friend table (read before any join)

20 of 22 unresolved tokens have a **hunter card catalogue row of the same
number**. This is a **namespace collision, not a binding**, and it is the most
likely wrong join available:

`M022`→card `022` · `M023`→`023` · `M024`→`024` · `M034`→`034` ·
`M035`→`035` · `M036`→`036` · `M040`→`040` · `M041`→`041` · `M042`→`042` ·
`M044`→`044` · `M046`→`046` · `M048`→`048` · `M049`→`049` · `M050`→`050` ·
`M051`→`051` · `M052`→`052` · `M054`→`054` · `M057`→`057` · `M058`→`058` ·
`M062`→`062` — **all 20 exist**. `M001` additionally collides with card `001`,
whose art the `C001` namespace already owns.

Proof they are different namespaces: the table itself uses both at once —
`CB0001_M01` has `res_id` `M001` **and** `ref_id` `001`, i.e. a monster token and
a card reference on the same row, and they are demonstrably different things (the
`ref_id` values resolve 120/120 to cards, 0/120 to monsters).

### 3.5 Hygiene

Read-only enumeration. No server, APK, client, emulator, account, tutorial,
LevelDB or coverage state was modified; **no coverage file was edited**; no
temporary script was left inside the workspace. The only workspace writes from
this probe are this file plus the mirrored impure note appended to
[`polluted-observations.md`](polluted-observations.md).

### 3.6 Key reading

1. This file — the 22-token verdict and the measured C-vs-M asymmetry.
2. [`m034-variance-2026-10-05.md`](m034-variance-2026-10-05.md) — per-appearance
   placement detail for M034/M035/M036 and the shared-tuning groups.
3. [`m001-m100-insider-2026-10-05.md`](m001-m100-insider-2026-10-05.md) — the
   two art-bearing tokens, with its §2.5 item 4 now superseded (§3.1).
4. [`episode-stat-adjudication-2026-10-05.md`](episode-stat-adjudication-2026-10-05.md)
   — the 37-row framing; its §3 provenance line is now superseded (§3.1).
5. [`coverage.md`](coverage.md) — the 0/22 monster denominator, unchanged.