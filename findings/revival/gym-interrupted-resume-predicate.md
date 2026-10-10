# Interrupted Gym NPC resume: guarded native predicate

2026-10-04. Read-only original Thumb instruction flow and `ghidra-trainer-house-npc.txt`; no patches, runtime calls, state writes, adb or Ghidra performed here. G addresses = ELF+0x10000.

## ABI and original branch

SetHouseNPC entry r0 manager, r1 nextNPC SceneTYPE, r2 stage-achievement TU gate, r3 entry tutorial TU. Prologue GEB258A r5=r0; GEB258E r10/sl=r3; GEB2590 r4=r2; GEB2594 r8=r1. These callee-saved registers preserve identities across calls. Stack parameters hold three dialogue-key strings; r4 is later reused for shared control, so do not mistake its post-prologue value for stagegate.

GetStageAchieveCnt gate called GEB25AA; compare GEB25AE and zero branch GEB25B0→GEB2658 locked ordinary NPC. Reaching state check therefore already proves the actual supplied achievement gate positive. Matched Gym caller provides nextSceneA8, stageGateTU16 (=actual n_01_07), entryTU8.

GEB25E6 reads SyncTutorial pointer from r6(SyncMgr)+0x24. GEB25E8 r1=sl; GEB25EA r2=0; call GetState GEB25EC (callee Gf9a956). GEB25F0 compares result to1; GEB25F2 BGT→GEB2726 chooses ordinary NPC. Original lower-state path later requests Clear8/0, then reaches TutorialNPC construction **GEB27F8**.

## Narrow recovery condition

A parent instrumented-only recovery can evaluate this conjunction at the state branch:

- exact known original library/callsite/class ABI;
- entryTU r10/sl==8;
- nextNPC scene r8==0xA8 (restrict to matched Gym caller);
- original GetState(8,0)>=2 (the interrupted/reentered case);
- fresh GetState(8,1) exactly0 or1 (actually pending; reject negative/unknown or >=2);
- actual stage7 positive already proved by the earlier native gate in this call.

On true, reuse **original TutorialNPC construction block GEB27F8**, retaining original NPC0042/SR_NPC_TUTORIAL_BRIDGE and all arguments. Do not redirect to earlier GEB25F6, which would issue Clear8/0 again. Do not alter tutorial state, local marker, nextscene, otherhouse predicates, sources or balances. Native TutorialNPC marker/finger handlers perform their original later selection/scene flow; no direct AE jump is part of this condition.

On false retain original CMP/BGT outcome and registers. A nested GetState call clobbers caller-saved registers and flags/LR; parent must preserve original state result and any live caller temporaries, restore ABI stack alignment and LR, and replay original compare on the unchanged false path. Callee-saved r5/r6/r7/r8/r9/r10 identities must remain intact. Original construction expects its full frame and stack string parameters, not a naked callable interior address from another frame.

## Limits

This establishes a narrowly guarded compatibility repair for an interrupted native entry phase; it is not recovered original server behavior. Marker6 currently denotes rank-guide continuation and may require a max-level eligible target; resuming the original NPC class does not manufacture that level or certify safe training. Before any material action, existing selected-source/target ownership protection and authorization still apply. No flag rollback or directscene request is justified by this report.
