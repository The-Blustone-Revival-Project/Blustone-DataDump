# Search Partner Home crash: exact tutorial continuation ownership

2026-10-05. Read-only original ELF Thumb/RTTI, existing Search partner dump and validated scene-pointer evidence. No Ghidra, VM, source edits or client patch. Parent reports a null SetVisible call after Home leaves Search Partner; runtime scene/row fields were not read by this lane.

## Exact callback identity

The function at **Ge37420 / ELFe27420** is selected by function-object vtable **ELF216f578**. Its invoke slot+20 contains ELFe27421. The original RTTI explicitly names:

```text
CSRSceneFindShardSelSupporter::SetTutorial::$_15::operator() nested lambda
```

This is positive closure ownership, not nearest-symbol inference. It is a pending tutorial helper-selection continuation, not a server response parser or global visibility function.

It reads a **raw captured scene pointer atfunction-object+40 at e37440**, and a captured row-name string at+0c. Its copy helper e377ac copies the raw scene member athelper+38 (function-object lambda storage offset8) with plain load/store e37804/e37806, **no shared-control retain or weak lock**. The captured shared pointer atfunction-object+18/+1c is the helper card, not a lifetime lock for that raw scene. The invoking entry also performs no scene weak-lock before dereferencing it. Consequently Home can expose stale scene/lifetime concerns as well as a missing row child.

## Exact failed lookup and dangerous fallthrough

At e37446 it calls FramedScene.FindCastByName<CMDrawable>(capturedScene,capturedRowName), putting the parent pointer atsp+0. It reads it at e3744a. It then resolves literal **SET_CK** (LDRe3744c/ADDe3744e), constructs CMHashID and searches beneath parent+4 at e3745c. Neither parent nor child result has a null guard.

After releasing the first lookup's shared control, it loads the child pointer atsp+8 e3749a and unconditionally calls **CMUpdatable.SetVisible(child,1) at e3749e**. A null child explains the reported call-level crash. It does not prove that static SET_CK XML is missing: the captured parent/scene may be stale, detached or no longer the selected row. A null parent also has an earlier unsafe parent+4 search path.

Critically, code after visibility changes **the CURRENT global Search Target**, not just captured scene visuals:

```text
Target.helper card +44/+48 <- captured card      e374c6/e374ca
Target count byte +40     <- captured value     e37534
Target virtual helper ID +58 <- captured string e3758e
Target friend PVID +50    <- captured uint64    e375d2
```

It then accesses capturedScene+6ac tutorial popup and calls FocusDraw.Disappear at e3762c with another guide continuation. Therefore a global nil SetVisible shim or skipping only the visibility call and falling through can still overwrite a newer Target with stale helper data and continue the wrong guide. No tutorial flag clear, fabricated grant or scene jump is justified.

## Exact current-scene identity comparison

Use the already validated native ownership chain, not a fabricated getter ABI:

```text
app = *(loadBias+ELF21ef1e0)       // g_pApp
manager = *(app+8)
currentScene = *(manager+34)
capturedScene = *(functionObject+40)
```

CSRApp.Init stores manager atapp+8 (858b48); CSRSceneMgr.RefreshAll reads currentScene+34 at eb1fcc; MoveScene reads it at eb2186; ApplyScene owns pair+34/+38. No separate exported GetCurrentScene getter was found in the retained catalog. Manager+44 is scene TYPE history, not a scene pointer.

**CSRSceneFindShardSelSupporter primary vptr is loadBias+ELF216f2ec** (_ZTV216f2e4+8). Pointer comparison does not require an invented base adjustment: original **shared_ptr<CSRScene> constructor from CSRSceneFindShardSelSupporter Gec15f4** stores the supplied pointer unchanged at ec1600. The secondary listener thunk uses a separate1620-byte adjustment; it must not be accepted as the primary scene pointer.

Compare the captured raw value against the guarded currentScene value **before dereferencing capturedScene**. A different current scene is sufficient to classify this continuation as stale for its scene-specific UI work. Matching pointer/vptr alone does not freeze lifetime or prevent an ABA reuse race; retain the bounded-observer limits already documented. No in-process C++ getter call is needed to perform this identity guard.

## Safe guard boundaries for parent implementation

An entry guard **before any original prologue instruction** may return from this void callback with BXLR when the capture no longer names the current scene, provided the shim preserves all callee-saved registers and incoming stack/LR. It has no constructed local objects to destroy at that point. **Do not jump to the original epilogue from before its prologue**, because the original function has already assumed a48-byte local area plus32 bytes of saved registers and initialized stack-canary storage. Any relocated-prologue trampoline needs its own exact ABI verification; no patch was created here.

For **child-null after e3749a**, the first parent shared-control result has already been released and the second child result has a constructed pair atsp+8/+0c. A conditional abort can follow the original **cleanup entry e3766e**, which releases child control atsp+0c, checks the canary at e3769a and restores the frame at e376a4..aa. This abort skips every Target write and guide continuation.

For **parent-null at e3744a**, the child lookup/pair has not been constructed and sp+0c is uninitialized. It cannot safely jump to the child-cleanup path without explicitly initializing the second pair and releasing any first-result control correctly. Treat that as a separate cleanup branch; do not read an uninitialized control pointer or pretend both null conditions share identical lifetime state.

A whole-continuation abort preserves guide progress rather than declaring it completed. An actual current scene with a missing row/SET_CK still requires resource/row lifecycle diagnosis and a normal UI retry; the defensive guard is not proof the underlying layout is fixed. Static XML absence and stale-scene causality remain separate until a bounded live scene/lookup observation distinguishes them.

## Independent candidate patch audit: initial static blocker

Read-only inspection of search-callback-guard.S, patch-native-search-callback.py and **libnative_core-search-guard-candidate.so SHA256f104408371053e366d1d892627b28e2bfdd29288f346ce16b7e69ebc6f49075f** found a **blocking PIC target error** in the initial candidate:

```text
near entry:  612ca0+4+u32[612ca4] =210d381  correct Thumb entry
near parent: 612cac+4+u32[612cb0] =210d3be  WRONG even pointer
near child:  612cb8+4+u32[612cbc] =210d3e6  WRONG even pointer
```

Actual cave instruction starts are guard_parent210d3bc and guard_child210d3e4; expected Thumb pointers are210d3bd and210d3e5. BX through the observed even pointers would switch to ARM and enter the wrong+2 address. Source cross-section expressions involving .thumb_func labels plus an explicit+1 need correction and **verification against final emitted bytes**, not confidence from llvm-nm's printed normalized symbols. Parent was notified to stop builder/release promotion pending correction. No implementation was changed by this audit.

Other emitted target literals checked correctly: entry replay e27425, parent replay e2745b, parent-null cleanup e27461, child replay e2749f, child-null cleanup e2766f; APP delta resolvesELF21ef1e0. Original4-byte hooks replay expected push/add, adds/add and ldr/movs on valid paths. Entry saves24 bytes of volatile regs/LR, restores before original push/add; stale path restores and BXLR without an original frame. Parent-null initializes sp+8/+0c then reuses hash destruction/first-result cleanup at e27460, reaching the child guard; child-null goes directly to e2766e and skips helper/Target/guide writes.

The near blob occupies612c9c..612cc0, beginning immediately after the occupied Gym12-byte trampoline612c90..612c9c. The candidate RX segment ends210d404 and remains within the original final mapping page; RW file offset210d550/VA210e550 remain unchanged. Patcher guards original hook bytes, zero cave/near spans, section/load overlaps and incoming branch targets. The source also changes only copy destinations, refusing the extracted original. These static checks do not compensate for the two wrong emitted BX targets and do not constitute a native or emulator PASS.

Scene identity equality uses the proved app→manager→currentScene chain before captured-scene dereference, but does not independently check app/manager/scene vptrs or freeze ownership. It suppresses an ordinary stale pointer after Home; ABA reuse/lifetime races remain bounded limitations. After fixing PIC targets, verify stale/null-app/null-manager/null-current, missing-parent/missing-child and valid branches under ASLR in an offline ABI test before native promotion. No VM/native execution was performed by this review lane.

## Corrected V2 and offline execution resolution

The initial-candidate BX error above was corrected before any APK build. V2 SHA
314df992afc1535e7608c44b75954cbf19c9a2999b1470d1636a2e9cc684ff34 has exactodd
entry210d381,parent210d3bd,child210d3e5 targets. Independent review verified all
PIC destinations and preserved Gym bytes. Ten Unicorn emitted-code paths passed
scene identities, stack/register/cookie and parent/child cleanup/valid replay.
The hard gate rejects the initial candidate. Published +10 carries V2; native
Home acceptance remains pending in episode-002. No broad guide bypass was added.
