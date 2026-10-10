# HANDOFF → server-programming agent (2026-10-08)

**From:** the stats/recovery research lane. **To:** whoever is driving
`server-ts`. **Supersedes `HANDOFF-SERVER-AGENT-2026-10-06.md`** — same
structure, updated with everything learned 2026-10-06 → 2026-10-08
(AGENTS.md §136–§165). Several stat-confidence verdicts have been **raised**
because the client now natively verifies them; the changes are flagged per row.
Honesty rules of `AGENTS.md` §15 still apply: recovered / fixture / unknown
labels stay exact.

---

## 1. Runtime state right now (what you will find)

- **Replica:** wrapper34924 / listener40092, stamp **1634673**, **35 package
  groups** (11 base + 13 Episode + 4 fishing + E01 story04/Bear/final-bg/E02/
  E03 overlays), **82 folded assets**, same instrumented **+12 APK**.
- **Profile:** `BLUSTONE_CARD_STAT_PROFILE=archive-2019-projection` is DEPLOYED
  (§159) — owned hunters 001..004 now carry curated 2019-archive reference
  bases (explicitly LOCAL, page-level/gear/final-version drift unknown).
- **Client:** PID8869 at the **E03 map, Story04 next, no active battle**.
  E03 S01/S02/S03 cleared natively; parent E03 uncleared (3/7 leaves);
  `reward_ids=[E02]` only.
- **Economy snapshot (all natively verified):** gold 11580 · AP50 · VIP EXP 20 ·
  Team EXP 840 (Lv4 curve) · free Manda 239670 / paid 240000 · **70 campaign
  stars** · 10 owned hunters in **namespace 1** (main IDs 1000001/2/4/5,
  recruits 12..17; legacy ID + 1,000,000 bijection, §155).
- **Owned hunter progression (native-verified §156):** 1000001/ref001 EXP340 ·
  1000002/ref002 EXP240 · 1000004/ref003 EXP240 · 1000005/ref004 EXP840.
  Use exact refs for stat identities — earlier journal labels (Captain/Diana)
  were mislabeled for 003/004.
- **Collector is still OFFLINE** — `adb logcat` is the only telemetry oracle.
  Do not touch Docker or its inference endpoint (§165 reaffirms).

## 2. CRITICAL PATH — Episode E03 continuation (Mirage is FIXED)

**Mirage no longer crashes.** §136 shipped `mirage.ts` GetInfo DTOs +
`GetExtra.local_time` (Unix seconds matching `server_utc` — the missing clock
sync input). Native entry renders "Mirage Ruins 0 Level / Left Until Rotation
5 Days", `Clear 25/0` is natively acknowledged, empty Floor 0 renders. The
Oct-6 `uiEndT>=uiCurT` assertion is retired. Still missing (do not claim
playable): mode content, weekly heroes/stairs, actual Mirage battle/rewards,
and GetInfo flag semantics beyond read.

**Current critical path is E03 Story04/05 → CB0302:**
- Story04 `EP0801A`: 15 texts, final "V-Vincent?!" — then prep.
- Story05 `EP0802A`: 20 texts, final "Tyltyl, right now! Go!" — then **CB0302
  Vincent combat** (fixed ally Gerard serial5; original Vincent HP **3000**,
  regen 0 — natively rendered §165).
- Still pending after: C010 Spine body render, C018_SND01 (actual external
  sound name in Vincent's skeleton), ENV7→STI001/ST001 (NOT "ST007" — do not
  invent), S06/S07 and `CUTIN_E0301`.
- Encounter stats are **original and encounter-specific** (§165): E03's M023
  is atk 650/def 160/regen 10 — *distinct from E02's M023*. Denali (CB0301)
  HP 1300. Do not merge same-token rows across chapters; this re-confirms the
  per-appearance model from the stat corpus (Table C).

Guarded-controller rules: `-BeginBattle` opt-in from visually verified prep,
attack bursts at (695,900) promptly with live HUD/stage guards, stop at
settlement/transitions. Injected touches are NOT proof of processed game taps
(§139 lesson). Counters `-1/-1` are legal while fighting — the input guard now
requires started=1, state13c&14==0, pause0, live camp0 hunter, no modal,
neither remain 0 (§154).

## 3. Fishing — entrance earned, settlement blocked on reference data

- Earned gate passed: Red Rock7 got 2 stars (AP50→49), Fishing Open notice,
  original NPC0004 "Calcium Smelt" intro, native `Clear 27/0` acknowledged.
- Tutorial rendered: cast/bobber/bite guides, hook scene, gauge driven to
  100/mode-3 with bounded phase-aware bursts (§142–143: advance at 70%
  guide → wait 1.5 s → positive inputs; live phase reader `--fishing-hook`
  pinned mode/decay/direction).
- **Wire-verified:** native `/fishing/EndWithSell` posts `log_id: "-1"` (signed
  sentinel via `std::to_string(int)`). Existing handler still refuses 2001.
- **Terminal ACK is `27/2`, not 27/1** (§144 corrected): Hook.OnRefresh
  mode-4 requests `RequestClear(27, step2)` and pushes the ordinary
  `CSRPopUpMFishingSuccess`, which requires `fish_id` → `GetItemData`
  reference; a missing reference logs and falls back to DUMMY/zero INFO —
  that is NOT a legitimate original catch. **Do not implement empty-catch
  success.** The original demo fish identity is unrecovered; scoped cache
  scans of all 3 preserved UserData/EtcData snapshots found zero
  `REFEN/REFERENCE/GETITEM` keys (§145 — these 6 containers exhausted).
- Success popup grades 1/2/3 = bronze/silver/gold; length display in
  hundredths cm; result gold is INFO+30, separate from wallet.
- Nothing can settle until an original fish item reference row exists. Fish
  item IDs/pools/prices remain the concrete data dependency; FS001..011 /
  FISH_01..09 are art families only.

## 4. Everything implemented since 2026-10-06 (the Oct-6→08 diff)

| Feature | Source | Native verification |
|---|---|---|
| Mirage GetInfo DTOs + `GetExtra.local_time` clock sync | `mirage.ts`, `game-routes.ts` | **YES** (§136: entry renders, ACK 25/0, no retry assert) |
| Veteran/VIP EXP (`vip_exp` uint32, lobby publication, 20-EXP receipt) | `supply.ts`, `login-bonus.ts` | **YES** (§146/§155: day3+day4 claimed, 100 gold + 20 VIP EXP) |
| Special Supply individual + Collect All settlement | `special-supply.ts` | **YES** (§147: 16 earned rows → +160 gold, panel empties) |
| Mail read + local sender fallback + detail/profile routes + 100×100 PNG portrait | `mail.ts`, assets | **YES** (§148–150: exact native 100×100 size gate, glyph renders) |
| **Owned-ID namespace migration v1** (legacy+1M bijection across roster/decks/snapshots/arena receipt keys/allocator) | `state.ts` | **YES** (§154 serial-collision proof → §155 full party renders M022 correctly) |
| **Archive-2019 stat projection** for owned 001..004 | `bootstrap.ts` profile | **YES** (§159: detail views match native base+up*level) |
| Episode E01 (7 stories + parent) and E02 (8 stories + parent) native clears; FMD1×30 wallet receipt | `episode-progress.ts`, `episode-reward.ts` | **YES** (§162/§164: parent Read + automatic Reward, wallet 239640→239670 in native Shop) |
| E03 materials (13 original packs) + first 3 story clears + CB0301 Denali win | profiles + routes | **YES** (§165) |
| Hunter level-selector semantics (no sentinel; first threshold above EXP → level-1) | docs/comment fixes | **YES** (§157/§158: fixture curve matches native selectors) |
| Nene active-skill activation (SP 10→7.04, cost-3 debit, pause/resume cycle) | native path only | **YES** (§161) — numeric effect damage NOT isolated |

**Deployed-but-unverified (do not claim working):** GC2 coupon redemption
(E01 reward still refuses — client auto-requested RewardE01 and was correctly
refused §162), FMD1 reward icon/thumbnail (blank; `IT_FMD` art exists but the
full GetItem FMD1 row binding is unknown), fishing settlement/catches, Mirage
mode content, gem UI, arena combat, skill effect magnitudes.

## 5. Stat corpus — verdicts RAISED by the last 48 hours

The estimate corpus (`STATS-ESTIMATE-2026-10-06.md`, ~132KB, Tables A–K) is
closed as research, but the live client has since **upgraded several rows**:

| Item | Oct-6 verdict | Now | New evidence |
|---|---|---|---|
| Grade EXP-to-max endpoints 200/400/1200/4800/24000 | 80 · HIGH [COMM×3–6] | **95 · HIGH** | in-client consumer audit §156 corroborates all five endpoints against owned EXP/levels |
| Owned-hunter display stats 001..004 | derived priors only | **native-verified at owned levels**: 001 Lv4 = 1561/1062/657/SPD7 · 002 Lv3 = 1654/842/685/SPD8 · 003 Lv3 = 1780/729/867/SPD7 · 004 Lv9 = 1557/688/688/SPD7 | §159 projection + native BuildTeam/detail parity. Verifies the *pipeline*; per-level growth (+10/+1/+1) and repeated rank rows remain fixtures |
| Episode encounter tuples (Denali, Vincent, chapter-specific M023) | Table C [ORIGDATA] per-appearance | **native-render confirmation**: Denali HP1300, Vincent HP3000/regen0, E03-M023 650/160/10 — observed live in combat §160–§165 | raises Table C encounter rows for CB0301/CB0302/E03-M023 to ~90 · HIGH |
| Wire stat growth contract | [UNKNOWN] | **[NATIVE]**: hp/atk/def/spd at CSRCardStat+18/+28/+38/+8, growth +c8/+d8/+e8; helper = uint32(base+up×level)×multiplier; Validate receives GetStatWithoutEquip | §158 — magnitudes still fixtures, but the formula shape is now proven |
| Attack-speed unit | unresolved | **closed**: actor interval = (1/spd)/atk_spd_bonus → buff → min 0.06 s; LevelData+254 = 0.8 (chunks 9/10/11/12/14) or 1.0 (17), omitted elsewhere | §158 |
| SP/Rage economy | [ORIGDATA] chunk 9 (0.21/s regen etc.) | mode-dependent: live CB0102 groups measured **rate 0.03, max 10**; do not assume chunk-9 values globally | §160/§161 |
| FMD1 = free-Manda identity | policy mapping | **native receipt verified**: E02 auto-reward credited 30 free Manda (239640→239670) | §164 — the ×30 quantity is original; the wallet mapping remains replica policy |
| Grade interior EXP thresholds | unknown | **still unknown** — endpoints only; do not invent interior rows | §156 |

**Unchanged from Oct-6 (still binding):**
- Era rule (2019-09-05 rebalance); archive tuples POST-era; never mix.
- Do-NOT-implement: transcendence ×1.30 / ×1.716 (refuted), CP OLS law as
  validator, `enemy_atk_per 100 = 100%` (never "fix" to 1), MON BLAST!
  cross-title numbers, `hp_page` semantics.
- Must stay fixture: shop prices, arena economy, chest amounts, first-clear
  gold/EXP, gacha pools, login calendar contents, trace thresholds, all
  training gold/XP magnitudes, team-EXP interior rows (fixture still two-row
  0/100 → Team Lv2).
- Owner decisions pending (4 CONTRADICTED rows): A1 skill gold, A3 skill
  materials-from-Lv5 ladder, A4 fragment ladder, E8 trace thresholds; plus new
  metadata decisions: FMD1 item row, GC2 pool/tier, Mirage weekly content.
- The remaining external-data hope is still other revival projects' captures
  and crowd-sourced old-client LevelDB caches (`native-reference-cache-
  candidates.md` scan method; all 6 local containers now exhausted §145).
  No more visual-stat hunts.

## 6. Working preferences — additions since the Oct-6 handoff

7. **Serial collisions are the default danger, not the exception.** Episode
   enemies share the owned-card serial namespace; enemy serial5 once resolved
   to an owned Diana. The namespace-1 bijection (legacy+1M) is the fix — never
   host-edit IDs, never allocate into the Search-helper reserved range
   (≥900000001), preserve 0 sentinels.
8. **Injected touches ≠ processed game taps.** Verify the live HUD/phase with
   the read-only observers (`--episode-scene`, `--fishing-hook`,
   `--combat-tuning`) before and after bursts; input-guard counters −1/−1 are
   legal mid-fight.
9. **Same monster token ≠ same stats.** Chapter-specific tuning is real
   (E02-M023 vs E03-M023); never merge STAT rows across encounters, and do not
   "repair" intended-original visuals (BG000_1 is genuinely 100% black;
   AS1..3 shadow-only is the shared original pattern).
10. **Reward quantity ≠ settlement proof.** HTTP 200 is not a receipt; native
    wallet/panel parity is. GC2/FMD1-style refusals stay until metadata/pool
    rows exist — no inert coupons or substitute grants.
11. **A cleared story's terminal is what advances the parent.** Client parent
    `Read` fires automatically after the last leaf; whole-chapter claims need
    the parent node — E01/E02 verified this end-to-end (§162/§164).
12. Local label mismatches (e.g. combat `stage_name E03_S03_TITLE` during
    Story02) do NOT misroute clears — do not patch original labels or host
    progress to "fix" them.

— end of handoff —