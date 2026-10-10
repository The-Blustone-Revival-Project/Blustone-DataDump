# E06 player skill publication and local effect path audit

2026-10-09. Independent read-only source/native-report review. No Ghidra, ADB, runtime actions, tuning, saves, or new stat research. Only the `BLUSTONE_ACTIVE_SKILLS` property was read from the private standing profile; no authentication fields were printed.

## Publication is conditional; verify the live branch

Captured standing `recovered-assets/replica-activation-20261005/profile.json` has **BLUSTONE_ACTIVE_SKILLS=fixture**. `skills.ts` accepts exactly `neutral` and `fixture`; omitted value defaults to **neutral**, which publishes all empty effect arrays/cost0. Resource overlays do not set this variable. Reading the captured profile is not proof of a running process's inherited environment or native cache. Root's normal restoration of that captured key must remain part of the launch recipe, or use already available native actor cost/result-list observations to corroborate publication. No broad process environment dump is justified.

With fixture selected, current `fixtureSkillSlots("003")` and `fixtureSkillSlots("004")` each publish five skill rows, types1..5 and target_rank1..5. Slot1 alone has a nonempty numeric effect; all remaining slots have cost0/empty effects despite their display icons. Current owned Nene rank3/skill1 level1 and Tyltyl rank1/skill1 level2 are eligible for slot1. Training passives currently cannot manufacture useful effects.

## Actual numeric rows

Nene003 slot1: cost3, cool_time0, crt_chance0, icon_id `C003_SI1`, cut_in_id empty. Its sole effect is serial1/effect_type1/target_type1/target_stat1/refer_target_type1/refer_target_stat1/base_number-95/up_number-5/duration0/duration_up0/interval0. Thus ownedLV1 coefficient is **-1.00**, using source combat attack and native defense/attribute processing. `value_calc` is description arithmetic; the numeric coefficient is nonzero and is the relevant runtime field.

Tyltyl004 slot1: cost4, cool_time0, crt_chance0, icon_id `C004_SI1`, cut_in_id empty. Its effect is serial1/effect_type1/target_type4/target_stat1/refer_target_type1/refer_target_stat3/base_number95/up_number5/duration0/duration_up0/interval0. At currentLV2 coefficient is **+1.05** of source combat DEF, healing FrontAlly and capped by native maxHP. Missing damage on a heal or zero healing on a full-HP target does not prove an empty effect.

Both retain string `value_calc` and array `effect_desc`; parser shapes and /100 coefficient normalization are corroborated in `starter-skill-combat-mechanics.md`. These selectors agree with its recovered source/target/HP meanings. Magnitudes, growth coefficients, target assignments and cooldown0 remain local fixtures; no original balance claim follows.

Git history shows skill publication was last changed by64985711 after ae89e3f1; no working-tree edits to `skills.ts`/`bootstrap.ts` were present during this review. The Episode/resource expansions therefore supply no observed source regression in these rows. Source immutability alone does not prove the freshly loaded native runtime list matches them.

## Reserve and application require more than a visible drawable

Existing original-native review `active-skill-gesture-rage.md` pins protocol10 -> OnProcSkillReserve -> ReserveSkill G9e6910 and group UseSkill G9a4084 -> actor UseSkill G981910. Group cost is debited only after returned effects are nonempty; ReserveSkill also rejects an empty returned list. This is client-local GameNet, not a missing `/episode/UseSkill` HTTP route. Adding a server endpoint would not repair this activation path.

The E01 observed Nene cost10→7.04/skill pause and later normal combat is positive prior acceptance of cost3/nonempty reservation under that client/profile. It does not by itself measure applied enemy damage or prove E06 loaded the same list. Current E06 actor+a7d enabled/visible/opacity factors1 establish only part of admission. Bound intersection, dispatched opacity byte255, correct actor serial/camp, role eligibility, actor state/stun/target validity, existing reservation, background pause8 and effect-list result still matter. A failed fixed-coordinate press cannot distinguish which later gate refused.

Tyltyl is role4 Support; eligible rear/airship input is required. Native role3/4 state3/4/8 can deliberately dim its icon, and the listener rejects byte128. Nene role2 can trigger automatic exchange if not already the active front actor. Do not use ordinary attack coordinate or a static portrait location as proof that the native icon event was delivered.

## Materials and callback gaps: what is and is not a demonstrated blocker

Current source publishes genuine AT skill icon names SI1, distinct from S2 SI01. Original C003_Q/C004_Q inventories positively contain SI1..5. Complete separate layout is documented to preserve original actor families while E06 adds Bibi/Dino; no concrete missing C003/C004 pack or changed icon name was found here. Residency remains a native observation, not an inference from file count. Existing live E01 Nene acceptance weakens a universal icon-load failure hypothesis but does not prove every E06 portrait/effect dependency.

The older audit sentence about empty `icon_id` is stale for current fixture publication. `cut_in_id` is still empty, but `starter-skill-resource-bindings.md`'s completed producer tracing establishes that skill view DATA+8/+14 are actor ref/ResID, **not cut_in_id**. Prologue always loads SR_INGAME/SKILL_EFT and actor-derived portrait; blindly assigning CUT_003 or CUT_004 is not supported. The four native dump review found no direct reference cut-field consumption in this view path. Original portrait/material failure remains possible and should be diagnosed only by exact native lookup/assertion or missing renderer, not assumed from empty cut field.

Original finish callback G9f5610 returns airship actor or applies exchange cooldown, ResumeGame(reason2), invokes model event0x11 and DeactiveSkill. No server HTTP receipt field is parsed there. The earlier G9f5198 wrong-mode decomp is unusable; Thumb evidence identifies a skill-tip callback, not the primary damage application. Complete causal timing from accepted actor result through HP application remains a measurement gap. The prior observed paused→normal E01 control supports finish event execution in that run, not complete healing/damage fidelity.

## Focused discriminator before more spending or trials

First corroborate current fixture branch/native slot1 cost and effect list from existing safe read-only diagnostic capability. During a controlled accepted gesture, distinguish (1) actual actor-bound press event, (2) protocol10/reservation with nonempty effects and one cost debit, (3) skill-view pause/portrait, (4) source/target effect application plus HP delta, (5) finish/resume. Cost never debited points upstream of accepted UseSkill; cost debited without HP effect points to result/target/application or immunity; pause without resume points to view/finish/materials. Preserve prompt ordinary attacks and stop at terminal screens.

No concrete coefficient-sign, zero-effect publication regression, missing server route or missing material was established by this review. This is an unresolved cause, not a conclusion that input alone explains E06 failures. Do not retune stats, clear native gates, force Rage or grant skills to turn uncertainty into a success claim.

## Live follow-up: support application now observed

2026-10-09 support-stun-001 validates the typed ACTOR_STATE reader: actual input-list Nene and source Tyltyl signed stun0 at the pre-input pause. A freshly reconstructed center3461437 tap then produced Tyltyl's partial player portrait transition, displayed Rage4-to0, green361 and NeneHP119-to449 during concurrent bleeding, followed by return to ship and ordinary combat. This closes visible support activation/application/finish for this run, without isolating exact float debit, sourceDEF, full runtime effect vector or pure net damage/healing. No server skill endpoint, stat retune or APK change was required. Older unobserved effect-path gaps above are historical for this positive control; do not generalize it to every Hunter or earlier press. See analysis/testing/support-stun-001/report.md.
