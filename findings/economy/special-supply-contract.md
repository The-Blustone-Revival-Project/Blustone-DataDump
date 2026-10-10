# Special Supply: genuine inventory reward seam

2026-10-05. Read-only original ELF Thumb and parent's completed ghidra-special-supply.txt/-keys.txt and ghidra-special-supply-refresh.txt/-keys.txt. No source, Ghidra, adb, VM, account mutations, grants or runtime claims. Addresses are Ghidra coordinates (ELF VA plus10000hex).

## Real native UI callers

**CSRSceneSupply::OnClickReceiveAll Gedc520** calls **CSRSyncSupply::RequestSpecialReward Gf96e68 atedc7bc**. **CSRSceneSupply::OnButtonClick Gede278** calls it atede858 for the individual UI path. These are positive direct call sites, unlike the platform-only Mail attachment path. UI completion is **CSRSceneSupply::ReqSupplyCB Gedc9a4**, taking result and list<SPECIAL_SUPPLY_INFO>. No live UI action was performed by this lane.

## Claim request serialization

RequestSpecialReward receives vector<uint64> IDs. It constructs a JSON collection by pushing unsigned integer elements atf96f62, then **JSON.dump atf970b6** yields the form value **id_list** (LDRf970ba / ADDf970bc). The URL is **/supply/SpecialListReward** (ADDf971e2). Fields are auth5 plusid_list:

```text
app_code, app_ver, market, pvid, otp, id_list="[123,456]"
```

This differs from Mail removal's comma-list serialization. The IDs identify existing SpecialSupply entries, not item/card instance IDs. The builder checks FindSpecialSupply and excludes a supply containing exactly one item when GetItemData's field+4 equals0x1e. That discriminator's named meaning remains unresolved; do not publish an arbitrary single-item row before checking this client-side filter. Its lookup also means valid item references matter before any HTTP claim.

## Claim callback and actual state mutations

**ReqSpecialRewardCB Gf97610** parses envelope result_code then ret_data atf97744. Its recovered parents are:

- **ret_data.achievement**: optional achievement parser.
- **ret_data.user**: optional nested resource/progression fields. gold, exp, vip_exp, free_iap, iap, honor use prev/cur pairs; card_inven_max usescur. AP and BP each have prev/cur **and their own nested deadline**: user.ap.ap_charge_time and user.bp.bp_charge_time. SyncAP/SyncBP are explicit calls, not mere UI reward labels.
- **ret_data.card[]**: numeric iteration; each complete owned card instance goes through **ParseCardInst atf9811c**, then Inventory.AddCard(card,1). A bare card object is not the numeric list contract.
- **ret_data.item[]**: rows **inst_id, ref_id, added** (ADDf982d8/f9837c/f98394); actual **Inventory.AddItem atf9842c**. added is an increment, not final quantity.
- **ret_data.gem[]**, **skin[]**, and **is_skin_duplicate**: separate branches. Their full settlement row shapes are not rederived here; omit unsupported rewards rather than guessing.
- **ret_data.target_inst_id[]**: array of SpecialSupply IDs acknowledged as settled. Despite its singular name, it is indexed numerically atf98886, each scalar converted to uint64 and zero skipped. Matched cached supplies are copied into the result list and **RemoveSpecialSupply** is called. A scalar target_inst_id is not the array contract.

The charge-time parent is corroborated by decompile pbVar8=user followed by ap indexing then ap_charge_time indexing before SyncAP; BP mirrors that. Flat resource aliases would not satisfy those nested deadline reads.

This is therefore a real card/item/resource delivery path. A success without matching reward mutations and target IDs would be misleading. A minimal one-feature receipt can supply only its supported item or resource rewards plus target_inst_id; unsupported optional branches should remain absent/null/empty as their guards permit. A precise full implementation still needs the user's earned source ledger and callback/display prerequisites verified; this research does not invent original balance or grants.

## Refresh list wrapper

**RequestRefreshSpecialList Gf991a0** posts **/supply/RefreshSpecialList** with auth5 only (URLADDf993d6). **ReqRefreshSpecialListCB Gf99758** indexes **ret_data** atf997ec, then **special** atf99800. It clears the prior SpecialSupply vector, iterates this collection, calls **ParseSpecialSupply Gf95bb8 atf998a2**, and adds only rows with nonzero ID through PlayData.AddSpecialSupply. A supplied empty special[] is a real authoritative empty list, not a merge retaining previously cached rows.

It also reads optional **ret_data.gacha_specific** (ADDf9990e); that subsystem's exact reset/update semantics are outside this task. Minimum empty refresh wrapper:

```json
{"result_code":1,"ret_data":{"special":[]}}
```

## SpecialSupply display row versus settlement row

ParseSpecialSupply consumes each display row directly. Exact names recovered:

```text
id, expire_date, npc_id, title,
ap, bp, honor, free_iap, iap, gold, user_exp, vip_exp,
is_skin_duplicate, str_id, str_param,
item_list[{id,qty}], card_list[{id,qty}], gem_list, skin_list
```

id is uint64 identity. String fields/translation parameters, expire_date time units, npc_id presentation and gem/skin subfields need further bounded parser review before a nonempty row can be advertised confidently. Crucially **display item_list{id,qty} is different from claim item{inst_id,ref_id,added}**, and display card_list{id,qty} is different from claim card[] full instances. Do not echo the display row as the claim receipt.

## Next safe implementation seam

Use an explicitly earned source (for example a recorded native completion with an intentionally deferred local reward), create one durable pending supply with supported published references, expose it through special[] onrefresh/lobby, and settle only authenticated selected IDs exactly once. No starter auto grant is justified. Record original quantities/prices/timers as unknown and any chosen local values as fixtures. Preserve unclaimed supplies across restart; validate stale/duplicate claims without repeating additive card/item receipts. Native ReceiveAll eligibility and individual control names should be reviewed atedc520/ede278 before testing the first actual claim.

Remaining narrow dumps: ParseSpecialSupplyf95bb8 for exact strings/date/npc types, RequestSpecialRewardf96e68 for named itemtype0x1e, ReqSupplyCBedc9a4 for display requirements, and refresh's gacha_specific consumer. No reward was issued or claimed here.
