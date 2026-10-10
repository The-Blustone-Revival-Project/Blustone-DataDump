# AE manual selection routes to ordinary AA detail

2026-10-04. Existing valid Gym decomp and read-only original ELF Thumb/vtable inspection. No source/client/runtime/Ghidra/adb edits.

## Exact observed route explained

Parent observed actual AE primary vptr ELF21772c0, then manual target5 click opens ordinary detail ELF216cbd8 rather than TutorialCardDetail ELF2176498. Original `_ZTV30CSRSceneTutorialLevelUpCardSel` ELF21772b8,sizeE8 proves inherited handlers: vtableoffset94 contains ThumbGfd6a70 TableCardList::OnTableViewButtonClick; secondaryoffsetD4 contains Gfd6f38 inherited thunk. There is no tutorial-specific manual handler override here.

The inherited handler reads selected cell's owned card instance, calls PutSelectedInstCard atGfd6c84, then **unconditionally** loads TYPEAA atGfd6c8a and calls PushSceneFadeOutIn Gfd6c98. No marker6 or tutorial state remap protects that ordinary click. Thus manual selection from AE naturally opens AA; the class/vptr observation does not require a Skip-caused defect.

## Genuine A9 action currently proved

TutorialCardSel OnInit only starts TutorialTraining when local marker==3. Its guided focus/touch/finger action eventually invokes **Geed6c0**, sets marker4, sorts all owned instances by registration date and automatically picks the first, then pushes **TYPEA9**. This differs from an ordinary manual click and cannot be replaced by assumed target5. Marker6 NPC continuation enters AE unchanged and does not start this marker3 guide at AE OnInit.

Do not force marker3, directly jump toA9, or invoke its callback. Only actual original guided input can establish this transition. Native intro Skip causation has not been recovered: no controlledbefore/afterSkip state evidence or exact Skipcallback is supplied. The inheritedclick is sufficient explanation for presentroute, not proof thatSkipneverchangesguidephase.

## Remaining rank-guide entry question

A9 is the proven first Raise guide path. Whether original marker6 rank guide intends a different continuation after ordinaryAA is still unknown. Ordinary CardDetail OnSelectedTrainingButton Gdcd5a0 has input-kind branches toTYPEB3/B6/A6 and no direct tutorial GetState call in its small body; target-kind and caller selection need fulldecomp before attributing those outputs. MissingMAX may independentlypreventadvanceavailability evenifrouteisordinary.

Smallest parent targets: **Gfd6a70..fd6c98** inherited click corroboration; **TutorialCardSel OnKillAll Geec770** and actual tutorial Skiphandler if causal question remains; **ordinary CardDetail OnInit Gdcc75c** and **OnSelectedTrainingButton Gdcd5a0** plus caller to pin normal-vs-rank-guide buttonmapping. Existing TutorialCardDetail SetTutorialRankUp Gee6834/RankUp2 Gee6924 are already exact symbolicguideentrytargets. No new material/flag action is proposed.

Parent's ordinary five-source Raise130→630/LV7 consumingonly7..11 remains a verified separateprogressionmilestone; this route investigation does not retract that success or label it tutorial8/1completion.

## Ordinary training-button outputs map to ordinary tables

Original ApplyScene table mapping and retained constructor calls:

- TYPEB3 → armGeab2d8 → CSRTableLevelUp ctorGeb3318 atGeab2e4; primary vptr ELF218278c.
- TYPEB6 → armGeab544 → CSRTableRankUp ctorGeb3598 atGeab550; primary vptr ELF2183b08.
- TYPEA6 → armGeac620 → AwakeLevelUp make_sharedGebe3cc atGeac6cc; primary vptr ELF21563e0.
- TutorialRankUp primary ELF217a824 is a distinct class and is not one of those output types.

OnSelectedTrainingButton Gdcd5a0 reads mode from detail+0x65c, subtracts1, TBB bytes atGdcd5be are [3,14,3,25,42]. Exact modes1/3 choose ordinary RaiseB3; mode2 chooses ordinary RankUpB6; mode4 chooses AwakeA6; mode5 emits toast. No tutorial marker/state remap is present in this small handler. Therefore reaching ordinaryRankUpbutton alone does not open TutorialRankUp through these outputs.

The caller's level/rank/awake→mode assignment is not fully recovered by this pass. Parent minimal dump **SetTrainingButton Gdd26bc..Gdd2b68 (size0x4ac)** plus its caller is required to pin exactMAX→mode2 condition. The existing server/native MAX requirement remains separate evidence; do not substitute that for the uninspected mode-selection arithmetic. No nativeflags/input/source modifications made.
