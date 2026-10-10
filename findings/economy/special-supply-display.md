# Special Supply display types and gold-only fixture prerequisites

2026-10-05. Read-only original ELF Thumb, completed special-supply parser dumps and current resource-serving source. No VM, device, source changes or grants. Addresses are Ghidra coordinates unless labeled ELF.

## Exact string and numeric types

ParseSpecialSupply Gf95bb8 reads these fields directly from each special[] row:

- **npc_id is a JSON string**: indexf95cc4, from_json<string>f95cd2, stored SPECIAL_SUPPLY_INFO+10. It is not a numeric NPC enum.
- **title is a string**: from_json<string>f95d20, stored+1c.
- **str_id is a string**: from_json<string>f96066, stored+54.
- **str_param is a string containing JSON**, not a JSON array value: from_json<string>f960b8. Empty string skips atf960ca. Nonempty text is parsed as JSON atf960de, iterated, and each element converted to string atf961b2 into vector+28. Safe neutral values are **"" or "[]"**; actual str_param:[] is the wrong outer type. For substitutions use serialized string arrays such as "[\"value\"]", with proper escaping.
- **expire_date is numeric**, stored its low32 word at+8 atf95cc0. Scalar numeric strings run through strtod, not an ISO date parser. Publish a JSON number; no date-format alias is justified.

This closes the string/type gap in special-supply-contract.md. Empty item_list/card_list/gem_list/skin_list remain the narrow gold-only unsupported-reward choice.

## Expiration0 has an explicit display branch

SceneSupply.PushList Ged7878 loads the copied row's expire_date ated7cca. **Zero branches directly toed7d3e and chooses9999 (MOVW#270f)**, then formats the day label. It is not a hidden date label and not an expired supply. A no-expiration local fixture may therefore use0, with the honest UI consequence that it shows9999 days.

Nonzero calls **SRCalculationRemainTime G10aca74 ated7cce**. This function obtains **CGMTime.GetCurUTC_0 at10acac0** and returns deadline minus that value at10acacc. PushList compares against3600 ated7cd4, divides by60 for minutes and uses day/hour constants later. This proves seconds-based absolute UTC-coordinate display rather than millisecond duration. It does not establish the original expiry policy or authorization checks for claims; server expiry validation remains separate.

## npc_id is an animation prefix; empty is unsafe to assume

PushList unconditionally constructs a CSRUIImageNode ated7b3a; reads SPECIAL_SUPPLY_INFO+10 ated7b8c; appends the literal **_TH** (LDR ed7b88 / ADD ed7b8a, append helpered7b92); and calls **LoadAnim ated7bae**. No empty-npc guard exists in that sequence. Therefore npc_id:"" requests `_TH`, and npc_id:"001" requests `001_TH`. Neither animation was verified. There is no GetNPCInfo lookup on this examined path; card IDs and animation prefixes are different namespaces.

A narrow already-supported **local portrait prefix is C001**. Historical native map-backdrop.md331 records working C001_TH/C001_THN. Current start-server.ps1 lines39..46 describe the preserved PAD art family and its default C001*.jet serving selection atline96; server.ts folds selected asset packages into E_NEW. The preserved **C001.jet** exists at1054905bytes with SHA256354b7ed832a450292caf9b127c004f5a759ea64c95ed87590917a2bd009a686a. Read-only JET inspection confirms embedded C001.png and C001_d.png. C001_TH is not a literal inside that raw multi-resource package; its exact animation descriptor was not freshly inspected in this lane. Consequently npc_id:"C001" is justified as an existing Lantern portrait fixture, **not** proof of an original SpecialSupply NPC identity or a fresh native render PASS. Verify current serving configuration still includes C001 art before testing.

## Plain title and receive completion

PushList's ordinary title branch tokenizes the stored title+1c around literal%s ated79da and appends string parameters when present. Empty str_id avoids the special EXPLORE_FRIEND_BONUS branch (length20/equalitychecked ed79a2..ed79c4). A plain local title with no%s and neutral str_param therefore follows the ordinary text path; it need not invent a localization key. The resulting UI_CM_LI_TL textbox is set ated7ade.

The positive individual/ReceiveAll routes are already pinned atede858/edc7bc. Success completion **ReqSupplyCB Gedc9a4** uses the returned list of cached SpecialSupply records to form display rewards, and constructs **CSRPopUpGetReward atedd39c**. The callback has error/full-card-inventory branches and refreshes displayed row user data. Thus the backend should return the claimed **target_inst_id array** referring to an actually cached pending supply; mutation alone with no matched cached supply cannot provide the same display list. For gold-only it avoids the requester filter for a single item of type0x1e and avoids card/gem/skin display parsing. It still needs a matching earned supply row and real coherent user.gold prev/cur receipt.

## Minimal neutral presentation choices

For an explicitly earned, persisted local gold supply, these are parser-supported presentation choices, not original balance:

```text
title: plain local research title
npc_id: "C001" (existing Lantern portrait fixture)
expire_date:0 (explicit9999-days display)
str_id:""
str_param:""
gold: earned local amount
all other numeric reward amounts:0
item_list/card_list/gem_list/skin_list:[]
```

Exact receive-control hashes/layout and all ReqSupplyCB result-popup dependencies were not fully audited here. Native render/claim testing must remain bounded and use actual earned source state; no starter grant, manual tutorial clear, APK asset patch or card-ID alias is justified by these findings.
