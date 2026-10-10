# First recovered story combat CB0101

2026-10-05. Read-only original ELF Thumb, curated ghidra-episode-decomp-02.txt, exported EPISODE_COMBAT_CB0101.json/EPISODE_STAT_ACTORS.json and prior map-backdrop.md. No Ghidra, VM, server source edits, combat outcome or grants.

## Original graph and local combat load

Recovered E01_S02 links first story combat **CB0101**. The original record has titleE01_TITLE, stage_nameE01_S02_TITLE, power"1500", **game_res_id:"99"**, bgmBGM_TRAIN, and win_dialog/lose_dialog/lose_dialog2 allEP_0302B. It has one left wave containing CB0101_009_1 and one right wave containing CB0101_003_1. These are shipped story actors, not an owned-player party or inferred mission-stage monsters.

**CSRMEpisode.LoadCombat Gb17260** first checks its combat cache+44 and selects an existing result into currentCombat+24/+28 if found. Otherwise it concatenates **combat/** with the supplied combatID (literalLDRb172fa/ADDb17300, concatb17304), calls **ReadJson atb17310**, and constructs **CSRMEpisode::COMBAT atb17348** from that local JSON. Case-normalized resource lookup for local names is already proved in episode-native-resource-loading.md. This is not a new /mission/Start or /episode/GetCombat server response.

## Fixed STAT actors and actual values

**FindActorRef Gb1c2ac** checks the episode-only CardInfo cache+50. On a miss it lazily reads local **stat** (LDRb1c328/ADDb1c32e, ReadJsonb1c338), searches the decoded STAT index and calls **ParseActor Gb1bd5c atb1c3be**. ParseActor constructs local CSRCardInfo from id,res_id,attr,role,cool_time,stat,skill. It parses stat through **CSRCardStat.parse atb1bfe8**, pushes it into that CardInfo atb1c004, parses each nonempty skill through **SRSKILL_INFO.parse atb1c130**, and assigns its parsed TYPE through **SetSkillInfo atb1c13a**.

The exported original rows are:

```text
CB0101_009_1: ref_id009, res_idC009, attr3, role2,
 rank2, HP323, ATK229, DEF320, SPD7.00, cool_time5000
CB0101_003_1: ref_id003, res_idC003, attr2, role2,
 rank3, HP514, ATK333, DEF394, SPD7.00, cool_time5000
```

These exact episode statistics must not be merged into ordinary hunter base stats. The STAT row's `ref_id` is present in the original JSON, but **ParseActor's inspected field reads do not include ref_id**. Its cache identity is the full actorID. The art prefix is parsed from res_id. Thus merely seeing `_009_` or ref_id009 in the recovered text does not prove the ordinary /reference/GetCard table requires a009 definition for this fixed episode path.

Original skill rows are also nonempty and stronger evidence than generic fixture effects:009 TYPE1 cost3 has Activate/Enemy/HP1, refer_target_type1/refer_target_stat1, base_number-1600;003 TYPE1 cost3 base_number-1800/crt_chance100, TYPE2 stun target_stat15 duration2500, and TYPE4 self HP effect referstat6 duration3100/interval1000. They retain their original parser omissions/defaults; this report does not equate their formula magnitudes with ordinary hunter skill balance.

## MakeStageInst distinguishes fixed actors from owned fallback

**CSRSceneMEpisode.MakeStageInst Gb23f60** reads current COMBAT, constructs fresh ACTOR_INFO records and handles both sides. For **nonempty actor_id** it copies the prebound shared actor reference at ACTOR+34/+38 (left instructionsb2418a..b241a2; matching right branch), then applies the combat thumb/skill settings. Left thumb is LV15/rank2/hyper0/attr3 with skill[1,0,0,0,0]; right LV1/rank3/hyper0/attr2 with skill[1,1,0,1,0]. The exact COMBAT constructor binding of that ACTOR reference needs further transitive corroboration if proving complete ordinary-reference independence; this lane does not claim a full successful fixed-actor runtime.

The **SetRefID call atb2437e** belongs to a different branch: empty actor_id copies from an owned Inventory.FindCard (callb24320), carrying awake/overcome and original card refID. That owned fallback is not exercised by CB0101's two nonempty actorIDs. Therefore those existing MakeStageInst lines cannot be used as positive proof that fixed009 demands an ordinary owned/global card reference. Art C009 and C003 remains required because their local CardInfo prefixes are explicit.

## game_res_id99 selects environment, not campaign stage99

COMBAT constructor reads **game_res_id as a string** atb14168/from_jsonb14176, stores it atCOMBAT+24. **SceneMEpisode.InitBackground Gb23e80** reads currentCombat+24 and passes it directly to **CSRGameBase.OnInitBackground G9cbf34 atb23ecc**.

OnInitBackground looks up this string in **CSRStaticData ENV_INFO map+150 at9cbf5e**, then obtains that record's art prefix atnode+34 (9cbf66) and formats it with environment layer suffixes (format%s_%s at9cbf96 and successors). Therefore CB0101's99 is an **environment-table selector**, not a campaign stage ID, not a literal99.JET package and not the field_bg_res value. The historical map-backdrop warning against placing99 in area.resource_id concerns a different art field and does not contradict this local COMBAT selector.

The inspected base environment reader does not guard a missing map entry before reading node+34. ENV_INFO99 must genuinely exist with its layer prefix/materials; serving a99 package or aliasing BG_RES is not a justified fix. Exact99→prefix descriptor and current runtime environment availability were not freshly verified in this unit.

## Init and resource dependencies

**InitBeforeOpen Gb23c38** loads local **leveling_e** through DataMgr.LoadLevelData atb23c5e. It looks up **UI_ROOT** then child **UI** (LDRb23c92/ADDb23c96 andLDRb23ca8/ADDb23caa), finds/creates **CSRFCUIBase** atb23cc0 and stores its shared binding atgame+20c/+210. Story combat therefore uses a specific local leveling/UI setup; the Arena-style UI class name alone does not imply an /arena battle protocol.

Required native materials include the genuine local CB0101 descriptor, STAT table, LEVELING_E, ENV_INFO99's actual layer art, C009/C003 art, BGM_TRAIN sound and EP_0302B dialog. R_EPISODE and art/profile exports supply only what their inventories prove; C003_DIALOG/local dialogue binding remains independently unresolved. No ordinary009 card definition, NPC namespace alias, invented monster or stage99 route follows from this evidence alone.

This report proves the load/schema branches and original values, not native battle entry, input, win/loss, reward completion or resource download. Further narrow parent dumps: COMBAT ctorb13fe0 for fixed-actor binding, FindActorRefb1c2ac, ParseActorb1bd5c, and ENV_INFO99 material table before promoting a first story fight.

## Parent corroboration from fresh full decompilation

LoadCombat b17260 binds each nonempty ACTOR.actor_id (ACTOR+28) through
FindActorRef and stores its shared reference into ACTOR+34/+38 on both sides.
FindActorRef first searches the Episode cache at +50; on a miss it loads local
stat JSON and parses the matching row. Its ref_id field is stored in a separate
Episode actor-to-display-reference map at +5c. No ordinary GetCard lookup appears
in this inspected binding path. This closes the prior narrow missing binding
link; it does not prove every later UI/skill helper avoids all global references.

The COMBAT constructor reads game_res_id into +24, and InitBackground passes
that field to ENV_INFO lookup. field_bg_res/BG_RES is not indexed there; do not
publish a speculative BG_RES alias. Original environment99 maps to STI099. The
opt-in profile now explicitly serves original ST099.jet and its byte-exact CDN
transport passed. LEVELING_E exists inside original LEVELING.jet, already present
byte-exact in instrumented +9. Native rendering/battle outcomes still unverified.
