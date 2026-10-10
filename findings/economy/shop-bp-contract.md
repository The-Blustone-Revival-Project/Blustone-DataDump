# BP / letter shop: independently recovered neighbor contract

2026-10-04. Read-only original ELF/RTTI/Capstone, existing shared-shop callback dump, and disposable selected UI LevelDB copy. No source/adb/Ghidra/client changes, implementation, purchase or push. Balance examples are local candidates, not recovered original prices/quantities.

## Actual entry and class

Village's letter/BP currency button is **BT_MY_LT**. In CSRPopUpVillage::OnButtonClick0xdac918, clicked CMHashID compares low32 **0x65944dc6**, high32zero at0xdad1b8..0xdad1c4. This equals standard CRC32 of the shipped BT_MY_LT literal.0xdad1ca calls **shared_ptr<CSRPopUpShopFCTicket>::make_shared0xc0d6b0**, then virtual Init0xdad1d6 and modal push. Separate fight-club screens also call the factory, including CSRPopUpFC0xc0c924 and CSRTableFC0xff4052.

Exact primary popup vptr is **B+ELF0x2166470**, `_ZTV20CSRPopUpShopFCTicket` ELF0x2166468+8. This is neither ShopFuel nor free SupplyFuel. Class names alone were not the attribution: the caller/factory plus actual vtable symbol identify it.

**FCTicket.Init0xd46cf8** loads its distinct resource **SR_COMMON/2_UI_CM_MD/6_UI_CM_M_LT**, exact LDR0xd46d14/slot0xd46e58/addPC0xd46d1a. It calls LoadView0xd46d1c and stores **view+0x94**, control+0x98 at0xd46d3e/0xd46d46. Use actual view/root guards if inspecting it later; no runtime popup was observed here.

Selected KO resource exists (8478 bytes), EN record absent. Existing loader KO fallback applies, so absence is not a proposed alias defect. XML directly uses **IT_LT** and **IT_TK_LT** for letter/resource/ticket art, alongside gold/Manda icons. These are genuine shipped sprite names, **not recovered original server item thumbnail mappings or IDs**. BT_MY_LT's actual on-screen hit coordinates and native scene availability remain tester observations to obtain.

## Independently proved item use type and quantity semantics

Init calls ItemInfo.get at0xd46da0; **r1=2**0xd46da4; **GetItemRefID(USETYPE2)**0xaf1374 at0xd46da6. That reference is stored in actual **+0xe8**. It gets matching global ticket reference with GetGlobalItemTicketRefID0xaf1518 at0xd46dce into **+0xf4**, then required ticket quantity GetGlobalItemTicketNeedQuantity0xaf1540 into **+0x104** at0xd46dfa.

Thus the virtual BP reference must be a **use_type2** item record. AP use_type1 does not satisfy this lookup. Extend the complete GetItem reference with both records; SetItem clears/rebuilds the whole table, so publishing BP-only rows would regress the now reconstructed AP lookup.

The established SetItem schema is shared because both popups call that same ItemInfo getter: envelope.ret_data.item array with strict id/name/desc/thumbnail_id/effect strings, numeric rank/use_type/sell_price/collect_qty; trace[], and global_item array keyed by matching item_id with buy_limit/provide_qty/type/ticket_ref_id/ticket_qty/price_list. See `shop-fuel-contract.md` for full parser evidence. A candidate **local_bp** identity, thumbnailIT_LT and effect"5" would be explicit local fixtures, not original catalog reconstruction.

Quantity is independently checked in this neighbor: UpdateText0xd47150 reads item.effect+0x44 and calls **atoi**0xd474b4, calls **GetGlobalItemProvideCnt0xaf18a0**0xd474c0, multiplies at0xd474c4. Success popup callback0xd47b70 repeats effect parse at0xd47bc0 and provide-count getter0xd47bcc. It sets receipt result kind3 at0xd47bea, distinct from AP receipt kind2. Use a numeric effect **string**, not a JSON effect object/array or numeric field.

## Actual request routes and payment arguments

This neighbor actually calls **RequestBuyGlobalItem0xf89ca8**, whose recovered route is **/shop/BuyGlobalItem**. Same nine form fields: app_code/app_ver/market/pvid/otp, target_ref_id,price_type,item_inst_id,qty. Target is this popup's reference+0xe8. Independent calls prove:

- **ticket price_type4** at0xd48572; reference argument+0xe8, actual ticket serial passed, qty1 at0xd48566/0xd48568.
- **gold price_type2** at0xd48a56; item_inst_id0, qty1, target+0xe8 at0xd48a44..0xd48a52.
- **Manda price_type1** in confirmation callback0xd49588; item_inst_id0,qty1 at0xd49576..0xd49584.

These are actual neighbor calls, not extrapolation from AP route names. GetGlobalItemPrice remains the same exact-count matcher: publish each supported `(price_type,buy_cnt)` tier; missing tier returns0, not last price. Original letter price/qty/ticket reference and reset schedule were not recovered.

## Shared capacity independently verified

FCTicket.UpdateText obtains gold count(type2) at0xd47294→stack+0x14, Manda count(type1)0xd472ec→stack+0x10, ticket count(type4)0xd47344→stack+0. VIP upgrade **UPGRADE_NUMBER_BP_CHARGE** literal appears at0xd4738e and adds to the effective limit before remaining calculation.

At0xd473ea..0xd473f8 it sums all three counters;0xd473fa subtracts the sum from effective limit;0xd473fe clamps negative remainder;0xd47404 stores **actual+0x100**. Therefore BP's advertised buy_limit is shared across payment types, independently of AP's already corrected capacity. Counter identity is the BP targetref, so don't share the AP ledger merely because wallets and parser are common. Original limit and VIP bonus magnitudes remain unknown. Do not publish "3 each" under a shared buy_limit3.

## Exact BP success response and native mutation

Shared **ReqBuyGlobalItemCB0xf8b4a8** parses the independently inspected BP branch. It retains ret_data.user in r6 (0xf8b604), detects user.bp at0xf8b870, indexes **user.bp**0xf8b882 and **cur**0xf8b88a. It then indexes **user.bp**0xf8b8d8 and **bp_charge_time**0xf8b8e2. It calls **PlayData.SyncBP0xb6c966** at0xf8b934 using currentBP and deadline (not an AP sync or top-level charge-time field).

Local example success excerpt for a5BP/5Manda fixture:

```json
{
  "result_code": 1,
  "ret_data": {
    "jackpot_level": 1, "jackpot_multiply": 1,
    "user": {
      "iap": {"iap_qty":100,"free_iap_qty":95},
      "bp": {"prev":3,"cur":8,"bp_charge_time":0}
    },
    "target_inst": {
      "item_id":"local_bp","price_type":1,
      "buy_cnt":{"prev":0,"cur":1}
    },
    "consumed_inst_list":[]
  }
}
```

Other values/deadline0 are illustrations only; actual reconstructed deadline must use existing server-clock/BP recharge convention. Nested **user.bp.bp_charge_time** is required for meaningful sync. Wallet iap_qty/free_iap_qty are direct current scalars; gold path uses user.gold.cur. Omit AP update for BP-only purchase. Target_inst buy count pair feeds SetGlobalItem/SetItemBuyCnt via the common callback. Reboot GetItemInven must expose **ret_data.global_item[{item_id,price_type,buy_cnt scalar}]**, independently keyed by local_bp; receipt-only counter update is insufficient.

FCTicket BuyGlobalItemCB0xd47b70 checks response result1 at0xd47b8e..0xd47b94, reloads UI controls/text, constructs shop result, and uses its own reference/effect/provide quantity as above. Non1 response skips success. Unsupported tickets should retain refusal; qty0/empty ref doesn't prove native ticket option disabled. Optional achievement/bonus items/target ticket quantities should be omitted until their actual mutation is modeled. Neutral jackpot1/1 preserves the established no-jackpot result semantics.

## Remaining exact parent dumps / native controls

For a future BP implementation, request these decomp targets if fuller control details are needed: **FCTicket.Init0xd46cf8..0xd46e5c**, LoadComponent0xd46e5c..0xd47150, **UpdateText0xd47150..0xd476ec**, **OnButtonClick0xd47e30..0xd48e0c**, **BuyGlobalItemCB0xd47b70..0xd47e30**, and confirmation callback containing **0xd49588**. Shared RequestBuyGlobalItem/ReqBuyGlobalItemCB, SetItem, price lookup and GetItemInven are already recovered in the AP reports; do not rederive their shape from route similarity alone.

Still unknown: original BP item identity/thumb mapping, balances, buy tiers/caps/reset, VIP BP bonus, native purchased overflow display, and expected BP spending in fight-club gameplay. Native control must verify correct FCTicket vptr/button, real purchase request, paid/free wallet total debit once, BP change/deadline, receipt kind, shared mixed-payment cap and reboot counters, while AP remains unchanged. This task identifies the seam; it does not implement or validate BP purchases.
