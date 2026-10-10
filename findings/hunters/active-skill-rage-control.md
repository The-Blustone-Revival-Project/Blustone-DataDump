# Bounded native Rage and active-skill control

2026-10-04. Read-only existing native evidence, original Thumb bytes, LEVELING chunk09 and current source fixtures. No source, Ghidra, adb or original mutations.

## Charge dataflow and corrected offsets

Previously recovered `active-skill-gesture-rage.md` pins group currentSP+0x2bc, passive rate+0x2c0, max+0x2c4. Charge getters G99b13e/G99b146/G99b14e read source default-stat +0x70 attack/+0x74 damage/+0x78 kill. Actor construction copies LevelData attack+0x220, damage+0x224, kill+0x21c.

**Correct a reversed LevelData sentence in that older report:** exact LoadLevelData decomp and strings prove LevelData+0x218=sp_increase_spd_per_sec, +0x228=sp_max. MakeCamp G9d3b10 loads max(+228)→r1; G9d3b38 loads rate(+218)→r2; SetSkillPointOption G9a43a8 stores r2,r1 at group+2c0,+2c4. Group probe offsets remain correct. Sources: ghidra-leveldata-decomp-01.txt stores near lines968..1112, ghidra-leveldata-strings-01.txt keys Ga1813a..Ga18312; original Thumb inspection.

OnDamange G9e0530 charges the **source actor group** for eligible actual delivered damage: target finalHP0 picks kill getter at G9e085a, otherwise attack getter G9e0882, AddSkillPoint G9a43b0 at G9e088a. Positive nonlethal ordinary damage predicates differ from skill/DOT HP events. Screen presses alone do not award Rage. Victim damage-charge getter is encountered earlier, but its complete addition predicate is not proved by this lane; do not use that as a predicted recharge source.

Preserved original analysis/in-game-stats/leveling-chunk09.json: rate0.21, attack0.02, kill2.0, damage0.01, max10, left.first_sp1.5/right1.45; play_time90. These are actual shipped chunk values, **not current selected runtime evidence**. Parent observed stage5 group rate0.01 and SP~1.174 after122s. That runtime does not exhibit the preserved passive rate/initial balance. Read actual selected LevelData and source default-stat charge values before changing encounter durability or estimating readiness.

## Native input distinction

Ordinary attack press path: OnProcessPress G9db1bc forwards root UI, then gates pause/state/capture and calls OnInputProcDash G9d2f68, which tests IsInputable/CanDash and invokes TryDash G9d2c18. Existing stage3-input-gate.md describes exact predicates. Short repeated presses are a supported ordinary attack observation; a held press is not proved to repeat attacks. `IsHoldAttack` is a positive buff counter at buff-state+0x98, **not evidence about a physically held finger**. Skill activation itself is one press on an opaque255 icon, not hold/drag; cost4 for Lantern/Tyltyl,3 Mowgli/Nene. Capture/catch and skill taps must remain separate.

## Evidence-backed encounter plan

First read actual source attack/kill charge values plus native timer remaining and measured ordinary hit damage. Retain costs and actual Rage; no forced fill, cost0, setting0 or guessed CUT bindings.

If actual kill charge is2, two ordinary enemy kills can produce4 Rage from near0. Keep a third, more durable enemy alive after those kills so the target/encounter predicate still passes for one skill. Existing single HP100 enemy is defeated by one normal hit and leaves no live encounter; merely increasing its HP removes kill recharge until it dies. Extra killed foes plus one surviving target is therefore preferable **only if the measured kill charge supports it**.

If actual kill/attack charges are tiny, calculate required ordinary hits before deciding a larger-HP control: N=ceil(max(0,cost-SP-rate*availableActiveSeconds)/attackCharge), excluding unproved victim gains. Durable fixture HP must exceed measured hit damage times planned hits, with a small buffer; retain modest enemy attack so damaged-target healing is observable without losing party. Example only: with SP1.174, cost4, rate0.01 and attackCharge0.02, waiting alone requires282.6 active seconds, while zero-wait recharge needs142 eligible hits. Such a control exceeds the preserved90-second chunk budget and is not justified without the actual stage timer/hit cadence. Original max/timer/stat values must not be fabricated from that arithmetic.

The next native run should obtain one real eligible skill, then confirm accepted protocol10/reserve, nonempty effect list, one cost debit, heal/damage and finish ResumeGame(2)/DeactiveSkill. Stop after the bounded control and record exact failures. No success is claimed by this report.

## Parent-only focused dumps if needed

- OnDamange G9e0530 (exact victim/source predicates and gains).
- OnTouch G9d72fc, OnProcessPress G9db1bc and OnProcessMove G9dbe00 (held/contact repeat behavior).
- Actor Attack G97f880 / AttackWithoutState G9859bc, OnClickAttack G9a145c (actual-hit cadence).
- LevelData LoadLevelData Ga178c4 and CSRDataMgr::LoadLevelData G8b26e4 (selected chunk/path if current native tuning disagrees).

Existing getters G99b13e/146/14e and group AddSkillPoint G9a43b0/OnRefresh G9a5760 are already simple enough for bounded live reads; a broad reverse-engineering dump is unnecessary before measuring these values.

## Across-wave continuation audit

Original Thumb getters verified exactly: G99b13e loads actor+0x8b4 then member+0x70; G99b14e loads actor+0x8b4 then member+0x78. Reader snapshots of those members are the actual selected attack/kill float gains.

Group AddAndActiveWave G9a2d3c tailcalls **same-object Activate(index) G9a2d88** at G9a2d84. Full Activate through next symbol G9a30cc manipulates wave actor list/positions, clears/reattaches children and idles actors; there is no direct currentSP/rate/max store. OnProcWaveStart Ga10430 (body428bytes) obtains enumerable camp via G9dae48 and starts updatables, without a direct SP setter. These support reuse rather than a new player group per ordinary wave.

OnProcWaveChange G9ce4c4 body2108bytes schedules effect lambdas at G9ceb1a and G9cecc0. Their bodies remain the narrow missing part of a complete persistence proof. Do not treat a reused group alone as proof no nested callback resets its state. Parent focused dump targets: OnProcWaveChange G9ce4c4 to identify closure vtables/operator addresses; GameNet OnProcWaveStart Ga10430; SRJSONToGroupData G10b02ac if packet-field provenance matters.

**Correction to an intermediate scan:** direct ParseGroupInfo calls G9cf72a/73c are in OnProcDeadGroup G9cf6fc, beyond WaveChange's body. Existing ghidra-complete-18-gamenet-decomp.txt/20-keys-parsegroup.txt prove ParseGroupInfo keys only ink,total_hp,total_hp_max; it does not itself reset SP. The earlier broad-scan concern about wave ParseGroupInfo is retracted.

Conditional three-wave experiment: if live friendly kill gain2 is confirmed, two HP100 ordinary enemy kills should accumulate4 plus passive gain in the reused player group; retain a live third enemy and immediately activate one eligible Tyltyl heal only when a damaged ally and SP>=4 are actually measured. One final HP100 enemy can still die before that input, so a modestly durable third-wave fixture or one withheld ordinary attack would improve the observation window. No new owned grants are needed. Original charge values, real wave persistence, final enemy survival, and target damage must each be observed, not inferred from configured2 alone.
