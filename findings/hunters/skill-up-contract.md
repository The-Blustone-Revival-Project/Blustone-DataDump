# Single owned-hunter SkillUp contract

2026-10-04. Read-only original-library Capstone and exact literal pairing. No adb/Ghidra/source/original edits. Addresses are Ghidra image addresses.

## Exact request

[RECOVERED] `CSRSyncCard::RequestSkillUp` (0xf558e8) posts **/gym/SkillUp**. Seven form keys are app_code, app_ver, market, pvid, otp, **target_inst_id**, **skill_idx**. Target is an owned uint64 instance serial; skill_idx is the passed SRSKILL_TYPE, formatted directly, with no recovered subtract1 conversion. Supported reference skill types are1..5.

Evidence: target_inst_id load0xf55a3e/addPC0xf55a46 ->0x1d6f8e7; skill_idx load0xf55ab4/addPC0xf55abc ->0x1d8f745; route load0xf55c3e/addPC0xf55c44 ->0x1d8f74f. The requester signature takes instance serial, skill type and callback; no desired level, source-item id, or idempotency nonce was found.

## Exact success shape

[RECOVERED] `ReqSkillUpCB` (0xf56074) consumes:

```json
{"result_code":1,"ret_data":{
 "user":{"gold":{"prev":1000,"cur":900}},
 "skill_idx":1,
 "target_inst":{"inst_id":2,"skill_1_level":{"prev":1,"cur":2}},
 "consumed_inst_list":[]
}}
```

The numbers are **[FIXTURE example]**; the shape is recovered. **target_inst and skill_idx are directly under ret_data**, not under card. The selected level field is dynamically formatted **skill_%u_level**. Send only the selected field when upgrading one skill; do not return scalar `skill_1_level:2` in this callback, because it indexes that value's prev/cur members.

- ret_data loaded0xf56180..86; retained in r6 at0xf5618c.
- Optional achievement at0xf56190 is null guarded0xf56196..98; omit it while unknown.
- ret_data.user indexed0xf561aa; gold indexed0xf561b4, prev0xf561bc, cur0xf56214. New gold is stored into playdata+0x154 at0xf5626a.
- ret_data.skill_idx: load0xf56268, slot0xf563b4, addPC0xf56272 ->0x1d8f745. Its scalar value is r4.
- target_inst: `mov r0,r6` at0xf562be proves ret_data ownership; index call0xf562c2; target object retained r6 at0xf562c8.
- target_inst.inst_id indexed0xf562cc and converted to uint64.
- skill field format **skill_%u_level** loaded0xf56316 and formatted with r4 at0xf5631c..20; lookup on target object0xf56330..32. cur lookup0xf5634a..4c; prev0xf563ce..d0.
- `CSRInventory::SetCardSkillLevel(uint64,SRSKILL_TYPE,unsigned)` called0xf56442. Instance id is passed via r2/r3; skill_idx/current level stack arguments come from r4/r5 at0xf5643e. Callback updates exactly that instance's selected skill field.
- ret_data.consumed_inst_list is indexed0xf56492..94 and passed to **CSRInventory::UseItem** at0xf5649c, unconditionally.

[RECOVERED no-item branch] UseItem (0xaea5f8) iterates the supplied JSON collection; array begin/end size is compared at0xaea63c..64a. Empty array has count0 and immediately exits0xaea702, before instance/qty decoding. Thus **consumed_inst_list:[] is a proved no-op** for a gold-only fixture. Do not fabricate original metron/material IDs. Positive consumption entries need separately validated instance/quantity accounting before enabling real material charges.

## Refusal and mutation integrity

ReqSkillUpCB checks transport callback status0 and response result_code1 at0xf560a6..b4; non-success jumps directly to callback delivery at0xf564e8 and skips mutation parsing. JSON result_code is checked again0xf56150..54. `CSRPopUpSkillUp::OnTrainingSkillUpEnd` (0xd59554) only takes ordinary success path forcode1 (0xd59572..74); specialcode10000 is handled separately, original business meaning not recovered. A non-success code is therefore a supported refusal path, but any local2001/other chosen code must be documented as local policy rather than an original business mapping.

Persist `ownedCard[skill_<idx>_level]`, gold, and any proven consumption together before success. Inventory/lobby/profile projections must show the same persisted level after restart. Check target ownership, selected type1..5, existing unlocked level, target-rank eligibility from its reference, and cap from its role/rank skill table. Inventory lock protects destruction; it is not evidence that locked targets cannot improve a skill.

Original success increment magnitude was not captured; **+1 per request** is the natural skill-training action policy, not a recovered server implementation. Original gold prices/material costs remain unknown. A gold-only fixture can use the independently recovered zero-source UI guards in `skill-level-reference.md`, leaving all four material refs empty/qty0 and consumed_inst_list[].

**Retry limitation:** request includes no current/desired level or nonce. Identical target/skill requests may be a legitimate next upgrade or a transport retry, so unconditional replay caching would block repeated intended training and unconditional mutation risks double spending after a lost response. Any retry window/local operation policy must be explicit and tested; no native token was recovered to solve it automatically.

`RequestMultiSkillUp` (0xf566c8) and `ReqMultiSkillUpCB` (0xf5700c) are separate symbols/paths. This report does not audit the multi-skill route or callback; do not map them to this single-skill parser by proximity.
