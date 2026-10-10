# Ordinary campaign result input: Java bridge audit

2026-10-09. Read-only source audit; no adb, UI, Ghidra, APK rebuild or game-state writes. This audit explains the Java routing boundary. It does not prove which native result handler received the retained Back/X inputs.

## Back is queued to native; Android default Back is bypassed

The preserved game `com.vshower.sr.MainActivity` extends `RMFrameworkActivity` and does not override key or touch handling. JADX renames its package to `com.vshower.p028sr` (`analysis/jadx/sources/com/vshower/p028sr/MainActivity.java:17`). The compile-only `instrumentation/stubs/com/vshower/sr/MainActivity.java` is explicitly a stub, not evidence of the installed game's superclass behavior.

`RMFrameworkActivity.onKeyDown` and `onKeyUp` call `RMJNIMethod.EnqueKeyInput((char) keyCode, true/false)` only when both initialized and running flags are true. For key code 4 (Back), each then returns false without calling its `Activity` superclass handler. Therefore these methods do not use the normal superclass Back path to finish the Activity. Returning false does not undo the preceding native enqueue. It also does not prove a native scene consumes that key.

Evidence: `analysis/jadx/sources/com/vshower/rann/RMFrameworkActivity.java:661-673`; native declaration `RMJNIMethod.java:233`. The preserved extracted smali corroborates the key-code-4 branch, flag tests and `EnqueKeyInput(CZ)V`: `analysis/patched/debug-manifest/smali/com/vshower/rann/RMFrameworkActivity.smali:1737-1808`. This is corroborating extracted evidence, not a live verification of the installed dex.

The flags are original fields `t` (JADX `f21411t`, set true after framework initialization at line177) and `u` (`f21412u`, set true when the main thread starts at line774, false when it stops at line787). A captured Activity dispatch alone does not establish these flags at the instant of input.

## Touch telemetry precedes the downstream native boundary

`instrumentation/src/InstrumentedActivity.java:42-44` records `Telemetry.touch(this,event)` before returning `super.dispatchTouchEvent(event)`. It neither overrides key handlers nor records their result. `Telemetry.touch`, at `instrumentation/src/Telemetry.java:285-295`, records action, pointer count, default-pointer x/y and event time. It does not record downstream view consumption, native enqueue or result-handler acceptance.

The original Activity's `onTouchEvent` at `RMFrameworkActivity.java:714-740` uses the same initialized/running gate. When admitted, pointer identifiers are mapped to native IDs as `pointerId + 1`. DOWN/POINTER_DOWN call `TouchesBegan`; UP/POINTER_UP and CANCEL call `TouchesEnded`; MOVE iterates all pointers and calls `TouchesMoved`. It then returns the superclass touch result. CANCEL is not a distinct native cancel call on this bridge. A false returned superclass value is not proof that JNI was skipped.

The coordinate helper (`RMFrameworkActivity.java:339-357`) casts coordinates to integers. On Android API below29 or when `f21400F` is true, it uses indexed local x/y with GL-view translation, navigation-bar and status-bar adjustments. Otherwise it uses indexed raw x/y. Consequently the instrumentation's default `getX()/getY()` fields are not universally identical to the values passed to JNI. No screenshot-derived native coordinate mapping is asserted here.

The GL surface class (`analysis/jadx/sources/com/vshower/rann/C3159b.java`) has no custom touch/key override in the recovered source. This does not exclude another Android child view or dialog consuming an event before Activity.onTouchEvent. In particular, the edit-box `onKeyPreIme` consumes Back-UP to hide editing (`RMEditBox.java:190-195`), and the framework native-message dialog's Java listener consumes Back-UP as dialog result2 (`RMFrameworkActivity.java:320-326`). These are explicit alternate Java paths; neither is established as present during the campaign result trials.

## What the failed cancellation trial proves

`analysis/testing/campaign-receipt-001/receipt-audit.md:32` retains result Back after Complete36 and result X after Complete37, followed by Start37/38. That proves those actions did not durably stop this observed automatic sequence. It does not choose among native timing, scene routing, hit-test rejection, key gating or Android interception.

The current wrapper contains no key telemetry, and touch telemetry is upstream of native dispatch. A next read-only audit should correlate the original JNI key queue, native scene key dispatch, result input gates and the delayed continuation callback. For X, inspect actual native hit-test ownership and activation, including DOWN/UP and modal state. Do not infer result-screen native bounds from Android coordinates alone, alter the APK merely to assume delivery, or treat shell injection success as result acceptance.
