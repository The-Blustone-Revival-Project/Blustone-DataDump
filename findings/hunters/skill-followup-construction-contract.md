# Hunter follow-up and critical construction contract

2026-10-09. Read-only original Thumb, existing symbol/export tables, STAT exports and current `skills.ts`. No Ghidra, ADB, state/reference changes or balance retune. Addresses use Ghidra coordinates (ELF codeVA+10000). This closes construction/selection, not every downstream buff application or original ordinary server value.

## Type2 belongs to the ordinary active effect list

Hunter **MakeBackEndActor G9ac2ac** saves owning rank from CardAnalyzer.GetRank at G9acef4..f8. It finds reference type1 at G9acf12, requires nonnull reference and owned rank>=target_rank at G9acf16..24, creates an **ACTOR_SKILL::_INFO** from a typed pool, and builds its result list at INFO+5c. Type1 cost is copied from reference+48 into default state+48.

After type1 effect construction, it finds reference **type2 at G9ad20a**, tests nonnull and the same rank gate at G9ad20e..21c. It searches the owning skill-level map for key2 via GetSkillLV G86f404 at G9ad222. Found node's unsigned value+14 becomes float at **G9ad258..266**. Each reference effect is copied into the SAME main active INFO result list+5c, not a new separately pressed skill.

Coefficient and duration apply the same rule as type1: parsed base + parsed up*owned level. Instructions **G9ad2ac..2ce** adjust scratch coefficient/duration; nested result rows are adjusted at G9ad2d4..2fa, then copied into a result node appended to INFO+5c at G9ad278..3d4. Consequently a type2 follow-up is returned with the normal type1 active effect, under the same one reservation/cost; this construction contains no second Rage debit or separate user skill button.

## Zero owned level is not a construction disable

There is **no currentLevel>0 gate** in the inspected type2 branch. The owned unsigned level is used arithmetically, including zero: base+up*0 leaves the base coefficient/duration. The map lookup itself requires the key; missing key follows the native error/throw path (G9ad23c/G9ad240), not an implicit skip. Current owned inventory publishes all five level fields, including0; preserve those entries.

Thus publishing a nonempty original type2 row for current Nene rank3/skill2LV0 may produce its base follow-up immediately, without an earned0→1 upgrade. Do not silently assume LV0 means inert, grant a skill level to force it, or add a backend positive-level gate and call it native. Rank admission remains separate; Tyltyl/Lantern/Mowgli currently rank1 fail type2 target_rank2 before this arithmetic.

## Type4 is a conditional additional active result

Reference **type4** is selected at **G9ad4de**, gated nonnull and rank>=target_rank at G9ad4e2..f0. It creates another typed ACTOR_SKILL::_INFO at G9ad512..51a with its own result list+5c. Owning key4 level is found at G9ad602..628 and converted at G9ad63a..648; again no positive-level test precedes result copying. Missing map entry errors; zero preserves base terms.

For ordinary ACTOR_INFO flags (mask5 clear), **G9ad4fe..50e** converts slot1 reference `crt_chance` (+4c) to float, divides by100, and stores default state+44. Alternate ACTOR_INFO flag paths retain their selected tuning rather than this normal branch; do not overwrite those flags or call the probability universal across scripted actors.

The type4 INFO is appended as a20-byte conditional rule to the outer ACTOR_SKILL at **G9ad84e..8a0**: INFO shared pair at rule+0/+4, tag1 at+8, configured probability at+c from default state+44, initial adaptive adjustment+10 zero. The main INFO remains separately assigned to outer ACTOR_SKILL+18/+1c at G9ad498..49c. This is an additional conditional result alongside the main active, not replacing its original damage or charging another skill.

Outer skill is registered through **CSRGameActor.ResistSkill G97e8c8** at G9ad92e (with a separate monster-prefix handling branch). This registration is not a `/gym` or HTTP route.

## Runtime selection and adaptive probability

Group.UseSkill **G9a4084** verifies cost<=actual groupSP and live/running actor, passes unsigned currentSP to Actor.UseSkill G981910 at G9a413a, and debits original cost only if the returned effect-list is nonempty (G9a4142..4158). Actor.UseSkill obtains the registered skill and calls **SkillMgr.Buy G9b23bc at G981a4c**. Its uint argument is supplied SP, not a directly supplied “critical=true” flag.

Buy validates item admission/cooldown/availability, then traverses conditional rules. It draws native random0..1 at **G9b2622**, compares against **rule+c configured probability + rule+10 adjustment** at G9b2626..63e. If random>=sum, the miss branch **G9b260c..2610 adds0.1 to adjustment**; a hit **G9b2640..2644 subtracts0.1**, then creates a GAME_ITEM carrying the rule INFO/tag. The normal main INFO is also emitted by G9b26fc..2790. Literal floats are original G9b2898=+0.1 and G9b289c=-0.1.

This is not an independent fixed Bernoulli probability on every use. In particular **configured crt_chance0 is not proof that a constructed type4 rule can never trigger**: misses increase its adjustment. This corrects the research lane's intermediate message speculating zero means never selected. Current fixtures still have empty type4 effects and current original party ranks1/1/3/1 are below target_rank4, so no useful type4 result is currently reconstructed; filling it later changes behavior materially.

Existing Actor.UseSkill applies GAME_ITEM INFO result lists to its returned reservation effects; downstream target/defense/immunity/periodic behavior remains governed by the already recovered BuffInfo pipeline. Construction plus probabilistic selection alone does not prove successful live stun/heal/critical animation.

## Original tuples that can exercise these mechanisms

Exact originals are enumerated with source ordinals in `starter-original-skill-coverage.md`:

- Nene `CB0101_003_1` type2: Debuff4/Enemy1/stat15, base100/duration2500; main skill cost3. `CB0003_C003` uses base1/duration1500; `CB1101_003_1` uses base1/duration2000 with a different reference-target selector. Do not collapse those encounter variants into a recovered ordinary growth curve.
- Lantern `CB0003_C001` type2: Debuff4/Enemy1/stat4/base-30/duration4000. Its type4 carries additional damage base-1000 and stat16/base-3/200ms. Later `CB1101_001_1` differs, including where the stat16 effect appears.
- Tyltyl `EVCB0201_004` type2: Buff3/FrontAlly4/stat6/base20/duration4000. Type4 contains effect_type5/stat19 plus sourceDEF heal20. `CB1602_C004` differs in type2 base30/4500 and extra heal24. Effect_type5/stat19 admission is not completely explained by this construction review.

Type3/5 passive branches are separately rank-gated at G9ada16..28 and G9adbdc..bee, find owned keys3/5, scale base/up with those values and populate default-state effect data rather than the above main/conditional INFO lists. Their complete activation clock/aura lifetime remains outside this focused type2/type4 closure; do not equate a0-level passive base with proved live admission.

## Implementation limits

The source currently publishes nonzero type1 fixtures only; all types2..5 remain empty. Restoring an original Episode actor's intact tuples can validate the native mechanisms without changing ordinary ownership. Publishing an ordinary follow-up adapter must explicitly label its selected encounter tuple and zero-level behavior as Episode-derived local policy, preserve saved skill levels/ranks, keep five reference slots, and validate actual returned effects/one cost debit/target change/finish. Original final ordinary magnitude, per-level upgrades and activation names/material bindings remain missing. No retune or reference edit was made by this lane.
