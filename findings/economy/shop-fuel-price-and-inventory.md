# ShopFuel exact tiers, limit-type consumer, and reboot buy counters

2026-10-04. Read-only original Capstone/literals, parent dumps `ghidra-shop-fuel-price.txt`, `ghidra-shop-fuel-inventory.txt` and accompanying strings. No source/adb/Ghidra/runtime changes. Ghidra code addresses.

## Price lookup has exact-count matching and zero fallback

**GetGlobalItemPrice0xaf155c** first finds the global item by reference ID. Missing global item returns0 at0xaf16c6. Price_type1 selects the Manda pair vector;2 selects gold. Other types do not use either ordinary currency vector.

Each pair is `(buy_cnt,price)`. It filters by **requestedCount==pair.buy_cnt**, except requestedCount0 takes every pair. It then returns the first selected pair's price at0xaf17dc. If selection empty, return0 at0xaf17f0/0xaf17f4. There is **no closest-lower tier, cap-to-last, or automatic row0 wildcard fallback**.

Exact assembly: query count retained in r8 at0xaf156a; selected-vector filter query0 bypasses the equality test, otherwise pair count read at0xaf1768 and compared0xaf176a (Manda), equivalent gold0xaf1670..76. Final selected-vector begin/end comparison0xaf17d4..da; price load begin+4 at0xaf17dc; missing-selection0xaf17f0/+17f4; finalreturnr4 at0xaf1826. Fresh decompile confirms both branch filters.

For a three-purchase local Manda fixture, publish buy_cnt1/2/3 explicitly. Query4 returns0, so backend must refuse at its advertised limit and UI should prevent that branch; do not accidentally treat its zero price as a free fourth purchase. Query0 is an all-rows request, not how ordinary ShopFuel computes the next tier (it asks current currency count+1). Duplicate count rows enter first-selected-row behavior with an internal ordering helper; avoid duplicates rather than choose an unproved tie rule.

## Global_item.type is a buy-limit mode, not proved daily/lifetime enum

The field is recovered by **GetGlobalItemBuyLimitType0xaf14fe**, which looks up the global item and returns its stored type (mapnode+0x1c); missing row returns0. An offline direct-BL scan found one consumer: **CSRPopUpBasic::SetCardInvenExtend0xb8de54**, call0xb8e00a. This is card-capacity shop UI, not ShopFuel.

That consumer snapshots gold(type2), Manda(type1), and ticket(type4) buy counters, sums all three for its total limit. It then dispatches:

- **type1**: gold next price uses goldCount+1 at0xb8e01e..26; Manda price uses MandaCount+1 at0xb8e032..3a. Currency-specific price indexing.
- **type2**: both gold/Manda next prices use combinedTotal+1 at0xb8e200..21c. Shared price indexing across payment methods.
- **other values, including0**: skips these recovered price-recalculation branches to0xb8e224. This does not prove a named0 limit mode, unlimited purchase, or lifetime reset schedule.

ShopFuel itself calls GetGlobalItemBuyLimit but **does not call GetGlobalItemBuyLimitType** on the recovered code paths. It computes next price from that currency's own buy count. Therefore type0 does not itself change native AP price indexing here, but choosing it must remain a structural local fixture, not an original semantic claim. Type1 is a more explicitly interpretable local candidate if the replica intentionally uses currency-specific counts; it is still **not recovered original AP type**. No daily/lifetime enum name or automatic reset was established. Keep a persisted no-reset/limited schedule only as documented revival policy and don't reuse a type0 AP fixture as a supposedly faithful card-extension reference.

## GetItemInven full shape, including global counters

**CSRInstanceSync::ReqItemCB0xae6080** accepts a successful full envelope and tail-calls **CSRPlayData::ParseUserItemInven0xb6962c** at0xae60a0. This parser explicitly indexes envelope.ret_data0xb6964a, retains that parent, and reads:

```json
{
  "result_code": 1,
  "ret_data": {
    "item": [],
    "global_item": [
      {"item_id": "local_ap", "price_type": 1, "buy_cnt": 2},
      {"item_id": "local_ap", "price_type": 2, "buy_cnt": 0},
      {"item_id": "local_ap", "price_type": 4, "buy_cnt": 0}
    ]
  }
}
```

The example values are local fixture state. **Global row buy_cnt is a direct scalar**, not `{prev,cur}`; the paired shape belongs to the purchase response only. item_id is a strict string, price_type and buy_cnt are numeric scalars.

Exact parent/key/mutation evidence: initial ret_data LDR0xb69642/slot0xb6994c/addPC0xb69648; item0xb6964e/add0xb69652; global_item LDR0xb69914/slot0xb69bb4/add0xb69918, indexed from retained ret_data at0xb69916..1a. Global row keys use slot0xb69bb8/add0xb699be **item_id**, slot0xb69bbc/add0xb699c4 **price_type**, slot0xb69bc0/add0xb699ca **buy_cnt**. Each parsed entry calls **Inventory.SetGlobalItem0xaea864** at0xb69abc.

Ordinary item entries, if needed later, use **inst_id,ref_id,qty,buy_cnt_gold,buy_cnt_manda** and call Inventory.SetItem0xaec33c at0xb69874. Beware the string resolver's apparent "d"/"tem" near0xb696e2/e4: correct matched ADDPCs0xb696e8/ea yield **qty** and **buy_cnt_gold**. Empty ordinary item array is enough for a currency-only AP purchase fixture; no fake AP owned item should be granted solely to preserve global buy counters.

This **corrects the existing bare-array GetItemInven assumption**: callback expects ret_data as an object with item/global_item arrays. The currently empty bare array may avoid useful mutation, but cannot restore a nonzero virtual purchase counter. Publish the exact object before claiming reboot persistence. Initial lobby Enter does not replace this separate callback's parser simply by adding an inferred global field to user.

## Implementation acceptance controls

Persist per-account targetref/payment-type counts. Fresh GetItemInven must publish those counts; include explicit zero rows for supported payment types when resetting a fixture schedule, rather than assuming omitted keys clear retained client counts. Counter reset timing is server policy until original reset evidence exists.

Complete a Manda purchase, verify `target_inst.buy_cnt.cur` updates the client immediately, then a preserved restart reconstructs the same counter through global_item scalar rows. Reopen AP shop: count2 queries tier3 and shows its configured price; count3 is exhausted/refused, not free tier4. Gold/ticket counters are independent unless the fixture explicitly chooses a coherent combined policy. Wrong/unsupported payment, insufficient funds or duplicate receipt must not spend or advance counts.

Native type1/2 behavior above is proved only for card-extension UI; original AP global type and daily reset rules remain unresolved. Exact price matching and GetItemInven reboot shape are recovered and ready for the parent server implementation.
