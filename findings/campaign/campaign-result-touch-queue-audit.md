# Campaign result touch queue: retained source audit

2026-10-09. Read-only audit of existing curated exports, original Java and shell
helper source. No ADB, UI, Ghidra, server, APK or game-state changes. G addresses
below are the relocated project addresses, not direct runtime addresses.

## A short injected contact is not proof of native coalescing

`tools/RapidTouch.java` injects Android DOWN through InputManager mode0 (async),
sleeps5ms, and attempts UP with the same downTime even after a DOWN failure. Each
success log proves only Android injection acceptance. It does not wait for the
Activity, JNI, native queue or popup consumer. The 5ms is requested sleep, not a
measured native processing interval. Its coordinate admission is restricted to
x400..750/y700..1050; this helper must not be repurposed for a result X coordinate
outside that range without an independently reviewed input contract.

Original Java maps each Android pointer ID to pointerID+1 and sends DOWN to
TouchesBegan, UP/CANCEL to TouchesEnded. Its initialized/running gate and possible
Android child-view interception remain upstream conditions. Telemetry at
dispatchTouchEvent precedes these conditions and cannot prove native delivery.

The retained `ghidra-skill-jni-touch-coordinates.txt` shows JNI Began G11035d0
allocates an unused slot among ten pointer-ID entries, rejects a duplicate active
ID, and passes converted coordinates, press1 and that slot to `_HandleTouch`.
Ended G11037dc looks up the matching slot, sends press0, then clears the JNI ID
entry. Unknown IDs do not obtain an Ended dispatch. Decompiled register temporaries
in the unrolled Began search are artifacts; do not treat them as extra timing gates.

`CRMApp::HandleTouch` G10bef2c does more than overwrite a latest-contact array.
With its engine pointer present, it stores per-slot coordinates/state/time/slot
and separately copies a 0x14-byte record into a ConcurrentQueue at app+1f8. Record
fields are x+0, y+4, state+8, native time+c and slot+10. Per-slot storage starts
app+12c with stride14, placing state134/time138/slot13c for slot0. Time comes from
RMGetInternalTime; this export does not establish its unit or permit conversion
to Android milliseconds.

For press1, previous state1 or2 and identical coordinates return early; changed
coordinates produce state2. A new contact produces state1. Press0 produces state0
and is not eliminated by that identical-coordinate check. Thus a normal admitted
DOWN then UP can enqueue two distinct snapshots even inside one render interval.
The retained producer code does have early returns for unavailable producer/block
or allocation failure. No evidence ties those branches to the live failed trials.
Dequeue ordering, draining limits, state reduction and downstream dispatch remain
unclosed; do not claim that every queued press is delivered either.

The guarded200ms skill attempt in `tools/attack-battle-visual.ps1` uses a same-point
Android swipe. Its contract bounds hold50..250ms and requires visible skill guard.
Observed Karl acceptance does not isolate duration as the cause: eligibility,
hit rectangle, callback timing and contact path differed or were not all observed.
It is not proof that RapidTouch's5ms contacts are universally dropped, nor proof a
held result contact will cancel automatic continuation.

## Geometry and pre-queue interception

`_HandleTouch` G10f4ac8 first tests an open CRMWebView and can return for a point
inside its rectangle. Otherwise it forwards to the current CRMApp if present.
This is a concrete possible interception boundary, not proof a WebView existed
over the observed WIN screens.

JNI uses Renderer.GetLogicalPos G10e0528. Original Java also adjusts physical
coordinates according to SDK/layout flags before JNI. Live renderer-layout-001
calibrated SDK25, translation0, inactive stored36px inset, logical651x1135 and
physical1080x1884 for that historical session. Two safe-menu points matched the
reconstructed conversion. Those observations do not establish current WIN
geometry, popup ownership or a universal36px offset. Result wrapper+a0 gate1,
child identity and hit-test dispatch must be sampled independently; visible text
and Android injection success are insufficient.

## No proven Android global touch switch

The symbol index contains RMSetTouchEventOn G1101e10. The exact native string
corpus contains `[FWK] RMSetTouchEventOn does't support on Android` at string
offset01d9c01a. This gives a strong reason to inspect its original body before
using its name as evidence of a functional global touch-disable flag. The string
alone does not prove the function is a no-op, which branch logs it, or whether
another application/scene switch exists. No retained result-X trial establishes
global disabling, and the wrapper+a0 gate is a separate, proven local admission
condition. Do not override either field or invoke the named function to test it.

## Narrow next native exports

The following candidates have exact named entries in native-evidence.tsv:

- CRMApp.GenerateInputEvent G10bea44: close queue dequeue and state-to-cursor
  event conversion, including any skipped or merged contacts.
- CRMApp.ResetInputBuffer G10bcfa0: identify explicit flushing and callers.
- CRMApp.OccurCursorPress G10bee20 and OccurCursorMove G10bee0e: close dispatcher
  ownership and timing arguments into popup/scene consumers.
- RMTOUCHINPUT ProducerBase.dequeue G10bf130: close record copying only if the
  GenerateInputEvent export needs the queue implementation.
- RMSetTouchEventOn G1101e10: body and exact caller references, distinguishing
  unsupported Android behavior from any independently named global gate.

Evidence used: ghidra-skill-app-touch-state.txt,
ghidra-skill-touch-dispatch-scroll-owner.txt,
ghidra-skill-jni-touch-coordinates.txt, native-evidence.tsv,
native-all-strings.tsv, campaign-result-java-input-audit.md,
campaign-result-native-input-gates.md, skill-native-hit-rectangle-contract.md,
testing/renderer-layout-001/report.md, tools/RapidTouch.java and
tools/attack-battle-visual.ps1. Result cancellation and durable marker removal
remain live-validation tasks; this audit supplies no new cancellation claim.

## Fresh original exports close queue consumption and local suppression

Root's subsequent read-only exports supersede the earlier unclosed-body items
above. RMSetTouchEventOn G1101e10 has only literal load, severity1 and a tail
branch to RMTrace; exact resolved text is the Android-unsupported message. Its
input argument is overwritten, with no touch-state store. This function is a
trace-only no-op in the recovered Android binary. That closes this particular
name, not every possible input gate in the application.

GenerateInputEvent G10bea44 consumes the touch queue. State2 dispatches app
virtual+2c (move); other states dispatch virtual+28 (press), with a stack boolean
computed as state==1. The decompiler omits that fifth parameter; exact Thumb
SUBS/CLZ/LSRS/STR instructions prove it for both the pending and fresh-record
paths. In particular state0 releases and state1 presses remain distinct events.

After eleven freshly dispatched records, the twelfth dequeued record is deferred
when its timestamp differs from the preceding nonzero timestamp. Equal timestamps
can continue past eleven: this is not an unconditional eleven-event cap. The
dequeue target and pending record resolve to the same shared static storage;
the next GenerateInputEvent call dispatches that retained record first when its
time is nonzero, then clears that time. This is deferred delivery, not demonstrated
loss of a short DOWN/UP pair. Queue draining and multiple producer selection do
not prove a strict global order across different producer threads. Native timing
units and live queue backlog remain unobserved.

ResetInputBuffer G10bcfa0 drains key/touch queues and zeroes input arrays, including
app+12c for200bytes. It does not show a store to the shared deferred record in
this export; do not assume every pending record is cleared by that routine.

App OccurCursorPress G10bee20 dispatches to manager+14; move uses+18. CSRSceneMgr
ProcessCursorPress Geb4440 first records input through CMInputMgr. It then skips
modal/base-scene touch routing when fader IsEnd is0 AND manager+672 equals1, or
when current scene IsEnd returns1. Fader IsEnd reads fader+61b, corresponding to
manager+673 for its embedded fader at+58. Scene IsEnd Gdf4bec reads scene+38.
These are exact local route gates; recording into CMInputMgr is not proof the
popup received the press.

When admitted, modal ProcessCursorPress G1085996 first forwards to its embedded
post-effect scene at modal+20. It returns consumed1 without forwarding to the
primary popup when post-effect IsWaiting is1 or secondary-list count+18 is
nonzero. Otherwise a nonempty primary list forwards to top popup virtual+40 and
consumes it. PostEffect.IsWaiting Ged3772 is true when HTTP GetProgSize G7e7856
returns nonzero (HTTP+70), or embedded post-effect+6bc is nonzero; the latter is
modal+6dc. This closes two further local interception conditions, not a global
touch switch or their actual value at a past failed X touch.

Fresh evidence: ghidra-campaign-touch-switch-and-queue.txt, -switch-keys.txt,
-switch-instructions.txt, -dequeue-dispatch.txt, -dispatch-registers.txt,
-dispatch-press-registers.txt, -pending-registers.txt, -dispatch-literals.txt,
-scene-router.txt, -routing-gates.txt, ghidra-campaign-modal-touch-press-registers.txt
and ghidra-campaign-modal-posteffect-wait.txt. Native reset callers are separately
retained; no live reset attribution is made here.

## Read-only observer review

Reviewed Root's expanded InspectNativeInput.inspectResultUi. It qualifies exact
app and manager vptrs, rechecks their links, and reads sceneEnd only for the
explicit known Game/MStageMap/Village types. Unknown scene types retain -1 rather
than receiving a guessed+38 semantic. Router flags must be0/1. Existing borrowed
scene pair checks require a nonexpired control; it does not derive every possible
scene-control subtype or pin lifetime by native strong-reference operations.

The HTTP weak holder at ELF21ce890 is accepted only with nonnull raw/control,
exact default-delete control primary ELF213d448, nonnegative strong-owner-minus-one
counter and control+c equal raw. HTTP+70 and modal+6dc counts are bounded4096;
primary/secondary lists are bounded32. Pointer/type/count/flag values are repeated
before output. No native singleton getter, allocation, lazy initialization,
input call or state write is added. All accesses use the existing mapped bounded
memory reader. No blocking defect was found in these diagnostic additions.

Compilation is Root-reported, not rerun by this reviewer. Positive MStageMap/live
WIN routing snapshots remain Root's validation work. Stable snapshots do not
exclude every race/ABA change, prove injected-event traversal, or eliminate
conditions occurring between snapshot and touch. The HTTP ownership constants
require their retained original singleton/control provenance; merely matching a
generic shared-owner counter would not supply that proof.

## Root live map validation

Expanded host observer compiled and read-only DeepCavern map sample passed:
faderEnd1/blockDuringFade0/sceneEnd0 (ELFscene2172620), HTTPprog0/postEffectWait0,
modalPrimary0/secondary0. Raw evidence: testing/touch-routing-001/map-routing.txt.
All3 saved gameStates compare exactly equal across the invocation. This confirms
the added ownership/type/flag branch on the safe map, not a WIN routing sample
or injected-event acceptance. No native getter/function/flag call or UI input.
