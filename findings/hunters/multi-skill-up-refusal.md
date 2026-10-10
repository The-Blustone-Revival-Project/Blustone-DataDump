# MultiSkillUp: exact request and safe refusal

2026-10-04. Read-only original-library inspection. No source/runtime/original changes. Ghidra addresses.

**Request route is /gym/MultiSkillUp**, `CSRSyncCard::RequestMultiSkillUp`0xf566c8; route literal0xf56ba0/addPC0xf56ba6. Fields include standard account metadata, **target_inst_id**, and exact misspelling **mulit_skill_up_count** (load0xf569e6/addPC0xf569ee ->0x1d8f796).

The requester takes a vector of SRSKILL_TYPE values. It counts occurrences of each type1..5, places counts at array index(type-1), then JSON-dumps the five-element array. Example vector[1,1,3] produces the form value **[2,0,1,0,0]**. Evidence: count comparison0xf56764..6c, array indextype-1 at0xf5677e, type-loop until6 at0xf567aa..b2, dump0xf567c0..d0. This is neither a bare total qty nor a list of instance IDs.

## Non-success safely skips mutation parsing

`ReqMultiSkillUpCB`0xf5700c:

- Nonzero transport status at0xf5703a..3c jumps to callback0xf575a4.
- Response result_code!=1 at0xf57046..48 jumps to the same callback, **before decryption/user/card/item reads**.
- Parsed JSON result_code!=1 also bypasses ret_data:0xf570e4..ea ->0xf5758a cleanup/callback. Callback receives the original non-success code and initialized zero result-parameter block.

Thus an **explicit non1 refusal** is the proven minimal implementation while multi-upgrade accounting is absent. Chosen refusal code is local policy, not a recovered original business-code mapping. A generic result_code1 with metadata ret_data is unsafe now that expanded cap rows may expose this UI operation.

## Success differs from the single callback

Success consumes optional user.gold prev/cur, optional achievement, direct **ret_data.target_inst.inst_id**. It loops skill types1..5, formats a level-field string, null-checks each selected field at0xf574c8..cc, reads its cur and calls SetCardSkillLevel0xf5754a. Missing skill fields therefore skip mutation; supplied fields need the proper nested cur value. The generated name is evaluated from explicit literals/operand flow; do not assume the single callback's skill_idx field exists here.

**consumed_inst_list entries are parsed using remaining quantity**, not the single callback's UseItem(delta) path. The callback reads an inst_id key and **remain** (resolved load0xf57286/addPC0xf5728c), then mutates inventory through a separate setter. Empty or absent list skips iteration0xf57220/0xf57298..9e. A positive-entry accounting implementation requires a separately completed material/remaining-quantity contract; do not guess source item IDs or apply the single callback's consumption model to this route.

This lane prioritizes the verified refusal and does not recommend shipping a multi-success response from this abbreviated audit. Single skill upgrade can remain usable while multi-upgrade explicitly declines.

## Follow-up: completed success parser audit

The generated slot field is exactly **skill_%s_level**: load0xf57468 ->slot0xf577a8; addPC0xf57476 yields the format. The loop converts types1..5 to decimal strings (0xf57496..9a), formats the field and indexes target_inst0xf574c0..c4. **Each missing field is explicitly null guarded** at0xf574c8..cc. For a present field it indexes only **cur** (slot0xf577ac/addPC0xf5747a; call0xf574d0), converts to unsigned current level, and calls `CSRInventory::SetCardSkillLevel(instance,type,current)` at0xf5754a. **Skill prev is not read; all five fields are not mandatory.** A response can carry exactly changed slots, each as `{cur:N}`. Including truthful prev as well is additive, and gives local diagnostics/reviewer visibility.

Full parser-compatible gold-only example:

```json
{"result_code":1,"ret_data":{
 "user":{"gold":{"prev":1000,"cur":500}},
 "target_inst":{"inst_id":2,
   "skill_1_level":{"prev":1,"cur":3},
   "skill_3_level":{"prev":1,"cur":2}},
 "consumed_inst_list":[]
}}
```

Counts and gold are illustrative local-policy values. The callback does **not** read a response skill_idx, count array or upgraded-count field in its complete inspected range0xf5700c..0xf575c8. It enumerates allfive possible target fields instead. Request count field need not be echoed for native mutation.

**Consumption is now pinned:** each consumed_inst_list element is `{inst_id:<uint64>,remain:<uint32>}`. `inst_id` is the literal loaded0xf5727c, slot0xf57364/addPC0xf57286; `remain` load0xf57286, slot0xf57368/addPC0xf5728c. The new absolute quantity r4 is stored as argument at0xf57392; instance low/high passed throughr2/r3; call0xf57394 resolves to **CSRInventory::SetItemQuantity(uint64,unsigned)**0xaec4bc. It is an absolute remainder, not qty-to-subtract, added delta, or item ref id. For gold-only fixtures, explicit empty list skips the iterator and changes no items.

**User is optional** at0xf5714e..52; when supplied, user.gold must carry prev/cur numeric values. Both are stored in the result parameter atsp+0x78/0x7c, and cur is written into playdata+0x154. Optional achievement is null guarded. Target_inst is null guarded0xf5740a..0e; a positive instance id is required for mutations (zero branches out0xf57438..3e). For a meaningful successful upgrade, supply the owned target plus every changed slot rather than using these guards to fabricate a no-op success.

**Result callback detail:** this multi callback initializes16bytes of SKILL_UP_PARAM to0 and populates gold prev/cur; it does not populate the single callback's level-prev/cur pair atparameter+8/+12. Its supplied caller callback must therefore be the genuine multi-training path. If a test manually feeds this response through the single SkillUp caller, the single UI ActionReady reads those zeros, which is not a valid end-to-end batch test. Native mutation parser proof does not yet establish batch animation/UX; exercise the original MultiSkillUp request path.

For atomic server implementation, validate the entirefive-count vector, ownership, unlocked slot eligibility, per-slot cap after applying its requestedcount, aggregate local gold cost, and any reconstructed real material requirements **before any mutation**. Sum each intermediate level's price when count>1 rather than charging one initial price for several upgrades. Keep all zero-cost/material-free values labeled fixtures; do not infer item IDs. Persist gold and all changed individual skill fields together, return truthful absolute current levels, and test restart/isolation/whole-batch refusal. Native request still supplies no expected version or nonce; retry ambiguity remains the same local-policy decision as single SkillUp.
