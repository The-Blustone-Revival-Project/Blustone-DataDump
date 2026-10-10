# Selected ordinary Hunter adapter: original types3..5 coverage

2026-10-09. Read-only audit of current AGENTS.md §189, skills.ts, the pinned original Episode exports and retained native contracts. No ADB, Ghidra, runtime reads, account changes or source edits. Only this report was written.

## Source identity and exact missing vectors

The original EPISODE_STAT_ACTORS.json SHA256 is f3b8cb90372c89490467e75ed0564bfc3f8a4d094370264caa2c821b0eb13b56, checked again in this audit. EPISODE_COMBAT_STAT.manifest.json traces it to preserved final PAD R_EPISODE.jet SHA2567f4362cdf80545a6da937444094837f334c8aae4f9f791d6ff4161948d98a01e, resource index3/RW payload3. Ordinals below are zero-based. These are encounter reference rows, not recovered ordinary GetCard balance.

Each effect tuple below contains all eight original numeric fields in order:
(effect_type,target_type,target_stat,refer_target_type,refer_target_stat,base_number,duration_ms,interval_ms).

- STAT[49] CB0003_C001: ref001/resC001/role3/attr1, STAT rank4. Type3/target_rank3 has one effect `(2,3,14,2,0,10,300,0)`. Type4/target_rank4 has two effects in original order: `(1,1,1,1,1,-1000,0,0)` and `(4,1,16,2,0,-3,200,0)`. Type5/target_rank5 has one effect `(2,3,6,2,0,15,300,0)`.
- STAT[47] CB0003_C003: ref003/resC003/role2/attr2, STAT rank4. Type3 and type5 are absent. Type4/target_rank4 has one effect `(1,2,1,1,6,100,3100,1000)`.
- STAT[18] EVCB0201_004: ref004/resC004/role4/attr1, STAT rank5. Type3 is absent. Type4/target_rank4 has two effects in original order: `(5,4,19,2,0,10,4000,0)` and `(1,4,1,1,3,20,0,0)`. Type5/target_rank5 has one effect `(2,3,13,2,0,100,300,0)`.

All these original secondary skill objects contain only type, target_rank and effect. They contain no independent cool_time, cost or crt_chance. Their effect objects contain no serial, up_number, duration_up, value_calc or effect_desc. Neither the secondary skills nor these selected main rows recover ordinary skill names, descriptions, icon_id or cut_in_id. Normalizing absent growth to0, assigning serial1..N, neutral secondary metadata and retaining reconstructed presentation bindings are local adapter policy, not newly recovered fields.

For completeness, selected slot1 metadata remains Lantern cost4/cool5000/crit100, Nene cost3/cool5000/crit100 and Tyltyl cost4/cool5000/crit50. It is that slot1 critical metadata which configures type4's conditional rule under the normal actor flag branch; inventing a secondary skill critical chance is unnecessary.

The original CB0003 COMBAT descriptors for Lantern and Nene each carry `[1,1,0,1,0]`, with thumb rank4. Do not treat the zeros as a proved universal passive-disable gate: the native constructor separately selects references, compares actual rank and uses selected levels arithmetically. In particular an admitted level0 passive retains base values. The thumb and selection descriptor alone do not prove actual Analyzer inputs or live aura delivery.

## Native admission and what publication would change

Retained skill-followup-construction-contract.md and skill-passive-registration-contract.md establish separate paths in Hunter MakeBackEndActor G9ac2ac:

1. Types3/5 require a nonnull selected reference and actual Analyzer rank >= reference target_rank (G9ada16..28/G9adbdc..ee). Their exact owned map keys3/5 must exist. There is no positive-level gate before AddAura. Coefficient and duration use parsed base + up*level; level0 retains base. Nonempty effects become source AURA rows, not immediate HP damage or extra user skill buttons.
2. Type4 similarly requires reference/rank and owned key4 (G9ad4de onward), with level0 retaining base. Its INFO enters a conditional rule beside the main active list. Normal ACTOR_INFO mask5-clear construction divides slot1 crt_chance by100 into default-state44; alternate flag paths may use selected tuning.
3. SkillMgr.Buy G9b23bc draws random0..1 against configured probability plus adaptive adjustment. A miss adds0.1 and hit subtracts0.1. This is not a fixed independent probability and zero configured chance does not prove eternal suppression. The selected additional results share one accepted active reservation/cost; publication is not evidence of a live accepted trigger.
4. SRSKILL_INFO::parse normalizes base/up by100 and duration/interval by1000. Thus Lantern type3's numeric payload is coefficient0.1/duration0.3s; type5 coefficient0.15/duration0.3s; Tyltyl type5 coefficient1/duration0.3s. These are payload signatures, not isolated measured stat gains.
5. AddAura appends stridee8 rows with a generated64-bit identity at e0/e4. UpdateAura resolves recipients, checks running gates and AddAuraEffect correlates recipient buff identity. Recharge resets remaining lifetime without unconditional new stacking. Root's existing owner-qualified observer can distinguish source registration, serial-matched admission and actual stat changes; each is a different claim.

Current episode-actives publication includes original slots1/2 only, with empty3..5. Current party ordinary Lantern/Tyltyl ranks1 and Nene rank3 do not admit any newly populated row above: Lantern requires3/4/5; Nene's only extra is4; Tyltyl requires4/5. Therefore complete reference publication can advance coverage for earned higher ranks, but does not supply an immediate CB0602 win or justify rank/level grants. Mowgli002 has no matching original Episode row and must keep its declared fixture; do not join the monster CB0001_M01 merely because ref_id001 matches Lantern.

## Precise next implementation and validation

Add a separate opt-in complete Episode-derived ordinary adapter profile, preserving neutral, fixture, episode-followups and episode-actives byte-for-byte. Extend the same full-identity selected source rows already used for slots1/2 to all present3..5 vectors above. Preserve missing type3/type5 slots as empty mandatory native keys, exact target_rank, effect order and cardinality, no unsupported Mowgli substitution, zero growth policy and caller clone isolation. Do not synthesize passives from another encounter variant.

Tests should pin the source hash when the private original export is available and compare every original tuple field and target_rank, then cover rank boundaries/level0 serialization, all five owned keys, unchanged saved ranks/levels/decks/economy and unchanged old-mode publication. These establish fidelity of the adapter and preservation, not native combat activation. Live validation should retain the current earned party and first show that below-rank ordinary actors gain no constructed extra results/auras. Eligible original fixed Episode actors can exercise native pathways without owned grants; actual Analyzer rank/reference/level and full aura identity must be observed before application claims.

Raw target_type3 and target_stat6/13 meanings and the complete effect_type5/stat19 path are not closed by these selected-row exports. Stat14's AddBuffAtk multiplier branch is recovered in starter-skill-combat-mechanics.md, but target resolution and immunity still apply. Do not replace unknown tags with friendly labels or convert Tyltyl effect_type5 into ordinary Buff3. Final ordinary magnitude/growth, presentation resources, all target selectors and exact passive removal/trigger outcomes remain incomplete.
