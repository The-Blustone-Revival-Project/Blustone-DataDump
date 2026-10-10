# ShopFuel source audit before native promotion

2026-10-04. Read-only review of `server-ts/src/shop-fuel.ts`, `state.ts::buyFuel/itemInventory`, route dispatch, persisted state normalization, and `tests/shop-fuel.ts`; original native Capstone/dumps for comparison. No code/adb/Ghidra/client changes or tests executed by this agent. This snapshot had daily limit3 **per currency** in backend while publishing global buy_limit3.

## Blocking native/backend capacity mismatch

**Native ShopFuel treats buy_limit as shared across gold, Manda and tickets.** Current backend checks only the requested currency's count, so it authorizes up to6 purchases while native UI exhausts after any3. The current test explicitly buys three Manda refills then accepts a gold refill, encoding the mismatch rather than validating native behavior.

Exact native proof in `ShopFuel::UpdateText0xd49f54`:

```text
GetGlobalItemBuyLimit returns base limit ->sl at0xd4a07e
VIP UPGRADE_NUMBER_AP_CHARGE may add to limit at0xd4a0d8
goldCount   = GetGlobalItemBuyCnt(type2) at0xd4a102 ->stack+0x10
mandaCount  = GetGlobalItemBuyCnt(type1) at0xd4a15a ->r4
ticketCount = GetGlobalItemBuyCnt(type4) at0xd4a1b2 ->sb
0xd4a1fe /0xd4a202 /0xd4a208:
    remaining = limit - goldCount - mandaCount - ticketCount
0xd4a20c clamps negative remainder to0
0xd4a212 stores remaining at actual+0x11c
```

OnButtonClick requires positive actual+0x11c before normal purchase branches. **Global_item.type1 does not fix this**; ShopFuel does not query the limit-type getter. Type1 affects a different card-extension UI's price indexing. Current VIP fixture has no proved additional AP purchase bonus, so base advertised3 is the effective shared capacity for this control.

Recommended minimum: keep native reference buy_limit3 and enforce **manda+gold<3** in backend, preserving separate currency counters for next-price tiers. Rename fixture documentation/test claims to three total daily purchases. Verify mixed sequence Manda→gold→Manda succeeds and both payment methods refuse a fourth request without debit. Publishing buy_limit6 while enforcing3 each would still let native attempt a fourth purchase in one currency, whose missing tier returns0; it is not an equivalent fix.

## Recovered parser shapes currently match

Reference base has all recovered mandatory fields: id/name/desc/thumbnail_id/effect strings; rank/use_type/sell_price/collect_qty numeric. use_type1 selects AP; effectString10 matches native atoi. Global row has item_id, buy_limit, provide_qty, type, ticket_ref_id, ticket_qty and price_list; flat arrays include exact buy_cnt1/2/3 for both currencies. There are no duplicate tier counts or guessed cap-to-last semantics. At current constant prices, server debit matches each published supported tier.

GetItemInven correctly returns **ret_data{item:game.items,global_item:[...] }**, with scalar buy_cnt rows, rather than old bare-array shape. Current buyFuel receipt has neutral jackpot1/1, correct user.ap.cur plus **nested ap_charge_time**, scalar user.iap balances for Manda or gold prev/cur for gold, and root target_inst item_id/price_type/buy_cnt previous/current pair. consumed_inst_list[] is safe; unknown achievement, bonus item and ticket mutation fields are omitted. No new parser-shape crash identified in this currency receipt.

Identity/name/IT_ST thumbnail mapping, AP10/Manda5/gold100/dailyUTC cap and free-first wallet priority remain explicit fixtures. Native real item ID/original balances and original reset schedule remain unknown.

## Unsupported ticket0 behavior

Current reference has ticket_ref_id empty/ticket_qty0, and server refuses price_type4. This protects economy but does **not** hide/disable the native ticket option automatically. Native checks `ownedTicketCount < ticket_qty`;0<0 is false, so it can pass affordability and try a ticket purchase while remaining capacity>0.

The native missing-string **GetItemInst0xaec894** fallback returns **inventory+8** at0xaec930, rather than null. OnButtonClick copies that default ITEM_INFO, obtains its serial, and can issue type4 with dummy0. Server rejects it before debit/AP/count mutations. This path is not a proved null-pointer crash, but an unsupported visible ticket action can still produce a non-success toast; do not call it implemented or advertise free-ticket cost0 as functional.

Publish a valid ticket reference/positive required quantity only after modeling its actual ownership/consumption; no dummy ticket grant is warranted here. If native control shows misleading ticket affordance, document it as an unsupported UI branch rather than patch/force the client. An explicit global_item price_type4 buy_cnt0 in inventory is a useful reset guard if old native ticket counters could exist: omitted rows don't prove a retained in-memory key cleared, and native shared capacity includes tickets. No such old positive counter was measured in this audit.

## Transaction review and bounded limits

Request validation correctly refuses unknown target/payment, qty!=1, nonzero item_inst_id, malformed/bool values, limit exhaustion and insufficient currency. Manda debit reduces free first then paid by only the remainder, so total decreases5 once. Gold debit100, AP increase10, selected counter increment and one persistence operation form the paid mutation. Lazy AP regeneration and UTC-cycle settlement precede it; their persistence is normal clock settlement rather than a second paid purchase. A refusal may legitimately settle a new day or elapsed AP before the purchase-specific validation finishes.

Restart counters are modeled and restored by the correct native inventory shape. Clock rollback does not reopen a paid cycle. The supplied test covers wallet crossover, receipt nesting, restart, account isolation and refusals, but its per-currency fourth-purchase assertion needs the capacity correction above.

Native request has no recovered nonce. Repeating a valid request before capacity exhaustion spends again; this is an acknowledged transport-retry/idempotency gap, not proof that identical intentional purchases should be deduplicated by body alone. Do not claim replay-safe exactly-once purchases without a justified receipt key.

After UTC midnight, backend resets on account inventory/purchase access, but a still-open native popup can retain exhausted global counters until it receives a new inventory/counter sync. This audit did not recover an automatic midnight resync route. Preserved restart/new GetItemInven is a proved refresh control; uninterrupted midnight UI continuity remains a limitation to test, not original daily behavior.

AP overflow is preserved by existing reward policy. Native under-cap purchase and native above-cap display need separate controls; server test50→60 is not native UI proof. Numeric safe-integer guards do not establish native uint32 overflow compatibility, though bounded3*10 AP in the normal fixture is far below that boundary.

## Promotion acceptance controls

Before announcing native ShopFuel working: repair shared capacity, run mixed-payment persistence/limit checks, then tester verifies under-cap real purchase renders10AP and exact wallet price, successful response updates both shop result and header, next native tier/counter survives relaunch, and a fourth mixed purchase cannot be made. Also test insufficient funds and unsupported ticket option without any AP/currency mutation. Retain fixture labels and no original-economy claim.

No additional server parser edit is demanded by the recovered base/receipt fields. The shared capacity mismatch is the concrete blocker identified in this review; native resources, ticket affordance, midnight refresh and retry semantics remain separately bounded risks.
