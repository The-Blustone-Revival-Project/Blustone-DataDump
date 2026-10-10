# Missing-hunter Search: reference and idle-instance contract

2026-10-05. Read-only parent dumps ghidra-find-shard-entry-contract.txt, ghidra-find-shard-inst-contract.txt and exact-keys; original Thumb comparison for Normal. No device/Ghidra/source/runtime actions.

## Catalog record and Normal selection

ParseRef G914d28 iterates **its JSON argument directly as records** and calls INFO::parse G90a58c. An array is the simple compatible record container; no ref/explore/list wrapper is indexed inside this function. It keys the map by parsed INFO.id. RequestRef G90d7c4 posts /explore/GetRef through PVHTTP TASK_READY lambdas. The exact caller unwrap into ParseRef is not included in this batch, so bare-array **ret_data** versus a caller-selected child is not yet proved solely by ParseRef. Do not mistake its direct argument for the whole envelope.

INFO record fields are exact:

```json
{"type":1,"serial":1,"id":"LOCAL_SEARCH_ID","target_card_id":"004","target_stage_id":"n_01_07","max_join_cnt":1,"max_play_cnt":1,"max_retry_cnt":0,"period":3600,"cost":0}
```

id/target_card_id/target_stage_id are **strict strings**. Other fields are numeric scalar conversions; JSON numbers suffice. The example identities, limits, period and cost are **local diagnostic fixtures**, not recovered Search content or balance. Card004 and stage n_01_07 already exist in the replica; original target-card/stage associations are unknown. Zero cost is not recovered free-search economics and must not enable an unsupported transaction.

**Normal accepts INFO.type==1 only**, proved by original CMP G90d400/#1 and nonmatching branch90d402→90d2d8. Other types must not be added just to populate this vector. At least one actual valid type1 row is necessary for default SceneFindShard.SetData, which dereferences first Normal element at e245a6 before RequestInst. Record serial/order and position cardinality must be checked against the shipped view's GetPositions; a one-row candidate is not by itself a native rendering PASS.

## Idle instance parser

ParseInst G915390 indexes its supplied argument with:

```json
{"inst":[],"play_log":[],"retry_log":[],"reset_price":{"price":0,"price_type":2},"retry_price":{"price":0,"price_type":2},"reset_cnt":0,"cooltime":0,"cleared_explore":[],"user":{}}
```

inst[] is parsed as PLAY_DATA and keyed by its numeric instance identity. Empty avoids creating any running job and clears the current instance map when the field is present. **play_log[] uses LOG records; retry_log[] uses strict strings**, correcting the earlier combined classification. Empty skips both iterations. LOG rows are recovered in search-attempt-persistence.md. cleared_explore[] entries are **strict strings** added to a local cleared-ID map; empty grants no fake completion. reset_price/retry_price are objects containing price and price_type, not flat price fields or vectors. reset_cnt is numeric; cooltime uses numeric conversion and a null/missing value preserves its previous stored field, so explicit0 is appropriate for an idle fixture. Prices/type2 in the example are local display fixtures; retry/reset/Begin should remain explicitly refused until reconstructed.

The final user object is passed to CSRPlayData.SyncUser unconditionally. Original SyncUser G b7047c begins with null-guarded optional resource indexes; its complete empty-object behavior was not decompiled in this batch. Verify user{} preserves all balances before calling this entire response a no-mutation native control. There is no justification to populate invented resource aliases or synthetic reward grants.

The RequestInst batch proves auth fields app_code/app_ver/market/pvid/otp and route /explore/GetInst. Its TASK_READY unwrap into ParseInst should be corroborated alongside the reference unwrap before promoting response hierarchy. No new Begin, End, Reward, Entrust or Retry implementation is established here.

## Actual UI resource

OnInit LoadView resolves **SEARCH/SE_MAIN** (LDRe23b9e/ADDe23ba6), then looks up **NORMAR_S_VIEW** (the misspelling is native) and source elements EXPLORE_CURRENT/PA_TK_SE and EXPLORE_HUNTER_LIST/PA_HT_LI. This independently pins the resource seam. Missing EN alone is not a failure proof because the established loader can fall back to KO. Check actual template/root only if a nonempty valid Normal reference still fails.

Next narrow gaps: TASK_READY reference/instance callback keys and exact ParseRef/ParseInst arguments; full SyncUser optional semantics; view positions and idle PLAY_DATA consumers only if native entry reaches them. An original Search reward/timer/drop claim remains unwarranted. The preserved current crash still exposes only x86 Houdini PC/dead0000, so this parser recovery does not certify the precise failing native instruction.

## Callback and no-mutation closure

Parent subsequently recovered **GetRef callback G91abb8**: successful full JSON envelope **ret_data.ref** goes to ParseRef, and **ret_data.event_ref** goes to ParseEvent. Therefore GetRef response ret_data is **{ref:[INFO rows],event_ref:[]}**, correcting the earlier unresolved outer shape. Do not send a bare ret_data array.

Original ELF direct-call scan located ParseInst caller **G91b22c**. Its success path has exactly one JSON index: LDRe91b256 slot91b290 (word0x144d75d), ADDr1,PC91b25a resolves G1d689bb **ret_data**, identical to the independently resolved GetRef callback literal. Call91b25c returns that object inr0; MOVr1,r0 at91b260 and MOVr0,r8 at91b262 feed ParseInst at**91b264**. No nested inst/info child is selected before ParseInst.

This is positively attributed to RequestInst: original function vtable **ELF2146840**, invoke slot**ELF2146860** (primary vptr+18) points **ELF90b22d/G91b22d**. Its actual typeinfo name contains CSRFindShardStage11RequestInst / TASK_READY $_10 / second callback UlSN_SR_E0. The outer RequestInst TASK_READY vtableELF2146800 invokes G91af00. Thus **GetInst ret_data directly contains the idle-instance fields** described above, not ret_data.explore or another alias.

Parent's fresh SyncUser decomp proves **user:null** initializes the SRET reward and returns immediately on JSON type0, before player writes. Use **user:null**, replacing the provisional user:{} in the earlier candidate. A no-job entry candidate is:

```json
{"inst":[],"play_log":[],"retry_log":[],"reset_price":{"price":0,"price_type":2},"retry_price":{"price":0,"price_type":2},"reset_cnt":0,"cooltime":0,"cleared_explore":[],"user":null}
```

Publish this as GetInst ret_data with no running instance, fake clear, reward or user balance update. Display prices/costs remain local fixtures and unsupported paid/start operations must not be treated as implemented. Parser shape is now closed; native entry rendering and catalog/view compatibility still require observation.
