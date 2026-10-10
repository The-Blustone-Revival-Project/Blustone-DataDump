# Ordinary campaign WIN result cancellation contract

Source-only review, 2026-10-09. No ADB, live input, APK change or Ghidra project access was performed by this reviewer. Root generated the curated exports while this review ran.

The relevant operation is `CSRPopUpGameResultWin::EnableAutoProgress(0)` at G `c49214`, rather than `StopAutoPlay` alone. Its false branch removes the **MissionAutoPlay** marker, hides **PA_AUTO_FADE**, finds the **auto_next** animation component and stops it. Relocated literal identities are recorded in `analysis/ghidra-campaign-result-enable-keys.txt`; the body is in `analysis/ghidra-campaign-result-auto.txt`.

WIN `OnProcessCursorPress` at G `c49874` invokes that false branch before forwarding cursor handling to the base result popup. This establishes a possible result-only cancellation path through normal input, without choosing a navigation button. It does not establish a working screen coordinate, that an arbitrary outside-popup touch reaches this method, or the precise accepted cursor phase. The decompiler mis-types the receiver as an unsigned integer and shows a spurious float return assignment; the call and constant zero are the evidence, not that inferred float signature.

**Timing correction: an early press is not proven to stop continuation durably.** WIN `OnMotionEvent` G `c49b30` handles **enable_auto**, reads **mission_auto/is_first_clear**, requires the converted low byte equal 1, then schedules `CMTaskStream::OnceImpl`. The registration instructions explicitly pass float bits `41000000`, or **8 native clock units**. `OnceImpl` G `76bfc8` adds this value to the native lifetime/task clock; do not substitute an unverified wall-clock delay.

The callable primary `216c6d8`, slot `216c6f0`, contains odd Thumb pointer `c51477` (entry G `c51476`). That callback checks modal count at most 1, weak-locks the captured owner and calls `EnableAutoProgress(1)`. It has **no marker/cancellation-state recheck**. Therefore a press that removed MissionAutoPlay before this pending task fires can be undone by the delayed arm while the popup remains alive. The shown false branch does not cancel that task. A future live test must establish the delayed arm has run or the captured popup owner has ceased to be reachable before claiming durable cancellation. No such counter-test is established here.

The countdown callable is separately located at primary `216c558`, invoke slot `216c570`, odd pointer `c50cbd` (entry G `c50cbc`). It requires a matching **auto_next** event and weak owner, then fires event pool `+430` and virtual slot `+4c`. It does not itself issue a reward request. These exact bodies and registrations are in `analysis/ghidra-campaign-result-enable-callback.txt`, `analysis/ghidra-campaign-result-enabler-registration.txt`, `analysis/ghidra-campaign-result-delay-helper.txt`, `analysis/ghidra-campaign-result-countdown-callback.txt` and the associated memory/key exports.

WIN `OnProcessPopUpBackKey` at G `c491e2` also disables automatic progress first. If `CMMotion::IsEnd(this+670)` equals 1, it additionally fires event pool `this+430` and calls virtual slot `+4c`. Therefore Back is not proven to be a cancellation-only input after the result animation ends. Its navigation destination needs the event registrations and virtual mapping.

WIN `StopAutoPlay` at G `c498a4` only hides **PA_AUTO_FADE** and calls `SRStopMotion` with **auto_next** for both motion strings. No marker removal appears in this body. Base `CSRPopUpGameResult::StopAutoPlay` at G `c41c58` delegates to it. Do not substitute these methods for `EnableAutoProgress(0)` in a marker-removal claim.

## Button dispatch identities

`CSRPopUpGameResultWin::OnButtonClick` G `c4911c` first checks modal ownership when modal count exceeds 1, then compares the button hash at `+268` and requires high word `+26c` equal 0:

- **BT_HOME**, CRC32 `05a397ad`, fires pool `this+3dc`.
- Hash `8a91c99a` fires pool `this+3f8`. **BT_REPLAY** has that standard CRC32, but no exact BT_REPLAY string was found in the searched native string corpus; retain this name as a candidate.
- **BT_OK** `5171c69e`, **BT_X_BT** `a4b45f7f`, and **BT_NEXT** `705a8b41` all fire pool `this+430`.

The exact BT_HOME/BT_OK/BT_X_BT/BT_NEXT names occur in `analysis/native-all-strings.tsv` and their standard zlib CRC32 values match the comparisons. This is a hash correspondence, not a pixel-position or destination proof. The event registrations still determine Home/replay/close consequences.

## Validation boundary

No live WIN frame or cancellation was validated here. Input must be conditional on a freshly verified WIN result, not a battle HUD, cut-in, partial result animation or preparation screen. Active battle requires prompt ordinary attacks under the user instruction; this cancellation contract does not authorize an active-battle exit control. A future result-only touch must verify normal dispatch, that the pending delayed arm cannot re-enable continuation, and that the marker/countdown stopped before allowing another input or interpreting safe map return. Source closure alone does not retrospectively attribute the unobserved campaign progression in §199.
