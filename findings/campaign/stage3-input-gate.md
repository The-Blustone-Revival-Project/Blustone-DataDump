# Stage3 zero player attacks: exact native input gates

2026-10-03. Read-only original-library Capstone research and visual inspection
of `analysis/testing/revival-005/01-stage3-afterattacks.png`. No Ghidra, adb,
server/client edits, live instrumentation, or new runtime control.

## Finding and limit

**[RECOVERED]** Taps reach a multi-gate native path. No recovered response field
directly enables basic attacks, and clearing an arbitrary tutorial pair is not
a demonstrated solution. Tutorial-class press processing does not simply eat
all taps: it forwards to the common game's press method.

The remaining uncertainty is **which gate was false in the recorded stage3
runtime**. Native instruction inspection establishes the exact candidate state
fields below; the screenshot and zero attack count cannot distinguish them.
Do not claim this is a confirmed FIRST_STAGE flag defect.

## 1. The tutorial press handler forwards to normal input

`CSRTutorialMStageSkill::OnProcessPress` (`0xeffe54`) checks an overlay/drawable
pointer at this+0x444 and its flag+0x270, maintains recent press timestamps,
then both paths converge at:

```text
00efff08 mov r0,this
00efff0a mov r1,touch
00efff0c bl CSRGameBase::OnProcessPress (0x9db1bc)
```

The alternative branch at `0xefff26` manipulates that timestamp list and
returns to the same forwarding point (`0xefffce`). A visible guide overlay
therefore does not establish that the tutorial press override swallowed input.

## 2. Common press gates, before actors are considered

`CSRGameBase::OnProcessPress` first forwards the touch to the root UI's
ProcessCursorPress (`0x9db1f4`), so buttons/overlays and game input coexist.
It reads touch kind at touch+0x20; value1 is the press path.

Its game-state gates are:

- **Pause mask this+0x140:** nonzero without bit0x10 enters the suppressed
  input branch (`0x9db1f8..0x9db202`). `PauseGame` (`0x9c20b8`) ORs a
  requested pause type into this exact mask (`0x9c20d4..0x9c20da`).
- **State byte this+0x13c:** bits0x14 suppress ordinary attack input
  (`0x9db204..0x9db20c`). Their complete named enum interpretation is unknown.
- **Catch/exchange pointer this+0x198:** if present, the press follows the
  exchange/catch flow rather than an ordinary dash (`0x9db23a..0x9db24c`).
- **CatchActor(touch)** may claim the touch at `0x9db246`; if so it skips dash.

Otherwise the method eventually calls **OnInputProcDash** at `0x9db2f8`.
Press coordinates alone do not bypass these gates. The padlocked AUTO/speed
controls do not identify which gate is active; those are separate feature UI.

## 3. Actor gates: input binding, cooldown, stun, hold

`OnInputProcDash` (`0x9d2f68`) walks the native input-actor list this+0x17c,
then calls TryDash only when both predicates pass:

```text
009d2fa2 bl CSRGameActor::IsInputable
009d2fa6 cbz result,skipActor
009d2faa bl CSRGameActor::CanDash
009d2fae cbz result,skipActor
009d2fce bl CSRGameBase::TryDash
```

**IsInputable** (`0x9859b0`) simply tests **actor+0xa6c != null**. This is a
shared UI skill-icon/binding object, not a tutorial type or a server numeric
attack-enable field. `SetInpuable` (`0x985f8c`, native spelling) receives a
weak CSRGameUISkillPoint; an expired/missing weak pointer clears+0xa6c at
`0x985fe8`. A valid point creates/fetches CSRGameUIIconSkill and stores the
binding at `0x986166` / `0x9862a8`.

The common frontend factory `MakeFrontActor` (`0x9ddc3c`) obtains that point
from game UI+0x20c through virtual method+0x6c at `0x9ddf74..0x9ddf7e`, then
passes it to SetInpuable at `0x9ddf84` for the applicable actor camp/condition.
Thus a valid rendered front actor can still have a missing input binding.
No missing binding was measured in this runtime; it is a concrete native gate.

**CanDash** (`0x98651e`) requires:

```text
actor.clock(+0x228) - actor.last_attack_time(+0xa68) >= GetAtkSpd()
AND not IsStun()
AND not IsHoldAttack()
```

Cooldown test `0x986528..0x98654a`; stun test `0x98654e`; hold test
`0x98655e`. IsStun (`0x99b168`) is buff-state+0x94 >0; IsHoldAttack
(`0x99b17a`) is buff-state+0x98 >0. The buff-state pointer is actor+0x8bc.
Do not confuse attack cooldown/hold with card inventory lock; inventory lock
only protects destruction and is not read in this basic-attack path.

**TryDash** (`0x9d2c18`) calls `AttackWithoutState` at `0x9d2c4a` immediately
after locking the supplied actor. The late steps iterate animation/machine
events. The decisive point to distinguish zero player attempts is whether
execution reaches that AttackWithoutState call at all.

## 4. Tutorial scene identity is a separate mode selector

`CSRSceneGame::OnInit` (`0xe3c9a8`) selects its game subclass by stored
**CSRGameBase::MODE**, via a9-way branch table at `0xe3c9dc`.
**mode5** selects `CSRTutorialMStageSkill` (factory call `0xe3cc84`);
the ordinary default path creates CSRMStage at `0xe3ca96`.
This factory does not itself read tuto rows or stage_id. A stage string alone
cannot prove the recorded game used mode5; the upstream chosen mode matters.

`CSRTutorialMStageSkill::InitBeforeOpen` (`0xefd954`) loads its own level-data
resource and UI bindings, distinct from the normal stage's initialization.
Its constructor initializes internal guide stage this+0x408 to0 and multiple
guide-state bytes to0 (`0xefd78c..0xefd7c4`). Its Tutorial_1_1_1 method only
runs for internal guide stage1 and an unset guide byte+0x415
(`0xf005e4..0xf005f4`). These fields are not directly the wire type/step values.

Earlier tutorial-clear research establishes n_01_03 maps to GACHA2,
GACHA_ACHIEVE10,HOTDEAL_ACHIEVE17 in StaticData::GetStageID; FIRST_STAGE45
maps n_01_01. Neither mapping proves a basic-attack gate. Persist actual
completed clear pairs; do not mark45 complete to make unrelated input work.

## 5. Screenshot evidence and next discriminating control

The supplied screenshot shows Mowgli as the frontline character and Lantern
in the airship, so the role-correct party is visible. It shows a0 attack-count
speech bubble, enemy100 x100, rage0, and padlocked AUTO/speed. The top strip
is fever guidance. There is no visible giant modal sheet in this image; that
does not prove the UI event system or pause flags are inactive.

The next control must establish, in order:

1. Chosen game mode (ordinary CSRMStage vs mode5 tutorial skill subclass).
2. Game pause mask+0x140, state-byte mask+0x13c, catch pointer+0x198 when a
   press is delivered; whether CatchActor consumes it.
3. Input-actor list membership and actor+0xa6c binding validity.
4. CanDash cooldown/stun/hold values; whether TryDash/AttackWithoutState fires.

Read existing telemetry for these facts first. If unavailable, fresh targeted
instrumentation would require a copied instrumented library/client and the
mandated release workflow; this research lane did not perform that action.
Repeated blind tap bursts or arbitrary pre-cleared tutorial sweeps would not
identify the missing gate and risk changing several variables simultaneously.

The zero player attack outcome is an unresolved native input defect, not a
proved missing server stats/reward field or permission to claim playable stage3.

## 6. Empty skill effects, hold, and cooldown hypotheses

`AddBuffHoldAttack` (`0x99b55e`) adds its argument to buff-state+0x98, a
counter. A whole-library direct-call scan found its caller at `0x99ccfc` in
the generic buff-application machinery. No direct "skill starts -> hold++"
call was found. Empty reference effect arrays skip their effect parser and
yield no reconstructed hold buff. This **weakens**, but does not universally
disprove, the hypothesis that the inert active skill holds basic attacks.
Other state/animation callbacks may behave differently and were not fully
audited. Cost0/cool0 and missing cut-in effects do not by themselves establish
that the active skill is harmless; do not claim one from the other.

`PauseAttack` (`0x9863d8`) is **a different mechanism**: it writes the cached
last-attack timestamp+0xa68 with a sentinel when enabled, rather than changing
the hold-buff counter. The direct-call scan found callers at `0xf1043a` and
`0xf104a4`, in the support tutorial class region. This is not a proved call
from the mode5 MStageSkill tutorial. Do not conflate PauseAttack and hold buffs.

**[RECOVERED] cooldown units:** hunter MakeBackEndActor
(`0x9ac2ac`) calls Analyzer::GetCoolTime at `0x9ac64e`, converts its integer
to float and divides **1000.0** at `0x9ac662`. That literal is at `0x9ac630`,
bytes representing1000.0. Thus a getter result1000 represents1second in that
path, not1000seconds.

Basic attack interval is computed separately: Analyzer::CalcAtkSpeed at
`0x9ac7ac`, reciprocal1/speed at `0x9ac7c8`, divided by level-data tuning
at+0x254 (`0x9ac7e4`/`0x9ac81a`), stored in default stat+0x3c.
`GetAtkSpd` (`0x99af30`) multiplies that interval by its buff interval factor
and clamps to a minimum **0.06seconds** (`0x99af44..0x99af52`, literal at
`0x99af5c`). Therefore speed100 tends toward a fast/minimum interval; it does
not itself imply a126second attack lock. Original speed/economy values remain
fixtures, but this particular units hypothesis does not explain zero attempts.

For a discriminating server-side reference experiment, preserve party, stage,
enemy and tutorial state and change only the active skill's availability using
a **recovered** level/rank eligibility rule; verify the native UI reflects it.
This lane did not recover a safe arbitrary disable flag, so it does not propose
deleting the five mandatory skill records (that restores the card-popup crash)
or guessing a client mask. Runtime measurements of the four gates in §5 are
more decisive than altering multiple skill fields at once.
