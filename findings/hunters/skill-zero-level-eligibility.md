# Eligible zero-level hunter skills can train 0→1

2026-10-04, read-only original ARM library inspected as Thumb with Capstone, prior exact SkillUp/RankUp reports. All addresses Ghidra (ELF+0x10000). No adb/Ghidra/server/original edits.

## Native UI proof

`CSRPopUpSkillUp::Select(SRSKILL_TYPE)` Gd55bfc finds owned card and reference selected skill. It reads the owned skill-level map (card+0x38 map tree); missing selected entry sets current level0 at Gd55d16, with actual found entry read at Gd561e4. Current value is saved at sp+0x20. This is a native zero default, not evidence that every slot is automatically initialized to1.

**The price getter is never asked for level0 in this selection path.** Gd55dac loads current from sp+0x20; Gd55dae computes current+1 into r4; Gd55dce passes r4 as price level; Gd55dd0 calls `CSRUserLV::GetCardSkillUpPrice` G10a0f60. Thus owned0 prices target1 safely. The getter itself remains unsafe for input0 because it indexes level-1, but this caller avoids that input. Dense price rows are indexed by destination level, so backend price selection should agree with current+1, not current.

Button enable tests are explicit: Gd56030 loads cap(sp+0x1c) and current(sp+0x20), Gd5603a..3c requires current<cap; material validity and sufficient gold follow; Gd5604a..54 reads owned rank card+0x24 and reference `SRSKILL_INFO.target_rank`+0, requires target_rank<=owned rank. Successful branch Gd561e8 passes1 to `SetEnhanceButtm_onActive` Gd57620. **There is no current>=1 test.** Zero with an eligible target rank, positive cap, and available costs reaches enabled training.

## Exact supported backend rule

Use existing `/gym/SkillUp` target_inst_id + skill_idx request. Allow current0→1 only when the selected reference slot exists, target_rank<=owned rank, cap>=1, and costs are payable. Persist the selected owned skill level and gold atomically. Keep rank-ineligible zero slots refused. Locking the card protects destructive consumption, not target improvement.

Existing recovered callback accepts the same shape with `skill_N_level:{prev:0,cur:1}` plus selected skill_idx, target_inst.inst_id, user.gold prev/cur, consumed_inst_list[]. Native ReqSkillUpCB Gf56074 calls SetCardSkillLevel Gaea2d0 with absolute cur; no separate unlock route or different callback is needed. This is structurally proven; original server business policy and original cost numbers remain unknown. Gold-only fixture zero-material guards are documented in skill-level-reference.md.

RankUp callback uses SetRank and does not mutate individual skill levels, as documented in rank-up-contract.md. Preserving zero through promotion is therefore compatible with explicit first training once eligible. Do not eagerly reseed all slots to1 on every login/promotion, which would alter existing ownership progression. Conversely, do not require current>=1 just because initial grants start some eligible skills at1.

## Remaining constructor/original-policy limits and next parent dumps

This pass does not prove original grant-time all-slot defaults, free automatic initialization, or original unlock prices. Native missing-map→0 and explicit0→1 enabled selection are sufficient to remove the backend blocker without guessing those policies.

Parent-only focused evidence preservation: Select Gd55bfc through next function Gd563a0 (especially Gd55cea..d55d18, Gd55dac..d55dd0, Gd56030..d56054 and Gd561e4..d561f0). Optional original defaults follow-up: CSRCard default constructor G86f850, CSRCard::parse G8680a4, SetRank G869c70, SetSkillLV G869f3c. Do not infer constructor initialization from only current grant fixtures. No research-only lane changes applied.

## Price arithmetic correction, exact getter and multi follow-up

GetCardSkillUpPrice G10a0f60 preserves incoming level in r8 at G10a0f78. G10a1054..56 returns default if vector count<input level. G10a1058 subtracts1 into index; G10a105c..5e throws if count<=index; G10a1060..62 returns begin+0x4c*index. There is **no clamping**. Therefore destination T selects vector[T-1]; next upgrade from owned L is T=L+1 and selects vector[L]. Earlier notes discussing vector[level-1] were getter-parameter arithmetic, not proof to pass owned level. For L0, T1 safely selects first row. Preserve prior persisted charged balances; correction applies to future operations.

All executable direct callers identified: Select Gd55dd0; SimulateSkillUp Gd589dc/Gd58eca; ActionReady Gd59de6; RefreshItem Gd5ae94. SimulateSkillUp Gd587f8 reads selected simulated owned level at [sl+0x14], adds1 at Gd589d8 and Gd58ec6, then calls getter. Thus its current next-upgrade price also uses the destination. To prove batch accumulation exactly, parent should dump SimulateSkillUp Gd587f8 and ActionReady Gd59650. Expected sum over destination L+1..L+n is an inference until that accumulator loop is recovered; no original price numbers asserted.
