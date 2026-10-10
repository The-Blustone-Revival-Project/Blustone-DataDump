# NPC/Episode dialogue choice listener and input prerequisites

2026-10-05. Read-only ghidra-episode-choice-input.txt and original ELF Thumb. No Ghidra/VM/source/flags/handler or scene calls. Parent reports2 normal Mission touches leaving dialogue unchanged; their selected node/listener/geometry state was not read by this lane.

## Selection callback is OnButtonClick, not generic tap advance

**CSRDlgPlayer.OnButtonClick G8f1214** is the actual button-selection callback. It first handles special skip/video controls, then reads the active talk vector+4bc and requires its **first drawable named UI_DI_SEL_HEAD** (literalLDR8f12b0/ADD8f12b6). A different first talk-box type exits that choice path.

It obtains scroll offset from ScrollView+10c; if offset magnitude>1 and the view is not already scrolling, it calls MoveTo instead of immediately selecting. Otherwise it iterates talk-box wrappers and gets each **BT_SEL** through ScrollView.GetButton at8f1334, comparing the returned pointer to the actually clicked widget at8f133a. Rendered Mission text or a delivered physical tap is not proof that this exact widget/listener path matched.

On an ordinary accepted row it highlights/updates UI_DI_TKB_TXT/UI_DI_SEL_COLOR and playsFX_D_NORMAL. Then it reads the selected dialog-info **next-ID vector+5c/+60 at8f13e6**. If nonempty it passes a one-element vector containing its first next ID to **SpawnNext G8edf70 at8f1412**. If empty it uses the selected info's+4 fallback ID and calls SpawnNext at8f143c. These are local narrative/controller transitions; no invented Episode network route is needed to make a choice advance.

## Conditional Episode gate: tuple4/2 requires actual n_02_03 achievement

The selected info fields+4/+8 are compared to **(4,2) at8f1346/8f134c**. Only that tuple diverts to8f14f2 and calls **GetStageAchieveCnt(TU_TYPE35) at8f14fc**. Nonzero resumes normal selection; zero builds a localized requirement notice instead of advancing.

The requirement stage is positively resolved: GameStage.GetStageData(TU_TYPE)84e8f0 calls StaticData.GetStageIDf42820; TBBindex35 atf4282e selects **armf428d0**, whose LDRf428d0/ADDf428d2 resolves **n_02_03**. This is an actual Glacier stage prerequisite, not a guessed Episode team-level threshold. It must be earned through real progression; no manual achievement/tutorial clear is justified.

This is not proof every Mission caption maps to tuple4/2. The actual selected node's pair must be recovered from the rendered conversation/listener state before attributing the parent's2 unchanged touches to that gate. A notice popup/control response would provide stronger evidence that OnButtonClick ran than unchanged pixels alone.

## Generic press gates and pending-animation vectors

**OnProcessCursorPress G8f1af4**, retained decompile, forwards the original UI input first and distinguishes script/video/talk handling. If script playback is not ended and no video is playing, it tries SkipScript. The generic tap-to-advance branch then requires previous press-state byte **player+109==1**, scroll offset magnitude<=1, elapsed deadline assembled from **uint64 fields+4f8,+500,+508**, and all3 pending begin/end pairs empty:

```text
4c8 ==4cc
4d4 ==4d8
4e0 ==4e4
```

It additionally requires active talk vector4bc!=4c0, a nonnull first info, and **!selection-type**. Selection detection recognizes **UI_DI_SEL_HEAD/BODY/TAIL** (IsTalkBoxTypeSelection8f1a84). Thus generic taps intentionally do not advance a choice layout; they depend on the BT_SEL listener. The pending-vector/timer conditions are evidence for ordinary dialogue advance and must not be incorrectly presented as all checked by OnButtonClick's choice branch. Their exact element types/timer units were not rederived here; output counts/raw deadline state, not invented actor/animation semantics.

## Geometry and NPC forwarding

**GetSelectionBoxArea G8f2318** checks the requested index against active4bc/4c0 vector size, gets that wrapper's drawable, finds **BT_SEL** (LDR8f236a/ADD8f236c), gets its rectangle by virtual+90 and **subtracts scrollY from both Y bounds**. Missing index/drawable/button returns a zero rectangle. A screenshot text location or unadjusted widget rectangle can therefore disagree with the actual selector area.

**NPC scene.OnProcessCursorPress Gec751c** forwards to its DlgPlayer atNPC+6d8 (virtual+40), as well as NPC overlay components when no video is playing, then calls FramedScene processing and ORs their results. This is a positive input-forwarding path, not proof the live Mission widget's listener is bound or accepted. Current input/modal/overlay state still matters.

## Minimal next evidence, kept finite

Parent targets to close actual choice selection:

```text
DlgPlayer.OnButtonClick8f1214
DlgPlayer.MakeTalkBox8ed03c (BT_SEL listener binding)
DlgPlayer.GetActiveTalk8f0dcc / IsTalkBoxTypeSelection8f1a84
DlgPlayer.SpawnNext8edf70
NPC.OnButtonClickec6ff4 (only if top overlay intercepts)
```

The minimal native observation is actual active talk count/first selection type, selected dialog-info tuple and next-ID count, script/video/previous-press state, pending vector counts, scroll state/offset, and adjusted BT_SEL rectangle. Use bounded read-only inspection with exact class guards; no C++ handler call, account dialogue text dump, flag write or direct SceneGoto. If tuple4/2 plus n_02_03 achievement0 is measured, the real prerequisite—not a listener patch—is the appropriate next progression seam. If no BT_SEL callback occurs, trace the original widget binding/hit path. If the callback and gate pass but SpawnNext does not, inspect its exact selected next-ID dependency.

No cause is selected from the2 unchanged Mission touches alone. Cruise control outcome, actual choice callback execution and listener/geometry state remain parent/tester evidence, not claimed here.
