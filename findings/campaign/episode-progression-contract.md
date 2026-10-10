# Episode progression from shipped story data

2026-10-05. Read-only original ELF Thumb/RTTI, existing episode-route-table.md/episode-scene-routing.md/native-episode-log.txt, parent's completed ghidra-episode-progression.txt/-keys.txt and ghidra-episode-progress-maps.txt/-keys.txt, and public PAD resource extraction. No Ghidra/VM/device/server edits, flag writes or grants.

## Critical correction: read_log encodes read versus clear

**CSRMEpisode::RequestRead Gb19638** prepends **r_** (LDRb19654/ADDb1965a), then calls **RequestReadOrClear Gb178f0 atb1969c**. **RequestClear Gb19710** passes the original unprefixed ID to the same method atb19750. Both post **/episode/Read**, with auth5 plus **id** (ADDb17a56, routeADDb17b9a). r_ is an ID prefix, not a generated request-key name.

**InsertReadOrClearID Gb1954c** compares the first2 characters against r_ (ADDb1958c). A matching prefix is removed atb195a6 and the remainder inserted into set **this+B8**. An unprefixed ID is inserted into set **this+C4**. Direct getters prove these meanings: IsReadDataByIdb1c7f8 readsB8; IsClearedDataByIdb1c810 readsC4; IsGotRewardByIdb1a600 separately reads **D0**.

**ParseLog Gb19268** iterates **read_log[].id** strings and calls InsertReadOrClearID atb19366. Thus the actual reload DTO is:

```json
{"read_log":[{"id":"r_E01_S01"},{"id":"E01_S01"}],"reward_log":[{"id":"E01"}]}
```

The example illustrates a read and clear of one shipped story plus a separately claimed episode reward, not completed live events. Bare unprefixed read IDs would restore clear state rather than read state. **This supersedes the old route-table description of independent read/reward maps.** Both read and clear sets B8/C4 are reset before read_log refill. reward_log[].id fills D0 directly; that set is separate and its destructive reset was not proved in the inspected ParseLog body. Empty reward_log cannot be described as definitely clearing an already-live D0 set.

## Exact Read completion callback

Original function-object vtable **ELF2153130**, invoke+20 points to **Gb20000**. Its RTTI explicitly names the RequestReadOrClear $_5 task continuation. It checks GetResultCode1 atb20022/b20028, then calls InsertReadOrClearID with the **captured request ID** atb20032. It does not require an echoed response id. On failure it stores that encoded ID through **CSRUserDB::PutUntreatedEpisodeData atb20044**, providing a local deferred retry seam.

The requester already calls InsertReadOrClearID optimistically **atb17910 before HTTP**. Therefore native immediate read-state changes do not prove backend persistence; reload must verify the durable encoded logs.

After either result branch, the callback extracts **full JSON.ret_data** atb20054 and passes it to **CSRAchieve::ParseLobbyEnter atb2005c**, then forwards the result to its captured callback. Return the established neutral achievement/lobby-quest receipt shape inside ret_data for a pure progress acknowledgment; do not invent episode card/item rewards here. Missing ret_data is not an independently audited safe callback DTO. Parent's existing achievement parser evidence owns exact neutral daily_quest/linear_quest fields.

## Reward route: known transport, settlement still gated

**RequestReward Gb1979c** posts **/episode/Reward**, auth5 plus **id** (ADDb19968, routeADDb19aac), using the original episode ID rather than r_-prefixed story ID. Its continuation's success path extracts ret_data atb206e4, calls achievement ParseLobbyEnter atb206f0, then **CSRMEpisode::ParseReward Gb1ca7c atb206fa**. That helper indexes top-level **item** (ADDb1cacc) and **user** (b1cb00), but its transitive parser/inventory/consumption semantics have not been fully reconstructed in this unit. Rewards must wait for exact receipt and valid item references; no generic success or copied display reward is justified.

## Catalog is local content, not an invented reference API

Already-known LoadData Gb1a618 and ReadJson Gb1a8b0 are now corroborated by original literals. LoadData reads local **season_list**, then SeasonParser (callb1a742), plus **event** and **tuto** resources. ReadJson appends **.JSON** (ADDb1a91a) and has localized resource fallback paths. No additional /episode/GetRef endpoint was recovered.

The public preserved **R_EPISODE.jet** (38080bytes, SHA2567f4362cdf80545a6da937444094837f334c8aae4f9f791d6ff4161948d98a01e) contains66 decoded resources. Its RW payload1 is **["season1"]**. Payload2's root is **type season/idS01**, containing E01..E18 episode nodes and real story/combat links. Resource filename/descriptor attribution must distinguish **season1** loader name from **S01** graph identity; root ID alone is not proof of the filename. Original descriptor names are being independently inventoried by the character lane.

The distinct **EPISODE.jet** (6529928bytes, SHA2567bc7b12c57847e690648286170167b2d14ab9207d6df21d35c87f7c6b909ed30) contains art resources and no JSON catalog in this read-only decode. Neither package's current native serving/loading was validated here; default start-server.ps1/source grep does not explicitly select R_EPISODE. Content availability needs resource-serving proof before story UI claims.

## Curated exports and recovered values

Exported **analysis/recovered-reference/EPISODE_S01.json** preserves the complete shipped graph; **EPISODE_S01.manifest.json** records source hash, resource index2/container offset1056, output hash and limits. Existing manifest was not overwritten by additional extraction.

Additional **EPISODE_STAT_ACTORS.json** contains152 shipped episode actor records. They are **episode-only actor STAT data, not ordinary hunter base stats**. Also exported61 **EPISODE_COMBAT_*.json** records, beginning CB0001..CB0004. **EPISODE_COMBAT_STAT.manifest.json** independently records all62 output hashes and their original zero-based payload indices. No references were merged into the live server or runtime catalog.

Real early nodes include E01_S01, E01_S02, E01_S03. E01_S01 has entrypointEP_0301A, local_MIDGARD position, battlefalse; E01_S02 usesEP_0302A/local_GYM and battletrue. These are actual shipped graph values, not fabricated campaign stage IDs. Shipped episode rewards include E01 GC2qty3, E02 FMD1qty30, E03 GC3qty3 plusGC4qty3, each free_iap0. Recovery of these values does not prove item references/materials are available or authorize a reward grant.

Payload0 is original event **EV05**, scheduled2020-12-24 through2021-01-07, with its own EV41 requirements. Do not silently enable that expired seasonal event under a present-day date. No original economy extrapolation is needed to implement the regular S01 progress bookkeeping.

## Narrow safe next implementation

Persist authenticated encoded /episode/Read IDs against the real exported graph, distinguish r_-read versus unprefixed-clear, and return them through read_log[].id after restart. Keep reward_log separate. Native optimistic state and deferred retries require idempotent bookkeeping. A read ACK should grant no reward and write no tutorial markers. Reward mutation and actual story battles require transitive parser/material/resource validation before promotion. This unit supplies source evidence and artifacts only.

## Neutral Read receipt and no invented debit

Follow-up original instruction inspection and the completed **ghidra-trace-lobby-achieve.txt/-keys.txt** prove the compatible neutral ret_data:

```json
{"dailyquest_min_stage":"","daily_quest":[],"linear_quest":[]}
```

CSRAchieve.ParseLobbyEnter indexes dailyquest_min_stage at844940 and converts it to a string **unguarded at844950**. Empty string skips assigning the existing gate at84496c; a nonempty string changes it. daily_quest (ADD84497c) and linear_quest (ADD844a44) are collections iterated for updates. Empty collections produce no fabricated quest updates. This corrects older battle-lifecycle.md's blanket claim that all3 may safely be omitted; that statement predates exact string-parser recovery.

The complete Read/Clear callback b20000 has no UseItem, SyncUser, AddItem, gold/AP debit or consume_result parser: it restores the captured encoded ID, or saves a failed request for retry, then processes achievement updates. The request itself is auth5+id with no quantity/cost field. These are positive protocol limits; they do not reconstruct all historical server authorization policies.

A recursive scan of the full recovered S01 graph (147 unique node IDs) finds **zero require fields**. Therefore an authenticated idempotent **regular S01 read/clear ACK-only implementation** is supported without inventing an inventory debit. Reward eligibility remains separate. Do not generalize this to seasonal EV05, whose shipped episode nodes explicitly require EV41 items, or fabricate event-cost behavior from the ordinary story path. This follow-up made no account or source mutation.

## Read save-failure rollback source review

The updated state.ts Read path now wraps persist() after a newly appended flag. On failure it removes the last element from the exact selected read_ids/cleared_ids collection and returns a non-success **neutral quest receipt**. recordEpisodeProgress only appends when changedtrue, and persist is synchronous, so the reviewed path removes its own new flag without disturbing earlier flags or touching the other collection. Duplicate existing IDs do not enter the rollback branch.

tests/episode-progress.ts injects a persist exception for both r_E01_S01 and E01_S01, asserts the entire game remains unchanged and the refusal includes dailyquest_min_stage:"", restores persistence, records those IDs normally, then reloads and verifies the durable encoded log. This demonstrates the intended source-level deferred retry behavior: a failed attempt does not leave an in-memory flag that would cause its next retry to skip saving. The injected failure test starts from empty progress; preservation of earlier flags is supported by append/pop source flow rather than a separate populated-state failure test.

Expected NativeAuthErrors for non-GetLog Episode actions now all receive the callback-safe neutral refusal; the previous auth-mismatch failure-shape gap is closed in source. Parent acknowledgments remain **actual explicitly received unprefixed IDs**. No inferred parents, tutorial markers or automatic descendant completion were added. This lane found no actionable bug in the small Read rollback and did not run tests or operate the native client.
