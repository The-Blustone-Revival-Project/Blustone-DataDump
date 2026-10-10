# Owned Hunter stats and progression: consumer audit

2026-10-08. Read-only source/corpus audit requested by the runtime owner. No
adb, Ghidra, runtime, server, state, APK, economy or progression changes. This
report consumes the existing `base-stats-visual-hunt/STATS-ESTIMATE-2026-10-06.md`
assessment and appendix; it does not reopen visual-stat hunting or web research.

## Finding

The namespace fix establishes actor identity/rendering, not combat balance.
Current ordinary reference stats remain two invented shapes, with 003/004
copying 001 and every ordinary grade repeating the same row. Ordinary Hunter
EXP remains a grade-independent linear 0..2900 curve. These fixtures visibly
differ from the recovered corpus, but neither a loss nor 120 input pairs proves
the correct replacement magnitude or intermediate EXP thresholds.

The existing corpus gives strong evidence for grade-specific EXP-to-max totals,
medium evidence for per-Hunter stat shapes and secondary-stat ladders, and
exact shipped Episode encounter tuples. These are three separate consumers.
No evidence supports raising owned stats merely until CB0102 can be won.

## Current source contract

Source locations are `server-ts/src/bootstrap.ts:55-59,82-93,147-150,185-203,
210,249-255,353` and `server-ts/src/hunter-levels.ts:1-10`.

`ordinaryRankStats` emits five rows, `rank` 1..5, `awk_step:0`, copying every
other field unchanged. There is no per-level stat row in that function. The
comment that native rank arithmetic provides higher-rank scaling must not be
treated as recovered original growth evidence.

For reference 001, and the copied 003/004 rows, each rank has:

```text
hp "1000"; atk "100"; def "50"; spd "100"
crt_chance "5"; crt_dmg "150"; penetration "0"
block_chance "0"; block_dec_dmg "0"
attr_enhance "0"; attr_resist "0"; hp_regen "0"
hp_up "10"; atk_up "1"; def_up "1"
```

002 has the same fields except `atk:"120"`, `def:"40"`, `spd:"110"`.
All stat values above are JSON strings; rank/awk_step are numeric. Equipment
and dialog arrays are empty. Native-recovered role/element binding in source:

- 001: Lantern catalog identity, C001, Fire1/Bomber3; starter base.name is
  `%user_name%`, so visible player-name text alone does not identify a ref row.
- 002: Mowgli, C002, Lightning3/Offense1, under default BLUSTONE_GACHA_CARD.
  An override changes its identity key while retaining this same fixture body;
  this lane has not queried live environment values.
- 003: Nene, C003, Ice2/Defense2; minimum published stat rank1.
- 004: Tyltyl, C004, Fire1/Support4; minimum published stat rank1.

Source new-grant birth policy has 002 rank2, 003 rank3, 004 rank1, 005 rank2,
006 rank1. Existing saves remain unchanged. Community Lantern birth rarity3
does not authorize rewriting existing owned001 rank1.

Each reference uses `fixtureSkillSlots(ref_id)`. The mandatory five native
display slots exist, but original ordinary effects/magnitudes are unresolved;
neutral display rows are not reconstructed combat skills. Their actual source
owner is `skills.ts`, not the recovered Episode skill arrays.

`ordinaryHunterLevels` emits 30 dense rows for each grade1..5:

```text
level = index+1; min_exp = 100*index
upgrade_exp = 100*(index+1); sell_price = 0
index = 0..29
```

Thus cumulative EXP reaching ordinary level30 is 2900 at every grade; level2
starts at100; sacrifice EXP is100 at Lv1 and3000 at Lv30. Neither the 30th
row's `upgrade_exp:3000` nor team/group EXP is the Hunter EXP-to-max total.
The cap30 is community-supported; amounts and grade independence are fixtures.

## Corpus comparison for 001..004

Appendix A contains these 2019 JP archive observations, crosswalked by title,
draw rarity, role and element. Preserve all fields and the source context:

```text
Order: HP ATK DEF | speed crit crit_damage pen block block_reduction
       element_enhance element_resistance hp_regen
001 Lantern, draw3: 1521 1058 653 | 7 14 180 0 14 42 0 0 38
002 Mowgli, draw2: 1624 839 682  | 8 33 200 0 14 42 0 0 41
003 Nene, draw3:   1750 726 864  | 7 14 180 0 33 50 0 0 48
004 Tyltyl, draw1: 1467 679 679  | 7 14 180 0 14 42 0 0 37
```

The appendix assigns 65/MEDIUM to001..003 and75/MEDIUM-HIGH to004. Those
percentages are author estimates, not measured error probabilities. The raw
archive TSV explicitly says `level:"not shown"`, `gear_state:"not established"`.
Its snapshots are2019-10..12, POST the2019-09-05 rebalance. They are external
community page readings, not shipped original GetCard responses; the appendix's
`[ORIGDATA-web]` label must not erase that distinction.

The appendix's approximate Lv1 inference comes from a single051 Lv30/no-gear
anchor and derived compound growth. It does not establish the level of these
four pages. Earlier shape-error prose also calls their magnitude Lv30-ish;
these inconsistent level interpretations cannot be silently resolved by
copying numerals into a live Lv1 reference row. Base-stat strict coverage is
still1/113, and none of001..004 is that one clean anchor.

Exact fixture-versus-observation differences:

- ATK/DEF is2.000 for001/003/004 and3.000 for002, versus archive ratios
  1.620/1.230/0.840/1.000 respectively. Nene's fixture has an offensive split
  despite its recovered defensive identity; Tyltyl has no support split.
- (ATK+DEF)/HP is0.150 or0.160, versus1.125/0.937/0.909/0.926. The fixture
  allocates much less attack plus defense per HP. This is shape evidence;
  multiplying all stats equally cannot repair it.
- SPD100/110 versus7/8 is a large unit/scale disagreement. Trace the native
  speed consumer before interpreting it as attacks per second or replacing it.
- Crit5/150 versus14/180 or33/200; block0/0 versus14/42,33/50; HP regen0
  versus37..48 discard recovered secondary distinctions. Pen0 and element
  enhancement/resistance0 match all four archive observations; do not impose
  generic5/5 priors on these four.
- No archive `hp_up/atk_up/def_up` fields supply original per-level growth.
  Their current10/1/1 cannot become growth coefficients by name alone.

The assessment lists HP-normalized candidate shapes at HP1000:
001 ATK696/DEF429,002517/420,003415/494,004463/463. These are derived ratios
with an explicitly undecided local magnitude, not source-backed base tuples
and not a request to install them. The six-row candidate document expressly
reserves the retune decision for the owner.

## Grade EXP: known endpoint, unknown interior

Assessment3.5 and appendix J agree on community EXP-to-max:

```text
Grade:                 1     2     3     4      5
Corroborated total:   200   400  1200  4800  24000
Current fixture:     2900  2900  2900  2900   2900
Fixture/original:    14.5  7.25  2.42  0.604  0.121
```

The total ladder has3..6 supporting community sources per rung,80/HIGH in
the synthesis, and mathematical shape200×R!. It is a Hunter grade ladder,
not the team/group/veteran EXP curve. The assessment's broad phrase
"contradicted8–14×" is not the exact comparison across every current grade;
the ratios above show direction reverses at grades4/5.

Per-level cumulative thresholds have not been recovered from the seven-corpus
search. The endpoint does not establish linear EXP/29, equal increments,
source-card sacrifice EXP, sell prices or training gold. Installing endpoint
correct but invented interior curves must carry a fixture label. With the
existing same EXP values it can change displayed levels, max EXP, rank-up
eligibility and which sources are exhausted; this requires an explicit
save-preservation/progression policy, not an unnoticed stat-reference edit.

In particular preserving legacy XP100→Lv2 while a grade1 cap is200 leaves
only100 EXP for the remaining28 level thresholds. That is mathematically
possible, but cannot be represented as recovered progression without actual
interior evidence. No existing EXP/rank should be normalized to the new
endpoint simply to obtain a stronger combat party.

## Native consumers: proven boundaries and remaining gap

All addresses below use retained Ghidra coordinates; no new decompilation ran.

1. **Reference identity and parser.** `CSRCardInfoContainer::SetCard87baa4`
   indexes the bare ret_data array, then row.base.id; role, attr and res_prefix
   are independent base fields. row.is_main is read from the row, not base.
   Current source supplies row.is_main (the historical shape audit's missing
   row.is_main claim is superseded). `GetCardStatData87d328` is present in the
   retained function list, but this lane does not have its complete arithmetic
   transitive consumers established. Do not claim that its existence proves
   automatic grade or per-level scaling.
2. **Stat string contract.** `CSRCardStat::parse886fc0` in
   `analysis/native-card-stat.txt` converts string fields through
   from_json<string>/floating_point.create; rank/awk_step use numeric
   conversion. `gem-reference-contract.md` pins the17-field names and mode1
   set-effect caller. The parser's mode-dependent divide/multiply path is
   not itself a recovered ordinary Hunter growth formula.
3. **Level table.** `CSRSyncRef::ReqLevelCBf84c7e` calls
   `CSRUserLV::SetLevel109f114`; `card` rows are rank-keyed numeric
   rank,level,min_exp,upgrade_exp,sell_price, stride16. Native
   `GetCardLevel10a0b2c` walks ordered thresholds; `GetCardMaxLevel10a0c68`
   returns the last level; `GetCardMinExp10a0da0` and
   `GetCardMaxExp10a0d0c` use current/next rows capped to last.
   `CSRCard::SetExp869ea4` derives/caches level from this table.
   `GetCardRaiseExp10a0e34` reads source-level `upgrade_exp`; it is distinct
   from the target cumulative min_exp. Awake curves use separate maps.
4. **Observed ordinary HP.** Prior `in-game-stats.md:298-300,420,444` and
   report017 record ordinary HP1000+hp_up10=1010 on three captures. The
   shape-error report interprets all *_up as flat additions and current
   leveling as stat-neutral. That observed HP equality is solid; extrapolating
   it to every level/grade/field/mode without complete native getter arithmetic
   is weaker. Current source publishes no differing grade stat values, and
   recovered `LEVELING.jet` monster rank rows are not Hunter growth.
5. **Episode fixed actors versus owned fallback.**
   `CSRMEpisode::LoadCombatb17260` binds nonempty actor_id through
   `FindActorRefb1c2ac` and `ParseActorb1bd5c`, using local STAT and an
   Episode-only CardInfo cache. `ParseActor` calls CardStat.parse atb1bfe8.
   `CSRSceneMEpisode::MakeStageInstb23f60` uses prebound refs for fixed
   actor_id, and Inventory.FindCard/SetRefID for empty actor_id owned slots.
   See `episode-first-combat-contract.md` and retained
   `ghidra-episode-combat-actors.txt`. CB0102's left has four empty entries;
   its right has two CB0102_M1 actors and one CB0102_005_1. Updating ordinary
   GetCard must not overwrite the Episode STAT cache.

## What the current loss does and does not prove

AGENTS155 and `testing/card-identity-001/report.md` record the corrected
namespace map, original firstM022 rendering and120 guarded touch pairs.
M022450→298.560181 and Gerard1000→944.800171 show real damage, then native
loss. They do not establish120 attack executions, an exact damage formula,
remaining opponent promotion, a correct skill/input cadence or victory.

Those two initial HP pools match original fixed CB0102 tuples: CB0102_M1
res_idM022 has450/430/180; CB0102_005_1 res_idC005 has1000/280/260,SPD5,
crit20/180,block25/25,regen5. These rows are per-encounter original data.
The appendix's LOW/MEDIUM confidence for them concerns reuse as base stats;
their shipped numerals themselves are exact. Native encounter conditions may
still apply modifiers, so matching initial HP does not close every consumer.

Owned serial1000005 and fixed actor_idCB0102_005_1 are different namespaces.
Current report supplies prep display names/levels and owned serials, not each
owned ref_id; this lane does not infer ref IDs from their trailing digits or
from Captain/Diana labels. Root should retain exact actor ref/resource binding
when relating the party to001..004. This audit does not inspect private state.

## Supported next work

- Close the owned stat selector/final getter chain around87d328, plus SPD and
  *_up consumers, from existing native evidence before inventing a level/rank
  curve. Retain actual reference identity for each actor. The0..2 historical
  order bounds remain the safe bounds from AGENTS.
- Use the recovered grade endpoints as a fidelity target. Design and label
  any missing interior thresholds as replica policy with preserved saved EXP,
  explicit level consequences and native/UI/server parity; never conflate
  Hunter XP with user/group/veteran XP or sacrifice contribution.
- Separate per-Hunter shape/secondary-field fidelity from magnitude. Archive
  identity/era bindings support differentiating001..004, but a proposed final
  row needs an explicit scale/level assumption and a consumer proof. Do not
  layer shared monster-rank or role modifiers onto already differentiated
  archive rows without demonstrating the original caller, to avoid double
  application.
- Audit actual skill availability/effects and damage cadence independently.
  Ordinary effects remain neutral fixtures; original Episode fixed actors have
  their own skills. Current namespace/render success is an appropriate start
  for that investigation, not evidence that stats are the sole reason for loss.

No portal combat-power fit, transcendence multiplier, EVCB1.36 scalar, global
monster retune or victory-conditioned buff is proposed. Story04 remains
uncleared; no host clear, reward, rank, EXP or grant is justified by this report.

Root live binding confirmation: owned1000001/ref001/EXP340,1000002/ref002/
EXP240,1000004/ref003/EXP240,1000005/ref004/EXP840. Recruits1000012..16
ref004/EXP0;1000017/ref003/EXP0. Native corresponding resourcesC001..C004.
Prior Captain/Diana journallabels must not select archive rows; use exact
reference/resource identities. FixedCB0102_005_1Gerard remainsnonowned.

Root original read-only getters now retained in analysis/ghidra-combat-stat-
vip-getters.txt: GetAtk99aef0 reads default actor+8b4/+38 and buffactor+8bc/
+38, upperbuff clamp3 and unresolvedDATlowerclamp, finalATK at least1.
GetDef99b078 uses default+40/buff+40 and upperclamp3, lowerDATunresolved.
GetAtkSpd99af30 uses default+3c×buff+3c withlowerDATthresholdunresolved.
Do not treat noisyFloatVector decompABI lanes orDATlabels as finalconstants.
GetUserVIPLevelb6cc2c delegatesVIPlevel selection using PlayData+150 EXP.
No live stat fields were changed or guessed from these getters.
