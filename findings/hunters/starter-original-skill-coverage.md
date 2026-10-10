# Starter Hunter skills: original Episode coverage and publication limits

2026-10-09. Read-only original exported STAT/COMBAT, current `skills.ts` and existing parser/mechanics reports. No Ghidra, ADB, grants, balance changes or fresh visual-stat hunts.

## Provenance and coverage

`EPISODE_COMBAT_STAT.manifest.json` identifies preserved final PAD **R_EPISODE.jet**, SHA2567f4362cdf80545a6da937444094837f334c8aae4f9f791d6ff4161948d98a01e, resource index3/RW payload3 -> `EPISODE_STAT_ACTORS.json`, SHA256f3b8cb90372c89490467e75ed0564bfc3f8a4d094370264caa2c821b0eb13b56. This is shipped **Episode-only** actor data, not a captured ordinary GetCard response.

Seven Hunter rows match original resources C001/C003/C004; **no C002 or ref002 row** exists in this export. Row55 `CB0001_M01` has ref_id001 but **resM001**, role1, skills[]: it is not Lantern and must not enter a ref_id-only skill join. Match full actor identity and art/role, not a substring or bare ref ID.

Below effects use the exact shorthand `(effect_type,target_type,target_stat,refer_target_type,refer_target_stat,base_number,duration_ms,interval_ms)`. All exported skills have type==target_rank. None of these seven rows includes effect up_number/duration_up, ordinary level-price/growth rows, names/descriptions, icon_id or cut_in_id. Missing growth is not evidence of the final ordinary upgrade policy.

## Exact original rows

- **Row49 CB0003_C001**, ref001/resC001/role3/rank4: skill1 cool5000/cost4/crit100, effects `(1,1,1,1,1,-2000,0,0)` and `(4,1,16,2,0,-3,200,0)`; skill2 `(4,1,4,2,0,-30,4000,0)`; skill3 `(2,3,14,2,0,10,300,0)`; skill4 `(1,1,1,1,1,-1000,0,0)` plus the same stat16/-3/200 effect; skill5 `(2,3,6,2,0,15,300,0)`. This is the sole complete1..5 Lantern tuple in the export. Original CB0003 combat enables `[1,1,0,1,0]` for this actor, so published rows3/5 do not imply those passives are active in that scripted fight.
- **Row81 CB1101_001_1**, ref001/resC001/role3/rank5: skill1 cool5000/cost4/crit50, `(1,1,1,1,1,-1500,0,0)`; skill2 `(4,1,4,2,0,-20,5000,0)` plus `(4,1,16,2,0,-3,200,0)`; skill4 `(1,1,1,1,1,-1500,0,0)`. No types3/5.
- **Row47 CB0003_C003**, ref003/resC003/role2/rank4: skill1 cool5000/cost3/crit100, `(1,1,1,1,1,-2000,0,0)`; skill2 `(4,1,15,2,0,1,1500,0)`; skill4 `(1,2,1,1,6,100,3100,1000)`. No types3/5.
- **Row63 CB0101_003_1**, ref003/resC003/role2/rank3: skill1 cool5000/cost3/crit100, `(1,1,1,1,1,-1800,0,0)`; skill2 `(4,1,15,2,0,100,2500,0)`; skill4 identical to CB0003_C003. No types3/5.
- **Row77 CB1101_003_1**, ref003/resC003/role2/rank5: skill1 cool5000/cost3/crit50, `(1,1,1,1,1,-1500,0,0)`; skill2 `(4,1,15,1,0,1,2000,0)`; skill4 `(1,2,1,2,4,8,4100,1000)` plus `(3,2,19,1,0,1,4000,0)`. No types3/5. The changed refer_target_type on skill2 and changed skill4 references must not be silently unified.
- **Row18 EVCB0201_004**, ref004/resC004/role4/rank5: skill1 cool5000/cost4/crit50, `(1,4,1,1,3,150,0,0)`; skill2 `(3,4,6,2,0,20,4000,0)`; skill4 `(5,4,19,2,0,10,4000,0)` plus `(1,4,1,1,3,20,0,0)`; skill5 `(2,3,13,2,0,100,300,0)`. No type3. Original EVCB0201 fixed party is an event encounter; its descriptors include high-level/rank/hyper scripted actors, not a native owned starter receipt.
- **Row129 CB1602_C004**, ref004/resC004/role4/rank5: skill1 cool5000/cost4/crit50, `(1,4,1,1,3,160,0,0)`; skill2 `(3,4,6,2,0,30,4500,0)`; skill4 same stat19/type5 effect as EVCB0201_004 plus HP1/base24 heal. No types3/5.

## Mechanism corroboration versus ordinary compatibility

Episode FindActorRef/ParseActor constructs local CardInfo keyed by full actor ID, parses stat through CSRCardStat and skill through **SRSKILL_INFO::parse**, then binds each type using SetSkillInfo. Owned ordinary reference publication uses the same skill parser/backend mechanism, so numeric fields are usable **as mechanisms and scripted-row fixtures**. It does not establish that ordinary003 skillLV1 should receive a CB0101 encounter-tuned1800 coefficient.

Native processing normalizes base/up by100 and duration/interval by1000, then applies owned skill level to growth terms. Slot1 original Lantern/Nene coefficients are -20/-18/-15, versus current local fixture -1 atLV1. Blind replacement would increase direct skill magnitude15–20 times. Higher scripted ranks do not monotonically raise those coefficients, disproving a simple rank-derived ordinary growth rule. Tyltyl's two rank5 encounter rows differ150 versus160 and secondary20 versus24, also proving no single invariant ordinary tuple from this corpus.

The recovered Tyltyl positive sourceDEF/FrontAlly/HP1 and Nene negative sourceAtk/Enemy/HP1 support the current mechanism selectors/costs; they do not recover current ordinary up_number5, crit policy, cooldown0 or level progression. Native supporter/front admission, nonempty effects, cost debit, target HP application and finish callbacks still require actual validation. Root's accepted ordinary Tyltyl heal is current fixture evidence, not validation of event-row150/160.

Types2/4 expose real original follow-up tuples, and Lantern types3/5 plus Tyltyl type5 expose original aura/passive mechanisms. Complete enum/application/trigger admission matters: e.g. stat15 stun is recovered, but copying duration/base alone cannot prove follow-up triggers, stat16 immunity penetration or effect_type5 behavior. Do not equate a field label or shipped prose with complete immunity mechanics. Existing `starter-skill-combat-mechanics.md` specifically leaves Lantern Invincible penetration incomplete.

## Actionable options

1. Keep exact scripted skills in their original Episode actors and validate the actual relevant encounter/materials. This advances recovered content without changing owned Hunter balance, earned skills, ranks or EXP.
2. Close native types2..5 construction/trigger admission and their enum branches using these original tuples as evidence. In particular, verify slot2 follow-up and slot4 trigger timing, zero owned skill-level behavior and required actor materials before publishing anything to ordinary cards. An added ordinary adapter must retain all five slots for popup lookups; absent Episode slots are partial coverage, not a license to remove them.
3. If an ordinary adapter is later selected, explicitly name the precise Episode actor source and mark transferred coefficients/cooldowns/zero growth as **Episode-derived local policy**, with separate opt-in profile and owned-level/rank compatibility checks. Do not call it recovered ordinary final-server skill balance. Preserve current saved skill levels; never reseed0→1 or grant rank to force passive eligibility.
4. Mowgli002 still needs original numeric skill evidence outside this Episode export. Existing shipped skill text/formulas support its bleed mechanism but do not supply absent numeric network coefficients. No new visual hunt or arbitrary reuse of another Hunter's row follows from this gap.

No ordinary reference or runtime change is warranted solely by this audit. It identifies concrete original mechanism coverage and avoids turning encounter-specific data into an undocumented combat buff.
