# Read-only Raise source/target observer specification

2026-10-04. Existing decomp, original native symbol/RTTI evidence only. No runtime operation, Java/Ghidra/adb, reader code or server mutation by this lane.

## Correct target shape

**table+0xd48/+0xd4c is a uint64 owned target instance ID, NOT a shared_ptr.** MakeInfo in ghidra-gym-auto-source-order.txt constructs CSRCardAnalyzer from *(ulonglong*)(this+0xd48); ArrangeStuff in ghidra-gym-source-sort.txt excludes candidates by exact low/high ID comparison against these words. Do not dereference target id5 as a CSRCard address. Candidate and selected source IDs are also uint64 serials, requiring no guessed CSRCard object offset.

The vectors are independently proved: OnReset G101b3f4 swaps ArrangeStuff result into candidate begin+0x65c/end+0x660/cap+0x664; AddStuff G101e3dc appends uint64 to selected begin+0x668/end+0x66c/cap+0x670, stores low/high at adjacent words and advances8. Sources: ghidra-gym-auto-source-order.txt, ghidra-gym-source-sort.txt, gym-tutorial-auto-source-selection.md.

## Guarded scene acquisition

Use established app→manager current-owner chain only:

```
app=u32(B+ELF0x21ef1e0)
manager=u32(app+8)
current=u32(manager+0x34)
```

Require readable, aligned pointers and exact primary vptr checks: app B+ELF0x2140cb0; manager B+ELF0x21735a4. For offsets in this report require current primary vptr **B+ELF0x2176e20 TutorialLevelUp**, or **B+ELF0x218278c ordinary TableLevelUp**. ELF vtable bases are symbol+8 and separately corroborated by native class evidence in gym-tutorial-auto-source-selection.md. Current manager field+34 is an owned scene pointer, not history; +44 history contains scene type enums and must not be followed.

If manager.current is another class while the Raise UI appears, return class-mismatch/inconclusive. A modal can belong to a separate native scene/UI hierarchy; this specification does not invent a currentmodal pointer or traverse arbitrary UI children to find a plausible table. The known primary TutorialLevelUp guard is sufficient **if that exact object is actually reached**. Source/target offset reads on Village/CardSel/Gym handlers or listener secondary vptrs are forbidden by the spec. To pin a different owning chain, inspect TutorialLevelUp creation/store in SceneMgr factory, not an arbitrary mapped address scan.

## Bounded coherent snapshot

Read candidates and selected as vector headers {begin,end,capacity}, plus target uint64. Require ordered begin<=end<=capacity, aligned pointers, lengths divisible by8, maximum32 entries, and entire requested spans readable in mapped memory; all-zero vector is empty. Reject null begin with nonzero end/capacity and unsigned wrap/oversized extents. Read only entry IDs, never card contents/secrets.

Re-read scene pointer/vptr and headers/target after copying both arrays. Accept only stable values; report unavailable/unstable otherwise. This minimizes mid-transition ambiguity without taking ownership or invoking native functions. A double-read does not make concurrent heap access inherently atomic; the existing reader must retain its mapped-page/read-failure safeguards.

Output scene class, target decimal uint64, candidate IDs, selected IDs and stable boolean. No memory writes, native calls, scene reload, selection changes or Train action belongs to this observer.

## Exact donor acceptance condition

The proposed fresh donor6 has **not yet been granted in this task context**. After independently successful authorized grant/unlock and native refresh, acceptable observation is target==the intended Tyltyl owned instance (parent currently target5), selected count1 and selected[0]==6. Candidates may contain protected originals; selection is the decisive consumption set. Candidate first6 corroborates auto-add sorting but cannot replace selected-only6 proof. Stop on selected2, any original/protected ID, multiple selections, target mismatch, class mismatch, unstable reads, or donor6 missing. No final Train permission is added by this report.

Next parent native proof if current chain misses: CSRSceneTutorialLevelUp::OnInit Geea490/SetTutorialLevelUp Geea4b0 and SceneMgr factory calls constructing TutorialLevelUp (shared_ptr conversion Gebddc4), to identify actual owner field. Existing target/vector code already settles ID shapes; no CSRCard instid-offset guess is needed.
