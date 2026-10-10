# Hunter Search settlement divergence and the Wednesday negative (2026-10-05)

**Read-only recording pass. No server code, fixture, test, state file, APK, seed,
LevelDB, emulator, VM or catalogue was changed or written.** This file is the
only artefact. `polluted-observations.md` is deliberately **not** appended — the
parent mirrors.

Scope: propagate three claims from
`analysis/research/base-stats-visual-hunt/blitz-search-consumers-2026-10-05.md`
§3.2 / §2.4 / §1.7 into a precise, locatable record.

1. **NEW DIVERGENCE** — the replica awards a trace **only** on
   `cleared_wave === max_wave`, while shipped `CONTENTS12_2` awards **one reward
   box per completed battle** with partial credit retained on defeat.
2. **WEDNESDAY NEGATIVE** — shipped `TIP_8` says Guild Blitz registration opens
   every Wednesday, but GVG runs on eight absolute server datetimes and the
   client has **no weekday logic**, so a Wednesday gate must **not** be
   implemented. Verified that nothing in `server-ts` or in the research tree
   currently proposes one.
3. **Propagation** — `InitEffect` registers wave-banner totals **2, 3 and 4
   only** (no total-1 family), corroborating
   `analysis/research/search-effect-root-contract.md` and confirming the
   2-wave `local_search_017` fixture is **native-legal** while 4 is the
   **original**.

**No coverage credit.** Strict base-stat coverage is unchanged at heroes
1/113, accessories 1/100, monsters 0/22 (`coverage.md`). Nothing here is a
hero, jewel, accessory or monster stat. Per `AGENTS.md` §15, recovered /
fixture / unknown are marked separately throughout.

---

# SECTION 1 — PURE: exact code paths and the native key list

Pure = verbatim replica source at a stated `file:line`, and verbatim native
literals / symbols / addresses from already-saved artefacts. No balance claim,
no era inference, no fixture conclusion in this section.

## 1.1 Where `SEARCH_WAVE_COUNT` is defined

`server-ts/src/search-stage.ts:3-6` — verbatim:

```ts
export const SEARCH_STAGE_ID = "local_search_017";
export const SEARCH_WAVE_COUNT = 2;
/** Search auto-shows IG_WAVE1_N; native InitEffect only registers N=2,3,4.
 * Use a distinct unlinked reference so ordinary campaign waves remain intact. */
```

The in-source comment **already cites the native registration bound** and is
correct. The bound is a *renderability* constraint (claim 3 below), not a
balance value.

`server-ts/src/search-stage.ts:12-18` builds the wave rows — verbatim:

```ts
export function searchStageMonsters(): StageMonsterRecord {
  const base = starterStageMonstersByStageId.n_01_01;
  const waves = Array.from({ length: SEARCH_WAVE_COUNT }, (_, index) => base.wave_list[0].map((monster) => ({
    ...monster, _id: `${SEARCH_STAGE_ID}_${index}_${monster.ref_id}`,
  })));
  return { ...base, _id: waves, wave_list: waves };
}
```

Two pure facts: wave count scales with the constant, and **every wave is a
verbatim clone of `n_01_01` wave 0** — so raising the constant to 4 would yield
four *identical* waves, not the documented rising difficulty.

## 1.2 The award site — the single place a trace is granted

`server-ts/src/search-battle.ts:192-223`, the `/explore/End` branch. Verbatim,
with line anchors:

```ts
192	  if (route === "/explore/End") {
193	    const logId = integer(payload.log_id), clearedWave = integer(payload.cleared_wave);
194	    if (!game.search.active) return game.search.last?.attempt.log_id === logId
195	      ? { data: { ...game.search.last.receipt, item: [] } } : { error: "Search log not found" };
196	    const attempt = game.search.active;
...
199	    if (logId !== attempt.log_id || !Number.isSafeInteger(clearedWave) || clearedWave < 0 || clearedWave > attempt.wave_count ||
200	        !info || typeof info !== "object" || Array.isArray(info))
201	      return { error: "Search log or wave mismatch" };
...
206	    const won = explicitSearchCapsuleVictory(info);
207	    if (won !== (clearedWave === attempt.wave_count)) return { error: "Search outcome and completed wave disagree" };
208	    const receipt: SearchEndReceipt = { wave: { cleared_wave: clearedWave, max_wave: attempt.wave_count },
209	      consume_result: [], item: [], gem: [], special: [], reward_item: [] };
210	    if (won) {
211	      const refId = "local_sylvester_trace";
...
214	      const quantity = attempt.guided ? GUIDE_TRACE_QTY : 1;
...
221	      receipt.item.push({ inst_id: item.inst_id, ref_id: refId, added: quantity });
222	      receipt.reward_item.push({ ref_id: refId, qty: quantity });
223	    }
```

**`search-battle.ts:210` — `if (won)` — is the only award site.** The trace
quantity is decided by `search-battle.ts:214` as a **flat scalar**: the guided
threshold, else `1`. There is no per-wave term anywhere in the branch.

The predicate behind `won` is `server-ts/src/search-capsules.ts:13-18` —
verbatim:

```ts
export function explicitSearchCapsuleVictory(raw: unknown): boolean {
  if (typeof raw === "string") { try { raw = JSON.parse(raw); } catch { return false; } }
  if (!raw || typeof raw !== "object" || Array.isArray(raw)) return false;
  const clear = (raw as Record<string, unknown>).clear;
  return clear === 1 || clear === "1" || clear === true;
}
```

## 1.3 Two structural constraints that make partial credit *impossible to persist*

`search-battle.ts:207` binds the win flag to full clear, so a **partial defeat
is accepted** (see §1.4). But the receipt shape itself is pinned to **exactly
zero-or-one** box. `server-ts/src/search-battle.ts:53-69`, the
`normalizeSearch` validation of the persisted `last` receipt — verbatim:

```ts
53	  if (value.last !== null) {
54	    check(value.last.attempt);
55	    const receipt = value.last.receipt;
56	    // Preserve already settled old one-trace guided receipts exactly.
57	    const quantities = value.last.attempt.guided ? [1, GUIDE_TRACE_QTY] : [1];
58	    if (!receipt || !Number.isSafeInteger(receipt.wave?.cleared_wave) || receipt.wave.cleared_wave < 0 ||
59	        receipt.wave.cleared_wave > value.last.attempt.wave_count || receipt.wave.max_wave !== value.last.attempt.wave_count ||
60	        ![receipt.item, receipt.gem, receipt.special, receipt.consume_result, receipt.reward_item].every(Array.isArray))
61	      throw new Error("Malformed Search receipt");
62	    if (receipt.consume_result.length || receipt.gem.length || receipt.special.length || receipt.item.length > 1 ||
63	        receipt.item.some((row) => !row || !Number.isSafeInteger(row.inst_id) || row.inst_id < 1 ||
64	          row.ref_id !== "local_sylvester_trace" || !quantities.includes(row.added)) ||
65	        receipt.reward_item.length !== (receipt.wave.cleared_wave === receipt.wave.max_wave ? 1 : 0) ||
66	        receipt.reward_item.some((row) => !row || row.ref_id !== "local_sylvester_trace" || !quantities.includes(row.qty)) ||
67	        receipt.item.length !== receipt.reward_item.length ||
68	        receipt.item.some((row, index) => row.added !== receipt.reward_item[index].qty)) throw new Error("Malformed Search reward");
```

Three load-bearing lines:

- **`search-battle.ts:65`** — `receipt.reward_item.length !== (cleared_wave === max_wave ? 1 : 0)`.
  This is the *same* full-clear equality as line 207, restated as a **persisted
  state invariant**. It is the single most actionable line for the divergence.
- **`search-battle.ts:62`** — `receipt.item.length > 1` throws
  `"Malformed Search reward"`. A multi-box receipt is structurally rejected.
- **`search-battle.ts:57` + `:64`/`:66`** — every `added`/`qty` must be a
  member of `quantities`, i.e. exactly `1`, or `1`/`10` for a guided attempt.

Consequence: a 4-wave Search that awards 4 boxes, **or** a partial defeat that
awards 1 box, would produce a receipt that this validator **throws on load**.
The divergence is therefore not merely a balance choice — it is baked into
persisted-state validation.

## 1.4 A partial defeat *is* structurally representable today

`server-ts/src/search-battle.ts:58-59` accepts
`cleared_wave` anywhere in `[0, wave_count]`, and
`search-battle.ts:199` likewise bounds the request by `attempt.wave_count`, not
by "win or zero". At `wave_count = 2` a loss reporting `cleared_wave: 1`
therefore passes `search-battle.ts:207` (`won === false`,
`clearedWave !== 2`) with no error, and is settled with an **empty**
`item`/`reward_item` (`search-battle.ts:208-209`).

**The information is available and discarded.** `cleared_wave` is received,
validated, persisted into `receipt.wave.cleared_wave` and echoed to the client —
it is only the `if (won)` guard at line 210 that suppresses the credit.

## 1.5 The attempt schema already admits `wave_count` 4

`server-ts/src/search-battle.ts:47` — verbatim:

```ts
        ![1, 2, 3, 4].includes(row.wave_count) || !Number.isSafeInteger(row.capsule_inst_id) ||
```

`search-battle.ts:179` sets `wave_count: SEARCH_WAVE_COUNT` on every new
attempt, and `search-battle.ts:104` already builds the Begin `wave_info` rows
from `attempt.wave_count`:

```ts
104	  return { log_id: attempt.log_id, reward_cnt: [1], wave_info: Array.from({ length: attempt.wave_count }, (_, wave) => ({ stage_id: attempt.stage_id, wave,
105	    enemy_hp_per: 100, enemy_atk_per: 100, skill1: 0, skill2: 0, skill3: 0, skill4: 0, skill5: 0 })),
```

**Pure finding:** the accepted-state set is `1,2,3,4` and both the Begin receipt
and the state validator already scale with the count. The only blockers to a
4-wave fixture are (a) the `SEARCH_WAVE_COUNT` constant and (b) the receipt
reward shape of §1.3. Nothing else in `search-battle.ts` needs to change for the
structure; the reward arithmetic is a separate, deliberate question.

## 1.6 A second full-clear-only gate: the guided-recruit tutorial prerequisite

`server-ts/src/state.ts:1236-1239`, inside the `/tuto/Clear` handler for the
`type 37 / step 1` pair — verbatim:

```ts
1236	      if (!game.tutorial.some((row) => row.type === 37 && row.step === 0 && row.is_cleared === 1) ||
1237	          !completed || completed.attempt.ref_id !== target.id ||
1238	          completed.receipt.wave.cleared_wave !== completed.attempt.wave_count || !ownedTrace)
1239	        return this.failure(2001, "Complete Search and collect the required traces before guided recruitment");
```

Line **1238** repeats the `cleared_wave !== wave_count` equality a third time.
Recorded because it is easy to fix §1.3 and miss this: even a partial-credit
award would not by itself advance tutorial 37/1. Whether the tutorial gate
*should* relax is a separate decision, not implied by `CONTENTS12_2`.

## 1.7 The trace reference rows the award uses

- `server-ts/src/hunter-traces.ts:10` — `{ id: "local_sylvester_trace", cardId: "006", rank: 1, name: "Sylvester Traces", collect_qty: 10 }`
- `server-ts/src/hunter-traces.ts:9` — `{ id: "local_gerard_trace", cardId: "005", rank: 2, name: "Gerard Traces", collect_qty: 20 }`
- `server-ts/src/search-battle.ts:8` — `const GUIDE_TRACE_QTY = HUNTER_TRACE_ITEMS.find((row) => row.cardId === "006")!.collect_qty;`

These ids are `local_*` and the quantities are replica-authored. Nothing here is
original game data.

## 1.8 Capsule earning is a separate path and is not per-wave

`server-ts/src/search-capsules.ts:20-22` — the doc comment states the caller must
establish "a live matching battle and native clear". Capsule drops are granted
by the **campaign** victory path, not by Search waves; `AIRSHIP_TICKET` is
consumed at Begin (`search-battle.ts:184`). So `cleared_wave` governs **only**
the trace award. Recorded to prevent conflating the two reward streams.

## 1.9 NATIVE KEY LIST — `InitEffect` wave-banner families

Source file: `analysis/ghidra-search-effect-root-keys.txt` (saved
`ResolvePcRelativeStrings` output for `InitEffect` at `0x009c33c4`). Verbatim,
lines 47-49 of that file — these are the **only three** `IG_WAVE` registration
sites in the function (line 50: `resolved: 48`):

```
47	ldr@009c6a82 slot=0x9c6aa0 w=0x13aed2b add@009c6a8a -> 0x1d757b9  "IG_WAVE%s_%s"
48	ldr@009c6bf6 slot=0x9c6eb8 w=0x13aebb7 add@009c6bfe -> 0x1d757b9  "IG_WAVE%s_%s"
49	ldr@009c6d56 slot=0x9c6ebc w=0x13aea57 add@009c6d5e -> 0x1d757b9  "IG_WAVE%s_%s"
```

All three resolve to the **same** literal `0x1d757b9 "IG_WAVE%s_%s"`. The loop
bounds that make the totals 2/3/4 are in
`analysis/research/search-effect-root-contract.md:43-49`, verbatim:

> - Lines4106..4191: current1..2, constant total2.
> - Lines4192..4277: current1..3, constant total3.
> - Lines4278..end: current1..4, constant total4.

**The registered key set, derived: `IG_WAVE1_2`, `IG_WAVE2_2`, `IG_WAVE1_3`,
`IG_WAVE2_3`, `IG_WAVE3_3`, `IG_WAVE1_4`, `IG_WAVE2_4`, `IG_WAVE3_4`,
`IG_WAVE4_4` — nine keys. There is NO total-1 family, so `IG_WAVE1_1` is
unregistered.**

The requesting side, `analysis/research/search-effect-root-contract.md:39`,
verbatim:

> **OnProcWaveChange**: **9ceaa2 compares game.MODE+2ec to4**. In that branch
> **9ceaa6 loads GROUP_DATA.current_wave+1c**, **9ceaaa loads max_wave+24**,
> **9ceab2 adds1 to current**, and **9ceab6 formats `IG_WAVE%d_%u`**
> (LDR9ceaae/slot9cedf4/ADD9ceab0). It then calls ShowEffect at**9ceb1a**. A
> one-wave initial group requests **IG_WAVE1_1**.

**Corroboration statement (claim 3).** `search-stage.ts:5-6`'s comment is
**accurate**: the supported wave-total set is `{2, 3, 4}`. Therefore:

- `SEARCH_WAVE_COUNT = 2` (`search-stage.ts:4`) is **native-legal** — inside the
  registered set. It is a *local reconstruction choice*, not a violation.
- `max_wave = 4`, the documented original, is **also native-legal**.
- `wave_count = 1` is **native-illegal** and would request the unregistered
  `IG_WAVE1_1` — the exact cause recorded in
  `search-effect-root-contract.md:49-51` and in `AGENTS.md` §74.

## 1.10 NATIVE KEY LIST — the Search fields that would express per-wave credit

From `blitz-search-consumers-2026-10-05.md:368-372`, addresses are `.rodata`
literal VAs in `analysis/native-all-strings.tsv`:

| address | key |
|---|---|
| `0x01d72a6a` | `cleared_wave` |
| `0x01d72b16` | `cleared_explore` |
| `0x01d72b26` | **`reward_cnt`** |
| `0x01d72b8c` | `max_wave` |
| `0x01d72c1e` | `play_cnt` |
| `0x01d72c27` | `retry_cnt` |

`reward_cnt` and `cleared_explore` are the native fields that would carry a
per-wave box count and a completed-explore flag. Pure field-name existence only
— no value, and no parser binding verified for the count semantics.

Note a replica-side naming collision worth recording: `search-battle.ts:104`
already emits a Begin-receipt field named **`reward_cnt`** as the literal
`[1]`, a different meaning from the `reward_cnt` field above. Do not treat the
two as the same contract without checking the parser.

## 1.11 NATIVE KEY LIST — GVG's eight absolute phase datetimes

From `blitz-search-consumers-2026-10-05.md:168-172`, addresses are `.rodata`
literal VAs:

| address | key |
|---|---|
| `0x01d79540` | `teaser_begin_dtm` |
| `0x01d79551` | `register_begin_dtm` |
| `0x01d79564` | `matching_begin_dtm` |
| `0x01d79577` | `deploy_begin_dtm` |
| `0x01d79588` | `combat_begin_dtm` |
| `0x01d79599` | `calc_begin_dtm` |
| `0x01d795a8` | `result_begin_dtm` |
| `0x01d795b9` | `finish_dtm` |
| `0x01d795c4` | `next_gvg_dtm` |

Consumers: `CSRGuildBattleMgr::GetCurGVGPhase()` at `0x00257344`,
`GetNextGVGBeginTime()` at `0x00259870`, `IsNextGVGBegin()` at `0x00259169`
(`analysis/native-all-strings.tsv`).

## 1.12 WEDNESDAY NEGATIVE — exhaustive search for weekday logic in `server-ts`

Searched `server-ts/` for
`wednesday|weekday|day_of_week|dayofweek|getday` (case-insensitive): **zero
matches in any file.**

Searched `server-ts/src` for `604800|_dtm|gvg|GVG|register_begin`: the only hits
are

- `server-ts/src/arena.ts:76-80` (the `604800` window, below),
- `server-ts/src/openapi.ts:78` — `gvg: "Guild versus guild"`, a route-family
  **display label** in the OpenAPI tag map, not scheduling,
- `server-ts/src/catalog.ts:10` — `"gvg"` in a route-name list,
- `server-ts/src/game-routes.ts:570` — verbatim:
  `if (/^\/(guild|gvg|arena|relation)\//.test(route)) Object.assign(data, { list: [], users: [] });`

That last line is the compatibility-fixture fallback (`AGENTS.md` §6). **No
`/gvg/*` route has a dedicated handler**, so no GVG phase clock, registration
window or weekday gate exists anywhere in the replica.

### The only weekly arithmetic in the replica, and why it is not Wednesday

`server-ts/src/arena.ts:72-81` — verbatim:

```ts
/** Native end_datetime subtracts GetCurServerTime seconds and divides by86400.
 * Units are recovered; weekly alignment and season schedule remain fixtures.
 * See arena-season-time-units.md; rendered countdown is still unverified. */
export function arenaSeason(now = Date.now()) {
  const start = Math.floor(now / 1000 / 604800) * 604800;
  return { season_no: 1, weekly_no: 1, start_datetime: start,
    end_datetime: start + 604800, next_datetime: start + 604800,
    weekly_start_datetime: start, weekly_end_datetime: start + 604800,
    weekly_next_datetime: start + 604800 };
}
```

Pure facts:

1. The window is a **rolling Unix-week bucket**, `floor(unix_seconds / 604800)`.
   The Unix epoch `1970-01-01` was a **Thursday**, so this anchor is
   Thursday-aligned. It is **not** Wednesday, and it is derived from an integer
   division, **not** from any weekday computation.
2. The window has **no observable effect**. `server-ts/src/arena.ts:66-71`
   (`arenaProfile`) hardcodes `season_no: 1` and `weekly_no: 1` as constants,
   and `server-ts/src/arena-service.ts:26-27` publishes `is_weekly_reward: 0`
   as a constant. Nothing increments `weekly_no` or `season_no`, so crossing an
   `arenaSeason` boundary changes only the emitted datetimes.
3. `server-ts/src/arena.ts:73-74` and
   `analysis/research/arena-season-time-units.md:5` both already state that
   "weekly alignment and season schedule remain fixtures".

**Conclusion (pure):** the replica contains no Wednesday gate, no weekday
computation, and no weekly FC-or-Blitz reset of any kind. The single
`604800` expression is a Thursday-anchored rolling window whose counters never
advance — a placeholder, and correctly labelled as one.

## 1.13 WEDNESDAY NEGATIVE — research-tree check: nothing proposes a Wednesday gate

Searched `analysis/research/` for
`weekly reset|weekly cycle|week gate|weekday gate|wednesday gate|weekly FC|weekly blitz`.
Five matches, **all of them prohibitions or the open question**, none a proposal:

| file:line | text | direction |
|---|---|---|
| `weekday-ui-2026-10-05.md:236` | row T6 `TIP_3` "every week" without a day → native binding **none** | negative |
| `weekday-ui-2026-10-05.md:305` | "Are Wednesday's two texts driven by the same weekly cycle as Sunday's, or by a separate one? Three texts, no shared literal, no answer." | **the open question** |
| `blitz-search-consumers-2026-10-05.md:414` | "…is answered **no** — GVG has a server-supplied absolute phase clock with no weekday logic client-side." | answers it **negative** |
| `blitz-search-consumers-2026-10-05.md:499` | "…leaves open whether Wednesday is driven by a shared weekly cycle." | restates the open question |
| `blitz-search-consumers-2026-10-05.md:513` | "A replica must not implement a Wednesday gate; it must publish `register_begin_dtm`/`finish_dtm`." | **explicit prohibition** |

Two further existing prohibitions worth citing so the negative is not
re-derived:

- `weekday-ui-2026-10-05.md:246-251` — "**Do not collapse them into the Sunday
  payout** and do not read 'Wednesday' as a rival answer to 'Sunday' — they are
  three distinct systems … A schedule model needs three separate rules, not one
  weekday."
- `weekday-ui-2026-10-05.md:268-270` — "Not that `weekly_end_datetime` is
  Sunday 24:00 UTC. The replica's current fixture aligns to a Unix week."
- `sunday-settlement-2026-10-05.md:141` — "Do not collapse Wednesday
  announcements into the Sunday payout."

**Conclusion (pure):** the research tree contains **no** proposal to implement a
Wednesday or weekly FC-or-Blitz reset. It contains the opposite, in three
places, plus the now-answered open question.

## 1.14 The shipped strings that create the apparent conflict

`analysis/recovered-data/leveldb-tables/all-tables.json`, `UI_TEXT_RO` rows,
values quoted from the existing sweep at
`weekday-ui-2026-10-05.md:117-138`:

| key | `EN` |
|---|---|
| `TIP_4` | `Fight Club rankings are announced every Wednesday.` |
| `TIP_8` | `Guild Blitz participation requests can be made every Wednesday.` |

Native side: `analysis/native-all-strings.tsv:453909` contains the single
literal `Wednesday` at `01dab83d`. Per
`sunday-settlement-2026-10-05.md:70,104` these weekday literals sit in an
**unbound libc/curl string block**, and `weekday-ui-2026-10-05.md:222-225`
re-states that the negative still stands. **No native weekday consumer exists.**
That is the whole basis for §1.12/§1.13.

---

# SECTION 2 — UNPURE: every numeral, with source and era

**Every numeral in this section is impure.** None is a recovered stat, none
changes a fixture, none counts toward any coverage denominator.

Era tags follow `analysis/research/base-stats-visual-hunt/stat-version-context.md`
(balance-epoch threshold **2019-09-05**), as used by the source pass:

- **[HELP-2.8.0.1]** — `UI_CSV.jet` from the shipped build. POST-threshold.
- **[DB-2.8.0.1]** — recovered LevelDB `UI_TEXT_RO` / `UI_JSON_RO`. Same shipped
  client lineage. POST-threshold.
- **[BINARY]** — a native literal or field name. **Era-neutral**: the binary
  carries no independent date, but GVG is absent from 1.4.4.1, so it is by
  construction a 2.8-era feature.
- **[CONTENTS12_2]** — the `UI_CSV.jet` help record. [HELP-2.8.0.1],
  single-version.
- **[REPLICA-LOCAL]** — a value authored in `server-ts`. **Not original game
  data and not era-classified**; it is this project's local policy.

## 2.1 `CONTENTS12_2` — the four numerals, all five locales

`analysis/research/base-stats-visual-hunt/help-2_8-sweep-2026-10-05.md:288-391`.
Record anchor (char offset) **152737**; `res: "G_LI12_2"`; keys in file order
`type`, `id`, `res`, `title`, `desc1`.

| numeral | `title` / `desc1` claim | locale agreement | era |
|---|---|---|---|
| **4** | `title` EN: `4 Consecutive Battles`. `desc1` EN: "All Hunter Searches **have four consecutive battles.**" | **5 of 5** locales: KO `4회의 연속적 전투와 보상 구성`, EN `4 Consecutive Battles`, JA `4回の連続バトルと報酬構成`, SC `4次连续战斗与奖励构成`, TC `4回連續戰鬥與獎勵構成` | [CONTENTS12_2] |
| **1** | `desc1` EN: "A reward box is given **with each battle completed**." | **5 of 5**. JA `各バトルが終了するたびに報酬BOXを1つ獲得でき`; SC `每次战斗结束时可获得1个奖励箱`; TC `每回戰鬥結束時可獲得1個獎勵箱` | [CONTENTS12_2] |
| **4** (max boxes) | `desc1` EN: "If all battles are won a maximum of **4** boxes can be obtained." | **5 of 5**. KO `모두 승리할 경우 한번에 최대 4개까지 상자를 획득합니다` | [CONTENTS12_2] |
| **partial on defeat** | `desc1` EN: "If you are defeated, you receive **only the boxes earned from complete battles**." | **5 of 5**. KO `중간에 패배할 경우, 그 때까지 획득한 상자의 보상만 획득합니다`; JA `途中で敗北した場合それまでに獲得したBOX報酬のみ獲得できます`; SC `战斗中途失败仅能获得之前已获得的奖励`; TC `戰鬥中途失敗僅能獲得之前已取得的獎勵` | [CONTENTS12_2] |

`desc1` per-locale value offsets and SHA-256, recorded so the wording is
re-verifiable: KO **152993** / 235 chars /
`776bb8d9c21c12b27db5024a13f2b3775702c176d3833dbee21cdd36c42c0cd3`; EN **153251**
/ 433 chars /
`880cfb2a1392c80a1a4cf6c3cee0ccfc17fcbb88d02d5eb3b8353eb08b762ca0`; JA
**153708** / 230 chars /
`a5f81572447b21342ab1effe1bffcda80510a512fe144eaa99923db14a5c7cef`; SC
**153961** / 104 chars /
`3a13c4cab87ac5fce55d7ff0a7e633b343661f2fb6651b15303ae9f735f5d236`; TC
**154088** / 109 chars /
`8752e24033fcd6f7358bed72057e2829bdf7399fc10d1a87c45d4aed38f8e386`.

**Why the five-locale agreement matters:** the partial-credit rule is not an
English rendering artefact. All five translations state it independently, and
the KO/EN phrasings differ structurally ("그 때까지 획득한 상자" = *the boxes
acquired up to that point* vs "only the boxes earned from complete battles")
while meaning the same thing. That is much stronger than the single-source
`help-2_8-sweep` record on its own. It remains **display copy**, not a parser
binding — see §2.4.

## 2.2 The replica's counter-numerals, all local

| numeral | replica location | meaning | era |
|---|---|---|---|
| **2** | `search-stage.ts:4` `SEARCH_WAVE_COUNT` | Search wave count in the fixture | [REPLICA-LOCAL] |
| **2** | `search-stage.ts:13-17` | wave rows built, each cloned from `n_01_01` wave 0 | [REPLICA-LOCAL] |
| **1** | `search-battle.ts:214` | ordinary-win trace quantity (flat) | [REPLICA-LOCAL] |
| **10** | `hunter-traces.ts:10` `collect_qty`, consumed at `search-battle.ts:8` | guided-win trace quantity = Sylvester exchange threshold | [REPLICA-LOCAL] |
| **0 / 1** | `search-battle.ts:65` | `reward_item.length` permitted values, keyed on full clear | [REPLICA-LOCAL] |
| **1** | `search-battle.ts:62` | maximum permitted `item.length` in a persisted receipt | [REPLICA-LOCAL] |
| **1,2,3,4** | `search-battle.ts:47` | accepted `wave_count` set | [REPLICA-LOCAL] |
| **604800** | `arena.ts:76,78,79,80` | rolling Unix-week window, Thursday-anchored; counters inert | [REPLICA-LOCAL] |
| **1** | `arena.ts:67,77` | hardcoded `season_no`/`weekly_no` | [REPLICA-LOCAL] |
| **0** | `arena-service.ts:27` | hardcoded `is_weekly_reward` | [REPLICA-LOCAL] |
| **1** | `search-capsules.ts:8,22-29` | capsule quantity per campaign victory | [REPLICA-LOCAL] |
| **20 / 10** | `hunter-traces.ts:9,10` | Gerard / Sylvester trace thresholds | [REPLICA-LOCAL] |

## 2.3 The divergence, stated numerically

Replica rule (`search-battle.ts:210`): **trace × 1 if `cleared_wave == max_wave`,
else × 0.** Shipped rule: **× 1 per completed battle**, maximum 4, retained
proportionally on defeat.

| Search shape | replica award | `CONTENTS12_2` award | agrees? |
|---|---|---|---|
| 2-wave, full clear (the only shape currently reachable) | 1 box | 2 boxes | **no** |
| 2-wave, defeat after wave 1 | 0 | 1 box | **no** |
| 4-wave, full clear (documented original) | 1 box | 4 boxes | **no** |
| 4-wave, defeat after wave 3 | 0 | 3 boxes | **no** |
| 4-wave, defeat at wave 0 | 0 | 0 boxes | yes |

**Corrected characterisation.** The source pass (§3.2c) said the divergence
"becomes observable the moment a Search is lost partway" and that it is
"invisible at the replica's 2-wave fixture". Both halves need one correction:
the divergence is **already present at 2 waves on the WIN path** — the replica
grants 1 box where the shipped per-battle rule grants 2. It is *invisible in
observed outcomes* only because no 2-wave loss has been captured, because the
current tests only assert the win case, and because no live account has reached
a partial defeat. `tests/search-battle.ts:107` asserts
`{cleared_wave: 2, max_wave: 2}` and `tests/search-battle.ts:150` uses
`cleared_wave: 0` for the loss leg — the **partial** defeat (`cleared_wave: 1`)
is not covered by any test. Recorded as a test-coverage gap, not a code change.

## 2.4 Why this is still recorded as a divergence and not a correction

Three reasons the repo owner, not this pass, should decide:

1. **The replica's shape may be the faithful one.** `reward_cnt` (`0x01d72b26`)
   and `cleared_explore` (`0x01d72b16`) exist as native fields but **no parser
   binding for their count semantics was verified**. `CONTENTS12_2` is display
   copy, and `AGENTS.md` §15 requires marking that. The shipped text could
   describe an intended cadence the original server did not implement
   literally, or the original could have used `cleared_explore` for exactly this
   partial credit.
2. **The persisted validator would need coordinated change.**
   `search-battle.ts:62`/`:65` and `state.ts:1238` are three coupled sites plus a
   legacy-migration question (`search-battle.ts:56-57` preserves "already settled
   old one-trace guided receipts exactly"). Changing them is a migration, not a
   one-line edit.
3. **Trace quantity is already a local fixture** (`1` / `10`,
   `hunter-traces.ts:9-10`). Introducing a per-wave multiplier multiplies two
   guessed quantities; no original drop rate has been recovered
   (`blitz-search-consumers-2026-10-05.md:416-418`: "No native reference data for
   `CONTENTS12_*` Search quantities … `cost` and `max_play_cnt` are *field
   names*, not values").

**Recommendation, recorded not applied:** if the owner moves to a 4-wave
fixture, §1.3's three lines must change in the same checkpoint, or
`normalizeSearch` will throw `"Malformed Search reward"` on the next load of a
legitimately partial or multi-box receipt. The cheapest interim is to keep 2
waves and record the divergence at both the award site and in the OpenAPI
description (`server-ts/src/openapi.ts:674`, which currently states "Local
ordinary victory awards 1 Sylvester trace … Defeat awards none" — itself a
truthful description of the *implemented* rule, so it is not wrong, only
under-documented relative to the shipped original).

## 2.5 The Wednesday numerals

| numeral | source | claim | native status | era |
|---|---|---|---|---|
| **Wednesday** | `UI_TEXT_RO` `TIP_4` (EN `Fight Club rankings are announced every Wednesday.`) | weekly FC ranking announcement | **no consumer**; single unbound literal `01dab83d` | [DB-2.8.0.1] / [BINARY] negative |
| **Wednesday** | `UI_TEXT_RO` `TIP_8` (EN `Guild Blitz participation requests can be made every Wednesday.`) | weekly Blitz registration open | **no consumer**; GVG uses the 8 `*_dtm` fields | [DB-2.8.0.1] / [BINARY] negative |
| **8** (dtm fields) | `0x01d79540`…`0x01d795b9` plus `next_gvg_dtm` `0x01d795c4` | GVG phase clock | **native, absolute server datetimes** | [BINARY] |
| **0** weekday logic | `analysis/native-all-strings.tsv` + `server-ts/` search | — | **none exists**, client or replica | — |

**Era note.** `TIP_4`/`TIP_8` are [DB-2.8.0.1], POST-threshold, and GVG is
absent from 1.4.4.1 — so the Wednesday copy and the GVG system are the same
era, which is exactly why the copy could not have been a stale translation of a
*different* system's schedule. It is a **server-side scheduling promise
presented as display copy** (`blitz-search-consumers-2026-10-05.md:511-513`).

## 2.6 The wave-count bound numerals

| numeral | source | meaning | era |
|---|---|---|---|
| **2, 3, 4** | `analysis/ghidra-search-effect-root-keys.txt:47-49` + `search-effect-root-contract.md:45-47` | the only registered `IG_WAVE` totals; 9 keys total | [BINARY] |
| **1** (absent family) | `search-effect-root-contract.md:43,49` | `IG_WAVE1_1` is **unregistered** — a hard native-illegal wave total | [BINARY] |
| **4** | `CONTENTS12_2` title + desc1 (5/5 locales, §2.1) | the original Search wave count | [CONTENTS12_2] |
| **2** | `search-stage.ts:4` | the replica's local wave count — inside the native set | [REPLICA-LOCAL] |

The bound is **renderability, not balance**: 2 and 4 are both legal, 1 is not.
No native literal supplies a value for `max_wave`.

## 2.7 Retractions / corrections forced by this pass

1. **"Invisible at the replica's 2-wave fixture" — CORRECTED** (§2.3). The
   divergence exists on the 2-wave **win** path too (1 box vs 2). It is
   unobserved, not absent.
2. **"Becomes observable only at 4 waves" — CORRECTED.** It becomes observable
   earlier, the first time a Search is **lost partway**. `wave_count = 4` is
   when it becomes *structurally* unavoidable, because only then does a full win
   exceed the current 1-box cap.
3. **Nothing to retract in `search-effect-root-contract.md`.** Its line-51
   wording — "two-wave content is a marked local reconstruction choice
   constrained by original UI support" — is vindicated exactly: the constraint
   it identified is real, native, and its "compatible minimum" of 2 waves is
   inside the registered set.
4. **`search-stage.ts:5-6`'s comment is confirmed correct** and needs no edit.

---

# §3 File log

- **This file (new):**
  `analysis/research/base-stats-visual-hunt/search-balance-divergence-2026-10-05.md`.
- **`polluted-observations.md`: NOT appended.** The parent mirrors. Confirmed
  unread for write purposes in this pass.
- **No other file created, modified or deleted.** No server code, fixture, test,
  OpenAPI text, state file, seed, APK, release, LevelDB, emulator or VM
  operation.

# §4 Limits — what this pass did NOT do

- **No Ghidra run.** All native function-level claims (§1.9, §1.10, §1.11) are
  quoted from **already-saved** artefacts:
  `analysis/ghidra-search-effect-root-keys.txt`,
  `analysis/research/search-effect-root-contract.md`,
  `analysis/native-all-strings.tsv`. No body was decompiled here and no parser
  key order was verified.
- **No test run, no build, no server start.** The line references are from
  reading the source, not from executing it. `tests/search-battle.ts` and
  `tests/guided-search-recruitment.ts` were read for coverage context only.
- **No original balance value recovered.** The replica's `1`/`10` trace
  quantities and `2` waves are local fixtures and remain so.
- **`reward_cnt` / `cleared_explore` semantics unverified.** Field names only;
  the per-battle box count they might carry is unconfirmed, which is the main
  reason this is a recorded divergence and not a fix.
- **Wednesday negative is scoped to weekday logic**, not to all schedule logic:
  the replica does publish arena weekly datetimes (`arena.ts:75-81`), and those
  are a documented local fixture, not a Wednesday gate.
- **Zero coverage credit.** Heroes 1/113, accessories 1/100, monsters 0/22
  unchanged. The broader base-stat goal remains far from its 70% thresholds.
