# Empty Search guide lifecycle and limits of an entry deferral

2026-10-05. Read-only existing verified OnInit/Arrange/SetTutorial/entry-callback evidence and original ELF Thumb. Parent reports +11 live zero eligible virtual helpers, Partner scene byte+2c0, owned guide/focus active and hardwareBack unchanged. No VM/Ghidra/source/flags/grants/native calls were performed by this lane.

## Actual caller condition

The proved Thumb continuation **Ge30c98** locks its captured scene weak owner, requires nonnull scene and captured status1, calls **Arrange** and tableResize, reads **tuto_explore**, and invokes **SetTutorial Ge2ffe4 only when its numeric marker is8**. Fresh ghidra-search-tutorial-entry-callback.txt/-keys.txt supplies the exact attribution. This valid path contains no direct Partner+2c write/input setter before SetTutorial. Its invalid branch writes marker5 and SceneGoto9; that existing error escape is not a proposed recovery action and must not be repurposed.

Current helper-template/used-ID evidence makes the zero-eligible observation meaningful: SetTutorial requires group.type2 and THUMB.available1; it has no used-row fallback. The one-Lantern local fixture, already used with no active replay reservation, cannot meet that prerequisite. Guide-state/usage reset is not justified.

## What SetTutorial creates and replaces

SetTutorial allocates/constructs TutorialBase **before** the availability scan, initializes it, and writes scene+6ac/+6b0, replacing a prior shared owner if present. It then focuses the selected row and queues the popup through **ModalHandler.Push atGe304a2**. Its body has no early existing-guide-null guard and no ModalHandler.Pop/Close of an old guide.

Releasing the scene's previous shared control does **not** prove the old popup was removed from the handler: the modal handler can retain another shared owner. Conversely on a truly fresh scene with no existing modal, returning before the allocation avoids creating/queuing a new guide and leaves marker8 unchanged. Whether the actual current blocked scene still has an old queued/active guide is separate; +11's owned active focus is positive evidence that simply deferring a later invocation is not a full cleanup of that state.

Do not call PopAll or remove an unrelated top modal to hide this problem. A parent-owned future cleanup would need exact ownership/top identity and normal lifecycle evidence. No such cleanup was implemented here.

## Byte+2c is a navigation/input gate, not renderer activation

**CSRScene constructor Gdf48e8** initializes byte+2c to1 (STRB atdf494a). Generic **OnProcessBackKeydf4c90** only navigates when that byte equals1; **OnProcessKeyInputdf4d14** also checks it for keycode4/release0 before dispatching its virtual back handler. Thus the observed Partner+2c0 is a relevant blocked Back condition. **OnProcessHomeKeydf4ce8 itself does not check+2c**; if invoked it follows the ordinary SceneGoto9 path. Failure of a visible Home touch must therefore be traced upstream through focus/header dispatch, rather than falsely attributing a+2c check to that Home method. Invoking it directly is not a proposed escape.

However **Activate Gdf4c64** and **Deactivate Gdf4c7a** change **byte+39**, not+2c (storesdf4c70/df4c86). Therefore calling renderer Activate/Deactivate or equating modal deactivation with a proved+2c restore is incorrect. The exact writer that changed the live Partner+2c from its constructor default1 to0 is **not yet identified**. Direct inspected OnInit/validcaller/SetTutorial stores do not close all transitive UI/renderer/event paths. A no-eligible entry return cannot be claimed to restore ordinary Home/Back until that writer/restorer is recovered.

TutorialBase constructor independently sets **its own+2c0 atd8556a**. The modal's input byte and underlying Partner byte are separate fields; the reader currently observes only the scene-owned guide/focus chain, not an independently guarded ModalHandler.GetTop result.

## Modal Push/Pop does not directly restore Partner+2c

**ModalHandler.Push G1085bcc** stores/queues a shared popup in its pending list and updates a timestamp. **Refresh G108574c** later calls rendererPushBack at10857d2 and popupActivate at10857da. It detects ended popups, deactivates/removes them and releases owners. **Pop G1085d08** calls the popup's virtual close+4c at1085d8c, Deactivate at1085d90 and rendererRemoveSceneRef at1085da0. The inspected functions have no direct Partner+2c1 store. Transitive renderer/event effects remain unproved; no input-restoration guarantee follows from simply describing this as a push/pop stack.

**ModalHandler.OnProcessBackKey G1085e70** selects a pending/active top popup, checks **that popup's+2c==1 at1085ea0**, calls its virtual+38, and only pops if that virtual returns1 (1085eb4..1085eba). Otherwise it returns0 at1085ec2. TutorialBase's own back method **d85e4c** checks byte+9d; default/not1 returns0 without navigation atd85f22, while1 creates a pause popup. This gives concrete reasons an active tutorial can persist on Back, but final propagation through the application's main key dispatcher was not fully audited. Do not infer that every returned0 means consumed or forwarded.

FocusDraw's active+850 pointer separately makes cursor processing return1, so the measured owned active focus is consistent with background header touches being intercepted. Survival and unchanged UI do not prove the e37420 Home continuation guard executed.

## Bounded conclusion and next proof

An entry guard can safely **avoid allocation of a new empty-candidate guide** in the narrow function-body sense: zero-eligible return before prologue/allocation performs no guide/Target/flag writes. It does **not yet prove** ordinary navigation is available, existing guide ownership is absent, or a previously active popup is closed. Treat fresh-entry deferral and current blocked-scene cleanup as separate requirements.

Minimum parent decompile targets to close those gaps:

```text
CSRScene.OnProcessHomeKey df4ce8
CSRScene.OnProcessKeyInput df4d14
Partner.OnInit e2ae34 and valid continuatione30c98 (already retained)
SetTutorial e2ffe4 (already retained)
ModalHandler.Push1085bcc / Refresh108574c / Pop1085d08
ModalHandler.OnProcessBackKey1085e70
```

If those confirm no+2c writer, follow only their concrete renderer/event helper targets, especially popup/base initialization and input enable callbacks; avoid broad address or symbol-name guessing. A bounded snapshot of guarded top modal identity versus scene+6ac owner is the smallest live distinction, parent-owned. No flags, used IDs, grant, SceneGoto escape or direct input-byte write is proposed.

Any future narrowly scoped client guard still requires exact ABI/owner/null-row bounds tests, instrumented build and mandatory release. This report does not implement or certify that guard.
