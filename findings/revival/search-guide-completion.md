# Search tutorial37/1 completes at guided recruitment

2026-10-05. Read-only original Thumb/RTTI and tutorial-clear-contract.md. No Ghidra/device/source/live state changes. Parent reports two real Search victories while server tutorial37/1 remains pending.

## ACK is not a battle-End event

**CSRPopUpFindShardConfirm::SetTutorialGacha Gbe7ba8** explicitly calls **RequestClear(type37,step1)**: MOVr1,#25hex atbe7dbe, MOVr2,#1 atbe7dc0, call**f9a0c4 atbe7dc4**. Neither ordinary Search victory nor End's trace award alone reaches this completion call.

Its entry comes from the **SetTutorialShard** guide sequence. Original callback **Gbeb68a** loads its captured popup and tail-calls SetTutorialGacha at**beb68c**. Callback vtableELF21591c0's actual RTTI names the nested CSRPopUpFindShardConfirm::SetTutorialShard lambda. This is positive guide attribution, not nearest-symbol naming.

## Recruit button is the real gate

**SetTutorialShard Gbe7830** looks up **BT_RECRUIT** (LDRbe784a/slotbe7b14/ADDbe7850), calls IsEnabled atbe7870, and **returns when false atbe7876** before installing the recruitment focus sequence. A disabled Recruit button therefore leaves37/1 pending legitimately.

The enable writer is **FindShardConfirm::SetHunter Gbe3c64**. It gets the selected hunter's CardInfo atbe3ca0, obtains that card's trace item ID from **CardInfo+18**, counts owned traces through **GetInstItemCnt atbe3cd0**, and saves the quantity atbe3cd4. The later **BT_RECRUIT** lookup (LDRbe42be/slotbe4308/ADDbe42c0) compares that quantity against **CardInfo+4c** atbe42e4..be42ea. Insufficient quantity calls SetEnablefalse atbe42f0; sufficient calls SetEnabletrue atbe430e. This proves the quantity/required-count gate directly. The exact upstream CardInfo+4c binding writer was not re-derived in this task.

Current item reference declares local_sylvester_trace collect_qty10 and one trace per Search win. Two actual trace1 victories are therefore consistent with the button staying disabled and37/1 pending. This numerical fixture relation must be checked against actual displayed/inventory counts; no original tutorial reward quantity or special initial payout is recovered here.

## Local guide marker progression

The native guide also uses a local **tuto_explore** marker. A guide-specific ProcessResult branch requires current marker9 (CMP90831c), then sets marker10 at90833c/908350. The FindShardConfirm guide dispatcher reads tuto_explore (LDRbe85b8/slotbe8664/ADDbe85c0): marker6 calls SetTutorialFind atbe8628; marker10 calls SetTutorialShard atbe8630. Ordinary later victories need not repeat that guide transition.

This is local native guide flow, separate from server tutorial state. It must not be manufactured or removed by the replica to force an ACK. The actual local marker at the parent's current UI is unobserved by this lane.

## Search identity017 is not a hunter-ID requirement

SetTutorialGacha copies **Target.INFO.target_card_id+14** atbe7bcc/be7bce into its context. It does not require a hunter reference named017. Search guide017 is the earlier proved **INFO.id/UI node name**. With a local target_card_id006, this handoff follows006; it does not recover original Lapis's card ID. English dialogue alone cannot justify publishing or granting card017.

## Reward-bearing tutorial-clear handoff

The actual Clear callback is **Gbeb7ec**, selected through original function vtable**ELF2159218**, invoke→ELFbdb7ed/Gbeb7ed; RTTI explicitly names SetTutorialGacha $_10 function<void(int)>.

It removes local tuto_explore, reads **tuto_explore_exchange_result** (LDRbeb858/slotbeba40/ADDbeb85c), and **checks that marker is nonnull atbeb87c..beb880**. When present it parses the stored card JSON through PlayData.ParseCardInst atbeb890, then invokes **ReqShardExchangeCB(1,card) atbeb8dc**, the recruitment/result display handoff. A missing marker skips that display path. This is not proof an ordinary /shop/PieceExchange must already have happened: the existing **CSRSyncTutorial::ReqClearCB Gf9ac40** has an optional card reward branch that feeds inventory and tutorial-explore markers, as recorded in tutorial-clear-contract.md.

Consequently a pair-only37/1 ACK can clear tutorial state yet skip the original reward/card display when the expected marker is absent. Do not auto-clear37/1 after battle wins or silently grant a hunter merely to satisfy this animation. If the guided Recruit action actually emits Clear37/1, recover its exact card/consume_result response and reward eligibility before claiming the complete handoff. Those reward economics remain unknown, even though the original callback supports them.

## Next legitimate acceptance

Continue only through actual earned traces and normal UI. Confirm trace count reaches the published required count, BT_RECRUIT enables, marker10's guide focuses it, and the guided touch naturally emits Clear37/1. Then distinguish a reward-bearing tutorial-clear path from the ordinary piece-exchange route and verify the card/result/consumption once. No manual tutorial clear, extra trace grant, missing-card alias or direct scene jump is justified.

Narrow parent targets if needed: **SetTutorialShard be7830**, **SetTutorialGacha be7ba8**, **Clear handoff beb7ec**, **ReqClearCB f9ac40** card/marker branch, **SetHunter be3c64**, and **ProcessResult9081f4**. Server37/1 remaining pending after two victories is not by itself a regression.

## Exact Clear reward and consumption contract

Additional original-ELF inspection closes the reward container gap. All addresses below are Ghidra coordinates (original ELF VA plus10000hex). Literal attribution matches each LDR destination to its own ADD-PC instruction; adjacent literal slots were not treated as field names.

**ret_data.card is a collection of full card-instance rows**, not a single bare card object. The field pair is LDRf9ad90 / slotf9af8c / ADDf9ad92, resolving `card`. Null skips the branch atf9ad9e. The callback constructs begin/end iterators, dereferences each element atf9ae2a, passes that same element to **PlayData.ParseCardInst atf9ae3e**, and adds the parsed card to **Inventory.AddCard(card,1) atf9ae8a**. An array containing one existing full cardInstance schema is the narrow safe representation. Object collection iteration exists too, but a bare instance object would incorrectly iterate its scalar field values. Reference and instance identity must remain valid; the ordinary card-instance schema, published reference and unique owned serial remain prerequisites.

After adding each card, the callback reads `tuto_explore` (LDRf9ae04 / slotf9af90 / ADDf9ae08). It constructs signed integer JSON0 atf9af16..f9af1e and evaluates **0 < marker** through nlohmann operator< atf9af24. A false comparison skips marker storage atf9af42. A true comparison calls **SetMarker atf9af5e**, using `tuto_explore_exchange_result` (LDRf9ae0c / slotf9af94 / ADDf9ae0e) and the **original element JSON**, still held inSL fromf9ae2e. There is no additional type37/step1 comparison in this card/marker branch. Multiple reward rows overwrite this one display marker, leaving the final row; one guided recruitment row avoids ambiguity. For the known numeric guide marker10 the comparison is true. Cross-type JSON ordering must not be mistaken for a general positive-number validator.

**ret_data.item[]** is separately optional (LDRf9b000 / slotf9b31c / ADDf9b002, null guardf9b00e). Each row indexes:

```text
inst_id  LDRf9b06a / slotf9b320 / ADDf9b072
ref_id   LDRf9b076 / slotf9b324 / ADDf9b078
added    LDRf9b07c / slotf9b328 / ADDf9b07e
```

`ref_id` is read as a string; `inst_id` and `added` use unsigned32 scalar conversion/default0. AddItem atf9b17a receives the resulting serial, reference and added quantity. This callback therefore supplies a narrower instance-ID conversion than some other inventory routes. Keep local item serials inside uint32. `added` is an addition, not a final inventory balance.

**ret_data.consume_result.item[]** is the consumption parent. The exact pairs are consume_result LDRf9b20c / slotf9b32c / ADDf9b20e and item LDRf9b216 / slotf9b330 / ADDf9b218. The extracted collection is passed to **Inventory.UseItem(JSON) atf9b222**. That helper's already recovered rows are `{inst_id,qty}`; `qty` is the quantity **to subtract**, not the post-consumption balance. The numeric overload subtracts its low-word quantity from current quantity ataea7fc and stores ataea800 without validating an adequate balance. The server must validate earned quantity before responding and avoid repeated additive receipts being applied twice.

The resulting proven structural template is:

```text
ret_data: {
  type:37, step:1,
  card:[FULL_CARD_INSTANCE],
  item:[],
  consume_result:{item:[{inst_id:TRACE_INSTANCE,qty:CONSUMED_COUNT}]}
}
```

This is a parser template, not a recovered reward amount or authorization to grant a card. Empty item/consumption lists and omitted optional rewards are safe for a pure ACK. Any reward-bearing implementation must atomically persist the matching owned card, earned-trace subtraction and completed pair. Lost-response replay deserves care: native RequestClear short-circuits state3 locally, but response-loss retries can precede that state and the wire has no nonce.

The SetTutorialGacha completion lambda **beb7ec** first requires callback result1 atbeb818 and a still-valid popup capture atbeb81e. It removes `tuto_explore` atbeb83e; reads the stored reward marker atbeb868; returns from the display branch if null atbeb880. It parses the marker as a card atbeb890, **removes the reward marker atbeb8ac**, then calls ReqShardExchangeCB(1,card) atbeb8dc. Thus the marker is a one-use local display handoff after inventory mutation, not a persisted server job and not proof of a prior PieceExchange HTTP call.

**Conclusion:** the native guided Recruit action may use reward-bearing Clear37/1 as its exchange transaction. Its response explicitly permits earned-item consumption, so treating it as an unconditional free grant is unsupported. Conversely, requiring an ordinary PieceExchange call first is also unsupported. The client proves the enabled-trace prerequisite and response machinery; original tutorial special reward/cost policy and exact quantity remain unknown. Continue normal UI until the real request identifies which path occurs.
