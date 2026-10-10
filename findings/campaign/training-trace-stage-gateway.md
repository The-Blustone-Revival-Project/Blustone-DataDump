# Training trace UI and campaign gateway

2026-10-04. Read-only current source, retained symbols, curated card bootstrap decomp and original Thumb disassembly. No device/Ghidra/server writes or client changes.

## Training popup is reference-card driven

The observed Find Training Opponent popup corresponds to **CSRPopupSearchStuff**: Init Gd3c64c, SetData Gd3c740, SetCardBook Gd3c97c, OnButtonClick Gd3d788. SetData calls SetCardBook twice (d3c7c0/d3c818), passing the requested rank stored by SetCardBook at stack+18.

SetCardBook enumerates four roles through GetCardDataByRole atd3ca42; retrieves each reference atd3ca82; excludes source byte info+3c==1 atd3ca88..8e; requires **info+44 equal requested rank** atd3ca90..96; reads inventory count using the string **info+18** atd3cada/d3cade. It builds the eligible reference-card list locally, not by directly iterating GetItem.trace.

The rank field is independently pinned: native-card-bootstrap.txt LAB87c38c calls **CSRCardInfo::GetMinRank** on actualInfo=allocation+0xc, then writes result allocation+0x50 = **actualInfo+0x44**. Thus grouping uses minimum published stat rank, not an owned hunter rank or recruitBirthRanks. Current ordinaryRankStats publishes ranks1..5 for each fixture reference, so empty rank2 is consistent; empty rank1 is not explained solely by birth-grade metadata. Do not add an invented base.rank to solve it. The shard/item identity at info+18 and additional rendering filters need exact parser/UI evidence.

OnButtonClick closes the popup, then its Recruitment branch passes **scene type0x5d** to normal PushSceneFadeOutIn (d3d7da/d3d7ec). It does not pass a campaign stage ID or grant tutorial completion. The button's actual control-name literal needs parent resolution if a scripted UI action is required.

## A native campaign source shortcut exists, but its input contract is incomplete

**CSRPopUpItemDetail::OnButtonClick Gcc6630** has a real source-navigation branch: GetStageLinksDataToStageID atcc6bdc, GetAreaData atcc6c0a, normal PushSceneFadeOutIn atcc7014, and UserDB.PutCurAreaID/PutCurStageID atcc703c/cc704c. This is evidence that an item source entry can navigate an existing campaign link through the game's UI. It does not establish that any arbitrary trace row or Recruitment shard-discovery entry reaches n_01_08.

Its **IsActivatedTrace Gcc7b88** dispatches TRACE_INFO.type and, on one path, calls GetStageAchieveCnt(string) using **TRACE_INFO+0x38** atcc7be0/cc7be4. The meaning of that string (target stage versus prerequisite stage) and numeric type mapping remain unproved. Do not silently put an uncleared stage8 ID into a guessed unlock field or claim that its source button is enabled.

Current fuelItemReference() supplies only AP/BP items and **trace:[]**; no hunter trace item reference or campaign trace-source rows are reconstructed. ItemInfo.SetItem Gaefe10 owns TRACE_INFO reference parsing (map insertion helper af0fd8, getter af13c8). Recruitment CreateGachaTraceCell Ge49590 uses inventory counts. **OnClickRequestTraceSearch Ge3f8b8 invokes RequestGachaGeneral Gf758fc at e3fb08**; despite the label, that branch consumes an inventory-backed recruitment operation, not proof of campaign navigation. Separate CSRFindShardStage and CSRListViewFindShard concern another exploration system; their names alone cannot justify mission Start aliases.

## Narrow next evidence and acceptance

Parent dump/resolve targets: SearchStuff.SetCardBook d3c97c and SetData d3c740; ItemDetail.CreateTraceList cc6044, OnButtonClick cc6630, IsActivatedTrace cc7b88; ItemInfo.SetItem aefe10 trace parser, including the writer of card-info shard ID+18 in SetCard. Resolve exact TRACE_INFO keys/type enum and active-source prerequisite before implementing any rows. No complete safe trace JSON is established in this report.

A campaign source for a real existing stage may be provided only after that contract is recovered; any association of a hunter trace drop with n_01_08 without original evidence must be marked a local fixture. Native UI activation must respect recovered achievement/area checks. Then verify the normal source button emits the existing stage/reference/mission routes; an actual stage8 victory and persisted stars can unlock the native campaign gate. Do not use direct scene jumps, flag clears, ownership consumption or completion aliases as substitutes.

Sources: analysis/native-evidence.tsv, native-card-bootstrap.txt, original libnative_core.so Thumb ranges above; server-ts/src/bootstrap.ts and shop-fuel.ts. G addresses are ELF code VA+0x10000.

## Parser closure from parent's exact dumps

New authoritative inputs: ghidra-training-trace-gateway.txt and ghidra-training-trace-literals.txt. **ret_data.trace is a flat ARRAY**, independent of item[], grouped internally by **item_id**. Each row requires strict strings item_id, source_id, thumb_id plus numeric order and type. SetItem indexes ret_data at aefe34, trace ataf0340/af03aa, item_id af03b0, order af03b8, type af04f0, source_id af0556 and thumb_id af05a0. Numeric strings are accepted by numeric conversion; JSON numbers are sufficient. No nested per-item trace array or invented reward/quantity field is consumed here. The row struct has type+0/order+4/item_id+8/thumb_id+14/source_id+38, stride44.

**Type3 is campaign**, proved by OnButtonClick case3 resolving source_id through GetStageLinksDataToStageID/GetAreaData and taking the original map navigation branch. **IsActivatedTrace case3 requires GetStageAchieveCnt(source_id)!=0**, not merely an unlocked next stage: cc7be0 uses trace+38, callcc7be4, normalized bool atcc7c44..4a. The same source_id identifies navigation destination. Therefore source_id n_01_08 is disabled until stage8 has stars; it cannot provide a first-clear shortcut. An already cleared stage7 source can return the player to the campaign map, where selecting stage8 is normal progression, subject to existing link/area/auto-combat guards. Actual scene/context acceptance remains untested.

Minimal parser-safe navigation candidate, **not an original hunter-drop assertion**:

```json
{"item_id":"EXISTING_ITEM_ID","order":1,"type":3,"source_id":"n_01_07","thumb_id":""}
```

Replace EXISTING_ITEM_ID only with the exact reference ID of the item whose detail popup can already be reached. CreateTraceList calls GetTraceData(popup+a0), so unrelated item IDs cannot populate that popup. Publish the row within ret_data.trace while preserving existing item/global_item arrays. Empty thumb_id is a verified safe path: SetThumbnail cc8b5a..cc8b68 tests string length and skips LoadThumbnail on zero. A known existing art key can be supplied later if independently verified. This row grants no items, rewards or stars and must be labeled a local source-navigation fixture; original drop tables are still missing.

### Why SearchStuff remains blank

The new SetCardBook dump exposes an additional **remove_if predicate FUN_d3dac0** after minimum-rank/role filtering. Offline original Thumb atd3dac0..d3dcfc proves it consults a **per-rank map of string-ID vectors** in popup+9c/a0/a4, searches for the candidate ref ID, and returns1 when search iterator equals end (d3dce8 subtraction, CLZd3dcee, shift d3dcf2). SetCardBook erases those matching the predicate, so **only IDs in this per-rank whitelist survive**. An absent rank creates an empty vector through map insertion and removes every candidate. This is a concrete independent cause of blank rank1 even when minrank1 references exist. The exact whitelist contents and their writer remain pending constructor **CSRPopupSearchStuff::CSRPopupSearchStuff G101f9bc** and helperd3dac0 parent dump/literal resolution. It is not established that current001..004 are in that whitelist; adding GetItem.trace alone cannot defeat this filter.

Thus the ItemDetail campaign contract is recovered, but a complete Gym/Recruitment-to-that-item UI chain is not yet certified. Recover the whitelist and exact per-card shard ID before adding a displayed hunter trace entry; do not fabricate a new playable hunter or lower an existing rank to bypass eligibility.
