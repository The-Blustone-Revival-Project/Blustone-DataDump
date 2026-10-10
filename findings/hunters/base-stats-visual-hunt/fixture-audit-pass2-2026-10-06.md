# Fixture audit, pass 2 - 2026-10-06

**Purpose.** Second sweep for **fixture contradictions the pass-1 audit
(`fixture-conflict-audit-2026-10-05.md`, 82 rows / 9 systems / 4 CONTRADICTED)
did not cover**. Pass 1's systems were training, campaign economy, Episode,
Search/traces, gacha, AP/BP/supply, arena and battle numerics. This pass goes
after what pass 1 labelled only "UNSUPPORTED", plus the gem surface, plus a
mechanical enumeration of every non-trivial numeric literal in `server-ts/src`.

**Read-only.** Nothing under `server-ts/`, `analysis/recovered-reference/` or any
fixture/bootstrap file was edited, and the build and dev server were not run.
Proof is in section 7.

**Honesty rules used here.** Three verdict classes, kept strictly apart:

- **CONTRADICTED** - recovered evidence (native decompile, shipped original data,
  or a measured on-device capture) states a different value, or the replica's own
  two declarations of the same quantity disagree with each other arithmetically.
  Only these are findings.
- **INTERNALLY INCONSISTENT** - two places inside the replica declare the same
  thing differently, or a published field disagrees with the value the server
  actually uses. No external evidence needed; arithmetic proves it.
- **UNCONSTRAINED** - no evidence bears on it. Reported separately in section 5
  and explicitly *not* counted as a defect. Most economy numbers are here.

"Looks arbitrary to me" is never promoted to a finding.

---

## 0. Method and positive controls

Extraction was mechanical (Python over the TypeScript source and over
`analysis/native-all-strings.tsv`), not impressionistic. Every zero was
discharged with a positive control before being read as a real negative.

| # | Positive control | Result |
|---|---|---|
| PC1 | Route vocabulary parse. Extract every `/word/Word` literal from `native-all-strings.tsv`, then intersect with routes string-quoted in `server-ts/src`. | **261** native literal routes parsed, **96** string-quoted in src, **174** unquoted. Non-zero on both sides, so the extraction demonstrably finds what it claims. |
| PC2 | "Exactly three stat-literal sites in the whole server" (the known `bootstrap.ts:201` defect). | Reproduced: `base_number` / `up_number` / `value_calc` each occur **once**, all in `skills.ts:23-27`. `ordinaryRankStats(` occurs at `bootstrap.ts:57, 90, 147, 201` only. |
| PC3 | Numeric-literal census per file (excluding 0-5, comments, `openapi.ts`, `server.ts`). | `state.ts` 103, `bootstrap.ts` 85, `campaign.ts` 78, `arena.ts` 20, `skills.ts` 19, `game.ts` 17, `search-battle.ts` 15, then the small modules. Every file cited below appears in this census. |
| PC4 | Skill coefficient arithmetic evaluated numerically against the fixture's own `value_calc` strings. | Reproduced the numbers in F2 verbatim from the source strings; no reading step involved. |
| PC5 | Wave-generator identity. `searchStageMonsters()` read as a generator, not run. | `Array.from({length: N}, (_, i) => base.wave_list[0].map(...))` with only `_id` varying -> N clones. Structural, not statistical. |

Scripts were run from `%TEMP%\opencode`; nothing was written into the repo
except this report.

---

## 1. Findings: CONTRADICTED or INTERNALLY INCONSISTENT

Ordered by severity. Each row: what, where, the arithmetic or the evidence,
and the honest bound on impact.

### F1 - Monster difficulty has no axis at all, structurally - SEVERITY HIGH

| | |
|---|---|
| **Where** | `server-ts/src/bootstrap.ts:1292-1330` (`starterMonsterFor`), `:1663-1671` (`stageMonsterRecord`), `:1240-1274` (`FIXTURE_MONSTER_IDS`, `FIXTURE_WAVE_REF_ID`) |
| **Claim** | Every published monster is literally the same encounter, and there is no field in the entire monster reference that could vary per stage or per area. |

Mechanical facts:

- `starterMonsterFor(monsterId)` returns `hp: "100"`, `atk: "10"`, `def: "5"`,
  `level: 1`, `rank: 1`, `crt_dmg: "100"`, `hp_page: "100"`, `penetration: "0"`,
  `block_chance: "0"`, `block_dec_dmg: "0"`, `attr_enhance: "0"`,
  `attr_resist: "0"`, `skill_start_time: 0`, `skill_list: []`,
  `battle_skill_effect: []`. The **only** fields that differ between two
  monsters are the identity strings and `title`. There is no `hp_up`/`atk_up`/
  `def_up` growth field at all - the monster record has no per-rank growth
  columns where the card record does (`bootstrap.ts:90-93`).
- `stageMonsterRecord(stageId)` builds exactly one wave of exactly one monster:
  `const waves: StageWave[][] = [[wave(stageId, FIXTURE_WAVE_REF_ID)]];` and
  `wave()` hardcodes `group: 1`, `next_spawn_ms: 0`.
- `FIXTURE_WAVE_REF_ID = FIXTURE_MONSTER_IDS[0]` and `FIXTURE_MONSTER_IDS`
  defaults to `["M001"]` alone (`:1247`). So all 50 published stages resolve to
  the same single wave with the same single monster.
- `stageRecord` (`:1038-1081`) publishes `enemy_atk_per: 100`,
  `enemy_hp_per: 100`, `ap_cost: 1`, `gold: 10`, `character_exp: 10`,
  `group_exp: 10`, `power: 1`, `title: "First Expedition"`,
  `desc: "Local compatibility test encounter"`, `story_id: ""`,
  `begin_dialog_id: ""`, `end_dialog_id: ""`, `achieve_condition: "[]"`,
  `type: 0`, `value: 0`, `item: []` - **identical for all 50 stages**. The only
  two fields that vary are `id` and `order`. PC3/PC5 verified this by parsing
  the object literal, not by reading it.

**Why this is a finding and not "unsupported".** It is not merely that
monster-HP-100 lacks provenance. It is that the replica has **no mechanism
whatsoever** for difficulty to escalate: no per-stage multiplier (both
percentages are the recovered-neutral 100), no monster level curve (level is
hardcoded 1 with no growth column), and only one monster is even published.
Pass 1 §2.5 recorded the *consequence* ("monster difficulty is a constant, so
per-area escalation does not exist"); pass 2's contribution is the mechanical
proof that it is not merely unpopulated but **unrepresentable** with the current
schema.

**Coupling note for the monster-base agent (not duplicated work).** A separate
agent is deriving monster base candidates from `EPISODE_STAT_ACTORS.json`. Three
couplings must be respected, all of which I am flagging rather than resolving:

1. **Hero ATK and monster HP move together or not at all.** Every recorded
   native win is one tap at 181-272 damage against `enemy_total_hp_max` 100
   (AGENTS §114, §116: `atk_total` 181 and 272 with `enemy_total_hp_max` 100;
   §32: `atk_total` 181). If the §1 candidate hero bases are applied (ATK
   387-696 per hero), a single basic attack becomes roughly 4x-7x the entire
   published monster HP pool, and the campaign degenerates further into one-tap
   clears. **Any monster-HP retune is a joint decision with the hero-base
   change, not an independent one.** Do not move monster HP alone.
2. **The Episode STAT table is not a monster base table.** HANDOFF §6.1: a row
   is a hero row only if `res_id` starts with `C` **and** the matching
   `EPISODE_COMBAT_<id>.json` `left`/`right` entry has `"type": "hunter"`.
   Correct partition is 109 rows / 54 identities, not 117 / 55. Eight rows are
   enemies placed as hunters and three `M*` rows carry hero `ref_id`s. Those
   rows are also **scripted per-encounter tuning**, not a level-1 baseline
   (`EPISODE_COMBAT_STAT.manifest.json` says so), so even a correctly filtered
   Episode stat is not automatically a `bootstrap.ts` `hp/atk/def` row.
3. **Nothing in `server-ts` reads the Episode STAT file today**, so any import
   is a new reference-table decision with its own state-migration question.

### F2 - Active-skill effect magnitudes: the coefficient and the `value_calc` disagree by 10x - SEVERITY HIGH

| | |
|---|---|
| **Where** | `server-ts/src/skills.ts:21-27` (`activeEffect`) |
| **Claim** | The same effect row declares its magnitude twice, in two conventions, and the two disagree. |

PC4 output, evaluating the fixture's own strings literally at owned skill
level 1, rank 1, arbitrary `stat`:

| effect | `base_number`/`up_number` reading (the file's own comment: "coefficient = (base+up*OWNED skill level)/100") | `value_calc` string reading | declared in the comment |
|---|---|---|---|
| 001, 003 direct | `(-95 + -5)/100` = **-1.000** | `-1*(stat*10)*(-100)/10000` = **+0.100 x stat** | "direct100% attack" (= -1.00) |
| 002 bleed | `(-19 + -1)/100` = **-0.200** | `(-1*(stat*10)*(-20)/10000)*5` = **+0.100 x stat** (per tick +0.020) | "bleed20% per tick" |
| 004 heal | `(95 + 5)/100` = **+1.000** | `stat*(100)/100` = **+1.000 x stat** | "heal100% DEF" |

The heal row is internally consistent. **Both damage rows are not:** the
comment's `/100` convention gives -1.000, the shipped `value_calc` gives
**+0.100**, and the sign is opposite. Under the `value_calc` reading, the
direct-damage effect would *heal* for 10% rather than damage for 100%.

Two further internal tensions inside the same three lines:

- **`duration: 4000, interval: 1000` with a hardcoded `*5`.** Ticks at
  `t = 0,1000,2000,3000,4000` inclusive give 5; strictly-before gives 4. The
  `*5` asserts 5. AGENTS §23 wrote "Durations4000ms/interval1000ms yield an
  immediate plus four nominal ticks" - i.e. **five** - so the comment and the
  multiplier agree *with each other*, and the only ambiguity is whether native
  fires a tick exactly at `t == duration`. That is a genuine open question, not
  a contradiction; flagging it so the retune does not silently pick a side.
- **Duration growth is declared zero.** `duration_up: 0` on every row while
  `up_number` grows the coefficient with skill level. So skill level raises
  magnitude but never length. No evidence either way; recorded as a question,
  not a contradiction.

**Severity note.** Whether this is live depends on a question AGENTS §23
already flagged and this audit did **not** settle: `ApplyBuff 0x99eb3c` is
reported to compute the live value from `RefData*storedScalar` *before*
`Apply 0x99c450`, and **not** to evaluate `value_calc` on that path. If
`value_calc` is inert on the live damage path then the practical impact is
zero and the defect is documentation-only. If any other path does evaluate it,
001/003 are inverted. **Either way the row currently states two different
magnitudes, which is the defect.** Do not resolve this by picking one - resolve
it by recovering which field is live.

### F3 - Published inventory capacity `card_inven_max: 100` is enforced on only one of two grant paths - SEVERITY MEDIUM

| | |
|---|---|
| **Where** | published at `server-ts/src/state.ts:784`; enforced at `server-ts/src/trace-exchange.ts:7, 33`; **not enforced** in `server-ts/src/state.ts:1610-1699` (`gachaPremium`) |
| **Claim** | The replica advertises a 100-hunter inventory ceiling and honours it for trace exchange, but the recruitment path grants cards with no ceiling check at all. |

- `state.ts:784` publishes `card_inven_max: 100` in `/lobby/Enter`.
- `trace-exchange.ts:7` `LOCAL_CARD_CAPACITY = 100`, enforced at `:33`
  `if (owned.length + count > LOCAL_CARD_CAPACITY)` - and the comment says
  "Matches the currently advertised lobby capacity". That comment is the only
  thing keeping the two literals equal; they are not derived from one value.
- `gachaPremium` (`state.ts:1610-1699`) checks `FIXTURE_GACHA_CARD_ENABLED`, the
  recruit reference, the price, the guarantee and affordability - **but never
  `owned.length`**. A single accepted 11-draw bundle therefore pushes ownership
  past the advertised 100 with no refusal.

**Why it is a finding.** It is internally inconsistent (one published ceiling,
one enforcing call site, one non-enforcing), and the two 100s are duplicated
literals that can drift. It is not "unsupported" - the contradiction is between
two statements the replica itself makes.

### F4 - Per-stage `group_exp: 10` is advertised but the server pays 30 - SEVERITY MEDIUM

| | |
|---|---|
| **Where** | advertised `server-ts/src/bootstrap.ts:1048`; paid `server-ts/src/state.ts:259, 1951, 1976` |
| **Claim** | The stage record tells the client a stage is worth 10 team EXP; the completion handler credits 30. |

- `bootstrap.ts:1048` `group_exp: 10` on every stage record (PC3: `group_exp: 10`
  occurs exactly once in `src`, at that line).
- `state.ts:259` `FIXTURE_STAGE_CLEAR_EXP = 30`; `:1951`
  `rewardExp = firstClear ? FIXTURE_STAGE_CLEAR_EXP : 0`; `:1976`
  `game.exp += rewardExp`.
- So `ret_data.user.group_exp` advances by 30 for a clear that the stage
  reference advertises as worth 10. Any client-side "rewards for this stage"
  panel reading `stage[].group_exp` displays a third of what is actually paid.

**Adjacent, and worth stating in the same breath.** The neighbouring field
`character_exp: 10` (`bootstrap.ts:1047`) *is* what the hunter EXP loop reads -
`state.ts:1917` `hunterReward = ...character_exp ?? 0` - so that one is
self-consistent. `gold: 10` matches `FIXTURE_STAGE_CLEAR_GOLD = 10`
(`state.ts:258`). **`group_exp` is the only one of the three published economy
fields that the server does not honour as written.** That asymmetry is the
finding; both numbers remain unconstrained fixtures.

### F5 - `card_inven_max` sibling `max_gdp: 100` with `gdp: 0` and no gdp model - SEVERITY LOW

`state.ts:783` publishes `gdp: 0, max_gdp: 100` beside `ap`/`bp`. No `gdp`
field exists anywhere else in `state.ts` (verified: `gdp` appears only at that
line), there is no regeneration, no spend route, and no native parser recovered
for it. Not a contradiction - an unimplemented field pair. Recorded so it is not
mistaken for a modelled resource.

### F6 - Login `level: 30` is a literal with no model, next to a two-row team curve that caps at 2 - SEVERITY LOW

- `state.ts:2066` `level: 30` in `accountSnapshot`.
- Every progression decision instead uses `teamLevel(game.exp)`
  (`team-level.ts:5`, reading `starterLevels.user`), whose table is
  `bootstrap.ts:350` `user: [{min_exp:0},{min_exp:100}]` - **two rows**, so the
  team level is hard-capped at 2.
- So the login response advertises level 30 while the mission/lobby surface can
  never exceed 2. Both are fixtures; the contradiction is that two surfaces
  report different levels for the same account.

Pass 1 §2.5 already flagged the two-row team curve as "the least visible and
most structurally limiting fixture in the economy". Pass 2's addition is the
**direct disagreement with the login `level: 30`** on the other surface.

### F7 - `login_day_count: 0` is permanently zero while the login-bonus calendar advances - SEVERITY LOW

- `state.ts:2065` `login_day_count: 0`, a literal, never updated.
- `login-bonus.ts:24-31` `observeLoginBonus` advances
  `state.eligible` (1..28) on each new UTC day, and `:32`
  `loginBonusInstance` publishes `cur_value: state.eligible`.

Two different notions of "login day" are published and only one of them moves.
No evidence pins which field native reads; recorded as an internal
disagreement, not a value claim.

### F8 - Arena weekly rewards exist in the reference and are unreachable in the state machine - SEVERITY LOW

- `arena.ts:97-98` publishes `weekly_reward: [{min_ranking: 1, max_ranking:
  999999, user_exp: 0, gold: 0, honor: 0, free_iap: 0, item_list: []}]` - a real
  weekly row with every amount zero.
- `arena-service.ts` has **no** weekly-reward path: the only routes handled are
  Enter / FindRival / GetMyRank / BattleStart / BattleComplete
  (`arena-service.ts:22, 29, 32, 33, 56`). `/arena/WeeklyReward` is not in the
  dispatch list at `game-routes.ts:266`, so it falls to the **generic mock**
  (see F10).
- `is_weekly_reward` is published as a hardcoded `0`
  (`arena-service.ts:27`) and `weekly_reward` is never granted.

Not a value contradiction (all amounts are 0 anyway) but a structural gap: a
published reward surface with no reachable claim path.

### F9 - Arena league arithmetic and boundary audit: **no off-by-one found** - SEVERITY NONE (positive result)

This was requested explicitly, so the negative is reported with its evidence.

| Boundary | Local rule | Verdict |
|---|---|---|
| Promotion | `arena-service.ts:84-86`: `if (league_win >= 6 && league_level < 6) { league_level += 1; league_win = 0 } else league_win = min(6, league_win)` | Correct and self-consistent: the counter is **reset** on promotion, and the reference publishes `max_win: 6` for every league (`arena.ts:96`), so 6 wins to advance matches the advertised row. |
| League cap | `arena.ts:34` validation `league_level < 1 \|\| league_level > 6 \|\| league_win > 6` throws | Matches `arena.ts:95` `length: 6`. No reachable state violates it: the only writer clamps at `min(6, ...)`. |
| League 6 terminal | `league_level < 6` guard means league 6 never promotes | `league_win` pins at 6 via the `else` branch. Self-consistent (a terminal league has no next rung). Deliberate, undocumented in the reference row - noted, not flagged. |
| Rating floor | `arena-service.ts:89` `Math.max(0, rating_point - 10)` | Floor at 0; `normalizeArena` (`arena.ts:33`) rejects negatives, so the floor is required, not decorative. |
| Rating/honour overflow | `arena-service.ts:80` guards `win+1`, `rating+10`, `honor+10` as safe integers before mutating | Correct pre-check. |
| BP cost | `arena.ts:7` `ARENA_BP_COST = 1`; debited at `arena-service.ts:43, 46` with a `bp < cost` guard | Once per accepted start, guarded, and the arena receipt deliberately does **not** resync AP/BP (per `arena-battle-contract.md` §38). Matches. |
| BP ceiling reanchor | `arena-service.ts:45` `if (game.bp >= game.max_bp) game.bp_updated_at = now` **before** the debit | Mirrors the AP pattern at `state.ts:1774`. Consistent with `regenerateResources`. |

**One genuine (non-arithmetic) observation.** `arena-service.ts:100-103` builds
the `card` EXP map as `pair(Number(card.exp), Number(card.exp))` - i.e.
`prev === cur`, a deliberate **zero** hunter EXP. Per
`arena-battle-contract.md` §74 that map is parsed **on either outcome**, and
`§66` warns "omitted pair members parse 0 and can destroy displayed progress".
Emitting `prev === cur` for owned serials is the safe form, so this is correct -
but it means the Fight Club EXP axis is inert, which is a fixture decision, not
a bug. Recorded for completeness.

### F10 - Native routes that fall to the generic mock with `result_code: 1` - SEVERITY MEDIUM

| | |
|---|---|
| **Where** | `server-ts/src/game-routes.ts:562-571` (the terminal fallback) |
| **Claim** | **164** native-recovered routes answer with `result_code: 1` and a synthetic body instead of an explicit refusal. **83** of them are state-changing verbs. |

PC1 gave 261 native literal routes; 96 are string-quoted in `src`; 174 are not.
Of the 174, ten are caught by the project's own refusal prefixes
(`/gem/`, `/fishing/`, `/explore/`, `/message/`, `/episode/`) - leaving **164**
that reach the generic mock at `game-routes.ts:562`:

```ts
const data: Record<string, unknown> = { mock: true, route, request_keys: ... };
if (route.startsWith("/reference/")) Object.assign(data, { list: [], items: [] });
if (route.startsWith("/lobby/")) Object.assign(data, { card_list: [], item_list: [], gem_list: [], mission_list: [] });
if (/^\/(gacha|shop|supply)\//.test(route)) Object.assign(data, { result: [], items: [] });
if (/^\/(guild|gvg|arena|relation)\//.test(route)) Object.assign(data, { list: [], users: [] });
return state.envelope(data);
```

`envelope()` pins `result_code: 1` (`state.ts:556-559`). A tightened verb test
(segment does not start with `Get`/`List`, and matches a state-changing verb)
selects **83**, by family: guild 14, relation 12, shop 12, gvg 9, world 8,
mission 5, mirage 4, skin 4, abyss 3, supply 3, arena 2, gym 2, achievement 1,
roulette 1, scenario 1, scheduler 1, tuto 1.

**The shop 12 are the important ones**, because this project has already proven
that a `result_code: 1` mock on a *shop* route is not harmless:
`/shop/SellCard`, `/shop/BuyItem`, `/shop/BuyHotDealItem`,
`/shop/BuyHotDealRequirementItem`, `/shop/SellItem`, `/shop/GachaGeneral`,
`/shop/GachaEvent`, `/shop/GachaSpecificList`, `/shop/IAPAchieveReward`,
`/shop/RewardGachaMileage`, `/shop/Refresh`, `/shop/Reset`. The precedent is in
AGENTS §26: `ret_data.card` absent on a mock response made
`ReqGachaPremiumCB` open the result popup **empty**. That was fixed for
`GachaPremium` only; the other eleven shop verbs keep the same shape.

Also note **`/shop/SellCard` is contract-recovered but unimplemented** (HANDOFF
§3: request `inst_id_list` as a JSON array in one form field; response
`user.gold.cur` absolute plus `item[]{inst_id, ref_id, added}`) and the mock
answers it as a success. That is a recovered contract being answered by a
placeholder.

**Scope limit, stated honestly.** This is a **coverage** finding, not a proven
live defect: none of these 83 routes has been observed to fire on device in any
tester report I read. It matters because the project's own history shows the
failure mode is silent (no assertion, no log), and because a state-changing verb
answering `1` is the one class of mock that can corrupt state silently rather
than merely render empty.

### F11 - Gem: reference routes behave differently from their own siblings - SEVERITY LOW

Direct answer to the requested question ("confirm no route still returns a
generic mock where a refusal is expected"):

- **All five `/reference/GetGem*` tables** -> `state.envelope([])`
  (`game-routes.ts:249-251`). Correct, parser-shaped, empty. No defect.
- **All five `/gem/*` verbs** (`Sell`, `LevelUp`, `PaidGacha`, `MileageGacha`,
  `DailyFreeGacha`) and `/card_handler/EquipGem` -> explicit `2001` refusal
  (`game-routes.ts:252`, `state.ts:1559-1562`). Correct.
- **`/lobby/GetGemInven`** -> authenticated `envelope([])` (`state.ts:1551-1557`).
  Correct.

**The gap is three sibling reference routes plus one lobby route** that the
project never named, so they inherit the generic mock:

| route | source | current answer |
|---|---|---|
| `/reference/GetPaidGemGacha` | `native-all-strings.tsv:01d90113` | generic mock, `result_code: 1` |
| `/reference/GetMileageGemGacha` | `native-all-strings.tsv:01d9012e` | generic mock, `result_code: 1` |
| `/reference/GetDailyFreeGemGacha` | `native-all-strings.tsv:01d9014c` | generic mock, `result_code: 1` |
| `/lobby/GetGemGachaInfo` | `native-all-strings.tsv:01d79d48` | generic mock, `result_code: 1` |

The inconsistency is that the five named `GetGem*` tables return a
**parser-shaped empty array** while these four return a **mock object with a
`route` string and echoed request keys**. If any of the four has a native
parser that indexes a key it does not receive, it reads `null`. Low severity
because no jewel gacha UI has been reached on device.

### F12 - Search waves: N identical clones, and the validator admits a natively illegal total - SEVERITY MEDIUM

Requested explicitly. Two distinct sub-findings.

**(a) The local wave table cannot express a distinct fourth wave.**
`search-stage.ts:12-18`:

```ts
export function searchStageMonsters(): StageMonsterRecord {
  const base = starterStageMonstersByStageId.n_01_01;
  const waves = Array.from({ length: SEARCH_WAVE_COUNT }, (_, index) =>
    base.wave_list[0].map((monster) => ({ ...monster, _id: `${SEARCH_STAGE_ID}_${index}_${monster.ref_id}` })));
  return { ...base, _id: waves, wave_list: waves };
}
```

Every wave is `base.wave_list[0]` with a rewritten `_id`. PC5 confirms it
structurally: **all N waves are byte-identical apart from `_id`**. So
`SEARCH_WAVE_COUNT = 2` (`search-stage.ts:4`) publishes **two clones**, and
raising it to the documented original 4 would publish **four clones** - exactly
the failure mode the prior note warned about, now confirmed at the generator
rather than inferred. The chosen stage, `n_01_01`, is the one with a real
single wave; the search stage was pointed at `n_01_07`
(`hunter-search.ts:9`) but the *monster* record is borrowed from `n_01_01`.

**(b) The persisted-state validator accepts `wave_count === 1`, which native
cannot render.** `search-battle.ts:47`:

```ts
![1, 2, 3, 4].includes(row.wave_count) || ...
```

HANDOFF §4 / AGENTS §74: `InitEffect` registers wave totals **2, 3, 4 only**; a
total-1 family does not exist, which is exactly why the pre-fix single-wave
fixture produced the assertion at 2938. `SEARCH_WAVE_COUNT = 2` is therefore
native-legal and `4` is the documented original - but the **validator's legal
set is `{1,2,3,4}`**, one wider than native's `{2,3,4}`. A hand-edited or
legacy-migrated save with `wave_count: 1` loads cleanly here and would request
a wave family that has no effect registration.

**(c) Migration consequence, checked.** `search-battle.ts:39-40` upgrades only
the *pending* attempt (`row.stage_id` rewritten, `wave_count` set to
`SEARCH_WAVE_COUNT`). A *completed* legacy receipt keeps its own `max_wave`,
and line `:59` requires `receipt.wave.max_wave === attempt.wave_count` - so a
legacy one-wave receipt stays internally consistent and legal-by-this-validator.
The (b) hole is reachable only by a state this replica does not itself write.
Stated so the reader does not over- or under-rate it.

### F13 - Gacha guarantee: satisfiable for every published selection, but only because one card is grade 3 - SEVERITY LOW (documented, no defect)

Requested explicitly: can the pool satisfy the guarantee for every selection?

- `state.ts:1636-1637` picks `guaranteedReference` as the **first**
  `starterReference` entry with `is_main === 0` and
  `(recruitBirthRanks[card.base.id] ?? 1) >= 3`.
- `recruitBirthRanks` (`bootstrap.ts:210`) is `{002:2, 003:3, 004:1, 005:2, 006:1}`.
  Exactly **one** published reference clears the >=3 bar: **003 (Nene)**.
- `state.ts:1639-1640`: `draws = 0` unless
  `(!needsGuarantee || guaranteedReference)`, so an unsatisfiable bundle
  **refuses before charging**. `state.ts:1642-1650` debits only when
  `affordable`, and `affordable` requires `draws > 0`. **No charge-then-refuse
  hole.** Verified by reading the order, not by running it.

So the guarantee is satisfiable, and the refusal path is atomic. Two honest
caveats:

- **Single point of failure.** The guarantee rests entirely on card 003 existing
  with `birth rank 3`. If `003` were ever unpublished, every 11-draw bundle
  would refuse rather than pay out - safe, but the feature would silently
  disappear. `BLUSTONE_RECRUIT_CARD` can already be pointed at 004 (the live
  profile), and 004 is born rank 1, so the live configuration *always* depends
  on the 003 substitution.
- **No odds are published at all**, so "are the published odds self-consistent"
  is not answerable: `gachaPremium` is deterministic. There is no probability
  field in the response. This matches pass 1 F4 (UNSUPPORTED). Recorded so the
  reader does not go looking for a rate table that was never written.

### F14 - Trace award quantity reuses the recruitment threshold - SEVERITY LOW (flagged, not new)

`search-battle.ts:8` `GUIDE_TRACE_QTY = HUNTER_TRACE_ITEMS.find(cardId === "006").collect_qty` = **10**,
and `:214` `const quantity = attempt.guided ? GUIDE_TRACE_QTY : 1`.

One constant, `collect_qty: 10`, is used as **both** the traces required to
recruit Sylvester **and** the traces granted by a guided Search victory. Those
are different quantities with different units. Pass 1 E11 already recorded this
as UNSUPPORTED; pass 2's contribution is the mechanical confirmation that they
are **literally the same expression**, so one future retune of `collect_qty`
silently changes a battle reward. This is the same non-commensurability trap
HANDOFF §5 documents for the `20/100/300` price table.

### F15 - Chest ladder is inverted relative to its own tier names - SEVERITY LOW

| | |
|---|---|
| **Where** | `server-ts/src/bootstrap.ts:522-526` |
| **Claim** | Chest 1 (10 stars) pays the **highest** grade ticket and the most gold; chest 3 (30 stars) pays the lowest. |

```ts
export const FIXTURE_CHEST_ITEMS = [
  { id: "914", title: "*4 Transcendence Ticket", qty: 1, gold: 300 },
  { id: "913", title: "*3 Transcendence Ticket", qty: 1, gold: 200 },
  { id: "912", title: "*2 Transcendence Ticket", qty: 1, gold: 100 },
] as const;
```

Index 0 maps to `achieve_cnt = stageCount * 1` (10), index 2 to
`stageCount * 3` (30). So the **easiest** chest awards the **rarest** ticket
and the **most** gold. Nothing recovered contradicts this - pass 1 C11 rated
the ids CORROBORATED and the amounts UNSUPPORTED - and a descending ladder is a
normal design. But the ordering is the opposite of the intuitive one and it is
paired with `gold: 300/200/100`, so it is worth a deliberate decision rather
than an inherited accident. Recorded as a question, not a defect.

---

## 2. Summary table

| # | Finding | Class | Severity |
|---|---|---|---|
| F1 | Monster difficulty axis does not exist structurally | INTERNALLY INCONSISTENT | HIGH |
| F2 | Skill coefficient vs `value_calc` disagree 10x and in sign | INTERNALLY INCONSISTENT | HIGH |
| F3 | `card_inven_max: 100` unenforced on the gacha path | INTERNALLY INCONSISTENT | MEDIUM |
| F4 | `group_exp: 10` advertised, 30 paid | INTERNALLY INCONSISTENT | MEDIUM |
| F10 | 164 native routes mock-succeed; 83 are state-changing | INTERNALLY INCONSISTENT (coverage gap) | MEDIUM |
| F12 | Search waves are N clones; validator accepts illegal total 1 | INTERNALLY INCONSISTENT | MEDIUM |
| F5 | `gdp` / `max_gdp` published with no model | unimplemented field | LOW |
| F6 | Login `level: 30` vs team level capped at 2 | INTERNALLY INCONSISTENT | LOW |
| F7 | `login_day_count: 0` frozen while the calendar advances | INTERNALLY INCONSISTENT | LOW |
| F8 | Weekly reward row published, unreachable | coverage gap | LOW |
| F11 | 3 gem-gacha reference + 1 lobby route return mocks | INTERNALLY INCONSISTENT | LOW |
| F13 | Gacha guarantee satisfiable; rests on one card | positive result + caveat | LOW |
| F14 | `collect_qty` reused as a battle reward | INTERNALLY INCONSISTENT | LOW |
| F15 | Chest ladder inverted vs its own tier names | question | LOW |
| F9 | Arena/BP boundary audit | **no off-by-one found** | NONE |

Zero of these are "recovered evidence says a different number". They are almost
all the replica disagreeing with itself - which is a cheaper class of defect to
find and a cheaper class to fix, and it is the class pass 1 was not looking for.

---

## 3. What is NOT a finding (explicitly cleared)

So a later reader does not re-raise these:

- **`FIXTURE_MONSTER_IDS` defaulting to `["M001"]` alone** is a **deliberate,
  documented** choice (`bootstrap.ts:1224-1238`), not an oversight. Widening it
  widens the one working battle path. Correct as-is.
- **`group_exp` / `character_exp` / `gold` all being `10`** is not a contradiction
  - only `group_exp` diverges from what is paid (F4). The other two are honoured.
- **`max_win: 6` being identical on all six league rows** (`arena.ts:96`) is
  consistent with the server's promotion rule (F9). It is not required to vary.
- **`SEARCH_WAVE_COUNT = 2` is native-legal.** HANDOFF §4 is explicit:
  `InitEffect` registers 2, 3 and 4. Two is a legal choice, not a bug. Only the
  *validator* being one wider than native is a defect (F12b).
- **`arenaSeason()` using a 604800-second bucket** is documented as a Thursday
  anchor (1970-01-01 was a Thursday) and its counters are inert by design.
- **`rating_point` floor 0 and +/-10** are internally consistent with the
  validator's non-negative requirement.
- **`BASE` hero substitution** (`bootstrap.ts:201`) is **pass-1's** finding,
  already documented in `replica-shape-error-2026-10-05.md` and
  `HANDOFF-to-server-agent.md` §1. Not re-raised here except as the coupling
  partner of F1.

---

## 4. Cross-agent coordination note

A separate agent is deriving monster base candidates from the Episode STAT
table. **Do not let that work and the hero-base change drift apart**: F1 shows
monster HP is published verbatim as `enemy_total_hp_max`, and every recorded
native win is a single tap at 181-272 damage against 100 HP. Changing hero ATK
without changing monster HP (or the reverse) moves the one-tap-clear rate in
one direction only. Whoever owns the retune should treat them as one decision
with two files.

---

## 5. UNCONSTRAINED, not wrong

Listed separately and **excluded from the findings**. Pass 1 already rated most
of these UNSUPPORTED; pass 2 adds the ones pass 1 did not enumerate.

**Monster / stage**
- `hp "100"`, `atk "10"`, `def "5"`, `crt_dmg "100"`, `hp_page "100"`,
  `penetration "0"`, `block_chance "0"`, `block_dec_dmg "0"`, `attr_enhance "0"`,
  `attr_resist "0"`, `level 1`, `rank 1` (`bootstrap.ts:1311-1325`).
- `group: 1`, `next_spawn_ms: 0` (`bootstrap.ts:1653, 1656`).
- `ap_cost 1`, `power 1`, `type 0`, `value 0`, `achieve_condition "[]"`,
  `story_id ""`, `begin_dialog_id ""`, `end_dialog_id ""`, `item []`
  (`bootstrap.ts:1045-1079`).
- Chest `gold 300/200/100`, `qty 1` each (`bootstrap.ts:522-526`) - amounts
  only; the ids are CORROBORATED.
- `FIXTURE_STAGE_CLEAR_GOLD 10`, `FIXTURE_STAGE_CLEAR_EXP 30`,
  `FIXTURE_STAGE_CLEAR_STARS 3` (`state.ts:258-260`) - the **star count** is
  corroborated (three-byte flag); the amounts are not.
- Default visible conditions: "Complete / Under 60s / <=1 Straggler"
  (`progression.ts:25-26`) - the *shape* is corroborated, the thresholds are not.

**Resources / shop**
- `RESOURCE_REFRESH_SECONDS = { ap: 300, bp: 1800 }` (`game.ts:436`); units are
  corroborated, intervals are not.
- `max_ap 50`, `max_bp 10`, `gold 10_000` (`game.ts:262-268`).
- AP `+10`, BP `+5`, `5` Manda / `100` gold, shared `buy_limit 3`
  (`shop-fuel.ts:4-9`) - the *shared-limit shape* is corroborated by
  `UpdateText`; the numbers are not.
- Free Supply `+10` AP once per UTC day, `00:00`-`23:59` (`supply.ts:5-6`).
- Login bonus `28` days x `100` gold, `cycle: 1` (`login-bonus.ts:4-5`).

**Arena**
- `ARENA_BP_COST 1` (`arena.ts:7`); honour `+10`, rating `+/-10`
  (`arena-service.ts:83, 89`); rival refresh `price 100 / type 2`
  (`arena-service.ts:9`); synthetic rival pvid `9_000_001`, instance
  `9_000_001_001`, `card_book` all zeros, `user_exp 0`, `vip_exp 0`
  (`arena.ts:5, 82-92`); all six league rows and the weekly row have every
  amount `0` (`arena.ts:95-98`); `rank: 1`, `season_no: 1`, `weekly_no: 1`
  (`arena.ts:67`).

**Search**
- `cost 1`, `max_join_cnt 1`, `max_play_cnt 1`, `max_retry_cnt 1`, `period 3600`
  (`hunter-search.ts:16`); retry `10` Manda, reset `30` Manda
  (`hunter-search.ts:22`); ordinary trace award `1` (`search-battle.ts:214`);
  helper serial `900_000_001` (`search-helpers.ts:5`).

**Traces**
- `collect_qty` 10 (006) / 20 (005) (`hunter-traces.ts:9-10`); navigation
  thresholds 20/10; one trace per victory. Pass 1 §2.3 already ruled the
  factor-2 claim **NOT UPHELD**; nothing here reopens it.

**Training / progression**
- `trainingPrices.level [100]`, `.rank [1000]` (`training.ts:5`);
  `stat_bonus 5` (`training.ts:10`); `min_exp 100*index`,
  `upgrade_exp 100*(index+1)`, `sell_price 0` (`hunter-levels.ts:8-9`); skill
  `gold 100*(index+1)`, all `source_N_qty 0` (`skill-training.ts:20-23`);
  `LOGIN_BONUS_*`; `GACHA_STARTING_BALANCE 300_000` (`game.ts:310`).
  Pass 1 A1/A3/A4 CONTRADICTED the skill price formula and the zero materials -
  **not re-raised**, they are pass 1's.
- `TUTORIAL_SWEEP_TYPES 8`, `TUTORIAL_SWEEP_STEPS 6` (`game.ts:233-234`).
- `DEFAULT_MISSION_START_IDEMPOTENCY_SECONDS 30` (`state.ts:209`) - declared a
  policy decision in AGENTS §16.2.
- `LOCAL_CARD_CAPACITY 100` (`trace-exchange.ts:7`) - the *enforcement* is
  F3; the *number* is unconstrained.

---

## 6. Limits of this audit

- **No route was exercised.** F10 and F11 are read off the dispatch table. No
  tester report in AGENTS §13-§127 shows any of the 83 verbs firing, so I
  cannot claim a live defect - only a coverage gap with a proven failure mode.
- **I did not re-derive anything native.** Every native citation here is
  second-hand from AGENTS.md, HANDOFF §3/§4/§5, or
  `analysis/research/arena-battle-contract.md`. I did not open Ghidra. Where I
  quote a native constraint (the `InitEffect` wave-total set, the arena result
  pair hierarchy, `UpdateText`'s shared buy limit) I attribute the source
  rather than vouching for it independently.
- **I did not touch the Episode STAT table** (F1 coordination note only).
- **"82 rows / 9 systems" of pass 1 was not re-derived.** Pass 2 is additive;
  where I touch a pass-1 row I say so and do not restate its verdict.
- **`polluted-observations.md` was not appended**, per instruction. Nothing in
  this audit is a base-stat observation anyway: zero coverage effect on
  heroes 1/113, accessories 1/100, monsters 0/22.
- **No numeric retune is recommended anywhere in this file.** Every finding is a
  statement about evidence or about internal disagreement.

---

## 7. Read-only confirmation

- **Edits made: one file, this report.** All extraction scripts were written to
  `%TEMP%\opencode\` and executed from there.
- **`server-ts/`:** `git status --porcelain -- server-ts` returned **0 lines at
  the start of this audit** and **2 lines at the end**. The two are
  `M server-ts/src/hunter-traces.ts` and `M server-ts/tests/hunter-traces.ts` -
  the other agent's active work (the `GOLD_DISPLAY_REFERENCE` addition), which
  appeared *while I was auditing*. **I authored neither.** The whole worktree
  was already dirty before I started (**869 porcelain lines at HEAD `6c632f2`**,
  888 after, the delta being the other agent's two files plus untracked
  research material).
- **`analysis/recovered-reference/`:** `git status --porcelain` returned
  **0 lines** throughout.
- **Not run:** `npm run build`, `npm test`, `npm run dev`. No server started.
  No emulator, no adb, no APK, no Ghidra, no state file touched.
- **Encoding:** written via the `write` tool as UTF-8. Verified after write:
  U+FFFD = 0, CRLF = 0 (see the verification output appended below).