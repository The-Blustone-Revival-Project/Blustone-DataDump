# Arena actor construction: recovered bonuses and remaining HP attribution

Read-only source audit of existing original native exports and recovered LEVELING
JSON. No emulator, ADB, Ghidra, runtime, original asset, server or balance edits.
The first Arena automatic win's player/enemy HP maxima28733/8496 and preparation
Mowgli levels5/1 were supplied by root; this note does not independently certify
those live measurements or infer a complete formula from them.

## Recovered source facts

`CSRFC::InitBeforeOpen G941518` calls `CSRDataMgr::LoadLevelData` with the literal
**leveling_b**; exact relocated string is resolved in
`ghidra-arena-battle-stage-strings.txt` at G941536/G94153c. This is separate from
ordinary expedition leveling_m and Episode leveling_e.

Preserved `in-game-stats/leveling-chunk09.json` contains the Arena-style tuning:
both atk_camp/def_camp bonuses have HP2.0/ATK2.6/DEF1.0; rank1..5 HP multipliers
are2.6/2.2/1.8/1.4/1.0, with ATK/DEF1.4/1.3/1.2/1.1/1.0. Offense/deffense roles
have HP1; bomberHP.85, supportHP.8. Stage b_00_01 lists an additional1.1 tuple
for card051. These are original resource entries, not reconstructed rival
metadata and not proof that every entry contributes in the current encounter.
Speed bonus.8, play_time90 and the remaining tuning similarly require the actual
selected LevelData/readback before claiming live values.

`CSRFC::MakeStageInst G9418b0`, in
`ghidra-arena-battle-stage-consumers.txt`, obtains deck kind4 from PlayData. For
each nonzero owned instance it finds the inventory card, constructs ACTOR_INFO,
sets the new card's instance serial/refID, copies worn skin and awakening, and
calls **CalcBonus(instanceSerial, TEAM_DIR0)**. This audit found no SetLevel,
SetExp or explicit level-normalization setter in this function. The fresh card
is not evidence that live owned EXP is cleared: downstream analyzer construction
must be followed before assigning that interpretation.

The opposing branch copies its BATTLE_ENEMY card via `CSRCard::operator=`, sets
refID/awakening, and calls **CalcBonus(sharedCard, TEAM_DIR1)**. Both sides also
collect other per-card contributions (equipped gems, and opposing card-book
metadata are visible in this export). The final function calls ApplyBonusBuff
for both assembled maps. Therefore preparation level alone does not describe
all encounter bonuses.

Shared ordinary arithmetic remains governed by the existing
`hunter-native-stat-growth.md`: explicit reference rank/awakening row selection;
SetExp derives level using UserLV; integral base growth is base+up*level before
later bonuses, rather than base+up*(level-1). `ghidra-owned-battle-stat-load.txt`
shows analyzer-derived rank, role, final health/attack/defense entering actor
default-stat fields. This establishes a construction boundary, not Arena's full
final health calculation.

Fixed Episode construction is a separate branch: ACTOR_INFO flag08 invokes
Analyzer.Load(ACTOR_INFO), which loads the supplied CardInfo and selects its
last stat-vector rank through GetMaxRank. Flag100 is the distinct GVG loader.
See `fixed-actor-skill-scalar-contract.md` and
`ghidra-fixed-actor-rank-selection.txt`. No observed Arena flag08/readback is
provided here; do not attribute Arena HP asymmetry to Episode fixed-rank behavior.

## Unclosed selection and next narrow evidence

Symbol evidence identifies the exact CalcBonus overloads:

- G a1bce4: instance serial and TEAM_DIR.
- G a1bfbc: shared Card and TEAM_DIR.
- G a1be5c: TEAM_DIR, CHAR_ROLE, unsigned rank, reference ID.

The inspected exports contain callers, not these three complete bodies. Export
their instructions to establish inventory lookup, actual role/rank selection,
bonus combination order and whether any rank/level normalization occurs there.
Then follow the downstream ActorInfo flag producer/analyzer load for Arena;
do not transfer Episode flag semantics without observing that Arena branch.

No source or live tuple in this audit independently reconstructs28733 or8496.
Those totals are consistent with different owned levels/parties plus original
role/rank/camp bonuses, but consistency is not causal proof. A qualified live
Arena actor-stat sample (identity/rank, HP maximum, selected LevelData and
effective bonuses) would distinguish construction from preparation display.
Do not retune rival HP, overwrite owned levels, infer equalized Arena stats,
or claim original final balance merely because automatic combat won.
