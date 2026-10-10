# CB0201 original actor contract

2026-10-08. Read-only recovered original JSON, retained native decompilation and
already-recorded CB0102 native frames. No ADB, Ghidra, server/save edits or grants.
This report does not claim a new CB0201 battle observation.

## Participants and expected identity

Original `analysis/recovered-reference/EPISODE_COMBAT_CB0201.json` declares one
left wave of four empty slots, filled from the player's actual Episode deck.
The right wave has three identical `CB0201_M1` monsters, then fixed Hunter
`CB0201_049_1` (Bright). With all four left slots, generated right serials are
5, 6, 7 and 8 respectively; owned left serials remain the actual high inventory
IDs. Right camp is 1; left camp is 0. No ordinary owned 049 grant is implied.

Both records are in the single original `EPISODE_STAT_ACTORS.json`; there is
no separate required STAT_MONSTERS file.

- CB0201_M1: res_id M023, attr1, role1, cool_time5000. Stat rank2,
  HP700, ATK400, DEF130, SPD0, crit20%, critdamage200, penetration0,
  attribute enhancement0, block20%, block reduction20, resistance0, regen8.
  Skills are an empty original array. Combat thumb is level5/rank2/hyper0/attr1;
  selected skills `[0,0,0,0,0]`. Do not extrapolate ordinary level growth onto
  these encounter-specific values or repair SPD0 speculatively.
- CB0201_049_1: ref_id049, res_id C049, attr1, role4, cool_time5000.
  Stat rank3, HP900, ATK300, DEF140, SPD5, crit20%, critdamage200,
  penetration0, block30%, block reduction40, resistance0, regen8.
  `attr_enhance` is omitted in the original record; preserve parser defaults.
  Combat thumb is level1/rank3/hyper0/attr1, skills `[1,1,1,0,0]`.
  Only two skill definitions actually exist in STAT. TYPE1/target_rank1 has
  cool_time8000, cost4; its effect fields are type1/target4/stat1,
  refer_target2/refer_stat4/base9/duration4100/interval1000. TYPE2/target_rank2
  has effect type4/target1/stat14/refer_target2/refer_stat0/base-30,
  duration5000/interval0. Three selected slots do not justify inventing a third
  definition, assigning English effect semantics or predicting actual healing.

## JSON monster type is not proof of native Mob class

`ghidra-episode-first-combat.txt` LoadCombat G b17260 binds every nonempty
actor_id on either side through Episode FindActorRef G b1c2ac. That function
lazily loads local STAT and ParseActor G b1bd5c constructs the Episode-only
CardInfo/parsed stats/skills. MakeStageInst G b23f60 copies this binding for
fixed actors; only empty left slots use Inventory.FindCard and SetRefID.
Its exact resolved `monster` literal is retained in
`ghidra-episode-first-combat-keys.txt` at b247a6/b247b0. Right actors get flag8;
monster additionally gets flag16, yielding 0x18 before other flags.

The generic MakeActor G9e9e68 decompilation loses an argument; it dispatches
native Mob versus Hunter from the additional group/type argument. Its type
selection cannot safely be reconstructed from the JSON string alone.
Generic Mob.MakeBackEndActor G9afd58 **does** unconditionally call global
GetMonsterData. Generic Hunter.MakeBackEndActor G9ac2ac explicitly reloads
the supplied ACTOR_INFO through CardAnalyzer when flag8 is set, and binds the
Episode reference's resource prefix for that path.

Existing actual CB0102 frames settle the practical distinction:
`analysis/testing/episode-stat-projection-001/battle/001.stdout.txt` and
`005.stdout.txt` show both M022 objects with actor primary214a3fc and
control214bdc4, the exact **Hunter** class/owner, and first body21363d4
(Image). Gerard C005 has the same Hunter actor class and a Spine body.
Therefore earlier summaries labeling these Episode M022 objects native Mob
are incorrect. A CB0201 snapshot should verify M023/5..7 and Bright/8 directly;
the consistent expected branch is Hunter for these fixed Episode actors.
Do not add global M023 fixtures solely because the JSON says monster.

## Environment, outcome and persistence

CB0201 power2700, BGM_TRAIN, game_res_id string2 selects original ENV2/STI002.
field_bg_res BG_RES is not the InitBackground lookup selector. Exact original
M023, C049 family and ST002 material graphs are documented in the E02 closure
report; offline graph closure remains distinct from native render proof.

Win dialog is EP_0503B; losses EP_0000A and repeat EP_0000B. The existing
original-dialogue audit (`episode02-entry-materials.md`) retains EP_0503B header
2453692, packed1562, RW15898, SHA256
196227d36f1994a26ebdadd4284d80185c2d3a464847362aab926e66fa9cfd02.
Its linear path is 0→1→2→3→4→5→6→7→8→17, seven nonempty texts. Final node8
is “Be a family?”; terminal17 executes episode_clear, black fade0.6,
wait0.6, ctrl-scene-back count2. Actual terminal traversal should emit the
current story's Read E02_S03, then save that clear; preparation or victory
alone does not prove persistence. No chapter/item reward or Bright grant is
part of this contract.
