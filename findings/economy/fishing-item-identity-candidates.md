# Fishing item identity candidates: corroboration limits

2026-10-07. Bounded read-only existing final public FISH_LIST/UI_ITEM/DIAL-EN/settings,13-table localization/reference export, original string index and current fishing parser reports. No visual-stat search, web hunt, Ghidra/adb/server/state/source mutation or catch grant.

## Result

**No original fish item ref_id is corroborated in the inspected evidence.** The native tutorial reached100% and requested EndWithSell(log_id-1); that is an earned interaction/request, not evidence of a returned fish identity. Do not substitute FS001, FISH_01, RP1 or a guessed FI001 as its item identity.

Positive original **name candidate**: DIAL-EN **NPC0004**, header2987855, node2 says **Hello, %user_name%! Do you like Calcium Smelt?** Its UserScript is empty. This proves an original named fish/species in fishing onboarding; it does **not** bind Calcium Smelt to a particular item ID, art ordinal or guaranteed tutorial reward.

A targeted exact-token scan of all13 exported tables (`analysis/recovered-data/leveldb-tables/all-tables.json`) for FS001..011/FISH01..09/FISH_01..09 and Calcium Smelt/Korean equivalent found zero matches. There is no full ITEM_REF export in the current recovered-reference directory. The original native string index also supplied no standalone canonical fish ID for these candidates. This scoped negative does not prove all private caches/other historical sources lack records.

## Exact art candidates, not ref_id aliases

Original **FISH_LIST.jet** complete **90-record** EOF walk provides these named sprite descriptors (header offset/packed bytes):

```text
FS001 560357/34   FS002 560589/34   FS003 560705/34
FS004 560937/34   FS005 561169/33   FS006 561400/34
FS007 561632/35   FS008 561865/35   FS009 562099/34
FS010 562332/34   FS011 562912/36
```

Original **UI_ITEM.jet** has named sprite descriptors **FISH_01..FISH_09**, respectively headers1645696,1645754,1645812,1645870,1645928,1645986,1646044,1646102,1646161; packed34bytes for01..07/09,35bytes for08. Both groups are actual encoded original resource names; their numbering is **not an item-table relation or Calcium Smelt mapping**. No media interpretation/visual-stat extraction occurred.

Original **FISHING_SETTINGS.json** comes from LEVELING namedFISHING and has common1/PLC001/TUTO. It contains timing/NPC configuration, **no fish catalog, ID→name/icon table or tutorial catch declaration**. Existing FISHING/MGM_FISH resource inventories likewise identify presentation assets without API identities.

## Native dependency chain is exact

`fishing-entry-contract.md` proves the successful GetFishingPool callback **Gb324c8** iterates ret_data directly, strict **lure_id** atGb32596/from_jsonGb325d6 and strict **fish_id** atGb325a4/from_jsonGb325ec, storing lure→vector<fishID> membership. The pool does not itself define item names/art.

`fishing-tutorial-settlement-contract.md` proves ParseEnd **Gb2a560** requires ret_data.fish_id STRING (ADDb2acd2/from_jsonGb2ace4) and writes **Fishing+68**. Nonempty identity feeds AddInven/UpdateRecord; it cannot be supplied as a cosmetic placeholder without native mutation semantics.

`fishing-tutorial-demo-identity.md` positively traces ordinary **Success.SetItemInfo Gd07620**: GetInfoGb2eff0 atGd07640 returns Fishing+50; **INFO+18 atGd0764a** is therefore that exact fish_id string; **ItemInfo.GetItemData Gaf109c atGd0764e** looks it up directly. No ordinal-to-FS-name conversion is proved at this dependency. The successful popup needs an actual matching item reference, not only a texture namedFS001.

The generic original GetItem row requires strict id/name/desc/thumbnail_id/effect strings plus numeric rank/use_type/sell_price/collect_qty (SetItem Gaefe10; shop-fuel-contract.md). The exact original fish values and thumbnail binding remain missing. Grade/length/price, additive receipt replay and tutorial completion are separate unresolved settlement policies; reaching the hook's100% does not recover them.

## Precise remaining source need

Recover an original **GetItem row whose id matches a fish_id returned by GetFishingPool/EndWithSell**. Then preserve its original name/thumbnail/effect/use_type rather than choosing an icon ordinal. An original authorized cached response or developer-provided table would be primary; `native-reference-cache-candidates.md` identifies bounded keys-only cache candidates, not an existing fish row. Parent's planned web research may corroborate species/display names, but those alone cannot establish internal IDs or a guaranteed demo catch. This report supplies exact candidate names/art/dependencies without inventing an item or reward.
