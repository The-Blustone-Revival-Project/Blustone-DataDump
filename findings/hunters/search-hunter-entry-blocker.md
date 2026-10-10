# Missing-hunter Search entry: next native seam

2026-10-05. Read-only retained symbols, current server routes and original Thumb disassembly. Evidence screenshots revival-010/35..39 and preserved search-failure/logcat.txt; no Ghidra/device/runtime/source writes.

The Search choice screen38 visibly separates missing hunters, Abyss and Mirage Ruins. The missing-hunter subsystem is **CSRSceneFindShard**, supported by its Normal/FindShard views and CSRFindShardStage reference/instance API. This is distinct from the earlier Recruitment trace purchase and the generic campaign stage map.

## Strongest concrete pre-request dependency

CSRSceneFindShard::SetData Ge244f4 reads UserDB.GetCurExploreID (e2451c). On the no-current/default path, it calls CSRFindShardStage::Normal G90d1e0 at**e2459c**, then performs an **unguarded first-element dereference**: LDRr0,[sp] e245a0; LDRr3,[r0] **e245a6**; first INFO string+8 access e245b0/e245b4. Only later does it call **RequestInst G90e34c at e246da**. An empty Normal catalog can therefore fault before any new HTTP request, matching the observed chronology. It is not established that e245a6 is the actual live fault instruction.

CSRViewFindShardNormal::Init G10b312c also reads **Normal** at10b327e and **GetPositions** at10b3286, but its initial vector-empty check at10b3292..32a0 is guarded. A valid Search reference must supply the native Normal catalog and its positions coherently; no numeric/field aliases are justified before parser recovery.

Current game-routes.ts has no dedicated /explore/GetRef or /explore/GetInst handler. Native URL strings retain **/explore/GetRef**, /explore/GetInst, /explore/Begin, /explore/End, /explore/Reward, /explore/Retry, /explore/Reset, /explore/Entrust. These have their own parser and battle lifecycle, not mission aliases. Exact live boot response/cached-reference contents remain unverified.

## Resource and parser dump targets

Minimal parent batch: **CSRSceneFindShard::OnInit Ge23b44**, **SetData Ge244f4**, **CSRFindShardStage::RequestRef G90d7c4**, **ParseRef G914d28**, **INFO::parse G90a58c**. Resolve OnInit LoadView's actual resource literal **LDRe23b9e / ADDe23ba6**, callLoadView e23ba8. Additional precise targets if the first batch requires them: RequestInst90e34c, ParseInst915390, CSRFindShardStage.Normal90d1e0/GetPositions917efa, CSRViewFindShardNormal.LoadContentsView10b2e88/Init10b312c, SceneFindShard.SetTutorialFinde273a4.

The preserved crash log contains only x86 Houdini PC0x24360e/faultdead0000 and no guest ARM/native game PC. That fault value is insufficient to identify a missing field, an asset or an empty cache. Screenshot39 shows BlueStacks home after process death, not a rendered hunter-search page. No native Search PASS has occurred.

Recover the exact catalog/container/INFO fields and resource key first, then compare what the current account actually received. A nonempty parser-derived local Search fixture may be the correct next server implementation; original hunter search rates/rewards/drop tables would remain fixtures if unrecovered. Avoid repeated clicks before that seam is inspectable; no guide-clear, direct scene jump or client suppression is established by this evidence.
