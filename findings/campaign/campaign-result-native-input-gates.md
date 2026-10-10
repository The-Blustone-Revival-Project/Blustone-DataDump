# Campaign result input gates and ordinary Back route

2026-10-09. Original version28010 native source plus host observer. This corrects
the assumption that a visible WIN popup's Back handler necessarily receives Android
Back. No live result input acceptance is proved here.

## Wrapper cursor/button admission

CSRPopUpGameResult constructor Gc3e0bc initializes byte+a0 to0 and child+a4 to0.
OnProcessCursorPress Gc40962 reads child+a4 and calls child virtual+40 ONLY when
child exists and wrapper+a0 equals1. It always continues through PopUpBase's own
view dispatch afterward. OnButtonClick Gc4092e likewise forwards child virtual+54
only when+a0 is1. Exact instructions are retained; no semantic name for the flag
is inferred beyond these proven gates.

Wrapper OnMotionEvent Gc414bc checks matching end event/highword0. With a child,
when+a0 is0 it plays FX_RESULT_2 and writes+a0=1 atGc41630; when already admitted,
it invokes child virtual+4c. The wrapper has other animation branches; visible
Victory/Next text is not proof that this end event ran. SetData Gc3eb78 has a
conditional game-kind0x14 path setting+a0=1; the meaning of that kind/path is not
closed and is not generalized to every campaign result.

Constructor relocation proves wrapper primary G216c124 (ELF215c124): word at
Gc3e434=157faf6 +PCc3e102→pointer21bdbf8→vtable216c11c +8. WIN primary G216c3dc
(ELF215c3dc): c4244c=157ba06 +PCc42202→21bdc08→216c3d4 +8. WIN slot+38 atG216c414
is oddThumbc491e3 (Back); slot+40 atG216c41c isc49875 (CursorPress).

## Ordinary Back is a game pause route

Java audit documents key4 DOWN/UP enqueue. CSRSceneGame.OnProcessKeyInput Ge3d278
first calls game atscene+658 virtual+18. On release (r3=0) key4 (r2=4), it then
calls game virtual+30 and returns1; it does not call CSRFramedScene.OnProcessKeyInput
on this release branch. Ordinary CSRMStage primary G2163f84 is already proven by
native-live-state-reader.md. Slot+18 G2163f9c is9db1b9: CSRGameBase.ProcessKeyInput
is exactly MOVS r0,0/BX LR. Slot+30 G2163fb4 is9dc563: CSRGameBase.OnPause.

OnPause G9dc562 returns if game+140 lowbit is set; otherwise it invokes virtual+70.
CSRMStage+70 atG2163ff4 isb35651 (PopUpPause). Thus ordinary key4 release is not a
reliable way to invoke the WIN popup's cancellation method. No live key-trial pause
bit or field state was captured, so that bit cannot be assigned as the particular
cause of the failed trial. The key-DOWN framed-scene path and any dispatch before
this scene method remain separate targets; this does not prove that the WIN handler
cannot receive a key by any other path. Generic CSRScene key4-release dispatch also has byte+2c
==1 gate, but that generic route is not the ordinary release branch above.

## Read-only diagnostic and validation limits

InspectNativeInput now supports `8701 --result-ui --frame`. It uses the proven
modal singleton/list ownership, caps counts32, and reads+a0/+2c only for the exact
wrapper type. Child fields are admitted only for the exact WIN type with matching
Back/Cursor virtual slots. Flags must be0/1. Holder/control vptr/list/top/child/flags
are rechecked before printing. All reads use bounded mapped memory; no getters,
marker writes, native game calls, input or lazy initialization are added. One render
breakpoint with count1 and finally resume/dispose remains the mechanism.

Compilation and independent review passed. Three safe Village samples report no modal
and no result fields read; saved gameStates remain unchanged. This validates absent
result handling and safe resume, NOT the positive wrapper/child branch or touch
acceptance. Temporal rechecks do not exclude every native race/ABA change.

Next: after a properly controlled campaign WIN, sample the wrapper gate and child
before one result-only touch, then correlate cancellation with native markers and
lack of a subsequent Start. Keep the pending8-unit auto-arm limit from §206 in scope.
No active battle probe or direct invocation/flag override is proposed.
