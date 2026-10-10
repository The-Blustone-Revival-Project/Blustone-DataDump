# Active skills: native press gesture, eligibility and Rage generation

2026-10-04. Offline native/reference inspection only; no adb/Ghidra/source or
client edits. Practical purpose: test the reconstructed numeric effects using
ordinary native input, with the correct role position and actual Rage evidence.

## Gesture and correction to the earlier alpha-only hypothesis

**Press/tap the visible, fully opaque skill icon/bubble.** No hold, drag or
release duration is required by this inspected activation path. Hunter swapping
uses a different capture/door/release gesture; do not use that as a skill test.

CSRGameUIIconSkill::OnProcessCursorPressa3c178 requires press=true (r3=1),
icon enabled byte+6c=1, and cursor intersection with its drawable+60 bound
(a3c18c..19e). It obtains drawable opacity at a3c1a4 and emits an opacity-scaled
byte through **CMEventPool<h>::Call a41920**, icon+44, at a3c1c4.
The previous report's characterization of this as merely changing alpha was
incorrect: a41920 is an event dispatcher, corroborated by its exact symbol and
its std::function<void(unsigned char)> call-loop. Actual SetAlpha is a3bc00.

SetInpuable985f8c finds the icon component and binds its event+44 at9861d8..256
through a callback into actor event+8c4. The thunk98dcce forwards the supplied
byte to that event. MakeFrontActor9ddc3c registers its listener on actor+8c4
at9ddfac..de020; exact closure virtual-call entry is9f7604.

That listener requires actor.IsSkillEnabled97ecba (actor byte+a7d) and the
received byte exactly255 (9f7640..4a). Otherwise it shows a localized refusal.
After combat/target checks it sends native **protocol10** via GameNet+48
at9f7a46..52, then calls game.ActivateSkill9dcbe0 at9f7a58.

## Frontline versus airship roles

Actor.OnRefresh97d1f8 gets source group's displayed SP through
CSRGameUISkillPoint::GetSPa3d47c, using actor.GetGroupID (97d6c4..cc).
If SP is below the actor's cost or the actor is stunned, it hides the icon
(97d6d8..f2). Exchange/global-skill cooldown logic also delays readiness.

SRCanUseSkillAirShip10ae4b0 returns true exactly for **role3 Bomber /4 Support**.
If such an actor is in native state3,4 or8, OnRefresh sets icon alpha128
(97d7b0..ce). Their listener then rejects activation because128!=255.
Use Lantern/Tyltyl from their eligible rear/airship position with an opaque
icon, rather than putting them at the front and treating its dim icon as ready.
This is numeric native role/state evidence, not just community terminology.

For role1 Offense /2 Defense the listener can select the active front serial
for an automatic exchange before reserving the clicked hunter's skill.
It constructs packet **who=clicked actor serial**, **exchange=front serial**:
9f79d2 literalG1d6973c "who";9f7a0c literalG1d7447b "exchange".
Supporter roles skip that front-serial exchange branch (9f78c6..d0).
GameNet::OnProcSkillReservea0ff0c calls OnExchangeImmediatly at a100f0 when
appropriate, then ReserveSkill9e6910 at a10104. Prefer an already-front
Mowgli for the first damage test to remove that extra exchange dependency.

The listener also checks relevant same/enemy-camp input actors, enemy visible
intersection and front stun. An opaque icon outside an active enemy encounter
may still be rejected. It does not directly check the game pause140 mask;
common root-UI forwarding before the manual attack gate permits the event to
be delivered. The reserve handler rejects an existing reserve and
IsBGPaused(8) at a0ffb4..bc; this is background object's pause field+278,
not a simple synonym for game pause140. Do not patch either mask for testing.

## Cost and nonempty result requirement

GetSkillCost99b12e reads actor default-stat pointer+8b4, float member+48.
Hunter construction selects reference skill slot1 at9acf12, checks its
eligibility rank and copies integer reference cost into that float at
9acf28..32. Native UI and backend therefore compare the same Rage units;
there is no division100 or1000 for this cost.

Recovered shipped slot1 costs:

```text
001 Lantern Bomber:4     002 Mowgli Offense:3
003 Nene Defense:3       004 Tyltyl Support:4
```

001/002 evidence isstarter-active-skills.md;003/004 verbatim slot1 EN entries
are in their card catalogue dossiers. This does not recover damage magnitudes.

Group::UseSkill9a4084 requires cost<=group SP at9a40ae..ba, a running/alive
actor at9a4124..28, then invokes Actor.UseSkill981910 at9a413a.
**It subtracts cost only when the returned effect list is nonempty**:
9a4142 empty-list test;9a4148 cost getter;9a4154 subtraction;9a4158 SP store.
ReserveSkill9e6a96..9c also rejects an empty returned effect list.
Consequently empty effect[] is a concrete reason that a visible tap produces
no valid reserved result or Rage debit. A formula string alone with zero
numeric coefficient is not a valid damage test; use the numeric rows from
starter-skill-combat-mechanics.md and retain their original-mechanic limits.

## Rage/SP state and generation

Group runtime layout and exact arithmetic:

```text
+2bc currentSP(float)  +2c0 recoveryPerSecond(float)  +2c4 maxSP(float)
```

AddSkillPoint9a43b0 adds delta, clamps to0/max and stores+2bc.
OnRefresh9a5760 computes current + recoveryPerSecond*group.deltaTime(+22c),
then clamps0/max. This is native active game time, not an external wall clock.
SetSkillPointOption9a43a8 stores the pair. MakeCamp9d3b10 reads rate from
LevelData+228 and9d3b38 reads max from+218 before SetSkillPointOption9d3b3e.
StartGame9e5fb4 resets group SP, reads GetCampParam(camp)+20 and adds initial
SP at9e60b0; that field is first_sp in the level tuning.

OnDamange9e0530 finds the source backend actor from DamageResult serial
at9e070c..14, resolves its group, then:

- if resulting target HP==0 (+10 of DAMAGE_RESULT), GetChargeSPByKill99b14e
  at9e085a supplies the delta;
- otherwise GetChargeSPByAtk99b13e at9e0882 supplies the delta;
- AddSkillPoint9a43b0 is invoked at9e088a on that **source group**.

Thus this path awards Rage for actual eligible delivered damage/kill events,
not every screen tap or attack animation. The earlier predicate excludes
nonpositive damage, and excludes nonlethal target_stat1/skill HP-change events
from this charge path (9e06e2..0706). Do not assume all skill/DOT damage charges
identically to normal manual attacks without a measured control.

Charge getters read source actor default-stat+70 (attack),+78 (kill).
Hunter construction copies these from LevelData+220 and+21c respectively
(9ac8ce..d4 and9ac94e..54); damage-charge tuning+224 goes to stat+74.
The inspected victim charge-by-damage branch99b146 at9e0698 leads to UI SP
refresh, but a separate victim SP delta addition was not pinned here. Do not
claim its configured0.01 is observed per incoming hit solely from its name.

One preserved **original LEVELING chunk9** has:

```text
sp_max10; sp_increase_spd_per_sec0.21;
sp_increase_per_atk0.02; sp_increase_per_kill2.0;
sp_increase_per_dmg0.01;
left.first_sp1.5; right.first_sp1.45
```

These are recovered resource values inanalysis/in-game-stats/leveling-chunk09.json,
not a guarantee that the current scene selected that exact chunk or tuning.
At rate0.21 from1.5, cost3 is reached after about7.15 active seconds and cost4
after11.91 without hits. Actual live SP/opaque icon should determine readiness.

## Actionable native effect control

Use a normal enemy encounter with Mowgli at the front and Lantern/Tyltyl in
their eligible rear positions. Publish the known slot1 costs and one recovered
numeric effect mechanism with fixture coefficients, preserving unknown original
magnitude/Invincible penetration. Wait until visible icon is fully opaque,
confirm source group's SP>=3/4, then issue one short tap on that actual icon.

Measure: protocol10/ReserveSkill, nonempty returned effects, exactly one cost
deduction, real enemy HP decrease or bounded DOT applications/heal, skill-end
completion and resumed normal inputs. Empty effects, a dim alpha128 icon,
insufficient SP, absence of enemy, active reserve or background pause are
independently identifiable refusal cases. No server-side fake battle completion,
manual Rage refill, guessed tutorial clears or client mask patch is required.
