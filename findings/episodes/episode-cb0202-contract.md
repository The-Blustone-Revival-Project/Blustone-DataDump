# CB0202 original actor and terminal contract

2026-10-08. Read-only original recovered JSON and existing native/material
reports. No ADB, Ghidra, source/runtime/profile/save edits or grants. Native
CB0202 participation, effects and outcome remain root validation tasks.

## Assembly, identity and exact fixed stats

`analysis/recovered-reference/EPISODE_COMBAT_CB0202.json` declares four empty
owned left slots followed by fixed Hunter `CB0202_049_1`; the right wave is
`CB0202_M1`, `CB0202_M2`, `CB0202_M3`, `CB0202_BOSS`, in that order.
MakeStageInst's positional serial counter still advances through owned slots
(existing `ghidra-episode-first-combat.txt`, G b23f60). Therefore expected fixed
left Bright is serial **5**, camp0; right serials **6,7,8,9**, camp1. Owned
slots retain actual inventory IDs in namespace1. Verify exact actor pointer,
serial-map source and camp with the native observer; these are source-derived
predictions, not this lane's live observations.

All fixed tuples come from original `EPISODE_STAT_ACTORS.json`:

- **Bright CB0202_049_1**: ref049/resC049, attr1/role4, cool_time5000;
  rank3, HP600, ATK356, DEF333, SPD7, crit12, critdamage180,
  penetration0, block12, block reduction42, resistance3, regen15.
  Original attr_enhance is omitted. Combat thumb level1/rank3/hyper0/attr1,
  selected skill flags `[1,1,0,0,0]`.
- **M1/M050**, serial6: attr1/role1, rank2, HP800, ATK680, DEF160,
  SPD0, crit20, critdamage200, penetration0, enhance0, block20,
  block reduction20, resistance0, regen15.
- **M2/M049**, serial7: attr2/role1; identical M1 numeric tuple.
- **M3/M051**, serial8: attr3/role1; same tuple except ATK700.
- **BOSS/M062**, serial9: attr1/role1, rank3, HP1800, ATK750, DEF160,
  SPD0, crit30, critdamage200, penetration0, enhance0, block30,
  block reduction30, resistance0, regen25.

Each monster cool_time5000 and skill definition array is empty. First three
combat thumbs level10/rank2/hyper0, boss level20/rank3/hyper0; attributes match
above. Every monster selected skill list is `[0,0,0,0,0]`. Preserve original
SPD0 and encounter-specific tuples; do not invent ordinary level scaling.
Bright ally HP600 is distinct from CB0201 enemy HP900. This fixed ally does
not confer owned Bright inventory, ordinary reference stats or a reward.

LoadCombat G b17260 binds all nonempty actor IDs through local Episode
FindActorRef G b1c2ac/ParseActor G b1bd5c, and MakeStageInst copies that
prebound CardInfo pair. JSON `monster` sets flags but is not alone native Mob
class proof: existing CB0102 material observations prove M022 uses native
Hunter primary214a3fc/control214bdc4. CB0202 should directly corroborate its
four monster class/owner bindings; do not add global monster references from
the JSON type string alone. See `episode-cb0201-contract.md` for retained
generic Hunter/Mob backend distinction.

## Bright skills and Rage boundaries

Bright has exactly two original definitions:

- TYPE1/target_rank1: cooldown8000, **cost4**. Effect numeric fields
  effect_type1, target_type4, target_stat1, refer_target_type1,
  refer_target_stat3, base_number20, duration4100, interval1000.
- TYPE2/target_rank2: effect_type4, target_type1, target_stat14,
  refer_target_type2, refer_target_stat0, base_number-25, duration5000,
  interval0. Cost/cooldown are omitted for this second definition.

Preserve numeric effect semantics; this report does not prove an English
heal/damage interpretation, a live Bright skill activation, automatic passive
application or observed HP deltas. Do not reuse CB0201 Bright TYPE1's base9
or reference type2/stat4; that is a different fixed actor definition.

Original LEVELING_E facts retained in `episode02-material-closure.md`:
atk_spd_bonus0.8, play_time300, initial SP left2/right1.8, role/camp/rank
HP/ATK/DEF factors1.0. Its RW SHA256 is
9286d223afc9d7c781544bd649cb8934efb200ef704fd4dd97caa5d6a00af8a8.
These are descriptor values, not new CB0202 live selection or Rage growth
observations. Root's guarded group SP/rate/max probe can verify actual values;
no forced Rage, invented costs or numerical balancing follows.

## Materials and environment

Combat power5000, game_res_id string2, BGM_BATTLE2; original ENV_INFO2
PreFix STI002 selects **ST002**, with actual A1/B1/C1/D1/E1 layers.
field_bg_res BG_RES is not the recovered InitBackground lookup selector.
M050/M049/M051 use original **M017.jet**, M062 **M021.jet**. The complete
AT→S2→I2 graphs and positive-alpha pixels are closed in
`episode02-material-closure.md`; M017/M021 AT/S2 bodies are raw. M050/M051
intentionally share M049_SHA for attack and shadow edges. No alias is needed.

Bright uses original C049/C049_Q/C049_EFT/C049_SND, not C049A/B variants.
Story05 portrait NPC families N500/N501 and VOICE_CDN5 are separately needed
for dialogue, not extra combat actors. Original BGM_BATTLE2 belongs to SND1;
victory voices Captain C009_35 belong VOICE_CDN7, C049_35_1/2 and CHILD_35
to VOICE_CDN4, N500_35 to VOICE_CDN5. Resource graph closure does not by
itself prove native delivery, residency, rendering or skill effects.

## Original victory terminal and persisted story

Original Episode catalog `EPISODE_S01.json` links **E02_S05** to CB0202.
Entry EP_0602A has15 nonempty texts; final node23 is “Haha... Stop playing
a hero, your life is at risk!” Terminal24 fades0.6, waits0.6, combat_goto
CB0202. Full/repeat loss uses EP_0000A/EP_0000B.

Victory chooses **EP_0602B**, original DIAL-EN header2459238, packed1512,
RW14953, SHA256
1255287e6c8ca0c8d425be685fae51e3faba76c2befff9238b513bee768bd93a.
Existing original outgoing-link audit has9 nodes/6 nonempty texts, linear
path0→1→2→3→4→5→7→8→6, no nonempty conditions. Final node8:
**“G-Guys! You're all safe!”** Terminal6 runs episode_clear, black fade0.6,
wait0.6, ctrl-scene-back count2.

Verify native bare `/episode/Read` **E02_S05**, saved cleared state and map
after advancing that final line. Enemy HP0 or win dialogue alone does not
prove terminal persistence. S06/EP_0603A is a separate subsequent story;
no parentE02 clear, FMD1 reward or owned Bright grant is entailed by S05.
