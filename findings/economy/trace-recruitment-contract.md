# Earned hunter traces → native PieceExchange

2026-10-05. Read-only original ELF Thumb/literal/call-site inspection and existing hunter/item reports. No actions, grants, source/client/Ghidra/adb edits. G=ELF+0x10000.

## Exact route/request and UI caller

Native transport name is **CSRSyncShop::RequestShardExchange Gf8a894**, route **/shop/PieceExchange**. Original literal ADDGf8ab68 (slotGf8ac4c) yields exact route. Seven form keys recovered by matching each register's literal LDR/ADD:

```
app_code app_ver market pvid otp item_inst_id cnt
```

item_inst_id literal ADDGf8a9f0/slotGf8ac44; cnt ADDGf8aa18/slotGf8ac48. Requester signature uint64 item instance, uint32 count, callback(int,shared_ptr<const CSRCard>). The request targets an **owned trace item instance**, not hunter ref006 or reference itemID. No nonce, desired hunter instance or expected quantity field recovered.

Sole direct original BL caller is **ShardExchangeConfirm::OnButtonClick Gce230c**, callGce2462. It loads item instance low/high from popup+C8/Cc atGce243a, requested count from popup+D8 atGce2440 and passes count on stack. To preserve curated proof of count semantics and slider/confirm UI, parent dump InitGce0e90, OnButtonGce230c and UI result callbackGce2680. `ReqTakeCard` was not a retained native symbol in this pass; do not invent a similarly named route.

## Native success mutation parser

Callback **CSRSyncShop::ReqPieceExchangeCB Gf8af68** requires ordinary successful transport/result_code1. Exact ret_data ADDGf8b04e/slotGf8b2d4; optional achievement ADDGf8b066/slotGf8b2d8 is null guarded. It additionally **unconditionally calls CSRAchieve::ParseLobbyEnter(ret_data)** atGf8b05e, so transitive achievement contract should be checked when constructing a minimal success.

ret_data.card ADDGf8b080/slotGf8b2dc is numerically indexed. Each row is passed to ParseCardInst atGf8b104, then Inventory.AddCard atGf8b1a2. **Use an ARRAY of owned CSRCard rows even for a single awarded hunter**, not the GachaPremium single-object special shape. This loop has no equivalent gacha cnt-based singleton dispatch. Card rows need the already recovered owned-card parse fields (inst_id,ref_id,rank,rank_up_cnt,exp,lock,awake/overcome counters and five individual skill levels), with published matching reference/stat/art support. Last successfully parsed card shared_ptr is returned to the UI callback; multiple-card presentation/quantity semantics require its UI dump.

ret_data.consumed_inst_list ADDGf8b248/slotGf8b4a4 is passed **unconditionally** to Inventory.UseItem atGf8b254. UseItem Gaea5f8 reads **inst_id** (ADDGaea60c) and **qty** (ADDGaea6c0): consumption is a delta, not MultiSkillUp's absolute remain. Empty array is a proved no-op but **not an honest earned-trace exchange receipt** when traces actually paid. No direct gold/balance key read occurs in the inspected PieceExchange callback.

Illustrative direct fragment only (all IDs/counts are local examples):

```
ret_data.card = [ complete_new_owned_hunter_row ]
ret_data.consumed_inst_list = [{inst_id: actual_owned_trace_item_instance, qty: actual_consumed_trace_count}]
```

No original10-trace threshold asserted. Current UI0061/10 reflects current published collect_qty10 fixture; backend should consume that configured required count per requested exchange once slider/cnt semantics are proven, rather than asserting original game rates. ItemINFO use_type3/effect006 mapping is independently recovered in hunter-trace-item-binding.md.

## Atomicity, identity and remaining native proof

Validate the owned positive-quantity trace instance, corresponding reference use_type3/effect matching hunter reference, published collect_qty, requested count, sufficient quantity and valid hunter birthgrade/stat coverage **before** debit/grant. Allocate a fresh persistent hunter ID without modifying originals; persist trace decrement and new ownership together. Response quantities must describe actual debit; callback itself changes native inventory/ownership from those receipts. A lost-response retry cannot be distinguished from another intended exchange because no nonce/expected quantity is sent; reconcile persisted ownership before retry.

Parent smallest complete decomp set: RequestShardExchange Gf8a894, ReqPieceExchangeCB Gf8af68, confirmation InitGce0e90/OnButtonGce230c/resultGce2680. If transitive achievements need exact source, ParseLobbyEnter G844918. Consumption UseItem Gaea5f8 is independently decoded. Actual native Request button still requires earned traces to meet configured threshold; this report performs no Search, grants, exchange or tutorial clear.

## Confirmation count/debit and result path closed by fresh evidence

Source `ghidra-trace-exchange-contract.txt` and `ghidra-trace-exchange-keys.txt`; original Thumb confirms decompiler's obscured division ABI.

Init reads CardInfo+0x18 trace reference, Inventory.GetItemInst supplies actual source instance stored+C8/Cc, aggregate GetInstItemCnt supplies trace quantity+D4. CardInfo+0x4c supplies per-hunter required traces stored+E4. Exact original instructions **Gce1252 r1=CardInfo.collect_qty; Gce1256 r0=owned qty; Gce125c divide; Gce1262 store max exchange count+DC**. Thus max hunters=floor(qty/collect_qty) for positive valid inputs. Require positive collect_qty reference; do not rely on undefined zero-divisor behavior. Slider initializes1..max atGce1748..4c.

UpdateSlideBar Gce217c stores selected hunter count+D8 atGce21ae; Gce21b2 multiplies count by threshold+E4 and stores **trace debit+E0**. Request sends+D8 as cnt. **cnt means requested number of hunters, not traces spent.** For current fixture threshold10 and earnedqty10, cnt1 consumes10; qty20 would permitcnt2 consuming20. Original threshold/rate10 is not asserted.

OnButton verifies remaining card capacity+D0 >= selectedcount+D8 before request; server must independently validate capacity as well as trace quantity and reference validity. Multiple native trace instances with same ref require care: UI quantity is aggregate but request sends GetItemInst's selected instance ID; the current canonical inventory design should keep that identity/quantity coherent rather than silently consuming unrelated item IDs.

UI callback Gce2680 requires result_code1 and nonnull returned card: it dereferences last card rank+0x24 with no success-null fallback. Rank<3 selects **UI_SHOP_BAD**, rank>=3 **UI_SHOP_GOOD**, then plays LotteryVideo with mode0xB6. Video finish event registered atGce282e resolves vtableG2172310, invoke**Gce3248**. Read-only original calls show it constructs **GachaX10Result::RESULT(inst_id)** atGce3332, dumps it, sets local gacha-result marker atGce337a, pushes resultsceneGce339c. This synthetic result conversion is client-side; wire only needs truthful owned-card array/consumption, not guessed additional GachaPremium result fields.

Transport parses all returnedcard rows but UI receives the last ownedcard pointer. Singlecnt1 is fully bounded by this flow; multi-award inventory parses are proven, while full plural result presentation is not yet validated. Parent can decompile Gce3248 for concise result-marker/scene proof if needed.

Special UI refusal10027(0x272b) opens card-inventory extension;10033(0x2731) shows localized toast (exact business label not recovered here). Other non1 redirects to Village scene9 plus toast. A non1 response is supported and skips successful mutation; no fakeemptycard success should be used for insufficient earned traces. Live has only1trace and no exchange occurred, per parent update. This report closes structuralcount/debit/UI contract without granting traces or attempting exchange.
