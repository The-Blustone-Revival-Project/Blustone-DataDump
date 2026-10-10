# Search capsules and Lapis identity

2026-10-05. Read-only recovered resources, existing native decomp/literals, original ELF verification and preserved community FAQ. No grants/source/client/runtime/Ghidra/adb edits.

## Exact capsule inventory reference

**AIRSHIP_TICKET** is a verified native inventory reference, not a guessed abbreviation. Search entry function builds this exact string and passes it to Inventory.GetInstItemCnt in ghidra-find-shard-entry-contract.txt around line395. Exact register-matched literal: LDRGe23f36 reads slotGe242b4; ADDGe23f38 uses architecturalPCGe23f3c, resolves G1d7f0b5 bytes AIRSHIP_TICKET followed byNUL. Original ELF PT_LOAD read agrees with ghidra-find-shard-exact-keys.txt. This code directly looks up inventory by ID; it does not need a GetItemRefID(use_type) lookup to establish capsule count.

**Unknown original metadata:** AIRSHIP_TICKET's use_type/rank/name/thumbnail/effect/prices and original acquisition payouts. Recovered all-tables/recovered-reference has no ITEM_REF table. Do not infer use_type1(AP),2(BP),3(hunter traces) for capsules merely because those enums are known elsewhere. No original item-definition row was found in this pass.

Preserved UI_TEXT_RO exact record key `아참 앞으로 계속 비행선을 이용하려면` says in EN that continuing to use the Aircraft requires a Helium Capsule, with KO/JA/SC/TC corroboration. Parent's native guide shows cost1 and capsulecount0; this is a current observation, not an acquisition grant or proof of every original Search's cost.

## Acquisition and reward evidence limits

FAQ lines259..265 discusses Missing Hunter Ruins: daily limited attempts, dispatches can trigger a new ruin, friend support can assist; dated2019-04-01 note says this activity uses Helium Capsules instead of fuel, and its rewards became hunter traces/metron fragments. This is preserved community guide text, not a final2.8.0.1 server response or precise capsule-supply schedule. It does **not** state capsule acquisition amount, daily refill, price or grant route.

RequestBegin G90eec0 / ParseBegin G915d6c, RequestReward G9118b8 and Retry G912578 belong Search transactions, not proved capsule acquisition routes. Next narrow purchase/quantity consumer to inspect is SceneFindShard::OnButtonClick Ge24880 and FindShardConfirm OnButton Gbe558c, especially RE_BUY/PA_TK_SE branches. A purchase opening alone does not establish its server route or original price. No invented mail/daily grant proposed.

## Independent Lapis card identity

Guide's hardcoded UI node **017** remains a Search reference id generated from Search INFO.id; it is not by itself a card-ref proof (search-guide-target-contract.md).

Independent catalogue evidence now supports **hunter017 = Lapis**:

- analysis/catalogue/data/cards.json and analysis/catalogue/cards/017.md link card_id017 to community name Lapis,1-star,Ice/Offense: https://blustone.miraheze.org/wiki/Lapis . These identity/element/rarity fields are COMMUNITY-SOURCED, not an original captured GetCard.base row.
- Preserved CHAR_STR_RO exact **017|TITLE** EN `Speedy Swordsman`; **017|SUMMARY** explicitly identifies an Offense with high attack speed and critical damage. These title/role descriptions are RECOVERED original resources. Gear/description records under017 and017_1 exist; no NAME record was found in the inspected exact keys.
- Original PAD resource files **C017.jet, C017_Q.jet, C017_EFT.jet, C017_SND.jet** exist. This establishes art coverage candidates, not exact original skill/resource bindings or stats. Ordinary base stats remain unknown, as its dossier states.

Thus assigning target_card_id017 could be an evidence-backed reconstructed Lapis binding after publishing a structurally valid card/reference/art set, but an original Search row with target_card_id017 was not recovered. Existing Search017→published006 fixture should remain explicitly labeled compatibility content until that additive restoration is deliberately implemented/tested. No hunter17 or capsule was granted by this lane.
