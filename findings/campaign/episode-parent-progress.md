# Episode parent clear state: enumeration versus acknowledgment

2026-10-05. Read-only original ELF Thumb and prior episode callback/map evidence. No Ghidra, VM, source changes, flags or grants. Addresses are Ghidra coordinates (ELF VA plus10000hex).

## RegisterClearIDs does not derive completion

**CSRMEpisode.RegisterClearIDs Gb1b2ec** clears its output vector, traverses the LINK map, finds matching CSREpisodeData.TYPE values, and calls **RecursiveRegisterClearIDs Gb1baf6 atb1b3ae**. It does not call IsClearedDataById, InsertReadOrClearID or RequestClear and does not write clear set+C4.

RecursiveRegisterClearIDs walks each LINK's child list (sentinel+14, first+18), recurses atb1bb3e, then appends the **current LINK ID** atb1bb80/b1bba0. This is postorder catalog enumeration: descendants precede their parent. It is not a condition checking all children completed and not a state aggregation writer. The misleading word Register must not be interpreted as registering a newly completed parent.

LoadData's direct call sites make the role explicit: atb1a7f2 it passesTYPE3/outputthis+AC; atb1a7fe TYPE4/output+A0. These vectors are generated from loaded content before future gameplay; no user clear state is inspected in those calls. Type-name attribution should follow the graph parser's enum evidence, not convenience names assigned here.

## Pending traversal consults actual clear IDs

**GetNeedClearItem Gb1d290** chooses output vector+AC or+A0 (TYPE4) and scans its IDs against actual clear set **this+C4** atb1d2b6/b1d2ce. It selects the first missing ID; when all entries are present it returns the last entry (b1d2e4..e8). **FindNeedClearItem Gb16880** performs the same scan for a supplied vector. It does not synthesize missing parents or write set+C4.

Therefore a parent not separately present stays pending even when its descendant IDs exist. Postorder enumeration provides a possible normal path to selecting the parent next; it is not proof that all-leaf completion must be inferred by the server's GetLog response.

## Explicit native parent acknowledgment path exists

**ComfirmClearAndReward Ge61f38** checks its current scene/table conditions, calls IsClearedDataById on the supplied ID at e61f5a, and if that clear check fails branches to **e6372c at e61f94**. This actual native closure preserves the supplied ID, captures the scene, and invokes **RequestClear Gb19710 at e638ce**. RequestClear posts that **unprefixed ID** through /episode/Read, already proved in episode-progression-contract.md. This is a separate normal native acknowledgment path, rather than a server-returned invented parent flag.

For the reward arm, ComfirmClearAndReward checks IsGotRewardById at e61f66 and **IsClearedDataById(id)==1 at e61f76..7c**, then tail-calls RequestReward at e61f86. Its immediate predicate is parent/current ID clear state. It does not inspect every descendant in that final function. Earlier scene/table enable logic and runtime completion selection remain separate prerequisites, not fully reconstructed here.

SceneStageList.SetData Ge5f2e4 calls IsClearedDataById at e5f3f8 and updates its per-cell flags accordingly. CheckSceneState Ge5f784 also retrieves runtime clear context through TryGetRuntimeClear b1d5c0 at e5f7ba. The full earlier selection/activation policy has not been decompiled in this read-only lane, so this report does not certify a particular live gesture will automatically emit an E05 parent clear after its8 stories.

## Native maps and safe server conclusion

IsClearedDataById Gb1c810 reads **C4 directly**. InsertReadOrClearID Gb1954c puts unprefixed IDs inC4 and strips r_ intoB8. ParseLog clearsB8/C4 and refills them from encoded read_log[].id. A server may therefore persist a real received **E05** acknowledgment separately from E05_S01..S08; prefixed r_E05 represents read state only. Rewards are the separateD0 set.

There is no proof in the inspected Register/GetNeed functions that the server must add inferred E05 to GetLog as soon as8 leaf IDs exist. **Retain actual native parent /episode/Read acknowledgments as the narrow faithful path.** If a parent row is absent after all children, inspect normal parent selection/ComfirmClearAndReward before changing reload logs. No blanket derived-parent sweep is justified by these functions.

The server's current requirement that all actual descendant bare story IDs be cleared before claiming E05 remains an explicit **LOCAL authorization policy**. It can coexist with native parent acknowledgments; a parent-only request must not bypass that policy. Inferring parent state server-side would be an additional local policy requiring clear documentation and native evidence, not original behavior proved here.

Narrow parent dump targets if needed: RegisterClearIDs b1b2ec, RecursiveRegisterClearIDs b1baf6, GetNeedClearItem b1d290, FindNeedClearItem b16880, ComfirmClearAndReward e61f38 and its e6372c closure, plus SetData e5f2e4/CheckSceneState e5f784 for upstream conditions. No flag was inferred or written by this research.
