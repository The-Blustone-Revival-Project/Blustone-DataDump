# Search Normal target exists without a running GetInst job

2026-10-05. Read-only original Thumb and retained symbols. No Ghidra/device/source/runtime operations. G = ELF VA+0x10000. This report separates selected target construction from helper choice and server job persistence.

## Exact normal selection route

CSRSceneFindShard::OnButtonClick Ge24880 extracts the clicked Normal reference ID and calls **CSRFindShardStage::FindExploreInst G90be3c at e24956**, then **PopUpComfirm Ge250d4 at e2495e**. PopUpComfirm constructs the existing FindShardConfirm popup and calls **CSRPopUpFindShardConfirm::SetData Gbe1258 at e25140**.

Despite its name, **FindExploreInst does NOT require an entry from the running PLAY_DATA instance map**. It searches the reference INFO map by the string ID at**90be4c**. If absent, it returns a null shared_ptr at90beec/90beee. If present, it allocates a new **0x80-byte shared allocation at90be58/90be5a**, with the actual PLAY_DATA object atallocation+0x10. It zeros the full object and stores the found shared INFO pointer/control at allocation+78/+7c (**PLAY_DATA+68/+6c**) at90bec4/90bec8. These are the exact fields later dereferenced by RequestStartExploreCardPiece.

Consequently the new normal target initially has zero inst_id, pvid, log_id, counters and helper fields, but a valid shared INFO. This is a normal locally selected attempt candidate, not a server-running job. **GetInst inst:[] is compatible with this construction.** Do not fabricate an owned or timed Search instance merely to avoid a target-null hypothesis.

## Popup and singleton ownership

**Confirm.SetData Gbe1258** retains the supplied shared PLAY_DATA in popup+66c/+670 (be1290/be1298). It immediately reads PLAY_DATA.INFO+68/type atbe12e8/be12ea for its original local marker. It passes the same supplied shared_ptr to **CSRFindShardStage.SetTarget G90b840 atbe13a8**.

SetTarget retains object/control in singleton **+90/+94** (90b870/90b878), then resets transient chosen-helper state: helper-card shared_ptr **PLAY_DATA+44/+48** cleared at90b8b8; friend ID **+50** cleared at90b8ea; virtual-friend ID string **+58** reset at90b8f4..90b922; play-count field+40 is cleared at90b8b4. It does **not** clear the shared INFO+68/+6c. Shared ownership persists beyond popup or GetInst container changes.

An empty GetInst clears the separate running-instance map+30/+34/+38; it does not automatically zero singleton Target+90/+94. A later unknown reference or explicit ResetTarget is a different path. The direct setter call scan found the normal Confirm.SetData call; do not identify SetData as OnInit simply because it is adjacent to that function.

## Begin dependencies remain separate

RequestStartExploreCardPiece Ge2be88 obtains singleton Target and dereferences **Target.INFO+68/type** at e2beae/e2beb0 without a null guard. A valid normal INFO type1 follows Begin; type2 additionally checks target.end_datetime/server clock. Native RequestBegin dereferences the same selected INFO for type/ref_id/target_stage and assigns its eventual log_id through ParseBegin.

Ordinary partner Begin BT_NEXT separately reads **Target.helper-card+44/+48** at e2bb36 and has a null/empty-card-ref fallback confirmation. SetTarget initially clears that helper intentionally; a real partner choice must populate it through normal UI afterward. Thus target existence and selected helper availability are not interchangeable, and a GetHelperList/reference failure must not be repaired with a fake PLAY_DATA job.

The parent's native preparation screenshot72 means the normal confirm UI was reached and is strong context for this path. It does not constitute a bounded live Target pointer or guest ARM fault PC at the later death. The lifecycle proof removes the need for running-job fabrication; it does not prove the cause of the observed partner-screen fault0x1.

## Narrow parent corroboration targets

If decomp or a future selected-target observation is needed: **FindExploreInst90be3c**, **SceneFindShard.OnButtonClick e24880**, **PopUpComfirm e250d4**, **FindShardConfirm.SetData be1258**, **SetTarget90b840**, **Target90b982**, **ResetTarget90b940**. Confirm reference id017 exists and the native INFO type/target stage remain coherent. Do not mutate flags, force scenes, grant a hunter, alter the owned party or call Begin just to create a target.
