# Episode reward material identity and reference limits

2026-10-05. Read-only recovered S01 graph, preserved LevelDB export, original PAD UI_ITEM/UI_ITEM_CHA package header inventory, original ELF Thumb instructions and existing native parser dumps. No inventory grants, source/VM/Ghidra/original edits. Addresses below are Ghidra coordinates (ELF + 0x10000).

## Original reward declarations are recovered

`analysis/recovered-reference/EPISODE_S01.json` preserves these chapter rewards, all with `free_iap:0`: E01 GC2 x3; E02 FMD1 x30; E03 GC3 x3 plus GC4 x3; E04 GC8 x1; E05 AIRSHIP_TICKET x20; E06 OV1 x10; E07 CERUM01 x20; E08 CERUM02 x20; E09 CERUM03 x20; E10 SK13 x30 plus SK23 x30; E11 SK33 x30 plus SK43 x30; E12 EM02 x2000; E13 LCOIN x20; E14 OV1 x30; E15 GC9 x1; E16 GC10 x1; E17 GC11 x1; E18 RP1 x100000.

These are exact original **reward.item[].ref_id/qty** declarations, not complete item references. In particular E02 records FMD1 as an item while its separate free_iap field is zero; do not silently rewrite this into an original currency receipt without tracing Episode ParseReward and the FMD1 consumer.

## Positive identity evidence

**GC2 is an owned Lottery coupon/reference.** Original `CSRSceneLottery::SetCurrency` Ge3e43c loads the exact GC2 literal via LDR Ge3e90c / ADD Ge3e90e, constructs a string Ge3e912, then calls **CSRInventory::GetInstItemCnt Gaeca80 at Ge3e91a**. Thus GC2 is actually looked up in inventory, not merely a display identifier. `OnClickRequestGachaByCoupon` Ge40020 also constructs GC2 at LDR Ge4013e / ADD Ge40140 / string assign Ge40146. Which coupon tier, use_type, effect and exact thumbnail mapping remain unknown. The latter routine's branch and request transitive semantics need full decompilation before activating redemption. GC3 and GC4 do not occur as standalone NUL-terminated original ELF strings in this bounded check; the general native item table may still handle them.

**FMD1 is a native free_iap display identity; RP1 is gold display identity.** Existing `ghidra-login-bonus-contract.txt` and `ghidra-login-bonus-keys.txt` prove ParseLoginBonusRef Gf4ae7c reads gold/free_iap separately, and synthesizes reward display refs RP1 (LDR Gf4b5dc / ADD Gf4b5de) and FMD1 (LDR Gf4b5ec / ADD Gf4b5ee). This is stronger than a naming guess, but does not supply original FMD1 item use_type/effect or prove that Episode's item form credits free Manda automatically. Original Episode popup also has a candidate FMD1 literal load at Gcfb1ba within `CSRPopupEpisodeReward::SetData`; that candidate was not independently followed to settlement and is not used as grant proof.

**AIRSHIP_TICKET** is the original Hunter Search capsule reference, proved by HunterSearch UpdateCurrency's direct inventory lookup in `search-capsule-content.md`. The current published reference use_type0/effect-empty remains an explicit local navigation fixture, not a recovered original item definition.

## Art inventory: available resources, unproved assignments

Original PAD `UI_ITEM.jet` traverses 391 headers to exactly 1655400 bytes; `UI_ITEM_CHA.jet` 133 headers to exactly 292960 bytes. Header uint64 names use the native base38 alphabet `0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ._`, as proved in starter-skill-resource-bindings.md. Later named animation records in UI_ITEM include:

- IT_2HQ, IT_3HQ, IT_4HQ, IT_3SE, IT_4SE and their _M/_S variants; IT_10FREE and variants.
- IT_FMD, IT_FMDXS, IT_FMD_M, IT_FMD_S; IT_MD and IT_MIXMD families.
- IT_TK_SE, IT_TK_SE_M, IT_TK_SE_S, IT_TK_SEXS; IT_TK_ST and IT_TK_BT families.
- IT_GCO, IT_RANBOX, IT_RBOX02/03, IT_OVL/OVI/OVF families; numerous UI_ITM_* and EV* records.

**Verified inventory only:** no recovered GetItem row binds GC2/GC3/GC4 to those HQ/SE resources. Do not assign a tier, rank or thumbnail from ordinal resemblance. Earlier unnamed/numeric header records are not treated as validated readable art names in this report. Named UI_ITEM_CHA animations include IT_CHA_001..065, with gaps/special901; those hunter-piece resources also do not identify these Episode coupon IDs.

## Missing original material table and safe next work

The preserved `analysis/recovered-data/leveldb-tables/all-tables.json` contains 13 exported tables (skills/tags/character text/dialog/localization/UI/admin/badword); none is ITEM_REF. A bounded exact-token GC2/GC3/GC4/FMD1 scan of every exported key/value returned zero matches. Current `server-ts/src/hunter-traces.ts` and shop-fuel references publish only documented local fixtures; they do not recover these Episode material semantics. This scoped result is not a claim that no other snapshot/file contains an original HTTP cache.

Native reference schema is already exact: **GetItem ret_data.item[]** rows require string `id,name,desc,thumbnail_id,effect` and numeric `rank,use_type,sell_price,collect_qty`; `ret_data.trace[]` and `global_item[]` are separate collections. CSRItemInfo.SetItem Gaefe10 parses them (shop-fuel-contract.md). An Episode reward ID/quantity alone cannot justify inventing the missing use_type/effect/collect_qty. Inert rows with use_type0 would be **new local fixtures**, not publishable original semantics, and would hide missing redemption behavior.

Narrow parent-only decomp targets if coupon support is selected: **CSRSceneLottery.OnClickRequestGachaByCoupon Ge40020** (exact GC2 branch/request), **CSRSceneLottery.SetCurrency Ge3e43c** (coupon balance consumers), and existing **CSRMEpisode.ParseReward Gb1ca7c** transitive item/currency receipt consumers. Keep Episode Reward explicit non-success until both matching material references and settlement are reconstructed. No original balances or grants were fabricated in this unit.
