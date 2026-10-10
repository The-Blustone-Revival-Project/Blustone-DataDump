# Tutorial open/input conditions: support timestamp and binding lifecycle

2026-10-04. Read-only original-library Capstone research. No Ghidra, adb,
client/server edits, native calls, hooks, or fresh live state reads. Companion
reports: stage3-input-gate.md and native-live-state-reader.md.

## 1. Correct the PauseAttack hypothesis before interpreting live state

**[RECOVERED]** `PauseAttack(true)` (`0x9863d8`) writes **-1,000,000.0** to
actor.last_attack_time at+0xa68. The literal at `0x986404` is bytes
`002474c9`. This is not a huge positive future deadline.

```text
true  -> last_attack_time = -1000000.0
false -> if last_attack_time <0, set0; else preserve it
```

The false behavior follows `0x9863ea..0x986402`; its zero literal is at
`0x986408`. `CanDash` (`0x98651e`) uses actor.clock-last_attack_time>=interval.
Thus a normal finite clock minus this negative sentinel **passes the manual
cooldown test**. A negative timestamp alone cannot explain manual zero attacks.
Other automatic/update paths may intentionally interpret a negative timestamp
as paused, but their full behavior was not audited here.

Successful `AttackWithoutState` overwrites+0xa68 with its current attack clock
at `0x985a2e`. This is another exact mechanism that leaves the sentinel state;
it does not require /tuto/Clear. No runtime timestamp was measured by this lane.

## 2. Support tutorial deliberately assigns that sentinel to non-monsters

`CSRTutorialSupportSkill::OpenStage` (`0xf103c0`) retrieves an episode combat
record via `CSRMEpisode::GetCombat`. Its combat discriminator at record+0x60
selects OpenMission for0 (`0xf103f8`) or OpenInGameBattle for1 (`0xf10400`).
It then walks **both** actor lists at game+0x17c and game+0x188. For each actor:

```text
IsMonster() true  -> leave it
IsMonster() false -> PauseAttack(true)
```

The calls are `0xf1043a` and `0xf104a4`. Finally it calls SetTutorialInfo at
`0xf104da`. That method creates/finds touch-guide and waiting-root UI objects
and sets a guide byte at this+0x438 to1 (`0xf10a64..0xf10a68`).

This is an **episode-backed support tutorial class**, not evidence that every
campaign n_01_03 instance uses it. The exact game primary vptr and mode must
match before attributing a live sentinel to this setup.

**Factory modes are recovered:** MStageSkill5, Prologue6, MEpisode7,
SupportSkill8. SupportSkill's primary game vptr is loadBias+0x217ac04;
MStageSkill's is+0x2179248. There is no evidence for a distinct
CSRSceneGameTutorial wrapper class in retained strings/symbols or exact ELF
dynsym. A scene vptr mismatch must be identified by its exact runtime RTTI;
do not broaden the reader guard using that presumed class name.

## 3. Input binding has a separate, non-monotonic lifecycle

`IsInputable` (`0x9859b0`) tests actor+0xa6c (shared CSRGameUIIconSkill pointer).
`SetInpuable` (`0x985f8c`) receives a weak CSRGameUISkillPoint:

- Missing/expired weak point at `0x985fd4..0x985fe0` reaches the clear path:
  binding+0xa6c=0 at `0x985fe8`, releases its old control block.
- Valid weak point reaches `0x98603c`; if an existing binding is nonzero,
  `0x986042` branches **back to that clear path**. Do not assume invoking this
  setter twice simply refreshes/retains input.
- When a valid point needs a new binding, it inspects existing components and
  creates/finds CSRGameUIIconSkill, then stores it at+0xa6c at `0x98610c`,
  `0x986166`, or `0x9862a8` depending on the component path.

The sole direct call to this setter found by the whole-library Thumb BL scan
is `MakeFrontActor` at `0x9ddf84`. It obtains the weak point through the game
UI's virtual method+0x6c. A renderable frontline actor is not proof its binding
is nonnull. If the live reader finds a null binding, tracing this setter's
weak point and call count is more useful than changing tutorial pairs blindly.

No direct server response field was recovered to set this pointer. UI resource
coverage and frontend lifecycle can affect it, but neither has been proven to
be the cause of the observed stage3 snapshot.

## 4. Hold is a counter, not an automatic consequence of an empty skill

`IsHoldAttack` reads buff-state+0x98>0. AddBuffHoldAttack at0x99b55e adds a
signed increment to that counter; the only direct call found at0x99ccfc is in
generic buff application. Its sign is selected from the applied buff transition
at0x99ccd4..0x99ccfa. Leaving a hold effect therefore requires balancing that
counter through its buff lifecycle, not toggling card inventory lock.

The published skill fixtures have empty effect collections, so no corresponding
hold-effect record was reconstructed. There is no pinned empty-skill-start
path calling AddBuffHoldAttack. A live positive hold counter would warrant
identifying its applied effect or state writer; an empty effect list alone is
not a verified explanation. Skill animation/cinematic end conditions are not
fully recovered and may have other gates.

## 5. Completion pairs and reference knobs: what is and is not connected

The recovered /tuto/Clear acknowledgement sets the exact echoed pair to3 and
reload Parse restores persisted pairs, as tutorial-clear-contract.md documents.
These pairs are stored in a separate tutorial map. No direct path was pinned
from SetState to clearing actor+0xa6c, buff hold+0x98 or last attack+0xa68.
Clearing a pair can cause a scene's upstream tutorial decision to change,
but that is not the same as directly releasing these attack gates.

Static n_01_03 mapping is GACHA2/GACHA_ACHIEVE10/HOTDEAL_ACHIEVE17; it does
not prove a particular current gate. FIRST_STAGE45 maps n_01_01. Persist
actually completed requests; do not mark45 or all49 types complete based on
the displayed attack hint.

Reference cool_time1000 is divided by1000 in the hunter backend, yielding1sec.
Basic interval is independently reciprocal CalcAtkSpeed divided by level
tuning, with a0.06sec lower bound. These units do not explain126sec of zero
manual attempts with otherwise normal finite clocks. A malformed nonfinite
speed/clock can still affect comparisons and should be reported raw by the
live reader rather than inferred from the wire label.

## 6. Discriminating interpretation of the pending live reader

- Exact SupportSkill mode8/vptr plus negative timestamp: expected setup;
  still inspect pause/state mask, binding, stun/hold to explain rejected taps.
- Null input binding with normal masks: CanDash is never attempted for that
  actor in OnInputProcDash. Focus UI weak-point/frontend lifecycle.
- Positive hold or stun: identify its buff source; do not blame reference
  empty effects without a writer.
- Nonzero game pause mask lacking0x10, or statebyte mask0x14: common press
  suppresses manual dash before reaching actor predicates.
- All gates normal: verify CatchActor/catch pointer routing and whether a
  TryDash/AttackWithoutState event executes; zero damage is different from
  zero attempts, and attack animation events are a further possible seam.

The recorded stage3 gate remains unresolved until live fields discriminate it.
This report establishes precise state transitions, not a speculative fix.

## 7. Recovered active-skill eligibility and effect enum vocabulary

`CSRGameActorGroup::UseSkill` (`0x9a4084`) finds the current-wave actor, reads
GetSkillCost at0x9a40ae and compares it with groupSP+0x2bc at0x9a40b6. It
continues when cost<=SP (`0x9a40c2`), requires CanRunning at0x9a4124, then
calls Actor::UseSkill at0x9a413a. **An empty result vector skips the later
consumption/event path** (`0x9a4142` ->0x9a4160). Therefore effect[] is not
equivalent to a valid damage skill whose numeric magnitude happens to0.

Support tutorial Refresh_Zone_0_Stage_1 (`0xf124aa`) runs its check only when
guidebyte+0x424==1, finds an inputable actor, then reads UI groupSP and requires
**SP >= actor.skill_cost +2** before entering Tutorial_0_2_2 at0xf1256e.
Comparison arithmetic is at0xf1254e..0xf1256a. Cost0 changes this threshold
to2; original cost4 would make it6. This condition is not a basic-attack gate
and should only be applied to a runtime-confirmed SupportSkill instance.

### Effect type and target type are numeric, with exact named dispatch

SRSKILL::ParseEffectType (`0xf2530c`) indexes seven strings, after subtracting1.
Its table is Ghidra0x218bad0, translated with ELF PT_LOAD mapping; entries:

```text
1 Activate   2 Passive   3 Buff   4 Debuff
5 T_Buff     6 T_Debuff  7 Ref_Value
```

SRSKILL::ParseTargetType (`0xf25108`) similarly indexes five names, table
Ghidra0x218babc:

```text
1 ENEMY   2 Self   3 Team   4 Front Ally   5 All Enemy
```

These are recovered enum identities, not proposed convenient numbers.
SRSKILL_INFO::parse consumes effect_type/target_type as scalar integer fields
and asserts when they are0 in a nonempty effect. Strings like "Activate" are
debug descriptions, not proven accepted wire enum values.

SRSKILL::ParseTargetStat (`0xf25134`) directly maps numeric branches:

```text
1 hp change by skill     2 hp max           3 atk
4 def                    5 atk spd         6 crt chance
7 crt dmg                8 penetration     9 block chance
10 block dmg             11 attr enhance   12 attr resist
13 hp regen              14 dmg            15 stun
16 invincible            17 trigger action 18 remove buff
19 remove debuff         20 forced exchange
21 hold attack           22 skill point    23 exchange stop
24 count attack cool     25 buff aura      26 debuff aura
31 DOT_heal              32 DOT_DMG        33 DOT_DMG_STAT
```

Indices27..30 use the error branch. Direct named strings are loaded by the
target-stat branch arms; the byte table beginning0xf25144 pins the mapping.
HP-change1 and damage14 are **different enums**; do not silently equate them.
DOT_DMG32/DOT_DMG_STAT33 identify relevant bleed candidates, but this lane has
not pinned which original002 record chose which. Original bleed duration4sec
and Rage cost3 are community/resource semantics, not a complete effect row.

### Nested parser fields recovered so far

Each entry of skill.effect is an object with numeric:

```text
serial, effect_type, target_type, target_stat,
refer_target_stat, refer_target_type,
base_number, up_number, duration, duration_up, interval
```

and **value_calc** string plus **effect_desc** collection of strings. The
fields are resolved in SRSKILL_INFO::parse (`0xf219ac..0xf22920`); main effect
loop parses effect[index].serial at0xf21c28, effect_type at0xf21c76,
target_type at0xf21ce6, target_stat at0xf21d96. The three enums must be nonzero;
refer_target_stat/type may be0 because they have no equivalent mandatory
nonzero assertions in the inspected reading.

base_number is read as numeric twice into integer/raw-float and normalized
copies (0xf21e9e,0xf21f16); normalization divides100.0 in one copy at0xf21f7c.
up_number likewise has a divided100 copy at0xf21ff0. The parser's constants
at0xf21d1c/0xf21d20 are100.0/1000.0. Multiple duration/interval copies exist
for integer and millisecond-to-second representations. **Do not label all
raw numeric fields as seconds or divide every value by100 server-side.**
The native already makes its internal conversions.

value_calc is converted to a string at0xf2230c. SRSKILL::substitution
(`0xf245f8`) explicitly replaces tokens skill_level, value_up, value, duration,
duration_up. CMTextCalc evaluates the substituted arithmetic in GetValue
(`0xf25338`). The shipped001 expression
`-1*(stat*(8+2*rank))*(value+value_up*skill_level)/10000` is recovered text;
the base/up numeric coefficients that should accompany it remain unknown.

### Candidate implementation boundary

A parser-compatible nonempty active effect can now use recovered enums and
the shipped formula, while labelling its missing numeric magnitude a fixture.
However a faithful direct-hit row still needs **the original target_stat1 vs14,
reference-stat source, and target/immune application rule** pinned. A faithful
bleed row needs32 vs33 and interval/negative-value handling pinned. This lane
does not promote either candidate to a recovered original effect or a tested
combat fix. Do not guess missing enum selections merely because the parser
accepts any nonzero integer.

Restore known original Rage costs4/3 independently if desired, but retain a
single-variable native control for active effects. Validate a nonempty result,
Rage deduction, enemy HP reduction, skill completion and subsequent basic
attacks; absence of parser assertions is not enough to call a skill working.

## 8. Complete nonempty diagnostic effect example, avoiding unresolved formulas

The following is a **parser-ready diagnostic fixture**, using recovered enum
identities Activate1/Enemy1/HP-change-by-skill1. It is not the original Lantern
or Mowgli skill and does not claim immunity penetration, bleed, or working
animation completion. Numeric magnitude50 is **[FIXTURE]**:

```json
{
  "serial": 1,
  "effect_type": 1,
  "target_type": 1,
  "target_stat": 1,
  "refer_target_stat": 0,
  "refer_target_type": 0,
  "base_number": 0,
  "up_number": 0,
  "duration": 0,
  "duration_up": 0,
  "interval": 0,
  "value_calc": "-50",
  "effect_desc": []
}
```

Place the object in the existing type1 outer skill's **effect array**. All
scalar fields above are numbers; value_calc is a string; effect_desc is an
array of strings (empty is a supported collection). A constant arithmetic
expression avoids unknown original coefficients, caller stat selection, rank
substitution and divided100 numeric copies. GetValue's CMTextCalc path at
0xf2538e evaluates the substituted arithmetic. Returning a nonempty effect
does not itself prove a nonempty final skill result or successful HP application;
measure those in the native control.

Zero reference fields have no mandatory nonzero assertions in the inspected
parser. Required effect_type/target_type/target_stat each have a nonzero guard.
The outer skill still needs type/target_rank/name/desc/cost/cool_time/crt_chance/
cut_in_id/icon_id, as card-stat-panel-crash.md documents; do not remove the
other mandatory type2..5 reference records while isolating this experiment.

### What supplies stat, and a separate reference-stat enum

SRSKILL::substitution receives **CSRCardStat const&** from its caller in r1,
the result-effect record in r2, and skill level in r3. It substitutes **stat**
by calling `reference_value(cardStat,effect.refer_target_stat)` at0xf24ad2;
effect field+0xc is the enum argument. This is **SRSKILL_REFER_STAT**, a
different enum from SRSKILL_TARGET_STAT. ParseRefStat (`0xf2508c`) maps:

```text
1 DMG                 2 DMG_DIV_10000     3 DEF
4 HP_MAX              5 hp_remain         6 HP_RECOVERY_NATURAL
7 Atk_spd             8 div_10_attk_spd    9 Crt_Chance
10 CRT_DMG            11 Block_Chance     12 Block_Dmg
```

The table is Ghidra0x218ba80 and uses the same verified PT_LOAD translation.
**Correction to a possible semantic shortcut:** refer_target_stat3 is DEF,
not ATK. Target-stat3 being ATK does not justify using3 as an attack reference.

reference_value (`0xf244c4`) selects float/decimal fields from the **supplied
CSRCardStat**, rather than reading actor+0x38 directly. Ref1 follows the
attack/damage floating value at cardStat+0x28/+0x30; ref2 uses the same value
with an additional division10000. The complete caller path choosing whose
cardStat and applying battle-specific attack scaling remains unpinned here.
Do not claim that stat is already the native actor's final scaled basic damage.

The shipped guide formula also uses **rank**. The inspected substitution
function explicitly resolves skill_level/value/value_up/stat/duration fields,
but the rank variable's complete supply path has not been established by this
lane. Reusing that formula as a live effect before pinning the caller's rank
binding could make an apparently valid expression evaluate incorrectly. The
constant diagnostic above deliberately avoids that unresolved dependency.

Control success requires: a valid native result, actual HP decrease of the
expected fixture quantum, original Rage cost deducted once, skill-end/next
input resumes, and no additional tutorial-state mutation beyond the guide's
actual completion. Preserve unsupported original immunity/bleed claims as
unknown even if the generic HP-change diagnostic works.

## 9. Live mode5 evidence and correction: pause40 is a generic start gate

The read-only snapshot `analysis/testing/revival-005/input-baseline.txt` proves
CSRSceneGame mode5 with exact MStageSkill vptr. At that early sample the mask
is40, state13c=0, caught198=null, Hunter input binding is nonnull, hold/stun=0.
It establishes the common press gate at that instant, **not** that a skill
completion is required to clear40, nor that the same mask persisted126 seconds.

Exact native writer and clear evidence (original library, Thumb addresses):

- `CSRGameBase::OnInit 9c1820`: 9c183c reads this+140;
  9c1844 ORR #40; 9c1848 stores this+140. MStageSkill::OnInit f00d68
  is a tail branch to that function.
- `CSRGameBase::OpenCamp 9d383c`: 9d392e reads this+140;
  9d3936 ORR #40; 9d393a stores this+140.
- `CSRGameBase::OnInitHandle 9cd8a0` registers protocol1a at9cd8da..de.
  Existing instruction-derived protocol table identifies its callback as
  `OnProcGameStart 9cdd0c`.
- `OnProcGameStart` performs playing-time/UI/actor HP visibility setup and
  converges at9ce1d4 (r0=this), 9ce1d6 (r1=40),
  9ce1d8 BL ResumeGame9de3fc. This clear has **no active-skill-result
  prerequisite** in the inspected callback. At9ce102 state bit40 skips
  HP-visibility loops straight to the same clear; it does not skip ResumeGame.
- ResumeGame clears that bit from the same this+140: its write uses an adjusted
  base after `ldr r6,[sl,#2c]!`, so `[sl,#114]` denotes original this+140.

Therefore do not turn the snapshot into a claimed proof of an empty-effect
skill causing this pause mask. The discriminating next observation is a later
snapshot plus receipt of the **native game-start protocol1a callback**. Its
upstream packet-emission timing is not recovered by this report; do not send a
synthetic external packet or patch the pause mask to replace that evidence.

## 10. Why node3 selects mode5 even with cleared tutorial rows

ApplyScene callback eba570 reads current stage at eba5a2 and calls
IsTutorialStage at eba5aa. If true it reads **next stage ID** at eba5c8 and its
achievement count at eba5d0. `clz/lsrs` eba5d8..dc makes r4=1 exactly when that
count is zero. eba5fa branches away when r4=0; otherwise eba5fc sets MODE5
and eba618 constructs CSRSceneGame. The latter scene dispatches mode5 to
MStageSkill at e3cc7c..e3d47c. This selection uses campaign progress rather
than tutorial-state pairs. No owned-card count or specific saved-party test
occurs in this inspected branch. This does not prove there is no later
script-specific roster dependency inside MStageSkill::MakeStageInst.

The static n01_03 GetStageID mapping for GACHA2, GACHA_ACHIEVE10 and
HOTDEAL_ACHIEVE17 explains the map's teammate-guide vocabulary; it is not
proof that runtime scene mode8 SupportSkill was selected. The live vptr rules
that out for this sample.

## 11. Gesture evidence boundary

Common OnProcessPress9db1bc forwards touches to root UI at9db1f4 **before**
reading pause140 at9db1f8. CSRGameUIIconSkill::OnProcessCursorPressa3c178
accepts the press=true case (r3=1), enabled flag+6c=1, and cursor intersection
with its drawable; it changes alpha viaa41920. **This function does not itself
activate a skill**, so root-UI forwarding alone does not prove active skills
can execute under pause40. The battle CatchActor and dash paths follow the
pause gate and are blocked with40 and caught=null.

The legacy draw-side ClickActorSkill9a6958 requires OnClickSkill9a1424,
which tests drawable-visible+270 and cursor intersection with actor+85c;
it pauses the actor and creates skill-view protocol7. Its sole direct callsite
9a95b2 follows parsed click/input boolean=true. This supports a click/press
hit test, but the full connection to this run's Hunter binding and UI gesture
has not been pinned. Do not claim hold/drag/release is mandatory from names
or from the empty skill fixture. A normal tap on the visibly enabled bubble
is a reasonable diagnostic action, with its actual callback/effect outcome
still required as evidence.

## 12. Native enter/start chain and loading discriminator

CSRGameNet::Open a0f4f4 registers protocol0a at a0f55e..562.
Its bound member pointer is loaded via literal slot a0f7e0, add-PC at a0f552,
GOT slot Ghidra21bd25c. The raw word is ELF9ff8ad, Thumb function
Ghidra a0f8ac **OnProcEnter**. Object bases and member pointer values are
checked rather than inferred from adjacent names.

OnProcEnter a0f8ac calls CSRGameBase::StartGame at a0f8c4,
OnProcWaveStart at a0f8ca, then calls GameNet virtual+4c at a0f8e8 with
protocol1a in r1 (a0f8e4), error0 in r3, delay0 on stack. Exact ELF
GameNet vtable214c918 has primary address point214c920; entry+4c at
214c96c contains ELFa0106d, i.e. Thumb Ghidra a1106c **SendLoopback**.
That produces the game-start callback which clears40. This is independent
of the skill-effect result pathway.

OpenMission9d3648 calls OpenCamp9d3670 then dispatches game virtual+98
at9d3792. Both exact primary MStage and MStageSkill vtables point+98 to
ELF9d4d3d -> Ghidra9e4d3c **OnProcLoopBackWaitLoading**.
That callback requeues protocol25 if manager IsLoading is true, or if
input list count at game+184 is zero. Otherwise it emits27 and calls
OpenWaitingArea(1) provided time is not over and state13c bit8 is absent.
Protocol28's Ready handler9d0e3c sets r3=0a then tail-branches to9ce4c4;
the entire ready/animation continuation remains outside this bounded trace.

Additional read-only live discriminator, after verified manager vptr:

```text
faderEnd = u8(manager + 0x673)
managerPhase = u8(manager + 0x32)
IsLoading = (faderEnd == 0) || (managerPhase == 1)
inputCount = u32(game + 0x184)
```

CSRSceneMgr::IsLoading eb4e20 calls CWIPSFader::IsEnd at eb4e28
with manager+58. That getter7bc232 reads byte+61b, therefore combined
manager+673. eb4e2c..40 returns true for unfinished fader or phase1.
The current live input list had two entries, so count0 is unlikely for that
sample, but the count itself should be read to confirm. An unfinished startup
transition/ready chain is a better-supported candidate than an active-skill
completion gate when mask40 persists.

## 13. Combat-coefficient correction (2026-10-04)

Subsequent native combat recovery in `starter-skill-combat-mechanics.md`
retracts §8's formula-only -50 row as a battle-damage example. The parser shape
is valid, but live BuffInfo.ApplyBuff uses the numeric normalized coefficient;
base_number0/up_number0 can produce no combat damage regardless of value_calc.
Use the new report's attack-scaled numeric candidate rows and validation limits.
Target_stat14 is an attack/damage modifier, not a direct HP-hit alternative;
33 is a DOT counter, distinct from periodic HP damage32. Invincible bypass
remains unimplemented/unknown for the original001 row.

## 14. Skill-icon event correction (2026-10-04)

`active-skill-gesture-rage.md` supersedes §11's alpha-only characterization.
a41920 has exact symbol CMEventPool<unsigned char>::Call; OnProcessCursorPress
emits an opacity-derived byte through icon+44. SetInpuable forwards it to
actor+8c4, whose MakeFrontActor listener9f7604 requires255 and then emits skill
reserve protocol10. Actual SetAlpha is a3bc00. Normal opaque-icon press/tap is
the recovered activation gesture. Root UI forwarding before the pause gate can
therefore deliver a skill event; native reserve/background guards still apply.
Actor+a6c is the bound icon component, while+a74/+a78 holds the weak group-SP
UI binding. Prior generic 'input binding' reads of+a6c remain valid for
CanCatch/IsInputable, but it should not be used as the meter object pointer.
