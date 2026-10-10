# HANDOFF → server-programming agent (2026-10-06)

**From:** the stats/recovery research lane. **To:** whoever is driving
`server-ts`. **Read this before your next server change** — it covers (1) what
the live runtime looks like right now, (2) the two open native contracts that
will crash the client if handled naively, (3) everything implemented in source
since 2026-10-05 that you may not have seen, and (4) the completed stat-recovery
corpus: what you can now implement, what must stay a fixture, and what is proven
unrecoverable.

Everything below is backed by files in `analysis/research/` — each section names
its source file. Honesty rules of `AGENTS.md` §15 apply: keep recovered /
fixture / unknown labels exact.

---

## 1. Runtime state right now (what you will find)

- **Replica:** wrapper44592, stamp **1634667**, 28 package groups (11 base +
  13 Episode + 4 fishing), 46 folded assets in E_NEW, persisted state intact.
- **Client:** PID3409 **exited** after the Mirage crash (§135). App stopped,
  no active battle, **AP49**, Red Rock **stage7 uncleared**. Fishing profile
  deployed (§130): 106MB prompt already accepted once.
- **Collector is OFFLINE** (Docker Desktop Inference failure, §132/§135).
  Until it returns, `adb logcat` is the only telemetry oracle; the bounded
  HTTP API (`:8099/v1/events`) will return nothing new. Do not restart Docker
  or touch the failed `dockerInference` reparse point.
- **Live account:** pvid 1000001, 10 hunters, party [2,4,1,5], gold 11160,
  team EXP 660+, campaign stars through Red Rock6 earned (Glacier 6..10 =
  3/2/2/3/2, Red Rock1 = 3), Episode read_ids [S01,E01,E01_S01,E01_S02…],
  login calendar claimed, no host grants anywhere.

## 2. CRITICAL PATH — Mirage `/mirage/GetInfo` (client-crashing contract)

Source: `analysis/research/mirage-native-entry-contract.md` (2026-10-06).
The ordinary Mirage entrance now works natively (NPC0023/Gullveig intro via the
normal `GoTown` path) and the client **sends `/mirage/GetInfo`**. The current
generic success response **kills the client**: `RetryInfo.cpp(58)` asserts
`uiEndT >= uiCurT` and the process exits.

Exact response hierarchy (presence-conditional parsers in success continuation
`G9359ac`; each helper receives its selected subtree, not the full envelope):

| ret_data key | Parser | Notes |
|---|---|---|
| `achievement` | `Achieve.ParseAchievementsElement` | |
| `entry` | `Parse_Entry` 933aec | iterated rows `{id, mirage_remain_hp}`; also calls `Inventory.ResetCardMirageRemainHP` — do NOT synthesize owned-hunter rows from guesses |
| `inst_base` | `Parse_InstBase` 933d80 | keys: `bg_res, dlg_begin, dlg_end, new_record, floor, stair, state, deck, tier_percent, highest, revive_price, begin_ltime` |
| `inst_enemy` | `Parse_InstEnemy` 92dff4 | rows `{n, ref_id, rank, rank_up_cnt, overcome_cnt, exp, skill_1..5_level}`; instantiates **ordinary card refs** — nonempty rows require published card identity/stats/art |
| `ref_stair` | `ParseStairInfo` 9343b4 | keys `{res_prefix, res_postfix_list, list, grade, balance}` |
| `ref_hero` | `ParseHeroInfo` 9347f8 | `{bonus, end_ltime, cur, next}`; `cur`/`next` are **hero-ID string collections** (strict STRING conversion per element), not card records |

**The crash mechanism is now pinned:** `RetryInfo.SetData` (Gc0643c) reads
`CGMTime.GetCurLocalTime()`, then `GetHeroInfo()+0x18` = model+0xb0 = exactly
`ref_hero.end_ltime` (stored 32-bit at 9348ba), and compares the two. Our
generic response omits `ref_hero`, so `end_ltime` is a default/zero field and
the comparison fails → assertion → exit.

**Rules for the fix:**
1. The client clock is synchronized from `/reference/GetExtra.server_utc`
   (already supplied). `end_ltime` must be **coherent with that clock** and
   with the weekly rotation model — do NOT just emit a far-future timestamp
   from the key name.
2. Weekly period / rotation / time coordinates / hero & stair content are
   still unreconstructed. A complete response must satisfy proven consumer
   dependencies, not merely silence one assertion with invented fields.
3. Next read targets if you need more: `RetryInfo.Init` c05554,
   `SetThisWeekHunter` c0589c, model helpers 933d80 / 9343b4 / 9347f8.
4. The request carries flags `reset/stay/entry` + `inst_base/inst_enemy/
   ref_stair_list/ref_hero`; their old interpretation as response objects
   (in `mirage-getinfo.md`) is historical — see the contract file.

Also from §135: the *repeated* "Mirage Ruins Open" notice is not proven to be a
server bug — Village `ResumeTutorials` reads/removes the local `mirage_open`
marker; closing `GoTown` is not a tutorial ACK. No `/tuto/Clear 25` observed.

## 3. Fishing — deployed profile + the entrance gate (do not bypass)

Source: `fishing-airport-earned-gate.md`, `fishing-*-contract.md` files.

- **Entrance gate (native-pinned):** the Airport dialogue variant selects
  NPC0005 (Cruise/Missions/**Fishing**) only when `GetStageAchieveCnt(n_03_07)
  > 0` — i.e. **at least one earned star on Red Rock stage 7**. Zero → NPC0000
  (current account state, matching the observed menu). The `tuto_gacha` marker
  nonzero forces NPC0000 regardless. **No server flag can or should unlock
  this** — it is earned progression. Red Rock7 is the next campaign target.
- Deployed: fishing collection routes `GetInven`/`GetRecord` return **bare
  `ret_data` arrays** (parsers consume the full envelope; bare empty arrays are
  the compatible empty state); all other fishing routes refuse with local 2001
  rather than mocking catches/prices.
- If you implement more fishing later: `RequestPool` receiver reads rows with
  `lure_id`/`fish_id` (lure→fish membership); `/fishing/Begin` response needs
  `{log_id uint32, float32 gauge values, nested min/max ranges}` with
  `first_burn/burn_cool/burn_dur/wait_time`; the client additionally requires
  its **cached `common1` COMMON_INFO** loaded at runtime (client-side
  dependency, already closed on the native side).

## 4. Everything implemented since 2026-10-05 you may not have seen

All in `server-ts/src`, full suite passing; deployment state noted per item.
AGENTS.md §78–§135 are the primary record; the short list:

| Feature | Source file | Native verification |
|---|---|---|
| Loss fuel refund + reservation (`ap_spent`, `ap_refund_cap`) | `mission-complete.ts`, `game.ts` | **YES** (§129: 60→59→60, native loss screen) |
| Completion reservation (standalone `/mission/Complete` = neutral receipt, no payout) | `mission-complete.ts` | host tests only |
| GC2 coupon guard (nonzero/invalid `item_inst_id` refuses; omit/0/"0" only passes) | `game-routes.ts` | route proven native (§118); no GC2 granted |
| Episode read/clear logs + 18 chapter declarations + E02/E05/E18 settlements | `episode-progress.ts`, `episode-reward.ts` | **YES** for stories (E01 cleared, §125–126); reward claims pending native UI |
| E18 RP1→gold receipt, E02 FMD1→30 free Manda | `episode-reward.ts` | policy mapping, native UI pending |
| Fishing collection + resource profile (stamp 1634667) | `fishing-contract.ts` | bootstrap YES (§130); catches/scene unverified |
| Gold calendar preview (RP1 display-only reference, ICON_GOLD→IT_CO) | source + CDN | **YES** (§128, screens 67/68) |
| Mail (read/archive/remove, deletion receipts) | `mail.ts` | native transport verified (§87–88); no live mailbox UI pass yet |
| Special Supply earned gold claims | `special-supply.ts` | host tests only |
| Login bonus calendar (28×100 gold LOCAL fixture) | `login-bonus.ts` | offer view verified; claim pending (§83) |
| Search battle/settlement/repeat/reset + trace exchange | `search-*.ts`, `trace-exchange.ts` | **YES** (§74, §80, §82: funded Search wins, 2/10 traces) |
| Guided Search recruit (37/1 + 10-trace threshold) | `guided-search-recruitment.ts` | threshold gate recovered; native claim pending |
| Gem inventory/reference shapes (authenticated empty arrays) | `gem-contract.ts` | parser shapes [NATIVE]; no jewels owned |
| Arena dedicated routes + GetMyRank rank:1 | `arena-service.ts` | native parser surface; gameplay unverified |
| Team EXP publication (ownedPartyProfile + lobby user.group_exp) | `game.ts` | level-2 derivation native-pinned; popup unverified |
| Hunter battle EXP (decimal-ID map, {prev,cur} absolutes) | `mission-complete.ts` | server award verified §32; result-screen XP pending |

**Deployed-but-unverified list (do not claim these work in-game):** native
Episode chapter reward claims, fishing scene/API behavior, Mail UI, Special
Supply ReceiveAll, login-bonus claim, Arena combat, skill effects (skills
remain inert), gem UI.

## 5. Stat recovery corpus — DONE, and what you can now use

**Deliverable:** `analysis/research/base-stats-visual-hunt/STATS-ESTIMATE-2026-10-06.md`
(~132KB). Appendix tables, every row with numeric `Conf%` (probability the
value is within ±10% of original), a word (HIGH ≥75 / MEDIUM 50–74 / LOW 25–49 /
VERY LOW <25 / CONTESTED), and a notes column. Table map: **A** per-hero stats
(113 rows) · **B** 117 Episode hunter tuples · **C** 34 monster tuples ·
**D** monster catalog · **E/E.2** jewel set bonuses (both shipped versions) +
6 panel samples · **F** multipliers · **G/G.2** per-area + per-stage rewards ·
**H** 18 Episode chapter rewards · **I** original-pixel anchors · **J** 32
price/economy rows · **K** non-card item rows.

**Structural verdict (why the corpus is complete):** no APK version carries
per-entity stat tables — stats were server-side; the 2019 JP archive (the only
external numeric mine) is **proven closed** (0 new rows on re-fetch). ~5,300
numeric data points were ingested. Do not assign anyone more visual-hunting
work; the remaining hope is other revival projects' server captures and
crowd-sourced old client caches (the client provably cached `REFEN/reference/*`
responses in LevelDB — `native-reference-cache-candidates.md` has the scan
method to validate any dump safely).

**Directly implementable now (HIGH/MEDIUM, real sources):**
- **Monster rank multipliers** (LEVELING.jet, [ORIGDATA]): hp **2.6/2.2/1.8/1.4/1.0**,
  atk/def **1.4/1.3/1.2/1.1/1.0** (rank 1→5). Role hp bonuses: Bomber **0.85**,
  Support **0.80**. `atk_camp` 2.0/2.6/1.0. SP economy: first 1.5, regen 0.21/s,
  +2.0/kill, +0.02/attack, max 10. Stage bonus 1.1 ×3 for card 051.
- **`enemy_atk_per`/`enemy_hp_per`: 100 means 100%** — neutral. Proven native;
  never "fix" it to 1.
- **Grade EXP-to-max ladder:** 200/400/1200/4800/24000 (= 200·R!), 3–6 sources
  per rung — supersedes the 2,900 fixture. Per-level compound ≈ ×1.0189
  (per-stat 1.01879/1.01852/1.01930; do not adopt a single g).
- **Hero base tuples:** 62 real 2019-archive rows (Table A, POST-era) + 54
  heroes in Episode data; identity reach 73/113. For the 51 uncovered heroes,
  derived priors are in Table A (HP = rarity median 1537/1624/1750/1955; ATK/DEF
  from role r/s medians — Defense r 0.76, Support 1.00, Offense 1.34, Bomber
  1.55). Mark every derived row LOW.
- **Jewel set bonuses, both versions** (Table E): 1.4.4.1 = HP 5%/AP 5%/DP 5%/
  Crit 4.5%/Block 4.5%/Fatal 50%/SuperBlock 5%(KO 9%)/Element 23/Resist 23/
  Speed 1.72/Regen 30/Pen 12; 2.8.0.1 = 6/6/6/1.72/6/60/35/16/5/10/35/30.
  Super Block is CONTESTED (the shipped client disagrees with itself by locale).
- **Era rule, absolute:** 2019-09-05 rebalance (equipment +50%, crystal mains
  +30%/+50%, substats +50%). Never mix PRE/POST rows without a scale bridge.

**Must stay fixture (do not present as recovered):** all shop prices (AP/BP
refills), arena economy (0/8 rows corroborated — the lowest-confidence system),
chest amounts, first-clear gold/EXP, gacha pools/pity, login calendar contents,
trace threshold absolutes, Raise/SkillUp/RankUp gold values, team EXP per-level
step. Table J carries per-row confidence so this is mechanical.

**Do-NOT-implement list (falsified or portal-derived):** transcendence ×1.30
as a live multiplier (measured, mechanism unproven) and ×1.716 cumulative
(**refuted** 0/9); the CP OLS law as a validator (R²=0.996 but portal-derived,
max residual ~81 cp); `hp_page` semantics (unresolved); MON BLAST! cross-title
monster numbers (different app, quarantined).

**Owner decisions pending (4 CONTRADICTED fixture rows, `fixture-conflict-audit-2026-10-05.md`):**
A1 skill gold formula (100×level vs banded 100–1000), A3 skill materials
(all-zero vs role-material-from-Lv5 ladder — the cleanest conflict), A4
fragment ladder, E8 trace thresholds (10/20 vs 20/40 — shape corroborated,
absolute unrecovered). No retune is recommended by the audit; these are yours
to decide with the user.

## 6. Working preferences that cost us before (§16.7 lessons, still binding)

1. Read the native parser before shaping a response — field names without the
   containing parser's key list produce plausible wrong shapes.
2. Slice logs on a launch marker; a stable metric can be a fact about the
   measurement.
3. `wave_list` is nested `vector<vector<monster>>`; `GetTargetStageMonster` is
   dual-keyed by monster id AND stage id; wave `ref_id` is a monster id.
4. Never attribute a crash by nearest preceding symbol (three `MakeStageInst`
   symbols exist).
5. `result_code: 1` is the native success value; on every path, or the client
   silently retries 8×.
6. The stat tables above are reference material for retuning decisions — blend
   nothing into the Mirage/fishing critical path until those ship.

— end of handoff —