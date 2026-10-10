# ShopFuel: item reference and BuyGlobalItem contract

2026-10-04. Read-only original Capstone, existing reference callback dump, and parent's fresh `ghidra-shop-fuel-contract.txt` / `ghidra-shop-fuel-strings.txt`. No source/adb/Ghidra/client changes. Addresses are Ghidra coordinates. `shop-economy.md` was not present; exact native evidence supersedes any inferred neighboring-route shape.

## Why header AP popup currently displays zero

Measured top vptr ELF0x2166678 is **CSRPopUpShopFuel**, independently attributed in `ap-popup-shopfuel-attribution.md`. Its Init0xd49b4c calls **CSRItemInfo.GetItemRefID(USETYPE1)**0xaf1374 at0xd49bfa, stores that reference string at actual+0x104, derives ticket_ref_id+0x110/requiredqty+0x120 from the global-item table, then loads its UI. GetItemRefID scans reference entries' use_type and returns the matching entry's reference ID; publishing Fuel activity data alone does not supply this table.

UpdateText0xd49f54 calls GetItemData(ref) at0xd4a06a. At0xd4a2b6..0xd4a2c6 it parses **item.effect as a numeric STRING with atoi** (short string+0x45 or heap pointer+0x4c). It then calls **GetGlobalItemProvideCnt**0xaf18a0 at0xd4a2d2 and multiplies the two to display provided AP. Missing use_type1 yields the EMPTY GetItemData warning and default/zero quantity; missing global prices yields cost0. These are a separate shop seam, not evidence of a free SupplyFuel eligibility/layout problem.

Verified local XML `KO/SR_COMMON/2_UI_CM_MD/5_UI_CM_M_ST` is9300 bytes and uses shipped icon names **IT_ST** and **IT_TK_ST**, among others. They can be candidate local thumbnail mappings with explicit fixture provenance; no original AP item ID or original thumbnail mapping was recovered here.

## GetItem reference schema

`CSRSyncRef::ReqItemCB`0xf83a14 passes the **full response envelope** into **CSRItemInfo::SetItem0xaefe10**. SetItem indexes envelope.ret_data at0xaefe36, then ret_data.item at0xaefe58. It clears the current item table and numerically iterates records; use an array, not an object keyed by item IDs.

Required base row fields recovered end-to-end:

- **Strings:** id, name, desc, thumbnail_id, effect. Their from_json<string_t> calls are strict. Effect is a string even when the contained value is numeric, e.g. **"10"**, not10 and not an effect-array/object.
- **Numeric fields:** rank, use_type, sell_price, collect_qty. Numeric conversions also tolerate numeric strings, but send ordinary nonnegative numbers.
- Base identity is **id**, not ref_id. **use_type1 is the actual AP-resource lookup used by ShopFuel**, directly from its Init call. The original ID/name/price/amount remain unknown.

Ret_data also contains arrays **trace** and **global_item**. Empty trace safely skips its item_id/order/type/source_id/thumb_id trace entries. A purchasable virtual resource needs a matching global_item record, indexed by its **item_id** string:

```json
{
  "result_code": 1,
  "ret_data": {
    "item": [{
      "id": "local_ap", "rank": 1, "use_type": 1,
      "sell_price": 0, "collect_qty": 0,
      "name": "Fuel", "desc": "Local revival AP refill",
      "thumbnail_id": "IT_ST", "effect": "10"
    }],
    "trace": [],
    "global_item": [{
      "item_id": "local_ap", "buy_limit": 3, "provide_qty": 1,
      "type": 0, "ticket_ref_id": "", "ticket_qty": 0,
      "price_list": [
        {"price_type": 1, "buy_cnt": 1, "price": 5},
        {"price_type": 1, "buy_cnt": 2, "price": 5},
        {"price_type": 1, "buy_cnt": 3, "price": 5}
      ]
    }]
  }
}
```

**This is a structural LOCAL FIXTURE candidate, not recovered original balance or a native-verified working reference.** ID, names, thumbnail assignment,10AP,5Manda,3limit and type0 are fixture choices. Global_item.type's semantic enum/reset behavior remains unpinned; type0 must not be described as original daily reset. Empty ticket_ref_id/no ticket grant deliberately means no reconstructed ticket path. Do not enable ticket purchase solely from ticket_qty0: server must refuse absent/unsupported ticket operations. Base table should not contain competing use_type1 rows without resolving native first-match ordering.

Exact global row keys: item_id0xaf07d6; buy_limit0xaf09a2; provide_qty slot0xaf0c94/addPC0xaf09f4; type slot0xaf0c98/add0xaf0a44; ticket_ref_id slot0xaf0c9c/add0xaf0a94 (strict string); ticket_qty0xaf0ad8; price_list0xaf0b2c/0xaf0b94. Each price_list entry reads price_type, buy_cnt and price. Before publishing tiers broadly, independently recover **GetGlobalItemPrice0xaf155c..0xaf18a0** to establish requested buy-count fallback and boundary behavior; don't assume a one-row vector caps to last like hunter enhancement prices. The example explicitly publishes its three advertised buy counts.

## Actual purchase request and payment meanings

**CSRSyncShop::RequestBuyGlobalItem0xf89ca8 posts /shop/BuyGlobalItem**, not a special fuel-only endpoint. Nine form fields: app_code,app_ver,market,pvid,otp, **target_ref_id**, **price_type**, **item_inst_id**, **qty**. Numeric values are emitted as decimal strings; target_ref_id is the AP reference discovered above. No recovered nonce or desired AP current value is sent.

ShopFuel native pathways establish:

- **price_type1 = Manda.** It reads existing buy count for type1, requests next-count price through GetGlobalItemPrice, and compares affordability against CPVDataMgr paid+free Manda **sum** (dump lines3568..3578). It opens normal purchase confirmation; its anonymous confirmation callback calls RequestBuyGlobalItem at0xd4c4b4 with price_type1, item_inst_id0 and qty1 (0xd4c4a2..0xd4c4ac). Original paid/free spend priority remains unknown, so any free-first policy is explicitly local.
- **price_type2 = gold.** Native direct RequestBuyGlobalItem path at0xd4b916 uses2, item_inst_id0 and qty1 (0xd4b902..0xd4b912); do not publish gold tiers unless server models that path coherently.
- **price_type4 = owned item ticket.** Direct call0xd4b20c passes4, actual ticket uint64 item_inst_id and qty1. Its reference ticket_ref_id/ticket_qty and owned item quantity must agree. A currency-only revival can safely refuse unsupported ticket path instead of fake spending.

Purchase quantity and count limit behavior are server policy plus native reference/UI constraints. Original daily reset/timezone and original prices were not recovered here; preserve receipts/counters across restart and label any reset schedule fixture.

## Success response: exact nesting and mutations

`ReqBuyGlobalItemCB0xf8b4a8` accepts full envelope and returns a GOODS_INFO result to ShopFuel's BuyGlobalItemCB0xd4a70c. Concrete currency purchase response excerpt (all numeric values/deadline are examples):

```json
{
  "result_code": 1,
  "ret_data": {
    "jackpot_level": 1, "jackpot_multiply": 1,
    "user": {
      "iap": {"iap_qty": 100, "free_iap_qty": 95},
      "ap": {"prev": 35, "cur": 45, "ap_charge_time": 0}
    },
    "target_inst": {
      "item_id": "local_ap", "price_type": 1,
      "buy_cnt": {"prev": 0, "cur": 1}
    },
    "consumed_inst_list": []
  }
}
```

**Deadline belongs INSIDE user.ap**, not beside it: callback retains user as r6 at0xf8b604, indexes user.ap at0xf8b830 then ap_charge_time at0xf8b838. It reads ap.cur and invokes **CSRPlayData.SyncAP** at0xf8b854. Use the already reconstructed resourceChargeTime/clock convention for real response values; zero in this example is not a recommended below-cap refill deadline policy.

User.iap **iap_qty/free_iap_qty are direct scalar current balances**, not prev/cur pairs. Optional user.gold reads gold.cur. The BP neighbor similarly has bp.cur/bp_charge_time but should be omitted on AP-only purchases. No new max_ap field is needed to grant a refill in this branch.

Target_inst is root ret_data.target_inst, not inside user/item. Strict item_id string at0xf8bd4a, numeric price_type, and **buy_cnt.cur** feed **Inventory.SetGlobalItem** and **SetItemBuyCnt** at0xf8be7e. Preserve the counter in persisted game state and publish the matching GetItemInven/global-item ownership representation once independently recovered; UI refresh alone is not reload persistence proof.

Optional target_item_inst contains **inst_id and scalar qty** and invokes SetItemQuantity for ticket balances. Optional item list contains ref_id/inst_id/qty/added and invokes AddItem, also building bonus-item result entries. Omit both for AP/Manda-only purchases unless real inventory mutation is modeled. **Consumed_inst_list[]** is a safe empty no-op; callback checks/iterates it before UseItem. Omit unknown achievement: any present nonnull value enters its parser; [] is not a proven safe schema.

Jackpot_level/multiply are parsed unconditionally. Use neutral1/1 for a no-jackpot local fixture: constructor's defaults are1 and float1.0, but missing jackpot_level parses to0. These fields propagate to the shop result popup; omission is not necessarily a neutral receipt.

On result_code!=1, ReqBuyGlobalItemCB skips success mutation parsing, and ShopFuel's callback skips its success result popup. No original business rejection code was recovered; use a documented local non1 failure rather than success with contradictory wallet/AP data.

## Minimal implementation acceptance controls and remaining risks

Before mutation require supported target_ref_id/price_type, unique correct qty bounds, affordable exact reference tier, matching owned ticket only if enabled, no active-state mismatch, and supported ordinary AP bounds. Debit total Manda once; don't debit paid and free by the same price. Increase AP and price-type buy counter atomically with any receipt and persist once. Overflow-above-max refill and daily-reset behavior are original-policy unknowns; choose/document a coherent fixture, don't silently assume normal regeneration rules settle purchased overflow.

Native checks: header AP popup has nonempty ref at+0x104, displays10AP and correct5Manda next tier; confirm one real purchase emits the recovered route/fields, wallet total decreases5, AP increases10 under fixture policy, response receipt displays neutral jackpot, next buy count/tier agrees, relaunch preserves wallets/AP/counter, and insufficient funds/unsupported tickets do not mutate anything. Duplicate network request receipt semantics need separate care: **no nonce is recovered**, so exact retry idempotency cannot be invented from a nonexistent field.

Remaining parent dump targets: GetGlobalItemPrice0xaf155c; Global_item.type meaning/reset consumer; global ownership/inventory parser (SetGlobalItem/GetGlobalItemBuyCnt and lobby inventory); ticket UseItem detailed contract if enabled; native Manda confirmation callback caller if full Request argument proof is needed. Core reference/full callback shapes are now recovered from the fresh dumps; no client patch or resource alias is needed to begin a bounded server-only fixture control.

Later follow-up resolves the first three targets in `shop-fuel-price-and-inventory.md`: price lookup requires an exact buy_cnt and returns0 on a missing tier; global_item.type has observed currency-specific1/shared2 indexing in card-extension UI but no proved reset semantics; GetItemInven is ret_data{item:[],global_item:[{item_id,price_type,buy_cnt}]} with scalar reboot counts. The structural type0 candidate above must remain explicitly local, and no original daily meaning should be assigned to it.
