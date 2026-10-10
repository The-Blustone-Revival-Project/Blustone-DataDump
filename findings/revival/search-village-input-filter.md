# Search guide and Village input filtering

2026-10-05. Read-only original ELF Thumb, curated ghidra-gym-village-training-entry.txt and village-ui-live-root.md. No Ghidra, adb, source changes or marker writes. Parent observes Home returning to an undimmed Village with a central hand; Supply and an Airport tap produce neither HTTP nor a scene transition. No runtime modal/marker snapshot was obtained by this lane.

## A Search-specific restriction exists

Village has no exported ProcessTutorial method. The actual methods are ResumeTutorials Gda0408, SetTutorials Gda0ccc, TutorialBegin Gda19f0 and SetTutorialExploreCardPiece Gdba26c. Do not attribute this to an imagined ProcessTutorial symbol.

ResumeTutorials checks GetState(37,0) atda08ba and GetState(37,1) atda08fc. When step0 is at least2 but step1 is below2, it enters da0904 and reads the local tuto_explore marker. Its curated decompile shows that a nonzero numeric marker is preserved; a zero/missing marker receives value2. This can recreate a legitimate Village Search entrance guide after an acknowledged intro while guided recruitment remains unfinished. Step37/1 pending alone does not prove a modal is currently installed.

SetTutorials reads tuto_explore atda0dd2/ADDda0dd8. Its marker2 branch calls TutorialBegin atda1096, then schedules a task atda10b8. Original callback vtable ELF216b46c invokes Gdbbc5e. That closure SwitchSide(0,1) atdbbc6a and tail-calls SetTutorialExploreCardPiece atdbbc74. This is an actual route to the Search tutorial, rather than proximity-based symbol attribution.

TutorialBegin sets Village byte+2c to0 atda1a08, creates CSRPopUpTutorialBase, stores its shared pointer atVillage+928/control+92c, initializes it and pushes it into CSRUIModalHandler atda1a96. TutorialEnd Gdba674 restores byte+2c to1 atdba67a and calls the tutorial popup's virtual close operation. An undimmed background is therefore not evidence that no tutorial modal is present.

## Exact target: BT_RD

SetTutorialExploreCardPiece calls SetNameTagVisible(button3,true) atdba28c and starts a nested focus/message sequence. Original callback chain:

```text
dba26c -> dca028 (guide message)
       -> dca27c (WaitForTouchInput atdca2a4)
       -> dca354 (message disappears)
       -> dca4a0 (target circle)
       -> dca724 (AddButtonClickCB atdca766)
       -> dca870 (focus disappears)
       -> dca9bc (normal Search scene transition)
```

The target drawable is **BT_RD**: LDRdca4c0, literal slotdca6b8, ADDdca4c2 resolves the original string atELF1d77d87. FindCastByName runs atdca4ce; virtual+90 obtains its actual rectangle atdca4da. The guide uses that rectangle's center atdca53e and half its width atdca54a, passed to FocusDraw.SetCircle atdca558. Screen coordinates or the English label cannot substitute for this actual rectangle. Supply and Airport are not the recovered target of this guide.

The final callback requests Clear37/0 atdcaa16, sets local tuto_explore to3 atdcaa5a, then PushSceneFadeOutIn(TYPE b9hex) atdcaa88. It does **not** clear37/1. RequestClear's already-cleared short circuit means an actual successful guide touch can transition without emitting another Clear37/0 HTTP packet. Thus no HTTP alone cannot establish whether a touch was ignored; the scene change also matters.

## Input interception versus bad coordinates

FocusDraw.OnProcessCursorPress G1079f52 checks active object+850. If nonnull, it dispatches its cursor event pool when present and **returns1 at1079f7e**, even if the pool is empty. If null it returns0 at1079f84. This supplies a concrete input interception path independent of background dimming. FocusDraw.OnButtonClick G1079f08 invokes its installed callback only when callback storage+8c4 is nonnull, hides the active object and dispatches the callback pool.

TutorialBase.OnProcessCursorPress Gd85fac also routes through its focus/message objects and pending touch callback/list before falling back to PopUpBase. The original fields and conditions are explicit, but this report does not claim the parent is currently in that exact callback state. A central hand may instead come from the separate ModalHandler finger indicator, which is not automatically the BT_RD circle described above.

Village.OnButtonClick Gdac918 is the ordinary action dispatcher. Its opening code tests actual drawable rectangles against the last Village cursor point before processing clicked controls; no blanket GetState(37,1) refusal was recovered at that entry. The modal/focus route can intercept input before this dispatcher, so failed background taps cannot establish a server route defect.

## Bounded next discrimination

Use the existing read-only Village root proof: manager+34 current scene, Village primary vptr ELF216b1c4, view+98, CMUIView root+8. Inspect the actual BT_RD node's visible state and ancestor transforms/rectangle through already validated bounded tools; observe the top modal and Village+928 owner if the parent's reader supports those exact guards. Do not invoke C++ methods or write byte+2c/markers. A screenshot showing the real highlighted target and normal press/release is useful before further guessed Airport coordinates.

If the exact tutorial popup/focus is active and BT_RD is the target, advance the shown guide through its normal touch and highlighted control; expected transition is Search TYPEb9, with possible no repeated HTTP. If no relevant modal is active, the same symptom remains inconclusive and requires actual hit rectangles/visibility rather than inferred tutorial clearing. Parent can obtain narrower decompile evidence at dca4a0, dca724, dca9bc, TutorialBase.d85fac, and FocusDraw.1079f52 if further callback/hit filtering is needed.

No broad tutorial clear, manual marker modification, forced visibility, direct scene jump or extra grant follows from these observations.
