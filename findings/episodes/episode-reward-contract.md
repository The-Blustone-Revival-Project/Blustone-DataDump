# Episode Reward: exact settlement parsers and replay limits

2026-10-05. Read-only original ELF Thumb/RTTI, exported S01 graph, existing SyncUser decompile and curated episode progression evidence. No Ghidra, VM, server source edits, grants or claims. Code addresses are Ghidra coordinates; vtables are explicitly ELF VAs.

## Transitive helpers are SyncItem and SyncUser

**CSRMEpisode::ParseReward Gb1ca7c** receives ret_data directly and builds SRREWARD_INFO. It extracts **item** (ADDb1cacc), calls **CSRPlayData::SyncItem Gb7108c atb1cada**, merges its returned display reward through SRREWARD_INFO.operator+= atb1cae4, then extracts **user** (ADDb1cb00), calls **SyncUser Gb7047c atb1cb0e**, and merges again atb1cb18. There are no distinct named ParseRewardItem/ParseRewardUser functions in this path. It does not parse a nested reward object or the shipped catalog's reward.item display rows directly.

## Exact item receipt: additive full instance identity

SyncItem initializes its returned reward structure, null-checks the supplied item collection atb710cc..d0, and iterates each row. Exact field literals:

```text
inst_id LDRb71126 / ADDb71128
ref_id  LDRb7112c / ADDb7112e
added   LDRb71132 / ADDb71134
```

inst_id uses uint64 conversion; ref_id is a **string**, from_json<string> atb711b6. added is converted to signed32 atb711f6 but passed as the quantity bit pattern to Inventory.AddItem's unsigned32 argument atb71230/34. Consequently negative values are unsafe and must be rejected server-side rather than used as deletion or rollback.

**Inventory.AddItem Gaec508** uses the supplied instance identity/reference, constructs the inventory entry if needed, and directly adds quantity at**aec5c0**, storing current quantity at**aec5c2**. Thus this receipt is **additive**, not an absolute inventory snapshot. SyncItem also appends ref_id/added to SRREWARD_INFO's display vector atb712ce..b712fe. A zero added row can still appear in the display vector; use an empty item array for a no-item acknowledgment instead of fabricated zero reward lines.

```text
ret_data.item:[{inst_id:ACTUAL_STACK_ID,ref_id:"GC2",added:3}]
```

This example matches the recovered E01 GC2qty3 catalog reward **only when** GC2's real item definition/resource and a valid durable inventory instance are available. It is not a performed grant. Shipped display reward.item[{ref_id,qty}] lacks the instance serial and uses a different quantity key; echoing that catalog row is not a valid settlement receipt.

## User receipts

SyncUser **Gb7047c** is the existing recovered shared resource parser. user:null initializes/returns an empty reward before any player write; this is safe for a genuinely item-only transaction. Wallet changes use **user.iap{prev,cur}**, **free_iap{prev,cur}**, **gold{prev,cur}**, not scalar quantities or Shop's iap_qty/free_iap_qty names. It writes absolute current balances and builds display deltas. Include only actual changes, with matching durable before/after values; unsupported resource branches should not be fabricated.

All recovered regular S01 episode rewards have free_iap0 in the examined early rows, so an item-only receipt with user:null is justified for those rows if their item settlement is implemented. This does not establish a general all-season reward wallet policy. Exact shared SyncUser proof is ghidra-find-shard-sync-user.txt and search-repeat-contract.md's wallet appendix.

## Request callback and reward marker

The existing requester **Gb1979c** posts auth5+id to /episode/Reward, preserving the unprefixed episode ID. Original function-object vtable **ELF21531b0**, invoke+20 points to **Gb20680**; its RTTI explicitly names RequestReward $_6 task continuation.

The continuation obtains GetResultCode atb206a2. On result1 it extracts **full JSON.ret_data atb206e4**, calls **CSRAchieve.ParseLobbyEnter atb206f0**, and invokes ParseReward atb206fa. It copies the resulting SRREWARD_INFO into its outgoing callback value. Only after these parser/mutation calls does it insert the **captured requested ID** (closure+30) into **CSRMEpisode reward set+D0 atb2074c**. No echoed response id or reward_log collection is needed for this immediate success path. A response whose parsers fail must not be treated as a completed/native-usable grant merely because server result1 was written.

Include the established neutral quest siblings at the same ret_data parent:

```text
dailyquest_min_stage:"",daily_quest:[],linear_quest:[],
item:[ACTUAL_SETTLED_ROWS],user:null
```

These quest fields are not nested under user or reward. reward_log[{id:EPISODE_ID}] on GetLog is the separate reload path for claimed state.

RequestReward first checks this+D0 atb197b8..c6. If already present, it skips HTTP, returns an empty SRREWARD_INFO and **result0x2806 (decimal10246) atb197fc** through the captured callback. This is native already-claimed rejection evidence, not permission to delete or reset reward flags. If server-side replay policy uses another non-success code, keep its behavior explicitly local rather than claiming original fidelity.

## Lost-response and duplicate receipt hazards

There is no request nonce beyond authenticated account and episode ID. A sound server ledger must settle each episode reward once and atomically persist claimed ID plus inventory/wallet changes. The client prevents normal repeat HTTP only after its local D0 set is updated; it cannot prove the first response arrived.

**Do not replay a cached full item[] receipt blindly.** A duplicate success applied to the same live native inventory will add the reward again, even if the server granted it once. Reconciliation through an actual absolute inventory refresh or an empty additive replay receipt is required. Returning success with item:[]/user:null can restore the local D0 marker without another native quantity addition, but after a truly lost first receipt the UI inventory/display may remain stale until refresh. That is a concrete limitation to document and test, not exactly-once native delivery proof. Returning already-claimed failure avoids duplicate additions but also leaves a lost-response client's claimed state dependent on GetLog refresh/reload.

The catalog proves original reward values, but completion eligibility, all-child read/clear aggregation and original retry code policy were not fully recovered in this task. Gate server claims against actual persisted story progression according to explicit local policy until that eligibility is proved. Never grant from a request for an arbitrary graph node, silently substitute another reward material, or enable expired EV05 because its catalog also exists.

No reward was issued or claimed by this lane. Remaining native acceptance: actual item-definition/resource validation, successful original UI claim, rendered reward popup, exact one additive inventory mutation, then restart restoring both stack quantity and reward_log without another grant.

## E05 capsule reward and native eligibility boundary

The exported original E05 node has **AIRSHIP_TICKETqty20/free_iap0**, and8 actual story descendants E05_S01..E05_S08. E05_S04 and E05_S06 have battletrue; the other6 have battlefalse. Therefore a supported-reference E05-only settlement can use item[{inst_id:ownedCapsuleStack,ref_id:"AIRSHIP_TICKET",added:20}], user:null, neutral quest siblings. Refusing any chapter containing unsupported material is coherent and avoids substitution. Fresh-only additive rows with empty replay rows match the parser limits described above; stale native inventory after a lost first response remains the documented refresh limitation.

**CSRSceneMEpisodeStageList::ComfirmClearAndReward Ge61f38** is a positive native reward eligibility caller. It checks IsGotRewardById at e61f66, then **IsClearedDataById(id)==1 at e61f76..e61f7c**, and tail-calls RequestReward at e61f86. It does not use IsReadDataById for that final reward gate. This checks the passed episode/parent ID's native clear set, not an already-proved all-leaf server predicate. Leaf-to-parent completion aggregation is implemented elsewhere through RegisterClearIDs b1b2ec / RecursiveRegisterClearIDs b1baf6 and remains unresolved here.

Requiring **all actual descendant story IDs in bare clear logs** server-side is a conservative explicit local authorization policy compatible with the wire; it must not be claimed as the exact recovered original aggregation rule. A parent-only clear or all-prefixed read logs should not bypass that chosen earned-completion policy. No reward was granted during this additional inspection.

## Source audit of the initial E05 implementation

Read-only inspection of state.ts episodeAction, episode-progress.ts and tests/episode-reward.ts confirms the recovered20 AIRSHIP_TICKET value is loaded from the exported original graph. The fresh receipt uses additive item rows and user:null; durable replay returns item:[]; all8 story clear IDs are required as the explicit LOCAL gate. Tests cover parent-only/prefixed/partial refusal, quantity overflow refusal,20 addition into an existing stack, reward marker reload, empty additive replay and account isolation. This lane did not run tests or observe a native claim.

Three actionable gaps in the inspected initial source were reported to parent:

- **Authentication refusal receipt:** episodeAction only catches the exact missing-account error text. Other expected NativeAuthErrors (pvid/transport mismatch) escape to server.ts's generic failure envelope, which lacks the neutral quest string. Read's callback processes ParseLobbyEnter even on failure, so every expected authentication refusal for that path needs the neutral quest fields while retaining the failed result. Existing tests cover missing credentials but not those mismatch shapes.
- **New stack serial collision:** allocation validates next_item_inst_id's numeric range but does not ensure it is unused among game.items. Normal counters may be coherent, but a stale migrated counter can create a duplicate serial resolving another reference in the native inventory. Refuse or safely derive an unused serial before mutation; do not silently overwrite another stack.
- **Persistence failure atomicity:** quantity/new stack/counter/reward marker mutate the shared in-memory game before persist() writes/renames its file. A write/rename exception leaves the process's game claimed and credited while disk remains old; a same-process retry then returns an empty additive receipt although the original HTTP failed. The successful synchronous path persists quantities and marker together, but storage-error atomicity is not proved. This is an existing store-wide pattern; a staged transaction or rollback must preserve consistent memory/disk outcomes before stronger atomic claims.

No existing native DTO incompatibility was found in the fresh E05 success path. Fix status of these gaps is not claimed by this initial audit; source/runtime edits remain parent-owned. No grants or live account actions occurred.

Follow-up source review closes those initial gaps: non-GetLog expected NativeAuthErrors all return neutral quest refusals; new stack IDs are checked against existing item serials; added totals are bounded to signed32 max; reward persist exceptions restore prior quantity/counter and remove only the newly appended marker/stack before returning failure. The related Read path now similarly rolls back its newly appended flag, so deferred native retry can save it. These are inspected source changes, not a new native reward/UI validation claim.
