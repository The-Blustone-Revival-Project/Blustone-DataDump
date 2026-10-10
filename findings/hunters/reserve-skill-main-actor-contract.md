# Rear Offense skill: Karl becomes the real front actor

2026-10-09. Read-only original Thumb, retained skill-view exports and existing native reports. No ADB, Ghidra, runtime/source edits, grants or retune. This distinguishes native role behavior from an assumption that a rear-coordinate skill safely returns its actor to the same reserve slot.

## Admission and automatic exchange

Karl `CB0601_012_1` is the original fixed Episode **role1 Offense**, rank4/HP1150, independent of ordinary owned skill profile. `episode-followups` adapts ordinary001/003/004 references; it does not replace this fixed actor's original skill/cooldown/stat tuple. Scripted skill1 cost3 and active/follow-up/critical flags remain their own original data.

Icon listener **G9f7604** requires actor+a7d enabled and dispatched opacity byte255, relevant same/opposite camp input actors with visible enemy intersection, game state13c bit4 clear and source/front stun admission. Roles3/4 are supporters; roles1/2 are not. For non-supporters the listener finds the current front serial, emits `who=clicked serial` and `exchange=front serial`, then sends skill protocol10 (G9f79d2/G9f7a0c/G9f7a46..58). This is not a manual battle exit or an HTTP deck mutation.

**GameNet.OnProcSkillReserve Ga0ff0c**, when exchange serial is nonzero, calls **OnExchangeImmediatly Ga11b3c at Ga100f0** BEFORE ReserveSkill G9e6910 at Ga10104. Exact instruction Ga100e4 stores flag0 with the exchange serial arguments. Despite the name “immediate,” this selects the normal **GameBase.ExchageKeys -> Group.ExchageKeys**, not forced flag1. Existing normal model checks—both actors present in their proper lists, CanExchange HP/cooldown/stop predicates and outgoing stun—still apply. Successful exchange really moves reserve/front list nodes and repositions the clicked actor; it is not just a cut-in portrait.

## Rage and actual skill purchase

Group.UseSkill **G9a4084** resolves the selected actor from the current group, checks cost<=groupSP at G9a40ae..c2 and CanRunning before Actor.UseSkill G981910. The latter receives unsigned currentSP, finds registered ACTOR_SKILL and calls SkillMgr.Buy G9b23bc. Buy also checks item availability/time/cooldown and cost before producing effects. Cost is debited only for a nonempty returned list (G9a4142..4158).

An accepted Karl skill therefore combines real exchange plus original skill cost; normal exchange itself has no explicit Rage fee in the inspected model chain (`native-manual-exchange-contract.md`). A accepted touch injector, bright portrait or prior activation does not establish that every later press passed these current model gates.

## Finish does not restore the previous front automatically

Skill view finish closure **G9f5610**, retained in `ghidra-active-skill-return.txt`, searches current **airship list sentinel game+188/first+18c** for the captured operator serial. If found, it calls **EnterAirship G9855ac** and SetVisible(true). This supports temporary rear-role cinematic movement when the operator remains a reserve member.

If operator is not found in that reserve list, the closure instead finds its back-end actor, reads **GetFrontExchangeCool G97ecb0** and calls **SetExchangeCool G97ec80**. It then resumes game reason2, sends model event0x11 and DeactiveSkill. It does **not** swap the previously front actor back, restore Karl's original reserve slot or reset his HP in this branch.

Thus a rear Offense Karl skill can leave **Karl as the real frontline combatant after the cinematic**. His rear portrait's disappearance is expected after a successful swap; it is not by itself evidence of death or a missing resource. He can then take normal enemy attacks after combat resumes. Paused cinematic immunity/exact damage timing is not inferred from this finish path.

## Separate cooldown meanings

**SetExchangeCool G97ec80** stores `actorClock228 + suppliedDuration - GetExchangeCool` into last-exchange timestamp+a58. Here GetFrontExchangeCool G97ecb0 tailcalls GetExchangeCool G99b0a8; passing that same value makes lastExchange equal current actorClock. CanCatch/IsFrontExchangeCool then require a full effective cooldown interval, computed default+6c * buff+6c. Root's earlier qualified Karl defaultCool5/multiplier1 is observed exchange timing, not a universal numeric constant for every actor.

**MakeSkillCool G9849ac** separately writes `actorClock + suppliedDuration` into deadline+a60. SkillMgr.Buy's registered-item cooldown and native scene-wide activation state are additional gates, distinct from exchange timestamp, skill icon visibility, ordinary attack interval and Rage affordability. Do not clear any of these fields or treat a fixed rear point as repeatedly available every controller milestone.

## Death and what the current frames prove

IsDead **G99aba0** is exact HP+8b0==0. CanRunning G99ac38 tests HP!=0. Mere absent reserve portrait does not prove either. The native death/group/model paths can move or remove actors from current battle lists; detailed complete automatic succession depends on those separate handlers. Fixed Karl's battle death would not consume an owned Hunter or permanently delete a roster card; no server ownership mutation follows from this client-local scripted participant.

Earlier `battle-skill-plan-validation.md` documents rear Karl1150/front Nene664 -> accepted player transition -> **front Karl1014/rear Nene617**, then continued Karl combat. That is direct prior normal exchange evidence. Current root `episode-followups-001/report.md` records CB0602 first9301370 attempt's Karl cut-in at011, changed reserve arrangement/absent Karl portrait at030 and eventual loss. It does not isolate Karl's exact HP trajectory, prove the later coordinate still targeted Karl, or establish a skill return/death bug.

Useful next observation after the first accepted Karl skill is the qualified current input/front actor serial/camp/HP and reserve membership, with exchange/stun/cooldown state. If Karl remains front, either continue real combat with him or perform one separately validated normal exchange; do not assume the same rear coordinate still calls Karl. A source-only contract cannot authorize repeated stale-position presses or turn a loss into a win.
