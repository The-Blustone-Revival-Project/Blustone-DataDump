# E06 earned progression options against current replica policy

2026-10-09. Read-only source, existing native reports and selectively projected local save fields. No ADB, Ghidra, runtime/source/save changes, grants or fresh stat hunts. Balances below are a snapshot, not authorization to spend them or proof that every starting fixture unit was earned.

## Current available resources

Main account currently has gold **11580**, AP50/BP10, ten Hunters. Original party: 1000001/ref001/rank1/EXP340/skill1 level1; 1000002/ref002/rank1/240/1; 1000004/ref003/rank3/240/1; 1000005/ref004/rank1/840/2. Five spare Tyltyls 1000012..16 are rank1/EXP0; spare Nene1000017 rank3/EXP0. All ten are locked. Leader1000001 and the four original cards are in world decktype1; spares are outside that deck. No active Search attempt is saved.

Items: four individual AP items914, two individual BP items913, local Sylvester trace inst6 qty3, Search capsule AIRSHIP_TICKET inst7 qty36. E05's native reward added20 capsules to the previous16; Search UI and original capsule artwork are verified. Capsules are Search admission, not Hunter EXP. Search stage publishes character_exp0 and does not directly solve leveling. Native earned Special Supply's16 entries were already settled; do not treat them as an available second160 gold. Day4 login credited100gold/20VIP; do not replay it.

Wallet contains gacha_iap_qty240000/gacha_free_qty239670, largely starter fixtures. They are not a newly earned 479670-Manda training budget. Native E02 reward30 free Manda is proved, but unpartitioned current totals do not establish how much remains of that specific receipt. Recruitment is not required for the first improvement below.

## Preserve all ten: ordinary Skill Training

Normal Hunter detail -> Skill Training is already validated. Actual native `/gym/MultiSkillUp` (intentional body typo `mulit_skill_up_count`) upgraded original Tyltyl skill1 from1 to2, debited200 gold, displayed Healing52.00→54.59, and retained EXP/ownership. See `native-skill-training-control.md`. `/gym/SkillUp` also has a native callback and server handler, but that report's UI used MultiSkillUp; prefer the proven UI route.

Current `skills.ts` fixture mode only gives slot1 nonzero effects. Slots2..5 remain inert even if training succeeds. Training those slots cannot be cited as improved combat. Native fixture effects use coefficient `(base+up*ownedSkillLevel)/100`: Nene/Lantern damage100% atLV1,115% atLV4,145% atLV10; Mowgli DOT20% atLV1,23% atLV4,29% atLV10 per nominal application; Tyltyl heal105% DEF at currentLV2,115% atLV4,145% atLV10. These are mechanisms and local numeric fixtures, not original final balance.

Gold-only destination prices are100*level. A bounded first Nene slot1 upgrade1→4 costs **900** and changes coefficient100%→115%, preserving ten Hunters, earned EXP and ranks. Tyltyl2→4 costs700, changing105%→115%. Both together leave9980 gold. This only improves successfully activated skills; root is closing moving hitbox/readiness controls, so do not claim a stronger party from displayed levels alone. Material damage/healing must be observed after correct native activation.

Rank1 cap10 applies to001/002/004; Nene rank3 allows cap30 under the current inferred rule. Nene1→14 alone costs10400, coefficient165%, leaves1180; this demonstrates affordability, not a recommendation to exhaust the wallet. Prices/material-free policy and caps remain reconstructed fixtures. Never train fixed Episode Karl: he is not one of these owned instances.

## Native Raise: available but consumes earned Hunters for modest gains

Normal Gym Raise -> select an owned target -> select unlocked partners -> Train has verified `/gym/LevelUp`, including five-source cap, exact source removal, boxing/result animation and responsive return. `native-five-partner-training.md` proved fiveLV1 sources, gold500 and EXP+500. Lock toggle/UI and source identity must be freshly checked; old carousel coordinates are unsafe. Current handlers protect leader/decktypes1/2/4/5, locked and active attempt source IDs; spare1000012..16 are candidates only after deliberate native unlock.

Every current rank has the fixture30-level cap/EXP2900, thresholds100 apart and LV1 source yield100. Five spares therefore add500EXP, **five levels**, for500gold. Archive2019 projection retains only hp_up10/atk_up1/def_up1. Thus this gain is +50HP/+5ATK/+5DEF, no recovered speed/crit increase; at archive ATK726..1058 it is below1% base attack. It also removes five owned Tyltyls, reducing roster10→5. Do not sacrifice them under the assumption that this alone offsets CB0602's enemy party.

The sixth spare adds another100EXP/one level if deliberately consumed. Leaving it owned preserves a second Nene. Current target maximum improvement from EXP240→2900 is27 levels (+270HP/+27ATK/+27DEF), from340→2900 is26, from840→2900 is21. These bounds show that the current native-compatible fixture growth is relatively shallow. No hidden rank multiplier should be invented to make Raise effective.

## Campaign victories: non-destructive earned EXP

Already validated normal campaign victory grants participant EXP through `/mission/Start` -> matching `/mission/Complete`, native `card_exp` absolute pairs and persisted owned EXP. `state.ts` grants published character_exp10 to the snapshotted firstfour owned participants on each accepted new matching victory, caps at2900, and gives no Hunter EXP on loss. Repeating an already-cleared stage can still grant this Hunter EXP, while first-clear gold/teamEXP is not repayable. Capsules additionally require genuine accepted normal victory. Native loss refund preserves overflow; idle battle is not a valid farm.

With10EXP/win, one level costs ten wins. Maxing EXP240 Nene/Mowgli requires266 wins, Lantern256 and Tyltyl206, subject to energy and real battle success. This preserves all ten and uses earned play, but is expensive relative to the small +1ATK/+1DEF per level. Existing AP items are normal consumables only; do not create/refill fuel or post synthetic completions. Search capsules can earn local Sylvester traces through separate native Search, not these four's direct EXP, and need actual combat/settlement; no immediate source-Hunter grant follows from qty36.

## Rank promotion is presently the wrong immediate stat remedy

`/gym/RankUp` requires published maxEXP2900, same-grade unused/unlocked materials and gold1000/material; no party member is currently eligible. Partial rank3 credit preserves EXP and supplies local5% primary-stat bonus per credited material, but Nene must first reach cap and the one spare rank3 can supply only one of three credits. This is an inferred arithmetic policy, not a proved live partial promotion.

Full rank1 promotion consumes one rank1 material and resets EXP to0. `ordinaryRankStats` explicitly repeats the same projected base across ranks1..5; full promotion counter0 has no implicit rank gain. It therefore loses level increments before retraining, although it raises skill cap and eligibility. Never claim promotion immediately increases archive2019 base stats. Native callback/partial animation/cached bonus caveats are documented in `rank-up-implementation-audit.md`; its old low-ID advice is superseded by namespace1 IDs.

## Guards and acceptance boundaries

Skill handlers check owned instance, valid slot/rank, cap, whole-batch costs, nonnegative counts and sufficient gold. Raise checks unique1..5 sources, locks/protected decks and curves before consumption; promotion checks samegrade/noawake and nextgrade references. The server cannot see a client-local Episode battle or cached Episode party; perform all progression in a freshly verified safe menu with no helper/battle, then rebuild/reselect native Episode party and verify the new detail values. Skill handlers have no active-attempt target guard, and RankUp only explicitly rejects ordinary active-battle targets; do not execute either during active arena/Search/Episode combat.

A legitimate first controlled step is a native Nene skill1 **1→4** preview/upgrade, followed by exact before/after gold11580→10680 and skill1 unchanged EXP240/rank3/ownership/decks, normal reload/party rebuild, then actor-bound accepted skill and real damage observation. This preserves the roster and exercises already proven progression rather than retuning reference stats. It is still an experiment under local balance, not a guarantee of CB0602 victory.
